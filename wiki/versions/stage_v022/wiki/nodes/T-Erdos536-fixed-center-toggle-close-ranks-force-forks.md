---
id: "T-Erdos536-fixed-center-toggle-close-ranks-force-forks"
type: "theorem"
title: "Erdos 536 fixed center toggle template with close ranks contains union fork"
status: "proved"
tags: ["close-ranks", "erdos-536", "fixed-center", "fork", "proved", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T192341-erdos536-center-drift-student.json", "raw/student/20260531T192341-erdos536-center-drift.md", "theory/nodes/T-Erdos536-fixed-coordinate-toggle-layer-template-union-free-rank-thin.json"]
---

# Theorem: Erdos 536 fixed center toggle template with close ranks contains union fork

## Statement

Fix a coordinate \(q\) and a rank set \(R\). Let \(\mathcal T_{R,q}=\{A\subseteq P_k\setminus\{q\}: |A|\in R\}\cup\{A\cup\{q\}: A\subseteq P_k\setminus\{q\}, |A|\in R\}\). If \(R\) contains ranks \(r<s\le2r\), then \(\mathcal T_{R,q}\) contains distinct \(A,B,C\) with \(A\cup B=C\). Consequently a fork-free full fixed-center toggle template must have multiplicatively lacunary ranks.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T192341-erdos536-center-drift-student.json`
- `raw/student/20260531T192341-erdos536-center-drift.md`
- `theory/nodes/T-Erdos536-fixed-coordinate-toggle-layer-template-union-free-rank-thin.json`

## Proof

\emph{Setup.}
Let
\[
S_k=\sum_{i\le k}\frac1{p_i},
\qquad
\nu_k(p_i\in S)=\frac1{p_i},
\qquad
H_{k,\theta}=\{S\subseteq P_k: |S|>\theta S_k\}.
\]
The active obstruction is a fork-free family \(\mathcal F_k\subseteq H_{k,\theta}\)
whose occupied-top defect shadows
\[
\mathsf D_{\mathcal F_k}(C)
=\{C\setminus A:A\in\mathcal F_k,\ A\subsetneq C\}
\]
are coherent and intersecting. The previous pass showed that the fixed
coordinate two-layer toggle template is coherent and fork-free, but rank-thin.

Candidate:
the Erdos536 fixed center coherent shadow collapse.

No full proof was found. The fixed-center branch did produce a useful
structural lemma for the natural toggle templates.

Fix a coordinate \(q\) and a rank set \(R\). Define the fixed-center toggle
template
\[
\mathcal T_{R,q}
=
\{A\subseteq P_k\setminus\{q\}: |A|\in R\}
\cup
\{A\cup\{q\}: A\subseteq P_k\setminus\{q\}, |A|\in R\}.
\]
If \(R\) contains \(r<s\le2r\), then \(\mathcal T_{R,q}\) contains a fork.
Choose \(C\subseteq P_k\setminus\{q\}\) with \(|C|=s\). Since \(s\le2r\), one
can choose distinct \(r\)-subsets \(A,B\subseteq C\) with \(A\cup B=C\). Then
\[
A,\quad B,\quad C
\]
are distinct members of \(\mathcal T_{R,q}\) and \(A\cup B=C\).

Thus a fixed-center toggle template that avoids forks cannot contain two
central ranks \(r<s\le2r\). In the central product-measure window
\([\theta S_k,MS_k]\), such a rank set has \(O_{\theta,M}(1)\) ranks, hence is
subcritical relative to \(\sqrt{S_k}\). Outside a sufficiently large multiple
of \(S_k\), the rank mass is negligible by Markov. This strongly supports the
fixed-center collapse route.

Admitted true node:
\[
the Erdos536 fixed center toggle close ranks force forks.
\]

However, this does not prove the full fixed-center theorem for arbitrary
center-stable coherent systems, because such systems need not be full toggle
templates. A sparse fixed-center system may avoid the close-rank complete-layer
forks while still using many ranks. I could not prove that all such sparse
systems either create a fork or collapse to \(o(\sqrt{S_k})\) ranks.

Candidate:
the Erdos536 moving center drift forces cross top fork.

No proof was found. The close-rank fixed-center lemma suggests why center drift
is the remaining hard case: if centers stay fixed and ranks are close, forks
appear; if ranks are lacunary, mass is lost. Moving centers might try to keep
ranks close while making the fork witnesses incompatible across tops.

The attempted proof strategy was:

1. pick two occupied tops whose centers \(q(C_1)\) and \(q(C_2)\) differ;
2. use positive mass and broad rank support to find comparable or near-comparable
   lower traces under the two tops;
3. force their union to land in another occupied top.

The missing step is the third one. Current local tools identify forks once an
occupied top is covered, but they do not force the union of two lower traces to
be occupied. Thus the moving-center cross-top forcing theorem remains open.

Candidate:
the Erdos536 diagnostic lacunary moving center construction.

No positive-mass moving-center construction was found.

Template tests:

Fixed-center close ranks produce forks by
  the Erdos536 fixed center toggle close ranks force forks.
Fixed-center lacunary ranks can avoid those complete-layer forks, but in the
  central window they use only \(O(1)\) ranks; outside a large central window,
  rank mass is negligible. This points to rank-thinness.
Full local downset shields have internal forks by
  the Erdos536 naive large defect downset shield has internal forks.
Random or moving center assignments were not turned into a construction:
  close ranks seem to create cross-top union pressure, while lacunary spacing
  loses mass.

The diagnostic status is therefore unresolved but sharper: a successful
construction must be sparse enough to avoid the fixed-center close-rank fork,
not so lacunary that rank mass vanishes, and coordinated enough to avoid
cross-top unions from moving centers.

the Erdos536 fixed center coherent shadow collapse: candidate_open;
the Erdos536 moving center drift forces cross top fork: candidate_open;
the Erdos536 diagnostic lacunary moving center construction: candidate_open.

Admitted true diagnostic node:
\[
the Erdos536 fixed center toggle close ranks force forks.
\]

No Erdos 536 theorem was solved and no source counterexample was constructed.
into a quantitative rank-window problem: close central ranks force forks unless
the family is very sparse, while too much lacunarity loses product mass.

around central-window density for moving-center systems: one close-rank
cross-top fork theorem, one sparse-close-rank rank-mass collapse theorem, and
one diagnostic randomized moving-center construction route.

_Proof source: `raw/student/20260531T192341-erdos536-center-drift.md`._

## Tags

`close-ranks`, `erdos-536`, `fixed-center`, `fork`, `proved`, `theorem`, `true`
