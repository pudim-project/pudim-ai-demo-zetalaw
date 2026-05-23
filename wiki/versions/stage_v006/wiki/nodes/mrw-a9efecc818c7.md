---
id: mrw-a9efecc818c7
type: proposition
title: Nested cut refinement bounds heavy signature corridors
aliases: ["mrw-a9efecc818c7", "Nested cut refinement bounds heavy signature corridors"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, complete-bipartite, nested-cores, signature-coherence, corridor-refinement, weighted-edge-bound, cross-core-coherence, support-tail, oracle-audited]
parents: [mrw-fced7420b905, mrw-816fd32c3294, mrw-c7c76faed872]
refs: ["references/sources/20260521T012914Z-corridor-refinement-context.md"]
  - raw/20260521T012914Z-erdos-536-heavy-complementary-signature-corridor-classificat.md
  - raw/20260521T012656Z-erdos536-heavy-signature-corridor-classification.md
  - theory/forage/responses/20260521T012656Z-erdos536-heavy-signature-corridor-classification-response.md
  - oracle/requests/20260521T012914Z-erdos536-corridor-refinement-oracle-request.md
  - oracle/responses/20260521T012914Z-erdos536-corridor-refinement-oracle-response.md
  - references/sources/20260521T012914Z-corridor-refinement-context.md
---

# Proposition: Nested cut refinement bounds heavy signature corridors

## Statement

Let \(P\) be a finite set and let \(\mathcal F\subseteq2^P\) be
pair-link-free.  For \(R\subseteq P\), write
\[
G_R^\mathcal F=(P\setminus R,E_R^\mathcal F),
\qquad
\{x,y\}\in E_R^\mathcal F
\Longleftrightarrow
R\cup\{x,y\}\in\mathcal F.
\]

Assume \(m\ge1\) and \(\ell\ge1\).  Let
\[
Q\subseteq R_i\subseteq P
\qquad(1\le i\le m+\ell)
\]
and let \(V\subseteq P\setminus\bigcup_i R_i\).  Suppose that for each \(i\),
\[
V=X_i\sqcup Y_i,
\qquad
X_i,Y_i\ne\varnothing,
\]
and \(G_{R_i}^\mathcal F\) contains the complete bipartite graph
\(K_{X_i,Y_i}\).

Use the first \(m\) cuts to define the coarse signature
\[
\sigma_0(v)=(\mathbf 1_{v\in X_i})_{i=1}^m\in\{0,1\}^m.
\]
Fix a complementary coarse signature pair
\[
A=\{v\in V:\sigma_0(v)=\tau\},
\qquad
B=\{v\in V:\sigma_0(v)=\mathbf 1-\tau\}.
\]
Use the remaining \(\ell\) cuts to define the refined signature
\[
\eta(v)=(\mathbf 1_{v\in X_{m+j}})_{j=1}^{\ell}\in\{0,1\}^{\ell}.
\]
For \(\omega\in\{0,1\}^{\ell}\), put
\[
A_\omega=\{a\in A:\eta(a)=\omega\},
\qquad
B_\omega=\{b\in B:\eta(b)=\omega\},
\qquad
\bar\omega=\mathbf 1-\omega.
\]

Let \(w_v\ge0\) be arbitrary weights on \(A\cup B\), and define
\[
\alpha_\omega=\sum_{a\in A_\omega}w_a,
\qquad
\beta_\omega=\sum_{b\in B_\omega}w_b.
\]
For the lower slice edge mass across the coarse corridor \(A|B\), set
\[
M_Q(A,B)
=
\sum_{\substack{\{u,v\}\in E_Q^\mathcal F\\
|\{u,v\}\cap A|=|\{u,v\}\cap B|=1}} w_u w_v .
\]
Then
\[
M_Q(A,B)
\le
\sum_{\omega\in\{0,1\}^{\ell}}\alpha_\omega\beta_{\bar\omega}.
\tag{1}
\]

In the one-cut case \(\ell=1\), write
\[
A=A_0\sqcup A_1,
\qquad
B=B_0\sqcup B_1,
\]
where \(A_i\) and \(B_i\) are the refined classes for the last cut, and write
\[
W_A=\alpha_0+\alpha_1,
\qquad
W_B=\beta_0+\beta_1.
\]
Then
\[
M_Q(A,B)\le \alpha_0\beta_1+\alpha_1\beta_0
=
W_AW_B-(\alpha_0\beta_0+\alpha_1\beta_1).
\tag{2}
\]
Consequently, if \(\varepsilon\ge0\) and
\[
M_Q(A,B)\ge(1-\varepsilon)W_AW_B,
\]
then
\[
\alpha_0\beta_0+\alpha_1\beta_1\le\varepsilon W_AW_B.
\tag{3}
\]

## Proof

Apply [[mrw-fced7420b905]] to the full list of \(m+\ell\) nested upper
complete bipartite blocks.  If
\[
\{u,v\}\in E_Q^\mathcal F\cap\binom V2,
\]
then the full signatures of \(u\) and \(v\) are complementary.

Now restrict to an edge counted by \(M_Q(A,B)\).  Since \(A\cap B=\varnothing\),
the edge has a unique endpoint \(u\in A\) and a unique endpoint \(v\in B\).
The first \(m\) signature coordinates are already complementary by the
definitions of \(A\) and \(B\).  Since the full signatures must be
complementary, the refined signatures from the remaining \(\ell\) cuts satisfy
\[
\eta(v)=\mathbf 1-\eta(u).
\]
Thus every lower edge counted by \(M_Q(A,B)\) lies in one of the refined
corridors
\[
A_\omega\times B_{\bar\omega}
\qquad(\omega\in\{0,1\}^{\ell}).
\]
The total weight of all possible pairs in this refined corridor is
\(\alpha_\omega\beta_{\bar\omega}\).  Summing these complete bipartite
weights over all \(\omega\) gives (1), since the actual lower edge set may be
a strict subgraph of the union of permitted refined corridors.

When \(\ell=1\), the only refined signatures are \(0\) and \(1\), so (1)
becomes
\[
M_Q(A,B)\le\alpha_0\beta_1+\alpha_1\beta_0.
\]
The identity
\[
\alpha_0\beta_1+\alpha_1\beta_0
=
(\alpha_0+\alpha_1)(\beta_0+\beta_1)
-(\alpha_0\beta_0+\alpha_1\beta_1)
\]
proves (2).  If \(M_Q(A,B)\ge(1-\varepsilon)W_AW_B\), then (2) implies
\[
(1-\varepsilon)W_AW_B
\le
W_AW_B-(\alpha_0\beta_0+\alpha_1\beta_1),
\]
which rearranges to (3).

## Depends on

- [[mrw-fced7420b905]] Nested path-shadow coherence for bipartite slice blocks
- [[mrw-816fd32c3294]] Signature fragmentation bounds nested bipartite lower slices
- [[mrw-c7c76faed872]] Complete bipartite blow-ups preserve pair-link freeness

## Used by

## Notes

- This is a local corridor-refinement estimate.  It does not prove that such
  refined cuts exist globally at positive mass, nor does it bound the total
  mass after summing over cores.
- The one-cut formula says exactly how an additional nested upper bipartition
  can preserve a heavy coarse corridor: the two sides \(A\) and \(B\) must be
  nearly anti-aligned for that new cut.  Same-side weighted product is lost
  from the possible lower edge mass.
- Iterating the bound gives the next bridge: a positive-mass candidate must
  either keep producing anti-aligned cuts on its heavy corridors or fragment
  those corridors into small refined signature classes.  This remains a route
  theorem, not a proof of \(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or an
  \(R_P(\theta)\) lift.
