---
id: mrw-90be6f9a7f88
type: corollary
title: Avoidance energy splits into diagonal and distinct nonchargeable overlap
aliases: ["mrw-90be6f9a7f88", "Avoidance energy splits into diagonal and distinct nonchargeable overlap"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, terminal-product-measure, high-window, overlap-energy, diagonal-energy, nonchargeable-pairs, cauchy, fubini, shielded-concentration, interval-shield, escaped-mass]
parents: [mrw-ad1f6f41665a, mrw-108414b9dce7, mrw-baa182012831, mrw-20ca89f696f2]
refs: []
  - raw/20260522T101007Z-erdos-536-diagonal-nonchargeable-energy-split.md
  - raw/20260522T101007Z-erdos536-diagonal-nonchargeable-energy-split.md
  - raw/20260522T101007Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T101007Z-erdos536-diagonal-nonchargeable-energy-split-request.md
  - theory/forage/responses/20260522T101007Z-erdos536-diagonal-nonchargeable-energy-split-response.md
  - oracle/requests/20260522T101007Z-erdos536-diagonal-nonchargeable-energy-split-oracle-request.md
  - oracle/responses/20260522T101007Z-erdos536-diagonal-nonchargeable-energy-split-oracle-response.md
---

# Corollary: Avoidance energy splits into diagonal and distinct nonchargeable overlap

## Statement

Let \(T\) carry a product probability law \(\nu_T\), let
\[
H=H_h(T)=\{R\subseteq T:|R|>h\},
\qquad
\tau=\nu_T(H)>0.
\]
Let \(\mathcal E\subseteq2^B\) be a finite endpoint-pattern set, let
\(\lambda_e\ge0\), and set
\[
\Lambda=\sum_{e\in\mathcal E}\lambda_e>0.
\]
For terminal fibers \(\mathcal R_e\subseteq2^T\), define
\[
M=\sum_{e\in\mathcal E}\lambda_e\,\nu_T(\mathcal R_e\cap H),
\qquad
\rho=\frac{M}{\Lambda\tau}.
\]

As in `mrw-ad1f6f41665a`, call an ordered pair
\((e,f)\in\mathcal E^2\) chargeable if \(e\ne f\) and there exists
\[
g\in\mathcal E\setminus\{e,f\}
\qquad\text{with}\qquad
g\in I_B(e,f).
\]
Let \(\mathcal C\) be the chargeable ordered-pair set and define
\[
\Omega_{\mathcal C}
=
\sum_{(e,f)\in\mathcal C}
\lambda_e\lambda_f\,\nu_T(\mathcal R_e\cap\mathcal R_f\cap H).
\]

Define the diagonal high-window overlap energy
\[
\Delta
=
\sum_{e\in\mathcal E}
\lambda_e^2\,\nu_T(\mathcal R_e\cap H),
\]
and the distinct nonchargeable ordered-pair overlap energy
\[
\Omega_{\mathcal N}
=
\sum_{\substack{e,f\in\mathcal E\\ e\ne f,\ (e,f)\notin\mathcal C}}
\lambda_e\lambda_f\,\nu_T(\mathcal R_e\cap\mathcal R_f\cap H).
\]
If
\[
\Omega_{\mathcal U}
=
\sum_{(e,f)\notin\mathcal C}
\lambda_e\lambda_f\,\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)
\]
is the avoidance energy from `mrw-ad1f6f41665a`, then
\[
\Omega_{\mathcal U}=\Delta+\Omega_{\mathcal N},
\]
and therefore
\[
\Omega_{\mathcal C}+\Delta+\Omega_{\mathcal N}
\ge
\frac{M^2}{\tau}.
\]

Consequently, if \(0\le\gamma,\delta\le1\) and
\[
\Omega_{\mathcal C}\le \gamma\frac{M^2}{\tau},
\qquad
\Delta\le \delta\frac{M^2}{\tau},
\]
then
\[
\Omega_{\mathcal N}
\ge
(1-\gamma-\delta)\frac{M^2}{\tau}.
\]

If \(\Omega_{\mathcal N}>0\), then there exists a distinct nonchargeable
ordered pair \((e,f)\) such that
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
\frac{\Omega_{\mathcal N}}{\Lambda^2\tau}.
\]
In particular, if \(M>0\), \(\gamma+\delta<1\), and the two smallness bounds
above hold, then some distinct nonchargeable ordered pair \((e,f)\) satisfies
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
(1-\gamma-\delta)\rho^2.
\]
For this pair,
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]
Thus the avoidance branch is either diagonal-heavy or contains a
high-window common-overlap pair whose endpoint interval is locally shielded
inside \(\mathcal E\) up to the two selected endpoints.

## Proof

