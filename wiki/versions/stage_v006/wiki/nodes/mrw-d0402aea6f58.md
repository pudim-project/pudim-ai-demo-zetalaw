---
id: mrw-d0402aea6f58
type: problem
title: Biased lower-shadow union-cover problem for Erdos 536
aliases: ["mrw-d0402aea6f58", "Biased lower-shadow union-cover problem for Erdos 536"]
status: open
tags: ["problem", "open", "erdos", "lcm", "squarefree", "biased-measure", "lower-shadow", "union-cover", "support-tail", "finite-prime", "next-frontier"]
parents: [mrw-37dbc6aeedf9, mrw-3c39ca3d1973, mrw-053bc325c601, mrw-9afb17b1b84a, mrw-4daa694d9526]
refs: []
---

# Problem: Biased lower-shadow union-cover problem for Erdos 536

## Statement

Let \(P\) be a finite set of primes and let \(\nu_P\) be the product law on \(2^P\) under which
\[
\nu_P(p\in S)=\frac1p.
\]
Put
\[
S_P=\sum_{p\in P}\frac1p
\]
and, for \(0\le\theta<1\),
\[
H_{P,\theta}=\{S\subseteq P:\ |S|>\theta S_P\}.
\]

For \(P_k=\{p_1,\ldots,p_k\}\), the biased lower-shadow union-cover problem asks whether the following statement is true.

For every fixed \(0\le\theta<1\) and every \(\eta>0\), every family
\[
\mathcal F\subseteq H_{P_k,\theta}
\]
with
\[
\nu_{P_k}(\mathcal F)\ge\eta
\]
contains three members \(A,B,C\in\mathcal F\) such that
\[
A,B\subsetneq C,\qquad A\ne B,\qquad A\cup B=C
\]
for all sufficiently large \(k\).

Equivalently, does every high-support family of fixed positive biased mass eventually fail to be lower-shadow union-cover-free?

## Evidence

By [[wiki/nodes/mrw-3c39ca3d1973|Pair-link shadow criterion for biased squarefree residuals]], a triple satisfying
\[
A,B\subsetneq C,\qquad A\ne B,\qquad A\cup B=C
\]
is a squarefree cosunflower triple.  Thus an affirmative answer to this problem would imply
\[
M_{P_k}(\theta)\to0
\]
for the biased squarefree residual in [[wiki/nodes/mrw-37dbc6aeedf9|Biased squarefree residual problem for Erdos 536]].

The problem is only a sufficient squarefree support-level route.  It is not equivalent to the full pair-link condition, because a pair-link completion may have
\[
A\triangle B\subseteq C\subseteq A\cup B
\]
without satisfying \(C=A\cup B\).  It also does not by itself prove the exponent-grid residual condition
\[
R_P(\theta)\to0
\]
from [[wiki/nodes/mrw-4daa694d9526|Low-support growing-prime criterion for Erdos 536]].

The ambient sparsity obstruction [[wiki/nodes/mrw-053bc325c601|Ambient cosunflower sparsity for biased squarefree supports]] shows that the full high-support event has vanishing random cosunflower triple density under \(\nu_P^3\).  Therefore a proof cannot be a plain ambient-density supersaturation argument.  The binary-choice obstruction [[wiki/nodes/mrw-9afb17b1b84a|Binary-choice squarefree obstruction to pointwise support envelopes]] shows that pointwise high-support cardinality also does not suffice, although the known block-transversal spikes have vanishing biased mass.

The current local structural reduction is [[wiki/nodes/mrw-cc4f876149b7|Intersecting deletion-trace obstruction for lower-shadow union covers]]: a lower-shadow union-cover-free family has pairwise-intersecting deletion traces below every top set.

## Depends on

- [[wiki/nodes/mrw-37dbc6aeedf9|Biased squarefree residual problem for Erdos 536]]
- [[wiki/nodes/mrw-3c39ca3d1973|Pair-link shadow criterion for biased squarefree residuals]]
- [[wiki/nodes/mrw-053bc325c601|Ambient cosunflower sparsity for biased squarefree supports]]
- [[wiki/nodes/mrw-9afb17b1b84a|Binary-choice squarefree obstruction to pointwise support envelopes]]
- [[wiki/nodes/mrw-4daa694d9526|Low-support growing-prime criterion for Erdos 536]]

## Used by

- Next #536 route: prove a biased weighted trace theorem forcing a non-intersecting deletion trace in every positive-mass high-support family, or construct a genuine nonvanishing counterexample.

## Notes

- This node is open.  No positive-mass counterexample is known locally.
- Single support layers and sparse rank sets are plausible lower-shadow-free examples but have vanishing biased rank mass on the \(S_{P_k}\to\infty\) scale.
- Parity or residue-class rank restrictions block one-deletions but still admit multi-deletion covers in typical large supports.
- Fixed-star or finite-junta families can have positive mass, but they appear downward-rich enough to create two disjoint deletions below a typical top set.
- The next proof mechanism should be weighted lower-shadow double counting plus a biased intersecting-trace bound, not another fixed-\(P\) prefix table.
