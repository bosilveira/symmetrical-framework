"""Consolidated, reproducible checks for the Symmetrical Framework.

Every check has an ID, a status label and a one-line statement.
Status labels used in this repository:
  [T] theorem or proposition proved in the text
  [V] verified by a symbolic or numerical computation (this file)
  [K] known result from the literature (not re-checked here)
  [I] interpretation, no proof claimed
Only [V] claims appear in this file.  Run:  python verification/run_all.py
"""
import random
import mpmath as mp
import sympy as sp
import numpy as np
from scipy.linalg import expm, sqrtm

mp.mp.dps = 30
CHECKS = []


def check(cid, status, statement, where):
    def deco(fn):
        CHECKS.append(dict(id=cid, status=status, statement=statement, where=where, fn=fn))
        return fn
    return deco


R, MU, X0 = mp.mpf('1.3'), mp.mpf('0.72'), mp.mpf('1.9')
TOL = mp.mpf('1e-14')
sech, tanh = mp.sech, mp.tanh


def ok(vals, tol=TOL):
    m = max(abs(v) for v in vals)
    return m < tol, 'max abs residual %s' % mp.nstr(m, 3)


def bump(x, r=R, mu=MU, x0=X0):
    return mp.sech(r * mp.log(x / x0)) / (2 * mp.sqrt(mu) * x)


def SO(f, x, r=R, mu=MU):
    f0, f1, f2 = f(x), mp.diff(f, x, 1), mp.diff(f, x, 2)
    return x**2 * f2 + 3 * x * f1 + (1 - r**2) * f0 + 8 * mu * r**2 * x**2 * f0**3


# ------------------------------------------------------------------ foundational paper
@check('F01', 'V', 'The sech bump solves the Master equation (M).', 'paper s4')
def _():
    return ok([SO(bump, mp.mpf(x)) for x in ('0.3', '1.1', '2.7', '9')])


@check('F02', 'V', 'Scale invariance: f_lambda(x)=f(x/lambda)/lambda solves (M); N(f) is invariant.', 'paper s3.1')
def _():
    lam = mp.mpf('2.3')
    fl = lambda x: bump(x / lam) / lam
    res = [SO(fl, mp.mpf(x)) for x in ('0.4', '1.5', '6')]
    N0 = mp.quad(lambda x: bump(x)**2 * x, [0, X0, mp.inf])
    N1 = mp.quad(lambda x: fl(x)**2 * x, [0, X0 * lam, mp.inf])
    return ok(res + [N0 - N1], mp.mpf('1e-12'))


@check('F03', 'V', 'SO[f] = (1/2x)(y_uu - r^2 y + 2 mu r^2 y^3) for y=2 x f, u=ln x (arbitrary f).', 'paper s3.2')
def _():
    g = lambda x: mp.e**(mp.mpf('0.3') * x) + x**2
    y = lambda u: 2 * mp.e**u * g(mp.e**u)
    out = []
    for x in (mp.mpf('0.8'), mp.mpf('2.1')):
        u = mp.log(x)
        lhs = SO(g, x)
        rhs = (mp.diff(y, u, 2) - R**2 * y(u) + 2 * MU * R**2 * y(u)**3) / (2 * x)
        out.append((lhs - rhs) / (1 + abs(lhs)))
    return ok(out, mp.mpf('1e-12'))


@check('F04', 'V', 'eps = y_u^2 - r^2 y^2 + mu r^2 y^4 equals 4 x^2 Phi[f]; (E1) holds on the bump and is W^2+S^2=1.', 'paper s3.3')
def _():
    g = lambda x: mp.e**(mp.mpf('0.3') * x) + x**2
    y = lambda u: 2 * mp.e**u * g(mp.e**u)
    Phi = lambda f, x: x**2 * mp.diff(f, x)**2 + 2 * x * f(x) * mp.diff(f, x) + (1 - R**2) * f(x)**2 + 4 * MU * R**2 * x**2 * f(x)**4
    x = mp.mpf('1.3'); u = mp.log(x)
    eps = mp.diff(y, u)**2 - R**2 * y(u)**2 + MU * R**2 * y(u)**4
    res = [(eps - 4 * x**2 * Phi(g, x)) / (1 + abs(eps))]
    res += [Phi(bump, mp.mpf(t)) for t in ('0.5', '2.2')]
    xx = mp.mpf('2.2'); f = bump(xx)
    W = -(1 + xx * mp.diff(bump, xx) / f) / R
    S = 2 * mp.sqrt(MU) * xx * f
    res.append(W**2 + S**2 - 1)
    return ok(res, mp.mpf('1e-12'))


@check('F05', 'V', 'At r=1 the bump is x0/(sqrt(mu)(x0^2+x^2)) and solves Delta_4 F + 8 mu F^3 = 0.', 'paper s1.2, s5.2')
def _():
    r1 = mp.mpf(1)
    F = lambda x: X0 / (mp.sqrt(MU) * (X0**2 + x**2))
    res = []
    for x in (mp.mpf('0.6'), mp.mpf('2.4')):
        res.append(F(x) - bump(x, r1))
        res.append(mp.diff(F, x, 2) + 3 * mp.diff(F, x) / x + 8 * MU * F(x)**3)
    return ok(res)


@check('F06', 'V', 'N(f) = int f^2 x dx = 1/(2 r mu) on the bump.', 'paper s4')
def _():
    N = mp.quad(lambda x: bump(x)**2 * x, [0, X0, mp.inf])
    return ok([N - 1 / (2 * R * MU)], mp.mpf('1e-18'))


