# The Matter Sector from the Arrow: Gauge Groups, Spin, Chirality, and Three Dimensions
Allen Proxmire
2026


---

> **Review note (2026-09-12).** Apart from one corrected group identity in the abstract (noted below), the text is the corpus copy. These corrections come from a review of this repository and take precedence over it.
>
> - **Corrected here:** the abstract read $U(N) = SU(N)\times U(1)$. The correct identity is $U(N) = (SU(N)\times U(1))/\mathbb Z_N$, as §2 already has. *The canonical corpus copy still needs this fix, or `check_paper_sync.py --apply` will restore the error.*
> - **§5's "ED predicts no parity-violating abelian force" is contradicted by the Standard Model.** Hypercharge $U(1)_Y$ is abelian and chiral: left- and right-handed fermions carry different hypercharge. This falsifier is already met.
> - **Channel multiplicities {1, 2, 3} give $U(1)\times U(2)\times U(3)$, which has three abelian factors.** The Standard Model group, $(SU(3)\times SU(2)\times U(1))/\mathbb Z_6$, has one. The correspondence in §2 does not hold as stated.
> - **§2 is textbook.** The structure group of norm-preserving transport on $\mathbb C^N$ is $U(N)$.
> - **§4.1 does not show that objects "must" be spin-½.** The belt trick shows that spinor representations are *available* to tethered frames. Integer-spin objects are tethered too.
> - **§3 evades a no-go theorem; it does not construct chiral fermions.** Escaping the hypotheses of Nielsen–Ninomiya is not the same as building a chiral fermion. §6's internal $d = 3$ and §7's linking premise are unexplained, and the "measured" linking result illustrates a known topological fact.

## Preamble — What This Paper Does *Not* Claim

1. **It does not derive the Standard Model.** The SM gauge group as a specific selection, the weak force's particular chirality, the fermion masses and mixings, and the Yang–Mills *dynamics* are not derived.
2. **The results are tiered, and the tier is stated for each.** *Derived* = follows from the primitives; *structural* = a coherent reading of the substrate, defensible but not closed; *account* = a tiered explanation, not a proof; *measured* = simulated. The spinor assembly, the lattice-gauge form, and the dimensional argument are structural; the chirality origin is an account; only the gauge-group-from-multiplicity step and the linking topology are at the firmer end.
3. **Anomaly cancellation — the deepest consistency requirement of a chiral gauge theory — is untouched.**
4. **"Why three dimensions" rests on a topological elimination plus an open premise.** The topology (a spatial link survives only in 3D) is rigorous; that ED *holds its commitment-order by spatial linking* is a hypothesis, not yet shown.
5. **It introduces no new substrate primitives**, and it does not claim ED *bars* real phenomena it simply does not yet build — where ED's structure leaves no room for something (a parity-violating abelian force, a stable large gauge group), that is stated as a falsifiable *prediction*, not a decree.

---

> **⚠️ Chirality correction (2026-07-10) — read the chirality claims in this paper with these two updates from later work; the gauge, spin, uniqueness, and dimensional results are unaffected.**
> 1. **The P-imprint is retired.** The account that the arrow's first commitment imprints *both* a matter/antimatter reference (C) *and* a parity reference (P) — the "screw → a parity reference (P-type)" of §5 and the abstract's "imprints both a matter/antimatter reference and a parity reference" — over-read its P-half. ED natively selects the **C** reference but **not** a native P (parity) reference. See `physics-papers/substrate-evaluation/Paper_ParityWall_ChiralityVerdict.md`.
> 2. **γ⁵ is global, not per-channel.** The "chirality is the arrow's screw, *a channel-topology class*" locus (abstract, §4.2, §9) is relocated: `γ⁵ = i γ⁰ γ¹γ²γ³` is the arrow (`γ⁰`) times the *one global* spontaneous spatial orientation (`γ¹γ²γ³`), which is why no *local* per-channel screw was ever found. See `physics-papers/substrate-evaluation/Paper_CleanSubstrateVector_ParitySpontaneous.md` §2.
>
> The successor result (same paper): the clean substrate is **provably vector for every channel-count** (a transport-level theorem), so parity violation is **necessarily spontaneous**, and *which* force is chiral is **inherited** (representation-theoretic, the pseudoreality of `SU(2)`), not derived. §4.2 below carries the same γ⁵-locus note inline.

