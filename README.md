# Event Density — an honest account

Event Density (ED) is a research program that tries to build physics from a relational, discrete substrate whose one special feature is that time runs one way: becoming is an irreversible commitment. The full corpus is about 280 papers. This repository sets out, without inflation, what the core of it amounts to.

## The short answer

As of 2026-09-12, **ED is an interpretive framework, not yet a theory you can calculate from.** Its 13 primitives are stated in prose, and they do not define a mathematical model that produces numbers.

The sixteen results collected here are the best of the corpus: the ones whose papers use only the starting assumptions. On review, none of them derives anything that was not already known.

- **7 are correct.** Six restate standard results in ED vocabulary, and one is a modest result specific to ED.
- **4 are identifications.** A known phenomenon is said to be a substrate object, without calculation.
- **5 are not established.** They are all in the gravity block and rest on steps that do not hold as written.

This is stated up front because the purpose of the repository is an honest account.

## What holds up

- **The bookkeeping.** Every assumption is listed, and every borrowing from standard physics is named on the page that uses it. That is what made a complete review possible in one pass. Most speculative programs cannot be checked this way.
- **The mathematics, where it is used.** The anyon, Clifford and winding-number results, and the parity-symmetric winding theorem, are correct.
- **Negative results, reported rather than buried.** A Coulomb field cannot be had without leaving ED. The attempt at a continuation-free thermal 2π failed. Both are recorded.
- **Conjectures worth keeping as conjectures:** that a fundamental arrow of time implies a preferred foliation, and that parity violation is spontaneous and tied to the matter/antimatter sign.

## What the repository holds

**[Foundation.md](Foundation.md)** — the 53 items ED starts from: 49 assumptions and 4 arguments, plus 3 definitions that are names rather than claims.

**[Results/](Results/)** — the sixteen results, one page each, with a review verdict. Each page gives what the paper claims, what review found, which foundation items it uses, what it borrows and how it could be killed.

**[Papers/](Papers/)** — the papers behind those results, plus the four upstream papers they depend on. Each opens with a review note that takes precedence over the text below it.

**[ED_Streamlined_Theory.xlsx](ED_Streamlined_Theory.xlsx)** — the same material as a workbook. It is generated from the markdown by [tools/build_workbook.py](tools/build_workbook.py), so edit the markdown and re-run `python tools/build_workbook.py`.

## The rule

A result appears here only if its paper uses nothing beyond Foundation.md. Passing that rule means a result adds no hidden assumptions. It does not make the result a derivation: most results that pass it restate known physics.

## How the review was done

On 2026-09-12 every file in this repository was reviewed by Claude, an AI model. The problems it found are recorded on the result pages and in the review notes at the top of each paper.

The earlier claims in this repository had been cross-checked by AI models too, and those checks missed these problems. So do not take the review's authority on trust either. The central technical points are short calculations that anyone with graduate-level physics can check:

- PPN β for the isotropic metric
- the chirality of hypercharge
- the khronometric scalar-speed formula

A physicist should confirm them before they are relied on in either direction.

A second, independent pass then took every claim whose own equations give a definite number or structure, and computed it. Those calculations are collected below.

## Calculations anyone can run

    python tools/run_checks.py

The script needs numpy and runs in seconds. Each check computes something the papers' own equations determine and compares it with established physics or mathematics.

| # | check | result |
|---|---|---|
| 1 | PPN γ and β for GR-I's metric as written | γ = 1 passes (light bending). β = 0 fails: Mercury's perihelion comes out at 57.3″ per century, against 43.0″ measured |
| 2 | Horizon area in that metric | diverges; a finite area needs a coordinate switch that is not derived |
| 3 | Entropy coefficient with r_s = kGM | S = A/(2k); the 1/4 needs k = 2, which is matched to Newton |
| 4 | Does GR-III's rule carry waves? | no: ω = −iDk², pure decay |
| 5 | Scalar speed, GR-III's route against GR-IV's | contradiction: GR-III's λ = 0 gives c_s = 0 |
| 6 | α₂ numerator on the luminal surface | vanishes, correctly, but only restates check 5 |
| 7 | Strong-coupling scale at λ ∼ 10⁻⁹³ | about 4×10⁻¹⁹ eV, so not perturbative |
| 8 | U(N) = SU(N) × U(1)? | no: it is (SU(N) × U(1))/Z_N |
| 9 | "No parity-violating abelian force" | already contradicted by Standard Model hypercharge |
| 10 | Parity-clean winding for N = 1–6 | zero, correct; standard symmetry reasoning |
| 11 | Dirac and Weyl gammas are similar | correct; Pauli's theorem |
| 12 | a₀ = cH₀/2π against the fitted a₀ | 0.87–0.94 of it; a known coincidence |
| 13 | Planck-mass remnant formulas | identities; they constrain nothing |
| 14 | r_s ∝ M in GR-III's simulations | exact by linearity, so built in |
| 15 | The ½ in kinetic energy | the Taylor coefficient of an inherited formula; an input |

Checks 5, 6 and 7 use formulas quoted from the khronometric literature rather than re-derived here. The corpus's own numerical fits (a₀(z), BTFR) are outside this repository and were not re-run.

## What is deliberately absent

Most of the corpus's results hold only *given a further local assumption*: around 130 of them. They are not on this list, which asks the narrower question of what follows from the starting assumptions alone. Also absent are results that are measured rather than derived, and results that amount to arithmetic on units.
