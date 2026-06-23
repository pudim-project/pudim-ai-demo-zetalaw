---
id: "T-Erdos536-top-local-EKR-star-threshold-sharp"
type: "theorem"
title: "Erdos 536 top local EKR star trace threshold is sharp"
status: "proved"
tags: ["ekr-threshold", "erdos-536", "proved", "sharpness", "star-trace", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T195803-erdos536-ekr-globalization-student.json", "raw/student/20260531T195803-erdos536-ekr-globalization.md", "theory/nodes/T-Erdos536-top-local-EKR-trace-threshold-forces-fork.json"]
---

# Theorem: Erdos 536 top local EKR star trace threshold is sharp

## Statement

Let \(C\) be a finite set of size \(s\), let \(r<s\le2r\), and fix \(q\in C\). The star trace \(\mathcal A_{r,q}(C)=\{A\subseteq C\setminus\{q\}: |A|=r\}\) has size \(\binom{s-1}{r}\) and contains no pair \(A,B\) with \(A\cup B=C\). Therefore the top-local EKR trace threshold in `T-Erdos536-top-local-EKR-trace-threshold-forces-fork` is sharp.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T195803-erdos536-ekr-globalization-student.json`
- `raw/student/20260531T195803-erdos536-ekr-globalization.md`
- `theory/nodes/T-Erdos536-top-local-EKR-trace-threshold-forces-fork.json`

## Proof

\emph{Setup.}
Use
\[
\nu_k(p_i\in S)=\frac1{p_i},\qquad
S_k=\sum_{i\le k}\frac1{p_i},\qquad
H_{k,\theta}=\{S\subseteq P_k: |S|>\theta S_k\}.
\]
The previous pass proved the top-local EKR threshold: for an occupied top
\(C\) of size \(s\) and \(r<s\le2r\), more than \(\binom{s-1}{r}\) lower
\(r\)-traces below \(C\) force two traces whose union is \(C\).

Candidate:
the Erdos536 trace density amplification above local EKR threshold.

No proof was found. The attempted incidence count is as follows. For a fixed
close-rank pair \(r<s\le2r\), count
\[
I_{r,s}
=
|\{(A,C): A,C\in\mathcal F_k,\ A\subsetneq C,\ |A|=r,\ |C|=s\}|.
\]
To prove the candidate, it would be enough to show
\[
I_{r,s}>
|\mathcal F_k^{(s)}|\binom{s-1}{r}
\]
for some central close-rank pair. This would force an occupied top with trace
size above the local EKR threshold.

The obstacle is that the EKR threshold is sharp. For a top \(C\) and a
coordinate \(q\in C\), the star trace
\[
\mathcal A_{r,q}(C)
=
\{A\subseteq C\setminus\{q\}: |A|=r\}
\]
has exactly
\[
|\mathcal A_{r,q}(C)|=\binom{s-1}{r}
\]
members, and no two of them cover \(C\), because every member omits \(q\).
Thus an incidence average at or below this threshold proves nothing. The
global amplification theorem must use positive mass or cross-top coherence to
force a strict excess over this sharp threshold somewhere. I could not prove
that strict excess.

Admitted true diagnostic node:
\[
the Erdos536 top local EKR star threshold sharp.
\]

Candidate:
the Erdos536 EKR star center synchronization.

No proof was found. The sharpness lemma shows the right local normal form:
sub-threshold or threshold-level occupied-top traces can look like defect
stars, all omitting a top-dependent coordinate \(q(C)\). A synchronization
proof would need to show that the centers \(q(C)\), or a small set of such
centers for near-star traces, either concentrate into \(o(\sqrt{S_k})\) weighted
profile blocks or produce incompatible dense profiles that create occupied
coverage.

The naive pigeonhole still fails. The number of possible coordinates is \(k\),
while the relevant mass scale is governed by \(S_k=\sum_{i\le k}1/p_i\), and
the top sizes in the central window are only \(O(S_k)\). A family can move star
centers across many coordinates without an immediate unweighted pigeonhole
forcing a common center. The missing ingredient is a weighted center-profile
entropy or stability theorem that sees prime-biased mass rather than ambient
coordinate count.

Candidate:
the Erdos536 diagnostic below threshold sparse code obstruction.

No positive-mass construction was found. The local threshold-sharp star is a
valid local template, but lifting it globally remains hard.

The natural construction attempt is:

1. choose many occupied tops \(C\) in a central rank \(s\);
2. assign to each top a moving center \(q(C)\in C\);
3. include lower traces \(A\subseteq C\setminus\{q(C)\}\), \(|A|=r\), at or
   below the EKR threshold;
4. arrange that unions of lower traces rarely land in the occupied top set.

The local star condition prevents forks inside a fixed top, but it does not
automatically prevent cross-top unions. If the occupied top set is too sparse,
its \(\nu_k\)-mass vanishes. If it is dense enough to have positive mass, the
number of candidate lower-trace unions becomes large and appears to force
collisions with occupied tops, but I did not turn this into a proof. If lower
traces are thinned enough to avoid such collisions, their mass contribution
seems to collapse toward the already known sparse/rank-thin alternatives.

Thus the below-threshold sparse-code route remains open, but it is now reduced
to a sharp local-star lifting problem rather than a vague random-code search.

the Erdos536 trace density amplification above local EKR threshold: candidate_open;
the Erdos536 EKR star center synchronization: candidate_open;
the Erdos536 diagnostic below threshold sparse code obstruction: candidate_open.

Admitted true diagnostic node:
\[
the Erdos536 top local EKR star threshold sharp.
\]

No Erdos 536 theorem was solved and no source counterexample was constructed.
one route should estimate the mass of star fibers below moving tops, one route
should force cross-top collisions between unsynchronized star centers, and one
route should try a threshold-sharp moving-star construction.

around the threshold-sharp moving-star regime: one weighted star-fiber mass
theorem, one cross-top star-center collision theorem, and one threshold-sharp
moving-star construction route.

_Proof source: `raw/student/20260531T195803-erdos536-ekr-globalization.md`._

## Tags

`ekr-threshold`, `erdos-536`, `proved`, `sharpness`, `star-trace`, `theorem`, `true`
