---
id: mrw-55a8d9eddd2e
type: problem
title: Prime-biased weighted union-free theorem
aliases: ["mrw-55a8d9eddd2e", "Prime-biased weighted union-free theorem"]
status: open
tags: ["problem", "open", "erdos", "lcm", "squarefree", "biased-measure", "union-free", "lower-shadow", "support-tail", "finite-prime", "next-frontier"]
parents: ["mrw-b4075311abd3", "mrw-d0402aea6f58", "mrw-37dbc6aeedf9", "mrw-4daa694d9526", "mrw-2a2c5551301e", "mrw-67f99fecf9e2"]
refs: ["references/sources/20260519T101422Z-erdos-536-union-free-context.md"]
---

# Problem: Prime-biased weighted union-free theorem

## Statement

Let
\[
P_k=\{p_1,\ldots,p_k\},\qquad
\nu_k(p_i\in S)=\frac1{p_i},
\qquad
S_k=\sum_{i\le k}\frac1{p_i},
\]
and, for \(0\le\theta<1\), let
\[
H_{k,\theta}=\{S\subseteq P_k:\ |S|>\theta S_k\}.
\]
For a family \(\mathcal F\subseteq2^{P_k}\), call \(\mathcal F\) union-free if
there are no three distinct \(A,B,C\in\mathcal F\) with \(A\cup B=C\).

The prime-biased weighted union-free theorem asks whether
\[
U_k(\theta)=
\sup\{\nu_k(\mathcal F):\ \mathcal F\subseteq H_{k,\theta}
\text{ and }\mathcal F\text{ is union-free}\}
\]
satisfies
\[
U_k(\theta)\to0
\]
for every fixed \(0\le\theta<1\).

## Evidence

By [[mrw-b4075311abd3]], this is exactly the biased lower-shadow union-cover
problem [[mrw-d0402aea6f58]] in standard extremal-set-theory language.  If true,
it implies \(M_{P_k}(\theta)\to0\) for the squarefree residual
[[mrw-37dbc6aeedf9]] via the pair-link shadow criterion [[mrw-3c39ca3d1973]].
That would still require a separate lift to the exponent-grid residual
\(R_P(\theta)\) in [[mrw-4daa694d9526]].

Classical uniform union-free results provide vocabulary and rank-layer
intuition, but they do not directly settle this problem.  The measure
\(\nu_k\) is an inhomogeneous product measure biased toward the smallest prime
coordinates, so uniform cardinality bounds in \(2^{[k]}\) do not automatically
control \(\nu_k\)-mass.

The exact-rank obstruction in [[mrw-67f99fecf9e2]] shows why global boundary
smallness is false.  The rank-only proposition [[mrw-02dadc6b1bba]] shows why
rank-layer examples are nevertheless harmless for high-support biased mass.
Thus the target is a weighted structural theorem or an explicit positive-mass
union-free counterexample that is not rank-only, not fixed-core, not
upward-closed, and not merely an exact-rank-layer skeleton.

## Depends on

- [[mrw-b4075311abd3]] for the exact union-free reformulation.
- [[mrw-d0402aea6f58]] for the prior lower-shadow formulation.
- [[mrw-37dbc6aeedf9]] and [[mrw-3c39ca3d1973]] for the squarefree residual
  bridge.
- [[mrw-4daa694d9526]] for the eventual exponent-grid residual target.
- [[mrw-2a2c5551301e]] and [[mrw-67f99fecf9e2]] for boundary mechanisms and
  obstructions.

## Used by

- Next #536 loop: prove a prime-biased Kleitman-type theorem, or construct a
  genuine nonvanishing high-support union-free family under \(\nu_k\).

## Notes

- This problem is open locally.
- The theorem is stronger than merely proving a boundary leakage lower bound:
  it must absorb boundary-heavy families into rank-layer-like negligible
  skeletons or force an actual union triple.
- Partition-free theorems are a useful nearby source family, but they do not
  replace the union-free target because the two lower sets in \(A\cup B=C\)
  need not be disjoint.
