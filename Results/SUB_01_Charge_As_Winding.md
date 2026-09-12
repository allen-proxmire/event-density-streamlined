# Charge as a winding number

**The claim.** The substrate carries an integer that cannot change: how many times the polarity angle winds around a closed loop. It is exactly quantized, it is conserved, and the arrow is what protects it. That integer is the skeleton of electric charge.

**Strength:** follows from the foundation, with the field itself still missing.
**Sector:** substrate tests. **Paper:** [Charge As Topology_Winding_Integral Gauss Law](../Papers/Charge%20As%20Topology_Winding_Integral%20Gauss%20Law.md). **Ledger row:** 93.

---

## What it uses from the foundation

| | item | how it enters |
|---|---|---|
| P09 | polarity is a U(1) angle | the angle that does the winding |
| P05 | polarity transport | the discrete connection the winding is measured along |
| P11 | commitment is irreversible | the protection. Changing the winding would mean uncommitting a polarity. This protects the number while its loop exists; it does not make the loop permanent |
| P04 | bandwidth | the weak channel through which the winding couples to anything |

## What it borrows from standard physics

| borrowed | why it is fair, and what it costs |
|---|---|
| that a circle's loops are counted by the integers | standard topology, and the reason the winding is exact rather than approximate |

## How it goes

Ask first what topological quantity the participation graph admits at all, without mentioning charge. The survivor is the phase accumulated around a closed loop. Once polarity is committed single-valued, that phase is a whole number of turns, exactly. Undoing a turn would require uncommitting, which the arrow forbids, so the number is conserved and protected rather than merely stable. It then couples weakly through bandwidth, and the circulation around any enclosing loop is the same number of turns regardless of the loop's size or shape, which is a Gauss law in integral form.

## What this leans on, stated plainly

- **The field is withheld.** At the discrete layer ED gets the integral Gauss law but not a determined local inverse-square field. The paper's own fork says you can have that field only by giving up either orientation-blindness or the arrow, which means leaving ED.
- The winding is inert: it couples weakly and does not drive the stability landscape.
- **What is protected, and what is not** (scope added 2026-09-12). The integer cannot change while the loop that carries it exists. The loop is not itself protected: it is made of live participations, and where participation ceases there is no phase to difference and the number has nothing to be a property of, with nothing uncommitted. `Paper_ED_CCC` §3.6.1 turns on exactly this, using it to clear residual charge at the end of a cosmic aeon. The consequence is worth saying plainly: in this account charge is a property of a live loop around a thing, not of the thing alone.
- The quantization and the loop-independence were confirmed in the certified simulator to machine precision. The argument is structural; the simulation checks it.
- The paper is strict that no charge spectrum was fitted. Reproducing the familiar ±1 and ∓⅓ pattern by fitting a topology to those values would violate its own discipline, and is not claimed.

## How it could be killed

A demonstration that the committed holonomy is not quantized to integers, or that the winding can change without an uncommitting. A measurement showing the circulation is not loop-independent. Or a determined local inverse-square field produced while keeping both orientation-blindness and the arrow.

## What it is not

Not a derivation of electric charge, its spectrum, or Coulomb's law. It is the skeleton: an exact, protected, conserved integer of the right shape.
