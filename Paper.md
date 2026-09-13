# Reflection-Symmetric Transport Carries No Handedness: A Result About Event Density's Substrate

**Allen Proxmire**

**September 2026**

---

## Abstract

Event Density (ED) describes the world as a discrete substrate: channels carrying a complex phase at indexed loci, with an irreversible arrow of time. This paper asks whether a net handedness can be written into the rules of that substrate's transport. It cannot. Model the transport of a family of N channels along a chain as H(k) = e^{ik}A + e^{−ik}B, where A is the forward hop and B the backward hop, and measure net handedness by the winding number of det H(k). If the transport is symmetric under reflection, the winding number is zero for every N and every forward hop A. ED's rules contain no reflection, so if ED's transport carries a handedness, it comes from a spontaneously broken symmetry in the state of the substrate, not from its rules. Two controls show the question is not empty: a one-way hop has winding N, and without the arrow no transport in this family could be handed at all. A short script checks the theorem numerically for N = 1 to 6.

---

## 1. Introduction

A system has a handedness when it distinguishes left from right. The question here is where a handedness could come from in ED: from the rules, or from the state the substrate happens to be in.

The answer depends on two facts about ED:

- **Its rules contain no reflection.** None of ED's thirteen primitives distinguishes left from right. (All thirteen are listed in Appendix A.)
- **It has an arrow.** Commitment is irreversible, so forward and backward transport need not mirror each other.

The first fact rules handedness out of the laws. The second makes handedness possible at all. The result below makes both statements precise for a definite model of transport, and proves the first for every number of channels.

Mathematically the result is modest. It is the principle that a reflection-symmetric system carries no reflection-odd invariant, worked out explicitly for this family of transport maps. What makes it specific to ED is where the symmetry comes from (ED's primitive list) and why the question is worth asking (ED's arrow).

Section 2 states every assumption. Section 3 states and proves the theorem. Section 4 gives the controls, Section 5 the numerical check, Section 6 the consequence for ED, and Section 7 the limits.

---

## 2. Assumptions

The result assumes the items in this section and nothing else.

### 2.1 The ED primitives used

ED has thirteen primitives. The result uses five of them.

| | primitive | what it supplies to the result |
|---|---|---|
| **P03** | **Indexing and spatial homogeneity.** Channels and loci carry discrete indices, and the substrate's rules are the same at every locus. | Transport is the same at every locus, so it can be written in terms of a wavenumber k. |
| **P05** | **Polarity transport.** Polarity is carried along the edges between neighbouring loci. | Transport is a hop to a neighbouring locus: forward (A) or backward (B). |
| **P07** | **Channels are basic objects.** Two channels at the same locus are distinct even when their contents coincide. | A family of N distinct channels, so each hop is an N × N matrix. |
| **P09** | **Polarity is a U(1) phase.** Each channel at each locus carries a phase e^{iπ}. | Hop amplitudes are complex numbers. |
| **P11** | **Commitment is irreversible.** No operation of the substrate undoes a commitment. | Forward and backward hops need not mirror each other, so transport need not be Hermitian. |

### 2.2 One property of the primitive list

**No primitive is a reflection.** None of the thirteen primitives (Appendix A) distinguishes a direction in space from its mirror image. So ED's rules are symmetric under reflection.

### 2.3 One definition

**Amplitudes add and scale.** They form a complex vector space, so a hop acts on the N channel amplitudes as an N × N complex matrix.

### 2.4 Modelling assumptions

These are not ED primitives. They are the choices that turn the primitives into something that can be calculated.

**M1. The transport map.** Transport for a family of N channels along a one-dimensional chain is

$$H(k) = e^{ik}A + e^{-ik}B,$$

where A is the N × N matrix for a hop forward along the chain, B the matrix for a hop backward, and k ∈ [−π, π] the wavenumber. A and B are independent complex matrices. In particular B need not equal A†; this is how the irreversibility of P11 enters the model.

**M2. How reflection acts.** Reflection reverses direction along the chain, sending k → −k. It also reverses the order of the channels, through the matrix S that sends channel i to channel N + 1 − i. S is a permutation matrix with S² = 1. A transport is reflection-symmetric when

$$S\,H(k)\,S^{-1} = H(-k) \quad \text{for all } k.$$

**M3. The measure of handedness.** Net handedness is measured by the winding number of det H(k) as k runs once over [−π, π]. For a closed curve f(k) in the complex plane and a point z₀ not on it, the winding number is

