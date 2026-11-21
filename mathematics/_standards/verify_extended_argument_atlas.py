#!/usr/bin/env python3
"""Targeted exact checks for §00.12: product/reciprocal logarithms and Wick maps.

Run from repo root:
    python mathematics/_standards/verify_extended_argument_atlas.py

Requires sympy. These checks test displayed formulas and selected branches;
they do not prove global norm equivalence or a geometric dimensional lift.
"""
from __future__ import annotations

import sympy as sp


def zero(label: str, expression) -> None:
    s = sp.simplify(sp.trigsimp(expression))
    if s != 0:
        s = sp.simplify(s.rewrite(sp.exp))
    if s != 0:
        raise AssertionError(f"{label}: {s}")
    print("PASS:", label)


def schwarzian(z, x):
    return sp.diff(z, x, 3) / sp.diff(z, x) - sp.Rational(3, 2) * (
        sp.diff(z, x, 2) / sp.diff(z, x)
    ) ** 2


def main() -> None:
    x, c, r, ell = sp.symbols("x c r ell", positive=True, real=True)
    u, v = sp.log(x / c), sp.log(x*c / ell**2)
    args = {
        "ratio": r*u,
        "product": r*v,
        "ratio reciprocal r/u": r/u,
        "ratio inverse 1/(ru)": 1/(r*u),
        "product reciprocal r/v": r/v,
        "product inverse 1/(rv)": 1/(r*v),
    }
    partials = {
        "ratio": (r/x, -r/c, u),
        "product": (r/x, r/c, v),
        "ratio reciprocal r/u": (-r/(x*u**2), r/(c*u**2), 1/u),
        "ratio inverse 1/(ru)": (
            -1/(r*x*u**2), 1/(r*c*u**2), -1/(r**2*u)),
        "product reciprocal r/v": (-r/(x*v**2), -r/(c*v**2), 1/v),
        "product inverse 1/(rv)": (
            -1/(r*x*v**2), -1/(r*c*v**2), -1/(r**2*v)),
    }
    for name, z in args.items():
        for q, result, variable in zip(
            ("x", "c", "r"), partials[name], (x, c, r)
        ):
            zero(name+" derivative "+q, sp.diff(z, variable)-result)
        zero(name+" Schwarzian", schwarzian(z,x)-1/(2*x**2))
    zero("reflected center", v-sp.log(x/(ell**2/c)))
    zero("ratio reciprocal x log slope",
         sp.diff(args["ratio reciprocal r/u"],x,2)
         / sp.diff(args["ratio reciprocal r/u"],x)
         + (u+2)/(x*u))

    z = args["ratio reciprocal r/u"]
    y = sp.sech(z)
    zx = sp.diff(z, x)
    zero("reciprocal sech x ODE",
         sp.diff(y,x,2)-sp.diff(z,x,2)/zx*sp.diff(y,x)
         -zx**2*(y-2*y**3))
    yy = sp.sech(r/u)
    zero("reciprocal sech u ODE",
         sp.diff(yy,u,2)+2*sp.diff(yy,u)/u
         -r**2/u**4*(yy-2*yy**3))
    q = sp.diff(sp.log(sp.cosh(z)),x)
    zero("reciprocal cosh Riccati pullback",
         sp.diff(q,x)+q**2-sp.diff(z,x,2)/zx*q-zx**2)

    tt = sp.symbols("t", real=True)
    zero("sinh Wick", sp.sinh(sp.I*tt)-sp.I*sp.sin(tt))
    zero("cosh Wick", sp.cosh(sp.I*tt)-sp.cos(tt))
    zero("tanh Wick", sp.tanh(sp.I*tt)-sp.I*sp.tan(tt))
    zero("sech Wick", sp.sech(sp.I*tt)-sp.sec(tt))
    zero("coth Wick", sp.coth(sp.I*tt)+sp.I*sp.cot(tt))
    zero("csch Wick", sp.csch(sp.I*tt)+sp.I*sp.csc(tt))
    for val in (sp.Rational(1,4), sp.Rational(3,5), -sp.Rational(2,3)):
        expr = sp.atan(sp.sinh(sp.I*val)) - sp.I*sp.asinh(sp.tan(val))
        if abs(complex(sp.N(expr,30))) > 1e-25:
            raise AssertionError(("Gudermannian branch", val))
    print("PASS: Gudermannian Wick branch samples")
    print("ALL TARGETED EXTENDED-ARGUMENT CHECKS PASSED")


if __name__=="__main__":
    main()
