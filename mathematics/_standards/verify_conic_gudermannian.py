#!/usr/bin/env python3
"""Verify foundational conics, two derivative clocks, parabolic invariant and measures.

This is finite independent symbolic/numerical testing, NOT proof of every global
or algebraic-geometric assertion in the associated chapters.

Run: python mathematics/_standards/verify_conic_gudermannian.py
Requires: sympy, mpmath.
"""
from __future__ import annotations

import mpmath as mp
import sympy as s


def exact(label: str, lhs, rhs=0) -> None:
    diff = s.trigsimp(s.simplify((lhs - rhs).rewrite(s.exp)))
    if diff != 0:
        diff = s.simplify(s.trigsimp(lhs - rhs))
    if diff != 0:
        raise AssertionError((label, diff))
    print("PASS:", label)


def run() -> None:
    u, r, c, x = s.symbols("u r c x", positive=True, real=True)
    A, B_gram, C_gram = s.symbols("A B_gram C_gram", positive=True, real=True)
    theta = r*u
    S = s.sech(theta)
    W = s.tanh(theta)
    R = s.cosh(theta)
    b = s.sinh(theta)
    P = (1+W)/2
    B_sq = S**2
    eta = s.atan(s.sinh(theta))
    Du = lambda expr: s.diff(expr,u)
    Deta = lambda expr: s.diff(expr,u)/(r*S)

    exact("circle", S**2 + W**2, 1)
    exact("hyperbola", R**2 - b**2, 1)
    exact("parabola Bsq=4P(1-P)", B_sq, 4*P*(1-P))
    exact("dS/du", Du(S), -r*S*W)
    exact("dW/du", Du(W), r*S**2)
    exact("dR/du", Du(R), r*b)
    exact("db/du", Du(b), r*R)
    exact("dP/du", Du(P), r*B_sq/2)
    exact("dBsq/du", Du(B_sq), -2*r*B_sq*W)
    exact("d2S/du2", Du(Du(S)), r**2*S-2*r**2*S**3)
    exact("d2W/du2", Du(Du(W)), -2*r**2*W+2*r**2*W**3)
    exact("d2R/du2", Du(Du(R)), r**2*R)
    exact("d2b/du2", Du(Du(b)), r**2*b)
    exact("d2P/du2", Du(Du(P)), 4*r**2*P*(1-P)*(1-2*P))
    exact("d2Bsq/du2", Du(Du(B_sq)), 4*r**2*B_sq-6*r**2*B_sq**2)
    exact("eta_u=rS", Du(eta), r*S)
    exact("circle u clock speed", Du(S)**2 + Du(W)**2, r*r*S*S)
    exact("hyperbola Minkowski speed", Du(b)**2-Du(R)**2, r*r)
    exact("circle eta harmonic S", Deta(Deta(S)), -S)
    exact("circle eta harmonic W", Deta(Deta(W)), -W)
    exact("hyperbola eta cubic R", Deta(Deta(R)), 2*R**3-R)
    exact("hyperbola eta cubic b", Deta(Deta(b)), 2*b**3+2*b)
    exact("parabola eta harmonic P", Deta(Deta(P)), s.Rational(1,2)-P)
    exact("parabola eta harmonic Bsq", Deta(Deta(B_sq)), 2-4*B_sq)
    exact("eta pendulum", Du(Du(eta)), -r**2*s.sin(2*eta)/2)
    exact("Gudermannian trigonometric b", s.tan(eta), b)
    exact("Gudermannian trigonometric R", 1/s.cos(eta), R)

    # One projective conic, homogeneous rational parameter
    T = s.symbols("T", positive=True, real=True)
    X = 1+T**2
    Y = T**2-1
    Z = 2*T
    exact("common homogeneous projective conic", X**2, Y**2+Z**2)
    P_h = X*(X+Y)/2
    B_h = Z**2
    Z_h = X**2
    exact("quadratic map to homogeneous parabola",
          B_h*Z_h, 4*P_h*(Z_h-P_h))

    # The free polynomial first-order flow has a first integral K.
    p, Bfield = s.symbols("p Bfield", real=True)
    p_u = r*Bfield/2
    B_u = 2*r*Bfield*(1-2*p)
    evolve = lambda z: s.diff(z,p)*p_u+s.diff(z,Bfield)*B_u
    K = Bfield - 4*p*(1-p)
    exact("parabolic flow invariant K", evolve(K), 0)
    exact("off-leaf P second-order", evolve(p_u),
          r**2*(4*p*(1-p)+K)*(1-2*p))
    exact("off-leaf B second-order", evolve(B_u),
          4*r**2*(1+K)*Bfield-6*r**2*Bfield**2)

    # Parameter derivatives: distinguish field B_sq from constant coefficient B_gram.
    J0 = A*s.exp(theta)+B_gram*s.exp(-theta)
    JG = J0+2*C_gram
    exact("J0 homogeneous", Du(Du(J0)), r**2*J0)
    exact("Gram shifted JG", Du(Du(JG)), r**2*(JG-2*C_gram))
    u_xc = s.log(x/c)
    sq_xc = s.sech(r*u_xc)**2
    w_xc = s.tanh(r*u_xc)
    exact("Bsq parameter derivative r at fixed x,c",
          s.diff(sq_xc,r), -2*u_xc*sq_xc*w_xc)
    exact("Bsq parameter derivative c at fixed x,r",
          s.diff(sq_xc,c), 2*r*sq_xc*w_xc/c)
    exact("Gram B constant under u derivative", Du(B_gram), 0)

    # Norm, original-kernel measure, uniform eta and squared-profile beta measures.
    mp.mp.dps = 35
    for q in [mp.mpf("0.7"),1,2,3,mp.mpf("3.3")]:
        beta = mp.beta(mp.mpf("0.5"),q)
        norm = mp.quad(lambda t: mp.sech(t)**(2*q),[-mp.inf,0,mp.inf])
        assert abs(norm-beta) < mp.mpf("1e-29"), ("beta norm", q)
        for z in [mp.mpf("-0.9"),0,mp.mpf("1.1")]:
            p0 = (1+mp.tanh(z))/2
            CDF = lambda qq:mp.betainc(qq,qq,0,p0,regularized=True)
            rec = CDF(q)+mp.tanh(z)*mp.sech(z)**(2*q)/(2*q*beta)
            assert abs(rec-CDF(q+1))<mp.mpf("1e-29"), ("beta recurrence",q,z)
        print("PASS: beta normalization / cumulative recurrence q =",q)

    angle_mass=mp.quad(lambda eta:1/mp.pi,[-mp.pi/2,mp.pi/2])
    assert abs(angle_mass-1)<mp.mpf("1e-32")
    expected=mp.quad(lambda w:1/(mp.pi*mp.sqrt(1-w*w)),[-1,0,1])
    assert abs(expected-1)<mp.mpf("1e-16")
    print("PASS: original kernel -> uniform eta -> arcsine W")
    print("ALL SELECTED CONIC / GUDERMANNIAN CHECKS PASSED")


if __name__ == "__main__":
    run()