## Abstract

Event Density's substrate offers matter two things: **channels** (directional participation pathways, P07, carrying a U(1) polarity phase P09 and transported by P05) and the **arrow** (irreversible commitment, P11). From these, the Standard-Model-facing structure assembles. **Gauge groups come from channel multiplicity:** a family of *N* indistinguishable channels, under bandwidth conservation (P04), has structure group $U(N)=(SU(N)\times U(1))/\mathbb{Z}_N$ — non-abelian force from multiplicity (*derived*), with the SM groups corresponding to multiplicities {1,2,3}. **The substrate is a lattice gauge theory** — P05-transport is a *U(N)* link variable, the field strength a plaquette holonomy — on a *relational* graph (no Brillouin torus) carrying a *retarded* arrow (non-hermitian), exactly the two premises the Nielsen–Ninomiya doubling no-go requires and ED lacks, which is how a discrete substrate escapes "the universe cannot be a lattice." **The four-component spinor assembles from channel structure:** its spin-½ is the signature of *relationality* — a node tethered to the graph by its channels carries the *SU(2)→SO(3)* double cover (orientation-entanglement; a free point would not), its chirality is the arrow's "screw" (a channel-topology class), its internal gauge index is the multiplicity, and its U(1) phase is the polarity (electromagnetism). **Parity violation is a non-abelian phenomenon** — the abelian single-channel coupling is chirality-blind (vector), so ED predicts *no* parity-violating abelian force — and **all chirality traces to the arrow's first commitment**, which imprints both a matter/antimatter reference and a parity reference, unifying parity violation with baryogenesis (an account, not a proof). **The number of forces reduces to one number:** the independently-stable channel families in the internal amplitude space $\mathbb{C}^d$ are exactly {1,…,d}, so the SM's {1,2,3} corresponds to internal dimension *d = 3*, with no room for a stable $SU(N\geq 4)$. And **the number of spatial dimensions is three because the arrow must hold its committed order:** the only topological holder of order in a one-dimensional structure is a spatial *link*, and a link survives in three dimensions alone — two dimensions cannot link, four dimensions unravel it (measured: unlinking is forced to a collision in 3D and slides free in 4D). Three dimensions by elimination — conditional on ED holding its order by linking, the paper's one open premise, which (carried by the channels) would also tie the internal *d = 3* to the spatial 3 through the single bridge that is not a category error. The frontier — full representation spectrum, the weak force's specific chirality, anomalies, and the linking premise — is named.

---

## 1. What the Substrate Offers Matter

ED's substrate is a participation graph. Four primitives carry the matter content:

- **Channels (P07):** a channel is "a direction a chain can keep going in" — a stable, directional, rule-type-selective pathway. Channels are countable and compose (branch/merge).
- **Polarity (P09):** a U(1) phase carried *along* a channel — the channel supplies the direction, polarity supplies the phase.
- **Transport (P05):** the connection primitive that moves participation along channels.
- **The arrow (P11):** commitment is irreversible. It is ED's only time-reversal-breaking primitive, and — this paper's spine — every chiral and dimensional fact traces back to it.

The claim of the matter sector is that gauge structure, spin, chirality, the number of forces, and the number of dimensions are all read off these four.

## 2. Gauge Groups from Channel Multiplicity *(derived)*

A rule-type family of **N indistinguishable channels** carries a complex amplitude $\psi$ $\in$ $\mathbb{C}^N$. Bandwidth conservation (P04) requires the transport of this amplitude to be norm-preserving — an isometry — and invertibility between commitments makes it a unitary. The structure group is therefore

$$ U(N) = \bigl(SU(N) \times U(1)\bigr)/\mathbb{Z}_N. $$

**Non-abelian gauge structure comes from channel multiplicity** (P07) — a derivation, where the prior gauge-vocabulary treatment (T17) had only an analogy. The abelian/non-abelian split is the single-channel/cross-channel split: single-channel transport (the V1 kernel) gives the abelian *U(1)*; cross-channel mixing (the V5 kernel) gives non-abelian *SU(N)*. The Standard Model's *U(1) × SU(2) × SU(3)* corresponds to channel-family multiplicities {1, 2, 3}.

