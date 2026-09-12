"""Re-run the definite calculations behind the 2026-09-12 review.

Each check takes a claim whose own equations give a definite number or
structure, computes it, and compares it with established physics or
mathematics. No corpus bookkeeping is involved.

    python tools/run_checks.py

Requires numpy. Three checks use formulas quoted from the literature rather
than re-derived here, and say so: the khronometric scalar speed, the alpha_2
numerator, and the strong-coupling scaling.
"""
import cmath, math, sys
from fractions import Fraction as F
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
rng = np.random.default_rng(0)


def report(n, title, found, verdict):
    print("[%2d] %s\n     found:   %s\n     verdict: %s\n" % (n, title, found, verdict))


# 1. PPN gamma and beta for GR-I's metric as written: g00 = -b, g_ij = b^-1 delta_ij,
#    with b = 1 - 2U. PPN form: g00 = -1 + 2U - 2 beta U^2, g_ij = (1 + 2 gamma U) delta_ij.
U = np.linspace(1e-4, 1e-2, 50)
c00 = np.polyfit(U, -(1 - 2 * U), 3)[::-1]      # coefficients of 1, U, U^2, U^3
cij = np.polyfit(U, 1 / (1 - 2 * U), 3)[::-1]
beta, gamma = -c00[2] / 2, cij[1] / 2
mercury = 42.98 * (2 + 2 * gamma - beta) / 3
report(1, "GR-I metric: PPN gamma and beta",
       "gamma = %.3f, beta = %.3f; Mercury perihelion %.1f\"/century (measured 43.0\"); Nordtvedt eta = %.1f"
       % (gamma, beta, mercury, 4 * beta - gamma - 3),
       "gamma = 1 passes (light bending). beta = 0 fails: excluded by Mercury and lunar laser ranging.")

# 2. Horizon area in the isotropic metric: A = 4 pi r^2 / b, b = 1 - r_s/r.
areas = ["%.2e" % (4 * math.pi * (1 + e) ** 2 / (1 - 1 / (1 + e))) for e in (1e-2, 1e-4, 1e-6)]
report(2, "GR-I metric: horizon area as r -> r_s (r_s = 1)",
       "A at r = r_s(1+eps), eps = 1e-2, 1e-4, 1e-6: " + ", ".join(areas),
       "Diverges. A finite area 4 pi r_s^2 needs the areal Schwarzschild form, which GR-I does not derive.")

# 3. Entropy coefficient with r_s = k G M (G = hbar = c = 1). kappa = 1/(2 r_s) either way.
out = []
for k in (1, 2, 3):
    rs = np.linspace(0, 1, 200001)
    dS = (1 / k) * 4 * math.pi * rs               # dM / T with dM = dr_s/k, T = 1/(4 pi r_s)
    S = float(np.sum((dS[1:] + dS[:-1]) / 2 * np.diff(rs)))
    out.append("k=%d: S/A = %.4f" % (k, S / (4 * math.pi)))
report(3, "Thermal2Pi: entropy coefficient if r_s = k G M",
       "; ".join(out),
       "S = A/(2k). The 1/4 requires k = 2, which is matched to Newton through b ~ 1 + 2 Phi, not derived.")

# 4. GR-III's rule b_t = D b_xx: does a disturbance travel?
D, L, n = 1.0, 40.0, 801
x = np.linspace(-L / 2, L / 2, n)
dx = x[1] - x[0]
dt = 0.2 * dx ** 2 / D
b = np.exp(-x ** 2)
for _ in range(int(5.0 / dt)):
    b[1:-1] += D * dt * (b[2:] - 2 * b[1:-1] + b[:-2]) / dx ** 2
centroid = float(np.sum(x * b) / np.sum(b))
report(4, "GR-III rule b_t = D b_xx: dispersion and propagation",
       "plane wave gives omega = -i D k^2 (pure decay); a bump evolved to t = 5 has centroid %.1e, peak %.3f of initial"
       % (centroid, b.max()),
       "No waves and no wave speed. Tensor modes and 'waves at c' are not produced by the built rule.")

