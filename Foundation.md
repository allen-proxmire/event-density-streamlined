# Foundation

**Event Density starts from 53 items: 49 assumptions and 4 arguments.** Three more items are definitions. They are names, not claims, and are listed at the end without being counted.

- **Assumptions** are starting points, taken as given. Nothing in ED derives them.
- **Arguments** are things a paper argues follow from the assumptions, with reasons that are not yet airtight. Until a full proof exists, they are treated like assumptions. When one is proven, it leaves this list.
- **Definitions** are just names for things already there. They cannot be wrong, and they are not counted.

Everything else ED says has to trace back to this page.

**Read this list with two facts in mind** (review, 2026-09-12):

- **The list takes the measured numbers of physics as given:** G, ħ, Λ, H₀, the particle masses, the couplings, and the MOND scale a₀. A result that uses one of them cannot count as predicting it.
- **The primitives are stated in words, not as a mathematical model.** Several cannot be evaluated as written; the canonical primitives paper says so of P12's Σ. That is why the results built on this list restate known physics rather than calculate new physics. See [Results](Results/README.md).

*Sources: the 13 primitives are canonical `Paper_087`; the constants and the first 14 axioms are the 38 core-theory lines of `ED_ItemizedTheory_TieredClaims_v2.xlsx` (ED Generative); every other item was read in its own paper on 2026-09-11.*

---

## Assumptions (49)

### The 13 primitives

| | primitive |
|---|---|
| P01 | Existence layer: the foundational existence commitment. Below it there is no further substrate structure. |
| P02 | Participation is the primitive relation. Chains participate, and composite structures derive from that. |
| P03 | Channels and loci are indexed, and space is homogeneous. |
| P04 | Bandwidth: a non-negative, additive quantity. |
| P05 | Polarity is transported between neighbouring loci. |
| P06 | Space has 3 dimensions, plus time (D = 3+1). |
| P07 | Channel structure is basic, not built from something else. |
| P08 | The substrate has a smallest scale, ℓ_ED (matched to the Planck length). |
| P09 | Polarity takes values in U(1), an angle. |
| P10 | Rule-types are primitive. This is what allows the V5 kernel to exist as one. |
| P11 | Commitment is irreversible, with the environment randomizing phase. This is the arrow of time. |
| P12 | Each chain has a stability landscape, Σ = Coh − Str − Grad. |
| P13 | Time is homogeneous, and events are discrete. |

### The 10 constants

Values ED takes as given.

| | constant |
|---|---|
| c | the rate of becoming: how a tick converts to a hop |
| G | Newton's constant, G = c³ℓ_P²/ħ |
| a₀ | the MOND acceleration scale, a₀ = cH₀/2π (the scale ∼ cH₀ is supported; the 1/2π is disputed) |
| Λ | the cosmological constant |
| ħ | the action of one commitment |
| ℓ_P | the Planck length, equal to ℓ_ED: the size of one hop |
| H₀ | the Hubble rate |
| masses | the particle masses |
| g | the gauge couplings |
| α | the fine-structure constant (about 1/137) and the mass ratios |

### The 26 axioms

**14 from the 38 core-theory lines**

| | axiom | where |
|---|---|---|
| 1 | **SCBU:** the MOND scale a₀ and the scale ξ come from one boundary, the cosmic horizon R_H = c/H₀ | SCBU paper |
| 2 | **P-Bipartite-Mapping:** two-chain states have tensor-product structure; unentangled states factor as Ψ^A ⊗ Ψ^B | 063 |
| 3 | **P-V5-Schmidt-Generic:** chains linked by V5 are generically entangled (Schmidt rank above 1) | 064 |
| 4 | **P-V5-Budget and P-Measure-Saturation:** each chain has a finite budget for entanglement, and maximal entanglement uses all of it | 065 |
| 5 | **P-V5-Hilbert-Constraint:** ED's correlations reach the Tsirelson bound and no further (no PR boxes) | 069 |
| 6 | **P-Quadratic-Strain (Model C):** the gravitational strain on a channel is the squared size of the total amplitude arriving on it, not a plain sum of the sources. The squared terms give Newton; the cross term between two sources gives MOND's geometric mean. The paper calls it a chosen reading, like Paper_026's linear one | QuadraticStrain |
| 7 | **P-YM-Action-Coarse-Graining:** zoomed out, the substrate gives the Yang–Mills action | 019 |
| 8 | **P-OS-Reflection-Positivity:** the zoomed-out theory satisfies reflection positivity (OS3) | 020 |
| 9 | **P-Profile-Rescaling:** the Yang–Mills continuum limit survives rescaling | 021 |
| 10 | **P-QMkin-Composition:** combined systems compose by tensor product, Ψ^AB = Ψ^A ⊗ Ψ^B | 002 |
| 11 | **P-RB-1:** there is a local rate of becoming, and the substrate's c is constant | 012 |
| 12 | **P-Gauge:** gauge rule-types carry a connection (a potential A) on their bundles, it shifts under a gauge group (U(1) or a larger one), and only the gauge-invariant (transverse) modes are physical. The paper says deriving it from the primitives is open | 114 |
| 13 | **P-QD-LiveWeight:** uncommitted correlation between branches uses up V5 budget | QuantumDarwinism |
| 14 | **V5 exists:** a kernel linking different chains exists (P10 allows it; nothing derives it) | 090 |

