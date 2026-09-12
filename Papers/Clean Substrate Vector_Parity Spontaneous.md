# The Clean Substrate Is Vector: Parity Violation in Event Density Is Necessarily Spontaneous, and the Weak Force's Chirality Is Inherited
Allen Proxmire
2026


---

> **Review note (2026-09-12).** The text below is the corpus copy, unchanged. These corrections come from a review of this repository and take precedence over it.
>
> - **The §4 theorem is correct.** As §4 itself says, it is the statement that a parity-symmetric model carries no parity-odd invariant, applied to this commitment-map model.
> - **§3's "N = 1 is forced vector, matching electromagnetism" misidentifies the abelian factor.** The Standard Model's fundamental abelian gauge factor is hypercharge $U(1)_Y$, and hypercharge is chiral: left- and right-handed fermions carry different hypercharge. Unbroken electromagnetism is vector, but it is not the fundamental abelian factor. So this capability claim is in tension with observed physics.
> - **§5's pseudoreality of $SU(2)$ is speculation.** It is not an established explanation of why the weak force is chiral.
> - **§7's prediction has no stated way to measure it.** The claim that handedness is spontaneous and correlated with the matter/antimatter sign comes with no method for testing it.

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **This paper does not derive the weak force's chirality.** *Which* force couples to one handedness (the "casting") is found to be a **representation-theoretic fact, inherited, not derived.** The paper strengthens the parity wall and grounds its operator; it does not breach it. The verdict remains: parity violation is inherited.
2. **The central positive is a theorem about the *clean* substrate at the transport level, plus a grounded operator.** The theorem: the parity-symmetric substrate is **vector for every channel-count** (proven at the channel-transport level; the relativistic descent to the full Dirac sector is open, §8), from which its corollary follows, *if* parity is violated its direction is **necessarily spontaneous** (a symmetry-breaking, not a law). This is a statement about the substrate's structure, not a derivation of the Standard-Model matter content.
3. **Every claim is tiered.** The clean-vector winding result is **derived** (a proof). The chirality operator `γ⁵ = arrow × orientation` is **structural**. The attribution of the casting to representation theory (the pseudoreality of `SU(2)`) is the **surviving candidate** (account tier), consistent with a companion computation, not a fresh proof. The stability formalism is a **definition**; the full representation spectrum is **not** computed here.
4. **It supersedes only the *tier* of the earlier verdict, not its direction.** *The Parity Wall* concluded "vector-default, P inherited" conditionally; this paper reaches the same direction with a theorem and a built operator. It is consistent with the retired first-arrival "C and P" over-read (the P-half stays retired; see §7).
5. **It introduces no new substrate primitives**, and it claims no charge magnitudes, no representation spectrum, no masses or mixings.
6. **Credit.** The lane-parity picture of the capability structure (§3) and the spontaneous-orientation route to the chirality operator (§2) are due to A. Proxmire; they are marked where used.

---

## Abstract

