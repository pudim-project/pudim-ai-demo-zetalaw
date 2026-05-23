---
id: mrw-f83b56a1aa89
type: proposition
title: Complete bipartite slices saturate path-shadow overlap
aliases: ["mrw-f83b56a1aa89", "Complete bipartite slices saturate path-shadow overlap", "Bipartite slice path-shadow collapse"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, path-shadow, overlap-collapse, complete-bipartite, product-measure, obstruction, support-tail, patch-gate-audited]
parents: [mrw-c6d0c6fa4d30, mrw-2bcc2955fe38, mrw-354b105d4977, mrw-a32a6d3a5f20, mrw-3c39ca3d1973]
refs: ["references/sources/20260520T233725Z-bipartite-path-shadow-collapse-context.md"]
  - raw/20260520T233725Z-erdos-536-path-shadow-overlap-collapse-stress-test-for-compl.md
  - references/sources/20260520T233725Z-bipartite-path-shadow-collapse-context.md
  - oracle/requests/20260520T233725Z-erdos536-bipartite-path-shadow-collapse-oracle-request.md
  - oracle/responses/20260520T233725Z-erdos536-bipartite-path-shadow-collapse-oracle-response.md
---

# Proposition: Complete bipartite slices saturate path-shadow overlap

## Statement

Let \(P\) be a finite set.  Let \(R,X,Y\subseteq P\) be pairwise disjoint, with
\(|X|\ge2\) and \(Y\ne\varnothing\), and define
\[
\mathcal F_{R,X,Y}
=
\{R\cup\{u,v\}:u\in X,\ v\in Y\}.
\]
Then \(\mathcal F_{R,X,Y}\) is pair-link-free: there are no pairwise distinct
\(A,B,C\in\mathcal F_{R,X,Y}\) with
\[
C\in I^\circ(A,B),
\qquad
I^\circ(A,B)
=
\{C:A\triangle B\subseteq C\subseteq A\cup B\}\setminus\{A,B\}.
\]

Fix distinct \(x,z\in X\).  In the notation of
[[mrw-c6d0c6fa4d30]], the endpoint-pair core is empty:
\[
\mathcal E_{xz}=\varnothing.
\]
The nonempty endpoint-pair path cores are exactly
\[
\mathcal P^y_{xz}=\{R\}
\qquad(y\in Y),
\]
and
\[
\mathcal P^r_{xz}
=
\{(R\setminus\{r\})\cup\{y\}:y\in Y\}
\qquad(r\in R).
\]
For \(w\notin R\cup Y\cup\{x,z\}\), the path core
\(\mathcal P^w_{xz}\) is empty.  Consequently,
\[
\mathcal S^y_{xz}=2^{R\cup\{y\}}
\qquad(y\in Y),
\]
while for each \(r\in R\),
\[
\mathcal S^r_{xz}
=
\bigcup_{y\in Y}2^{R\cup\{y\}}.
\]