@check('F07', 'V', 'Envelope f_s=1/(2 sqrt(mu) x) is NOT a solution (SO = r^2/(2 sqrt(mu) x)); f_pm=1/(2 sqrt(2mu) x) ARE solutions.', 'paper Prop 4.4')
def _():
    fs = lambda x: 1 / (2 * mp.sqrt(MU) * x)
    fp = lambda x: 1 / (2 * mp.sqrt(2 * MU) * x)
    x = mp.mpf('1.7')
    return ok([SO(fs, x) - R**2 / (2 * mp.sqrt(MU) * x), SO(fp, x)])


@check('F08', 'V', 'Linear backbone: J=1/y obeys J_uu = r^2 J and J_u^2 - r^2 J^2 = -mu r^2 on the bump.', 'paper Prop 3.5')
def _():
    J = lambda u: 1 / (2 * mp.e**u * bump(mp.e**u))
    out = []
    for u in (mp.mpf('-0.4'), mp.mpf('0.9')):
        out.append(mp.diff(J, u, 2) - R**2 * J(u))
        out.append(mp.diff(J, u)**2 - R**2 * J(u)**2 + MU * R**2)
    return ok(out, mp.mpf('1e-13'))



@check('F09', 'V', 'Scalar curvature of the metric f^2 |dz|^2 on R^4: -6 Delta f / f^3 = 6(1-r^2)/(x^2 f^2) + 48 mu r^2 (equals 48 mu at r=1).', 'paper Prop 5.2(a)')
def _():
    out = []
    for r in (mp.mpf('1.3'), mp.mpf('1')):
        f = lambda x: bump(x, r, MU, X0)
        for x in (mp.mpf('0.7'), mp.mpf('2.9')):
            lap = mp.diff(f, x, 2) + 3 * mp.diff(f, x) / x
            Rs = -6 * lap / f(x)**3
            out.append(Rs - (6 * (1 - r**2) / (x**2 * f(x)**2) + 48 * MU * r**2))
        if r == 1:
            out.append(-6 * (mp.diff(f, mp.mpf('1.1'), 2) + 3 * mp.diff(f, mp.mpf('1.1')) / mp.mpf('1.1')) / f(mp.mpf('1.1'))**3 - 48 * MU)
    return ok(out, mp.mpf('1e-12'))


@check('F10', 'V', 'Proof steps of Theorem 4.2: (y^2)\'\' = 2 y\'^2 + 2 s y^2 - 4 kappa y^4 (convexity step), and y_hat = sqrt(s/kappa) sech(sqrt(s)(u-u0)) solves (S).', 'paper s4 proof')
def _():
    s, kap = mp.mpf('0.8'), mp.mpf('0.3')
    yh = lambda u: mp.sqrt(s / kap) * sech(mp.sqrt(s) * (u - mp.mpf('0.4')))
    out = []
    for u in (mp.mpf('-0.5'), mp.mpf('1.1')):
        out.append(mp.diff(yh, u, 2) - (s * yh(u) - 2 * kap * yh(u)**3))
    y, yp = sp.symbols('y yp'); S, K = sp.symbols('s kappa')
    ypp = S * y - 2 * K * y**3
    d = sp.simplify(sp.diff(y**2, y) * ypp + sp.diff(sp.diff(y**2, y) * yp, y) * yp - (2 * yp**2 + 2 * S * y**2 - 4 * K * y**4))
    return (d == 0 and max(abs(v) for v in out) < mp.mpf('1e-13')), 'symbolic residual %s, numeric %s' % (d, mp.nstr(max(abs(v) for v in out), 3))


@check('S09', 'V', 'Bump values: integral of L_c dx = r/(3 mu); virial ratio int y_u^2 : int r^2 y^2 : int mu r^2 y^4 = 1 : 3 : 2.', 'structural properties')
def _():
    y = lambda u: sech(R * u) / mp.sqrt(MU)
    A = mp.quad(lambda u: mp.diff(y, u)**2, [-mp.inf, 0, mp.inf])
    B = mp.quad(lambda u: R**2 * y(u)**2, [-mp.inf, 0, mp.inf])
    C = mp.quad(lambda u: MU * R**2 * y(u)**4, [-mp.inf, 0, mp.inf])
    Lc = (A + B - C) / 4
    return ok([Lc - R / (3 * MU), B / A - 3, C / A - 2], mp.mpf('1e-12'))


# ------------------------------------------------------------------ identifications
@check('I01', 'V', "Euler-top separatrix (k=1): V=tanh, D=Y=sech solve V'=DY, D'=-VY; Nahm triple (-coth,-csch,-csch).", 'paper s5.1')
def _():
    out = []
    f1 = lambda s: -1 / mp.tanh(s)
    f2 = lambda s: -1 / mp.sinh(s)
    for t in (mp.mpf('0.7'), mp.mpf('-1.4')):
        out += [mp.diff(tanh, t) - sech(t) * sech(t), mp.diff(sech, t) + tanh(t) * sech(t), tanh(t)**2 + sech(t)**2 - 1]
        out += [mp.diff(f1, t) - f2(t) * f2(t), mp.diff(f2, t) - f2(t) * f1(t)]
    return ok(out, mp.mpf('1e-14'))


@check('I02', 'V', 'phi=(1+W)/2: phi(1-phi)=mu x^2 f^2, phi_u=2r phi(1-phi), phi_uu=4r^2 phi(1-phi)(1-2phi).', 'paper s5.2')
def _():
    ph = lambda u: (1 + tanh(R * (u - mp.log(X0)))) / 2
    out = []
    for u in (mp.mpf('-0.3'), mp.mpf('0.8')):
        p = ph(u); x = mp.e**u
        out += [p * (1 - p) - MU * x**2 * bump(x)**2,
                mp.diff(ph, u) - 2 * R * p * (1 - p),
                mp.diff(ph, u, 2) - 4 * R**2 * p * (1 - p) * (1 - 2 * p)]
    return ok(out)


