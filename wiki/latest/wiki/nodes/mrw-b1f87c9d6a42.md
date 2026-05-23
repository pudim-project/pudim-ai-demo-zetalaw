---
id: mrw-b1f87c9d6a42
type: proposition
title: Full rank bands have full genuine pair-link projection
aliases: ["mrw-b1f87c9d6a42", "Full rank bands have full genuine pair-link projection"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, rank-band, rare-relation, projection-obstruction, support-tail, patch-gate-audited]
parents: [mrw-3c39ca3d1973, mrw-4f1e9a2d6b73, mrw-6d4a8b0f2c91]
refs: ["references/sources/20260520T014549Z-rare-pair-link-full-band-projection-context.md"]
  - raw/20260520T014549Z-erdos-536-rare-pair-link-geometry-prove-or-refute-a-rare-hig.md
  - references/sources/20260520T014549Z-rare-pair-link-full-band-projection-context.md
  - oracle/requests/20260520T014549Z-erdos536-rare-pair-link-full-band-projection-oracle-request.md
  - oracle/responses/20260520T014549Z-erdos536-rare-pair-link-full-band-projection-oracle-response.md
---

# Proposition: Full rank bands have full genuine pair-link projection

## Statement

Let \(P\) be a finite set and let
\[
I(A,B)=\{C\subseteq P:\ A\triangle B\subseteq C\subseteq A\cup B\},
\qquad
I^\circ(A,B)=I(A,B)\setminus\{A,B\}.
\]
If \(2\le r\le |P|-1\), then every \(A\in\binom Pr\) has a genuine same-rank pair-link witness: there exist \(B,C\in\binom Pr\), with \(A,B,C\) pairwise distinct, such that
\[
C\in I^\circ(A,B).
\]

Consequently, if
\[
\mathcal B_{a,b}(P)=\{A\subseteq P:\ a<|A|\le b\}
\]
is any cardinality band, then every \(A\in\mathcal B_{a,b}(P)\) with \(|A|\ge2\) and \(P\setminus A\ne\emptyset\) lies in the first-coordinate projection of the genuine pair-link relation
\[
R^\circ_{\mathcal B}(A,B)
\quad\Longleftrightarrow\quad
I^\circ(A,B)\cap\mathcal B_{a,b}(P)\ne\emptyset.
\]

More generally, let \(P_k\) be finite sets and let \(S_k>0\) be scales satisfying
\[
S_k\to\infty,
\qquad
|P_k|-\alpha S_k\to\infty
\]
for a fixed \(\alpha>0\).  For fixed \(0<\theta<\alpha\), put
\[
\mathcal B_{k,\theta,\alpha}
=
\{A\subseteq P_k:\ \theta S_k<|A|\le\alpha S_k\}.
\]
Then for all sufficiently large \(k\), the genuine pair-link relation on the full band \(\mathcal B_{k,\theta,\alpha}\) has full first-coordinate projection.

In particular, for \(P_k=\{p_1,\ldots,p_k\}\) and \(S_k=\sum_{i\le k}1/p_i\), the conclusion applies.  When the capped random-pair sparsity hypotheses for fixed support bands apply to this full band, the relation can simultaneously have conditional pair measure \(O(S_k^{-1})\) and full first-coordinate projection.

## Proof

Fix \(A\in\binom Pr\) with \(2\le r\le |P|-1\).  Choose distinct \(x,z\in A\) and choose \(y\in P\setminus A\).  Define
\[
B=(A\setminus\{x\})\cup\{y\},
\qquad
C=(A\setminus\{z\})\cup\{y\}.
\]
Then \(|B|=|C|=|A|=r\), so \(B,C\in\binom Pr\).  Also \(B\ne A\), since \(y\in B\setminus A\).  We have \(C\ne A\), since \(y\in C\setminus A\), and \(C\ne B\), since \(x\in C\setminus B\).  Thus \(A,B,C\) are pairwise distinct.

The symmetric difference is
\[
A\triangle B=\{x,y\}.
\]
Because \(z\ne x\), the element \(x\) remains in \(C\), and by construction \(y\in C\).  Hence
\[
A\triangle B\subseteq C.
\]
Moreover,
\[
C\subseteq A\cup\{y\}=A\cup B.
\]
Therefore \(C\in I(A,B)\).  Since \(C\ne A,B\), we have \(C\in I^\circ(A,B)\).  This proves the exact-rank statement.

For a cardinality band \(\mathcal B_{a,b}(P)\), apply the exact-rank statement with \(r=|A|\).  The constructed sets \(B\) and \(C\) have the same cardinality as \(A\), so they remain inside the same band.  Thus every such \(A\) lies in the first-coordinate projection of \(R^\circ_{\mathcal B}\).

For the asymptotic statement, if \(A\in\mathcal B_{k,\theta,\alpha}\), then \(|A|>\theta S_k\), so \(|A|\ge2\) for all sufficiently large \(k\).  Also \(|A|\le\alpha S_k<|P_k|\) for all sufficiently large \(k\), because \(|P_k|-\alpha S_k\to\infty\).  Hence \(P_k\setminus A\ne\emptyset\), and the band projection statement applies.

For \(P_k=\{p_1,\ldots,p_k\}\) and \(S_k=\sum_{i\le k}1/p_i\), the program uses the standard facts \(S_k\to\infty\) and \(S_k=o(k)\).  Thus \(|P_k|-\alpha S_k=k-\alpha S_k\to\infty\), and the preceding paragraph applies.

Finally, the capped random-pair pair-link sparsity corollary gives \(O(S_k^{-1})\) conditional random-pair visibility for the capped pair-link relation under its hypotheses.  The genuine relation \(R^\circ_{\mathcal B}\) is a subrelation of the full pair-link relation there, so it inherits the same \(O(S_k^{-1})\) upper bound.  The preceding paragraphs show that this small pair measure is compatible with full first-coordinate projection on the full band.

## Depends on

- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree residuals
- [[mrw-4f1e9a2d6b73]] Capped random-pair pair-link sparsity for fixed support bands
- [[mrw-6d4a8b0f2c91]] Rare pair-link endpoint-degree and rectangle invisibility

## Notes

- This proposition does not prove \(U_k(\theta)\to0\), does not construct a positive-mass pair-link-free or union-free counterexample, and does not lift by itself to an exponent-grid residual.
- The point is a route obstruction: \(O(S_k^{-1})\) random-pair visibility, no positive-mass endpoint cores, and no product rectangles do not imply local absence of pair-link witnesses.  Sparse pair measure can coexist with full vertex projection.
- The next route must use the structure of pair-link-free subfamilies or the underlying three-uniform pair-link hypergraph, not merely endpoint projection, endpoint degree, or product-rectangle sparsity.