# 5. Khronometric scalar speed (formula quoted from Blas-Pujolas-Sibiryakov, as used in GR-IV):
#    c_s^2 = (beta + lambda)(2 - alpha) / [alpha (1 - beta)(2 + beta + 3 lambda)].
def cs2(a, bt, lam):
    return (bt + lam) * (2 - a) / (a * (1 - bt) * (2 + bt + 3 * lam))

tuned = [cs2(l / (1 + 2 * l), 0, l) for l in (1e-6, 1e-3, 0.1)]
report(5, "Scalar speed: GR-III's route (lambda = 0) vs GR-IV's (alpha = lambda/(1+2 lambda))",
       "lambda = 0, alpha = 1e-3: c_s^2 = %.3f; tuned alpha: c_s^2 = %s" % (cs2(1e-3, 0, 0), ", ".join("%.6f" % t for t in tuned)),
       "GR-III's lambda = 0 gives c_s = 0, not c. c_s = c needs a tuning ED does not derive.")

# 6. alpha_2 numerator at beta = 0 (quoted in GR-IV): -lambda + alpha + 2 alpha lambda.
vals = [-l + l / (1 + 2 * l) + 2 * (l / (1 + 2 * l)) * l for l in (F(1, 10**6), F(1, 1000), F(1, 3))]
report(6, "GR-IV: alpha_2 numerator on the luminal surface",
       "exact values: " + ", ".join(str(v) for v in vals),
       "Vanishes identically. Correct, but it is the c_s = c condition restated, so it inherits check 5.")

# 7. Strong-coupling scale ~ sqrt(lambda) M_P (scaling quoted from the khronometric literature).
report(7, "GR-IV: strong-coupling scale at lambda ~ 1e-93",
       "sqrt(1e-93) x 1.22e28 eV = %.1e eV" % (math.sqrt(1e-93) * 1.22e28),
       "Far below any energy of interest; the theory would not be perturbative.")

# 8. U(N) = SU(N) x U(1)? The map (g, z) -> z g has kernel {(w I, 1/w) : w^N = 1}.
res = []
for N in (2, 3, 4):
    w = cmath.exp(2j * math.pi / N)
    g = w * np.eye(N)
    res.append("N=%d: det(wI) = %s, (1/w)(wI) = I: %s" % (N, np.round(np.linalg.det(g), 12),
                                                         np.allclose(g / w, np.eye(N))))
report(8, "MatterSector: is U(N) = SU(N) x U(1)?",
       "; ".join(res),
       "No: the map has an N-element kernel, so U(N) = (SU(N) x U(1))/Z_N.")

# 9. Standard Model hypercharge (Q = T3 + Y), left-handed Weyl basis per generation.
fields = [("Q_L", 6, F(1, 6)), ("u_R^c", 3, F(-2, 3)), ("d_R^c", 3, F(1, 3)), ("L_L", 2, F(-1, 2)), ("e_R^c", 1, F(1))]
grav = sum(m * y for _, m, y in fields)
cubic = sum(m * y ** 3 for _, m, y in fields)
report(9, "MatterSector falsifier: 'no parity-violating abelian force'",
       "Y(u_L) = 1/6, Y(u_R) = 2/3, Y(e_L) = -1/2, Y(e_R) = -1; anomaly sums Y = %s, Y^3 = %s" % (grav, cubic),
       "Hypercharge is abelian and chiral (anomaly sums confirm the values). The falsifier is already met.")

# 10. Point-gap winding of det H(k), H = e^{ik} A + e^{-ik} S A S^-1 (parity-clean) vs one-way control.
def winding(vals, z0):
    ph = np.angle(vals - z0)
    return int(round(np.sum(np.angle(np.exp(1j * np.diff(np.append(ph, ph[0]))))) / (2 * math.pi)))

k = np.linspace(0, 2 * math.pi, 4001)[:-1]
clean, oneway = set(), []
for N in range(1, 7):
    S = np.fliplr(np.eye(N))
    for _ in range(10):
        A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
        d = np.array([np.linalg.det(np.exp(1j * q) * A + np.exp(-1j * q) * S @ A @ S) for q in k])
        z0 = 0
        while np.min(np.abs(d - z0)) < 1e-3 * np.max(np.abs(d)):
            z0 = complex(*rng.normal(size=2)) * np.max(np.abs(d)) * 0.1
        clean.add(winding(d, z0))
    A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    oneway.append(winding(np.array([np.linalg.det(np.exp(1j * q) * A) for q in k]), 0))