@check('I03', 'V', 'Friedmann dictionary (s,kappa,eps)=(-k,-Lambda/3,C): conformal-time cubic, constraint, cosmic-time cosine.', 'paper s5.3')
def _():
    s, kap = mp.mpf('0.8'), mp.mpf('0.3')
    k, Lam, C = -s, -3 * kap, 0
    a = lambda e: mp.sqrt(s / kap) * sech(mp.sqrt(s) * e)
    gd = lambda x: 2 * mp.atan(mp.e**x) - mp.pi / 2
    out = []
    for e in (mp.mpf('-0.5'), mp.mpf('0.9')):
        out.append(mp.diff(a, e, 2) + k * a(e) - 2 * Lam / 3 * a(e)**3)
        out.append(mp.diff(a, e)**2 - (C - k * a(e)**2 + Lam / 3 * a(e)**4))
        t = gd(mp.sqrt(s) * e) / mp.sqrt(kap)
        out.append(a(e) - mp.sqrt(s / kap) * mp.cos(mp.sqrt(kap) * t))
    return ok(out)


@check('I04', 'V', "Stationary focusing cubic NLS: -y'' - 2 mu r^2 y^3 + r^2 y = 0 for y = mu^{-1/2} sech(r u).", 'paper further realizations')
def _():
    y = lambda u: sech(R * u) / mp.sqrt(MU)
    return ok([-mp.diff(y, u, 2) - 2 * MU * R**2 * y(u)**3 + R**2 * y(u) for u in (mp.mpf('-0.6'), mp.mpf('1.2'))])


@check('I05', 'V', "Sine-Gordon / pendulum separatrix: phi = 2 gd(theta) + pi solves phi'' = sin phi; phi'/2 = sech.", 'paper further realizations')
def _():
    gd = lambda x: 2 * mp.atan(mp.e**x) - mp.pi / 2
    phi = lambda t: 2 * gd(t) + mp.pi
    out = []
    for t in (mp.mpf('-1.3'), mp.mpf('0.4'), mp.mpf('2.1')):
        out += [mp.diff(phi, t, 2) - mp.sin(phi(t)), mp.diff(phi, t) / 2 - sech(t)]
    return ok(out)


@check('I06', 'V', "KdV stationary equation for w=y^2: w''=4r^2 w-6 mu r^2 w^2; Hirota tau=J: (ln J)''=mu r^2 y^2.", 'paper further realizations')
def _():
    y = lambda u: sech(R * u) / mp.sqrt(MU)
    w = lambda u: y(u)**2
    J = lambda u: mp.sqrt(MU) * mp.cosh(R * u)
    out = []
    for u in (mp.mpf('-0.5'), mp.mpf('0.7')):
        out.append(mp.diff(w, u, 2) - (4 * R**2 * w(u) - 6 * MU * R**2 * w(u)**2))
        out.append(mp.diff(lambda s: mp.log(J(s)), u, 2) - MU * R**2 * y(u)**2)
    return ok(out)


@check('I07', 'V', "phi^4 kink: W=tanh(r u) solves W''=-2 r^2 W + 2 r^2 W^3.", 'paper further realizations')
def _():
    W = lambda u: tanh(R * u)
    return ok([mp.diff(W, u, 2) + 2 * R**2 * W(u) - 2 * R**2 * W(u)**3 for u in (mp.mpf('-0.4'), mp.mpf('0.9'))])


@check('I08', 'V', "Mercator/Gudermannian: gd' = sech, cos(gd)=sech, sin(gd)=tanh.", 'paper further realizations')
def _():
    gd = lambda x: 2 * mp.atan(mp.e**x) - mp.pi / 2
    out = []
    for t in (mp.mpf('-1.1'), mp.mpf('0.6')):
        out += [mp.diff(gd, t) - sech(t), mp.cos(gd(t)) - sech(t), mp.sin(gd(t)) - tanh(t)]
    return ok(out)


@check('I09', 'V', "Euclidean bounce: action 2r/(3 mu); fluctuation operator has negative mode sech^2 (eigenvalue -3r^2) and zero mode y'.", 'paper further realizations')
def _():
    y = lambda u: sech(R * u) / mp.sqrt(MU)
    SE = mp.quad(lambda u: mp.diff(y, u)**2 / 2 + R**2 * y(u)**2 / 2 - MU * R**2 * y(u)**4 / 2, [-mp.inf, 0, mp.inf])
    M = lambda psi, u: -mp.diff(psi, u, 2) + (R**2 - 6 * MU * R**2 * y(u)**2) * psi(u)
    neg = lambda u: sech(R * u)**2
    zero = lambda u: mp.diff(y, u)
    u = mp.mpf('0.45')
    return ok([SE - 2 * R / (3 * MU), M(neg, u) + 3 * R**2 * neg(u), M(zero, u)], mp.mpf('1e-12'))


# ------------------------------------------------------------------ structural properties
@check('S01', 'V', 'Euler-Lagrange: EL(L) = x * SO[f] for L=-x^3 f_x^2/2 + (1-r^2) x f^2/2 + 2 mu r^2 x^3 f^4.', 'structural properties')
def _():
    x, r, mu = sp.symbols('x r mu', positive=True)
    f = sp.Function('f')(x)
    L = -x**3 * sp.diff(f, x)**2 / 2 + (1 - r**2) * x * f**2 / 2 + 2 * mu * r**2 * x**3 * f**4
    EL = sp.diff(L, f) - sp.diff(sp.diff(L, sp.diff(f, x)), x)
    SOe = x**2 * sp.diff(f, x, 2) + 3 * x * sp.diff(f, x) + (1 - r**2) * f + 8 * mu * r**2 * x**2 * f**3
    d = sp.simplify(EL - x * SOe)
    return d == 0, 'difference = %s' % d


