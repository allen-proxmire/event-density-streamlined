# Event Density — one result

Event Density (ED) builds physics from a discrete substrate whose defining feature is that time runs one way: commitment is irreversible. This repository holds one result of that program, and only what the result needs.

## The result

**In ED's substrate, handedness cannot be written into the rules. If the transport between channels carries a net handedness, that handedness came from a broken symmetry.**

More precisely, write the transport of N channels along a chain as H(k) = e^{ik}A + e^{−ik}B, where A is the forward hop and B the backward hop. **If the rules are symmetric under reflection, the winding number of det H(k) is zero for every N and every forward hop A.** That winding number is the measure of net handedness. A nonzero winding is possible in this family, but only when the reflection symmetry is broken.

- [Result.md](Result.md) — the statement, the proof and what it does and does not reach.
- [Assumptions.md](Assumptions.md) — everything the result assumes.
- `python tools/check_result.py` — a numerical check of the theorem (needs numpy).

## What it takes

- **Five ED primitives:** indexed, homogeneous space (P03); transport between neighbouring loci (P05); distinct channels (P07); a U(1) phase (P09); irreversible commitment (P11).
- **One definition:** amplitudes add and scale.
- **The fact that no ED primitive is a reflection.**
- **Three modelling assumptions:** the form of the transport map, how reflection acts on it, and the measure of handedness.

## How far it reaches

The result is modest. It is the general principle that a reflection-symmetric system cannot carry a reflection-odd invariant, made explicit for this family of transport maps and shown for every number of channels.

What makes it specific to ED is where the two ingredients come from:
- **The symmetry:** ED's rules supply it, because none of them is a reflection.
- **A question worth asking:** ED's arrow makes the transport non-Hermitian. Without the arrow, a handed transport would not be possible at all.

The result is about transport. It does not construct relativistic fermions, and it does not say which force in nature is handed.

## Source

The result comes from *The Clean Substrate Is Vector* (Allen Proxmire, 2026), included here as [The_Clean_Substrate_Is_Vector.md](The_Clean_Substrate_Is_Vector.md). [Result.md](Result.md) states only the part of that paper the result needs, and the review note at the top of the paper takes precedence over its text.
