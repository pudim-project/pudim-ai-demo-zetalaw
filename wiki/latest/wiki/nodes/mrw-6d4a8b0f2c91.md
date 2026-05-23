---
id: mrw-6d4a8b0f2c91
type: corollary
title: Capped pair-link relations have no positive-mass endpoint core
aliases: ["mrw-6d4a8b0f2c91", "Capped pair-link endpoint-degree invisibility"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, union-free, pair-link, capped-band, random-pair, endpoint-degree, rectangle-sparsity, route-kill]
parents: [mrw-4f1e9a2d6b73, mrw-c7f4e0c9a821, mrw-3c39ca3d1973, mrw-55a8d9eddd2e]
refs: []
  - raw/20260520T010053Z-erdos-536-rare-pair-link-endpoint-degree-invisibility-after.md
  - references/sources/20260520T010053Z-rare-pair-link-endpoint-context.md
  - theory/forage/requests/20260520T005456Z-erdos536-rare-overlap-pair-geometry-request.md
  - theory/forage/responses/20260520T005456Z-erdos536-rare-overlap-pair-geometry-response.md
  - oracle/requests/20260520T010053Z-erdos536-rare-pair-link-endpoint-degree-oracle-request.md
  - oracle/responses/20260520T010053Z-erdos536-rare-pair-link-endpoint-degree-oracle-response.md
---

# Corollary: Capped pair-link relations have no positive-mass endpoint core

## Statement

Let
\[
P_k=\{p_1,\ldots,p_k\},
\qquad
\nu_k(p_i\in S)=\frac1{p_i},
\qquad
S_k=\sum_{i\le k}\frac1{p_i}.
\]
Fix
\[
0<\theta<1,\qquad \theta<\alpha<2\theta,\qquad \eta>0,
\]
and put
\[
B_{k,\theta,\alpha}
=
\{A\subseteq P_k:\theta S_k<|A|\le \alpha S_k\}.
\]
Let
\[
\mathcal F_k\subseteq B_{k,\theta,\alpha},
\qquad
\nu_k(\mathcal F_k)\ge\eta,
\]
and write
\[
\lambda_k=\nu_k(\,\cdot\mid\mathcal F_k).
\]

On \(\mathcal F_k\times\mathcal F_k\), define the capped union relation
\[
R^\cup_k(A,B)
\quad\Longleftrightarrow\quad
A\cup B\in\mathcal F_k,
\]
and the pair-link relation
\[
R^I_k(A,B)
\quad\Longleftrightarrow\quad
I(A,B)\cap\mathcal F_k\ne\varnothing,
\]
where
\[
I(A,B)=\{C\subseteq P_k:A\triangle B\subseteq C\subseteq A\cup B\}.
\]
The same statements below hold for
\[
R^{I^\circ}_k(A,B)
\quad\Longleftrightarrow\quad
I^\circ(A,B)\cap\mathcal F_k\ne\varnothing,
\qquad
I^\circ(A,B)=I(A,B)\setminus\{A,B\}.
\]
These are endpoint-inclusive ordered-pair relations, except for the explicit
\(I^\circ\) deletion.  If one instead uses the genuine distinct-triple
subrelations
\[
R^{\cup,\circ}_k(A,B)
\quad\Longleftrightarrow\quad
A\ne B,\qquad A\cup B\in\mathcal F_k\setminus\{A,B\},
\]
or
\[
R^{I,\mathrm{3pt}}_k(A,B)
\quad\Longleftrightarrow\quad
A\ne B,\qquad I^\circ(A,B)\cap\mathcal F_k\ne\varnothing,
\]
then all bounds below still hold, since these are subrelations of the
endpoint-inclusive ones.

For any one of these three relations \(R_k\), define its conditional endpoint
degree by
\[
d_{R_k}(A)
=
\lambda_k\{B\in\mathcal F_k:(A,B)\in R_k\}.
\]
Then
\[
\int_{\mathcal F_k}d_{R_k}(A)\,d\lambda_k(A)
=
(\lambda_k\times\lambda_k)(R_k)
=
O_{\eta,\theta,\alpha}(S_k^{-1}).
\tag{1}
\]
Consequently, for every threshold \(\tau_k>0\),
\[
\lambda_k\{A\in\mathcal F_k:d_{R_k}(A)\ge\tau_k\}
\le
O_{\eta,\theta,\alpha}\!\left(\frac1{\tau_kS_k}\right).
\tag{2}
\]
Moreover, for every \(\mathcal G_k\subseteq\mathcal F_k\) with
\(\lambda_k(\mathcal G_k)>0\),
\[
\mathbb E_{\lambda_k(\cdot\mid\mathcal G_k)}d_{R_k}(A)
\le
O_{\eta,\theta,\alpha}\!\left(\frac1{\lambda_k(\mathcal G_k)S_k}\right).
\tag{3}
\]