report(10, "Clean Substrate theorem: parity-clean winding for N = 1..6",
       "parity-clean windings seen: %s; one-way control windings: %s" % (sorted(clean), oneway),
       "Correct: zero for every N (control gives N). It is the parity-symmetry statement applied to this model.")

# 11. Cl(3,1) uniqueness: Dirac and Weyl gammas, intertwiner S = sum_A G'_A X G_A^-1.
s = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
I2, Z2 = np.eye(2), np.zeros((2, 2))
dirac = [np.block([[I2, Z2], [Z2, -I2]])] + [np.block([[Z2, si], [-si, Z2]]) for si in s]
weyl = [np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, si], [-si, Z2]]) for si in s]
eta = np.diag([1, -1, -1, -1])
alg = max(np.abs(g[m] @ g[v] + g[v] @ g[m] - 2 * eta[m, v] * np.eye(4)).max()
          for g in (dirac, weyl) for m in range(4) for v in range(4))


def basis(g):
    out = []
    for mask in range(16):
        M = np.eye(4, dtype=complex)
        for i in range(4):
            if mask >> i & 1:
                M = M @ g[i]
        out.append(M)
    return out

X = rng.normal(size=(4, 4))
Sm = sum(bp @ X @ np.linalg.inv(bd) for bp, bd in zip(basis(weyl), basis(dirac)))
inter = max(np.abs(weyl[m] @ Sm - Sm @ dirac[m]).max() for m in range(4))
report(11, "Frame Uniqueness: Dirac and Weyl gammas are similar",
       "Clifford relation error %.1e; intertwiner error %.1e; |det S| = %.2f" % (alg, inter, abs(np.linalg.det(Sm))),
       "Correct: Pauli's fundamental theorem. Standard mathematics.")

# 12. a_0 = c H_0 / 2 pi against the fitted a_0 ~ 1.20e-10 m/s^2.
r12 = ["H0=%.1f: %.3e m/s^2 (%.2f of fit)" % (h, 2.998e8 * h * 1e3 / 3.0857e22 / (2 * math.pi),
                                              2.998e8 * h * 1e3 / 3.0857e22 / (2 * math.pi) / 1.20e-10)
       for h in (67.4, 73.0)]
report(12, "GR-IV: a_0 = c H_0 / 2 pi", "; ".join(r12),
       "Close, not equal. A numerical coincidence known since Milgrom, not a derivation.")

# 13. Planck identities used for the remnant mass.
hbar, c, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
lP = math.sqrt(hbar * G / c ** 3)
report(13, "Horizon paper: G = c^3 lP^2/hbar and M* = hbar/(c lP) = M_P",
       "c^3 lP^2/hbar / G = %.12f; hbar/(c lP) / sqrt(hbar c/G) = %.12f" % (c ** 3 * lP ** 2 / hbar / G, hbar / (c * lP) / math.sqrt(hbar * c / G)),
       "Identities once lP is defined from G. They constrain nothing.")

# 14. Linearity: steady state of D b'' = kappa rho with b -> 1 at the edges.
m = 201
Lap = (np.diag(-2 * np.ones(m)) + np.diag(np.ones(m - 1), 1) + np.diag(np.ones(m - 1), -1))
rho = np.zeros(m)
rho[m // 2] = 1.0
deficit = lambda M: 1 - (np.linalg.solve(Lap, M * rho) + 1)
ratio = np.max(np.abs(deficit(2.0))) / np.max(np.abs(deficit(1.0)))
report(14, "GR-III: is r_s proportional to M emergent?",
       "deficit(2M) / deficit(M) = %.12f" % ratio,
       "Exactly 2 by linearity, before any simulation. Built in, not emergent.")

# 15. The 1/2 in kinetic energy.
x = 1e-3
report(15, "Adjacency-Bandwidth: where the 1/2 comes from",
       "(sqrt(1 + x^2) - 1) / x^2 at x = 1e-3: %.9f" % ((math.sqrt(1 + x * x) - 1) / (x * x)),
       "The 1/2 is the Taylor coefficient of the inherited relativistic energy. It is an input, not an output.")
