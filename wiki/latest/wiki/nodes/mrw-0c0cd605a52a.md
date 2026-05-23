---
id: mrw-0c0cd605a52a
type: corollary
title: High-support parents have uniformly tiny cover atoms
aliases: ["mrw-0c0cd605a52a", "High-support parents have uniformly tiny cover atoms"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, endpoint-fiber, terminal-product-measure, high-window, cover-probability, cover-atom, top-union-free, prime-biased, route-quarantine, residual-obstruction]
parents: [mrw-7273d9801756, mrw-9077aa1c34bc]
refs: []
  - raw/20260523T034558Z-erdos-536-high-support-cover-atom-collapse.md
  - raw/20260523T034558Z-erdos536-high-support-cover-atom-collapse.md
  - raw/20260523T034558Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T034558Z-erdos536-high-support-cover-atom-collapse-request.md
  - theory/forage/responses/20260523T034558Z-erdos536-high-support-cover-atom-collapse-response.md
  - oracle/requests/20260523T034558Z-erdos536-high-support-cover-atom-collapse-oracle-request.md
  - oracle/responses/20260523T034558Z-erdos536-high-support-cover-atom-collapse-oracle-response.md
---

# Corollary: High-support parents have uniformly tiny cover atoms

## Statement

Let \(T\) be finite and carry a product law with coordinate probabilities
\[
0<q_t\le\frac12
\qquad(t\in T).
\]
Set
\[
c_t=q_t(2-q_t).
\]
Order the coordinates so that
\[
c_{(1)}\ge c_{(2)}\ge\cdots\ge c_{(|T|)}.
\]
For \(1\le m\le |T|\), define
\[
\kappa_m(T)=\prod_{i=1}^m c_{(i)}.
\]
Then every \(U\subseteq T\) with \(|U|\ge m\) satisfies
\[
C_U:=\prod_{u\in U}q_u(2-q_u)
\le
\kappa_m(T)
\le
\left(\frac34\right)^m.
\]

Consequently, for \(h\ge0\), put
\[
m(h)=\lfloor h\rfloor+1
\]
and
\[
H_h(T)=\{U\subseteq T:|U|>h\}.
\]
If \(m(h)\le |T|\), then every \(U\in H_h(T)\) satisfies
\[
\operatorname{cov}^{\ne}_U
\le
C_U
\le
\kappa_{m(h)}(T)
\le
\left(\frac34\right)^{m(h)}.
\]
If \(m(h)>|T|\), then \(H_h(T)=\emptyset\), so the assertion is vacuous.

In the prime-biased specialization \(q_p=1/p\), suppose \(T\) contains at
least \(m\) primes and let
\[
r_1<r_2<\cdots<r_m
\]
be the \(m\) smallest primes in \(T\).  Then
\[
\kappa_m(T)
=
\prod_{i=1}^m\left(\frac2{r_i}-\frac1{r_i^2}\right)
\le
\frac{2^m}{r_1r_2\cdots r_m}
\le
\frac{2^m}{p_1p_2\cdots p_m}
\le
\frac{2^m}{(m+1)!},
\]
where \(p_i\) is the \(i\)-th prime.  Hence \(\kappa_m(T)\to0\) uniformly over
finite prime sets with at least \(m\) elements.

Therefore, along any half-biased terminal sequence with high-support cutoffs
\[
h_n\to\infty,
\]
every lower parent \(U\in H_{h_n}(T_n)\) has
\[
\operatorname{cov}^{\ne}_U\le\left(\frac34\right)^{\lfloor h_n\rfloor+1}\to0.
\]
In particular, in growing positive-threshold high-support windows, a single
high-support lower parent cannot supply a fixed positive upper-fiber loss
through the cover-probability cap of `mrw-9077aa1c34bc` alone.  Its possible
loss is at most
\[
1-\sqrt{1-\kappa_{m(h)}(T)},
\]
which tends to \(0\) whenever \(m(h)\to\infty\) and \(\kappa_{m(h)}(T)\to0\).

## Proof

