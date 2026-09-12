# The Topological Skeleton of Charge: Quantized Winding and an Integral Gauss Law on the Event-Density Graph
Allen Proxmire
2026


---
> **Review note (2026-09-12).** The text below is the corpus copy, unchanged. These corrections come from a review of this repository and take precedence over it.
>
> - **The integer winding is $\pi_1(U(1)) = \mathbb Z$.** For a single-valued phase it is exact by construction, so "confirmed to machine precision" could not have come out otherwise.
> - **Loop independence is the ordinary vortex winding of an XY / lattice U(1) model.** Calling it an "integral Gauss law" is an analogy. Gauss's law relates a field's flux to enclosed charge, and here there is no field, as §5 says.
> - **"Protected by the arrow" is an interpretation, not a separate result.**
> - **§5 is a genuine, honestly reported negative:** a determined $1/r^2$ field appears only when ED's own invariants are dropped.

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **ED does not derive electromagnetism, Maxwell's equations, or the Coulomb field.** No Maxwell derivation is claimed anywhere; §7 states the open problem and explicitly disclaims a derivation.
3. **The result is reached graph-first, not charge-first.** The topological invariant is forced by the participation-graph structure and only *then* compared to charge. No topology is retrofit to hit a target value: **the charge spectrum (±1, ∓⅓), the Standard-Model content, and the fine-structure constant are not produced and not claimed.** The integers ±1, ∓⅓ do not appear; what appears is an integer winding `w ∈ ℤ` with no selected magnitude.
4. **The winding is inert under the certified rule.** Because the Σ-selection is orientation-blind (phase-blind), the winding has no dynamical effect at the Σ level; it couples only weakly, through the P04 bandwidth channel. It is a conserved topological invariant, not a dynamically active charge.
5. **The absence of a determined local (Coulomb) field at the discrete layer is correct, not a deficiency.** A continuous determined field is a coarse-grained object by construction; demanding it on the graph is a layer error (§5, §7). Whether ED's DCGT coarse-graining *yields* Maxwell/Coulomb in the continuum limit is **open and unproven** (§7).
6. **Structural / form parallel only.** This is a claim about *which structure* ED realizes (the topological skeleton of charge), not a claim that ED's winding *is* electric charge or explains it. No content claim about electromagnetism.
7. **One certified substrate, minimal arenas (U(1) on cycles / small graphs).** The contrasts (quantized integer winding; loop-size-independent circulation; sweep-dependence with vs without P11) are the result, not absolute magnitudes.

---

## Abstract

