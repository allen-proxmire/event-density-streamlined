# Gauge groups and channel multiplicity

**The claim.** The paper claims a family of N indistinguishable channels has structure group U(N) = (SU(N) × U(1))/Z_N, so non-abelian gauge structure comes from having more than one channel, and the Standard Model's groups correspond to multiplicities {1, 2, 3}.

**Strength:** Textbook result, restated in ED terms. Norm-preserving invertible maps on C^N form U(N). The match to the Standard Model does not hold as stated.
**Sector:** quantum field theory. **Paper:** [MatterSector_Gauge_Spin_Chirality_3D](../Papers/MatterSector_Gauge_Spin_Chirality_3D.md). **Ledger row:** 84.

---

## What review found

- **The main step is standard linear algebra:** U(N) is the group of norm-preserving transformations of C^N.
- **The multiplicities don't produce the Standard Model group.** Multiplicities {1, 2, 3} give U(1) × U(2) × U(3), which has three abelian factors. The Standard Model group, (SU(3) × SU(2) × U(1))/Z₆, has one.
- **One kill condition was already met, and has been removed.** The earlier version of this page listed "a parity-violating abelian force" as a way to kill the result. The Standard Model already has one: hypercharge U(1)_Y couples differently to left- and right-handed fermions. So the paper's claim that ED's abelian coupling is blind to handedness is contradicted by known physics.
- **The "no stable SU(N ≥ 4)" bound is assumed, not derived.** It rests on an internal amplitude dimension d = 3 that the paper takes as given.
- **One step is unnamed.** "Invertibility between commitments", which turns an isometry into a unitary, is not one of the primitives, and it sits awkwardly with the irreversibility of P11.
- **Two errors were corrected in the paper on 2026-09-11:** the group identity, which still needed fixing in the paper's abstract and has now been fixed, and the primitive cited for channel multiplicity, which should have been P07 rather than P08.

## What it uses from the foundation

| | item | how it enters |
|---|---|---|
| P04 | bandwidth is conserved | forces transport to preserve the norm |
| P07 | channel structure is basic | supplies the multiplicity N |
| P09 | polarity is a U(1) angle | the phase the amplitude carries |
| axiom 14 | V5 exists | cross-channel mixing, the non-abelian part |
| axiom 21 | the V1 kernel's shape | single-channel transport, the abelian part |
| definition 2 | amplitudes add and scale | lets the channel content be a complex vector |

## What it borrows from standard physics

| borrowed | why it is fair, and what it costs |
|---|---|
| the Standard Model's own multiplicities {1, 2, 3} | matched, not derived |
| the coupling strengths | measured |

## How it goes

A family of N indistinguishable channels carries a complex amplitude with N components. Bandwidth conservation makes transport norm-preserving. Assume invertibility, and it is unitary. So the structure group is U(N).

## What this leans on, stated plainly

- The unnamed invertibility step.
- An assumed internal dimension d = 3 for the bound on N.

## How it could be killed

The linear-algebra step cannot fail. The physical claims attached to it already conflict with the Standard Model: hypercharge is chiral, and the group structure does not match.

## What it is not

Not a derivation of the Standard Model's gauge group, and not a correct account of which groups appear.
