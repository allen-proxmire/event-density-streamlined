# Papers

The papers behind the sixteen results, copied from the `ED Generative` repository. The drafting headers (series, status, repository paths, genre) have been removed, so each paper reads as itself.

## Review notes come first

Each paper opens with a **review note (2026-09-12)** above its first section. The notes record errors, unsupported steps and places where a "derivation" restates known physics. **Where a note and the paper disagree, the note takes precedence.**

Two more things to keep in mind when reading:

- **The audit labels overstate.** Tier labels in the papers' own audit tables ("D", "D-via-I", "form-FORCED", "M1/M3") often mark a known result restated in ED terms rather than a derivation. Read the review note before trusting a tier.
- **One paper's body has been changed.** MatterSector's abstract carried a wrong group identity. It was corrected here, and its review note says so.

Fourteen papers carry the sixteen results, because GR-II carries three.

| paper | result it carries | verdict |
|---|---|---|
| Anyon Prohibition in 3_1D | no anyons in three dimensions | textbook, restated |
| Frame Uniqueness_Clifford 3_1 | the spinor frame is unique | textbook, restated |
| Charge As Topology_Winding_Integral Gauss Law | charge as a winding number | textbook, restated |
| MatterSector_Gauge_Spin_Chirality_3D | gauge groups and channel multiplicity | textbook, restated |
| Adjacency-Bandwidth Asymmetry from Spatial Homogeneity | the 1/2 in kinetic energy | textbook, restated |
| GR-II_ED Gravity is Khronometric Class | geodesic motion; gravitational class; gravitational-wave speed | textbook; not established; not established |
| Clean Substrate Vector_Parity Spontaneous | parity violation must be spontaneous | modest ED-specific |
| Horizon as Decoupling Surface | the horizon as a decoupling surface | identification |
| Hawking Spectrum | the Hawking temperature | identification |
| BH_Rindler_Cosmological_Acoustic Horizons as One Substrate Object | four kinds of horizon as one object | identification |
| Inflationary Spectrum | primordial and present-day gravitational waves | identification |
| GR-III_Dynamical Rule | the speed of the extra gravitational mode | not established |
| GR-IV_Preferred Frame Safety_Quantum Coherence | the preferred-frame parameter α₂ | not established |
| Thermal 2Pi_Entropy Coefficient | the black-hole entropy coefficient 1/4 | not established |

## Keeping them current

These are copies. The canonical papers live in the `ED Generative` corpus and change there, and a copy left alone goes stale without saying so.

    python tools/check_paper_sync.py            # report drift
    python tools/check_paper_sync.py --apply    # refresh, keeping each local title block

**`--apply` keeps the review notes and loses one local fix:**

- **Review notes survive.** Each note sits in the local title block, which `--apply` preserves.
- **The MatterSector fix does not.** It is in the paper body, so `--apply` would restore the error until the canonical paper is fixed too. Until then `check_paper_sync.py` will report that one file as drifted, which is expected.

The problems recorded in the review notes also exist in the canonical papers and should be fixed there.

## Upstream

[upstream/](upstream/) holds four papers that are not results here but that the sixteen stand on.
