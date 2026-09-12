# The black-hole entropy coefficient 1/4

**The claim.** The paper claims that ED produces the coefficient, not just the area law: a black hole's entropy is S = A/4 in Planck units, with both halves of the 1/4 coming from ED's own geometry.

**Strength:** Not established. The calculation is general relativity's own. It needs the exact Schwarzschild metric in areal coordinates and r_s = 2GM, and ED derives neither.
**Sector:** black holes. **Paper:** [Thermal 2Pi_Entropy Coefficient](../Papers/Thermal%202Pi_Entropy%20Coefficient.md). **Ledger row:** 41.

---

## What review found

- **The algebra is correct, and it is the standard Gibbons–Hawking calculation:** continue to imaginary time, require no conical defect, read off T = κ/2π, integrate the first law.
- **S = A/4 needs two things GR-I does not derive:** r_s = 2GM exactly, and A = 4πr_s². Together they are the Schwarzschild metric in areal-radius coordinates. With r_s = kGM the first law gives S = A/(2k), so the 1/4 requires k = 2; that 2 comes from GR-I's identification b ∼ 1 + 2Φ, which matches the metric to Newtonian gravity rather than deriving it. GR-I builds its metric in isotropic form, g_ij = b⁻¹δ_ij. In that form the horizon area r²/b diverges at b = 0, and the second-order metric gives PPN β = 0, which observation excludes. The switch to the areal form is not justified.
- **A statement on this page was wrong.** It said the exact horizon radius did not matter because a horizon forming at all "is all this derivation needs". The coefficient depends directly on that radius.
- **Net:** ED reproduces GR's 1/4 by adopting GR's metric. It gives no independent derivation.

## What it uses from the foundation

Nothing directly. It runs on one earlier ED result, the shape of the horizon.

| | item | how it enters |
|---|---|---|
| — | (none used directly) | |

## What it uses from earlier ED results

| result | what it supplies | where that stands |
|---|---|---|
| GR-III's vacuum profile | the horizon's shape, b(r) = 1 − r_s/r, and from its slope the surface gravity κ = 1/(2r_s) | the linear rule clipped at b = 0; passes through GR-I's lapse, which rests on the band-accounting premise; the areal-coordinate reading is not derived |
| GR-I | the relation g₀₀g_rr = −1 | holds in areal coordinates only, which GR-I does not establish (see its review note) |

## What it borrows from standard physics

| borrowed | why it is fair, and what it costs |
|---|---|
| Euclidean continuation (turning time imaginary) | the same tool every derivation of the Hawking temperature uses |
| the smoothness condition (no conical defect) | standard; it turns the geometry into a temperature |
| the Schwarzschild metric in areal coordinates | effectively borrowed: ED's metric matches it only after a change of coordinate form that GR-I does not justify |

## How it goes

Near the horizon, the profile takes the Rindler form: measure proper distance from the horizon and the metric becomes −κ²ρ²dt² + dρ². Turn time imaginary and this is a flat plane in polar coordinates, with κτ as the angle. The plane is smooth at its centre only if the angle runs a full 2π. So imaginary time has period 2π/κ, which is a temperature T = κ/(2π). Feed that into the first law with M = r_s/2 and integrate: S = πr_s² = A/4.

## What this leans on, stated plainly

- The horizon shape comes from GR-III, whose lapse comes from GR-I, and that lapse rests on a band-accounting premise that is argued rather than closed.
- The areal-coordinate form of the metric and r_s = 2GM, neither derived (see "What review found").
- The 2π comes from a reversible-time device, used in a theory whose defining primitive is an irreversible arrow. The paper flags a continuation-free route as open, and its own attempt at one failed (§4b).

## How it could be killed

A consistent derivation of ED's metric in a single coordinate form that is not Schwarzschild at second order would remove it. The isotropic form GR-I uses is already such a case.

## What it is not

Not a derivation of the 1/4 independent of general relativity. Not a derivation of the horizon's location. Not a continuation-free derivation of the 2π.