Does Event Density's substrate produce the weak force's parity violation, or inherit it? *The Parity Wall* answered "inherited," but conditionally: vector "by default," for a "minimal construction," with the deciding channel-topology program unbuilt. This paper builds that program and hardens the verdict into a theorem, while grounding the chirality operator the earlier paper found missing. Three results. **First, the chirality operator is grounded:** `γ⁵ = i γ⁰ γ¹γ²γ³` reads in ED as `(the arrow) × (the spontaneous spatial orientation)`, both factors native and established, which reconciles the earlier "no local screw" finding (`γ⁵` is not a per-channel feature) with a *global* orientation that is provably spontaneous (the parity-clean rules cannot fix a handedness) and single-valued across the causal patch (the substrate has no reflection to make its emergent space non-orientable). **Second, the clean substrate is vector at the channel-transport level, as a theorem.** Modelling a family of `N` channels as a commitment map `H(k) = e^{ik} A + e^{-ik} B`, parity-cleanness (parity is a symmetry) forces the backward hop to mirror the forward hop, `B = S A S⁻¹` with `S` the lane reflection, which makes `det H(k)` an even function of `k`; the point-gap winding that would mark a chiral coupling therefore vanishes identically, for every `N` and every `A`. So the clean transport carries no net chirality at any channel-count, and any parity violation must break the parity symmetry, i.e. its direction is **necessarily spontaneous** (a transport-level result; the relativistic descent to the full Dirac sector is the standing open arc, §8). **Third, the casting is inherited.** The winding is zero in the clean substrate and grows monotonically with `N` when the symmetry is broken; the Standard Model's *non-monotone* pattern (vector, chiral, vector for one, two, three channels) matches neither, so *which* force is chiral is not a transport-dynamical fact. It is the representation-theoretic fact that `SU(2)`'s fundamental is pseudoreal while `SU(N \geq 3)`'s are complex, inherited exactly as the gauge-group multiplicities and the constants are. Two facets of the one parity-cleanness fact, the coupling geometry and the arrow-driven stability, both supply the *capability* for chirality and both miss the *selection*, consistent evidence that the casting is genuinely not an ED output. The clean-vector theorem also fixes the anomaly baseline: a vector theory is automatically anomaly-free, so the clean substrate carries no gauge anomaly, and the nontrivial cancellation of the chiral Standard Model is inherited with its content. Net: a substrate that builds the entire *stage* of chirality (the operator, its spontaneity, its capability) and inherits the one *assignment*, with a sharpened, falsifiable prediction, parity violation is a spontaneous, contingent orientation correlated with the matter/antimatter sign, against the Standard Model's law-level fixed handedness.

---

## 1. Introduction: What *The Parity Wall* Left Open, and What Closes It

*The Parity Wall* reduced the weak force's chirality to a single geometric quantity, a "screw pitch," and found the minimal primitives do not force it: the emergent fermion is **vector by default**. It was careful to tier that as conditional, and it named three things it left open: (i) the chirality operator itself was undefined (there was no grounded `γ⁵`); (ii) the verdict held "for the minimal construction," with the full channel-topology program unbuilt, so "vector forever" was explicitly not claimed; and (iii) *why* the weak force specifically, the assignment, had no mechanism, only the word "inherited."

This paper closes all three, in the honest direction. It **grounds the operator** (§2), it **builds the channel program and proves the clean substrate vector for every channel-count** (§4), and it **names the assignment's origin** (§5, representation theory). The verdict's *direction* is unchanged, parity violation is inherited, but its *tier* rises from "default, conditional, unbuilt" to "theorem, plus a grounded operator, plus a named inherited mechanism." Along the way it upgrades a stance into a theorem: parity violation in ED is *necessarily spontaneous*.

The reader map: §2 grounds `γ⁵`; §3 gives the capability structure (the lane picture); §4 is the theorem; §5 places the casting where it lives (inherited); §6 draws the anomaly corollary; §7 states the verdict and the prediction; §§8–10 give limitations, falsifiers, and the position.

### 1.5 Load-Bearing Step Audit

| Claim | Tier | Source / justification |
|---|---|---|
| `γ⁵ = arrow × spatial orientation` | **structural** | §2, standard definition read in ED terms; both factors native |
| The orientation is spontaneous | **derived** | §2.1, parity-clean rules cannot fix a handedness |
| The emergent space is orientable (within the causal patch) | **structural** | §2.2, no reflection primitive, so no orientation-reversing holonomy |
| Capability split (N=1 vector, N≥2 chiral-capable) | **derived-conditional** | §3, the reflection-odd coupling sector, empty only at N=1 |
| **Clean substrate is vector for every N (transport level)** | **derived (theorem)** | §4, `det H(k)` even in `k` ⟹ winding `\equiv 0` |
| If parity is violated, its direction is necessarily spontaneous | **derived (corollary)** | §2.1 + §4, chirality requires breaking the parity symmetry |
| Rule-type = attractor of the commitment map | **definition** | §4, method framing; full spectrum not computed |
| The casting is representation-theoretic (inherited) | **account (surviving candidate)** | §5, non-monotone SM pattern matches no transport winding |
| Clean substrate is anomaly-free | **structural (contingent on the substrate→Dirac reduction)** | §6, vector theories carry no gauge anomaly |
| The nontrivial (chiral) anomaly cancellation is inherited | **inherited / wall** | §6, downstream of the inherited content |
| "ED derives the SM matter content" | **NOT CLAIMED** | preamble 1, 5 |

