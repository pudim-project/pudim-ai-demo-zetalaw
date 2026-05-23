---
id: mrw-c6d0c6fa4d30
type: proposition
title: Path-shadow overlap bottleneck for endpoint-pair cores
aliases: ["mrw-c6d0c6fa4d30", "Path-shadow overlap bottleneck for endpoint-pair cores"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, path-shadow, lower-shadow, product-measure, overlap-bottleneck, endpoint-pair-core, support-tail, patch-gate-audited]
parents: [mrw-2bcc2955fe38, mrw-3c39ca3d1973, mrw-354b105d4977, mrw-a32a6d3a5f20, mrw-55a8d9eddd2e]
refs: ["references/sources/20260520T114136Z-path-shadow-overlap-context.md"]
  - raw/20260520T114136Z-erdos-536-product-measure-lower-shadow-theorem-for-pair-link.md
  - references/sources/20260520T114136Z-path-shadow-overlap-context.md
  - oracle/requests/20260520T114136Z-erdos536-path-shadow-overlap-oracle-request.md
  - oracle/responses/20260520T114136Z-erdos536-path-shadow-overlap-oracle-response.md
---

# Proposition: Path-shadow overlap bottleneck for endpoint-pair cores

## Statement
Let \(P\) be a finite set, let \(x,z\in P\) be distinct, and let
\(\mathcal F\subseteq2^P\) be pair-link-free: there are no pairwise distinct
\(A,B,C\in\mathcal F\) with
\[
C\in I^\circ(A,B),
\qquad
I^\circ(A,B)=\{C:A\triangle B\subseteq C\subseteq A\cup B\}\setminus\{A,B\}.
\]
Write
\[
\Omega_{xz}=2^{P\setminus\{x,z\}}
\]
and define the endpoint-pair core
\[
\mathcal E_{xz}
=
\{D\in\Omega_{xz}:D\cup\{x,z\}\in\mathcal F\}.
\]
For \(y\in P\setminus\{x,z\}\), define
\[
\mathcal P^y_{xz}
=
\{R\subseteq P\setminus\{x,y,z\}:
R\cup\{x,y\}\in\mathcal F,\ R\cup\{y,z\}\in\mathcal F\}
\]
and the corresponding endpoint-pair path shadow, equivalently the
\(y\)-augmented lower shadow,
\[
\mathcal S^y_{xz}
=
\{D\in\Omega_{xz}:D\subseteq R\cup\{y\}
\text{ for some }R\in\mathcal P^y_{xz}\}.
\]
Put
\[
\mathcal S_{xz}
=
\bigcup_{y\in P\setminus\{x,z\}}\mathcal S^y_{xz}.
\]
Then
\[
\mathcal E_{xz}\cap\mathcal S_{xz}=\varnothing.
\tag{1}
\]

