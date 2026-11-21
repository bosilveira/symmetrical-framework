#!/usr/bin/env python3
"""Symbolic checks for Sym^2 cone sections, mixed Hessians and catenoid Jacobi modes.

Run: python mathematics/_standards/verify_sym2_hessian.py
Requires: sympy, mpmath. Tests complement the proofs; they do not
establish novel results or automatically validate external correspondences.
"""
from __future__ import annotations

import sympy as sp
import mpmath as mp


def check(label: str, expr) -> None:
    value = sp.trigsimp(sp.simplify(expr))
    if value != 0:
        value = sp.trigsimp(sp.simplify(value.rewrite(sp.exp)))
    if value != 0:
        raise AssertionError((label, value))
    print("PASS:", label)


def main() -> None:
    theta, u, r, phi, t = sp.symbols("theta u r phi t", real=True)
    S, W = sp.sech(theta), sp.tanh(theta)
    R, b = sp.cosh(theta), sp.sinh(theta)
    H = S**2
    eta = sp.atan(sp.sinh(theta))
    P = (1 + W) / 2

    # The Sym^2 null cone and its plane sections.
    y1, y2, y3 = sp.exp(theta), sp.Integer(1), sp.exp(-theta)
    check("Sym^2 null cone", y1 * y3 - y2**2)
    X, Y, Z = (y1 + y3)/2, (y1 - y3)/2, y2
    check("hyperbolic plane chart", X-R)
    check("hyperbolic chart second component", Y-b)
    check("circle projective normalization", (Y/X)**2 + (Z/X)**2-1)
    check("null-plane parabola with t coordinate", (1 + t)/2 *
          (1 - (1 + t)/2) * 4 - (1 - t*t))
    check("canonical power profile parabola", H - 4*P*(1-P))
    check("half-angle projective map",
          ((sp.exp(theta)-1)/(sp.exp(theta)+1) -
           sp.tanh(theta/2)).rewrite(sp.exp))
    check("Gudermannian half-angle",
          sp.tan(eta/2)-sp.tanh(theta/2))
    # Last result needs real trig simplification / half angle.
    fields = {"S":S, "W":W, "R":R, "b":b, "H":H, "P":P, "eta":eta}
    specific = {
        "S":-H*W**2 + 2*theta*H*W*(2*W**2-1),
        "W":H**2*(4*theta*W-1),
        "R":-b*b-2*theta*b*R,
        "b":-R*R-2*theta*b*R,
        "H":-4*H*H*W*W+8*theta*H*H*W*(2-3*H),
        "P":H**2*(4*theta*W-1)/4,
        "eta":H*(2*theta*W-1),
    }
    for name, func in fields.items():
        a = sp.diff(func, theta)
        d = sp.diff(func, theta, 2)
        f_ur = sp.diff(func.subs(theta,u*r),u,r)
        check(name+" mixed", f_ur-(a+theta*d).subs(theta,u*r))
        hess = sp.hessian(func.subs(theta,u*r),(u,r))
        check(name+" determinant general",
              hess.det()-(-a*a-2*theta*a*d).subs(theta,u*r))
        check(name+" determinant field",
              hess.det()-specific[name].subs(theta,u*r))

    # Lorentz null coordinates, Riccati, fixed catenoid Jacobi modes.
    check("R Riccati", sp.diff(r*W,theta)*r+(r*W)**2-r*r)
    check("S logarithmic derivative sign",sp.diff(S,theta)/S+W)
    check("catenoid Jacobi azimuthal mode n=0",
          sp.diff(W,theta,2)+2*H*W)
    check("catenoid Jacobi azimuthal mode n=1",
          sp.diff(S,theta,2)+(2*H-1)*S)
    N = sp.Matrix([S*sp.cos(phi), S*sp.sin(phi), -W])
    check("Gauss normal unit length", N.dot(N)-1)
    check("Gauss meridian squared speed",
          sp.diff(N,theta).dot(sp.diff(N,theta))-H)
    check("Gudermannian arclength", sp.diff(eta,theta)-S)

    # Specific ZIP Milne carrier normalization: rho^2 = 2 cosh(r u), |Wr| = r.
    check("Milne-vs-Gudermannian factor two",
          r / (2*R) - r*S/2)
    mp.mp.dps = 30
    for target, expected in [
        (mp.mpf("0.25"), mp.mpf("0.521813447795768604")),
        (mp.mpf("0.5"), mp.mpf("0.771702319209104224"))
    ]:
        root = mp.findroot(lambda z: z*mp.tanh(z)-target, mp.mpf("0.6"))
        assert abs(root-expected) < mp.mpf("1e-17")
        print("PASS: threshold theta*tanh(theta) =", target, "->", root)
    print("ALL SELECTED SYM^2 / HESSIAN CHECKS PASSED")


if __name__ == "__main__":
    main()
