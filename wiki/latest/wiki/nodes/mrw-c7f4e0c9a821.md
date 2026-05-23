---
id: mrw-c7f4e0c9a821
type: proposition
title: Entropy overlap energy forces linearly many high-intersection clusters
aliases: ["mrw-c7f4e0c9a821", "Conditional overlap-energy bound", "Entropy overlap graph bound"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, union-free, pair-link, overlap-graph, relative-entropy, product-measure, biased-measure, high-intersection, cluster-cover, route-kill]
parents: [mrw-18e9c7b0a5af, mrw-7c6a0e9f2d31, mrw-55a8d9eddd2e, mrw-d0402aea6f58, mrw-b4075311abd3, mrw-cc4f876149b7, mrw-3c39ca3d1973]
refs: ["references/sources/20260519T233444Z-overlap-entropy-context.md"]
  - raw/20260519T233444Z-erdos536-mixed-overlap-graph.md
  - references/requests/20260519T233444Z-overlap-entropy-erudition-gate.md
  - references/sources/20260519T233444Z-overlap-entropy-context.md
  - theory/forage/requests/20260519T233444Z-erdos536-mixed-overlap-graph-request.md
  - theory/forage/responses/20260519T233444Z-erdos536-mixed-overlap-graph-response.md
  - raw/20260519T234204Z-scout-forage-ingest.md
  - oracle/requests/20260519T233444Z-erdos536-overlap-entropy-oracle-request.md
  - oracle/responses/20260519T233444Z-erdos536-overlap-entropy-oracle-response.md
---

# Proposition: Entropy overlap energy forces linearly many high-intersection clusters

## Statement

Let \(P\) be a finite set of primes and let \(\nu_P\) be the product law on
\(2^P\) with
\[
\nu_P(p\in X)=q_p=\frac1p.
\]
Put
\[
\Sigma_2(P)=\sum_{p\in P}\frac1{p^2}.
\]
Let \(\mathcal F\subseteq2^P\) have positive mass
\[
m=\nu_P(\mathcal F)>0.
\]
Let \(X,Y\) be independent \(\nu_P\)-samples conditioned on lying in
\(\mathcal F\), and write
\[
a_p=\Pr(p\in X\mid X\in\mathcal F).
\]
Then
\[
\mathbb E\bigl(|X\cap Y|\mid X,Y\in\mathcal F\bigr)
=
\sum_{p\in P}a_p^2
\le
4\Sigma_2(P)+2\log\frac1m.
\tag{1}
\]
Consequently, for every \(t\ge1\),
\[
(\nu_P\times\nu_P)
\{(A,B)\in\mathcal F^2:\ |A\cap B|\ge t\}
\le
m^2\,
\frac{4\Sigma_2(P)+2\log(1/m)}{t}.
\tag{2}
\]

Suppose in addition that \(\mathcal F\) is covered by
\(M\) subfamilies
\[
\mathcal F\subseteq\bigcup_{j=1}^M\mathcal C_j,
\qquad 1\le M<\infty,
\]
where every member of every \(\mathcal C_j\) has size at least \(t\), and every
two distinct members of the same \(\mathcal C_j\) have intersection at least
\(t\).  Then
\[
M
\ge
\frac{t}{4\Sigma_2(P)+2\log(1/m)}.
\tag{3}
\]

In particular, let
\[
P_k=\{p_1,\ldots,p_k\},
\qquad
S_k=\sum_{i\le k}\frac1{p_i},
\qquad
H_{k,\theta}=\{A\subseteq P_k:\ |A|>\theta S_k\}.
\]
Fix \(0<\gamma<\theta<1\) and \(\eta>0\).  If
\(\mathcal F_k\subseteq H_{k,\theta}\) and
\(\nu_{P_k}(\mathcal F_k)\ge\eta\), then the ordered conditional edge density
of the \(\gamma S_k\)-overlap relation satisfies
\[
\Pr\bigl(|X\cap Y|\ge\gamma S_k\mid X,Y\in\mathcal F_k\bigr)
=O_{\eta,\gamma}(S_k^{-1}).
\tag{4}
\]
Moreover, any cover of \(\mathcal F_k\) by internally
\(\gamma S_k\)-intersecting subfamilies requires
\[
M_k=\Omega_{\eta,\gamma}(S_k)
\tag{5}
\]
clusters.

## Proof