---

## 2. The Chirality Operator, Grounded: `γ⁵ = (the arrow) × (the spontaneous orientation)`

*The Parity Wall* found no per-channel "screw." That finding was correct, and it is explained here: the chirality operator is not a per-channel object at all. The Dirac chirality operator is, by definition, `γ⁵ = i γ⁰ γ¹ γ² γ³`. Read its two factors in ED's terms.

- **`γ⁰` is the arrow.** ED's timelike direction is the commitment order, the arrow (P11, retarded-only transport). `γ⁰` *is* ED's process primitive.
- **`γ¹γ²γ³` is the spatial orientation.** The product of the three spatial gamma matrices is the oriented volume element; the choice of `γ¹γ²γ³` versus `γ¹γ³γ²` *is* a handedness of the 3-frame, and under a spatial reflection it flips sign, the parity-odd object, as it must be.

So `γ⁵ = i \cdot (\text{the arrow}) \times (\text{the spatial orientation})`. Both factors are native and established, which grounds the chirality operator in ED's own structure. This **reconciles** the earlier results: *The Parity Wall* looked for chirality in a *local* screw and correctly found none, because `γ⁵` is a *global* object, the arrow times a global orientation. The apparent dead end (no local screw) and the operator's existence fit together here. It also updates the matter-sector headline (MS-II §4.2, which located `γ⁵` as a per-channel channel-topology "screw class," at account tier): the operator is not per-channel but global, the arrow times the one global orientation, which is why no per-channel screw was ever found. It also gives the matter/antimatter (C) and parity (P) references a shared basis: `γ⁵` literally contains the arrow (the C-side ingredient, which sets matter over antimatter) and the orientation (the P-side ingredient), so the two are attributes of one operator, both set at the arrow's early action. Tier: structural (the definition of `γ⁵` is standard; the ED content is that both factors are native).

The operator is only as physical as its orientation factor is real. Two properties, both provable, make it so.

### 2.1 The orientation is spontaneous *(derived; credit AP for the route)*

ED's rules are parity-symmetric: no primitive is a reflection. A parity-symmetric rule set cannot fix a handedness, so any global orientation the substrate carries is chosen by **spontaneous symmetry breaking**, not written into the law. This is exactly a ferromagnet picking a direction: the dynamics is rotation-symmetric, the ground state is not. The payoff is twofold. It grounds the paper's distinctive prediction (parity violation, if orientational, is *necessarily* a spontaneous, contingent choice), and it removes the obstruction that killed the earlier "select a handedness from an ensemble" routes, spontaneous breaking is a single global choice, not an average over a racemic ensemble, which parity-symmetric dynamics produce routinely.

**This route is distinct from the two parity routes *The Parity Wall* closed, and survives where they did not.** That paper retired a *first-commitment pseudoscalar* (its Route 3: selecting a point on the internal P09 phase circle is parity-inert, so it gives a matter/antimatter reference, not a handedness) and measured a *diastereomeric coupling* to null (its Route 4: `κ_h ≈ 0` on the V5 all-pairs coherence). The order parameter here is neither. It is the **orientation of the emergent 3-frame itself** (the `γ¹γ²γ³` factor), a genuinely parity-odd spatial object, chosen by symmetry breaking. It is not an internal phase (so it is not parity-inert like Route 3), and it is not an energetic handedness bias that must be amplified from a racemic mix (so the null of Route 4 does not touch it): a single spontaneous orientation choice needs no diastereomeric energy difference and no ensemble average. So the retired first-commitment P-half stays retired (its mechanism really was parity-inert), while parity is reintroduced here through a different, spatial, order parameter that the earlier probes never tested.

### 2.2 The emergent space is orientable *(structural, within the causal patch)*

