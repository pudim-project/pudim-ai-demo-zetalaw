---
id: mrw-a32a6d3a5f20
type: proposition
title: Weighted cross-core Mantel bound for pair-link-free families
aliases: ["mrw-a32a6d3a5f20", "Weighted cross-core Mantel bound for pair-link-free families"]
status: proved
tags: [erdos-536, squarefree-support, pair-link, hypergraph-independent-set, two-extension-slice, weighted-mantel, cross-core-aggregation, product-measure, support-tail, patch-gate-audited]
parents: [mrw-354b105d4977, mrw-3c39ca3d1973, mrw-25cdd8da0601, mrw-55a8d9eddd2e]
refs: ["references/sources/20260520T102016Z-cross-core-mantel-context.md"]
  - raw/20260520T102016Z-erdos-536-weighted-cross-core-aggregation-of-triangle-free-t.md
  - references/sources/20260520T102016Z-cross-core-mantel-context.md
  - oracle/requests/20260520T102016Z-erdos536-cross-core-mantel-oracle-request.md
  - oracle/responses/20260520T102016Z-erdos536-cross-core-mantel-oracle-response.md
---

# Proposition: Weighted cross-core Mantel bound for pair-link-free families

## Statement
Let \(P\) be a finite set and let \(\nu\) be the product law on \(2^P\) with
\[
\nu(p\in A)=q_p,\qquad 0<q_p<1.
\]
Write
\[
\nu(A)=\prod_{p\in A}q_p\prod_{p\notin A}(1-q_p),
\qquad
a_p=\frac{q_p}{1-q_p}.
\]
For \(R\subseteq P\), put
\[
W(R)=\sum_{p\in P\setminus R}a_p.
\]

If \(\mathcal F\subseteq2^P\) is pair-link-free, then
\[
\sum_{A\in\mathcal F}\binom{|A|}{2}\nu(A)
\le
\frac14\sum_{R\subseteq P}\nu(R)W(R)^2.
\tag{1}
\]

In particular, for the prime-biased law \(q_p=1/p\), let
\[
S_P=\sum_{p\in P}\frac1p,
\qquad
T_P=\sum_{p\in P}\frac1{p^2(p-1)}.
\]
Then every pair-link-free \(\mathcal F\subseteq2^P\) satisfies
\[
\sum_{A\in\mathcal F}\binom{|A|}{2}\nu_P(A)
\le
\frac14\left(S_P^2+T_P\right).
\tag{2}
\]

Consequently, if
\[
H_{P,\theta}=\{A\subseteq P:\ |A|>\theta S_P\}
\]
and \(\theta S_P>1\), then every pair-link-free
\(\mathcal F\subseteq H_{P,\theta}\) satisfies
\[
\nu_P(\mathcal F)
\le
\frac{S_P^2+T_P}{2\theta S_P(\theta S_P-1)}.
\tag{3}
\]
For fixed \(\theta>0\) and \(P_k=\{p_1,\ldots,p_k\}\), this gives
\[
\limsup_{k\to\infty}\nu_{P_k}(\mathcal F_k)
\le
\frac1{2\theta^2}
\]
for any sequence of pair-link-free
\(\mathcal F_k\subseteq H_{P_k,\theta}\).  This asymptotic consequence is
nontrivial only when the right side is below \(1\), and it is not a vanishing
mass theorem.

Equivalently, the continuous denominator in (3) may be replaced by the sharper
integer denominator
\[
4\binom{\lfloor\theta S_P\rfloor+1}{2}
\]
whenever \(\lfloor\theta S_P\rfloor+1\ge2\).

## Proof
First record the weighted Mantel inequality needed below.  Let \(G=(V,E)\) be
triangle-free and let \(a_v\ge0\) be vertex weights.  Put
\[
W=\sum_{v\in V}a_v,\qquad
M=\sum_{uv\in E}a_ua_v,
\qquad
d(v)=\sum_{u:\ uv\in E}a_u.
\]
Here \(d(v)\) is the weighted open-neighborhood degree.
If \(uv\in E\), then \(N(u)\cap N(v)=\varnothing\), because a common neighbor
would form a triangle.  Hence
\[
d(u)+d(v)\le W
\qquad(uv\in E).
\]
Therefore
\[
\sum_{v\in V}a_vd(v)^2
=
\sum_{uv\in E}a_ua_v(d(u)+d(v))
\le
WM.
\tag{4}
\]
On the other hand,
\[
2M=\sum_{v\in V}a_vd(v),
\]
so Cauchy's inequality gives
\[
4M^2
\le
\left(\sum_{v\in V}a_v\right)
\left(\sum_{v\in V}a_vd(v)^2\right)
\le
W^2M.
\]
If \(M=0\) there is nothing to prove; otherwise \(M\le W^2/4\).