@check('S02', 'V', 'Noether charge of the dilation x->l x, f->f/l for L_c=-2L equals -eps/4.', 'structural properties')
def _():
    x, r, mu, f, fp = sp.symbols('x r mu f fp')
    Lc = x**3 * fp**2 - (1 - r**2) * x * f**2 - 4 * mu * r**2 * x**3 * f**4
    p = sp.diff(Lc, fp)
    Q = p * (-f - fp * x) + Lc * x
    Phi = x**2 * fp**2 + 2 * x * f * fp + (1 - r**2) * f**2 + 4 * mu * r**2 * x**2 * f**4
    d = sp.simplify(Q + x**2 * Phi)
    return d == 0, 'Q + eps/4 = %s' % d


@check('S03', 'V', "Jerk equation y''' = r^2 y'(1-6 mu y^2); first integral C = y'' - r^2 y + 2 mu r^2 y^3 (C=0 on the bump).", 'structural properties')
def _():
    y = lambda u: sech(R * u) / mp.sqrt(MU)
    out = []
    for u in (mp.mpf('-0.5'), mp.mpf('0.8')):
        out.append(mp.diff(y, u, 3) - R**2 * mp.diff(y, u) * (1 - 6 * MU * y(u)**2))
        out.append(mp.diff(y, u, 2) - R**2 * y(u) + 2 * MU * R**2 * y(u)**3)
    return ok(out, mp.mpf('1e-12'))


@check('S04', 'V', "Log-derivative (Miura) map: v=y'/y obeys v''+2r^2 v-2 v^3=0 for every solution (any eps).", 'structural properties')
def _():
    r, mu, y, yp = sp.symbols('r mu y yp')
    ypp = r**2 * y - 2 * mu * r**2 * y**3
    D = lambda e: sp.diff(e, y) * yp + sp.diff(e, yp) * ypp
    v = yp / y
    v1 = D(v)
    v2 = D(v1)
    d = sp.simplify(v2 + 2 * r**2 * v - 2 * v**3)
    return d == 0, 'residual = %s' % d


@check('S05', 'V', 'Position moments (weight dx): E[x^k] = c^k sec(pi k/(2r)) for |k|<r.', 'structural properties / moments')
def _():
    r, c = mp.mpf('2.7'), mp.mpf('1.9')
    f = lambda x: mp.sech(r * mp.log(x / c)) / (2 * x)
    I = mp.pi / (2 * r)
    out = []
    for k in (mp.mpf('0.5'), mp.mpf('-1.2'), mp.mpf('2')):
        m = mp.quad(lambda x: x**k * f(x), [0, c, mp.inf]) / I
        out.append(m - c**k * mp.sec(mp.pi * k / (2 * r)))
    return ok(out, mp.mpf('1e-12'))


@check('S06', 'V', 'Amplitude (Wallis) moments: int sech^k(r u) du = sqrt(pi) Gamma(k/2) / (r Gamma((k+1)/2)).', 'structural properties / moments')
def _():
    out = []
    for k in (1, 2, 3, 4):
        num = mp.quad(lambda u: sech(R * u)**k, [-mp.inf, 0, mp.inf])
        out.append(num - mp.sqrt(mp.pi) * mp.gamma(mp.mpf(k) / 2) / (R * mp.gamma(mp.mpf(k + 1) / 2)))
    return ok(out, mp.mpf('1e-14'))


@check('S07', 'V', "Reciprocal map: y''=sy-2kappa y^3 with integral eps  =>  E=1/y obeys E''=sE+2 eps E^3 with integral -kappa.", 'structural properties / duality')
def _():
    s, kap, eps, y, yp = sp.symbols('s kappa epsilon y yp')
    ypp = s * y - 2 * kap * y**3
    D = lambda e: sp.diff(e, y) * yp + sp.diff(e, yp) * ypp
    E = 1 / y
    E1 = D(E)
    E2 = D(E1)
    yp2 = eps + s * y**2 - kap * y**4
    d1 = sp.simplify(E2.subs(yp**2, yp2) - (s * E + 2 * eps * E**3))
    d2 = sp.simplify((E1**2).subs(yp**2, yp2) - s * E**2 - eps * E**4 + kap)
    return (d1 == 0 and d2 == 0), 'residuals %s, %s' % (d1, d2)


@check('S08', 'V', 'Curvature of (y^2/4)(du^2+dpsi^2): K = 4 kappa + 4 eps / y^4 (constant iff eps=0).', 'structural properties / geometry')
def _():
    s, kap, eps, y = sp.symbols('s kappa epsilon y', positive=True)
    ypp = s * y - 2 * kap * y**3
    yp2 = eps + s * y**2 - kap * y**4
    lnypp = ypp / y - yp2 / y**2
    K = sp.simplify(-4 / y**2 * lnypp)
    d = sp.simplify(K - (4 * kap + 4 * eps / y**4))
    return d == 0, 'residual = %s' % d


