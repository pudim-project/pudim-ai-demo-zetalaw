---
id: mrw-b52df00c958c
type: proposition
title: Iterated endpoint-fiber towers have exact terminal residual value
aliases: ["mrw-b52df00c958c", "Iterated endpoint-fiber towers have exact terminal residual value"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, iterated-tower, variational-reduction, product-measure, support-tail, self-similar-obstruction, cross-core-coherence]
parents: [mrw-d7b3299d3813]
refs: []
  - raw/20260521T093015Z-erdos-536-iterated-endpoint-fiber-towers-have-exact-terminal.md
  - raw/20260521T092704Z-erdos536-iterated-endpoint-fiber-reduction.md
  - theory/forage/requests/20260521T092704Z-erdos536-iterated-endpoint-fiber-reduction-request.md
  - theory/forage/responses/20260521T092704Z-erdos536-iterated-endpoint-fiber-reduction-response.md
  - oracle/requests/20260521T093015Z-erdos536-iterated-endpoint-tower-oracle-request.md
  - oracle/responses/20260521T093015Z-erdos536-iterated-endpoint-tower-oracle-response.md
---

# Proposition: Iterated endpoint-fiber towers have exact terminal residual value

## Statement

Let \(r\ge0\), and let
\[
P=P_0\supseteq P_1\supseteq\cdots\supseteq P_r
\]
be a finite endpoint tower such that, for each \(1\le j\le r\),
\[
P_{j-1}=P_j\sqcup X_j\sqcup Y_j,
\qquad X_j,Y_j\ne\varnothing.
\tag{1}
\]
Thus \(P_r\) and all endpoint classes \(X_j,Y_j\) are mutually disjoint.
Let \(\nu_P\) be a product law on \(2^P\) with coordinate probabilities
\(q_p\in(0,1)\), and let \(\nu_{P_r}\) be the restricted product law on
\(2^{P_r}\).  For \(x\in X_j\) and \(y\in Y_j\), put
\[
\alpha_{j,x}=q_x\prod_{u\in X_j\setminus\{x\}}(1-q_u),
\qquad
\beta_{j,y}=q_y\prod_{v\in Y_j\setminus\{y\}}(1-q_v),
\tag{2}
\]
and
\[
\alpha_j=\sum_{x\in X_j}\alpha_{j,x},
\qquad
\beta_j=\sum_{y\in Y_j}\beta_{j,y},
\qquad
\Gamma_r=\prod_{j=1}^r\alpha_j\beta_j,
\tag{3}
\]
with \(\Gamma_0=1\).

For an endpoint transcript
\[
\mathbf e=((x_1,y_1),\ldots,(x_r,y_r))
\in \prod_{j=1}^r(X_j\times Y_j),
\]
write
\[
E(\mathbf e)=\{x_1,y_1,\ldots,x_r,y_r\}.
\]
Given terminal fibers \(\mathcal R_{\mathbf e}\subseteq2^{P_r}\), define the
iterated exact endpoint-fiber tower
\[
\mathcal A
=
\{R\cup E(\mathbf e):
\mathbf e\in\prod_{j=1}^r(X_j\times Y_j),\
R\in\mathcal R_{\mathbf e}\}.
\tag{4}
\]
Then \(\mathcal A\) is pair-link-free in \(2^P\) if and only if every
terminal fiber \(\mathcal R_{\mathbf e}\) is pair-link-free in \(2^{P_r}\).

For a finite set \(W\) and real threshold \(t\), define
\[
\mathfrak M_W(t)
=
\sup\{\nu_W(\mathcal R):
\mathcal R\subseteq2^W,\ \mathcal R\text{ is pair-link-free},\
\mathcal R\subseteq\{R:|R|>t\}\}.
\tag{5}
\]
Let \(\mathfrak T_r(P_\bullet,X_\bullet,Y_\bullet)\) be the class of
iterated exact towers (4) whose terminal fibers are pair-link-free.  Then
\[
\sup_{\mathcal A\in\mathfrak T_r(P_\bullet,X_\bullet,Y_\bullet)}
\nu_P(\mathcal A\cap\{S:|S|>L\})
=
\Gamma_r\,\mathfrak M_{P_r}(L-2r).
\tag{6}
\]

In particular, for the prime-biased law \(\nu_P(p\in S)=1/p\) and
\[
H_{P,\theta}=\{S\subseteq P:|S|>\theta S_P\},
\qquad
S_P=\sum_{p\in P}\frac1p,
\]
one has
\[
\sup_{\mathcal A\in\mathfrak T_r(P_\bullet,X_\bullet,Y_\bullet)}
\nu_P(\mathcal A\cap H_{P,\theta})
=
\Gamma_r\,\mathfrak M_{P_r}(\theta S_P-2r).
\tag{7}
\]
Thus an iterated exact endpoint tower has no more high-support mass than the
terminal pair-link-free core residual multiplied by the product of the
one-from-each endpoint probabilities.

## Proof

The case \(r=0\) is just the definition of \(\mathfrak M_P(L)\), so assume
\(r\ge1\).

