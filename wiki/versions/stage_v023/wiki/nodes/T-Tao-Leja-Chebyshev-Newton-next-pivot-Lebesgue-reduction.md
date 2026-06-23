---
id: "T-Tao-Leja-Chebyshev-Newton-next-pivot-Lebesgue-reduction"
type: "theorem"
title: "Next-pivot Lebesgue reduction for finite Chebyshev-Leja Newton conditioning"
status: "proved"
tags: ["proved", "theorem"]
parents: ["Chebyshev root grid O(log n)-norming property", "finite Leja maximal pivot property", "ordinary prefix Lebesgue function identity", "T-Polynomial-root-logderivative-localization-principle"]
refs: [".pudim/attack-plans/AP-20260604T-tao-leja-chebyshev-next-pivot-reduction.json", ".pudim/oracle/responses/ORACLE-OS-20260604T-tao-leja-chebyshev-quadratic-upper-student-response.md", ".pudim/raw/student/20260604T-tao-leja-chebyshev-next-pivot-reduction.md", ".pudim/wiki/notes/tao-leja-chebyshev-next-pivot-reduction.md"]
---

# Theorem: Next-pivot Lebesgue reduction for finite Chebyshev-Leja Newton conditioning

## Statement

The Newton condition number for canonical finite Chebyshev-Leja ordering is bounded by a logarithmic norming factor times the sum of next-pivot Lebesgue functions.
\[
Lambda_N(pi(X_n)) <= 1 + C log n sum_{l=2}^n (1 + lambda_{l-1}(x_l)).
\]

## Dependencies

- Chebyshev root grid O(log n)-norming property
- finite Leja maximal pivot property
- ordinary prefix Lebesgue function identity
- [[wiki/nodes/T-Polynomial-root-logderivative-localization-principle|Polynomial root and logarithmic-derivative localization principle]]

## Proof and provenance references

- `.pudim/attack-plans/AP-20260604T-tao-leja-chebyshev-next-pivot-reduction.json`
- `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-leja-chebyshev-quadratic-upper-student-response.md`
- `.pudim/raw/student/20260604T-tao-leja-chebyshev-next-pivot-reduction.md`
- `.pudim/wiki/notes/tao-leja-chebyshev-next-pivot-reduction.md`

## Proof source health

_No extractable public proof fragment was found for this proved theorem-like node._

- .pudim/attack-plans/AP-20260604T-tao-leja-chebyshev-next-pivot-reduction.json: not a public proof-fragment source
- .pudim/raw/student/20260604T-tao-leja-chebyshev-next-pivot-reduction.md: not a public proof-fragment source
- .pudim/wiki/notes/tao-leja-chebyshev-next-pivot-reduction.md: not a public proof-fragment source

## Do not claim

- Do not claim the O(n^2) upper bound is proved.
- Do not claim source_open_solved_scoped.
- Do not rely on exact dyadic prefix structure.

## Tags

`proved`, `theorem`