# ------------------------------------------------------------------ geometry
@check('G01', 'V', 'Spindle: K=4 mu r^2 (Liouville), pole-to-pole distance I = pi R, area pi/(r mu), Gauss-Bonnet = 4 pi.', 'paper s5.2 / geometry')
def _():
    y = lambda u: sech(R * u) / mp.sqrt(MU)
    out = []
    for u in (mp.mpf('-0.3'), mp.mpf('0.6')):
        out.append(mp.diff(lambda s: mp.log(y(s)), u, 2) + MU * R**2 * y(u)**2)
    I = mp.quad(lambda x: bump(x), [0, X0, mp.inf])
    Rr = 1 / (2 * R * mp.sqrt(MU))
    out.append(I - mp.pi * Rr)
    area = 4 * mp.pi * R * Rr**2
    out.append(area - mp.pi / (R * MU))
    out.append(area / Rr**2 + 2 * (2 * mp.pi - 2 * mp.pi * R) - 4 * mp.pi)
    return ok(out, mp.mpf('1e-13'))


@check('Z01', 'V', 'f^2 is NFW at r=1/2; rho(1/xi)=xi^4 rho(xi); log-slope = -2-2r tanh; rho x dx split in half at r_s; r=1/2 finite-mass threshold.', 'paper further realizations')
def _():
    f2 = lambda x, r: x**(2 * r - 2) / (1 + x**(2 * r))**2
    nfw = lambda x: 1 / (x * (1 + x)**2)
    out = [f2(mp.mpf('0.37'), mp.mpf(1) / 2) - nfw(mp.mpf('0.37'))]
    for r in (mp.mpf('0.8'), mp.mpf('1.7')):
        xi = mp.mpf('1.9')
        out.append(f2(1 / xi, r) - xi**4 * f2(xi, r))
        x = mp.mpf('2.7')
        W = (x**(2 * r) - 1) / (x**(2 * r) + 1)
        out.append(mp.diff(lambda t: mp.log(f2(mp.e**t, r)), mp.log(x)) + 2 + 2 * r * W)
    half = mp.quad(lambda t: t * nfw(t), [0, 1]) / mp.quad(lambda t: t * nfw(t), [0, 1, mp.inf])
    out.append(half - mp.mpf(1) / 2)
    r = mp.mpf('1.5')
    z = mp.pi / (2 * r)
    ratio = mp.quad(lambda t: t**2 * f2(t, r), [0, 1, mp.inf]) / mp.quad(lambda t: t * f2(t, r), [0, 1, mp.inf])
    out.append(ratio - z / mp.sin(z))
    return ok(out, mp.mpf('1e-12'))


# ------------------------------------------------------------------ duality dial
def Z3(r):
    return 1 + 2 * mp.nsum(lambda n: mp.sech(r * n), [1, mp.inf])


def Z2(r):
    return 2 * mp.nsum(lambda n: mp.sech(r * (n + mp.mpf(1) / 2)), [0, mp.inf])


def Z4(r):
    return 1 + 2 * sum((-1)**n * mp.sech(r * n) for n in range(1, 400))


@check('D01', 'V', 'Fourier self-reciprocity: int sech(r u) e^{iku} du = (pi/r) sech(pi k/(2r)); unitary fixed point r*=sqrt(pi/2).', 'duality dial')
def _():
    r = mp.sqrt(mp.pi / 2)
    out = []
    for k in (mp.mpf('0.3'), mp.mpf('1.9')):
        ft = mp.quad(lambda u: sech(r * u) * mp.cos(k * u), [-mp.inf, 0, mp.inf]) / mp.sqrt(2 * mp.pi)
        out.append(ft - sech(r * k))
    return ok(out, mp.mpf('1e-14'))


@check('D02', 'V', 'Lattice sum: sum_n sech(r n) = theta_3(e^{-r})^2 = (pi/r) sum_n sech(pi^2 n / r) (Poisson duality r -> pi^2/r).', 'duality dial')
def _():
    out = []
    for r in (mp.mpf('0.9'), mp.mpf('2.3')):
        Z = Z3(r)
        out += [Z - mp.jtheta(3, 0, mp.e**(-r))**2, Z - mp.pi / r * Z3(mp.pi**2 / r)]
    return ok(out, mp.mpf('1e-14'))


@check('D03', 'V', 'Three lattice sums are theta_2^2, theta_3^2, theta_4^2; Z3^2 = Z2^2 + Z4^2; S: Z4(r)=(pi/r) Z2(pi^2/r).', 'duality dial')
def _():
    r = mp.mpf('1.4')
    q = mp.e**(-r)
    a, b, c = Z3(r), Z2(r), Z4(r)
    return ok([a - mp.jtheta(3, 0, q)**2, b - mp.jtheta(2, 0, q)**2, c - mp.jtheta(4, 0, q)**2,
               a**2 - b**2 - c**2, c - mp.pi / r * Z2(mp.pi**2 / r)], mp.mpf('1e-14'))


@check('D04', 'V', 'Half-split: int_0^c f dx = pi/(4 r sqrt(mu)) = Leibniz/(r sqrt(mu)); f dx is invariant under x -> c^2/x.', 'duality dial / half-split')
def _():
    f = lambda x: bump(x, R, MU, X0)
    left = mp.quad(f, [0, X0])
    right = mp.quad(f, [X0, mp.inf])
    x = mp.mpf('0.77')
    inv = f(X0**2 / x) * X0**2 / x**2 - f(x)
    leib = mp.nsum(lambda n: (-1)**int(n) / (2 * n + 1), [0, mp.inf]) / (R * mp.sqrt(MU))
    return ok([left - mp.pi / (4 * R * mp.sqrt(MU)), right - left, inv, left - leib], mp.mpf('1e-12'))


