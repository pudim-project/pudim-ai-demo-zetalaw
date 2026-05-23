---
id: mrw-bf64e9def00c
type: proposition
title: Upward-closed high-support families force lower-shadow triples
aliases: ["mrw-bf64e9def00c", "Upward-closed high-support families force lower-shadow triples"]
status: proved
tags: ["proposition", "proved", "erdos", "lcm", "squarefree", "biased-measure", "lower-shadow", "union-cover", "monotone-family", "upward-closed", "support-tail", "patch-gate-audited"]
parents: [mrw-d0402aea6f58, mrw-cc4f876149b7, mrw-37dbc6aeedf9, mrw-30aae977a4b6]
refs: []
---

# Proposition: Upward-closed high-support families force lower-shadow triples

## Statement

Let \(P_k=\{p_1,\ldots,p_k\}\) be the first \(k\) primes and let \(\nu_{P_k}\) be the product law on \(2^{P_k}\) with \(\nu_{P_k}(p\in S)=1/p\).  Put
\[
S_{P_k}=\sum_{p\in P_k}\frac1p,
\qquad
H_{P_k,\theta}=\{S\subseteq P_k:\ |S|>\theta S_{P_k}\}.
\]

Fix \(0\le\theta<1\) and \(\eta>0\).  If \(\mathcal F_k\subseteq H_{P_k,\theta}\) is upward-closed and
\[
\nu_{P_k}(\mathcal F_k)\ge\eta,
\]
then, for all sufficiently large \(k\), \(\mathcal F_k\) contains a lower-shadow union-cover triple.  That is, there are \(A,B,C\in\mathcal F_k\) such that
\[
A,B\subsetneq C,\qquad A\ne B,\qquad A\cup B=C.
\]

## Proof

Let
\[
E_k=\{S\subseteq P_k:\ |P_k\setminus S|\le1\}.
\]
Under \(\nu_{P_k}\),
\[
\nu_{P_k}(E_k)
=
\prod_{i=1}^k\frac1{p_i}
\left(
1+\sum_{i=1}^k(p_i-1)
\right).
\]
This tends to \(0\) as \(k\to\infty\), because the product \(\prod_i p_i^{-1}\) decays faster than the displayed finite sum grows.

For all sufficiently large \(k\), we therefore have \(\nu_{P_k}(E_k)<\eta\).  Since \(\nu_{P_k}(\mathcal F_k)\ge\eta\), the family \(\mathcal F_k\) contains some set \(A_0\notin E_k\).  Thus \(P_k\setminus A_0\) contains two distinct primes \(x\) and \(y\).

By upward closure,
\[
A=A_0\cup\{x\},\qquad
B=A_0\cup\{y\},\qquad
C=A_0\cup\{x,y\}
\]
all lie in \(\mathcal F_k\).  They satisfy
\[
A,B\subsetneq C,\qquad A\ne B,\qquad A\cup B=C.
\]
This is the required lower-shadow union-cover triple.

## Depends on

- [[wiki/nodes/mrw-d0402aea6f58|Biased lower-shadow union-cover problem for Erdos 536]]
- [[wiki/nodes/mrw-cc4f876149b7|Intersecting deletion-trace obstruction for lower-shadow union covers]]
- [[wiki/nodes/mrw-37dbc6aeedf9|Biased squarefree residual problem for Erdos 536]]
- [[wiki/nodes/mrw-30aae977a4b6|Finite-core high-support cylinders force lower-shadow triples]]

## Used by

- Rules out monotone positive-mass high-support counterexamples to the biased lower-shadow union-cover route.

## Notes

- This proposition is deterministic after choosing one member of \(\mathcal F_k\) that misses at least two primes.  The biased-mass hypothesis is used only to ensure such a member exists for large \(k\).
- A genuine counterexample to [[wiki/nodes/mrw-d0402aea6f58|Biased lower-shadow union-cover problem for Erdos 536]] must therefore be nonmonotone, in addition to being non-rank-only and not a fixed finite-core high-support cylinder.
- The proposition does not prove the full trace theorem because arbitrary positive-mass families need not be upward-closed, and replacing a family by its upward closure may introduce triples that were not present in the original family.