First prove the pair-link criterion.  Suppose \(A,B,C\in\mathcal A\) are
pairwise distinct and \(C\in I(A,B)\).  If the endpoint transcripts of
\(A\) and \(B\) differ, let \(j\) be any level where they differ.  If their
\(X_j\)-endpoints differ, then \(A\triangle B\) contains two distinct points
of \(X_j\), so every \(C\in I(A,B)\) contains both of them.  This is
impossible for a member of \(\mathcal A\), which contains exactly one point
from \(X_j\).  The same argument applies if their \(Y_j\)-endpoints differ.
Hence \(A\) and \(B\) have the same endpoint transcript \(\mathbf e\).

Now \(A\cup B\) contains no endpoint coordinates except those in
\(E(\mathbf e)\).  Since \(C\subseteq A\cup B\) and \(C\) contains exactly one
point from each \(X_j\) and \(Y_j\), the endpoint transcript of \(C\) is also
\(\mathbf e\).  Deleting the common endpoint set \(E(\mathbf e)\), the
condition \(C\in I(A,B)\) is exactly a pair-link triple inside the terminal
fiber \(\mathcal R_{\mathbf e}\).  Therefore \(\mathcal A\) is pair-link-free
whenever every terminal fiber is pair-link-free.  The converse is immediate:
any pair-link triple in a terminal fiber, after adjoining the same endpoint
transcript, becomes a pair-link triple in \(\mathcal A\).

Next compute the measure.  The transcript events are disjoint.  For a fixed
\(\mathbf e=((x_1,y_1),\ldots,(x_r,y_r))\), independence gives
\[
\nu_P(\{S:S\cap X_j=\{x_j\},\ S\cap Y_j=\{y_j\}\text{ for all }j\})
=
\prod_{j=1}^r\alpha_{j,x_j}\beta_{j,y_j}.
\tag{8}
\]
This event is independent of the terminal \(P_r\)-section.  Moreover every
set \(R\cup E(\mathbf e)\) has cardinality \(|R|+2r\).  Hence
\[
\nu_P(\mathcal A\cap\{S:|S|>L\})
=
\sum_{\mathbf e}
\left(\prod_{j=1}^r\alpha_{j,x_j}\beta_{j,y_j}\right)
\nu_{P_r}(\{R\in\mathcal R_{\mathbf e}:|R|>L-2r\}).
\tag{9}
\]
For every transcript, the truncated terminal fiber in (9) is pair-link-free
and lies inside \(\{R:|R|>L-2r\}\).  Its measure is therefore at most
\(\mathfrak M_{P_r}(L-2r)\).  Summing the endpoint weights gives
\[
\nu_P(\mathcal A\cap\{S:|S|>L\})
\le
\mathfrak M_{P_r}(L-2r)
\prod_{j=1}^r
\left(\sum_{x\in X_j}\alpha_{j,x}\right)
\left(\sum_{y\in Y_j}\beta_{j,y}\right)
=
\Gamma_r\,\mathfrak M_{P_r}(L-2r).
\]
Taking the supremum over \(\mathcal A\) proves the upper bound in (6).

For the reverse inequality, choose an extremal terminal core family
\(\mathcal R^*\subseteq\{R:|R|>L-2r\}\) for
\(\mathfrak M_{P_r}(L-2r)\).  Such a family exists because \(P_r\) is finite;
equivalently, one may use an \(\varepsilon\)-extremizer and let
\(\varepsilon\downarrow0\).  Put
\[
\mathcal R_{\mathbf e}=\mathcal R^*
\qquad\text{for every endpoint transcript }\mathbf e.
\]
The pair-link criterion just proved shows that the resulting tower is
pair-link-free, and (9) gives
\[
\nu_P(\mathcal A^*\cap\{S:|S|>L\})
=
\Gamma_r\,\nu_{P_r}(\mathcal R^*)
=
\Gamma_r\,\mathfrak M_{P_r}(L-2r).
\]
This proves (6).  The prime-biased statement (7) is the specialization
\(L=\theta S_P\).

## Depends on

- [[mrw-d7b3299d3813]] One-from-each two-class assemblies decouple by endpoint pair

## Used by

## Notes

- This proposition iterates the self-similar obstruction from
  [[mrw-fe13472e08c8]].  Repeating exact coherent two-class endpoint
  decompositions cannot create extra high-support mass; it only multiplies
  the terminal residual by endpoint one-from-each probabilities.
- [[mrw-fe13472e08c8]] is the \(r=1\) variational special case and conceptual
  ancestry.  The direct proof uses only the endpoint-transcript decoupling
  mechanism from [[mrw-d7b3299d3813]].
- The result is sharp inside the exact tower model, because the same terminal
  extremal core family in every endpoint transcript attains the bound.
- This does not prove \(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or any
  \(R_P(\theta)\) lift.  A terminal proof must either force positive-mass
  candidates to leave the exact tower and pay mixed-overlap defects such as
  [[mrw-bc27191b14d4]], or prove a genuinely stronger terminal-core residual
  theorem.