A single global orientation exists only if the emergent 3-space is orientable. It is, by the same parity-cleanness. Orientability fails only if a reflection (determinant `-1`) is built into the frame bundle somewhere (the Möbius identification is the canonical example). ED's transport is a continuous, invertible connection, hence a proper rotation (in the identity component, determinant `+1`), and a holonomy around any loop is a product of such proper transports, hence itself proper; and no primitive is a reflection. All-proper frame relations give an orientable space. **ED cannot build a non-orientable space; it has no reflection in its toolkit.** The same fact does double duty: no reflection primitive makes the orientation spontaneous (§2.1) *and* makes the space orientable (here). Growth from a single seed then propagates one orientation across the causal patch, a single global handedness, not a patchwork.

So the chirality operator is real: `γ⁵` = the arrow times a genuine, spontaneously chosen, globally consistent orientation.

---

## 3. Capability Versus Selection: the Lane Picture at the Operator Level *(derived-conditional; credit AP)*

Having a defined `γ⁵` is not yet parity violation. Parity violation is the dynamics treating the two `γ⁵` eigenspaces differently. The question splits, cleanly, into *capability* (is there a genuine left/right to couple to at all?) and *selection* (does the dynamics use it?). A highway picture (AP) captures the capability exactly: in one lane there is no left or right; in the middle of three lanes the two sides are mirror-symmetric, again no net handedness; in two lanes there is a genuine left and right. Made precise, the spatial reflection (the orientation factor of `γ⁵`) acts on the set of `N` channels, and a parity-clean coupling that references the orientation must live in the **reflection-odd** part of the gauge structure. Counting that part:

- `N = 1` (a single channel, abelian): the reflection-odd sector is **empty**. There is no orientation-referencing coupling to build, so the coupling is **forced vector**. This matches electromagnetism (abelian, vector).
- `N \geq 2`: the reflection-odd sector is **nonempty**, so a chiral coupling is **possible**. There is a genuine left/right to couple to.

This delivers the *capability* and only the capability. A nonempty reflection-odd sector means a chiral coupling *can* exist; it does not force one. That distinction is the whole content of the wall: the geometry says whether the highway has a left and a right lane; it does not say whether the universe drives in one of them. The "which lane" is the selection, and §§4–5 show it is not an ED dynamical output.

One honest caution, stated so it is not over-read: the capability count singles out `N = 1` (forced vector) cleanly, but among `N \geq 2` it does not by itself distinguish two channels from three (both have a nonempty reflection-odd sector). The even/odd reading of the lane picture is an intuition pump that matches the three Standard-Model forces but does not generalize as a rule; the genuine distinction that makes two channels special is representation-theoretic (§5), not a parity-of-`N` fact.

---

## 4. The Theorem: the Clean Substrate Is Vector for Every Channel-Count

The capability structure leaves the selection open. This section settles the clean-substrate side of it, and the answer is a theorem.

**The object.** Model a family of `N` channels as a commitment map on a one-dimensional emergent chain, `H(k) = e^{ik} A + e^{-ik} B`, where `A` is the forward (arrow-directed, retarded) cross-channel hop, `B` the backward hop, and `k` the emergent-space wavenumber. The chirality of such a map is measured by its **point-gap winding**, the number of times `det H(k)` winds around a reference as `k` runs over its period; a nonzero winding is the net-chirality signature (the one the earlier toy computations exhibited only for one-way, arrow-carrying hopping), a zero winding is vector.

**The constraint the substrate forces.** ED's substrate is parity-clean, so parity is a symmetry. Parity is the spatial reflection `k \to -k` together with the lane reflection `S` (the reversal `i \mapsto N{+}1{-}i` of the channel row). For `H` to be parity-symmetric, `S H(k) S^{-1} = H(-k)`, which forces the backward hop to be the mirror of the forward hop:

$$ B = S A S^{-1}. $$

`A` (the retarded forward hop, the arrow acting on the channel connection) is the only free structure; `B` is then fixed by parity-cleanness, not chosen.

**The theorem.** With `B = S A S^{-1}`,

$$ S\,H(k)\,S^{-1} = e^{ik} S A S^{-1} + e^{-ik} S B S^{-1} = e^{ik} B + e^{-ik} A = H(-k), $$

so `\det H(k) = \det H(-k)`: the determinant is an **even** function of `k`. As `k` runs over its period the determinant path traces out and then retraces itself, so it encircles no reference point. **The point-gap winding is identically zero, for every `N` and every forward hop `A`.**