@check('D05', 'V', 'Symplectic invariant of the sech state: RMS(|psi|^2) x RMS(|psi-hat|^2) = pi/6, independent of r.', 'duality dial / symplectic')
def _():
    def sd(w):
        n = mp.quad(w, [-mp.inf, 0, mp.inf])
        m2 = mp.quad(lambda t: t * t * w(t), [-mp.inf, 0, mp.inf])
        return mp.sqrt(m2 / n)
    out = []
    for r in (mp.mpf('0.6'), mp.mpf('1.7')):
        A = lambda u: sech(r * u)
        Ah = lambda k: mp.pi / r * sech(mp.pi * k / (2 * r))
        out.append(sd(lambda u: A(u)**2) * sd(lambda k: Ah(k)**2) - mp.pi / 6)
    return ok(out, mp.mpf('1e-14'))


@check('D06', 'V', 'Wigner function of the sech state in closed form; negativity volume is about 0.0162 (r=1).', 'duality dial / symplectic')
def _():
    r = mp.mpf(1)
    u, k = mp.mpf('0.37'), mp.mpf('0.8')
    closed = (4 * mp.pi / r) * mp.sin(2 * k * u) / (mp.sinh(2 * r * u) * mp.sinh(mp.pi * k / r))
    direct = mp.quad(lambda s: sech(r * (u + s / 2)) * sech(r * (u - s / 2)) * mp.cos(k * s), [-40, 0, 40])
    ug = np.linspace(0, 16, 2000)
    kg = np.linspace(0, 12, 2000)
    U, K = np.meshgrid(ug, kg, indexing='ij')
    with np.errstate(divide='ignore', invalid='ignore'):
        W = 4 * np.pi * np.sin(2 * K * U) / (np.sinh(2 * U) * np.sinh(np.pi * K))
        W = np.where(U < 1e-12, 4 * np.pi * K / np.sinh(np.pi * K), W)
        W = np.where(K < 1e-12, 8 * U / np.sinh(2 * U), W)
        W = np.where((U < 1e-12) & (K < 1e-12), 4.0, W)
    tz = np.trapezoid
    integ = lambda F: 4 * tz(tz(F, kg, axis=1), ug) / (2 * np.pi)
    norm, neg = integ(W), integ(np.abs(W))
    delta = neg / norm - 1
    good = abs(closed - direct) < 1e-10 and abs(norm - 2) < 1e-4 and abs(delta - 0.0162) < 5e-4
    return bool(good), 'closed-direct=%s, norm=%.6f, delta=%.5f' % (mp.nstr(closed - direct, 3), norm, delta)


# ------------------------------------------------------------------ Lie structure
@check('L01', 'V', 'EP charges form sl(2): {K,D}=K, {D,H0}=H0, {K,H0}=2D; Casimir H0 K - D^2 = g/4; Q+ Q- - H^2 = Omega^2 g; {Q+,Q-}=4 Omega H.', 'structural / Lie')
def _():
    Y, p, g, Om = sp.symbols('Y p g Omega', positive=True)
    PB = lambda F, G: sp.diff(F, Y) * sp.diff(G, p) - sp.diff(F, p) * sp.diff(G, Y)
    H0 = p**2 / 2 + g / (2 * Y**2)
    D = Y * p / 2
    K = Y**2 / 2
    H = H0 - Om**2 * K
    Qp = H0 + 2 * Om * D + Om**2 * K
    Qm = H0 - 2 * Om * D + Om**2 * K
    res = [PB(K, D) - K, PB(D, H0) - H0, PB(K, H0) - 2 * D, H0 * K - D**2 - g / 4,
           Qp * Qm - H**2 - Om**2 * g, PB(Qp, Qm) - 4 * Om * H, PB(Qp, H) - 2 * Om * Qp, PB(Qm, H) + 2 * Om * Qm]
    bad = [sp.simplify(e) for e in res if sp.simplify(e) != 0]
    return not bad, 'nonzero residuals: %s' % bad


@check('L02', 'V', 'EP point symmetries X1=d_u, X2=e^{ru}(d_u+(r/2)Y d_Y), X3=e^{-ru}(d_u-(r/2)Y d_Y) form sl(2); the Master cubic keeps only X1.', 'structural / Lie')
def _():
    u = sp.symbols('u', real=True)
    r, mu, g, Y = sp.symbols('r mu g Y', positive=True)
    Om = r / 2

    def residual(xi, eta, F):
        yp, yy = sp.symbols('yp yy')
        Dt = lambda E: sp.diff(E, u) + yp * sp.diff(E, yy) + F.subs(Y, yy) * sp.diff(E, yp)
        et, xi_ = eta.subs(Y, yy), xi.subs(Y, yy)
        e1 = Dt(et) - yp * Dt(xi_)
        e2 = Dt(e1) - F.subs(Y, yy) * Dt(xi_)
        return sp.simplify(e2 - (xi_ * sp.diff(F.subs(Y, yy), u) + et * sp.diff(F.subs(Y, yy), yy)))

    EP = Om**2 * Y + g / Y**3
    Mst = r**2 * Y - 2 * mu * r**2 * Y**3
    gens = [(sp.Integer(1), sp.Integer(0)),
            (sp.exp(r * u), Om * Y * sp.exp(r * u)),
            (sp.exp(-r * u), -Om * Y * sp.exp(-r * u))]
    ep_ok = all(residual(a, b, EP) == 0 for a, b in gens)
    mst_ok = [residual(a, b, Mst) == 0 for a, b in gens]

    def comm(A, B):
        (x1, e1), (x2, e2) = A, B
        return (sp.simplify(x1 * sp.diff(x2, u) + e1 * sp.diff(x2, Y) - x2 * sp.diff(x1, u) - e2 * sp.diff(x1, Y)),
                sp.simplify(x1 * sp.diff(e2, u) + e1 * sp.diff(e2, Y) - x2 * sp.diff(e1, u) - e2 * sp.diff(e1, Y)))
    c23 = comm(gens[1], gens[2])
    good = ep_ok and mst_ok == [True, False, False] and c23 == (-2 * r, 0)
    return bool(good), 'EP ok=%s, cubic symmetric flags=%s, [X2,X3]=%s' % (ep_ok, mst_ok, c23)


