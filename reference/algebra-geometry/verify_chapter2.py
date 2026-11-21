#!/usr/bin/env python3
"""Representative Chapter 2 exact and numerical checks.

Run: python "Part I - Algebra And Geometry/verify_chapter2.py"
Dependencies: sympy, mpmath. Tests do not replace mathematical proofs.
"""
from pathlib import Path
import mpmath as mp
import sympy as sp

r, t, x, c = sp.symbols("r t x c", positive=True, real=True)
S = 2*t/(1+t**2)
W = (t**2-1)/(1+t**2)
f = S/(2*x)

def D(expr):
    return sp.factor(r*t*sp.diff(expr,t))

def zero(expr, label):
    result = sp.simplify(sp.factor(sp.together(expr)))
    assert result == 0, (label,result)

fx = (D(S)-S)/(2*x**2)
fxx = (D(D(S))-3*D(S)+2*S)/(2*x**3)
fxxx = (D(D(D(S)))-6*D(D(S))+11*D(S)-6*S)/(2*x**4)
zero(f.subs({x:c,t:1})-1/(2*c),"center value")
zero(fx.subs({x:c,t:1})+1/(2*c**2),"center slope")
zero(fxx.subs({x:c,t:1})-(2-r**2)/(2*c**3),"center second jet")
zero(fxxx.subs({x:c,t:1})-3*(r**2-1)/c**4,"center third jet")
inverted = S.subs(t,1/t)/(2*(c**2/x))
zero(inverted-(x**2/c**2)*f,"inversion weight two")
zero((D(S)-S)/(2*x)+(1+r*W)*f,"Euler x derivative")
zero(D(S)+r*S*W,"log profile derivative")
zero(D(W)-r*(1-W**2),"phase Riccati")
zero(D(W)/x-4*r*x*f**2,"spatial density relation")

u,k=sp.symbols("u k",real=True)
Q=r*sp.tanh(r*u)
V_minus=r**2-2*r**2*sp.sech(r*u)**2
zero(Q**2-sp.diff(Q,u)-V_minus,"Darboux minus")
zero(Q**2+sp.diff(Q,u)-r**2,"Darboux plus")
psi=(-sp.I*k+Q)*sp.exp(sp.I*k*u)
zero(-sp.diff(psi,u,2)+V_minus*psi-(r**2+k**2)*psi,
     "Darboux scattering intertwiner")

mp.mp.dps=35
TOL=mp.mpf("1e-23")
def close(a,b,label):
    assert mp.almosteq(a,b,rel_eps=TOL,abs_eps=TOL), (
        label,mp.nstr(a,18),mp.nstr(b,18))

def rho(xx,rr,cc):
    return 2*rr/mp.pi*cc**rr*xx**(rr-1)/(cc**(2*rr)+xx**(2*rr))

for rr,cc,aa,dd in [
    (mp.mpf("1.7"),mp.mpf("2"),mp.mpf("2.3"),mp.mpf("3.5")),
    (mp.mpf("0.9"),mp.mpf("4"),mp.mpf("-1.6"),mp.mpf("1.2")),
    (mp.mpf("2.7"),mp.mpf("1.5"),mp.mpf("-1"),mp.mpf("4")),
]:
    for yy in [mp.mpf("0.3"),mp.mpf("1"),mp.mpf("5")]:
        xx=cc*(yy/dd)**(1/aa)
        jac=abs(xx/(aa*yy))
        close(rho(xx,rr,cc)*jac,rho(yy,rr/abs(aa),dd),
              "nonzero-power family closure")