Now assume \(\mathcal F\) is pair-link-free.  For each \(R\subseteq P\), let
\[
G_R^\mathcal F=(P\setminus R,E_R^\mathcal F),
\qquad
\{x,y\}\in E_R^\mathcal F
\Longleftrightarrow
R\cup\{x,y\}\in\mathcal F.
\]
By [[mrw-354b105d4977]], \(G_R^\mathcal F\) is triangle-free.  Applying the
weighted Mantel inequality with vertex weights \(a_p=q_p/(1-q_p)\) on
\(P\setminus R\) gives
\[
\sum_{\{x,y\}\in E_R^\mathcal F}a_xa_y
\le
\frac14W(R)^2.
\tag{5}
\]
Multiplying (5) by \(\nu(R)\) and summing over all \(R\subseteq P\), we get
\[
\sum_{R\subseteq P}\nu(R)
\sum_{\{x,y\}\in E_R^\mathcal F}a_xa_y
\le
\frac14\sum_{R\subseteq P}\nu(R)W(R)^2.
\tag{6}
\]
For \(x,y\notin R\), the odds identity gives
\[
\nu(R)a_xa_y
=
\nu(R\cup\{x,y\}).
\tag{7}
\]
Thus the left side of (6) is
\[
\sum_{R\subseteq P}
\sum_{\substack{\{x,y\}\subseteq P\setminus R\\R\cup\{x,y\}\in\mathcal F}}
\nu(R\cup\{x,y\}).
\]
Each \(A\in\mathcal F\) is counted once for every two-element subset
\(\{x,y\}\subseteq A\), namely with \(R=A\setminus\{x,y\}\).  Hence the left
side equals
\[
\sum_{A\in\mathcal F}\binom{|A|}{2}\nu(A),
\]
which proves (1).

For the prime-biased specialization, \(q_p=1/p\) and
\[
a_p=\frac1{p-1}.
\]
If \(R\sim\nu_P\), then
\[
W(R)=\sum_{p\in P}\frac{\mathbf 1_{p\notin R}}{p-1}.
\]
Therefore
\[
\mathbb E W(R)=\sum_{p\in P}\frac{1-1/p}{p-1}
=
\sum_{p\in P}\frac1p
=S_P
\]
and, by independence,
\[
\operatorname{Var}(W(R))
=
\sum_{p\in P}
\frac{1}{(p-1)^2}\frac1p\left(1-\frac1p\right)
=
\sum_{p\in P}\frac1{p^2(p-1)}
=T_P.
\]
Thus
\[
\sum_{R\subseteq P}\nu_P(R)W(R)^2
=
\mathbb E W(R)^2
=
S_P^2+T_P,
\]
and (2) follows from (1).

Finally, if \(A\in H_{P,\theta}\) and \(\theta S_P>1\), then
\[
\binom{|A|}{2}\ge \frac{\theta S_P(\theta S_P-1)}2.
\]
Combining this lower bound with (2) gives (3).  Along
\(P_k=\{p_1,\ldots,p_k\}\), the quantity \(T_{P_k}\) is bounded while
\(S_k\to\infty\), yielding the displayed limsup bound.

## Depends on
- [[mrw-354b105d4977]] Pair-link-free two-extension slices are triangle-free
- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree residuals

## Used by

## Notes
- This is the first global weighted aggregation of the common-core
  triangle-free slice theorem, but it is still nonterminal.  It gives a
  second-support-moment bound, not \(\nu_{P_k}(\mathcal F_k)\to0\).
- The proof uses the actual pair-link-free hypothesis through
  [[mrw-354b105d4977]].  It does not apply to arbitrary union-free families:
  a union-free family need not have triangle-free two-extension slice graphs.
- The frontmatter parents include `mrw-25cdd8da0601` and `mrw-55a8d9eddd2e`
  as route context, but the proof dependencies are only the pair-link
  formulation and the triangle-free slice theorem listed above.
- Complete bipartite slice graphs are exactly the local stress test for the
  weighted Mantel inequality.  The global estimate shows what one obtains by
  summing all such weighted local bounds, and the remaining gap is that the
  resulting high-support mass bound is only constant-size.
- The result becomes a vanishing theorem only if a later argument improves the
  aggregate \(S_P^2/4\) scale to \(o(S_P^2)\) under pair-link-freeness.
- No claim is made for \(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or a lift
  to \(R_P(\theta)\).  A future theorem must improve the factor
  \(S_P^2/4\) by exploiting cross-core coherence beyond weighted Mantel, or
  else construct a genuine positive-mass pair-link-free family that nearly
  saturates this bound and survives the full interval criterion.