The theorem's role is to make precise, and to verify by direct computation, what parity symmetry already guarantees in the abstract: a parity-symmetric object carries no parity-*odd* invariant, and chirality is parity-odd. The mathematical step is short (an even determinant retraces its path), and it deliberately is: the substantive, load-bearing content is in the two inputs, that ED's clean substrate is parity-symmetric of this commitment-map form, and that the point-gap winding is the operative chirality invariant. Both are modelling inputs (the first established, the second the standard non-Hermitian chirality invariant); neither is derived by the theorem. What the theorem adds over "parity symmetry forbids a parity-odd term" is that it holds for *every* channel-count with no exception, verified numerically, which is exactly the generality *The Parity Wall*'s minimal-construction verdict lacked.

> **The parity-clean substrate carries no net chirality at any channel-count.** The parity-odd invariant that would mark a chiral coupling vanishes identically. The clean substrate is vector for one channel, two channels, three channels, all of them.

This was checked numerically as a control on the proof (`evaluation/ChiralGauge/rep_spectrum_casting_winding.py`): for `N = 1` through `6`, over many random forward hops `A`, the parity-clean winding is `0` in every case, matching the theorem.

**Corollary, the strong positive.** Since the clean transport is vector, any parity violation must break the parity symmetry, that is, it must come from the spontaneous orientation choice of §2.1. **If parity is violated in ED, its direction is necessarily spontaneous.** (ED does not derive *that* parity is violated, that is the inherited casting, §5; it establishes that the direction, if there is one, cannot be a law-level handedness written into the rules, because the rules cannot carry one, but is a contingent, symmetry-broken choice.) This is the earlier papers' stance, now a theorem.

**Method note (the stability framing).** The commitment map is the linearization of ED's actual process: a chain commits, a channel is selected, irreversibly (P11). A persistent particle is then a **stable pattern of that process**, an attracting fixed point of the (non-invertible, hence non-Hermitian) commitment map, "a stable pattern of the happening" rather than a static shape. In that framing the casting is exactly the point-gap winding of the map's linearization, which is what §4 computes and §5 reads off. The framing is stated as a definition; the full enumeration of stable patterns (the representation spectrum) is not carried out here, and its discreteness comes from topology (spin, charge quantization, the family-size bound), not from stability, which is the selection filter, not the source of the list.

---

## 5. The Casting Is Inherited: Representation Theory, Not ED Dynamics *(account, surviving candidate)*

The theorem gives the clean baseline (vector) and its breaking (spontaneous). It does not, by itself, say *which* channel-count ends up chiral once the symmetry is broken. The companion computation settles that it is not fixed by the transport at all.

The winding is `0` in the clean substrate (the theorem). Under a natural breaking of the parity symmetry (a one-way arrow that no longer mirrors under `S`), the winding is `N`, one per channel, monotone in the channel-count. The Standard Model's actual pattern is **non-monotone**: one channel vector (electromagnetism), two channels chiral (the weak force), three channels vector (the strong force). A non-monotone pattern matches **neither** the clean winding (`0`) nor the broken winding (`N`). So *which* force is chiral is not a transport-winding fact.

Where it does live is representation theory. The distinguished feature of the two-channel case is that the fundamental representation of `SU(2)` is **pseudoreal**, while the fundamentals of `SU(N \geq 3)` are **complex**, an "`N = 2` is special" fact, not a parity-of-`N` fact. This is the genuine invariant behind the lane picture's correct hit on the two-channel case, and it is a fact of representation theory that ED **inherits**, exactly as it inherits the gauge-group multiplicities and the fundamental constants. The wall stands; the paper's contribution is to name what is behind it.

Two facets of ED's one parity-cleanness fact reach this same boundary. The **coupling geometry** (§3) supplies the capability and is permissive (a nonempty reflection-odd sector for every `N \geq 2`, selecting nothing further). The **arrow-driven stability** (§4) supplies the clean-vector theorem and is likewise silent on the selection (winding `0` clean, monotone broken). These are not two independent confirmations, they are the same input (the lane reflection `S` is a symmetry) applied to two different objects, the generator algebra and the transport determinant, a consistency check rather than corroboration from an unrelated quarter. That this one fact, read two ways, delivers the *capability* but not the *selection* is what makes the honest reading clear: ED builds the stage and inherits the one assignment.