Because \(0<q_t\le1/2\),
\[
0<c_t=q_t(2-q_t)\le\frac12\cdot\frac32=\frac34<1.
\]
Fix \(U\subseteq T\) with \(|U|\ge m\), and choose any \(m\)-element subset
\[
U_m\subseteq U.
\]
Since all \(c_t<1\),
\[
\prod_{u\in U}c_u
=
\left(\prod_{u\in U_m}c_u\right)
\left(\prod_{u\in U\setminus U_m}c_u\right)
\le
\prod_{u\in U_m}c_u.
\]
The product over any \(m\)-element subset is at most the product of the
\(m\) largest coordinate values.  Hence
\[
C_U=\prod_{u\in U}c_u\le\prod_{i=1}^m c_{(i)}=\kappa_m(T).
\]
The bound
\[
\kappa_m(T)\le(3/4)^m
\]
follows from \(c_{(i)}\le3/4\) for every \(i\).

For real \(h\ge0\), the integer condition
\[
|U|>h
\]
is equivalent to
\[
|U|\ge\lfloor h\rfloor+1=m(h).
\]
If \(m(h)>|T|\), no such \(U\) exists.  Otherwise the previous paragraph gives
\[
C_U\le\kappa_{m(h)}(T).
\]
Since `mrw-7273d9801756` gives
\[
\operatorname{cov}^{\ne}_U\le C_U
\]
for every nonempty \(U\), and \(h\ge0\) makes every \(U\in H_h(T)\) nonempty,
the high-window estimate follows.

In the prime-biased specialization,
\[
c_p=\frac1p\left(2-\frac1p\right)=\frac2p-\frac1{p^2}.
\]
The function
\[
f(x)=\frac2x-\frac1{x^2}
\]
has derivative
\[
f'(x)=-\frac2{x^2}+\frac2{x^3}
=
\frac{2(1-x)}{x^3}<0
\qquad(x>1).
\]
Thus \(c_p\) is strictly decreasing over primes \(p\ge2\), so the \(m\)
largest \(c_p\)'s among \(T\) come from the \(m\) smallest primes
\(r_1,\ldots,r_m\) in \(T\).  Therefore
\[
\kappa_m(T)=
\prod_{i=1}^m\left(\frac2{r_i}-\frac1{r_i^2}\right)
\le
\prod_{i=1}^m\frac2{r_i}
=
\frac{2^m}{r_1\cdots r_m}.
\]
Since \(r_i\ge p_i\), where \(p_i\) is the \(i\)-th prime, and \(p_i\ge i+1\),
\[
r_1\cdots r_m\ge p_1\cdots p_m\ge2\cdot3\cdots(m+1)=(m+1)!.
\]
This proves the displayed factorial bound and its convergence to \(0\).

Finally, the cover cap from `mrw-9077aa1c34bc` has the form
\[
\mu_T(\mathcal W)\le\sqrt{1-\operatorname{cov}^{\ne}_U}.
\]
If \(U\in H_h(T)\), then
\[
\operatorname{cov}^{\ne}_U\le\kappa_{m(h)}(T),
\]
so the loss forced by this one lower parent is no larger than
\[
1-\sqrt{1-\kappa_{m(h)}(T)}.
\]
When \(\kappa_{m(h)}(T)\to0\), this loss tends to \(0\).

## Depends on

- `mrw-7273d9801756`: small distinct-cover probability is controlled by the
  terminal cover atom \(C_U\), and \(\operatorname{cov}^{\ne}_U\le C_U\).
- `mrw-9077aa1c34bc`: top-union-free sections have the cover-probability mass
  cap.

## Used by

- Future route selection: individual high-support lower parents in growing
  windows cannot provide a fixed positive upper-fiber loss through the
  cover-probability cap alone.
- Future aggregation attempts: any successful use of `mrw-9077aa1c34bc` in
  positive high-support regimes must aggregate many lower parents, use
  cross-fiber exclusions, or classify residual/product structure beyond
  individual cover probability.

## Notes

- This is a route-quarantine corollary, not terminal Erdos 536 evidence.
- The result does not rule out aggregation over many lower parents, weighted
  charging, endpoint interval triples, terminal cross-fiber exclusions, or
  residual/product classification.
- The \(h\ge0\) assumption keeps the empty-block boundary out of the statement.
  If \(h<0\), then \(\emptyset\in H_h(T)\) and
  \(\operatorname{cov}^{\ne}_\emptyset=0\) is the vacuous boundary case already
  separated in `mrw-7273d9801756`.
- Oracle accepted the proposition with the explicit \(m>|T|\) vacuity clause
  and suggested the general \((3/4)^m\) strengthening.  Scout returned only a
  scaffold response and was ingested raw-only.