@check('L03', 'V', "Riccati V'=r^2-V^2: cross-ratio superposition from three particular solutions gives exact solutions.", 'structural / Lie systems')
def _():
    V = lambda u, ph: R * tanh(R * u + ph)
    phis = (mp.mpf('-0.4'), mp.mpf('0.3'), mp.mpf('0.9'))

    def sup(u, kk):
        x1, x2, x3 = [V(u, p) for p in phis]
        return (x1 * (x3 - x2) * kk + x2 * (x1 - x3)) / ((x3 - x2) * kk + (x1 - x3))
    out = []
    for kk in (mp.mpf('0.7'), mp.mpf('-2.3')):
        f = lambda u: sup(u, kk)
        u0 = mp.mpf('0.25')
        out.append(mp.diff(f, u0) - (R**2 - f(u0)**2))
    return ok(out, mp.mpf('1e-14'))


@check('L04', 'V', 'sl(2,R): m=span(sigma3,sigma1) and m=span(sigma1,R) are Lie triple systems; a null generator has no complement.', 'structural / Lie')
def _():
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    Rr = sp.Matrix([[0, 1], [-1, 0]])
    br = lambda a, b: a * b - b * a
    tri = lambda x, y, z: br(br(x, y), z)
    random.seed(0)
    good = True
    for (m1, m2) in ((s3, s1), (s1, Rr)):
        for _ in range(4):
            el = lambda: random.randint(-3, 3) * m1 + random.randint(-3, 3) * m2
            x, y, z, u, v = [el() for _ in range(5)]
            good &= sp.simplify(tri(x, x, z)) == sp.zeros(2)
            good &= sp.simplify(tri(x, y, z) + tri(y, z, x) + tri(z, x, y)) == sp.zeros(2)
            good &= sp.simplify(tri(u, v, tri(x, y, z)) - tri(tri(u, v, x), y, z) - tri(x, tri(u, v, y), z) - tri(x, y, tri(u, v, z))) == sp.zeros(2)
    N = sp.Matrix([[0, 1], [0, 0]])
    F = sp.Matrix([[0, 0], [1, 0]])
    chain = (br(N, F) == s3 and br(N, s3) == -2 * N)
    return bool(good and chain), 'axioms=%s, Jordan chain=%s' % (good, chain)


@check('L05', 'V', "Lax pair L=W T1+S T2, M=r S T3: L'=[L,M] (and [L,M] != 0), tr L^2 const; Hopf connection A=(dtau-cos(Theta)dphi)/2 has c1=1.", 'structural / Hopf')
def _():
    u, r = sp.symbols('u r', real=True)
    I = sp.I
    T = [-I * m / 2 for m in (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]]))]
    br = lambda a, b: a * b - b * a
    W, S = sp.tanh(r * u), sp.sech(r * u)
    L = W * T[0] + S * T[1]
    M = r * S * T[2]
    simp = lambda e: sp.simplify(e.rewrite(sp.exp))
    lax = (sp.diff(L, u) - br(L, M)).applyfunc(simp)
    comm_nonzero = br(L, M).applyfunc(simp) != sp.zeros(2)
    tr = sp.simplify((L * L).trace())
    Th, ph = sp.symbols('Theta phi', real=True)
    A_phi = -sp.cos(Th) / 2
    c1 = sp.integrate(sp.integrate(sp.diff(A_phi, Th), (Th, 0, sp.pi)), (ph, 0, 2 * sp.pi)) / (2 * sp.pi)
    good = lax == sp.zeros(2) and comm_nonzero and tr == sp.Rational(-1, 2) and c1 == 1
    return bool(good), 'Lax residual zero=%s, [L,M]!=0: %s, tr L^2=%s, c1=%s' % (lax == sp.zeros(2), comm_nonzero, tr, c1)


@check('L06', 'V', 'Thomas-Wigner: composing perpendicular boosts of rapidities a,b gives rotation alpha with tan(alpha/2)=tanh(a/2) tanh(b/2).', 'structural / Hopf')
def _():
    s3 = np.array([[1, 0], [0, -1]], float)
    s1 = np.array([[0, 1], [1, 0]], float)
    out = []
    for a, b in ((0.8, 1.1), (2.0, 0.5), (1.5, 1.5)):
        M = expm(a * s3 / 2) @ expm(b * s1 / 2)
        Rot = np.real(np.linalg.inv(sqrtm(M @ M.T)) @ M)
        alpha = 2 * np.arctan2(Rot[0, 1], Rot[0, 0])
        out.append(abs(abs(alpha) - 2 * np.arctan(np.tanh(a / 2) * np.tanh(b / 2))))
    return max(out) < 1e-9, 'max error %.2e' % max(out)


# ---- Lie-system closure (vector fields, exact modular arithmetic)
_P = 2**61 - 1


def _padd(a, b, s=1):
    r = dict(a)
    for k, c in b.items():
        r[k] = (r.get(k, 0) + s * c) % _P
        if r[k] == 0:
            del r[k]
    return r


def _pmul(a, b):
    r = {}
    for (i, j), c in a.items():
        for (k, l), d in b.items():
            r[(i + k, j + l)] = (r.get((i + k, j + l), 0) + c * d) % _P
    return {k: c for k, c in r.items() if c}