---

## 6. Anomaly-Freedom: the Clean Baseline Is Automatic; the Chiral Cancellation Is Inherited *(structural corollary, contingent on the substrate→Dirac descent; content inherited)*

The clean-vector theorem has an immediate consequence for the deepest consistency requirement of a chiral gauge theory, anomaly cancellation. A gauge anomaly is a failure of gauge-current conservation, and it requires *chiral* content: in a vector-like theory the two handednesses contribute with opposite sign and cancel automatically. So:

> The clean transport is vector (§4), therefore it is **automatically anomaly-free** at that level. There is no chiral flow in the clean substrate to threaten gauge-charge conservation. (Contingent, like the theorem, on the descent to a genuine vector Dirac sector, the open substrate-to-Dirac arc; a gauge anomaly is properly a relativistic object, and the transport-level result is what is proven.)

This dovetails with the conservation side ED already has, read with that paper's own caveats. The charge-as-topology result establishes an exact integral Gauss law (circulation quantized and loop-independent, measured to machine precision). That paper is careful that the winding is **inert / Σ-blind** (it couples only weakly, and the result is form-and-structure only, not a claim that the winding *is* electric charge), and it does not itself use the word "anomaly." Reading the exact Gauss law as exact gauge-charge conservation, hence the substrate statement of anomaly-freedom for the charge sector, is therefore an *interpretive* step on top of the measured result, taken here (and in the anomaly state-note), not a claim the charge paper makes. Together, the anomaly question splits the same way the casting did. The **conservation face** is solid (the exact Gauss law) and the **clean baseline** is solid (vector, hence trivially anomaly-free). The **nontrivial part**, the Standard Model's chiral anomaly cancellation, the special balance of hypercharges that ties quarks to leptons, is a property of the chiral **content**, which appears only after the spontaneous breaking and *which* content is the inherited casting. So the nontrivial cancellation is **inherited with the content**, not independently derived, the same wall as the representation spectrum. The one place ED might say more, whether the exact Gauss law *forces* anomaly-freedom as a constraint on whatever chiral content emerges, remains an open, analytic candidate gated on the substrate-to-Dirac reduction; it is named, not claimed.

---

## 7. The Verdict, and the Distinctive Prediction

**The verdict.** ED builds the entire *stage* of chirality and inherits the one *assignment*. It grounds the chirality operator (`γ⁵` = arrow times a spontaneous, orientable, single-valued orientation); it proves the clean transport vector for every channel-count, so that if parity is violated its direction is necessarily spontaneous; it supplies the capability structure (a genuine left/right for two or more channels, forced-vector for one); and it fixes the clean anomaly baseline (vector, hence anomaly-free at the transport level). What it does *not* derive is the assignment, *which* force is chiral, which is the representation-theoretic pseudoreality of `SU(2)`, inherited. This supersedes *The Parity Wall*'s conditional "vector by default": the verdict is now a theorem plus a built operator, in the same direction. It also keeps the earlier correction intact, the first-arrival mechanism natively selects a matter/antimatter reference (C), while the parity reference (P) is inherited; the retired "imprints both C and P" over-read stays retired, now with the clean-vector theorem explaining *why* the P-half could never have been native (the clean rules cannot carry a handedness).

**The prediction, sharpened.** Because the clean substrate is provably vector, ED's parity violation is *necessarily* a spontaneous, contingent, per-universe orientation, tied to the arrow. The same arrow sets the matter/antimatter sign. So ED predicts the gauge handedness and the matter/antimatter sign are **correlated**, two faces of one first-commitment choice, against the Standard Model's law-level, fixed, uncorrelated handedness. This is the firmest footing this prediction has had, resting now on a theorem rather than a stance.

---

## 8. Limitations (honest)

