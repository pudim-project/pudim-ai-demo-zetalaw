---
id: mrw-7c6a0e9f2d31
type: proposition
title: Private-shadow bound kills sparse-intersection high-support codes
aliases: ["mrw-7c6a0e9f2d31", "Private-shadow sparse-intersection code quarantine"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, union-free, pair-link, sparse-intersection, private-shadow, packing, biased-measure, support-tail, route-kill]
parents: [mrw-55a8d9eddd2e, mrw-d0402aea6f58, mrw-b4075311abd3, mrw-cc4f876149b7, mrw-3c39ca3d1973, mrw-4b9f5c2e6a1d, mrw-9afb17b1b84a]
refs: []
  - raw/20260519T173438Z-erdos536-private-shadow-code-quarantine.md
  - references/requests/20260519T173438Z-private-shadow-erudition-gate.md
  - references/sources/20260519T173438Z-private-shadow-context.md
  - theory/forage/requests/20260519T173438Z-erdos536-private-shadow-code-quarantine-request.md
  - theory/forage/responses/20260519T173438Z-erdos536-private-shadow-code-quarantine-response.md
  - raw/20260519T175028Z-scout-forage-ingest.md
  - oracle/requests/20260519T173438Z-erdos536-private-shadow-code-oracle-request.md
  - oracle/responses/20260519T173438Z-erdos536-private-shadow-code-oracle-response.md
---

# Proposition: Private-shadow bound kills sparse-intersection high-support codes

## Statement

Let \(P\) be a finite set of primes, and let \(\nu_P\) be the product law on
\(2^P\) with
\[
\nu_P(p\in X)=\frac1p.
\]
Put
\[
q_p=\frac1p,\qquad
a_p=\frac{q_p}{1-q_p}=\frac1{p-1},\qquad
\delta_P=\prod_{p\in P}(1-q_p).
\]
Let \(\mathcal F\subseteq2^P\).  Suppose that every \(A\in\mathcal F\) has
\[
|A|\ge r
\]
and that every two distinct \(A,B\in\mathcal F\) satisfy
\[
|A\cap B|<t,
\]
where \(1\le t\le r\).  Then
\[
\nu_P(\mathcal F)
\le
\frac{\nu_P(|X|=t)}{\binom r t}
\le
\binom r t^{-1}.
\tag{1}
\]

Consequently, for
\[
P_k=\{p_1,\ldots,p_k\},\qquad
S_k=\sum_{i\le k}\frac1{p_i},
\]
and fixed \(0<\gamma<\theta\), any family
\[
\mathcal F_k\subseteq \{A\subseteq P_k: |A|>\theta S_k\}
\]
whose distinct members satisfy
\[
|A\cap B|<\gamma S_k
\]
has
\[
\nu_{P_k}(\mathcal F_k)\to0.
\tag{2}
\]

Moreover, sparse-intersection capped bands give no positive-mass obstruction to
the union-free or squarefree pair-link routes:

1. If \(0<\theta<\alpha<2\theta\) and
   \(\mathcal F_k\subseteq\{\theta S_k<|A|\le\alpha S_k\}\) has all distinct
   intersections \(<\gamma S_k\) for some \(0<\gamma<2\theta-\alpha\), then
   \(\mathcal F_k\) is union-free for all large \(k\), but
   \(\nu_{P_k}(\mathcal F_k)\to0\).
2. If \(0<\theta<\alpha<2\theta\) and
   \(\mathcal F_k\subseteq\{\theta S_k<|A|\le\alpha S_k\}\) has all distinct
   intersections \(<\gamma S_k\) for some
   \(0<\gamma<(2\theta-\alpha)/2\), then every pair-link interval
   \(I(A,B)\) from [[mrw-3c39ca3d1973]] lies above the upper cap for all
   distinct \(A,B\in\mathcal F_k\).  Hence the family is squarefree
   pair-link-free, but still has \(\nu_{P_k}(\mathcal F_k)\to0\).

In particular, for \(1/2<\theta<1\), any positive-mass high-support
squarefree pair-link obstruction has a positive-mass capped part for some
\(1<\alpha<2\theta\), and that capped part cannot have uniformly
sublinear or small-linear pairwise intersections.  Thus the broad
low-overlap code template is impossible; any positive-mass capped obstruction
must contain linearly large intersections somewhere.

## Proof

