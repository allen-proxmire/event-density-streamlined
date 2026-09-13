# Event Density: one result

Event Density (ED) is an attempt to describe the world as a discrete substrate in which time runs one way: once something happens, it can't be undone. This repository holds one result about that kind of world, and only what the result needs.

**The result: a world whose rules look the same in a mirror can't have handedness written into those rules. If it has a handedness, the handedness was chosen by the state the world is in.**

## The idea in plain words

Picture a highway with several lanes. Traffic hops forward or backward from one stretch of road to the next, and at each hop it can also switch lanes in some pattern. That pattern of hops is the *transport*.

Now ask whether the traffic has a built-in twist: a preference for spiralling one way rather than the other. A number called the *winding number* measures that twist. Zero means no net preference.

The result says that **if the rules for hopping look the same in a mirror, the twist is exactly zero**, for any number of lanes and any hopping pattern. A mirror flips forward and backward and flips the lanes left to right. If the rules survive that flip, every bit of twist one way is matched by the same amount the other way, and they cancel.

Two things give the result its content:

- **Twist is only possible because time runs one way.** If hopping forward and hopping backward were perfect time-mirrors of each other, the twist would be zero no matter what. The irreversibility is what opens the door.
- **Twist really does appear when the mirror symmetry is broken.** Traffic that only ever hops forward twists once per lane.

Put together: **one-way time makes handedness possible, and mirror-symmetric rules keep it out of the laws.** So if an ED world has a handedness, it wasn't written into the rules. It was picked by the state, the way a magnet picks a direction that its laws don't prefer.

This is a "you can't get there from here" result, a kind that has a long history of guiding physics. The Nielsen–Ninomiya theorem, which says you can't simply put handed particles on a regular lattice, is similar in spirit and shaped decades of work. This result is far smaller, but it is the same kind of thing: a guardrail that says where handedness has to come from.

## Precisely

Write the transport of N lanes (channels) as H(k) = e^{ik}A + e^{−ik}B, where A is the forward hop, B the backward hop, and k the wavenumber. If the transport is symmetric under reflection, the winding number of det H(k) is zero for every N and every A.

## What it assumes

- **From ED:** space is uniform, phases are carried between neighbouring points, channels are distinct objects, the phase is a complex number, and time runs one way. None of ED's rules is a mirror reflection.
- **Modelling choices:** the form of H(k) above, how a reflection acts on it, and the winding number as the measure of handedness.

## How far it reaches

The result is modest. It is the general principle that a mirror-symmetric system can't carry a mirror-odd quantity, made explicit for this model and shown for every number of channels. It is about this model of transport only. It does not say how nature's handedness arose, or which force in nature is handed.

## Check it yourself

```
python tools/check_result.py
```

The script (needs numpy) tests the result for 1 to 6 channels, along with the two cases above: forward-only traffic, and traffic without one-way time.

## Files

- [Paper.md](Paper.md): the full proof, every assumption, the controls and the limits.
- [Result.md](Result.md): the statement and proof on one page.
- [Assumptions.md](Assumptions.md): everything the result assumes.
