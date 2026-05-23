---
id: mrw-4f1e9a2d6b73
type: corollary
title: Capped random pair-links are overlap-sparse
aliases: ["mrw-4f1e9a2d6b73", "Capped random pair-link sparsity"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, union-free, pair-link, overlap-graph, capped-band, random-pair, route-kill]
parents: [mrw-c7f4e0c9a821, mrw-3c39ca3d1973, mrw-55a8d9eddd2e, mrw-d0402aea6f58, mrw-b4075311abd3, mrw-7c6a0e9f2d31, mrw-18e9c7b0a5af]
refs: []
  - raw/20260520T001456Z-erdos536-sparse-overlap-graph.md
  - references/sources/20260520T001456Z-capped-pair-link-context.md
  - theory/forage/requests/20260520T001456Z-erdos536-sparse-overlap-graph-request.md
  - theory/forage/responses/20260520T001456Z-erdos536-sparse-overlap-graph-response.md
  - raw/20260520T002348Z-scout-forage-ingest.md
  - oracle/requests/20260520T001456Z-erdos536-sparse-overlap-graph-oracle-request.md
  - oracle/responses/20260520T001456Z-erdos536-sparse-overlap-graph-oracle-response.md
---

# Corollary: Capped random pair-links are overlap-sparse

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
0<\theta<1,\qquad \theta<\alpha<2\theta,
\qquad \eta>0,
\]
and put
\[
B_{k,\theta,\alpha}
=
\{A\subseteq P_k:\theta S_k<|A|\le\alpha S_k\}.
\]
Let
\[
\mathcal F_k\subseteq B_{k,\theta,\alpha},
\qquad
\nu_k(\mathcal F_k)\ge\eta,
\]
and let \(X,Y\) be independent samples from
\(\nu_k(\,\cdot\mid\mathcal F_k)\).  Then for every fixed
\[
0<\gamma<2\theta-\alpha
\]
one has
\[
\Pr\bigl(|X\cup Y|\le\alpha S_k\bigr)
\le
\Pr\bigl(|X\cap Y|\ge\gamma S_k\bigr)
=O_{\eta,\gamma}(S_k^{-1}).
\tag{1}
\]
In particular,
\[
\Pr(X\cup Y\in\mathcal F_k)=O_{\eta,\theta,\alpha}(S_k^{-1}).
\tag{2}
\]

For \(A,B\subseteq P_k\), let
\[
I(A,B)=\{C\subseteq P_k:A\triangle B\subseteq C\subseteq A\cup B\}
\]
be the pair-link interval from [[mrw-3c39ca3d1973]].  Then for every fixed
\[
0<\gamma<\frac{2\theta-\alpha}{2}
\]
one has
\[
\Pr\bigl(I(X,Y)\cap B_{k,\theta,\alpha}\ne\varnothing\bigr)
\le
\Pr\bigl(|X\cap Y|\ge\gamma S_k\bigr)
=O_{\eta,\gamma}(S_k^{-1}).
\tag{3}
\]
Consequently,
\[
\Pr\bigl(I(X,Y)\cap\mathcal F_k\ne\varnothing\bigr)
=O_{\eta,\theta,\alpha}(S_k^{-1}),
\tag{4}
\]
and the same bound holds with \(I^\circ(X,Y)=I(X,Y)\setminus\{X,Y\}\) in
place of \(I(X,Y)\).

## Proof

By [[mrw-c7f4e0c9a821]], conditioning on \(\mathcal F_k\) gives
\[
\mathbb E\bigl(|X\cap Y|\mid X,Y\in\mathcal F_k\bigr)
\le
4\sum_p\frac1{p^2}+2\log\frac1\eta
=C_\eta<\infty.
\tag{5}
\]
Therefore Markov's inequality gives, for every fixed \(\gamma>0\),
\[
\Pr\bigl(|X\cap Y|\ge\gamma S_k\mid X,Y\in\mathcal F_k\bigr)
\le
\frac{C_\eta}{\gamma S_k}.
\tag{6}
\]

If \(|X\cup Y|\le\alpha S_k\), then since
\(|X|,|Y|>\theta S_k\),
\[
|X\cap Y|
=
|X|+|Y|-|X\cup Y|
>
(2\theta-\alpha)S_k.
\tag{7}
\]
Thus, whenever \(0<\gamma<2\theta-\alpha\),
\[
\{|X\cup Y|\le\alpha S_k\}
\subseteq
\{|X\cap Y|\ge\gamma S_k\}.
\]
Combining this inclusion with (6) proves (1).  If \(X\cup Y\in\mathcal F_k\),
then \(X\cup Y\in B_{k,\theta,\alpha}\), so \(|X\cup Y|\le\alpha S_k\), and
(2) follows.

Now suppose
\[
I(X,Y)\cap B_{k,\theta,\alpha}\ne\varnothing.
\]
Choose \(C\in I(X,Y)\cap B_{k,\theta,\alpha}\).  Since \(C\in I(X,Y)\), one has
\[
X\triangle Y\subseteq C,
\]
and hence
\[
|X\triangle Y|\le |C|\le\alpha S_k.
\tag{8}
\]
Using
\[
|X\cap Y|
=
\frac{|X|+|Y|-|X\triangle Y|}{2},
\]
and again \(|X|,|Y|>\theta S_k\), (8) yields
\[
|X\cap Y|
>
\frac{2\theta-\alpha}{2}S_k.
\tag{9}
\]
Thus, whenever \(0<\gamma<(2\theta-\alpha)/2\),
\[
\{I(X,Y)\cap B_{k,\theta,\alpha}\ne\varnothing\}
\subseteq
\{|X\cap Y|\ge\gamma S_k\}.
\]
Equation (3) follows from (6).  Since \(\mathcal F_k\subseteq
B_{k,\theta,\alpha}\), (4) follows, and replacing \(I\) by the smaller interval
\(I^\circ\) can only decrease the probability.

The strict lower cutoff \(|A|>\theta S_k\) avoids endpoint rounding issues; the
displayed strict \(\gamma\)-gaps are fixed before \(k\) varies.

## Consequences

This corollary rules out one specific proof style: a positive-density
random-pair union completion or capped random-pair pair-link supersaturation
inside a fixed upper cap
\[
\theta S_k<|A|\le\alpha S_k<2\theta S_k.
\]
It does not rule out rare high-overlap pairs, deterministic or extremal
pair-link arguments, pair-link completions that leave the fixed cap, or
non-capped arguments.

Thus the measured sparse-overlap frontier after [[mrw-c7f4e0c9a821]] is sharper
but still not terminal.  A proof of the prime-biased weighted union-free theorem
[[mrw-55a8d9eddd2e]] must use the geometry of the \(O(S_k^{-1})\) high-overlap
pair set, a genuinely union-specific rooted hypergraph/container mechanism, the
fair-thinning upward-boundary route, or another invariant not captured by
random-pair capped averaging alone.
