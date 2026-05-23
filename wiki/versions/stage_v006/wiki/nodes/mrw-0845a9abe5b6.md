---
id: mrw-0845a9abe5b6
type: corollary
title: Empty-atom mass or chargeable-or-shield trichotomy
aliases: ["mrw-0845a9abe5b6", "Empty-atom mass or chargeable-or-shield trichotomy"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, endpoint-fiber, prime-biased-endpoints, high-window, overlap-energy, diagonal-energy, empty-atom, chargeable-pairs, nonchargeable-pairs, trichotomy, local-shield, lower-shadow, escaped-mass]
parents: [mrw-c79041553496, mrw-ad1f6f41665a, mrw-90be6f9a7f88, mrw-108414b9dce7, mrw-20ca89f696f2]
refs: []
  - raw/20260522T125020Z-erdos-536-empty-atom-mass-or-shield-trichotomy.md
  - raw/20260522T125020Z-erdos536-empty-atom-mass-or-shield-trichotomy.md
  - raw/20260522T125020Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T125020Z-erdos536-empty-atom-mass-or-shield-trichotomy-request.md
  - theory/forage/responses/20260522T125020Z-erdos536-empty-atom-mass-or-shield-trichotomy-response.md
  - oracle/requests/20260522T125020Z-erdos536-empty-atom-mass-or-shield-trichotomy-oracle-request.md
  - oracle/responses/20260522T125020Z-erdos536-empty-atom-mass-or-shield-trichotomy-oracle-response.md
---

# Corollary: Empty-atom mass or chargeable-or-shield trichotomy

## Statement

Let \(B\) be finite and let \(\pi_B\) be the product law on \(2^B\),
\[
\pi_B(e)=\prod_{b\in e}q_b\prod_{b\notin e}(1-q_b),
\qquad
0<q_b\le\frac12.
\]
Set
\[
P_0(B)=\prod_{b\in B}(1-q_b).
\]
Let \(T\) carry a probability law \(\nu_T\), let \(H\subseteq2^T\) satisfy
\[
\tau=\nu_T(H)>0,
\]
and let \(\mathcal E\subseteq2^B\).  For fibers
\[
\mathcal R_e\subseteq2^T\qquad(e\in\mathcal E),
\]
define
\[
M=\sum_{e\in\mathcal E}\pi_B(e)\nu_T(\mathcal R_e\cap H),
\qquad
\Lambda=\sum_{e\in\mathcal E}\pi_B(e).
\]
When \(M>0\), define
\[
\rho=\frac{M}{\Lambda\tau}.
\]
Assume the predecessor-node overlap accounting
\[
\Omega_{\mathrm{tot}}\ge\frac{M^2}{\tau},
\qquad
\Omega_{\mathrm{tot}}
=
\Omega_{\mathcal C}+\Delta+\Omega_{\mathcal N},
\]
where \(\Omega_{\mathcal C}\) is the chargeable ordered-pair energy,
\(\Delta\) is diagonal high-window energy, and \(\Omega_{\mathcal N}\) is
distinct nonchargeable ordered-pair energy.  Assume also the empty-atom
diagonal quarantine
\[
\Delta\le P_0(B)M.
\]

Fix
\[
0\le\gamma<1,
\qquad
0<\varepsilon<1-\gamma.
\]
Then at least one of the following alternatives holds.

1. Chargeable energy branch:
\[
\Omega_{\mathcal C}\ge\gamma\frac{M^2}{\tau}.
\]
If \(M>0\) and \(\gamma>0\), then there is a chargeable ordered pair
\((e,f)\) and a witness
\[
g\in\mathcal E\setminus\{e,f\},
\qquad
g\in I_B(e,f),
\]
such that
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
\gamma\rho^2.
\]

2. Empty-atom high-window mass branch:
\[
M\le\frac{P_0(B)\tau}{\varepsilon}.
\]

3. Distinct nonchargeable shield branch:
\[
\Omega_{\mathcal N}
\ge
(1-\gamma-\varepsilon)\frac{M^2}{\tau}.
\]
If \(M>0\), then there exists a distinct positive-weight nonchargeable ordered
pair \((e,f)\) such that
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
(1-\gamma-\varepsilon)\rho^2
\]
and
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]

Moreover, suppose additionally that \(T\) is finite, \(\nu_T\) is a product
law, and
\[
H=H_h(T)=\{R\subseteq T:|R|>h\}.
\]
Let
\[
\mathcal F
=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}.
\]
If \(\mathcal F\) is pair-link-free, then in the chargeable branch the witness
\(g\) can be chosen so that
\[
\nu_T(\mathcal R_g)\le1-\gamma\rho^2.
\]
More generally, every extracted chargeable pair with overlap density at least
\(\alpha\) gives the bound \(\nu_T(\mathcal R_g)\le1-\alpha\) under the same
product/high-window lower-shadow hypotheses.

## Proof

If \(M=0\), then
\[
M\le\frac{P_0(B)\tau}{\varepsilon},
\]
so the empty-atom high-window mass branch holds.  Assume \(M>0\).  Since every
endpoint atom \(\pi_B(e)\) is positive, this implies \(\Lambda>0\).

