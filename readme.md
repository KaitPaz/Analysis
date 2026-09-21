# 📊 Algorithm Analysis & Data Structures

**Digging into how algorithms actually behave as problems scale — and using
that understanding to make real design decisions, not just pick a
data structure out of habit.**

This repo is where I worked through algorithmic complexity from the ground
up: reasoning about time and space growth, comparing search and sorting
strategies both theoretically and hands-on, hunting down a subtly broken
sort, and using everything from that analysis to justify concrete
optimization and data structure choices.

---

## 🎯 Skills demonstrated

| Skill | What it looks like here |
|---|---|
| **Big-O reasoning** | Analyzing how runtime and memory scale with input size, independent of any one implementation |
| **Algorithm comparison** | Linear vs. binary search, and iterative vs. recursive sorting — trading off simplicity, speed, and space |
| **Debugging** | Tracking down a sorting bug that looked correct on the surface but broke on real input |
| **Data structure selection** | Choosing between lists, sets, and maps based on what each one actually costs for the access pattern at hand |
| **Optimization** | Taking a working-but-slow solution and speeding it up with targeted structural and algorithmic changes |

## 🧭 What's inside

### Time & space complexity
Where it starts: building intuition for how an algorithm's cost grows with
input size, then putting that intuition to the test with a direct
comparison — linear search versus binary search — as a concrete example of
why complexity class matters more than raw speed on any single input.

### Sorting algorithms
Moving from analyzing complexity to producing it. I implemented and
compared sorting approaches from both the iterative and recursive angle,
then dug into a sort that looked fine until it wasn't — chasing down the
actual bug rather than papering over the symptom.

### Choosing and optimizing data structures
Where the analysis pays off. I compared lists, sets, and maps against the
access patterns they'd actually see, then took a working solution and
optimized it — applying what the complexity analysis predicted would
matter, and checking that it did.

## 📂 Structure

```
algorithm-analysis/
├── complexity/          # Time/space complexity exploration, linear vs. binary search
├── sorting/              # Iterative & recursive sorts, debugging exercise
└── optimization/         # Data structure selection & solution optimization
```

## 📄 Notes

A self-directed deep dive into algorithmic thinking — the goal wasn't just
to get working code, but to understand *why* one approach beats another,
and to be able to back that up with actual analysis.
