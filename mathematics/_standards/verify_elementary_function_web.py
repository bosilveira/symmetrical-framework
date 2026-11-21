#!/usr/bin/env python3
"""Reproducible finite checks for the typed elementary-function transformation web.

Run: python mathematics/_standards/verify_elementary_function_web.py
Requires: sympy and mpmath. A check is not a universal proof or an independent
verification of geometry beyond the particular specified equations.
"""
from __future__ import annotations

import sympy as sp
import mpmath as mp


def exact(label: str, left, right=0) -> None:
    diff = sp.simplify(sp.trigsimp(left - right))
    if diff != 0:
        diff = sp.simplify(sp.expand_trig(diff.rewrite(sp.exp)))
    if diff != 0:
        raise AssertionError((label, diff))
    print("PASS:", label)


def symbolic_checks() -> None:
    theta = sp.symbols("theta", positive=True, real=True)
    t = sp.exp(theta)
    s, w = sp.sech(theta), sp.tanh(theta)
    R, b = sp.cosh(theta), sp.sinh(theta)
    eta = sp.atan(b)
    i = sp.I

    for label, lhs, rhs in [
        ("tanh = sin gd", sp.sin(eta), w),
        ("sech = cos gd", sp.cos(eta), s),
        ("sinh = tan gd", sp.tan(eta), b),
        ("cosh = sec gd", 1/sp.cos(eta), R),
        ("coth = csc gd", 1/sp.sin(eta), 1/w),
        ("csch = cot gd", 1/sp.tan(eta), 1/b),
        ("Cayley complex circle", s+i*w, -i*(1+i*t)/(1-i*t)),
        ("complex log derivative", sp.diff(s+i*w,theta)/(s+i*w), i*s),
        ("Gudermannian arclength", sp.diff(eta,theta), s),
        ("Gudermannian half-angle", sp.sin(eta)/(1+sp.cos(eta)),
         sp.sinh(theta)/(sp.cosh(theta)+1)),
        ("projective half angle", sp.tanh(theta/2), (t-1)/(t+1)),
    ]:
        exact(label, lhs, rhs)

    # x > c, theta > 0: amplitude-swap involution.
    dual_t = (t+1)/(t-1)
    for label, lhs, rhs in [
        ("dual involution", (dual_t+1)/(dual_t-1), t),
        ("dual S = original W", 2*dual_t/(dual_t**2+1), w),
        ("dual W = original S", (dual_t**2-1)/(dual_t**2+1), s),
        ("dual sinh = reciprocal b", (dual_t-1/dual_t)/2, 1/b),
        ("dual cosh = R/b", (dual_t+1/dual_t)/2, R/b),
        ("dual derivative", sp.diff(sp.log(dual_t),theta), -1/b),
    ]:
        exact(label, lhs, rhs)

    for n in (2, 3, 4):
        exact(f"Chebyshev T_{n}", sp.cosh(n*theta), sp.chebyshevt(n,R))
        exact(f"Chebyshev U_{n-1}", sp.sinh(n*theta),
              b*sp.chebyshevu(n-1,R))
        even = sum(sp.binomial(n,j)*w**j for j in range(0,n+1,2))
        odd = sum(sp.binomial(n,j)*w**j for j in range(1,n+1,2))
        exact(f"tanh multiple {n}", sp.tanh(n*theta), odd/even)
        exact(f"sech multiple {n}", sp.sech(n*theta), s**n/even)

    # The regular dimension-indexed family at D = 1, 3, 5.
    Z1, Z3 = R, b/theta
    Z5 = 3*sp.diff(Z3,theta)/theta
    for D, Z in [(1,Z1),(3,Z3),(5,Z5)]:
        exact(f"Z_{D} radial ODE",
              sp.diff(Z,theta,2)+(D-1)*sp.diff(Z,theta)/theta-Z)
        L = sp.diff(Z,theta)/Z
        exact(f"Z_{D} log Riccati",
              sp.diff(L,theta)-(1-L**2-(D-1)*L/theta))
    exact("Langevin coth pole cancellation", sp.diff(Z3,theta)/Z3,
          sp.coth(theta)-1/theta)

    # Hopf connection and its local curvature; choose eta in (0, pi/2).
    v = sp.symbols("v", real=True)
    sw = sp.sin(v)
    cs = sp.cos(v)
    exact("Hopf curvature d(W^2) = 2SW d eta", sp.diff(sw**2,v),
          2*sw*cs)


def numerical_checks() -> None:
    mp.mp.dps = 30
    for rr, kk in [(mp.mpf("1.3"),mp.mpf("0.4")),
                   (mp.sqrt(mp.pi/2),mp.mpf("1.7"))]:
        left = mp.quad(lambda u:mp.sech(rr*u)*mp.cos(kk*u),
                       [-mp.inf,0,mp.inf])/mp.sqrt(2*mp.pi)
        right = mp.sqrt(mp.pi/2)*mp.sech(mp.pi*kk/(2*rr))/rr
        assert abs(left-right) < mp.mpf("1e-25"), ("unitary Fourier",rr,kk)
        print("PASS: unitary sech Fourier at", rr, kk)

    for rr in (mp.mpf("0.8"), mp.mpf("2.2")):
        energy = mp.quad(lambda u:rr**2*mp.sech(rr*u)**4,
                         [-mp.inf,0,mp.inf])
        assert abs(energy-4*rr/3) < mp.mpf("1e-25")
        print("PASS: topological tanh energy at",rr)

    hopf_mass = mp.quad(lambda v: mp.sin(2*v),[0,mp.pi/2])
    assert abs(hopf_mass-1) < mp.mpf("1e-25")
    print("PASS: Hopf base curvature integral with one half-chart")


if __name__=="__main__":
    symbolic_checks()
    numerical_checks()
    print("ALL TARGETED ELEMENTARY-WEB CHECKS PASSED")
