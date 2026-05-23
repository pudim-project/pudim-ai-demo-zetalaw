---
id: mrw-b2b9ece4dd87
type: corollary
title: Mixed-overlap lower bounds force coherent-component defect
aliases: ["mrw-b2b9ece4dd87", "Mixed-overlap lower bounds force coherent-component defect"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, mixed-overlap, defect-certificate, endpoint-fiber, iterated-tower, component-normal-form, support-tail, cross-core-coherence]
parents: [mrw-bc27191b14d4]
refs: []
  - raw/20260521T100912Z-erdos-536-mixed-overlap-lower-bounds-force-coherent-componen.md
  - raw/20260521T100704Z-erdos536-mixed-overlap-defect-certificate.md
  - theory/forage/requests/20260521T100704Z-erdos536-mixed-overlap-defect-certificate-request.md
  - theory/forage/responses/20260521T100704Z-erdos536-mixed-overlap-defect-certificate-response.md
  - oracle/requests/20260521T100912Z-erdos536-mixed-overlap-defect-certificate-oracle-request.md
  - oracle/responses/20260521T100912Z-erdos536-mixed-overlap-defect-certificate-oracle-response.md
---

# Corollary: Mixed-overlap lower bounds force coherent-component defect

## Statement

Use the setting of [[mrw-bc27191b14d4]].  Thus \(K\) is a finite
parity-consistent connected component of the complete robust side-overlap
multigraph, with normalized sides
\[
\widehat S_i^a=S_i^{a+\epsilon_i\pmod2},
\qquad
\widehat D_i^a=D_i^{a+\epsilon_i\pmod2}
\qquad(i\in K,\ a\in\{0,1\}).
\]
Define the mixed normalized overlap energy
\[
\mathcal E_{\mathrm{mix}}(K)
=
\sum_{\{i,j\}\subseteq K}
\sum_{\substack{a,b\in\{0,1\}\\a\ne b}}
w(\widehat S_i^a\cap\widehat S_j^b),
\tag{1}
\]
and the total component side defect
\[
\mathcal D(K)=\sum_{i\in K}(D_i^0+D_i^1).
\tag{2}
\]
Then
\[
\mathcal E_{\mathrm{mix}}(K)
\le
(|K|-1)\mathcal D(K).
\tag{3}
\]
Consequently, any independent same-component lower bound, with \(\eta>0\),
\[
\mathcal E_{\mathrm{mix}}(K)\ge \eta
\tag{4}
\]
forces the quantitative defect lower bound
\[
\mathcal D(K)\ge\frac{\eta}{|K|-1}
\qquad(|K|\ge2).
\tag{5}
\]
Equivalently, if
\[
\mathcal D(K)<\frac{\eta}{|K|-1},
\tag{6}
\]
then at least one of the following must fail:

1. the tested side-overlap graph is the complete robust side-overlap graph on
   the corridor set;
2. the component is parity-consistent and has the normalized potential used in
   [[mrw-bc27191b14d4]];
3. the corridor near-purity defects \(D_i^0,D_i^1\) correctly measure the
   discarded side mass;
4. the claimed lower bound (4) is valid.

In the complete case \(\mathcal D(K)=0\), one has
\[
\mathcal E_{\mathrm{mix}}(K)=0.
\tag{7}
\]
Thus a complete coherent component cannot contain positive-weight mixed
normalized sharing.  In particular, whenever an exact endpoint-tower candidate
from [[mrw-b52df00c958c]] is also realized as a zero-defect complete coherent
robust component in the sense of [[mrw-bc27191b14d4]], positive mixed
normalized sharing is impossible.  Therefore positive mixed normalized
sharing in such a candidate is an escape certificate: either the candidate is
not in the exact coherent tower normal form, or positive near-purity defect
must be paid before the component-level conclusion of [[mrw-bc27191b14d4]] can
apply.

## Proof

Equation (3) is exactly the summed mixed-overlap estimate (4) of
[[mrw-bc27191b14d4]], rewritten with the abbreviations (1) and (2).  If
\(|K|\ge2\) and (4) also holds, then
\[
\eta
\le
\mathcal E_{\mathrm{mix}}(K)
\le
(|K|-1)\mathcal D(K),
\]
which gives (5).  The contrapositive is (6): if the defect is smaller than
\(\eta/(|K|-1)\) while a lower bound (4) is asserted, then the hypotheses
needed to invoke [[mrw-bc27191b14d4]] or the lower-bound assertion itself
cannot all be true.

When \(\mathcal D(K)=0\), (3) gives
\(\mathcal E_{\mathrm{mix}}(K)\le0\).  Since all weights are nonnegative,
\(\mathcal E_{\mathrm{mix}}(K)=0\), proving (7).  The final statement is just
this zero-defect conclusion combined with the exact-tower sharpness
quarantine from [[mrw-b52df00c958c]]: exact endpoint towers do not create extra
mass beyond terminal residuals, so any useful positive mixed-overlap source
must be accounted for as a failure of exact coherence or as near-purity
defect.

## Depends on

- [[mrw-bc27191b14d4]] Coherent robust components have defect-bounded normalized mixed overlaps

## Used by

## Notes

- This corollary does not prove that positive high-support mass creates the
  lower bound (4).  It records the exact accounting target for the next global
  step.
- In the underlying normalized signature picture, the two expected signature
  classes are disjoint because they are complementary ancestor-signature
  classes.  The corollary uses the already-packaged component estimate
  [[mrw-bc27191b14d4]], while the Scout advisory response rederived the same
  bound by this direct disjoint-class union-bound argument.
- The result is intentionally one-way: a future theorem must still produce
  mixed normalized overlap from positive high-support mass inside one
  completed robust component, or construct a candidate where no such lower
  bound exists.
- [[mrw-b52df00c958c]] is contextual route ancestry, not a direct proof
  dependency: exact endpoint towers must first be bridged into the zero-defect
  coherent robust-component framework before the final escape interpretation
  becomes a formal consequence.
- The corollary does not prove \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or an \(R_P(\theta)\) lift.  It turns any future
  same-component mixed-overlap source into a quantified defect obligation.
