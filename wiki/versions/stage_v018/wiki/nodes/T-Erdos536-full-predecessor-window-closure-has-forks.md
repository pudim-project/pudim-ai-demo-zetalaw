---
id: "T-Erdos536-full-predecessor-window-closure-has-forks"
type: "theorem"
title: "Erdos 536 full predecessor rank window closure contains union forks"
status: "proved"
tags: ["erdos-536", "fork", "predecessor-closure", "proved", "rank-window", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T203844-erdos536-predecessor-obstruction-student.json", "raw/student/20260531T203844-erdos536-predecessor-obstruction.md", "theory/nodes/T-Erdos536-central-lacunary-rank-windows-are-rank-thin.json", "theory/nodes/T-Erdos536-diagnostic-predecessor-star-closure-test.json", "theory/nodes/T-Erdos536-fixed-center-toggle-close-ranks-force-forks.json"]
---

# Theorem: Erdos 536 full predecessor rank window closure contains union forks

## Statement

Let \(P\) be a finite set and let \(m<n\le2m\) with \(|P|\ge n\). The full rank-window family \(\mathcal W_{m,n}(P)=\{A\subseteq P:m\le |A|\le n\}\) contains distinct \(A,B,C\) with \(A\cup B=C\). Consequently, for constants \(0<a<b<2a\), any full predecessor-window closure of a linear top window containing all ranks from \(\lceil aS_k\rceil-1\) through \(\lfloor bS_k\rfloor\) is not fork-free for all sufficiently large \(k\).

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T203844-erdos536-predecessor-obstruction-student.json`
- `raw/student/20260531T203844-erdos536-predecessor-obstruction.md`
- `theory/nodes/T-Erdos536-central-lacunary-rank-windows-are-rank-thin.json`
- `theory/nodes/T-Erdos536-diagnostic-predecessor-star-closure-test.json`
- `theory/nodes/T-Erdos536-fixed-center-toggle-close-ranks-force-forks.json`

## Proof

\emph{Setup.}
The previous true diagnostic node is
the Erdos536 linear window predecessor star code avoids pushforward. It builds a
positive-mass central top code
\[
  \mathcal T_k=\{C\subseteq P_k:aS_k\le |C|\le bS_k\},
  \qquad \theta<a<1<b<2a,
\]
and assigns to each occupied top \(C\) one singleton predecessor star
\(\{C\setminus\{q(C)\}\}\). Two independent predecessor traces almost never
union back into \(\mathcal T_k\), because their ranks nearly double unless the
two tops have an atypically large intersection.

The caveat is that this is only a top-code model. It does not show that the
full induced set family is fork-free. This pass tests whether adding natural
predecessor-closure layers immediately creates forks.

Candidate:
the Erdos536 nondegenerate lower rank stars hit top code.

This theorem remains open. If lower traces below a central occupied top have
rank \(r\le |C|-\delta S_k\), then
\[
  |A\cup B|=|A|+|B|-|A\cap B|
\]
can fall back into a central top window for plausible overlap sizes. However,
the current hypotheses still do not force the required overlap distribution or
an occupied top hit. A rank calculation alone is insufficient: one also needs a
coverage or incidence theorem connecting lower traces to the occupied top code.

Candidate:
the Erdos536 fork free coherence links top window to lower star ranks.

The full coherence theorem remains open. The diagnostic calculation below proves
that a full rank-window predecessor closure is impossible in a fork-free family,
but it does not exclude sparse predecessor closures. Thus it identifies a real
failure mode for the naive closure, not a complete proof that every coherent
moving-star obstruction either has nondegenerate lower ranks or vanishing mass.

Candidate:
the Erdos536 diagnostic predecessor star closure test.

The full predecessor-window closure fails by a deterministic finite lemma.

Let \(P\) be a finite set and let \(m<n\le 2m\) with \(|P|\ge n\). Define
\[
  \mathcal W_{m,n}(P)=\{A\subseteq P:m\le |A|\le n\}.
\]
Choose \(C\subseteq P\) with \(|C|=n\). Put \(t=2m-n\), so \(0\le t<m\).
Choose \(I\subseteq C\) with \(|I|=t\), and split
\[
  C\setminus I=X\sqcup Y,
  \qquad |X|=|Y|=n-m.
\]
Then
\[
  A=I\cup X,\qquad B=I\cup Y
\]
have \(|A|=|B|=m\), while \(A\cup B=C\). Since \(n>m\), the sets \(A,B,C\) are
distinct. Therefore \(\mathcal W_{m,n}(P)\) contains a union fork.

Apply this with
\[
  m_k=\lceil aS_k\rceil-1,\qquad n_k=\lfloor bS_k\rfloor.
\]
Because \(b<2a\), for all large \(k\) one has \(m_k<n_k\le2m_k\), and
\(|P_k|\ge n_k\). Hence any full closure containing every rank from
\(m_k\) through \(n_k\) contains distinct \(A,B,C\) with \(A\cup B=C\).
In particular, the linear-window predecessor-star top code cannot be upgraded
to a full predecessor-window closure while remaining fork-free.

Admitted true node:
\[
the Erdos536 full predecessor window closure has forks.
\]

This is diagnostic only. It rules out the full rank-window closure, but sparse
or selectively centered predecessor closures remain the live obstruction.

the Erdos536 nondegenerate lower rank stars hit top code: candidate_open;
the Erdos536 fork free coherence links top window to lower star ranks: candidate_open;
the Erdos536 diagnostic predecessor star closure test: candidate_true.

Promoted diagnostic node:
\[
the Erdos536 diagnostic predecessor star closure test.
\]

Admitted true node:
\[
the Erdos536 full predecessor window closure has forks.
\]

No Erdos 536 theorem was solved. The terminal frontier remains open. The next
partial predecessor-window closure still forces forks, prove that avoiding
full windows forces mass collapse, or construct a sharper sparse predecessor
obstruction.

_Proof source: `raw/student/20260531T203844-erdos536-predecessor-obstruction.md`._

## Tags

`erdos-536`, `fork`, `predecessor-closure`, `proved`, `rank-window`, `theorem`, `true`
