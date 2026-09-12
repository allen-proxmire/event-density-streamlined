# The result

## Statement

**Theorem.** Let H(k) = e^{ik}A + e^{−ik}B be the transport map of a family of N channels, with A and B complex N × N matrices. Let S be the matrix that reverses the order of the channels. If the transport is symmetric under reflection, S H(k) S⁻¹ = H(−k), then the winding number of det H(k) about any point off its path is zero. This holds for every N and every forward hop A.

**Consequence for ED.** A transport with net handedness, meaning a nonzero winding, requires S H(k) S⁻¹ ≠ H(−k). ED's rules contain no reflection, so they cannot supply that asymmetry. **If ED's transport carries a handedness, it comes from the state the substrate is in, a spontaneously broken symmetry, and not from its rules.**

The assumptions behind each step are in [Assumptions.md](Assumptions.md).

## Proof

**1. Symmetry fixes the backward hop.**

$$S\,H(k)\,S^{-1} = e^{ik}\,SAS^{-1} + e^{-ik}\,SBS^{-1}, \qquad H(-k) = e^{-ik}A + e^{ik}B.$$

These are equal for all k exactly when the coefficients of e^{ik} match: B = SAS⁻¹. The coefficients of e^{−ik} then match too, because S² = 1. So the backward hop is the mirror image of the forward hop, and A is the only free structure.

**2. The determinant is even.** Write f(k) = det H(k). Then

$$f(-k) = \det H(-k) = \det\!\left(S\,H(k)\,S^{-1}\right) = \det H(k) = f(k).$$

**3. The winding is zero.** As k runs over [−π, π], f traces a closed curve. Its winding number about a point z₀ not on the curve is

$$W = \frac{1}{2\pi i}\int_{-\pi}^{\pi} \frac{f'(k)}{f(k) - z_0}\,dk.$$

Because f is even, f′ is odd, so the integrand is odd and the integral over the symmetric interval vanishes. W = 0. ∎

## Why the question is not empty

Handed transport does exist in this family, so the theorem rules something out:

- **Break the symmetry and the winding appears.** With a purely one-way hop (B = 0), det H(k) = e^{iNk} det A, whose winding about 0 is N.
- **Without the arrow, no transport could be handed.** If transport were Hermitian (B = A†), det H(k) would be real and its winding about any point off the real axis would be zero whatever the symmetry. It is the arrow (P11) that makes forward and backward hops independent, and so makes handedness possible at all.

So the theorem separates two cases: ED's arrow makes handed transport possible, and ED's reflection-symmetric rules keep it out of the laws.

## Check

    python tools/check_result.py

The script computes det H(k) for random forward hops A and N = 1 to 6. It confirms that the determinant is even and that the winding is zero in the symmetric case. It also runs the two controls above, showing winding N for the one-way hop and zero for Hermitian transport.

## How far it reaches

- **This model only.** The result is about the transport model in M1–M3. That ED's substrate transport has this form is assumed, not derived.
- **Transport only.** It does not construct relativistic fermions (a Dirac sector). It does not say whether nature's handedness arose this way, or which force is handed.
- **Modest in mathematical terms.** It is the principle that a reflection-symmetric system carries no reflection-odd invariant, made explicit for this family and shown for every N.
