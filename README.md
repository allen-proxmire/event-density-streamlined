# Event Density — just the derivations

Event Density is a research program that builds physics from a relational, discrete substrate whose one special feature is that time is one-way. Becoming is an irreversible commitment. This folder is not the entire program. The core theory can be found here, and the immediate derivations. 

The repository holds four things.

**[Foundation.md](Foundation.md)** — the 53 items ED starts from: 49 assumptions and 4 arguments, plus 3 definitions that are names rather than claims. Every item was read in the paper that declares it. Nothing on the list is derived from anything else on the list.

**[Results/](Results/)** — the 16 results that follow from those 53 with nothing hidden added. One page each: what it claims, which foundation items it uses, what it borrows from published physics, what it leans on, and how it could be killed.

**[Papers/](Papers/)** — the papers behind those results, plus the four upstream papers they depend on.

**[ED_Streamlined_Theory.xlsx](ED_Streamlined_Theory.xlsx)** — the same material as a workbook: the foundation, the results, a map of which result uses which assumption, and what was left out. It is generated from the markdown by [tools/build_workbook.py](tools/build_workbook.py), not maintained by hand, so the two cannot drift apart. Edit the markdown and re-run `python tools/build_workbook.py` to rebuild it.

## The rule

Everything here traces back to Foundation.md and the 53 assumptions. A result that needs another assumption not on that page does not belong on this list, however good the result is. There are many results like this, with the need for an additional assumption, but they do not appear here. 

## What is deliberately absent

The full corpus is roughly 280 papers. Most of its results hold *given a further local assumption* — around 130 of them. Those are real work and they are honestly labelled in the main repository, but they are not on this list, because this list answers a narrower question: what follows from the starting assumptions alone.

Also absent: results that are measured rather than derived, and results that are true but amount to arithmetic on units.