def _dx(a):
    return {(i - 1, j): (c * i) % _P for (i, j), c in a.items() if i != 0}


def _dv(a):
    return {(i, j - 1): (c * j) % _P for (i, j), c in a.items() if j > 0}


def _act(A, f):
    return _padd(_pmul(A[0], _dx(f)), _pmul(A[1], _dv(f)))


def _br(A, B):
    return (_padd(_act(A, B[0]), _act(B, A[0]), -1), _padd(_act(A, B[1]), _act(B, A[1]), -1))


def _flat(V):
    d = {}
    for c in (0, 1):
        for m, co in V[c].items():
            d[(c,) + m] = co
    return d


class _Ech:
    def __init__(s):
        s.piv = {}

    def add(s, d):
        d = dict(d)
        while d:
            m = max(d)
            if m in s.piv:
                c = d[m]
                for k, co in s.piv[m].items():
                    d[k] = (d.get(k, 0) - c * co) % _P
                    if d[k] == 0:
                        del d[k]
            else:
                inv = pow(d[m], _P - 2, _P)
                s.piv[m] = {k: (c * inv) % _P for k, c in d.items()}
                return True
        return False


def closure_dims(gens, depth, cap=60):
    E = _Ech()
    basis = []
    for g in gens:
        if E.add(_flat(g)):
            basis.append(g)
    dims = [len(basis)]
    frontier = list(basis)
    for _ in range(depth):
        new = []
        for A in basis:
            for B in frontier:
                C = _br(A, B)
                if (C[0] or C[1]) and E.add(_flat(C)):
                    new.append(C)
        if not new:
            return dims, True
        basis += new
        frontier = new
        dims.append(len(basis))
        if len(basis) > cap:
            return dims, False
    return dims, False


@check('L07', 'V', 'Vessiot-Guldberg closure: Riccati and Ermakov-Pinney close at dimension 3; the cubic r(t) family grows 2,3,5,10,24,... (no closure).', 'structural / Lie systems')
def _():
    one = {(0, 0): 1}
    ric = [(one, {}), ({(1, 0): 1}, {}), ({(2, 0): 1}, {})]
    ep = [({(0, 1): 1}, {(-3, 0): 1}), ({}, {(1, 0): 1})]
    cub = [({(0, 1): 1}, {}), ({}, {(1, 0): 1, (3, 0): _P - 1})]
    d1, f1 = closure_dims(ric, 4)
    d2, f2 = closure_dims(ep, 4)
    d3, f3 = closure_dims(cub, 4)
    good = (f1 and d1[-1] == 3) and (f2 and d2[-1] == 3) and (not f3 and d3[:5] == [2, 3, 5, 10, 24])
    return bool(good), 'Riccati %s, EP %s, cubic %s' % (d1, d2, d3)


# ------------------------------------------------------------------ recurrence / Lucas sequence
@check('R01', 'V', 'h_n=(A^{n+1}-B^{n+1})/(A-B); Cassini h_{n-1}^2-h_n h_{n-2}=(AB)^{n-1} (also at A=B); Green kernel is h_{n-k}.', 'follow-ups / recurrence')
def _():
    from fractions import Fraction as Fr
    A, B = Fr(3, 2), Fr(5, 7)
    h = [Fr(1), A + B]
    for n in range(2, 14):
        h.append((A + B) * h[-1] - A * B * h[-2])
    ok1 = all(h[n] * (A - B) == A**(n + 1) - B**(n + 1) for n in range(14))
    ok2 = all(h[n - 1]**2 - h[n] * h[n - 2] == (A * B)**(n - 1) for n in range(2, 14))
    a = Fr(2, 3)
    hd = [(n + 1) * a**n for n in range(10)]
    ok3 = all(hd[n - 1]**2 - hd[n] * hd[n - 2] == (a * a)**(n - 1) for n in range(2, 10))
    k0 = 3
    x = {0: Fr(0), 1: Fr(0)}
    for n in range(2, 12):
        x[n] = (A + B) * x[n - 1] - A * B * x[n - 2] + (1 if n == k0 else 0)
    ok4 = all(x[n] == (h[n - k0] if n >= k0 else 0) for n in range(2, 12))
    return bool(ok1 and ok2 and ok3 and ok4), 'closed=%s cassini=%s degenerate=%s green=%s' % (ok1, ok2, ok3, ok4)


@check('R02', 'V', 'h_n(J) are monic orthogonal polynomials of the semicircle on [-sqrt(mu), sqrt(mu)]: moments C_n (mu/4)^n; norms (mu/4)^n.', 'follow-ups / recurrence')
def _():
    mu = mp.mpf('0.72')
    sq = mp.sqrt(mu)
    w = lambda J: 2 / (mp.pi * mu) * mp.sqrt(mu - J**2)
    out = []
    for n in range(0, 4):
        m = mp.quad(lambda J: J**(2 * n) * w(J), [-sq, sq])
        out.append(m - mp.binomial(2 * n, n) / (n + 1) * (mu / 4)**n)
    h = [lambda J: 1, lambda J: J]
    for n in range(2, 5):
        h.append((lambda a, b: (lambda J: J * a(J) - mu / 4 * b(J)))(h[-1], h[-2]))
    out.append(mp.quad(lambda J: h[3](J)**2 * w(J), [-sq, sq]) - (mu / 4)**3)
    out.append(mp.quad(lambda J: h[2](J) * h[4](J) * w(J), [-sq, sq]))
    return ok(out, mp.mpf('1e-14'))
