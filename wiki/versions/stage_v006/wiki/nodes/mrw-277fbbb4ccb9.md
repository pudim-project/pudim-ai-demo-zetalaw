---
id: mrw-277fbbb4ccb9
type: problem
title: Erdos equal pairwise least-common-multiple problem
aliases: ["mrw-277fbbb4ccb9", "Erdos equal pairwise least-common-multiple problem"]
status: open
tags: ["problem", "open", "erdos", "least-common-multiple", "lcm", "finite-shadow", "restart-frontier", "patch-gate-audited"]
parents: [mrw-538319137c76, mrw-1ac4e44cbbad]
refs: ["https://www.erdosproblems.com/536"]
---

# Problem: Erdos equal pairwise least-common-multiple problem

## Statement

Let \(f(N)\) be the largest size of a set
\[
A\subseteq \{1,\ldots,N\}
\]
with no three distinct elements \(a,b,c\in A\) satisfying
\[
[a,b]=[b,c]=[a,c],
\]
where \([u,v]\) denotes the least common multiple.  Erdos Problem #536 asks for estimates for \(f(N)\), in particular whether
\[
f(N)=o(N).
\]

## Evidence

- Source: Thomas F. Bloom, Erdos Problems Database, problem #536, accessed 2026-05-18.
- The source page marks the problem open, says no partial or complete solutions are claimed in the comments, and was last edited 2026-04-29.
- The page records Abbott--Gardner's lower bound
\[
f(N)\ge (1-o(1))(\log\log N)\frac{N}{\log N}
\]
and an upper-bound context of the shape
\[
f(N)\le \left(\frac{221}{225}+o(1)\right)N,
\]
so the specific density question \(f(N)=o(N)\) remains unresolved in the cited source.

## Local Bridge

For prime valuations \(v_p\), the equality
\[
[a,b]=[b,c]=[a,c]
\]
is equivalent to the condition that, for every prime \(p\), the maximum of
\[
v_p(a),\quad v_p(b),\quad v_p(c)
\]
is attained at least twice.  In the squarefree finite-prime model this becomes a cosunflower condition on prime-support sets.  This makes #536 a natural restart from the residue-shadow branch: it keeps finite prime-coordinate shadows and lcm geometry, but avoids the stalled residue-tail continuity problem in Erdos #25.

## First Attack Target

Prove or refute a finite-prime fiber lifting lemma.  For a dense set \(A\subseteq[1,N]\), seek a finite prime set \(P\), a common outside kernel \(r\), and a dense family of \(P\)-smooth divisors \(d\) such that \(rd\in A\).  A successful fiber should contain three \(P\)-smooth divisors whose valuation vectors have no coordinate with a unique maximum, and whose outside kernel is identical.  That would lift a finite-prime cosunflower to an actual lcm triangle in \(A\).

## Depends on

- [[wiki/nodes/mrw-538319137c76|Modular residue distribution and successor entropy]]
- [[wiki/nodes/mrw-1ac4e44cbbad|Zeta-law successor entropy and modular resolution]]

## Used by

- Next restart after the Erdos #25 residue-tail route stalls.

## Notes

- This node is source-grounded open-problem context only.  It is not a solved or partial result.
- The local finite-prime bridge is a proposed attack direction, not an imported theorem.
- Scout response `theory/forage/responses/20260518T233011Z-full-nonstaging-loop-scout-response.md` was not used for this promotion because its primary candidate returned to the parked routine \(s=9\) branch.
