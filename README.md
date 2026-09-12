# Event Density — just the facts

Event Density is a research program that tries to build physics out of a discrete substrate whose one special feature is that becoming is an irreversible commitment. This folder is not the program. It is the part of the program that can be backed, written so that someone outside it can check the work.

It holds three things.

**[Foundation.md](Foundation.md)** — the 53 items ED starts from: 49 assumptions and 4 arguments, plus 3 definitions that are names rather than claims. Every item was read in the paper that declares it. Nothing on the list is derived from anything else on the list.

**[Results/](Results/)** — the 16 results that follow from those 53 with nothing hidden added. One page each: what it claims, which foundation items it uses, what it borrows from published physics, what it leans on, and how it could be killed.

**[Papers/](Papers/)** — the papers behind those results, plus the four upstream papers they depend on.

**[ED_Streamlined_Theory.xlsx](ED_Streamlined_Theory.xlsx)** — the same material as a workbook: the foundation, the results, a map of which result uses which assumption, and what was left out. It is generated from the markdown by [tools/build_workbook.py](tools/build_workbook.py), not maintained by hand, so the two cannot drift apart. Edit the markdown and re-run `python tools/build_workbook.py` to rebuild it.

## The rule

Everything here traces back to Foundation.md. A result that needs an assumption not on that page does not belong on this list, however good the result is.

## What is deliberately absent

The full corpus is roughly 280 papers. Most of its results hold *given a further local assumption* — around 130 of them. Those are real work and they are honestly labelled in the main repository, but they are not on this list, because this list answers a narrower question: what follows from the starting page alone.

Also absent: results that are measured rather than derived, and results that are true but amount to arithmetic on units.

## The one thing a reader should know up front

Six of the sixteen pass through the same step: ED's emergent metric, whose lapse rests on a band-accounting premise that is argued rather than closed. If that premise fails, those six fall together. They are marked on every page that carries them and in the [Results index](Results/README.md).

## Where this comes from

Assembled 2026-09-11 from the `ED Generative` repository and its claims ledger, `ED_ItemizedTheory_TieredClaims_v2.xlsx`. That repository remains the canonical source; this one is the readable subset.