## 3. The Substrate Is a Lattice Gauge Theory *(structural)*

P05-transport of the *N* channels — bandwidth-conserving, invertible between commitments — is a *U(N)* **link variable**: the gauge field is the per-edge generator (*U = e^{iA}*, *A $\in$ $\mathfrak{u}$(N)*), and the field strength is the **plaquette holonomy** $U_\square$ (non-trivial holonomy = curvature; non-commutativity = non-abelian *F = dA + A$\wedge$A*). So ED's matter sector is a *U(N)* lattice gauge theory — but on a **relational graph** (no Brillouin torus) carrying the **retarded arrow** (non-hermitian transport).

This is the answer to the sharpest objection to any discrete-substrate program, **Nielsen–Ninomiya**: on a regular lattice, chiral fermions come in mirror-paired doublers that cancel, leaving a vector-like world — so "the universe cannot be a discrete lattice." The theorem's engine is the compact Brillouin-torus topology *and* hermiticity. ED has **neither** — relational graph, retarded arrow — with locality intact (finite-width kernels). The doubling no-go does not bind ED. (Whether the surviving fermion is genuinely chiral, beyond merely undoubled, is §5 and the open frontier.)

## 4. The Spinor, Assembled from Channels

The four-component Cl(3,1) spinor — the algebra of which is standard (T2/T4) — finds its *substrate object* in the channels. Four ingredients, four sources:

**4.1 Spin-½ is the signature of relationality *(structural — the new centerpiece).*** An ED object is never an isolated point; it is a node embedded in the graph, **tethered to its surroundings by its channels**. Act with the emergent spatial rotation group SO(3). The relevant topological fact is *$\pi_1(\mathrm{SO}(3))=\mathbb{Z}_2$*: a 2$\pi$ rotation is a non-contractible loop, a 4$\pi$ rotation contractible. For a *free* point this is invisible; for a *tethered* node it is physical — the Dirac belt / orientation-entanglement relation: rotating a tethered frame by 2$\pi$ leaves its tethers twisted, and only 4$\pi$ removes the twist. An object that must track that twist transforms under the universal cover **SU(2)** and picks up the −1 under 2$\pi$. **That is spin-½** — and an ED object cannot avoid it, because it is tethered. The deep reading: a free object would not need the double cover; a relational one does. *Spin-½ is the mark of being embedded in the graph rather than floating free* — "two is more fundamental than one," read off a rotating tethered frame. Standard physics *posits* spinors; ED *forces* them from its relational ontology.

**4.2 Chirality $\gamma^5$ is the arrow's screw *(structural, tiered as account).*** A commitment advances time and twists the P09 phase; the handedness of that twist is a spatial handedness — the "screw," located as a **channel-topology class**: $\gamma^5$ is which screw-handedness class the channel belongs to. **Citation correction (2026-07-05):** the evidence for this is a 1+1D toy-lattice computation (`foundations/ChiralGauge_SQ1b_ContinuumChirality_ToyModel.md`, `ChiralGauge_SQ1c_PointGapChirality.md`; `evaluation/ChiralGauge/chiral_winding.py`), not a property of the canonical V1 kernel itself (`Paper_089`'s $K_{V1}$ is a real scalar with no non-Hermitian operator or periodic parameter). The toy computation compares Hermitian vs. retarded ("arrow") lattice hopping and finds, only in the retarded case, nonzero point-gap winding, a non-Hermitian skin effect, and net spectral flow under $U(1)$ flux insertion — three converging signatures of a single net chirality, all zero in the Hermitian control. Three bridges remain open before this is a relativistic result: whether the toy chirality survives Lorentz-covariantization to a genuine $\gamma^5$ coupling (needs the open substrate-V1$\to$Dirac coarse-graining), whether the non-unitary generating mechanism coheres with an emergent unitary QFT (candidate: sparse commitment, unshown), and anomaly cancellation itself (untouched, named in the frontier below). **Locus update (2026-07-10):** the "screw as a *per-channel* channel-topology class" reading here is superseded, `γ⁵ = i γ⁰ γ¹γ²γ³` is a **global** object, the arrow (`γ⁰`) times the one spontaneous global spatial orientation (`γ¹γ²γ³`), which is why no *local* per-channel screw was ever found (T4_04/T4_10). This does not change the tier (account) or the verdict, it relocates the operator from per-channel to global. See `physics-papers/substrate-evaluation/Paper_CleanSubstrateVector_ParitySpontaneous.md` §2.

