#!/usr/bin/env python3
"""Representative Chapter 3 symbolic and numerical checks.

Run: python "Part I - Algebra And Geometry/verify_chapter3.py"
Requires sympy and mpmath; not a substitute for mathematical proofs.
"""
import sympy as sp
import mpmath as mp

r,t,x,c,mu=sp.symbols("r t x c mu",positive=True,finite=True)
S=2*t/(1+t**2)
W=(t**2-1)/(1+t**2)
f=S/(2*sp.sqrt(mu)*x)

def D(expr):
    return sp.factor(r*t*sp.diff(expr,t))

def check(expr,label):
    result=sp.simplify(sp.factor(sp.together(expr)))
    assert result==0,(label,result)

y=S/sp.sqrt(mu)
yp=D(y)
ypp=D(yp)
energy=yp**2-r**2*y**2+mu*r**2*y**4
check(ypp-r**2*y+2*mu*r**2*y**3,"cubic Master")
check(energy,"separatrix zero energy")
fx=(D(S)-S)/(2*sp.sqrt(mu)*x**2)
fxx=(D(D(S))-3*D(S)+2*S)/(2*sp.sqrt(mu)*x**3)
check(x**2*fxx+3*x*fx+(1-r**2)*f+8*mu*r**2*x**2*f**3,
      "spatial nonlinear Master")
check((x*fx+f)**2-r**2*f**2*(1-4*mu*x**2*f**2),
      "zero-energy constraint")

# Euler polynomial recurrence, checked against the direct operator on f.
w=sp.symbols("w")
P=sp.Integer(1)
current=f
for n in range(6):
    check(current/f-P.subs(w,W),"Euler polynomial "+str(n))
    current=D(current)-current
    P=sp.expand(r*(1-w**2)*sp.diff(P,w)-(1+r*w)*P)

# Ordinary spatial derivative polynomials use a different falling factorial.
Q=sp.Integer(1)
current=f
for n in range(6):
    check(current/(f/x**n)-Q.subs(w,W),"ordinary polynomial "+str(n))
    current=(D(current)-(n+1)*current)/x
    Q=sp.expand(r*(1-w**2)*sp.diff(Q,w)-(n+1+r*w)*Q)

# Reciprocal, Pinney and arbitrary energy identities.
Y,yp0=sp.symbols("Y yp0",positive=True)
acc=r**2*Y-2*mu*r**2*Y**3
energy_general=yp0**2-r**2*Y**2+mu*r**2*Y**4
Jsecond=2*yp0**2/Y**3-acc/Y**2
check(Jsecond-r**2/Y-2*energy_general/Y**3,"reciprocal cubic defect")
rootsecond=sp.Rational(3,4)*yp0**2/Y**sp.Rational(5,2)-acc/(2*Y**sp.Rational(3,2))
check(rootsecond-r**2/(4*sp.sqrt(Y))-mu*r**2*Y**sp.Rational(3,2)/4
      -3*energy_general/(4*Y**sp.Rational(5,2)),
      "Pinney square-root defect")

u,A,B,C=sp.symbols("u A B C",real=True)
J=A*sp.exp(r*u)+2*B+C*sp.exp(-r*u)
check(2*J*sp.diff(J,u,2)-sp.diff(J,u)**2-r**2*J**2
      -4*r**2*(A*C-B**2),"Pinney envelope determinant")
check(sp.diff(J,u,2)-r**2*J+2*r**2*B,"Pinney intersection")

# Radial Kelvin covariance tested symbolically on an arbitrary power.
# The document contains a separate chain-rule proof for general smooth F.
a,power=sp.symbols("a power",positive=True)
radius=a**2/x
trial=radius**power
kelvin=a**2*trial/x**2
radial_laplacian=sp.diff(kelvin,x,2)+3*sp.diff(kelvin,x)/x
lap_at_radius=power*(power+2)*radius**(power-2)
check(radial_laplacian-a**6*lap_at_radius/x**6,"Kelvin radial Laplacian on powers")
check(kelvin/x**2-a**6*trial/(x**6*radius**2),"Kelvin Hardy term")
check(kelvin**3-a**6*trial**3/x**6,"Kelvin cubic")

v=sp.symbols("v",real=True)
q=-2*r**2*sp.sech(r*v)**2
check(sp.trigsimp(sp.diff(q,v,2)-4*r**2*q-3*q**2),
      "stationary KdV potential")
check(sp.trigsimp(sp.diff(q,v)**2-4*r**2*q**2-2*q**3),
      "stationary KdV first integral")

mp.mp.dps=35
RR=mp.mpf("1.3"); MM=mp.mpf("2.2")
for kind,values in [
    ("dn",[mp.mpf("0.3"),mp.mpf("0.7"),mp.mpf("0.97")]),
    ("cn",[mp.mpf("0.56"),mp.mpf("0.8"),mp.mpf("0.97")]),
]:
    for m in values:
        if kind=="dn":
            amp=1/mp.sqrt(MM*(2-m));scale=RR/mp.sqrt(2-m)
            expected_energy=-RR**2/MM*(1-m)/(2-m)**2
        else:
            amp=mp.sqrt(m/(MM*(2*m-1)));scale=RR/mp.sqrt(2*m-1)
            expected_energy=RR**2/MM*m*(1-m)/(2*m-1)**2
        fn=lambda z:amp*mp.ellipfun(kind,scale*z,m)
        at=mp.mpf("0.37")
        deriv=mp.diff(fn,at)
        ode=mp.diff(fn,at,2)-RR**2*fn(at)+2*MM*RR**2*fn(at)**3
        en=deriv**2-RR**2*fn(at)**2+MM*RR**2*fn(at)**4
        assert mp.almosteq(ode,0,abs_eps=mp.mpf("1e-28")),(kind,m,ode)
        assert mp.almosteq(en,expected_energy,rel_eps=mp.mpf("1e-28")),(kind,m,en)

# The generic quartic is smooth exactly away from two singular energies.
z,e=sp.symbols("z e")
check(sp.discriminant(e+z**2-z**4,z)+16*e*(4*e+1)**2,
      "energy quartic discriminant")

print("Chapter 3 symbolic checks and Jacobi numerical checks passed.")