The 38 lines carry one more line, the six acoustic-metric guardrails of Paper_035. It is six rules in one. The first, "c stays constant", is axiom 11 above. The other five are listed on their own at 22–26.

**7 more, found in the foundation papers**

| | axiom | where | what the paper says |
|---|---|---|---|
| 15 | **P-LinRate:** a channel is chosen in proportion to its bandwidth. This is the core of the Born rule, taken as given | 003 | "the load-bearing postulate" |
| 16 | **P-Channel-Orthogonality:** different channels do not overlap | 004 | "remains fully open"; three attempts to derive it failed |
| 17 | **P-Gleason-Compatibility:** ED's probabilities meet the conditions Gleason's theorem needs | 004 | partly shown (2026-07-02 update) |
| 18 | **P-T18-Arrow-Inheritance:** the everyday arrows of time (heat, light, the cosmos) come from the kernel's arrow | 093 | a postulate |
| 19 | **P-Causality-Propagation:** everyday cause and effect comes from the substrate's | 094 | a postulate |
| 20 | **P-Hierarchy-Closure:** zooming out never creates a new kind of kernel | 092 | a postulate |
| 21 | **The V1 kernel has this shape:** a chain's response to its own earlier state is a bounded envelope in the separation, set by the smallest scale, times a factor saying which times count. P10 allows a kernel; nothing derives this shape | 089 | the audit calls the form a postulate (§3.1). Which times count, past only or not, is argument 1 and argument 2 below |

**5 working conditions for the gravity picture**

These are not claims about what the world is made of. They are conditions the emergent-gravity picture needs in order to work. Paper_035 declares each one a postulate (C2 to C6), and nothing derives them.

| | condition | where | what the papers say |
|---|---|---|---|
| 22 | **Space's shape changes gently:** it cannot change sharply over distances as small as one hop | 035 (C2) | a postulate |
| 23 | **Time stays different from space:** the emergent geometry always has one time direction and three space directions | 035 (C3) | a postulate |
| 24 | **No negative-energy waves:** any added kind of wave carries positive energy (no "ghosts") | 035 (C4) | a postulate |
| 25 | **Zoom out the right amount:** the blur is much bigger than the substrate's smallest scales and much smaller than the flow being described | 035 (C5) | a postulate |
| 26 | **Horizons behave:** where there is a horizon, the links between inside and outside die off there | 035 (C6), 039 | 039 (May) takes the horizon's place from general relativity. GR-III (July) has its linear gravity rule reach b = 0 on a surface whose size grows with the mass, but only because the solution is clipped at zero; that is not a strong-field result. The areal-coordinate Schwarzschild form the horizon results use is not derived (review, 2026-09-12) |

---

## Arguments (4)

Argued in their papers, not yet proven airtight. Treated as assumptions until they are.

| | argument | where | what the paper says |
|---|---|---|---|
| 1 | **P-T18-Kernel-Retardation:** every kernel looks only at the past | 093 | "formalizes the §7.1 conclusion" |
| 2 | **P-NoBackwardChain:** no backward-in-time chain can be built from the primitives | 089 | argued "by inspection of the primitive list"; a rigorous proof is still owed |
| 3 | **P-SubstrateLocality:** things only touch their near neighbours | 089 | "an implicit consequence of P03 + P08"; the paper calls that argument loose |
| 4 | **P-Primitive-Forward-Causality:** no signal ever goes backward | 094 | stated as following from P04, P11 and kernel retardation |

---

## Definitions (3, not counted)

| | definition | where |
|---|---|---|
| 1 | **P-EDThreshold-Collapse:** a nickname for "a threshold, an irreversible commitment and a projector, acting together" | 005_5 ("a naming convenience, not a new postulate") |
| 2 | **P-Motif-Algebra:** amplitudes can be added and scaled like arrows (they form a complex vector space) | 007 ("definitional") |
| 3 | **P-Hierarchy-Indexing:** kernels are sorted by their size, their memory and their reach | 092 (a classification scheme) |
