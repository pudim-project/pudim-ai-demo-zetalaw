---
id: mrw-900d84ddee24
type: problem
title: Exact inverse-tail floor formula at s=7
aliases: ["mrw-900d84ddee24", "Exact inverse-tail floor formula at s=7"]
status: superseded
tags: ["scout-forage", "candidate", "superseded", "tail-zeta", "inverse-tail"]
parents: [mrw-6ad81d0b87f7]
refs: []
---

# Problem: Exact inverse-tail floor formula at s=7

## Statement

Problem statement: Find an exact computable formula for
\[
\left\lfloor \zeta_n(7)^{-1}\right\rfloor,
\qquad
\zeta_n(s)=\sum_{k=n}^{\infty} k^{-s}.
\]

Literature status: advisory open candidate. The 2018 paper by Kim and Song defines the tail \(\zeta_n(s)\), reviews exact formulas for \(s=2,3,4,5\), records an \(s=6\) formula valid for sufficiently large \(n\), and states that no such formula was known for integer \(s>6\) at that time. A 2024 AIMS Mathematics article studies asymptotic inverse-tail formulas for zeta, Hurwitz zeta, and Dirichlet \(L\)-functions, but this local pass did not verify an exact \(s=7\) floor formula in the literature.

References:
- Donggyun Kim and Kyunghwan Song, "The inverses of tails of the Riemann zeta function", Journal of Inequalities and Applications 2018, article 157. https://link.springer.com/article/10.1186/s13660-018-1743-6
- Zhenjiang Pan and Zhengang Wu, "The inverse of tails of Riemann zeta function, Hurwitz zeta function and Dirichlet L-function", AIMS Mathematics 9(6), 16564-16585, 2024. DOI: https://doi.org/10.3934/math.2024803

Connection to THEORY: This is a tail-partition analogue of the zeta-law normalization already used in the manuscript.

Expected difficulty: low-to-medium if a telescoping rational enclosure can be audited; not solved until all algebraic identities and finite cases are verified locally.

## Literature Status

Imported from scout-forage response, then audited locally. The 2018 source states that no such exact formula was known for integer \(s>6\) at publication. A bounded primary-source check found a 2024 asymptotic inverse-tail paper, but no exact \(s=7\) floor formula.

## Connection To Theory

See the candidate block above and the response artifact.

## Solved by

- [[wiki/nodes/mrw-28bcccec471e|Exact inverse-tail floor formula at s=7]]

## Source References

- Donggyun Kim and Kyunghwan Song, "The inverses of tails of the Riemann zeta function", Journal of Inequalities and Applications 2018, article 157. https://link.springer.com/article/10.1186/s13660-018-1743-6
- Zhenjiang Pan and Zhengang Wu, "The inverse of tails of Riemann zeta function, Hurwitz zeta function and Dirichlet L-function", AIMS Mathematics 9(6), 16564-16585, 2024. DOI: https://doi.org/10.3934/math.2024803

## Notes

- priority: 1
- status after proof audit: solved locally by a proved theorem node.
