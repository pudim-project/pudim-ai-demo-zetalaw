---
id: mrw-7f0eb8d1648c
type: corollary
title: Pointwise mixed incidence produces coherent-component defect
aliases: ["mrw-7f0eb8d1648c", "Pointwise mixed incidence produces coherent-component defect"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, mixed-overlap, pointwise-incidence, defect-certificate, component-normal-form, endpoint-fiber, cross-core-coherence]
parents: [mrw-b2b9ece4dd87, mrw-bc27191b14d4]
refs: []
  - raw/20260521T104936Z-erdos-536-pointwise-mixed-incidence-production-criterion.md
  - raw/20260521T104705Z-erdos536-pointwise-mixed-incidence-production.md
  - theory/forage/requests/20260521T104705Z-erdos536-pointwise-mixed-incidence-production-request.md
  - theory/forage/responses/20260521T104705Z-erdos536-pointwise-mixed-incidence-production-response.md
  - oracle/requests/20260521T104936Z-erdos536-pointwise-mixed-incidence-oracle-request.md
  - oracle/responses/20260521T104936Z-erdos536-pointwise-mixed-incidence-oracle-response.md
---

# Corollary: Pointwise mixed incidence produces coherent-component defect

## Statement

Use the setting of [[mrw-b2b9ece4dd87]] and [[mrw-bc27191b14d4]].  Thus
\(K\) is a finite parity-consistent coherent robust component, with
normalized sides
\[
\widehat S_i^a=S_i^{a+\epsilon_i\pmod2}
\qquad(i\in K,\ a\in\{0,1\}),
\]
and, after fixing any ordering of the finite set \(K\), mixed normalized
overlap energy
\[
\mathcal E_{\mathrm{mix}}(K)
=
\sum_{i<j}
\left[
w(\widehat S_i^0\cap\widehat S_j^1)
+
w(\widehat S_i^1\cap\widehat S_j^0)
\right],
\tag{1}
\]
and total component side defect
\[
\mathcal D(K)=\sum_{i\in K}(D_i^0+D_i^1).
\tag{2}
\]
Assume the usual corridor side disjointness
\[
S_i^0\cap S_i^1=\varnothing
\qquad(i\in K),
\tag{3}
\]
which is part of the lower-corridor interpretation \(S_i^0=U_i\),
\(S_i^1=W_i\).

Define the two pointwise normalized incidence supports
\[
C_a(K)=\bigcup_{i\in K}\widehat S_i^a
\qquad(a\in\{0,1\})
\tag{4}
\]
and the pointwise mixed-incidence mass
\[
\Xi(K)=w(C_0(K)\cap C_1(K)).
\tag{5}
\]
Then
\[
\Xi(K)\le \mathcal E_{\mathrm{mix}}(K)
\le (|K|-1)\mathcal D(K).
\tag{6}
\]
Consequently, any positive pointwise mixed-incidence lower bound
\[
\Xi(K)\ge \eta>0
\tag{7}
\]
forces
\[
\mathcal D(K)\ge\frac{\eta}{|K|-1}
\qquad(|K|\ge2).
\tag{8}
\]

In particular, if \(\mathcal D(K)=0\), then
\[
w(C_0(K)\cap C_1(K))=0.
\tag{9}
\]
Thus a zero-defect coherent component has a genuine two-class point support
modulo \(w\)-null sets: all normalized \(0\)-sides lie in \(C_0(K)\), all
normalized \(1\)-sides lie in \(C_1(K)\), and these two supports are disjoint
up to zero weight.  Equivalently, any positive-weight point used by both
normalized classes is a local certificate that the component must pay
near-purity defect, unless one of the coherent robust-component hypotheses
fails.

## Proof

The second inequality in (6) is exactly [[mrw-b2b9ece4dd87]].  It remains to
prove the pointwise production inequality
\[
\Xi(K)\le \mathcal E_{\mathrm{mix}}(K).
\tag{10}
\]

Fix a point \(x\in C_0(K)\cap C_1(K)\).  By definition of \(C_0(K)\) and
\(C_1(K)\), there are \(i,j\in K\) such that
\[
x\in\widehat S_i^0
\qquad\text{and}\qquad
x\in\widehat S_j^1.
\]
If \(i=j\), then
\[
x\in \widehat S_i^0\cap\widehat S_i^1,
\]
which contradicts the side disjointness (3), since normalization only swaps
the two sides of the same corridor.  Hence \(i\ne j\).  Therefore \(x\) lies
in one of the two mixed intersections counted by (1) for the ordered pair
\(\{i,j\}\): if \(i<j\), it lies in
\(\widehat S_i^0\cap\widehat S_j^1\), while if \(j<i\), it lies in
\(\widehat S_j^1\cap\widehat S_i^0\).

Thus the indicator of \(C_0(K)\cap C_1(K)\) is pointwise bounded by the sum of
the indicators of all mixed normalized intersections appearing in (1).
Summing with the nonnegative weights \(w\) gives (10).  Combining (10) with
[[mrw-b2b9ece4dd87]] proves (6).  If (7) holds and \(|K|\ge2\), then
\[
\eta\le \Xi(K)\le (|K|-1)\mathcal D(K),
\]
which is (8).  Finally, if \(\mathcal D(K)=0\), then (6) gives
\(\Xi(K)\le0\), and nonnegativity gives (9).  The two-class point-support
interpretation follows directly from the definitions (4) and (5).

## Depends on

- [[mrw-b2b9ece4dd87]] Mixed-overlap lower bounds force coherent-component defect
- [[mrw-bc27191b14d4]] Coherent robust components have defect-bounded normalized mixed overlaps

## Used by

## Notes

- This is the promised same-component production criterion in its local
  pointwise form.  The remaining global problem is to prove that positive
  high-support pair-link-free mass produces \(\Xi(K)>0\) in a completed
  robust component, or to show that the candidate stays inside the two-class
  point-support alternative.
- The first inequality \(\Xi(K)\le\mathcal E_{\mathrm{mix}}(K)\) is purely
  pointwise and does not use robustness or parity consistency.  Robustness and
  parity consistency enter only through the defect budget imported from
  [[mrw-b2b9ece4dd87]].
- The disjointness hypothesis can be weakened to
  \(w(S_i^0\cap S_i^1)=0\) for every corridor \(i\), with the same proof
  interpreted modulo null sets.  The stated form records the ordinary
  lower-corridor side disjointness used in the current Erdos 536 route.
- If \(\Xi(K)=0\), this node gives the exact local escape alternative: the
  component is two-class at the point-support level.  This is the local
  signature-potential shape that endpoint-tower candidates must exploit.
- This corollary does not prove \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or an \(R_P(\theta)\) lift.  It identifies the concrete
  pointwise overlap quantity that the next global high-support argument must
  force.