$$W = \frac{1}{2\pi i}\int_{-\pi}^{\pi} \frac{f'(k)}{f(k) - z_0}\,dk,$$

the number of times the curve goes around z₀. For non-Hermitian hopping models this is the standard invariant, known as the point-gap winding number [2, 3]. Its simplest example is the Hatano–Nelson model [1], in which unequal forward and backward hopping gives a nonzero winding.

### 2.5 Mathematics used

Determinants, and the winding number of a closed curve in the complex plane.

---

## 3. The theorem

**Theorem.** Let H(k) = e^{ik}A + e^{−ik}B with A and B complex N × N matrices, and let S reverse the order of the channels. If S H(k) S⁻¹ = H(−k) for all k, then the winding number of det H(k) about any point off its path is zero. This holds for every N and every forward hop A.

### Proof

**Step 1: symmetry fixes the backward hop.** Conjugating by S and reversing k give

$$S\,H(k)\,S^{-1} = e^{ik}\,SAS^{-1} + e^{-ik}\,SBS^{-1}, \qquad H(-k) = e^{-ik}A + e^{ik}B.$$

The functions e^{ik} and e^{−ik} are linearly independent, so these are equal for all k exactly when their coefficients match. The coefficient of e^{ik} gives B = SAS⁻¹. The coefficient of e^{−ik} gives SBS⁻¹ = A, which then holds automatically because S² = 1. So the backward hop is the mirror image of the forward hop, and A is the only free structure.

**Step 2: the determinant is even.** Write f(k) = det H(k). Since the determinant is unchanged by conjugation,

$$f(-k) = \det H(-k) = \det\!\left(S\,H(k)\,S^{-1}\right) = \det H(k) = f(k).$$

**Step 3: the winding is zero.** f is a polynomial in e^{ik} and e^{−ik}, so it is smooth and periodic, and f(k) traces a closed curve as k runs over [−π, π]. Take any z₀ not on the curve. Because f is even, f′ is odd, so the integrand f′(k)/(f(k) − z₀) is odd. The integral of an odd function over the symmetric interval [−π, π] is zero. So W = 0. ∎

Geometrically: as k runs from 0 to π the curve traces a path, and as k runs from −π to 0 it traces the same path backwards. A curve that retraces itself goes around no point.

---

## 4. Why the question is not empty

The theorem would say nothing if no transport in this family could be handed. Two controls show that handed transport exists, and what makes it possible.

**Break the symmetry and the winding appears.** Take a purely one-way hop, B = 0, with det A ≠ 0. Then

$$\det H(k) = \det(e^{ik}A) = e^{iNk}\det A,$$

a circle of radius |det A| traversed N times. Its winding number about 0 is N. So transport in this family can carry any amount of handedness once the reflection symmetry is broken.

**Without the arrow, no transport could be handed.** Suppose instead that transport were Hermitian, the case in which forward and backward hops mirror each other in time: B = A†. Then H(k)† = e^{−ik}A† + e^{ik}A = H(k), so H(k) is Hermitian and det H(k) is real for every k. A curve on the real line goes around no point off the real line, so the winding is zero whatever the symmetry. It is the arrow (P11), through the independence of A and B in M1, that makes handed transport possible at all.

**The smallest case.** For N = 1, S = 1 and the symmetry condition is simply B = A. The transport is H(k) = 2A cos k, a segment traced back and forth, with winding zero. Taking |B| ≠ |A| instead gives the Hatano–Nelson model [1], whose curve is an ellipse around 0 with winding +1 or −1.

So the theorem separates two cases. ED's arrow makes handed transport possible, and ED's reflection-symmetric rules keep it out of the laws.

---

## 5. Numerical check

The script `tools/check_result.py` (requires numpy) checks the theorem and both controls directly.

```
python tools/check_result.py
```

For each N from 1 to 6 it:

1. **Tests the theorem.** It draws 20 random complex forward hops A, sets B = SAS⁻¹, and computes det H(k) at 4000 values of k. It reports how far f(k) is from f(−k), relative to the size of f, and the winding number about a random point off the curve.
2. **Runs the one-way control.** With B = 0 it computes the winding about 0.
3. **Runs the Hermitian control.** With B = A† it computes the winding about a point just off the real axis.

Output:

```
N  symmetric: max|f(k)-f(-k)|/max|f|  windings | one-way winding | Hermitian windings
1  1.0e-15  [0] | 1 | [0]
2  2.0e-15  [0] | 2 | [0]
3  3.2e-15  [0] | 3 | [0]
4  3.9e-15  [0] | 4 | [0]
5  4.4e-15  [0] | 5 | [0]
6  4.3e-15  [0] | 6 | [0]

result holds for N = 1..6
```

The determinant is even to machine precision and the symmetric winding is always 0. The one-way winding is N and the Hermitian winding is 0, as Section 4 says. The script exits with an error if any of these fails.

---

## 6. Consequence for ED

By the theorem, a nonzero winding requires S H(k) S⁻¹ ≠ H(−k): the transport must break the reflection symmetry. By Section 2.2, ED's rules contain no reflection, so they cannot supply that asymmetry. Therefore:

> **If ED's transport carries a net handedness, the handedness comes from the state the substrate is in, a spontaneously broken symmetry, and not from its rules.**

This is the familiar pattern of a ferromagnet. Its laws treat every direction alike, yet the magnet picks one. The theorem says that in ED, handedness in transport can only arise that way.

---

## 7. How far the result reaches

- **This model only.** The result concerns the transport model defined by M1–M3. That ED's substrate transport has this form, that reflection acts on it as in M2, and that the winding number is the right measure of handedness are assumptions, not derivations.
- **Transport only.** The result does not construct relativistic fermions, and it does not say whether nature's handedness arose this way or which force in nature is handed.
- **A negative result about the rules.** It shows that ED's rules cannot contain a handedness in this model. It does not show that ED's substrate does break the symmetry, or how it would.
- **Mathematically modest.** It is the principle that a reflection-symmetric system carries no reflection-odd invariant, made explicit for this family and shown for every N.

### Could it have come out wrong?

The proof is short, so the result's content lies in its inputs and its controls:

- **The controls could have failed.** If the arrow did not make handed transport possible (Section 4), the theorem would be empty. It does: the one-way hop has winding N.
- **The symmetry claim could fail.** If any ED primitive turned out to be a reflection, Section 2.2 would fail, and the consequence in Section 6 would not follow. The full list is in Appendix A so that this can be checked.
- **The model could be wrong for ED.** If ED's transport is not of the form M1, or reflection does not act as in M2, the theorem still holds but no longer applies to ED.

---

## Appendix A. The thirteen ED primitives

Listed so that the property in Section 2.2 can be checked. Only P03, P05, P07, P09 and P11 are used by the result.

| | primitive |
|---|---|
| P01 | A discrete substrate exists, carrying the structure the other primitives describe. |
| P02 | Chains (persistent sequences of events) participate in channels at loci. Participation is a basic relation. |
| P03 | Channels and loci carry discrete indices, and the substrate's rules are the same at every locus. |
| P04 | Each channel at each locus carries a non-negative bandwidth, additive over disjoint channels. |
| P05 | Polarity is transported along the edges between neighbouring loci. |
| P06 | Space has three dimensions, plus one of time. |
| P07 | Channels are basic objects: two channels at the same locus are distinct even when their contents coincide. |
| P08 | The substrate has a smallest length scale. |
| P09 | Polarity is a U(1) phase. |
| P10 | The substrate supports several distinct types of rule. |
| P11 | Commitment is irreversible: at a commitment event a chain's participation collapses to a single channel, and no operation of the substrate undoes it. |
| P12 | Each chain carries a stability functional, Σ = Coh − Str − Grad (coherence minus strain minus gradient content). |
| P13 | The substrate's rules are the same at every time. |

None of these distinguishes a direction in space from its mirror image. P11 distinguishes the future from the past, which is a different asymmetry, and it is the one Section 4 shows is needed for handed transport to be possible.

---

## References

[1] N. Hatano and D. R. Nelson, "Localization transitions in non-Hermitian quantum mechanics," *Physical Review Letters* **77**, 570 (1996).

[2] Z. Gong, Y. Ashida, K. Kawabata, K. Takasan, S. Higashikawa and M. Ueda, "Topological phases of non-Hermitian systems," *Physical Review X* **8**, 031079 (2018).

[3] K. Kawabata, K. Shiozaki, M. Ueda and M. Sato, "Symmetry and topology in non-Hermitian physics," *Physical Review X* **9**, 041015 (2019).
