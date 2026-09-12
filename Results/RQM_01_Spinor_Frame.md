# The spinor frame is unique

**The claim.** In 3+1 dimensions there is exactly one four-component spinor structure, up to a change of basis. Every way of writing the gamma matrices (Dirac, Weyl, Majorana) is the same object in different clothes, so nothing physical depends on which one is used.

**Strength:** follows from the foundation, using standard algebra.
**Sector:** relativistic quantum mechanics. **Paper:** [Frame Uniqueness_Clifford 3_1](../Papers/Frame%20Uniqueness_Clifford%203_1.md). **Ledger row:** 90.

---

## What it uses from the foundation

| | item | how it enters |
|---|---|---|
| P06 | space is 3 dimensions plus time | load-bearing. It forces the signature, and so fixes which Clifford algebra applies |
| P03 | channels and loci are indexed | the indexing the gamma matrices act on |
| P05 | polarity transport | the transport the Clifford structure is defined over |
| P09 | polarity is a U(1) angle | the angular structure carried onto the gammas |
| P10 | rule-types | supplies the spinor carriers |
| condition 23 | time stays different from space | the signature comes through the emergent metric, which needs this condition held |

## What it borrows from standard physics

| borrowed | why it is fair, and what it costs |
|---|---|
| Clifford algebra, Pauli's theorem on gamma matrices, Schur's lemma | standard mathematics, uncontroversial, and the engine of the uniqueness proof |

## How it goes

The signature fixes the algebra. That algebra has a four-dimensional irreducible representation, and by Pauli's theorem any two realizations of the gammas are related by a similarity transformation. Schur's lemma makes the connecting matrix unique up to scale. So the frame is unique, and a basis choice is a choice of that matrix rather than an extra physical input.

## What this leans on, stated plainly

- The signature arrives through the emergent metric rather than straight from the primitives, so this result inherits that machinery and its conditions.
- The heavy lifting is standard mathematics. ED's content is that its own structure lands in this algebra at all.

## How it could be killed

Evidence that the algebra admits inequivalent four-dimensional irreducible representations, which would contradict Pauli's theorem. Detection of spinor content in 3+1 dimensions that is not four-component. Evidence that the substrate permits a dimension other than 3+1.

## What it is not

Not a derivation of the Dirac equation, and not a claim that any particular basis is preferred.