For \(A\subseteq P\), write
\[
a_A=\prod_{p\in A}a_p.
\]
Then
\[
\nu_P(\mathcal F)=\delta_P\sum_{A\in\mathcal F}a_A.
\tag{3}
\]
For each \(A\in\mathcal F\),
\[
a_A
=
\binom{|A|}{t}^{-1}
\sum_{\substack{T\subseteq A\\ |T|=t}} a_Ta_{A\setminus T}
\le
\binom r t^{-1}
\sum_{\substack{T\subseteq A\\ |T|=t}} a_Ta_{A\setminus T}.
\tag{4}
\]
The \(t\)-subsets \(T\) appearing in (4) are private to their parent member
\(A\).  Indeed, if the same \(T\) lay in two distinct members \(A\) and \(B\),
then \(|A\cap B|\ge t\), contrary to the hypothesis.

Since \(a_p=1/(p-1)\le1\), one has \(a_{A\setminus T}\le1\).  Summing (4) over
\(A\in\mathcal F\) and using privacy gives
\[
\nu_P(\mathcal F)
\le
\delta_P\binom r t^{-1}
\sum_{\substack{T\subseteq P\\ |T|=t}}a_T
=
\binom r t^{-1}\nu_P(|X|=t)
\le
\binom r t^{-1}.
\]
This proves (1).

For the asymptotic statement, take
\[
r_k=\lfloor\theta S_k\rfloor+1,\qquad
t_k=\lceil\gamma S_k\rceil.
\]
Since \(0<\gamma<\theta\), \(1\le t_k\le r_k\) for all sufficiently large
\(k\), and
\[
\binom{r_k}{t_k}\to\infty.
\]
Applying (1) gives (2).

Now assume \(0<\theta<\alpha<2\theta\) and
\(\mathcal F_k\subseteq\{\theta S_k<|A|\le\alpha S_k\}\).  If distinct
\(A,B\in\mathcal F_k\) satisfy \(|A\cap B|<\gamma S_k\) with
\(\gamma<2\theta-\alpha\), then
\[
|A\cup B|
=|A|+|B|-|A\cap B|
>(2\theta-\gamma)S_k
>\alpha S_k.
\]
Thus \(A\cup B\notin\mathcal F_k\), so the capped family is union-free.  Its
mass still vanishes by (2), because \(\gamma<2\theta-\alpha<\theta\).

For the pair-link statement, use the stronger condition
\(\gamma<(2\theta-\alpha)/2\).  Then
\[
|A\triangle B|
=|A|+|B|-2|A\cap B|
>(2\theta-2\gamma)S_k
>\alpha S_k.
\]
Every \(C\in I(A,B)\) contains \(A\triangle B\).  Hence
\[
|C|>\alpha S_k,
\]
so \(I(A,B)\) misses the capped family.  By the pair-link criterion
[[mrw-3c39ca3d1973]], this gives a squarefree pair-link-free family, but (2)
again forces vanishing mass.

It remains to justify the final positive-mass consequence.  Under
\(\nu_{P_k}\),
\[
\mathbb E|X|=S_k,\qquad
\operatorname{Var}(|X|)=\sum_{i\le k}\frac1{p_i}\left(1-\frac1{p_i}\right)
\le S_k.
\]
Since \(S_k\to\infty\), Chebyshev gives
\[
\nu_{P_k}(|X|>\alpha S_k)\to0
\]
for every fixed \(\alpha>1\).  If \(1/2<\theta<1\) and a high-support
pair-link obstruction has positive mass along a subsequence, choose
\(1<\alpha<2\theta\).  Its capped part
\[
\mathcal F_k\cap\{\theta S_k<|A|\le\alpha S_k\}
\]
still has positive mass along a further subsequence.  The pair-link
sparse-intersection conclusion then rules out uniformly low overlaps on that
capped part.  Therefore a positive-mass capped obstruction must exhibit
linearly large intersections somewhere.

## Consequences

This does not prove the prime-biased weighted union-free theorem
[[mrw-55a8d9eddd2e]].  It eliminates a natural non-root counterexample
template: a high-support family whose members behave like a broad low-overlap
code.  Such families can be union-free or can avoid all pair-link intervals
inside a narrow upper rank cap, but the private-shadow count shows that their
\(\nu_{P_k}\)-mass vanishes.

The next obstruction, if any, must therefore involve high-intersection
phenomena after capping.  A useful continuation target is to quantify whether
those linearly overlapping pairs force a genuine cluster, a rooted/container
mechanism not defeated by the near-total-root equivalence
[[mrw-4b9f5c2e6a1d]], or instead allow an explicit positive-mass
high-intersection pair-link-free family.