Let
\[
\lambda=\nu_P(\,\cdot\mid\mathcal F).
\]
Since \(\lambda(S)=\nu_P(S)/m\) for \(S\in\mathcal F\) and \(\lambda(S)=0\)
otherwise,
\[
D(\lambda\|\nu_P)=\log\frac1m.
\tag{6}
\]
Let \(\lambda_p\) be the one-coordinate marginal of \(\lambda\) at \(p\), so
\(\lambda_p=\operatorname{Bern}(a_p)\).  Since \(\nu_P=\bigotimes_p
\operatorname{Bern}(q_p)\), the finite-product entropy decomposition gives
\[
D(\lambda\|\nu_P)
=
D\!\left(\lambda\middle\|\bigotimes_{p\in P}\lambda_p\right)
+
\sum_{p\in P}
D\bigl(\lambda_p\|\operatorname{Bern}(q_p)\bigr).
\tag{7}
\]
The first term on the right is nonnegative, hence
\[
\sum_{p\in P}d(a_p\|q_p)\le\log\frac1m,
\tag{8}
\]
where
\[
d(a\|q)=a\log\frac aq+(1-a)\log\frac{1-a}{1-q}
\]
is the Bernoulli divergence, with the usual endpoint convention
\(0\log 0=0\).

For fixed \(0<q<1\), the function \(a\mapsto d(a\|q)\) has
\[
\frac{d^2}{da^2}d(a\|q)=\frac1{a(1-a)}\ge4
\]
on \(0<a<1\), and it vanishes with first derivative zero at \(a=q\).  By
continuity at \(a=0,1\),
\[
d(a\|q)\ge2(a-q)^2
\qquad(0\le a\le1).
\tag{9}
\]
Now split coordinates.  If \(a_p\le2q_p\), then
\[
a_p^2\le4q_p^2.
\tag{10}
\]
If \(a_p>2q_p\), then \(a_p\le2(a_p-q_p)\), so by (9),
\[
a_p^2\le4(a_p-q_p)^2\le2d(a_p\|q_p).
\tag{11}
\]
Combining the two cases gives, for every \(p\),
\[
a_p^2\le4q_p^2+2d(a_p\|q_p).
\tag{12}
\]
Summing (12) and using (8) proves
\[
\sum_{p\in P}a_p^2
\le
4\sum_{p\in P}q_p^2+2\log\frac1m
=
4\Sigma_2(P)+2\log\frac1m.
\]
Since \(X,Y\) are independent under \(\lambda\),
\[
\mathbb E\bigl(|X\cap Y|\mid X,Y\in\mathcal F\bigr)
=
\sum_{p\in P}\Pr(p\in X\mid X\in\mathcal F)^2
=
\sum_{p\in P}a_p^2,
\]
so (1) follows.  Markov's inequality applied to the conditional pair
\((X,Y)\) gives (2).

It remains to prove the cover lower bound.  Assign each \(A\in\mathcal F\) to
one cluster \(\mathcal C_j\) containing it, and let \(\mathcal P_j\) be the
resulting disjoint pieces.  If two conditioned samples \(X,Y\) lie in the same
piece, then \(|X\cap Y|\ge t\): this is the internal intersection condition
when \(X\ne Y\), and it is the member-size condition when \(X=Y\).  Therefore
\[
\sum_{j=1}^M\nu_P(\mathcal P_j)^2
\le
(\nu_P\times\nu_P)
\{(A,B)\in\mathcal F^2:\ |A\cap B|\ge t\}.
\tag{13}
\]
By Cauchy's inequality,
\[
\sum_{j=1}^M\nu_P(\mathcal P_j)^2
\ge
\frac1M\left(\sum_{j=1}^M\nu_P(\mathcal P_j)\right)^2
=
\frac{m^2}{M}.
\tag{14}
\]
Combining (13), (14), and (2) gives (3).

For the asymptotic statement, take
\[
t_k=\lceil\gamma S_k\rceil.
\]
If \(A\in H_{k,\theta}\), then \(|A|>\theta S_k>\gamma S_k\), so
\(|A|\ge t_k\).  If two members satisfy
\(|A\cap B|\ge\gamma S_k\), then the integer-valued intersection is also at
least \(t_k\).  Since \(\Sigma_2(P_k)\le\sum_p p^{-2}<\infty\) and
\(\nu_{P_k}(\mathcal F_k)\ge\eta\), the denominator in (3) is bounded by a
constant depending only on \(\eta\).  Equations (4) and (5) follow.

## Consequences

This proposition sharpens the mixed overlap-graph frontier left by
[[mrw-7c6a0e9f2d31]] and [[mrw-18e9c7b0a5af]].  For every fixed
\(0<\gamma<\theta\), a positive-mass high-support family has vanishing
conditional edge density in the \(\gamma S_k\)-overlap graph.  Thus a surviving
positive-mass obstruction is not only outside every \(o(\sqrt{S_k})\)
high-intersection clique cover; it is outside every \(o(S_k)\) such cover.

This does not prove the prime-biased weighted union-free theorem
[[mrw-55a8d9eddd2e]].  The proposition is not union-free-specific and does not
classify measured graphs with small edge density and tiny independent sets.  It
does, however, force any remaining positive-mass union-free or pair-link-free
obstruction into a more rigid shape: a very sparse overlap graph with no
positive-mass low-overlap independent set and no sublinear high-overlap clique
cover.
