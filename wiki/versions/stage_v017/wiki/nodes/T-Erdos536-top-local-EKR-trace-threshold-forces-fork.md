---
id: "T-Erdos536-top-local-EKR-trace-threshold-forces-fork"
type: "theorem"
title: "Erdos 536 occupied top local EKR lower trace threshold forces union fork"
status: "proved"
tags: ["ekr-threshold", "erdos-536", "fork", "local-trace", "occupied-top", "proved", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["private librarian audit", "private proof note", "theory/nodes/T-Erdos536-disjoint-defect-shadow-equivalent-fork.json"]
---

# Theorem: Erdos 536 occupied top local EKR lower trace threshold forces union fork

## Statement

Let \(\mathcal F\) be a finite set family and let \(C\in\mathcal F\) have \(|C|=s\). Fix \(r<s\le2r\), and put \(\mathcal A_r(C)=\{A\in\mathcal F:A\subsetneq C, |A|=r\}\). If \(|\mathcal A_r(C)|>\binom{s-1}{r}\), then there exist distinct \(A,B,C\in\mathcal F\) with \(A\cup B=C\). Equivalently, every fork-free occupied top has each close-rank lower trace at or below the Erdos-Ko-Rado star threshold in defect-complement coordinates.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `theory/nodes/T-Erdos536-disjoint-defect-shadow-equivalent-fork.json`

## Proof

\emph{Setup.}
Use the prime-biased product law
\[
\nu_k(p_i\in S)=\frac1{p_i},
\qquad
S_k=\sum_{i\le k}\frac1{p_i},
\qquad
H_{k,\theta}=\{S\subseteq P_k: |S|>\theta S_k\}.
\]
The active missing step is not the local fork combinatorics. If an occupied top
\(C\) already has two lower traces \(A,B\in\mathcal F_k\) with
\(A\cup B=C\), the fork is immediate. The hard step is to force that occupied
top from close-rank lower-trace density and moving centers.

Candidate:
the Erdos536 occupied union coverage from close rank density.

The full theorem remains open. The double-counting route reaches a clean local
threshold but does not globalize.

Let \(C\in\mathcal F\) have \(|C|=s\), and fix \(r<s\le2r\). Define the
\(r\)-trace below \(C\) by
\[
\mathcal A_r(C)=\{A\in\mathcal F:A\subsetneq C,\ |A|=r\}.
\]
If two members \(A,B\in\mathcal A_r(C)\) satisfy \(A\cup B=C\), then
\((A,B,C)\) is the required fork. Conversely, if no such pair exists, then the
defect complements
\[
\mathcal D_r(C)=\{C\setminus A:A\in\mathcal A_r(C)\}
\]
form an intersecting family of \((s-r)\)-subsets of \(C\). Since
\(s-r\le s/2\), the Erdos-Ko-Rado bound gives
\[
|\mathcal D_r(C)|
\le
\binom{s-1}{s-r-1}
=
\binom{s-1}{r}.
\]
Therefore
\[
|\mathcal A_r(C)|>\binom{s-1}{r}
\quad\Longrightarrow\quad
\exists A,B\in\mathcal A_r(C): A\cup B=C.
\]

Admitted true node:
\[
the Erdos536 top local EKR trace threshold forces fork.
\]

This identifies the exact local obstruction: fork-free occupied tops may still
have large lower traces, but their defect complements must be EKR-star-like
intersecting families. What remains missing is a global theorem proving that
positive close-rank lower-trace density forces some occupied top to exceed this
local threshold, or forces two profile classes whose traces cover an occupied
top.

Candidate:
the Erdos536 center profile regularization close rank density.

No full regularization theorem was proved. The local EKR threshold gives the
right target for profile regularization: below every fork-free occupied top,
each close-rank trace must be contained at or below an intersecting defect
threshold. Near-extremal local behavior is therefore star-like in defect
coordinates, which suggests a center profile.

The missing step is synchronization across occupied tops. EKR star centers may
move with \(C\), and the current hypotheses do not force those centers into
\(o(\sqrt{S_k})\) blocks or into two incompatible dense profiles satisfying the
coverage theorem. A naive pigeonhole over center coordinates is too weak
because the ambient coordinate set has size \(k\), while the mass scale is
controlled by \(S_k=\sum_{i\le k}1/p_i\), and the active ranks are only of order
\(S_k\).

Thus the regularization route remains open. It now has a sharper local input:
replace vague "intersecting shadows" by EKR-threshold defect stars below
occupied tops.

Candidate:
the Erdos536 diagnostic sparse random code moving center obstruction.

No positive-mass construction was found. The random-code idea has two regimes.

If occupied tops keep lower traces above the local EKR threshold on many close
central ranks, then the top-local theorem creates forks inside those occupied
tops. If the construction keeps every occupied-top trace below that threshold,
then the obstruction must distribute many EKR-star-like local profiles across
many tops without synchronizing their centers and without losing product mass.

This gives a more precise obstruction template but not a construction. A viable
positive-mass random-code obstruction would have to satisfy all of the
following:

central rank support not covered by \(o(\sqrt{S_k})\) ranks;
each occupied top has close-rank lower traces below the EKR fork threshold;
the local EKR-star centers fail to synchronize into center-stable blocks;
candidate unions of lower traces escape the occupied top set;
the retained \(\nu_k\)-mass remains bounded below.

I could not make these constraints compatible. However I also did not prove
that sub-EKR local traces have vanishing mass or regularize. The construction
route remains open.

the Erdos536 occupied union coverage from close rank density: candidate_open;
the Erdos536 center profile regularization close rank density: candidate_open;
the Erdos536 diagnostic sparse random code moving center obstruction: candidate_open.

Admitted true diagnostic node:
\[
the Erdos536 top local EKR trace threshold forces fork.
\]

No Erdos 536 theorem was solved and no source counterexample was constructed.
prove trace-density amplification above the local threshold, synchronize the
local EKR stars into center profiles, or construct a below-threshold sparse-code
obstruction.

around globalizing the top-local EKR trace threshold: one trace-density
amplification theorem, one EKR-star center synchronization theorem, and one
below-threshold sparse-code obstruction construction.

_Proof source: `private proof note`._

## Tags

`ekr-threshold`, `erdos-536`, `fork`, `local-trace`, `occupied-top`, `proved`, `theorem`, `true`