- **The casting is inherited, not derived.** The paper names the mechanism (pseudoreality of `SU(2)`) but does not produce it from ED; it is a representation-theoretic fact ED carries. The wall is strengthened and explained, not breached.
- **The theorem is about the transport/commitment map, not the full relativistic Dirac sector.** The relativistic descent (the substrate-to-Dirac reduction) is the standing open arc behind both a fully relativistic chirality statement and the one non-inherited anomaly candidate. The clean-vector result is proven at the channel-transport level, which is where the casting question was posed.
- **The stability framing is a definition, not a computed spectrum.** "Particle = attractor of the commitment map" is stated and used to locate the casting; the full enumeration of stable patterns is not carried out here.
- **The broken-case winding is illustrative.** The `winding = N` result uses one natural breaking; the robust, model-independent result is the clean-case theorem (`winding \equiv 0`).
- **No content, no numbers.** No representation spectrum, no hypercharges, no masses or mixings, no charge magnitudes.

---

## 9. Falsification Criteria

### 9.1 A chiral clean substrate

**Falsifier sentence:** *A demonstration that the parity-clean commitment map carries a nonzero net point-gap winding for some channel-count, i.e. a chiral coupling without breaking the parity symmetry, would overturn the theorem of §4 and the "necessarily spontaneous" corollary.*

### 9.2 A derived casting

**Falsifier sentence:** *A construction that fixes which channel-count is chiral from ED's transport or stability dynamics alone, reproducing the non-monotone Standard-Model pattern without inheriting the representation-theoretic input, would overturn the "casting is inherited" verdict of §5.*

### 9.3 An uncorrelated handedness

**Falsifier sentence:** *Evidence that the gauge handedness is not correlated with the matter/antimatter sign, or that parity violation is a fixed law-level handedness rather than a spontaneous contingent one, would falsify the distinctive prediction of §7.*

### 9.4 A non-orientable or law-fixed orientation

**Falsifier sentence:** *A demonstration that ED's emergent space is non-orientable, or that a global orientation is fixed by the rules rather than spontaneously chosen, would break the operator grounding of §2 and its spontaneity corollary.*

---

## 10. Position Statement

**Event Density builds the entire stage of chirality and inherits the one assignment.** It grounds the chirality operator as the arrow times a spontaneous, orientable, single-valued spatial orientation; it proves, as a theorem at the channel-transport level, that the parity-clean substrate is vector for every channel-count, so that if parity is violated its direction is necessarily spontaneous; it supplies the capability structure (forced-vector for a single channel, a genuine left/right for two or more); and it fixes the clean anomaly baseline (vector, hence automatically anomaly-free at that level). The one thing it does not derive, *which* force is chiral, is a representation-theoretic fact (the pseudoreality of `SU(2)`), inherited exactly as the gauge multiplicities and the constants are.

**What this paper claims.** A grounded chirality operator (structural); a theorem that the clean substrate is vector for every channel-count at the transport level, with the corollary that if parity is violated its direction is necessarily spontaneous (derived); a capability structure that forces the single-channel case vector (derived-conditional); an inherited, representation-theoretic origin for the casting (account, surviving candidate); a clean anomaly-free baseline, contingent on the substrate-to-Dirac descent, with the nontrivial chiral cancellation inherited (structural + inherited); and a sharpened, falsifiable prediction (handedness correlated with the matter/antimatter sign).

**What this paper does not claim.** That ED derives the weak force's chirality (inherited); that it produces any representation spectrum, hypercharges, masses, or charge magnitudes (none); that the stability framing computes the spectrum (a definition only); or that the relativistic Dirac-sector chirality and the full anomaly cancellation are closed (both gated on the open substrate-to-Dirac reduction).

**Series context.** The matter-sector chirality verdict of the ED program, one tier firmer than *The Parity Wall*, which it supersedes on the verdict. It turns on the same primitive the reduction program isolates, the arrow (P11), which breaks time (giving the arrow, the matter/antimatter reference, and now, once spontaneously oriented, the parity reference) and, by the theorem here, cannot break spatial parity in its clean rules, so parity violation must be spontaneous. It pairs with the gauge-structure paper (the `SU(2)` whose chirality is here shown inherited and explained), the charge-as-topology paper (the conservation face of anomaly-freedom), and the minimal-ontology and quantum-logic papers (the arrow as the sole asymmetry).

---

## Appendix, Glossary and Reader Map

### Glossary

