# If the world is left-handed, it chose to be

**The claim.** The paper claims that a substrate whose rules do not favour a handedness cannot produce a handed transport, for any number of channels. So parity violation cannot be written into ED's law; it has to be a broken symmetry.

**Strength:** Modest ED-specific result. The theorem is correct, but it is the statement that a parity-symmetric model carries no parity-odd invariant, and one claim in the paper conflicts with Standard Model hypercharge.
**Sector:** substrate tests. **Paper:** [Clean Substrate Vector_Parity Spontaneous](../Papers/Clean%20Substrate%20Vector_Parity%20Spontaneous.md). **Ledger row:** 94.

---

## What review found

- **The theorem is correct.** For a parity-symmetric one-way hopping map H(k) = e^{ik}A + e^{−ik}SAS⁻¹, det H(k) is even in k, so the point-gap winding is zero for every channel count.
- **Its content is modest.** As the paper itself says, it is "parity symmetry forbids a parity-odd invariant" applied to this model. The physical content lies in whether ED's substrate has this form.
- **One claim misidentifies the abelian factor.** The paper says "N = 1 is forced vector, matching electromagnetism". The Standard Model's fundamental abelian factor is hypercharge, and hypercharge is chiral.
- **Two claims are unsupported.** Offering the pseudoreality of SU(2) as the origin of the weak force's chirality is speculation. The paper's distinctive prediction, that handedness is spontaneous and correlated with the matter/antimatter sign, has no stated way to measure it.

## What it uses from the foundation

| | item | how it enters |
|---|---|---|
| P09 | polarity is a U(1) angle | the phase structure the winding is computed from |
| P11 | commitment is irreversible | the one-way hop |
| — | the absence of any reflection primitive | parity is a symmetry of the rules |

## What it borrows from standard physics

| borrowed | why it is fair, and what it costs |
|---|---|
| representation theory, for which forces are chiral in the Standard Model | the part ED does not supply; the paper calls the casting inherited |
| the point-gap winding as the chirality invariant | the standard invariant for non-Hermitian hopping models |

## How it goes

Suppose the rules are blind to handedness. Then the backward hop is the mirror image of the forward hop, which makes the determinant even in the wavevector, which makes the winding vanish. Zero winding means vector-like, not chiral. This was checked numerically for one through six channels.

## What this leans on, stated plainly

- **Transport level only.** The step from substrate transport to a genuine Dirac sector is open.
- **The model form.** Everything rests on ED's substrate having this commitment-map form.

## How it could be killed

A parity-symmetric map of this form with nonzero winding is mathematically impossible, so the theorem itself cannot fail. The physical claim fails if ED's substrate is not parity-symmetric in this form, or if handedness is shown to be a fixed property of the law.

## What it is not

Not a derivation of the weak force's handedness, or of the Standard Model's matter content.
