---
id: mrw-efc6dd81fc95
type: note
title: Obstruction to naive finite-prime fiber lifting for lcm triangles
aliases: ["mrw-efc6dd81fc95", "Obstruction to naive finite-prime fiber lifting for lcm triangles"]
status: proved
tags: ["note", "proved", "erdos", "lcm", "finite-prime", "fiber", "obstruction", "patch-gate-audited"]
parents: [mrw-277fbbb4ccb9, mrw-2e217726536f]
refs: []
---

# Note: Obstruction to naive finite-prime fiber lifting for lcm triangles

## Statement

Naive finite-prime fiber lifting is false if it asserts that positive density alone forces a rich common outside-kernel fiber.

More precisely, fix a finite set \(P\) of primes and put
\[
M_P=\prod_{p\in P}p.
\]
Every integer \(n\) has a unique decomposition
\[
n=ks,
\]
where \(s\) is \(P\)-smooth and \((k,M_P)=1\).  The factor \(k\) is the outside-\(P\) kernel.  The positive-density set
\[
B_N(P)=\{n\le N:\ (n,M_P)=1\}
\]
has only the single \(P\)-smooth multiplier \(s=1\) in every outside-kernel fiber.  Hence positive density does not force any fiber to contain a nontrivial finite-prime lcm triangle.

## Proof

By elementary inclusion-exclusion,
\[
|B_N(P)|
=
\left(\prod_{p\in P}\left(1-\frac1p\right)\right)N+O_P(1),
\]
so \(B_N(P)\) has positive lower and upper asymptotic density for fixed \(P\).

If \(n\in B_N(P)\), then no prime in \(P\) divides \(n\).  In the decomposition \(n=ks\), with \(s\) \(P\)-smooth and \((k,M_P)=1\), this forces \(s=1\).  Therefore every outside-kernel fiber of \(B_N(P)\) contains at most the single \(P\)-smooth multiplier \(1\).  In particular, no fiber contains three distinct \(P\)-smooth multipliers forming a finite-prime lcm triangle.

Thus a finite-prime lifting principle needs an additional hypothesis, such as weighted fiber mass, projection balance, or an energy bound; positive density alone is not enough.

## Depends on

- [[wiki/nodes/mrw-277fbbb4ccb9|Erdos equal pairwise least-common-multiple problem]]
- [[wiki/nodes/mrw-2e217726536f|Prime-valuation criterion for equal pairwise lcm triples]]

## Used by

- Next #536 target: finite-prime weighted fiber extremal problem.

## Notes

- The safe lifting statement is only this: if three \(P\)-smooth multipliers form a finite-prime lcm triangle inside one fixed outside kernel \(k\), then multiplying all three by \(k\) gives an integer lcm triangle.
- Future work should bound weighted sums of finite-prime fiber extremal functions rather than trying to force one rich fiber from positive density alone.
