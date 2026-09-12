"""Check the paper copies in this repository against the canonical corpus.

The papers here are copies, cleaned of drafting headers. When a canonical
paper changes, the copy goes stale silently. This reports that, and refreshes
on request, keeping each copy's local title block and replacing the body.

    python tools/check_paper_sync.py            # report drift
    python tools/check_paper_sync.py --apply    # refresh the drifted copies

Needs the ED Generative corpus on disk. Set ED_CANON to its physics-papers
directory if it is not at the default path below.
"""
import io, os, sys
sys.stdout.reconfigure(encoding="utf-8")
CANON = os.environ.get("ED_CANON", r"C:\Users\allen\GitHub\ED Generative\physics-papers")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MAP = {
 "Papers/Adjacency-Bandwidth Asymmetry from Spatial Homogeneity.md": "qm-kinematics/Paper_012_7_AdjacencyBandwidth_Galilean.md",
 "Papers/Anyon Prohibition in 3_1D.md": "relativistic-qm/Paper_104_AnyonProhibition.md",
 "Papers/BH_Rindler_Cosmological_Acoustic Horizons as One Substrate Object.md": "black-hole/Paper_047_5_HorizonUniversalization.md",
 "Papers/Charge As Topology_Winding_Integral Gauss Law.md": "substrate-evaluation/Paper_ChargeAsTopology_B4.md",
 "Papers/Clean Substrate Vector_Parity Spontaneous.md": "substrate-evaluation/Paper_CleanSubstrateVector_ParitySpontaneous.md",
 "Papers/Frame Uniqueness_Clifford 3_1.md": "relativistic-qm/Paper_103_Cl31_FrameUniqueness.md",
 "Papers/GR-III_Dynamical Rule.md": "gravity/Paper_GR-III_DynamicalRule.md",
 "Papers/GR-II_ED Gravity is Khronometric Class.md": "gravity/Paper_GR-II_KhronometricClass.md",
 "Papers/GR-IV_Preferred Frame Safety_Quantum Coherence.md": "gravity/Paper_GR-IV_ArrowsAlibi.md",
 "Papers/Hawking Spectrum.md": "black-hole/Paper_047_HawkingSpectrum.md",
 "Papers/Horizon as Decoupling Surface_Trans Planckian Resolution_Planck Mass Remnant.md": "black-hole/Paper_039_HorizonDecoupling.md",
 "Papers/Inflationary Spectrum.md": "cosmology/Paper_ED_Cos_06_InflationarySpectrum.md",
 "Papers/MatterSector_Gauge_Spin_Chirality_3D.md": "qft/Paper_MS-II_MatterSectorFromTheArrow.md",
 "Papers/Thermal 2Pi_Entropy Coefficient.md": "black-hole/Paper_BH_Thermal2Pi_EntropyCoefficient.md",
 "Papers/upstream/GR-I_Weak Field Einstein Metric.md": "gravity/Paper_GR-I_WeakFieldEinsteinMetric.md",
 "Papers/upstream/The 13 Primitives.md": "foundations/Paper_087_13Primitives.md",
 "Papers/upstream/V1 Kernel_Finite Width Retarded.md": "foundations/Paper_089_V1Kernel.md",
 "Papers/upstream/V5 Kernel_Cross Chain Correlation.md": "foundations/Paper_090_V5Kernel.md",
}


def body(text):
    """Everything from the first '## ' heading on: the paper minus its header block."""
    lines = text.replace("\r\n", "\n").split("\n")
    for i, l in enumerate(lines):
        if l.startswith("## "):
            return "\n".join(lines[i:]).strip()
    return text.strip()


def head(text):
    """The cleaned local header: everything before the first '## ' heading."""
    lines = text.replace("\r\n", "\n").split("\n")
    for i, l in enumerate(lines):
        if l.startswith("## "):
            return "\n".join(lines[:i])
    return ""


if __name__ == "__main__":
    apply = "--apply" in sys.argv
    drift = []
    for rel, canon_rel in MAP.items():
        rp, cp = os.path.join(REPO, rel), os.path.join(CANON, canon_rel)
        if not os.path.exists(rp):
            print("MISSING COPY  ", rel); continue
        if not os.path.exists(cp):
            print("MISSING CANON ", canon_rel); continue
        rt = io.open(rp, encoding="utf-8").read()
        ct = io.open(cp, encoding="utf-8").read()
        rb, cb = body(rt), body(ct)
        if rb != cb:
            drift.append(rel)
            print("DRIFT  %-62s  copy %d chars / canon %d" % (os.path.basename(rel), len(rb), len(cb)))
            if apply:
                io.open(rp, "w", encoding="utf-8", newline="\n").write(head(rt) + cb + "\n")
                print("       refreshed, local header preserved")
    if not drift:
        print("all 18 copies match canon")
    else:
        print("\n%d file(s) drifted%s" % (len(drift), " and were refreshed" if apply else ""))
