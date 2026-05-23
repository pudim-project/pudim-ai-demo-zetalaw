---
id: mrw-cdf34678a1e1
type: counterexample
title: Endpoint pair-link-free families need not obey two-layer chain envelopes
aliases: ["mrw-cdf34678a1e1", "Endpoint pair-link-free families need not obey two-layer chain envelopes"]
status: proved
tags: [counterexample, proved, erdos-536, squarefree-support, pair-link, endpoint-residual, homogeneous-product, chain-envelope, lubell-obstruction, theta-zero-boundary, route-kill, endpoint-profile]
parents: [mrw-baa182012831, mrw-3c39ca3d1973, mrw-20ca89f696f2]
refs: []
  - raw/20260522T064952Z-erdos-536-homogeneous-endpoint-chain-envelope-obstruction.md
  - raw/20260522T064952Z-erdos536-homogeneous-endpoint-chain-envelope.md
  - raw/20260522T070340Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T064952Z-erdos536-homogeneous-endpoint-chain-envelope-request.md
  - theory/forage/responses/20260522T064952Z-erdos536-homogeneous-endpoint-chain-envelope-response.md
  - oracle/requests/20260522T064952Z-erdos536-homogeneous-endpoint-chain-envelope-oracle-request.md
  - oracle/responses/20260522T064952Z-erdos536-homogeneous-endpoint-chain-envelope-oracle-response.md
---

# Counterexample: Endpoint pair-link-free families need not obey two-layer chain envelopes

## Statement

The ordinary endpoint pair-link-free condition does not imply the
2-Sperner condition.  Consequently, the endpoint residual profile from
`mrw-baa182012831` cannot be bounded in general by the Lubell two-layer chain
envelope.

More concretely, let \(B=\{1,2,3\}\), let the endpoint law be homogeneous with
coordinate probability \(q=1/10\), and let \(a=-1\).  Define
\[
\mathcal A
=
\{\varnothing,\{1\},\{2\},\{3\},B\}.
\]
Then \(\mathcal A\) is ordinary pair-link-free, but
\[
\varnothing\subsetneq\{1\}\subsetneq B,
\]
so it is not 2-Sperner.  Moreover,
\[
\nu_{3,1/10}(\mathcal A)=\frac{973}{1000}.
\]
The homogeneous rank probabilities are
\[
w_0=\frac{729}{1000},\qquad
w_1=\frac{243}{1000},\qquad
w_2=\frac{27}{1000},\qquad
w_3=\frac{1}{1000}.
\]
Thus the sum of the two largest eligible rank masses is
\[
w_0+w_1=\frac{972}{1000},
\]
while
\[
\nu_{3,1/10}(\mathcal A)
>
w_0+w_1.
\]
Therefore the proposed bound
\[
\mathfrak P_{n,q}(a)
\le
\text{sum of the two largest eligible homogeneous rank masses}
\]
is false without an additional 2-Sperner or antichain-like hypothesis.

## Proof

The pair-link interval convention is
\[
I(A,B)=\{C\subseteq B:\ A\triangle B\subseteq C\subseteq A\cup B\}.
\]
Check pair-link-freeness of \(\mathcal A\).

If one endpoint is \(\varnothing\), then
\[
I(\varnothing,X)=\{X\}.
\]
So no third distinct member of \(\mathcal A\) lies in such an interval.

If \(i\ne j\), then
\[
I(\{i\},\{j\})=\{\{i,j\}\},
\]
and \(\{i,j\}\notin\mathcal A\).

If \(i\in B\), then
\[
I(\{i\},B)=\{B\setminus\{i\},B\},
\]
and \(B\setminus\{i\}\notin\mathcal A\), while \(B\) is one of the two
interval endpoints.  These cases exhaust all distinct pairs in
\(\mathcal A\), so no pairwise distinct triple
\[
A_1,A_2,A_3\in\mathcal A,\qquad A_3\in I(A_1,A_2)
\]
exists.  Hence \(\mathcal A\) is ordinary pair-link-free.

However, \(\mathcal A\) contains the strict inclusion chain
\[
\varnothing\subsetneq\{1\}\subsetneq B.
\]
The middle set \(\{1\}\) is not in \(I(\varnothing,B)\), because
\[
I(\varnothing,B)=\{B\}.
\]
Thus ordinary pair-link-freeness does not imply 2-Sperner.

Finally, under the homogeneous \(q=1/10\) law,
\[
\nu_{3,1/10}(\mathcal A)
=
\left(\frac9{10}\right)^3
+3\left(\frac1{10}\right)\left(\frac9{10}\right)^2
+\left(\frac1{10}\right)^3
=
\frac{973}{1000}.
\]
Since \(a=-1\), all ranks are eligible.  The two largest rank probabilities
are \(w_0=729/1000\) and \(w_1=243/1000\), whose sum is \(972/1000\).  This
gives the advertised violation.

## Depends on

- `mrw-3c39ca3d1973`: pair-link interval convention
  \(I(A,B)=\{C:A\triangle B\subseteq C\subseteq A\cup B\}\).
- `mrw-baa182012831`: pointwise endpoint residual reduction, whose endpoint
  residual profile cannot be bounded by this false chain envelope.
- `mrw-20ca89f696f2`: endpoint-terminal interval factorization context.

## Used by

- Future endpoint residual profile work should avoid Lubell/2-Sperner
  envelopes unless an additional antichain-like or 2-Sperner hypothesis is
  explicitly proved.

## Notes

- This is a boundary-threshold obstruction: the displayed numerical violation
  uses \(a=-1\), so the empty endpoint pattern is eligible.  It kills the
  proposed universal homogeneous two-layer envelope, but it does not by itself
  settle positive-\(\theta\) endpoint residual profiles.
- The corrected Lubell statement remains true for genuinely 2-Sperner
  families, but ordinary endpoint pair-link-free families need not be
  2-Sperner under the squarefree cosunflower interval convention.
- The next target should use the actual symmetric-difference interval
  structure, or impose and justify a stronger interval-shield/antichain
  decomposition before applying chain-counting tools.
