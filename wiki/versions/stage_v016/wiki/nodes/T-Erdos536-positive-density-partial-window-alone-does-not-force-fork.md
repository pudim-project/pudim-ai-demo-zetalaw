---
id: "T-Erdos536-positive-density-partial-window-alone-does-not-force-fork"
type: "theorem"
title: "Erdos 536 positive density partial predecessor window alone does not force local fork"
status: "proved"
tags: ["ekr-star", "erdos-536", "fork-obstruction", "partial-window", "positive-density", "proved", "theorem", "true"]
parents: ["T-Erdos536-top-local-EKR-star-threshold-sharp", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T205129-erdos536-sparse-predecessor-closures-student.json", "raw/student/20260531T205129-erdos536-sparse-predecessor-closures.md", "theory/nodes/T-Erdos536-partial-predecessor-window-fork-theorem.json", "theory/nodes/T-Erdos536-top-local-EKR-star-threshold-sharp.json"]
---

# Theorem: Erdos 536 positive density partial predecessor window alone does not force local fork

## Statement

Let \(C\) be a finite set of size \(n\), let \(m<n\le2m\), and fix \(q\in C\). The partial lower layer \(\mathcal A_{m,q}(C)=\{A\subseteq C\setminus\{q\}: |A|=m\}\) has positive relative density \((n-m)/n\) inside \(\binom{C}{m}\), but no two members \(A,B\in\mathcal A_{m,q}(C)\) satisfy \(A\cup B=C\). Hence positive lower-layer density alone does not force a local predecessor-window fork; a super-EKR threshold, center synchronization, or additional closure hypothesis is required.

## Dependencies

- [[wiki/nodes/T-Erdos536-top-local-EKR-star-threshold-sharp|Erdos 536 top local EKR star trace threshold is sharp]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T205129-erdos536-sparse-predecessor-closures-student.json`
- `raw/student/20260531T205129-erdos536-sparse-predecessor-closures.md`
- `theory/nodes/T-Erdos536-partial-predecessor-window-fork-theorem.json`
- `theory/nodes/T-Erdos536-top-local-EKR-star-threshold-sharp.json`

## Proof

\emph{Setup.}
The current true input is the full predecessor-window fork lemma:
\[
  \mathcal W_{m,n}(P)=\{A\subseteq P:m\le |A|\le n\}
\]
contains a fork whenever \(m<n\le2m\) and \(|P|\ge n\). This kills full
rank-window closure, but not sparse or threshold-star closure.

The main local obstruction is the sharp EKR star threshold already present in
the Theory. If \(C\) has size \(n\), \(m<n\le2m\), and \(q\in C\), then
\[
  \mathcal A_{m,q}(C)=\{A\subseteq C\setminus\{q\}: |A|=m\}
\]
has
\[
  |\mathcal A_{m,q}(C)|=\binom{n-1}{m}
  =\frac{n-m}{n}\binom{n}{m},
\]
and no two members of \(\mathcal A_{m,q}(C)\) union to \(C\), because every
member omits \(q\). Thus a positive fraction of the \(m\)-layer below a top is
not enough by itself to force a fork. The local theorem needs density strictly
above the EKR threshold, or an additional cross-top synchronization hypothesis.

Admitted true child node:
\[
the Erdos536 positive density partial window alone does not force fork.
\]

Candidate:
the Erdos536 partial predecessor window fork theorem.

The candidate remains open. The full rank-window lemma proves the dense
extreme, and the local EKR theorem proves a super-threshold version below a
fixed occupied top:
\[
  |\mathcal A_m(C)|>\binom{n-1}{m}
  \quad\Longrightarrow\quad
  \exists A,B\in\mathcal A_m(C)\text{ with }A\cup B=C.
\]
However the AP candidate only asks for a positive-density partial rank window.
That is too weak without a threshold or stability condition, since the star
\(\mathcal A_{m,q}(C)\) has positive relative density \((n-m)/n\) and avoids
all local forks.

The missing theorem is therefore not a plain positive-density statement. It
must show either that global coherence amplifies some local trace above the EKR
threshold, or that threshold-level stars synchronize their centers in a way
that creates cross-top forks or rank collapse.

Candidate:
the Erdos536 sparse predecessor layer mass collapse.

This theorem remains open. The existing true rank tools prove only the pure
rank-sparse alternatives:

\(o(\sqrt{S_k})\) exact ranks have \(o(1)\) \(\nu_k\)-mass by
  the Erdos536 rank block anti concentration;
central \(2\)-lacunary rank windows have vanishing mass by
  the Erdos536 central lacunary rank windows are rank thin.

Avoiding partial-window forks does not currently imply either kind of rank
sparsity. A family can avoid local forks at a nonlacunary pair of ranks by
using an EKR-star trace at the sharp threshold. To turn this into mass collapse
one still needs a center-profile stability theorem: threshold-star centers must
either live in \(o(\sqrt{S_k})\) rank/center cells, or unsynchronize enough to
force occupied-union coverage.

Candidate:
the Erdos536 diagnostic sparse predecessor center construction.

No genuine positive-mass fork-free coherent construction was found. The tested
templates separate into known failures:

1. Full nonlacunary rank windows fail by
   the Erdos536 full predecessor window closure has forks.
2. Exact rank layers and central \(2\)-lacunary rank mixtures are union-free
   templates, but they have vanishing mass by rank-block anti-concentration and
   central-lacunary thinning.
3. Local EKR stars avoid a fork below a fixed top at positive lower-layer
   density, but this is only a local threshold-sharp obstruction. It does not
   by itself provide a positive-mass coherent global family.

Thus the remaining construction, if it exists, must be more specific: it must
live at or below the local EKR threshold, spread over nonlacunary central ranks,
and avoid both center synchronization and cross-top occupied-union hits. I did
not construct such a family, and I did not prove it impossible.

the Erdos536 partial predecessor window fork theorem: candidate_open;
the Erdos536 sparse predecessor layer mass collapse: candidate_open;
the Erdos536 diagnostic sparse predecessor center construction: candidate_open.

Admitted true child node:
\[
the Erdos536 positive density partial window alone does not force fork.
\]

No Erdos 536 theorem was solved. The source coherence node and the terminal
weighted union-free frontier remain open.

around below-EKR predecessor-star stability: one super-EKR amplification
theorem, one EKR-star center synchronization theorem, and one diagnostic
below-threshold sparse top-code construction route.

_Proof source: `raw/student/20260531T205129-erdos536-sparse-predecessor-closures.md`._

## Tags

`ekr-star`, `erdos-536`, `fork-obstruction`, `partial-window`, `positive-density`, `proved`, `theorem`, `true`