The boldest falsifiable claim of the Contrast-First ontology is that a physical constant can be a *global relational fact* — and electric charge, a discrete conserved quantity, is the cleanest concrete case. We test it graph-first: *does the ED participation graph admit a topological invariant that behaves like charge, forced by the graph structure rather than fit to it?* It does, and we map exactly how far the parallel reaches. **The skeleton is realized.** Single-valued committed U(1) polarity (P09 + P11) yields an integer **winding `w ∈ ℤ`** (`π₁(U(1)) = ℤ`, confirmed to machine precision); the winding is **conserved and irreversibility-protected** (it cannot slip without an "uncommitting" P11 forbids); it couples weakly through a discrete `w`-indexed bandwidth ladder (`∝ cos²(πw/N)`, P04); and it obeys an **integral Gauss law** — the circulation around any enclosing loop equals `2πw`, independent of loop size and shape (the topological content of Gauss's law). **The metric flesh is withheld at the discrete layer.** There is no *determined local field* (no Coulomb `1/r²`): the per-edge configuration is gauge/sweep-dependent (sweep-dependence 0.76 when orientation-blindness alone is relaxed), and a determined isotropic `1/r²` field appears only when P11 irreversibility is *also* removed (`deficit·r² ≈ 0.126`, initialization-independent) — at which point the system is ordinary lattice-field relaxation, no longer ED. The single reason throughout is that the Σ-selection is **orientation-blind**. We then make one surgical correction (the Round-5 reframe): a determined *continuous* field was being sought at the *discrete* layer. Read as **lattice gauge theory**, the holonomies are link variables, the Coulomb field is their **continuum (DCGT) limit**, the "undetermined local field" is ordinary lattice gauge freedom, and the relevant **Maxwell-like action is already latent** in the coherence term `cos²(Δφ/2)` — orientation-blind Σ simply does not minimize it at the micro layer. So "outside ED by construction" becomes the well-posed, ED-native open question: **does ED's DCGT coarse-graining select the Maxwell-action configuration as the continuum expectation of the holonomies?** This paper realizes the topological skeleton of charge, locates the Coulomb field one coarse-graining layer up, and leaves that one question honestly open.

---

## 1. Introduction

### 1.1 What this paper does

The Contrast-First ontology re-classifies physical constants as *global relational facts* rather than free parameters. Electric charge is the load-bearing concrete test: it is discrete, conserved, and topological-looking. This paper asks, **graph-first**, whether the ED participation graph admits a topological invariant that behaves like charge — and, crucially, lets the graph structure decide *which* invariants exist before any comparison to charge is made. It maps the result precisely: which features of charge ED's structure realizes (the topological skeleton), which it withholds at the discrete layer (the determined field), and why.

### 1.2 The discipline (graph-first, never charge-first)

The standing crank-safety rule is reached **graph-first**: let the participation-graph structure force which invariants exist; only then ask whether any behaves like charge. **Never retrofit a topology to hit ±1 or ∓⅓** — that is the failure mode this paper is built to avoid. The integers ±1, ∓⅓ do not appear in any result; an integer winding with *no selected magnitude* does. The FS↔ED parallel and any physics reading are **form/structure only**.

### 1.3 Why it matters

This is the ontology's test on the **confirmation** axis: can ED *earn* "constants are global relational facts" for the one case where the claim is concrete? The honest answer — *the topological skeleton yes, the metric flesh as a coarse-grained limit, with one open question* — is more useful than either a triumphant "ED makes charge" (which it does not) or a flat "ED says nothing about charge" (which undersells a genuine structural realization).

### 1.4 Regime of validity

Every result is for the **certified Σ-rule substrate** on **minimal arenas** — single cycles (rings) for the holonomy/winding, small grids for the Gauss-law and fork tests. **No claim is made about large-scale networks, about multi-cycle interactions, or about coupling between several windings.** The continuum-limit behaviour (whether DCGT yields Maxwell/Coulomb) is **not** a result of this paper but its one declared open question (§7). The contrasts — quantized integer winding, loop-independent circulation, sweep-dependence with vs without P11 — are the result, not absolute magnitudes or large-system claims.

---

## 2. Primitive Inputs and Method

**Substrate primitives (postulated, Paper_087), load-bearing here:** P05 (adjacency transport — the discrete connection), P09 (U(1) polarity — the angle), P11 (commitment irreversibility — single-valuedness and protection), P04 (four-band bandwidth — the weak coupling channel). The defining constraint is that the **Σ-selection is orientation-blind**: Σ reads ρ and graph structure, never the polarity. Concretely: **orientation-blind Σ means the selection rule reads ρ and graph structure *only*; the U(1) phase is invisible to Σ, so the winding cannot influence front propagation *except indirectly*, through the P04 bandwidth tie-break (§4.2).** This single constraint is the reason behind every result below (§6).

**Method (graph-first).** A reconnaissance step asks which topological invariants the participation graph admits at all (independent of charge). The candidate that survives — the U(1) holonomy on cycles — is then probed in four steps: **quantize** (does commitment make the winding integer?), **couple** (can the winding act, given orientation-blind Σ?), **source** (does it obey a Gauss law?), and the **ontology fork** (can a determined local field be forced, and at what cost to ED's invariants?). The certified substrate is used as-is; deviations in the fork (relaxing orientation-blindness; removing P11) are explicit and labeled. Scripts: `holonomy_test.py`, `coupling_test.py`, `sourcing_test.py`, `relaxation_test.py`.

**No primitive forcing is invoked**, and no topology is fit to a charge value.

**Reproducibility.** Step 1 (quantization) uses minimal U(1)-on-a-cycle arenas (rings): the holonomy is the summed per-edge phase difference `Σ_e Δφ_e` around the cycle, and the winding `w = (1/2π) Σ_e Δφ_e` is read after the polarity is committed single-valued (P11); quantization to `ℤ` is exact to machine precision. Step 3 (Gauss law) measures the same circulation on enclosing loops of varying length and shape on a grid, checking `Σ_{e∈L} Δφ_e = 2πw` independent of the loop. Step 4 (the fork) relaxes the per-edge phase on an `S×S` grid carrying a central winding: *sweep-dependence* is the variation of the converged per-edge configuration under different update orderings (0.76, with orientation-blindness relaxed and P11 kept), and the *isotropic-field* test fits the radial deficit, reporting `deficit·r²` (≈ 0.126, initialization-independent to 0.0005) — which appears only when P11 is *also* removed. Scripts: `holonomy_test.py`, `coupling_test.py`, `sourcing_test.py`, `relaxation_test.py`.

---

## 2.5 Load-Bearing Step Audit

| Step | Status | Source / justification |
|---|---|---|
| 13 primitives postulated | P | Paper_087 |
| Graph admits a continuous U(1) holonomy on cycles | **measured** | §3 — recon; ρ ruled out, b₁ arena, Z₂ too coarse |
| Quantized winding `w ∈ ℤ` (`π₁(U(1))=ℤ`) | **measured** | §4.1 — to machine precision (P09 + P11) |
| Conserved, irreversibility-protected | **D** | §4.1 — slipping requires uncommitting (P11 forbids) |
| Weak `w`-indexed bandwidth coupling `cos²(πw/N)` | **measured** | §4.2 — P04; no Σ-level coupling (orientation-blind) |
| Integral Gauss law: circulation `= 2πw`, loop-independent | **measured** | §4.3 |
| No determined local field at the discrete layer | **measured** | §5 — per-edge gauge/sweep-dependent |
| Determined `1/r²` only if orientation-blindness **and** P11 removed | **measured** | §5 — `deficit·r²≈0.126`; then it is not ED |
| Orientation-blindness is the single reason throughout | **D-structural** | §6 |
| Holonomies = lattice gauge link variables; Coulomb = continuum limit | **interpretation (reframe)** | §7 — standard lattice→continuum dictionary |
| Maxwell-like action latent in `cos²(Δφ/2)` | **D-structural** | §7 — continuum form is `∫(∇φ)²`-type |
| DCGT yields Maxwell/Coulomb | **OPEN — not claimed** | §7 |
| ED derives electromagnetism / charge values | **NOT CLAIMED** | preamble 2–3 |

All steps P, D, measured, structural, interpretation, open, or explicitly not-claimed. *The positive results are measured graph-first; the Coulomb-field "absence" is a discrete-layer fact reframed (not a deficiency); the one open item is labeled open.*

---

## 3. Reconnaissance: Which Invariants the Graph Admits

Before any comparison to charge, the question is what topological invariants the participation graph carries. The event-density field ρ supports none of the right kind (it is a scalar deposit, not a connection). The graph's first Betti number `b₁` (independent cycles) is the arena for holonomy. A `Z₂` invariant is too coarse. What survives is the **continuous U(1) holonomy on cycles** — the holonomy of the discrete U(1) connection given by P05 transport carrying the P09 angle. This is the only candidate, and it was reached without reference to charge.

*Why U(1)?* It is the simplest non-trivial continuous group, and `π₁(U(1)) = ℤ` makes its holonomy *automatically* integer-quantized — so it is the natural candidate for a discrete, conserved, charge-like invariant, and (on this graph) the only surviving one. Nothing about charge is assumed in choosing it; it is what the cycle structure of the participation graph supports.

---

## 4. The Topological Skeleton

### 4.1 Quantize — an integer winding, conserved and protected

On a minimal U(1)-on-a-cycle arena, single-valued committed polarity (P09 angle made single-valued by P11 commitment) forces the holonomy around the cycle to an **integer winding `w ∈ ℤ`** — exactly `π₁(U(1)) = ℤ`, confirmed to machine precision. The winding is **conserved**: it cannot change continuously, and changing it discretely would require "uncommitting" a polarity, which **P11 irreversibility forbids**. So the winding is a quantized, conserved, **irreversibility-protected** topological invariant — the first and most charge-like feature. *(**Scope note added 2026-09-12.** This is the claim that `w` cannot **change** while its cycle exists, established on fixed ring arenas. It is not the claim that the cycle itself persists. The winding is the holonomy of a loop of **live participations** — P02 makes participation the time-indexed four-tuple `(C, K, u, t)`, and P09 hangs polarity on each channel-locus participation — so where participation ceases there is no phase to difference and the invariant has no carrier, with nothing uncommitted and P11 respected. Load-bearing downstream: `Paper_ED_CCC` §3.6.1 uses exactly this to clear residual charge at the contrast-zero limit. A dissolving-arena test is not runnable on the certified engine, which enforces monotone commitment with no release channel.)* It is, however, **inert** at the Σ level: orientation-blind Σ never reads the phase, so the winding has no direct dynamical effect.

### 4.2 Couple — weakly, through bandwidth

Can the inert winding act at all? Only weakly, and only through the P04 bandwidth channel: the coherence bandwidth carries a discrete `w`-indexed ladder, `∝ cos²(πw/N)`. There is **no strong or Σ-level coupling** — again because Σ is orientation-blind. So the winding influences the substrate only through the weak bandwidth tie-break, never through the selection rule.

### 4.3 Source — an integral Gauss law

Does the winding source a field? It obeys the **integral content of Gauss's law**: the circulation of the connection around *any* enclosing loop equals `2πw`, **independent of the loop's size and shape**. Explicitly, for any simple closed loop `L` on the graph the discrete holonomy satisfies

$$
\sum_{e \in L} \Delta\phi_e = 2\pi w,
$$

the *same* integer `w` for every enclosing `L`, regardless of its length or shape. This is the unscreenable, topological statement of charge-sourcing — the flux through any surface enclosing the winding is fixed by `w` alone. It is genuine and graph-native.

What is **not** present is a *determined local field* — a per-edge `1/r²` configuration. The circulation is fixed (topological), but how it distributes over individual edges is undetermined at the substrate (§5).

---

## 5. The Ontology Fork: the Metric Flesh is Withheld at the Discrete Layer

Step 3 leaves the local field undetermined; can it be *forced*? We relax ED's invariants one at a time:

- **Relax orientation-blindness alone** (Σ now sees coherence; P11 kept): the result is a **sweep-dependent seam, not a field** — the local configuration depends on the order of evaluation (sweep-dependence 0.76). No determined field.
- **Also remove P11 irreversibility:** a determined isotropic `1/r²` field appears (`deficit·r² ≈ 0.126`, initialization-independent to 0.0005) — but this is now ordinary XY/lattice-field relaxation. **It is no longer ED.**

**To state the fork unambiguously: the isotropic `1/r²` deficit profile appears *only* when *both* orientation-blindness and P11 are removed; with *either* invariant intact, no determined local field appears.** And the sweep-dependence of the intermediate case is the discrete analogue of **gauge redundancy** — the per-edge values are not physical, only the loop holonomies are (developed in §7).

So a determined local Coulomb field is blocked by **two** invariants — orientation-blind selection *and* irreversible commitment — and producing one requires abandoning both. At the discrete layer, the metric flesh is outside ED.

---

## 6. The Complementarity

The single reason runs through every step: **the Σ-selection is orientation-blind.** That one invariant is what makes the winding quantized-but-inert (Step 1), weakly-coupled (Step 2), Gauss-law-sourcing-but-locally-undetermined (Step 3), and unforceable-into-a-field (Step 4). And it is the *same* invariant — together with P11 — that makes ED a **determinacy engine** in the first place (orientation-blind, irreversible commitment is what produces definite facts). So ED's two signature commitments are *precisely* what realize the topological skeleton of charge **and** *precisely* what withhold a determined continuous field at the discrete layer. The same architecture does both: this is complementarity, not deficiency.

---

## 7. The Honest Open Edge: Lattice Gauge Theory and the Coulomb Continuum Limit

§5's "the field is outside ED by construction" contains a layer error worth correcting surgically — and the correction *preserves every discrete result* while converting a dead end into a well-posed problem.

**The holonomies are lattice gauge link variables.** The discrete U(1) holonomies, the Wilson loops, the integral Gauss law — that is exactly the **lattice layer of a U(1) gauge theory**. The continuous electromagnetic field (`A_μ`, `F_{μν}`, the Coulomb `1/r²`) is the **known continuum limit** of those link variables. So the Coulomb field was never a substrate object: it lives at the coarse-grained (DCGT) layer, and demanding it on the graph is the same mistake as demanding a smooth metric on a single event.

*Disclaimer.* This paper does **not** claim ED *implements* lattice gauge theory, or that the substrate *is* a gauge theory. The correspondence is **structural** — used only to *locate* the continuum field one layer up and to recognize the per-edge ambiguity as ordinary gauge freedom. No gauge-theory dynamics are imputed to ED. (The lattice→continuum dictionary used here is the standard one — Wilson's lattice gauge theory, 1974 — with Dirac's 1931 charge-quantization-from-topology and the topological charge of XY/`O(2)` models as the conceptual lineage for "charge as winding.")

**Step 3's "undetermined local field" is ordinary lattice gauge freedom.** Per-link configurations in lattice gauge theory are gauge-dependent (individually unphysical); the physical, *determined* object is the gauge-invariant, action-selected configuration. ED's "sweep/gauge-dependence" is exactly that redundancy — expected, not a failure.

**The Maxwell-like action is already latent.** Why is the configuration undetermined *at the substrate*? Because the physical continuum field is selected by an **action**, and orientation-blind Σ supplies no action over the phase. But the relevant action is already present in P04's coherence structure: the coherence energy `b_e = cos²(Δφ_e/2)` (incoherence `sin²(Δφ_e/2)`) has the continuum form of an `∫(∇φ)²`-type (Maxwell/XY-like) action. Explicitly, in the continuum limit `cos²(Δφ_e/2) ≈ 1 − ¼(Δφ_e)²`, so the incoherence `sin²(Δφ_e/2) ≈ ¼(Δφ_e)² → ¼(∇φ)²` is exactly the standard `∫(∇φ)²` action density. **ED has the right action latent; orientation-blind Σ simply does not minimize it at the micro layer.**

**The corrected open problem (unproven; no Maxwell derivation claimed).** In lattice gauge theory the action's selection happens at the **ensemble / coarse-grained** level: the determined field is the gauge-invariant expectation of the link variables, dominated by low-action (coherent) configurations. So the ED-native question is:

> **Does ED's DCGT coarse-graining produce Maxwell/Coulomb as the continuum limit of the discrete holonomies — i.e., is the DCGT measure coherence-weighted enough to select the Maxwell-action configuration as the continuum expectation?**

If so, the continuum field emerges as a **coarse-grained statistical fact, with orientation-blindness untouched** — the selection occurs at the ensemble layer, not in the micro rule. This *replaces* "ED would have to break its invariants" with "the field is obtained by coarse-graining, the same machinery ED uses for the emergent metric." **It is unproven, and this paper claims no Maxwell derivation.** It is the honest open edge.

---

## 8. Relation to the Program

This is one instance of the program's single deepest open thread. The determined continuous structure — **the field (here), the metric (the gravity arc), the boundary (emergent horizons), the diffusion PDE (the continuum-limit result)** — is in every case the coarse-grained shadow, and the live question is always the same: *does ED's coarse-graining supply it?* Charge is the **cleanest** instance, because the lattice→continuum dictionary (lattice gauge theory) is already standard, so the open question is unusually sharp: not "what continuum object should appear?" but "does the DCGT measure select the known one?"

---

## 9. Limitations (honest)

- **The discrete skeleton is genuine; the continuum field is open.** Every discrete result (winding, conservation, protection, integral Gauss law) is solid; the Coulomb continuum limit is unproven, and no derivation is claimed.
- **No magnitudes, no spectrum.** ED produces an integer winding with no selected magnitude — not the ±1, ∓⅓ charge spectrum, not the SM content, not the fine-structure constant.
- **Minimal arenas, one certified substrate.** The contrasts (integer winding; loop-independent `2πw`; sweep-dependence with vs without P11) are the result, not absolute magnitudes.
- **Form/structure only.** The winding is a structural realization of charge's topological skeleton, not a claim that it *is* electric charge.

---

## 10. Falsification Criteria

### 10.1 The winding is not integer / not conserved

**Falsifier sentence:** *A demonstration that the committed-polarity holonomy is not quantized to `w ∈ ℤ`, or that the winding can change without an uncommitting (violating P11 protection), would falsify §4.1 and the topological-skeleton claim.*

### 10.2 The Gauss law is loop-dependent

**Falsifier sentence:** *A measurement showing the circulation around enclosing loops is not `2πw` independent of loop size/shape would falsify the integral Gauss law (§4.3).*

### 10.3 A determined field appears without breaking ED

**Falsifier sentence:** *Producing a determined local `1/r²` field while keeping both orientation-blindness and P11 — i.e. without leaving ED — would falsify the §5 fork and the complementarity claim (§6).*

### 10.4 The reframe fails: DCGT does not yield Maxwell

**Falsifier sentence:** *A demonstration that ED's DCGT coarse-graining of the holonomies provably cannot yield Maxwell/Coulomb (the DCGT measure is not coherence-weighted enough to select the Maxwell-action configuration) would close the §7 open edge negatively — returning charge to the "skeleton only, no continuum field even in the limit" verdict.*

### 10.5 A retrofit charge spectrum

**Falsifier sentence:** *Any result reproducing the ±1, ∓⅓ charge spectrum would, if reached by fitting a topology to those values rather than graph-first, violate the discipline of this paper (§1.2) — and is explicitly not claimed.*

---

## 11. Position Statement

**ED realizes the topological skeleton of electric charge and locates the Coulomb field one coarse-graining layer up.** Reached graph-first: committed U(1) polarity (P09 + P11) gives a quantized, conserved, irreversibility-protected **integer winding** that couples weakly through bandwidth (P04) and obeys an **integral Gauss law** (`2πw`, loop-independent) — the topological skeleton. The determined local Coulomb field is **not** a discrete-layer object; forcing one requires abandoning both orientation-blindness and P11, i.e. ceasing to be ED. Read as lattice gauge theory, this is exactly right: the holonomies are link variables, the Coulomb field is their continuum limit, and the Maxwell-like action is latent in the coherence term.

**What this paper claims.** ED's participation-graph structure forces a topological invariant with charge's *skeletal* features (quantized integer winding, conservation, irreversibility protection, an integral Gauss law), by the single invariant of orientation-blind selection — and that same invariant withholds a determined continuous field at the discrete layer, where it correctly does not live.

**What this paper does not claim.** ED does not derive electromagnetism, Maxwell, or the Coulomb field; it produces no charge magnitudes, no spectrum, no fine-structure constant; the winding is inert and weakly coupled; and whether DCGT coarse-graining yields Maxwell/Coulomb in the continuum limit is the **honest open edge** — unproven, no derivation claimed.

**Series context.** The cleanest instance of the program's deepest open thread (the determined continuum as coarse-grained shadow), because the lattice→continuum dictionary is already standard. Companion to the continuum-limit and finite-memory-ceiling substrate-evaluation results.

---

## Appendix — Artifacts and Glossary

### Artifacts (certified substrate; `evaluation/B4_Arc/`)

- `holonomy_test.py` — Step 1 (U(1)-on-a-cycle; winding quantization to `ℤ`).
- `coupling_test.py` — Step 2 (`w`-indexed bandwidth ladder `cos²(πw/N)`).
- `sourcing_test.py` — Step 3 (integral Gauss law; circulation `= 2πw`).
- `relaxation_test.py` — Step 4 (ontology fork: relax orientation-blindness / P11; sweep-dependence; `1/r²` only off-ED).
- `docs/B4_Round5_Reframe_LatticeToContinuum.md` — the lattice-gauge reframe (§7).

### Glossary

- **Holonomy.** The total phase a U(1) connection accumulates around a closed loop — here the summed per-edge phase difference `Σ_{e∈L} Δφ_e`; its `1/2π` multiple is the integer winding.
- **Winding `w ∈ ℤ`.** The integer holonomy of the committed U(1) polarity around a cycle (`π₁(U(1)) = ℤ`); quantized, conserved, irreversibility-protected — the topological skeleton of charge.
- **Integral Gauss law.** Circulation around any enclosing loop `= 2πw`, loop-independent — the topological/unscreenable content of charge-sourcing.
- **Orientation-blind Σ.** The Σ-selection reads ρ and graph, never the polarity — the single invariant that realizes the skeleton and withholds the field.
- **Metric flesh.** A determined continuous local field (Coulomb `1/r²`); a coarse-grained object, not a discrete-layer one.
- **Latent Maxwell action.** The coherence term `cos²(Δφ/2)`, whose continuum form is the `∫(∇φ)²`-type Maxwell/XY action — present in P04 but not minimized by orientation-blind Σ at the micro layer.
- **The open edge.** Whether ED's DCGT coarse-graining selects the Maxwell-action configuration as the continuum expectation of the holonomies — unproven; no Maxwell derivation claimed.

### Reader map and open work

*Intuition — why charge is topological here.* Charge is topological because the phase must return to itself after going around a loop; ED's irreversible commitment (P11) makes that return **single-valued**, and `π₁(U(1)) = ℤ` makes it **quantized**. The winding counts how many times the committed phase wraps — an integer that cannot change without uncommitting.

**Where to look next.**
- *The continuum-limit question in general (does coarse-graining supply the determined object?):* the Continuum paper and the gravity arc.
- *The same coarse-graining wall for the metric:* GR-II.
- *The internal determinability ceiling:* the A1 result.

**Open work** (declared): the **DCGT → Maxwell test** — does the coherence-weighted continuum measure select the Maxwell-action configuration (§7)?; multi-cycle / multi-winding interactions; coupling of the winding to matter (ρ) fronts; and whether gauge *potentials* (`A_μ`) emerge alongside the field in the continuum limit.

---

**End of Paper (Charge as Topology).**

*Substrate-evaluation arc. ED realizes the topological skeleton of charge — quantized integer winding (`π₁(U(1))=ℤ`), conserved, irreversibility-protected, integral Gauss law `2πw` — by the single invariant of orientation-blind selection, and withholds the determined Coulomb field at the discrete layer (forcing one requires leaving ED). Read as lattice gauge theory the holonomies are link variables and the Coulomb field is their DCGT continuum limit, with the Maxwell-like action latent in the coherence term; whether the DCGT measure selects it is the honest open edge. Graph-first throughout; no charge values, no Maxwell derivation, claimed.*