Assume the first two alternatives fail.  Then
\[
\Omega_{\mathcal C}<\gamma\frac{M^2}{\tau}
\]
and
\[
M>\frac{P_0(B)\tau}{\varepsilon}.
\]
By the empty-atom diagonal quarantine,
\[
\Delta\le P_0(B)M.
\]
The second strict inequality gives
\[
P_0(B)M<\varepsilon\frac{M^2}{\tau},
\]
so
\[
\Delta<\varepsilon\frac{M^2}{\tau}.
\]
Using the total overlap lower bound and decomposition,
\[
\frac{M^2}{\tau}
\le
\Omega_{\mathrm{tot}}
=
\Omega_{\mathcal C}+\Delta+\Omega_{\mathcal N}.
\]
Therefore
\[
\Omega_{\mathcal N}
\ge
\frac{M^2}{\tau}-\Omega_{\mathcal C}-\Delta
>
(1-\gamma-\varepsilon)\frac{M^2}{\tau}.
\]
Thus the third alternative holds.

For the chargeable pair extraction, suppose
\[
\Omega_{\mathcal C}\ge\gamma\frac{M^2}{\tau},
\qquad
M>0,
\qquad
\gamma>0.
\]
By the weighted ordered-pair definition,
\[
\Omega_{\mathcal C}
=
\sum_{(e,f)\in\mathcal C}
\pi_B(e)\pi_B(f)\nu_T(\mathcal R_e\cap\mathcal R_f\cap H),
\]
where \(\mathcal C\) is the chargeable ordered-pair class.  Its total endpoint
weight is at most
\[
\sum_{(e,f)\in\mathcal C}\pi_B(e)\pi_B(f)\le\Lambda^2.
\]
Since
\[
\frac{M^2}{\tau}
=
\rho^2\Lambda^2\tau,
\]
weighted averaging gives a chargeable ordered pair \((e,f)\) satisfying
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
\gamma\rho^2.
\]
By chargeability, choose
\[
g\in\mathcal E\setminus\{e,f\}
\qquad\text{with}\qquad
g\in I_B(e,f).
\]

For the distinct nonchargeable extraction, put
\[
c=1-\gamma-\varepsilon>0.
\]
If
\[
\Omega_{\mathcal N}\ge c\frac{M^2}{\tau},
\]
then the same weighted averaging over the distinct nonchargeable ordered-pair
class gives a pair \((e,f)\) satisfying
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
c\rho^2.
\]
Because the pair is nonchargeable,
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]

Finally, assume the additional product/high-window and pair-link-free
hypotheses.  For an extracted chargeable pair and witness \(g\), let
\[
\mathcal G=\mathcal R_e\cap\mathcal R_f.
\]
The common high-window overlap lower bound says
\[
\nu_T(\mathcal G\cap H)\ge \gamma\rho^2\tau.
\]
By the common-fiber lower-shadow exclusion behind `mrw-108414b9dce7`,
\[
\mathcal R_g\cap\downarrow\mathcal G=\varnothing.
\]
The product lower-shadow charging lemma gives
\[
\nu_T(\downarrow\mathcal G)
\ge
\frac{\nu_T(\mathcal G\cap H)}{\tau}
\ge
\gamma\rho^2.
\]
Therefore
\[
\nu_T(\mathcal R_g)
\le
1-\nu_T(\downarrow\mathcal G)
\le
1-\gamma\rho^2.
\]
The same argument gives \(\nu_T(\mathcal R_g)\le1-\alpha\) whenever the
extracted chargeable pair has overlap density at least \(\alpha\).

## Depends on

- `mrw-c79041553496`: empty-atom diagonal mass quarantine
  \(\Delta\le P_0(B)M\).
- `mrw-ad1f6f41665a`: total high-window overlap lower bound and chargeable
  pair extraction.
- `mrw-90be6f9a7f88`: diagonal/nonchargeable split and nonchargeable pair
  extraction.
- `mrw-108414b9dce7`: product/high-window lower-shadow charging for the strong
  chargeable third-fiber bound.
- `mrw-20ca89f696f2`: endpoint interval factorization behind chargeability and
  local shielding.

## Used by

- Future branch control: once \(M\) is known to exceed the empty-atom scale,
  this trichotomy leaves only chargeable overlap or distinct nonchargeable
  shielded overlap.
- Future proof attempts: chargeable overlap can be converted to a third-fiber
  exclusion under product/high-window hypotheses; distinct nonchargeable
  overlap is the remaining structural branch.
- Future obstruction accounting: if neither overlap branch can be charged,
  the high-window mass must be quarantined as \(M=O(P_0(B)\tau)\).

## Notes

- This is a branch-packaging corollary, not terminal Erdos 536 evidence.
- The trichotomy itself is an energy accounting statement.  The strong
  third-fiber bound \(\nu_T(\mathcal R_g)\le1-\gamma\rho^2\) requires the
  product/high-window lower-shadow hypotheses; pair-link-freeness alone over
  arbitrary \(H\) gives only weaker direct disjointness bounds.
- The parameter \(\gamma=0\) makes the chargeable branch vacuous because
  \(\Omega_{\mathcal C}\ge0\).  The useful form has \(\gamma>0\).
