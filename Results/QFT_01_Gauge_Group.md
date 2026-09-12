# Where the gauge groups come from

**The claim.** The structure group of a family of N indistinguishable channels is U(N), which is (SU(N) × U(1))/Z_N. Non-abelian gauge structure is not put in by hand; it is what having more than one channel means.

**Strength:** follows from the foundation, with one step in the paper left unnamed.
**Sector:** quantum field theory. **Paper:** [MatterSector_Gauge_Spin_Chirality_3D](../Papers/MatterSector_Gauge_Spin_Chirality_3D.md). **Ledger row:** 84.

---

## What it uses from the foundation

| | item | how it enters |
|---|---|---|
| P04 | bandwidth is conserved | forces transport to preserve the norm, which makes it an isometry |
| P07 | channel structure is basic | supplies the multiplicity N |
| P09 | polarity is a U(1) angle | the phase the amplitude carries |
| axiom 14 | V5 exists | cross-channel mixing, which is the non-abelian part |
| axiom 21 | the V1 kernel's shape | single-channel transport, which is the abelian part |
| definition 2 | amplitudes add and scale | lets the channel content be a complex vector |

## What it borrows from standard physics

| borrowed | why it is fair, and what it costs |
|---|---|
| the Standard Model's own multiplicities {1, 2, 3} | ED does not predict which families exist. The correspondence to U(1), SU(2) and SU(3) is matched, not derived |
| the coupling strengths | measured |

## How it goes

A family of N indistinguishable channels carries a complex amplitude with N components. Bandwidth conservation makes transport norm-preserving; together with invertibility between commitments that makes it unitary. So the structure group is U(N). Splitting it, single-channel transport gives the abelian piece and cross-channel mixing gives the non-abelian piece.

## What this leans on, stated plainly

- **One step in the paper is not named as an assumption.** "Invertibility between commitments" is what turns an isometry into a unitary. It is not one of the thirteen primitives, and given that the arrow makes commitment itself irreversible, it deserves a line of its own rather than a clause.
- The paper as written said U(N) = SU(N) × U(1), which is not right as a group identity. Corrected to the quotient form on 2026-09-11.
- The paper cited P08 for channel multiplicity, where the canonical primitive list puts channel structure at P07. Corrected the same day.

## How it could be killed

A stable fundamental gauge sector with N of 4 or more, since ED's stable families run to three. A parity-violating abelian force, since ED's abelian coupling is blind to handedness.

## What it is not

Not a derivation of the Standard Model's gauge group. It says where groups of this shape come from, not which ones nature picked.