Finally, for all \(\mathcal G_k,\mathcal H_k\subseteq\mathcal F_k\),
\[
(\lambda_k\times\lambda_k)
\bigl(R_k\cap(\mathcal G_k\times\mathcal H_k)\bigr)
=
O_{\eta,\theta,\alpha}(S_k^{-1}).
\tag{4}
\]
In particular, if \(\mathcal G_k\times\mathcal H_k\subseteq R_k\), then
\[
\lambda_k(\mathcal G_k)\lambda_k(\mathcal H_k)
=
O_{\eta,\theta,\alpha}(S_k^{-1}).
\tag{5}
\]

## Proof

For \(R^\cup_k\), equation (1) is exactly the random-pair union-completion
estimate from [[mrw-4f1e9a2d6b73]]:
\[
(\lambda_k\times\lambda_k)(R^\cup_k)
=
\Pr(X\cup Y\in\mathcal F_k)
=
O_{\eta,\theta,\alpha}(S_k^{-1}),
\]
where \(X,Y\) are independent \(\lambda_k\)-samples.

For \(R^I_k\), the same cited corollary gives
\[
(\lambda_k\times\lambda_k)(R^I_k)
=
\Pr(I(X,Y)\cap\mathcal F_k\ne\varnothing)
=
O_{\eta,\theta,\alpha}(S_k^{-1}).
\]
The estimate for \(R^{I^\circ}_k\) follows because
\[
R^{I^\circ}_k\subseteq R^I_k.
\]
This proves (1) for all three relations.

Markov's inequality applied to the nonnegative function \(d_{R_k}\) gives
\[
\lambda_k\{A:d_{R_k}(A)\ge\tau_k\}
\le
\frac{\int d_{R_k}\,d\lambda_k}{\tau_k},
\]
which is (2).

If \(\lambda_k(\mathcal G_k)>0\), then
\[
\mathbb E_{\lambda_k(\cdot\mid\mathcal G_k)}d_{R_k}(A)
=
\frac1{\lambda_k(\mathcal G_k)}
\int_{\mathcal G_k}d_{R_k}(A)\,d\lambda_k(A)
\le
\frac1{\lambda_k(\mathcal G_k)}
\int_{\mathcal F_k}d_{R_k}(A)\,d\lambda_k(A),
\]
and (3) follows from (1).

Finally,
\[
R_k\cap(\mathcal G_k\times\mathcal H_k)\subseteq R_k,
\]
so (4) follows from (1).  If \(\mathcal G_k\times\mathcal H_k\subseteq R_k\),
then
\[
\lambda_k(\mathcal G_k)\lambda_k(\mathcal H_k)
=
(\lambda_k\times\lambda_k)(\mathcal G_k\times\mathcal H_k)
\le
(\lambda_k\times\lambda_k)(R_k),
\]
which proves (5).

## Consequences

Inside a fixed cap
\[
\theta S_k<|A|\le\alpha S_k<2\theta S_k,
\]
random-pair capped union completions and random-pair capped pair-link hits are
not merely globally sparse.  They also have no positive-mass endpoint core and
contain no positive-mass product rectangle.

Thus a proof of [[mrw-55a8d9eddd2e]] cannot proceed by showing that a
positive-mass capped family has a positive-mass set of endpoints, each with a
fixed-positive capped union or pair-link neighborhood.  Such a statement is
false for every positive-mass family in the cap, independently of union-free
constraints.  The live route must instead exploit the internal structure of
the \(O(S_k^{-1})\) rare pair set, use a genuinely union-specific
hypergraph/container mechanism, use fair-thinning upward boundary, or leave
the fixed capped random-pair framework.

## Depends on

- [[mrw-4f1e9a2d6b73]] Capped random pair-links are overlap-sparse
- [[mrw-c7f4e0c9a821]] Entropy overlap bound for prime-biased families
- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree residuals
- [[mrw-55a8d9eddd2e]] Prime-biased weighted union-free problem