Set
\[
W(R)=\sum_{e\in\mathcal E}\lambda_e\,1_{\mathcal R_e}(R).
\]
Then
\[
M=\int_H W(R)\,d\nu_T(R),
\]
and
\[
\int_H W(R)^2\,d\nu_T(R)
=
\sum_{e,f\in\mathcal E}
\lambda_e\lambda_f\,\nu_T(\mathcal R_e\cap\mathcal R_f\cap H).
\]
By Cauchy's inequality on \(H\),
\[
\int_H W^2\,d\nu_T
\ge
\frac{1}{\tau}\left(\int_H W\,d\nu_T\right)^2
=
\frac{M^2}{\tau}.
\]

The ordered pairs \(\mathcal E^2\) split disjointly into chargeable ordered
pairs, diagonal ordered pairs, and distinct ordered pairs not in
\(\mathcal C\).  Chargeability requires \(e\ne f\), so the diagonal
contribution is exactly
\[
\sum_{e\in\mathcal E}
\lambda_e^2\,\nu_T(\mathcal R_e\cap\mathcal R_e\cap H)
=
\Delta.
\]
The remaining distinct nonchargeable contribution is \(\Omega_{\mathcal N}\).
Thus
\[
\Omega_{\mathcal C}+\Delta+\Omega_{\mathcal N}
=
\sum_{e,f\in\mathcal E}
\lambda_e\lambda_f\,\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)
\ge
\frac{M^2}{\tau}.
\]
Equivalently, the unchargeable energy from `mrw-ad1f6f41665a` satisfies
\[
\Omega_{\mathcal U}=\Delta+\Omega_{\mathcal N}.
\]

If the chargeable and diagonal energies satisfy the two displayed upper bounds,
then
\[
\Omega_{\mathcal N}
\ge
\frac{M^2}{\tau}-\Omega_{\mathcal C}-\Delta
\ge
(1-\gamma-\delta)\frac{M^2}{\tau}.
\]

Now suppose \(\Omega_{\mathcal N}>0\).  Put
\[
W_{\mathcal N}
=
\sum_{\substack{e,f\in\mathcal E\\ e\ne f,\ (e,f)\notin\mathcal C}}
\lambda_e\lambda_f .
\]
Then \(W_{\mathcal N}>0\), and by weighted averaging some distinct
nonchargeable ordered pair \((e,f)\) satisfies
\[
\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)
\ge
\frac{\Omega_{\mathcal N}}{W_{\mathcal N}}
\ge
\frac{\Omega_{\mathcal N}}{\Lambda^2},
\]
because \(W_{\mathcal N}\le\Lambda^2\).  Dividing by \(\tau\) gives
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
\frac{\Omega_{\mathcal N}}{\Lambda^2\tau}.
\]

If \(M>0\), \(\gamma+\delta<1\), and the two smallness bounds hold, then the
lower bound on \(\Omega_{\mathcal N}\) is strictly positive, so the averaging
step applies.  Substitution gives
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
(1-\gamma-\delta)\frac{M^2}{\Lambda^2\tau^2}
=
(1-\gamma-\delta)\rho^2.
\]

Finally, because the selected pair is distinct and not chargeable, there is no
\[
g\in\mathcal E\setminus\{e,f\}
\]
with \(g\in I_B(e,f)\).  Equivalently,
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]

## Depends on

- `mrw-ad1f6f41665a`: chargeable endpoint-pair energy alternative and the
  high-window overlap-energy lower bound.
- `mrw-108414b9dce7`: product lower shadows charge common high-window terminal
  mass; this is the next charging tool once a genuine chargeable triple is
  found.
- `mrw-baa182012831`: pointwise endpoint conditioning, which motivates
  separating diagonal energy from distinct nonchargeable overlap.
- `mrw-20ca89f696f2`: endpoint-terminal interval factorization underlying the
  chargeability definition.

## Used by

- Future avoidance-branch decompositions: if chargeable and diagonal overlap
  are both small, the remaining high-window overlap is carried by distinct
  pair-level interval-shielded endpoint pairs.
- Future diagonal-control attempts: the term \(\Delta\) isolates the effective
  endpoint-count or Herfindahl obstruction.
- Future nonchargeable-pair classification attempts: the conclusion
  \(\mathcal E\cap I_B(e,f)\subseteq\{e,f\}\) identifies the local shielded
  relation that must be upgraded to a structural endpoint-support theorem.

## Notes

- This is an accounting and averaging corollary, not terminal Erdos 536
  evidence.  It does not prove that the diagonal energy is small, and it does
  not classify endpoint supports whose distinct overlap is nonchargeable.
- The final shielding statement is only pair-level.  It should not be read as
  saying that \(\mathcal E\) is globally interval-shielded.
- The positivity assumptions in the last branch are essential: \(M>0\) and
  \(\gamma+\delta<1\) ensure \(\Omega_{\mathcal N}>0\), so the selected
  distinct pair actually exists.