- **`γ⁵` (chirality operator).** `i γ⁰ γ¹ γ² γ³`; in ED, the arrow (`γ⁰`) times the spatial orientation (`γ¹γ²γ³`). A global object, not a per-channel screw.
- **Orientation (spatial).** The oriented volume element `γ¹γ²γ³`, a handedness of the 3-frame; parity-odd; in ED, spontaneously chosen and globally single-valued.
- **Point-gap winding.** The number of times `det H(k)` winds around a reference as `k` runs over its period; nonzero marks net chirality, zero marks vector.
- **Parity-clean.** The substrate has no reflection primitive; parity is a symmetry, so the backward hop mirrors the forward hop (`B = S A S^{-1}`).
- **Capability vs selection.** Capability: is there a genuine left/right to couple to (a nonempty reflection-odd sector)? Selection: does the dynamics use it? ED supplies the first, inherits the second.
- **Casting.** The assignment of which channel-count (which gauge force) is chiral; inherited, representation-theoretic.
- **Necessarily spontaneous.** Because the clean substrate is vector (theorem), any parity violation must break the parity symmetry, hence is a symmetry-breaking, not a law.

### Reader map

*Intuition.* Chirality needs a built-in sense of left versus right. ED's arrow is a time direction, so on its own it tells past from future and (through the phase) matter from antimatter, but not left from right. This paper shows two things at once: the substrate *can* define left and right (the arrow times a spontaneously chosen spatial orientation gives a real handedness operator), but its *clean rules cannot use* that handedness (a parity-clean transport has zero net chirality, provably, at every channel-count). So any actual parity violation has to be a spontaneous choice, like a magnet picking a pole, and *which* force ends up chiral is a fact of group theory (the two-channel group is the special one), which ED takes as given, the same way it takes the constants as given.

*Why the theorem matters.* The earlier verdict was "vector by default, we did not find chirality where we looked." This paper replaces "did not find" with "cannot carry, and here is the proof": the parity-clean determinant is even in the momentum, so its winding is zero for every channel-count. That turns a careful negative into a theorem, and it turns "parity violation is probably spontaneous" into "parity violation is necessarily spontaneous."

### Artifacts

- `evaluation/ChiralGauge/rep_spectrum_casting_winding.py` — the winding computation (clean-case theorem control for `N = 1..6`; broken-case `winding = N`).
- `foundations/T4_10_GateII_Opened_Gamma5IsArrowTimesOrientation.md` — the operator grounding (§2).
- `foundations/T4_08_*`, `foundations/T4_09_*` — orientation spontaneous (§2.1) and space orientable (§2.2).
- `foundations/T4_12_*`, `foundations/T4_13_*` — the lane picture and the capability/selection split (§3).
- `foundations/RepSpectrum_Step1_StabilityFormalism_*`, `foundations/RepSpectrum_Step1_RESULT_*` — the stability framing and the theorem (§4–§5).
- `theory/Anomaly_Cancellation/Anomaly_State_After_CleanVectorTheorem_2026-07-10.md` — the anomaly split (§6).

**Open work** (declared): the relativistic substrate-to-Dirac reduction (behind a fully relativistic chirality statement and the one non-inherited anomaly candidate); whether the exact Gauss law forces anomaly-freedom as a constraint on emergent chiral content; the full enumeration of stable patterns (the representation spectrum), whose discreteness is topological, not stability-sourced.

---

**End of Paper (The Clean Substrate Is Vector).**

*Substrate-evaluation arc. The chirality operator is grounded as the arrow times a spontaneous, orientable, single-valued orientation; the parity-clean commitment map has `det H(k)` even in `k`, so its point-gap winding is identically zero for every channel-count, the clean substrate is vector, and parity violation is necessarily spontaneous. The casting (which force is chiral) matches no transport winding (clean `0`, broken monotone-`N`, against the non-monotone Standard Model), so it is the inherited representation-theoretic pseudoreality of `SU(2)`. Vector clean substrate is automatically anomaly-free; the chiral cancellation is inherited with the content. Supersedes The Parity Wall on the verdict's tier, from conditional default to theorem plus grounded operator, same direction, P inherited. Distinctive prediction: parity handedness is spontaneous, contingent, and correlated with the matter/antimatter sign.*
