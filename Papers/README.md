# Papers

The papers behind the sixteen results, copied from the `ED Generative` repository and cleaned: the drafting headers (series, status, repository paths, genre) are gone, so each paper reads as itself rather than as an entry in a filing system. The physics is untouched.

Fourteen papers carry sixteen results, because GR-II carries three.

| paper | result it carries |
|---|---|
| Anyon Prohibition in 3_1D | no anyons in three dimensions |
| Charge As Topology_Winding_Integral Gauss Law | charge as a winding number |
| Clean Substrate Vector_Parity Spontaneous | parity violation must be spontaneous |
| Horizon as Decoupling Surface | the horizon as a decoupling surface |
| Hawking Spectrum | the Hawking temperature |
| MatterSector_Gauge_Spin_Chirality_3D | where the gauge groups come from |
| GR-II_ED Gravity is Khronometric Class | geodesic motion; the khronometric class; gravitational waves at c |
| GR-III_Dynamical Rule | the khronon speed |
| GR-IV_Preferred Frame Safety_Quantum Coherence | the preferred-frame parameter α₂ = 0 |
| Thermal 2Pi_Entropy Coefficient | the black-hole entropy coefficient 1/4 |
| Adjacency-Bandwidth Asymmetry from Spatial Homogeneity | why kinetic energy carries a 1/2 |
| Frame Uniqueness_Clifford 3_1 | the spinor frame is unique |
| BH_Rindler_Cosmological_Acoustic Horizons as One Substrate Object | four kinds of horizon, one law |
| Inflationary Spectrum | primordial tensor modes |

## Keeping them current

These are copies. The canonical papers live in the `ED Generative` corpus and change there; a copy left alone goes stale without saying so. Copies verified against canon **2026-09-12**.

    python tools/check_paper_sync.py            # report drift
    python tools/check_paper_sync.py --apply    # refresh, keeping each local title block

## Reading them

Each paper opens with a preamble stating what it does **not** claim, written before the rest of the paper. That is the fastest way to see the shape of a result, and it is where the borrowing is admitted.

Each also carries a step audit, usually §2.5 or §4, marking every load-bearing step as postulated, derived, inherited, measured or open. The [result pages](../Results/) are built from those audits, read against the papers rather than summarized from memory.

## Upstream

[upstream/](upstream/) holds four papers that are not themselves results here, but that the sixteen stand on.