**4.3 Internal gauge index is the multiplicity** (§2); **4.4 the U(1) phase is the polarity** (P09) — the chirality-blind vector coupling, i.e. electromagnetism.

So **spinor = channel-topology (spin double cover + chirality) dressed with the polarity phase (EM)**. The spinor's kinematic skeleton is grounded in the substrate; the open part is the full classification of *which* topology classes carry *which* spins and groups (the frontier).

## 5. Parity Violation Is Non-Abelian; All Chirality Traces to the Arrow *(account)*

**Parity violation can live only in the non-abelian sector.** The abelian (single-channel, V1) coupling is chirality-blind — vector, parity-conserving (electromagnetism). Only the non-abelian (cross-channel, V5) coupling is chirality-sensitive. So **ED predicts no parity-violating abelian force** — a falsifiable prediction, since general gauge theory *permits* chiral abelian *U(1)*s. It matches the low-energy world: electromagnetism (abelian) is vector; the weak force (non-abelian) is chiral. (This places parity violation in the non-abelian sector; it does not by itself derive that the weak *SU(2)* is the chiral one — QCD's *SU(3)* is non-abelian and vector. Chirality is a property of the matter handedness-*assignment*, not the group. That assignment is the open core, §5 and below.)

**All chirality traces to the arrow's first commitment.** The arrow is ED's only handedness-breaking primitive. A commitment is a handed event carrying both a P09 phase and a channel-topology screw. The universe's *first* commitment imprints two global references at once: the phase → a matter/antimatter reference (C-type); the screw → a parity reference (P-type). Both are topological, hence all-or-nothing — *maximal* — matching the maximal parity violation and complete matter selection observed. **Parity violation and the matter/antimatter asymmetry are then two attributes of one first-arrival imprint** — correlated (same event) but distinct (so C and P are violated separately, with CP only partial), unifying the chiral-gauge structure with baryogenesis under the arrow. This is an *account*, not a proof: *which* handedness is selected is a contingent initial condition (standard spontaneous-symmetry-breaking), and *why the weak force specifically* inherits it rests on a candidate (the weak force as the commitment-coupled, flavor-changing one), the least-closed step.

## 6. The Number of Forces Reduces to One Number *(structural)*

Why {1,2,3} and no larger gauge group? Model the *N* same-rule-type channels of a family as complex unit vectors in the internal amplitude space $\mathbb{C}^d$; they coexist stably only if they stay **distinguishable** (mutual coherence below threshold). The maximum set of mutually-orthogonal (independent) channels in $\mathbb{C}^d$ is exactly **N = d**; beyond *d*, coherence is forced up (the Welch bound) and channels interfere. So the stable channel families are {1, …, d}.

This does **not** derive 3 — it **reduces the question to one number**: the SM's {1,2,3} corresponds to **internal amplitude dimension d = 3** (singlet, doublet, triplet are exactly the independently-stable families in $\mathbb{C}^3$), and ED leaves **no room for a stable $SU(N\geq 4)$** — a falsifiable prediction. The remaining question is sharp and singular: *why is the internal channel-amplitude dimension three?* — and it is an *internal* three, distinct in kind from the spatial three (a complex internal space, not a real spatial frame), so it does not reduce to spatial dimension by the naive identification.

## 7. Why Three Spatial Dimensions: the Arrow Must Hold Its Order *(structural; topology measured)*

ED's defining act is to lay down an **irreversible, ordered record** — which committed before which (the arrow). For that record to *persist*, the order must be *held* against continuous rearrangement. The only topological holder of order in a one-dimensional structure is a **spatial link**, and a link survives in exactly **three** spatial dimensions:

- **2D:** one-dimensional curves cannot pass each other — order is frozen, with no held linking structure.
- **3D:** curves link, and the linking is **topologically protected** (a continuous, self-avoiding motion cannot undo it). *Measured* (`linking_3d_vs_4d_probe`): unlinking two linked loops forces them to collide — minimum loop-to-loop distance driven to 0.000 — so the link is held.
- **4D:** every link comes apart — a curve lifts into the fourth coordinate and slides past another with room to spare. *Measured:* the same unlinking stays self-avoiding, minimum distance 0.600 — the order is *not* held.

So **three spatial dimensions by elimination**: the arrow needs somewhere it can keep its committed order, and only 3D both *forms* and *holds* the link. This is conditional on the one open premise — that ED holds its commitment-order by spatial linking of its chains — which is the next probe, not yet shown; the *dimensional* half (a link survives only in 3D) is rigorous, the *ED* half is the hypothesis. (An earlier framing in terms of *worldline* braiding was corrected: worldline braiding is a two-spatial-dimension phenomenon — anyons live in 2+1 — whereas spatial *linking* of one-dimensional curves is the three-dimensional fact.)

**This is the bridge §6 needed.** If the channels carry the same spatial-linking structure, their stable content is fixed by the 3D link/braid structure rather than by a free internal dimension — so the internal *d = 3* of §6 would *be* the spatial 3, not by identifying axes (the category error) but because the arrow's held order and the channels' stable structure are the *same* 3D-linking fact. The two threes meet at linking.

## 8. The Honest Open Frontier

- **The full channel-topology → representation spectrum:** which topology classes carry spin-0/½/1 and which gauge groups (§4 gives the double cover and §2 the internal multiplicity; the complete classification is open).
- **Why the weak force specifically is chiral** — the matter handedness-assignment (§5); a candidate, not a derivation.
- **Anomaly cancellation** — untouched; the hardest consistency requirement.
- **Whether ED holds its commitment-order by spatial linking** (§7's premise) — the *chains-as-links* probe that would turn "3D is where links hold" into "the arrow forces 3D."

## 9. Conclusion

ED's matter sector assembles from channels and the arrow. **Gauge groups are derived from channel multiplicity** ($U(N)=(SU(N)\times U(1))/\mathbb{Z}_N$); the substrate is a **lattice gauge theory** that escapes the discreteness no-go by being relational and retarded; the **spinor is assembled from channel structure**, with spin-½ revealed as the signature of *relationality* and chirality as the arrow's screw; **parity violation is non-abelian** (no parity-violating abelian force) and **all chirality traces to the arrow's first commitment** (unifying it with baryogenesis, as an account); the **number of forces reduces to one number** (the stable families are {1,…,d}, so {1,2,3} $\iff$ internal *d = 3*, no room for $SU(N\geq 4)$); and the **number of spatial dimensions is three** because the arrow must hold its committed order, and a spatial link — the sole topological order-holder — survives in 3D alone. One primitive, the arrow, runs through every result. The frontier — the representation spectrum, the weak chirality, the anomalies, and the linking premise — is named, not papered over.

---

## Falsifiers

- A **parity-violating abelian force** (general gauge theory permits one; ED's abelian coupling is the chirality-blind kernel, so ED predicts none).
- A **stable fundamental $SU(N\geq 4)$** gauge sector (ED's stable families are {1,…,d} with *d = 3*).
- ED shown **unable to carry net chirality** or the **spin double cover** from its channel structure (would break §4–§5).
- ED shown to **hold its committed order without spatial linking** — or the chains-as-links probe failing to find held order in 3D — would break the §7 dimensional argument.

## Tiers and Inheritances

*Derived:* gauge group $U(N)=(SU(N)\times U(1))/\mathbb{Z}_N$ from multiplicity (§2). *Structural:* the lattice-gauge form and Nielsen–Ninomiya escape (§3); the spinor assembly — spin double cover from relationality, chirality as screw-class (§4); the channel-stability reduction {1,2,3} $\iff$ *d = 3* (§6); the dimensional argument (§7). *Account:* parity-violation-is-non-abelian and chirality-from-the-arrow, with the weak-assignment a candidate (§5). *Measured:* the linking topology held-in-3D / erasable-in-4D (§7). *Inherited:* the Cl(3,1) spinor algebra (T2/T4); the standard topology (*$\pi_1(\mathrm{SO}(3))=\mathbb{Z}_2$*, codimension-2 linking); the Welch bound. *Supersedes* MS-I (*Gauge from Channels*), absorbing its four results and adding spin-from-relationality, the uniqueness-to-one-number reduction, and the dimensional argument.
