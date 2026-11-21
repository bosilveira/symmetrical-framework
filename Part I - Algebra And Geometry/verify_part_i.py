#!/usr/bin/env python3
"""Representative exact and numerical checks for Part I of Symmetrical Framework.

Run with: python "Part I - Algebra And Geometry/verify_part_i.py"
Dependencies: sympy, mpmath.
A passing run does not constitute a formal proof of every chapter claim.
"""
import math
import sympy as sp
import mpmath as mp

r, t, x, c = sp.symbols("r t x c", positive=True, finite=True)
S = 2*t/(1+t**2)
W = (t**2-1)/(t**2+1)

def D(expr):
    """Euler derivative with fixed x-prefactor, t=(x/c)**r."""
    return sp.factor(r*t*sp.diff(expr, t))

def exact_zero(expr, label):
    result = sp.factor(sp.together(expr))
    assert result == 0, (label, result)

f = S/(2*x)
Df = (D(S)-S)/(2*x)
D2f = (D(D(S))-2*D(S)+S)/(2*x)
fx = sp.factor(Df/x)
fxx = sp.factor((D2f-Df)/x**2)

exact_zero(S**2+W**2-1, "unit circle")
exact_zero(D(S)+r*S*W, "sech flow")
exact_zero(D(W)-r*S**2, "tanh flow")
exact_zero(D(W)/x-4*r*x*f**2, "half density")
exact_zero(x*fx+f+r*W*f, "Euler equation")
exact_zero((x*fx+f)**2-r**2*f**2*(1-4*x**2*f**2), "first order")
exact_zero(x**2*fxx+3*x*fx+(1-r**2)*f+8*r**2*x**2*f**3, "second order")
exact_zero(fxx-S*(2-r**2+3*r*W+2*r**2*W**2)/(2*x**3),
           "second derivative")
exact_zero(S.subs(t, 1/t)-S, "log parity")

# Schwarzian of W(x) via the Euler derivative D, without branch assumptions.
wx = D(W)/x
wxx = (D(D(W))-D(W))/x**2
wxxx = (D(D(D(W)))-3*D(D(W))+2*D(W))/x**3
schwarz = sp.together(wxxx/wx-sp.Rational(3,2)*(wxx/wx)**2)
exact_zero(schwarz-(1-4*r**2)/(2*x**2), "Schwarzian")

# Inflection polynomial in z=t**2 and exact discriminant.
z = sp.symbols("z")
Q = 2*r**2*W**2+3*r*W+2-r**2
qpol = sp.factor(sp.together(Q*(1+t**2)**2))
target = (r+1)*(r+2)*z**2+(4-6*r**2)*z+(r-1)*(r-2)
terms = sp.Poly(sp.expand(qpol), t).terms()
assert all(exponents[0] % 2 == 0 for exponents, coefficient in terms)
qpol_z = sum(coefficient*z**(exponents[0]//2)
             for exponents, coefficient in terms)
exact_zero(qpol_z-target, "inflection polynomial")
exact_zero(sp.discriminant(target,z)-4*r**2*(8*r**2-7),
           "inflection discriminant")

# The dimensionless r=1 graph-length curve is a genus-two quintic.
P = (1+z)**4+4*z
assert sp.degree(z*P, z) == 5
assert sp.discriminant(P,z) == -23296
assert sp.gcd(z*P,sp.diff(z*P,z)) == 1

# Weighted-square norm, exactly.
a = sp.symbols("a", positive=True)
assert sp.simplify(sp.integrate(a/(1+a**2)**2,(a,0,sp.oo))/r
                   -1/(2*r)) == 0

# Numerical checks of disk volume and area integrability at r=1.
mp.mp.dps = 40
def fnum(xx, rr=1, cc=1):
    return cc**rr*xx**(rr-1)/(cc**(2*rr)+xx**(2*rr))
def fdnum(xx, rr=1, cc=1):
    return (cc**rr*xx**(rr-2)
            *((rr-1)*cc**(2*rr)-(rr+1)*xx**(2*rr))
            /(cc**(2*rr)+xx**(2*rr))**2)

for rr in [mp.mpf(1),mp.mpf("1.5"),mp.mpf(2),mp.mpf(3)]:
    volume = mp.pi*mp.quad(lambda v:fnum(v,rr)**2,[0,1,mp.inf])
    expected = mp.pi**2/(4*rr**2*mp.sin(mp.pi/(2*rr)))
    assert mp.almosteq(volume,expected,rel_eps=mp.mpf("1e-24")), rr

area_r1 = 2*mp.pi*mp.quad(
    lambda v:fnum(v)*mp.sqrt(1+fdnum(v)**2),
    [0,1,mp.inf])
assert 0 < area_r1 < mp.inf

print("All representative Part I checks passed.")
print("r=1 surface area (fixed numerical axes):",mp.nstr(area_r1,15))