Let \(\mu\) be a product measure on \(\Omega_{xz}=2^{P\setminus\{x,z\}}\), with
\(\mu(p\in D)=q_p\in(0,1)\).  Put
\[
B_{xz}=\prod_{p\in P\setminus(R\cup Y\cup\{x,z\})}(1-q_p)
\prod_{y\in Y}(1-q_y),
\]
and, for \(y\in Y\),
\[
a_y=\frac{q_y}{1-q_y},
\qquad
c_y=\frac1{1-q_y}=1+a_y.
\]
Let
\[
A_Y=\sum_{y\in Y}a_y,
\qquad
C_Y=\sum_{y\in Y}c_y=|Y|+A_Y,
\qquad
m=|R|,
\qquad
n=|Y|.
\]
Then
\[
\mu(\mathcal S^y_{xz})=B_{xz}c_y
\qquad (y\in Y),
\]
\[
\mu(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz})=B_{xz}
\qquad (y\ne y',\ y,y'\in Y),
\]
\[
\mu(\mathcal S^r_{xz})=B_{xz}(1+A_Y)
\qquad(r\in R),
\]
and
\[
\mu\!\left(\bigcup_{w\in P\setminus\{x,z\}}\mathcal S^w_{xz}\right)
=
B_{xz}(1+A_Y).
\]
Consequently, with
\[
T=\sum_{w\in P\setminus\{x,z\}}\mu(\mathcal S^w_{xz}),
\qquad
Q=\sum_{w,w'\in P\setminus\{x,z\}}
\mu(\mathcal S^w_{xz}\cap\mathcal S^{w'}_{xz}),
\]
where \(Q\) is the ordered diagonal-including double sum, one has
\[
T=B_{xz}\bigl(C_Y+m(1+A_Y)\bigr)
\]
and
\[
Q=
B_{xz}\Bigl(C_Y+n(n-1)+2mC_Y+m^2(1+A_Y)\Bigr).
\]

Thus the obstruction isolated in [[mrw-c6d0c6fa4d30]] is real: a locally
complete bipartite slice can create many \(x-w-z\) two-edge paths while the
corresponding endpoint-pair path shadows collapse onto the same union of
downsets.  The Cauchy lower bound
\[
\mu\!\left(\bigcup_w\mathcal S^w_{xz}\right)\ge \frac{T^2}{Q}
\]
is asymptotically sharp up to the factor
\[
\frac{
(1+A_Y)\bigl(C_Y+n(n-1)+2mC_Y+m^2(1+A_Y)\bigr)
}{
\bigl(C_Y+m(1+A_Y)\bigr)^2
},
\]
which tends to \(1\) when \(q_y\to0\) uniformly over fixed \(R\) and \(Y\).

## Proof

First prove pair-link-freeness.  Let
\[
A=R\cup e,\qquad B=R\cup e'
\]
be distinct members of \(\mathcal F_{R,X,Y}\), where \(e,e'\) are edges of the
complete bipartite graph \(K_{X,Y}\).  If \(e\cap e'=\varnothing\), then
\(A\triangle B=e\cup e'\) has four points outside \(R\).  No member of
\(\mathcal F_{R,X,Y}\) contains four points outside \(R\), so no
\(C\in\mathcal F_{R,X,Y}\) can lie in \(I(A,B)\).

If \(e\) and \(e'\) share their \(X\)-endpoint, then \(A\triangle B\) consists
of two distinct points of \(Y\).  Every \(C\in I(A,B)\) must contain both of
those \(Y\)-points, while every member of \(\mathcal F_{R,X,Y}\) contains
exactly one point of \(Y\).  Again no \(C\in\mathcal F_{R,X,Y}\) lies in
\(I(A,B)\).  The case where \(e\) and \(e'\) share their \(Y\)-endpoint is
identical, with \(X\) and \(Y\) interchanged.  Thus
\(\mathcal F_{R,X,Y}\) is pair-link-free.

Now fix distinct \(x,z\in X\).  No member of \(\mathcal F_{R,X,Y}\) contains
both \(x\) and \(z\), so \(\mathcal E_{xz}=\varnothing\).

If \(y\in Y\), then
\[
R\cup\{x,y\},\qquad R\cup\{y,z\}
\]
are members of \(\mathcal F_{R,X,Y}\), and the only common core in the
definition of \(\mathcal P^y_{xz}\) is \(R\).  Thus
\[
\mathcal P^y_{xz}=\{R\},
\qquad
\mathcal S^y_{xz}=2^{R\cup\{y\}}.
\]

If \(r\in R\), then a set \(C\subseteq P\setminus\{x,z,r\}\) lies in
\(\mathcal P^r_{xz}\) precisely when
\[
C\cup\{x,r\}=R\cup\{x,y\},
\qquad
C\cup\{r,z\}=R\cup\{z,y\}
\]
for some \(y\in Y\).  Hence
\[
\mathcal P^r_{xz}
=
\{(R\setminus\{r\})\cup\{y\}:y\in Y\},
\]
and
\[
\mathcal S^r_{xz}
=
\bigcup_{y\in Y}2^{R\cup\{y\}}.
\]
If \(w\notin R\cup Y\cup\{x,z\}\), no such representation is possible, so
\(\mathcal P^w_{xz}\) is empty.

The product-measure formulas follow from these explicit shadows.  For
\(y\in Y\), the event \(\mathcal S^y_{xz}=2^{R\cup\{y\}}\) means that every
coordinate in \(P\setminus(R\cup\{x,z,y\})\) is absent, while the coordinates
in \(R\cup\{y\}\) are free.  Therefore
\[
\mu(\mathcal S^y_{xz})
=
B_{xz}c_y.
\]
For \(y\ne y'\) in \(Y\),
\[
2^{R\cup\{y\}}\cap2^{R\cup\{y'\}}=2^R,
\]
so
\[
\mu(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz})=B_{xz}.
\]

The union of all \(Y\)-shadows consists of all subsets of \(R\), together with
all subsets of \(R\cup\{y\}\) containing \(y\) for a unique \(y\in Y\).  Since
each \(r\)-shadow is the same union, the union over all nonempty shadows is
also this set.  Its measure is
\[
B_{xz}
+\sum_{y\in Y}q_y
\prod_{p\in P\setminus(R\cup Y\cup\{x,z\})}(1-q_p)
\prod_{\substack{y'\in Y\\y'\ne y}}(1-q_{y'})
=
B_{xz}(1+A_Y).
\]
This also gives
\[
\mu(\mathcal S^r_{xz})=B_{xz}(1+A_Y)
\qquad(r\in R).
\]

Now sum the ordered intersections.  The \(Y\)-\(Y\) part contributes
\[
B_{xz}\bigl(C_Y+n(n-1)\bigr),
\]
with the first term from the diagonal and the second from ordered distinct
pairs.  The \(R\)-\(Y\) and \(Y\)-\(R\) parts contribute
\[
2mB_{xz}C_Y,
\]
because \(\mathcal S^y_{xz}\subseteq\mathcal S^r_{xz}\).  The \(R\)-\(R\) part
contributes
\[
m^2B_{xz}(1+A_Y).
\]
Adding these terms proves the displayed formula for \(Q\), and the formula for
\(T\) is obtained by summing the individual shadow measures.

Finally, substituting the expressions for \(T\), \(Q\), and the union measure
into the Cauchy bound from [[mrw-c6d0c6fa4d30]] gives the displayed sharpness
factor.  If \(q_y\to0\) uniformly over fixed \(R\) and \(Y\), then
\(A_Y\to0\) and \(C_Y\to n\), so the factor tends to
\[
\frac{n+n(n-1)+2mn+m^2}{(n+m)^2}=1.
\]
This proves the claimed asymptotic sharpness.

## Depends on

- [[mrw-c6d0c6fa4d30]] Path-shadow overlap bottleneck for endpoint-pair cores
- [[mrw-2bcc2955fe38]] Pair-link two-edge paths cast lower-core shadows
- [[mrw-354b105d4977]] Pair-link-free two-extension slices are triangle-free
- [[mrw-a32a6d3a5f20]] Weighted cross-core Mantel bound for pair-link-free families
- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree residuals

## Notes

- This is a local obstruction and stress test, not a positive-mass
  high-support counterexample to the prime-biased residual problem.
- The first draft of this node omitted the additional middle vertices
  \(r\in R\).  The Oracle audit caught that omission; the corrected statement
  includes the \(R\)-middle shadows and the resulting global \(T,Q\) formulas.
- The construction explains why controlling \(Q\) purely by the number of
  middle vertices or path cores cannot prove a vanishing theorem: complete
  bipartite slices can make the off-diagonal part of \(Q\) quadratic while the
  path-shadow union stays essentially one common product-measure region.
- A terminal theorem must use a global cross-core constraint that prevents
  these bipartite-slice collapses from carrying positive \(\nu_{P_k}\)-mass in
  high support, or it must construct a genuine positive-mass coherent version
  and test the full pair-link interval criterion.
- No reverse lift to the exponent-grid residual \(R_P(\theta)\) is obtained.
