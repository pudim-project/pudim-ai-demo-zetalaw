---
id: mrw-a261a0a4df25
type: proposition
title: Finite box certificate for the three-prime Erdos 536 weighted grid
aliases: ["mrw-a261a0a4df25", "Finite box certificate for the three-prime Erdos 536 weighted grid"]
status: proved
tags: ["proposition", "proved", "erdos", "lcm", "three-prime", "weighted-grid", "finite-prefix", "upper-bound", "patch-gate-audited"]
parents: [mrw-277fbbb4ccb9, mrw-f835f9671070, mrw-34f73025a206, mrw-c5a954e7138b]
refs: []
---

# Proposition: Finite box certificate for the three-prime Erdos 536 weighted grid

## Statement

Let \(g_{235}(t)\) denote the maximum size of a subset of
\[
\Gamma_{235}(t)=
\{(i,j,k)\in\mathbb Z_{\ge0}^3:2^i3^j5^k\le t\}
\]
with no three distinct vectors whose pairwise coordinatewise maxima are all equal.  Then
\[
\int_1^\infty g_{235}(t)t^{-2}\,dt
\le
\frac{149}{48}.
\]
Consequently, if \(f(N)\) is the largest size of a subset of \(\{1,\ldots,N\}\) with no three distinct elements having equal pairwise least common multiples, then
\[
\limsup_{N\to\infty}\frac{f(N)}N
\le
\frac{149}{180}<\frac56.
\]

The finite \([0,2]^3\) weighted independent-set certificate from the previous raw calculation is correct:
\[
\max_{S\subseteq[0,2]^3\ \mathrm{bad\text{-}free}}
\sum_{(i,j,k)\in S}2^{-i}3^{-j}5^{-k}
\le \frac{743}{300}.
\]
However, that number is not the finite-prime integral.  The proof below uses a corrected prefix-rank plus pair-tail certificate.

## Proof

First recall the pair-slice bound from [[wiki/nodes/mrw-34f73025a206|Pair-slice obstruction for three-prime Erdos 536 weighted grids]].  With
\[
P(t)=
\#\{(i,j,k)\in\Gamma_{235}(t): i=0\text{ or }j=0\},
\]
one has
\[
g_{235}(t)\le P(t)
\]
for all \(t\), and
\[
\int_1^\infty P(t)t^{-2}\,dt=\frac{25}{8}.
\]

Let \(B=[0,2]^3\).  Define
\[
R_B(t)=
\max\{|S|:S\subseteq B\cap\Gamma_{235}(t),\ S\text{ is bad-free}\},
\]
and
\[
O_B(t)=\#(\Gamma_{235}(t)\setminus B).
\]
Every bad-free subset of \(\Gamma_{235}(t)\) has at most \(R_B(t)\) points in \(B\cap\Gamma_{235}(t)\) and at most all \(O_B(t)\) outside-box points, so
\[
g_{235}(t)\le R_B(t)+O_B(t).
\]
Thus, for \(1\le t<48\),
\[
g_{235}(t)\le \min\{P(t),R_B(t)+O_B(t)\}.
\]
For \(t\ge48\), we use only \(g_{235}(t)\le P(t)\).

The exact finite prefix certificate in `calculations/20260519T021730Z-erdos536-p235-finite-prefix-certificate.md` gives the following deficits of the improved prefix bound relative to \(P(t)\) on \(1\le t<48\):
\[
P(t)-\min\{P(t),R_B(t)+O_B(t)\}=1
\]
on
\[
[15,18),\qquad [20,24),\qquad [45,48),
\]
and the deficit is \(0\) elsewhere before \(48\).  Therefore
\[
\int_1^\infty g_{235}(t)t^{-2}\,dt
\le
\frac{25}{8}
-\left(\frac1{15}-\frac1{18}\right)
-\left(\frac1{20}-\frac1{24}\right)
-\left(\frac1{45}-\frac1{48}\right).
\]
Since
\[
\frac1{15}-\frac1{18}
+\frac1{20}-\frac1{24}
+\frac1{45}-\frac1{48}
=\frac1{48},
\]
we obtain
\[
\int_1^\infty g_{235}(t)t^{-2}\,dt
\le
\frac{25}{8}-\frac1{48}
=\frac{149}{48}.
\]

Now apply [[wiki/nodes/mrw-f835f9671070|Finite-prime weighted-grid reduction for Erdos 536]] with \(P=\{2,3,5\}\).  Here
\[
\delta_{235}
=
\left(1-\frac12\right)
\left(1-\frac13\right)
\left(1-\frac15\right)
=\frac4{15}.
\]
Hence
\[
\limsup_{N\to\infty}\frac{f(N)}N
\le
\frac4{15}\cdot\frac{149}{48}
=\frac{149}{180}<\frac56.
\]

It remains only to explain why the earlier \(743/300\) certificate is not used directly.  The finite-prime reduction integrates the prefix rank \(g_{235}(t)\).  The supremum of one weighted independent set in a fixed box can be smaller than the prefix-rank integral because different prefixes may have different extremal sets.  In this box the exact prefix-rank contribution is
\[
1+\frac12+\frac13+\frac14+\frac15+\frac19+\frac1{10}
+\frac1{18}+\frac1{25}+\frac1{50}+\frac1{100}
=\frac{131}{50},
\]
not \(743/300\).  The corrected certificate above is therefore a prefix-rank certificate, not merely a weighted independent-set certificate.

## Depends on

- [[wiki/nodes/mrw-277fbbb4ccb9|Erdos equal pairwise least-common-multiple problem]]
- [[wiki/nodes/mrw-f835f9671070|Finite-prime weighted-grid reduction for Erdos 536]]
- [[wiki/nodes/mrw-34f73025a206|Pair-slice obstruction for three-prime Erdos 536 weighted grids]]
- [[wiki/nodes/mrw-c5a954e7138b|Finite-prime weighted fiber extremal problem for lcm triangles]]

## Used by

- Next #536 route: extend finite-prefix plus pair-tail savings beyond \([0,2]^3\), or replace pair-slice tails by stronger weighted covers.

## Notes

- This improves the local #536 constant from \(5/6\) to \(149/180\), but it is still a constant-density upper bound.  It does not prove Erdos #536, whose terminal target is \(f(N)=o(N)\).
- The old raw branch-and-bound value \(743/300\) is now certified as a finite weighted independent-set bound, but the density proof uses the corrected prefix-rank certificate.
