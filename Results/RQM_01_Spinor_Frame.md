# The spinor frame is unique

**The claim.** In 3+1 dimensions there is exactly one four-component spinor structure up to a change of basis, so the Dirac, Weyl and Majorana forms of the gamma matrices are the same object written differently.

**Strength:** Textbook result, restated in ED terms. This is Pauli's fundamental theorem on gamma matrices. ED assumes the dimension (P06) and inherits the signature.
**Sector:** relativistic quantum mechanics. **Paper:** [Frame Uniqueness_Clifford 3_1](../Papers/Frame%20Uniqueness_Clifford%203_1.md). **Ledger row:** 90.

---

## What review found

- **The result is correct.** The heavy lifting is Pauli's theorem and Schur's lemma.
- **ED supplies no input beyond assuming 3+1 dimensions.** The Lorentzian signature is inherited from another paper.
- **One minor error.** The paper calls the choice between Cl(3,1) and Cl(1,3) a convention. That is true for complex representations, but as real algebras the two are not isomorphic, which matters for Majorana spinors. The uniqueness claim is unaffected.
- **The earlier kill conditions were mostly "Pauli's theorem is wrong".** That is not a physical test.

## What it uses from the foundation

| | item | how it enters |
|---|---|---|
| P06 | space is 3 dimensions plus time | fixes which Clifford algebra applies |
| P03 | channels and loci are indexed | the indexing the gamma matrices act on |
| P05 | polarity transport | the transport the Clifford structure is defined over |
| P09 | polarity is a U(1) angle | the angular structure |
| P10 | rule-types | the spinor carriers |
| condition 23 | time stays different from space | the signature comes through the emergent metric |

## What it borrows from standard physics

| borrowed | why it is fair, and what it costs |
|---|---|
| Clifford algebra, Pauli's theorem on gamma matrices, Schur's lemma | standard mathematics, and the whole engine of the result |

## How it goes

The signature fixes the algebra. The algebra has a four-dimensional irreducible representation, and by Pauli's theorem any two realizations of the gammas are related by a similarity transformation, unique up to scale by Schur's lemma.

## What this leans on, stated plainly

- The assumed dimension and the inherited signature.

## How it could be killed

Nothing here is specific to ED. The mathematics is settled, and the physical input, 3+1 dimensions, is assumed.

## What it is not

Not a derivation of the Dirac equation, and not a derivation of the dimension of spacetime.