for rr,c1,c2 in [
    (mp.mpf("1.4"),mp.mpf("1"),mp.mpf("4")),
    (mp.mpf("0.8"),mp.mpf("2"),mp.mpf("2")),
    (mp.mpf("3.4"),mp.mpf("5"),mp.mpf("0.7")),
]:
    center=mp.log(mp.sqrt(c1*c2))
    delta=rr*mp.log(c2/c1)
    integrand=lambda v: 1/(4*mp.cosh(rr*(v-mp.log(c1)))*
                           mp.cosh(rr*(v-mp.log(c2))))
    left=mp.quad(integrand,[-mp.inf,center])
    right=mp.quad(integrand,[center,mp.inf])
    expected=(delta/(2*rr*mp.sinh(delta)) if delta else 1/(2*rr))
    close(left+right,expected,"weighted overlap")
    close(left,right,"two-scale half split")

K=lambda d: d/mp.sinh(d) if d else mp.mpf(1)
for omega in [mp.mpf("0"),mp.mpf("0.7"),mp.mpf("2")]:
    transform=2*mp.quad(lambda d: K(d)*mp.cos(omega*d),[0,1,mp.inf])
    target=(mp.pi**2/2)/mp.cosh(mp.pi*omega/2)**2
    close(transform,target,"overlap Fourier transform")

pdf=lambda v: 1/(mp.pi*mp.cosh(v))
moments=[
    (lambda v: mp.tanh(v)**2,mp.mpf("0.5")),
    (lambda v: v*mp.tanh(v),mp.mpf(1)),
    (lambda v: v**2,mp.pi**2/4),
    (lambda v: v**2/mp.cosh(v)**2,mp.pi**2/8-1),
    (lambda v: (1-v*mp.tanh(v))**2,mp.pi**2/8),
    (lambda v: mp.tanh(v)*(1-v*mp.tanh(v)),mp.mpf(0)),
]
for i,(g,target) in enumerate(moments):
    actual=mp.quad(lambda v: pdf(v)*g(v),[-mp.inf,0,mp.inf])
    close(actual,target,"Fisher moment "+str(i))

RR,CC=mp.mpf("1.7"),mp.mpf("2.4")
F=lambda xx: 2/mp.pi*mp.atan((xx/CC)**RR)
phase=lambda xx: mp.tanh(RR*mp.log(xx/CC))
P=lambda xx: (1+phase(xx))/2
for x1,x2 in [(mp.mpf("0.6"),mp.mpf("1.5")),
              (mp.mpf("3.2"),mp.mpf("6.4"))]:
    star=x1*x2/CC
    close(phase(star),
          (phase(x1)+phase(x2))/(1+phase(x1)*phase(x2)),
          "tanh multiplication group")
    P1,P2=P(x1),P(x2)
    close(P(star),P1*P2/(P1*P2+(1-P1)*(1-P2)),
          "logistic multiplication group")
    tangent=lambda v: mp.tan(mp.pi*v/2)
    close(F(star),2/mp.pi*mp.atan(tangent(F(x1))*tangent(F(x2))),
          "CDF multiplication group")
low1,low2=mp.mpf("0.6"),mp.mpf("1.2")
assert low1*low2<CC**2
local_x=((low1**RR+low2**RR)/(1-(low1*low2/CC**2)**RR))**(1/RR)
close(F(local_x),F(low1)+F(low2),"restricted CDF addition")

chapter=Path(__file__).resolve().parent/"02-foundational-symmetries"
assert not (chapter/"02-gemini.md").exists(), "Gemini source should have been consolidated and removed"
fence=chr(96)*3
for file in chapter.glob("02-*.md"):
    raw=file.read_text(encoding="utf-8")
    assert "\\operatorname{" not in raw, file
    assert "\\boxed" not in raw and "$$" not in raw, file
    lines=raw.splitlines()
    for i,line in enumerate(lines):
        if line.startswith(fence+"math"):
            assert line==fence+"math",(file,i)
            assert i>=2 and lines[i-1]=="" and lines[i-2]!="",(file,i)
            assert i+4<len(lines) and lines[i+2]==fence,(file,i)
            assert lines[i+3]=="" and lines[i+4]!="",(file,i)
        assert not (line.startswith(" ") and line.lstrip().startswith(fence)),file

print("Chapter 2 verification passed: symbolic, numerical and Markdown checks.")
