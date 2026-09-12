# Results

Sixteen results from the ED Generative corpus. They were chosen because their papers use only the items on [the foundation](../Foundation.md) and nothing else. Each page gives:

- what the paper claims
- what a review of 2026-09-12 found
- which foundation items it uses
- what it borrows from standard physics
- how it could be killed

## What review found

None of the sixteen derives anything that was not already known:

- **Seven are correct:** six restate standard results in ED vocabulary, and one is a modest result of ED's own.
- **Four are identifications:** they say a known phenomenon is a substrate object, without calculating anything.
- **Five, all in the gravity block, are not established:** they rest on steps that do not hold as written.

The list is still worth having, because it makes this visible. Every borrowing was already named on the pages, which is what made a complete review possible.

## The sixteen

| page | verdict | sector | row |
|---|---|---|---|
| [No anyons in three dimensions](RQM_02_No_Anyons.md) | textbook result, restated | relativistic QM | 91 |
| [The spinor frame is unique](RQM_01_Spinor_Frame.md) | textbook result, restated | relativistic QM | 90 |
| [Charge as a winding number](SUB_01_Charge_As_Winding.md) | textbook result, restated (with an honest negative) | substrate tests | 93 |
| [Gauge groups and channel multiplicity](QFT_01_Gauge_Group.md) | textbook result, restated; Standard Model match fails | QFT | 84 |
| [The 1/2 in kinetic energy](QM_01_Galilean_Asymmetry.md) | textbook result, restated | QM kinematics | 89 |
| [Geodesic motion](GRAV_01_Geodesic_Motion.md) | textbook result, restated | gravity | 66 |
| [If the world is left-handed, it chose to be](SUB_02_Parity_Is_Spontaneous.md) | modest ED-specific result | substrate tests | 94 |
| [The horizon as a decoupling surface](BH_02_Horizon_Mechanism.md) | identification | black holes | 28 |
| [The Hawking temperature](BH_03_Hawking_Temperature.md) | identification | black holes | 36 |
| [Four kinds of horizon as one object](BH_04_One_Horizon_Law.md) | identification | black holes | 320 |
| [Primordial and present-day gravitational waves](COS_01_Primordial_Tensor_Modes.md) | identification | cosmology | 44 |
| [ED's gravitational class](GRAV_02_Khronometric_Class.md) | not established | gravity | 67 |
| [Gravitational-wave speed](GRAV_03_Gravity_Waves_At_c.md) | not established | gravity | 68 |
| [The speed of the extra gravitational mode](GRAV_04_Khronon_Speed.md) | not established | gravity | 70 |
| [The preferred-frame parameter α₂](GRAV_05_Alpha2_Zero.md) | not established | gravity | 71 |
| [The black-hole entropy coefficient 1/4](BH_01_Entropy_Coefficient.md) | not established | black holes | 41 |

## What the verdicts mean

- **Textbook result, restated.** The result is correct, but it is known physics or mathematics. ED supplies vocabulary and, at most, an assumed input such as the number of dimensions.
- **Modest ED-specific result.** A correct statement about an ED model that is not simply a restatement. Its physical reach is limited.
- **Identification.** A known phenomenon is said to be a particular substrate object. Nothing is calculated, and no distinctive test follows.
- **Not established.** The argument relies on a step that does not hold as written.

## The gravity block's shared problems

- **The metric is fixed only to first order.** In the isotropic form GR-I uses, the second-order term gives PPN β = 0, which observation excludes. The Schwarzschild form used for perihelion precession, horizons and entropy is reached by switching coordinate form, and that switch is not derived.
- **ED's only built dynamics is one scalar.** It is a diffusion equation. Tensor modes and waves at c are written in by hand, not derived.
- **GR-III and GR-IV contradict each other on the scalar mode's speed.** GR-III's argument for c_s = c does not survive the standard formula GR-IV relies on.
- **GR-IV's tiny couplings run into strong coupling.** At λ ∼ 10⁻⁹³, the literature's strong-coupling scale is near 4×10⁻¹⁹ eV.

The definite calculations behind these points can be re-run with `python tools/run_checks.py` (see the [main README](../README.md#calculations-anyone-can-run)).
- **The lapse rests on a band-accounting premise that is argued, not closed.**

## What holds up

- **Correct mathematics, where it is used:** anyons, Clifford uniqueness, winding numbers, the parity-symmetric winding theorem.
- **Genuine negative results, honestly reported:** a determined Coulomb field does not arise without leaving ED ([charge](SUB_01_Charge_As_Winding.md)), and the attempt to get the thermal 2π without Euclidean continuation failed (Thermal2Pi §4b).
- **Two correct general statements.** At first order, a single scalar b setting g₀₀ ∝ b and g_ij ∝ b⁻¹ gives the factor of two in light bending. In khronometric gravity with both speeds luminal, α₂ vanishes identically.
- **Two conjectures worth stating as conjectures:** that a fundamental arrow of time implies a preferred foliation, and that parity violation is spontaneous and correlated with the matter/antimatter sign.

## What is not here

- results that are measured rather than derived
- results that are unit bookkeeping
- the roughly 130 results that need a further local assumption

Those live in the ED Generative repository.
