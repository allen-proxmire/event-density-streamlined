# Black-hole entropy: the coefficient 1/4

**The claim.** A black hole's entropy is a quarter of its horizon area in Planck units, S = A/4. ED produces the 1/4, not just the area law.

**Strength:** follows from the foundation, with two borrowed tools.
**Sector:** black holes. **Paper:** [Thermal 2Pi_Entropy Coefficient](../Papers/Thermal%202Pi_Entropy%20Coefficient.md). **Ledger row:** 41.

---

## What it uses from the foundation

Nothing directly. It runs entirely on one earlier ED result, the shape of the horizon, which is itself built from the primitives.

| | item | how it enters |
|---|---|---|
| — | (none used directly) | |

## What it uses from earlier ED results

| result | what it supplies | where that stands |
|---|---|---|
| GR-III's vacuum profile | the horizon's shape, b(r) = 1 − r_s/r, and from its slope the surface gravity κ = 1/(2r_s) | built from the primitives, but through GR-I's lapse, which rests on the band-accounting premise (see "What this leans on") |
| GR-I | the relation between the two metric parts, g₀₀g_rr = −1 | same chain |

## What it borrows from standard physics

| borrowed | why it is fair, and what it costs |
|---|---|
| Euclidean continuation (turning time imaginary) | the same tool every derivation of the Hawking temperature uses, general relativity included. ED is level with GR here, not ahead of it |
| the smoothness condition (no conical defect) | standard. It is what turns the geometry into a temperature |

## How it goes

Near the horizon, ED's own profile takes the Rindler form: measure proper distance from the horizon and the metric becomes −κ²ρ²dt² + dρ². Turn time imaginary and this is a flat plane in polar coordinates, with κτ as the angle. A plane is smooth at its centre only if the angle runs a full turn, 2π. So imaginary time has period 2π/κ, which is a temperature T = κ/(2π). Feed that into the first law and integrate: S = πr_s² = A/4.

Both halves of the 1/4 come from ED's own geometry: the 1/2 from the profile's slope, the 2π from the angle of one turn around the horizon.

## What this leans on, stated plainly

- The horizon shape comes from GR-III, whose lapse comes from GR-I. GR-III closes GR-I's α = 1 assumption **only modulo a band-accounting premise**. If that premise fails, this result falls with the rest of the gravity block.
- The exact horizon radius, the 2 in 2GM/c², is not pinned. The simulations show a horizon forms and its size grows in step with the mass, which is all this derivation needs.
- The 2π is obtained with a reversible-time device in a theory whose defining primitive is an irreversible arrow. The paper flags a substrate-native, continuation-free route as the genuine open frontier (§4b).

## How it could be killed

A demonstration that the rule's strong-coupling behaviour does not form a finite-radius horizon, or that the near-horizon geometry is not Rindler, would take the 1/4 with it. (GR-III §11.4; Thermal2Pi §2, which reports the numerical check b/(κρ)² → 1.)

## What it is not

Not a derivation of the horizon's location from the substrate. Not a continuation-free derivation of the 2π. Not a claim to have gone beyond general relativity here: ED reads the 2π off the same near-horizon geometry GR does, and its addition is that the geometry itself is derived from the bandwidth rule rather than assumed.
