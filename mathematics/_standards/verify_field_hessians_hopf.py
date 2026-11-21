#!/usr/bin/env python3
"""Symbolic checks: conic-field parameter Hessians and selected Hopf–Villarceau identities.

Run: python mathematics/_standards/verify_field_hessians_hopf.py
Requires: sympy. A check of a displayed identity is not independent proof
of all topological, spectral, bibliographic, or global geometric claims.
"""
import sympy as sp


def zero(label, expr):
    expr = sp.trigsimp(sp.simplify(expr))
    if expr != 0:
        expr = sp.simplify(sp.trigsimp(expr.rewrite(sp.exp)))
    if expr != 0:
        raise AssertionError((label, expr))
    print("PASS:", label)


def verify_hessians():
    x, c, r = sp.symbols("x c r", positive=True, real=True)
    t = sp.symbols("t", real=True)
    u = sp.log(x/c)
    theta = r*u
    S = sp.sech(t)
    W = sp.tanh(t)
    F = {
        "S": S,
        "W": W,
        "R": sp.cosh(t),
        "b": sp.sinh(t),
        "P": (1+W)/2,
        "H": S**2,
        "eta": sp.atan(sp.sinh(t)),
        "T": sp.exp(t),
    }
    for name, phi in F.items():
        f = phi.subs(t, theta)
        a = sp.diff(phi, t).subs(t, theta)
        d = sp.diff(phi, t, 2).subs(t, theta)
        expected = {
            "xx": (r*r*d-r*a)/x**2,
            "xc": -r*r*d/(x*c),
            "xr": (a+r*u*d)/x,
            "cc": (r*r*d+r*a)/c**2,
            "cr": -(a+r*u*d)/c,
            "rr": u*u*d,
        }
        for indices, rhs in expected.items():
            zero(name + "_" + indices, sp.diff(f, *indices)-rhs)
    s = sp.sech(theta)
    w = sp.tanh(theta)
    f = s/(2*x)
    zero("kernel f_rr", sp.diff(f,r,2)-u*u*f*(2*w*w-1))
    zero("kernel f_cc", sp.diff(f,c,2)-f*(r*r*(2*w*w-1)-r*w)/c**2)
    zero("kernel f_rc", sp.diff(f,r,c)-f*(w+r*u*(1-2*w*w))/c)
    q0=r*w
    H=s*s
    zero("log-slope q0_rr", sp.diff(q0,r,2)-(2*u*H-2*r*u*u*H*w))
    zero("log-slope q0_cc", sp.diff(q0,c,2)-(r*r*H-2*r**3*H*w)/c**2)
    zero("log-slope q0_rc", sp.diff(q0,r,c)-(-2*r*H+2*r*r*u*H*w)/c)


def verify_hopf():
    eta, alpha, beta, delta, v = sp.symbols("eta alpha beta delta v", real=True)
    S, W = sp.cos(eta), sp.sin(eta)
    R, b = 1/S, W/S
    n = sp.Matrix([sp.sin(2*eta)*sp.cos(delta),
                   sp.sin(2*eta)*sp.sin(delta), sp.cos(2*eta)])
    for j, val in enumerate(sp.diff(n,eta,2)+4*n):
        zero("Hopf base harmonic " + str(j), val)
    den=1-W*sp.sin(beta)
    X=S*sp.cos(alpha)/den
    Y=S*sp.sin(alpha)/den
    Z=W*sp.cos(beta)/den
    rho=S/den
    zero("stereographic ring torus",
         (rho-R)**2+Z**2-b**2)
    xv=X.subs({alpha:v,beta:v+delta})
    yv=Y.subs({alpha:v,beta:v+delta})
    zv=Z.subs({alpha:v,beta:v+delta})
    zero("Villarceau plane", zv-b*(xv*sp.cos(delta)-yv*sp.sin(delta)))
    zero("Villarceau radius", (xv-b*sp.sin(delta))**2
         +(yv-b*sp.cos(delta))**2+zv**2-R**2)


if __name__ == "__main__":
    verify_hessians()
    verify_hopf()
    print("ALL TARGETED SECOND-DERIVATIVE AND HOPF CHECKS PASSED")
