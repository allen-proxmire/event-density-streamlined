"""Numerical check of the result in Result.md.

For H(k) = e^{ik} A + e^{-ik} B with N channels:
  symmetric case  B = S A S^-1   -> det H(k) even in k, winding 0
  one-way control B = 0          -> winding N about 0
  Hermitian control B = A^dagger -> det H(k) real, winding 0

    python tools/check_result.py

Requires numpy.
"""
import math
import sys
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")
rng = np.random.default_rng(0)
k = np.linspace(-math.pi, math.pi, 4001)[:-1]


def dets(A, B):
    return np.array([np.linalg.det(np.exp(1j * q) * A + np.exp(-1j * q) * B) for q in k])


def winding(f, z0):
    ph = np.angle(f - z0)
    steps = np.angle(np.exp(1j * np.diff(np.append(ph, ph[0]))))
    return int(round(steps.sum() / (2 * math.pi)))


def reference(f):
    """A point well clear of the curve f."""
    scale = np.max(np.abs(f))
    z0 = 0.0
    while np.min(np.abs(f - z0)) < 1e-3 * scale:
        z0 = complex(*rng.normal(size=2)) * 0.1 * scale
    return z0


ok = True
print("N  symmetric: max|f(k)-f(-k)|/max|f|  windings | one-way winding | Hermitian windings")
for N in range(1, 7):
    S = np.fliplr(np.eye(N))
    even_err, sym_w, herm_w = 0.0, set(), set()
    for _ in range(20):
        A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
        f = dets(A, S @ A @ S)
        even_err = max(even_err, np.max(np.abs(f - f[::-1][np.r_[-1, :len(f) - 1]])) / np.max(np.abs(f)))
        sym_w.add(winding(f, reference(f)))
        g = dets(A, A.conj().T)
        herm_w.add(winding(g, reference(g) + 1j * 1e-3 * np.max(np.abs(g))))
    A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    oneway = winding(dets(A, np.zeros((N, N))), 0)
    ok &= sym_w == {0} and oneway == N and herm_w == {0} and even_err < 1e-9
    print("%d  %.1e  %s | %d | %s" % (N, even_err, sorted(sym_w), oneway, sorted(herm_w)))

print("\nresult holds for N = 1..6" if ok else "\nCHECK FAILED")
sys.exit(0 if ok else 1)