Let \(\mu\) be any probability measure on \(\Omega_{xz}\).  Set
\[
T=\sum_{y\in P\setminus\{x,z\}}\mu(\mathcal S^y_{xz}),
\qquad
Q=\sum_{y,y'\in P\setminus\{x,z\}}
\mu(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz}).
\]
The sum defining \(Q\) is the ordered double sum and includes the diagonal
terms \(y=y'\).
If \(T>0\), then \(Q>0\) and
\[
\mu(\mathcal S_{xz})\ge \frac{T^2}{Q}.
\tag{2}
\]
Consequently,
\[
\mu(\mathcal E_{xz})+\frac{T^2}{Q}\le1,
\tag{3}
\]
and, when \(\mu(\mathcal E_{xz})<1\),
\[
Q\ge\frac{T^2}{1-\mu(\mathcal E_{xz})}.
\tag{4}
\]

Finally suppose that \(\mu=\mu_{xz}\) is a product measure on
\(\Omega_{xz}\), with coordinate probabilities \(0<q_p<1\), and let
\(\mu_{xyz}\) denote the same product law restricted to
\(P\setminus\{x,y,z\}\).  Then, for each \(y\),
\[
\mu_{xz}(\mathcal S^y_{xz})
\ge
\mu_{xyz}(\mathcal P^y_{xz}).
\tag{5}
\]

## Proof
First prove (1).  Let \(D\in\mathcal S^y_{xz}\).  Then there exists
\(R\in\mathcal P^y_{xz}\) such that \(D\subseteq R\cup\{y\}\).  By the
definition of \(\mathcal P^y_{xz}\),
\[
R\cup\{x,y\},\qquad R\cup\{y,z\}\in\mathcal F.
\]
The path-shadow proposition [[mrw-2bcc2955fe38]] applied to this two-edge path
implies that every endpoint-pair completion \(D\cup\{x,z\}\), with
\(D\subseteq R\cup\{y\}\), is absent from \(\mathcal F\).  Thus
\(D\notin\mathcal E_{xz}\).  Since this holds for every \(y\), the endpoint
core \(\mathcal E_{xz}\) is disjoint from \(\mathcal S_{xz}\).

For (2), define the shadow multiplicity function
\[
N(D)=\sum_{y\in P\setminus\{x,z\}}1_{\mathcal S^y_{xz}}(D)
\qquad(D\in\Omega_{xz}).
\]
The support of \(N\) is \(\mathcal S_{xz}\), and therefore
\[
\int N\,d\mu=T,
\qquad
\int N^2\,d\mu=Q.
\]
Cauchy's inequality gives
\[
T^2
=
\left(\int_{\mathcal S_{xz}}N\,d\mu\right)^2
\le
\mu(\mathcal S_{xz})\int_{\mathcal S_{xz}}N^2\,d\mu
=
\mu(\mathcal S_{xz})Q.
\]
If \(T>0\), then \(Q>0\), and division gives (2).  Combining (1) and (2)
gives (3), and rearranging (3) gives (4).

It remains to prove the product-measure lower bound (5).  For fixed \(y\),
the two embedded copies
\[
\mathcal C^0_y=\{R:R\in\mathcal P^y_{xz}\},
\qquad
\mathcal C^1_y=\{R\cup\{y\}:R\in\mathcal P^y_{xz}\}
\]
are disjoint subsets of \(\Omega_{xz}\).  Both are contained in
\(\mathcal S^y_{xz}\), because \(R\subseteq R\cup\{y\}\) and
\(R\cup\{y\}\subseteq R\cup\{y\}\).  Product independence gives
\[
\mu_{xz}(\mathcal C^0_y)
=(1-q_y)\mu_{xyz}(\mathcal P^y_{xz}),
\qquad
\mu_{xz}(\mathcal C^1_y)
=q_y\mu_{xyz}(\mathcal P^y_{xz}).
\]
Hence
\[
\mu_{xz}(\mathcal S^y_{xz})
\ge
\mu_{xz}(\mathcal C^0_y)+\mu_{xz}(\mathcal C^1_y)
=
\mu_{xyz}(\mathcal P^y_{xz}),
\]
which proves (5).

## Depends on
- [[mrw-2bcc2955fe38]] Pair-link two-edge paths cast lower-core shadows
- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree residuals
- [[mrw-354b105d4977]] Pair-link-free two-extension slices are triangle-free
- [[mrw-a32a6d3a5f20]] Weighted cross-core Mantel bound for pair-link-free families
- [[mrw-55a8d9eddd2e]] Prime-biased weighted union-free theorem

## Used by

## Notes
- This is a lower-bound and bottleneck theorem for endpoint-pair path shadows.
  It is not a proof that the prime-biased high-support pair-link-free mass
  tends to zero.
- The phrase "path shadow" is used because \(\mathcal S^y_{xz}\) includes all
  \(D\subseteq R\cup\{y\}\), not only the strict lower-core sets
  \(D\subseteq R\).
- Since \(Q\) includes the diagonal, (4) forces genuinely off-diagonal shadow
  overlap only after the lower bound exceeds the diagonal scale.  In particular,
  the proposition itself does not control intersections
  \(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz}\) for \(y\ne y'\).
- Equation (4) identifies the next obstruction precisely: if an endpoint-pair
  core \(\mathcal E_{xz}\) has positive product-measure mass while many
  \(x-y-z\) two-edge paths exist, then the corresponding path shadows must
  overlap heavily.  The next route must control or exploit this overlap
  collapse.
- No reverse lift to the exponent-grid residual \(R_P(\theta)\) is obtained
  here.
