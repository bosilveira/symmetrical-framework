#!/usr/bin/env python3
"""Independent symbolic checks for selected typed transformation formulas.

Run: python reference/atlas/verify_transformations.py
Requires SymPy. This verifies displayed algebra, not global geometry or novelty.
"""
import sympy as sp

r, A, B = sp.symbols("r A B", positive=True, finite=True)
u, C = sp.symbols("u C", real=True, finite=True)
mu = sp.symbols("mu", positive=True)
epsilon = sp.symbols("epsilon", real=True)
z, p, e = sp.symbols("z p e", real=True)
Delta = A*B-C**2
J = A*sp.exp(r*u)+2*C+B*sp.exp(-r*u)
der = sp.diff(J,u)

def zero(expr, label):
    residual = sp.cancel(sp.together(expr))
    residual = sp.simplify(residual)
    if residual != 0:
        raise AssertionError(f"{label}: {residual}")

# SF-M-004: jets reconstruct all three Gram coefficients at fixed r and u.
jet_P=sp.diff(J,u,2)/r**2
jet_D=der/r
zero(sp.exp(-r*u)*(jet_P+jet_D)/2-A, "Gram coefficient A")
zero(sp.exp(r*u)*(jet_P-jet_D)/2-B, "Gram coefficient B")
zero((J-jet_P)/2-C, "Gram coefficient C")
zero(der**2-r**2*(J**2-4*C*J-4*Delta), "Gram first integral")

# SF-M-005: equivalent polynomial identity for positive Pinney square root.
zero(2*J*sp.diff(J,u,2)-der**2-r**2*J**2-4*r**2*Delta, "Pinney determinant")

# SF-M-007: general reciprocal ODE; importantly epsilon is not set to zero.
y, y_u=sp.symbols("y y_u", nonzero=True, real=True)
y_uu=r**2*y-2*mu*r**2*y**3
E=y_u**2-r**2*y**2+mu*r**2*y**4
Jinv=1/y
Jinv_uu=2*y_u**2/y**3-y_uu/y**2
zero(Jinv_uu-r**2*Jinv-2*E*Jinv**3, "generic reciprocal defect")
zero(y_u**2-r**2*y**2+mu*r**2*y**4-E, "Master energy definition")

# SF-M-010: amplitude and independent-variable changes remove mu and r.
theta=sp.symbols("theta")
yp=sp.symbols("yp", real=True)
zeta=sp.sqrt(mu)*y
p_theta=sp.sqrt(mu)/r*yp
e_dimless=mu/r**2*(yp**2-r**2*y**2+mu*r**2*y**4)
zero(p_theta**2-e_dimless-zeta**2+zeta**4, "dimensionless energy")

# SF-M-011: degree-two quotient, with preserved marked time differential.
X=-z**2
Y=-2*z*p
curve=Y**2-4*X*(X**2+X-e)
zero(curve.subs(p**2,e+z**2-z**4), "quartic quotient")
zero(sp.diff(X,z)/Y-1/p, "marked differential dX/Y = dz/p")

# SF-M-013: periodic dn linearization is n=2 Lame after rescaling.
m=sp.symbols("m",real=True)
dn2, sn2=sp.symbols("dn2 sn2")
L_scaled=(2-m)-6*dn2
zero(L_scaled.subs(dn2,1-m*sn2)-(6*m*sn2-(4+m)), "Lame potential")

# SF-M-014: tau_G determines Gram shape but not its positive scale.
A0,a0,b0=sp.symbols("A0 a0 b0",positive=True)
tau_re=a0
tau_im=b0
Crec=A0*tau_re
Brec=A0*(tau_re**2+tau_im**2)
zero((Crec+sp.I*sp.sqrt(A0*Brec-Crec**2))/A0-(tau_re+sp.I*tau_im),
     "Gram tau reconstruction")

# SF-M-015: Lambda>0 local clock and amplitude normalization.
Lambda,epsR,Z=sp.symbols("Lambda epsR Z",positive=True)
zR=sp.sqrt(Lambda)*Z
eR=epsR**2/Lambda**2
# dz_R/dh = Lambda * dZ/dtheta; equation divided by Lambda^2.
zero((epsR**2+Lambda*zR**2-zR**4)/Lambda**2
     -(eR+Z**2-Z**4), "Riemann oscillator normalization")

# SF-M-016: the spatial nonlinear power map requires the resolution Jacobian.
x, c, s_res, lam = sp.symbols("x c s_res lam", positive=True)
T = sp.symbols("T", positive=True)  # invariant (x/c)^r = exp(theta)
x_new = c*(x/c)**(1/s_res)
jac = sp.diff(x_new,x)
f_old = T/(x*(1+T**2))
f_new = T/(x_new*(1+T**2))
zero(jac-x_new/(s_res*x), "resolution Jacobian")
zero(f_new*jac-f_old/s_res, "unnormalized density resolution weight")
zero((2*s_res*r/sp.pi)*f_new*jac-(2*r/sp.pi)*f_old,
     "normalized density pushforward")
zero(sp.expand((s_res*y_u)**2-(s_res*r)**2*y**2
     +mu*(s_res*r)**2*y**4
     -s_res**2*(y_u**2-r**2*y**2+mu*r**2*y**4)),
     "resolution transported Master energy")
zero(mu*s_res**2*epsilon/(s_res*r)**2-mu*epsilon/r**2,
     "dimensionless energy invariance")

# SF-M-017: simultaneous x,c dilation is distinct from resolution transport.
zero(((lam*x)/(lam*c))**r-(x/c)**r, "dilation log-coordinate invariant")
zero((f_old/lam)*lam-f_old, "dilation mass covariance")

# SF-M-018: diagonal Gram boost fixes AB, C, Delta and chi.
delta=sp.symbols("delta",real=True)
Anew=A*sp.exp(r*delta)
Bnew=B*sp.exp(-r*delta)
zero(Anew*Bnew-A*B, "Gram boost product")
zero(Anew*Bnew-C**2-Delta, "Gram boost determinant")
zero((Anew*sp.exp(r*u)+2*C+Bnew*sp.exp(-r*u))
     -J.subs(u,u+delta), "Gram boost envelope transport")
tau_root=sp.symbols("tau_root",positive=True)
tau_G=(C+sp.I*tau_root)/A
tau_new=(C+sp.I*tau_root)/Anew
zero(tau_new-sp.exp(-r*delta)*tau_G,"Gram shape boost")

print("PASS: symbolic checks for Gram, Pinney, reciprocal, time-coordinate, elliptic quotient, Lamé, shape, and Riemann contracts")
