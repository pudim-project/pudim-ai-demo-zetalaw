---
id: mrw-724d68db9b8c
type: proposition
title: Diagonal high-window energy is controlled by endpoint Herfindahl and max atom
aliases: ["mrw-724d68db9b8c", "Diagonal high-window energy is controlled by endpoint Herfindahl and max atom"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, endpoint-fiber, high-window, overlap-energy, diagonal-energy, herfindahl, max-atom, endpoint-concentration, nonchargeable-pairs, cauchy, fubini, escaped-mass]
parents: [mrw-90be6f9a7f88, mrw-ad1f6f41665a, mrw-20ca89f696f2]
refs: []
  - raw/20260522T105008Z-erdos-536-diagonal-herfindahl-control.md
  - raw/20260522T105008Z-erdos536-diagonal-herfindahl-control.md
  - raw/20260522T105008Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T105008Z-erdos536-diagonal-herfindahl-control-request.md
  - theory/forage/responses/20260522T105008Z-erdos536-diagonal-herfindahl-control-response.md
  - oracle/requests/20260522T105008Z-erdos536-diagonal-herfindahl-control-oracle-request.md
  - oracle/responses/20260522T105008Z-erdos536-diagonal-herfindahl-control-oracle-response.md
---

# Proposition: Diagonal high-window energy is controlled by endpoint Herfindahl and max atom

## Statement

Let \(T\) carry a probability law \(\nu_T\), let
\[
H=H_h(T)=\{R\subseteq T:|R|>h\},
\qquad
\tau=\nu_T(H)>0.
\]
Let \(\mathcal E\subseteq2^B\) be finite, let \(\lambda_e\ge0\), and set
\[
\Lambda=\sum_{e\in\mathcal E}\lambda_e>0.
\]
For terminal fibers \(\mathcal R_e\subseteq2^T\), define
\[
M=\sum_{e\in\mathcal E}\lambda_e\,\nu_T(\mathcal R_e\cap H),
\qquad
\rho=\frac{M}{\Lambda\tau},
\]
and assume \(M>0\).  Put
\[
w_e=\frac{\lambda_e}{\Lambda},
\qquad
a_e=\frac{\nu_T(\mathcal R_e\cap H)}{\tau}.
\]
Then
\[
0\le a_e\le1,\qquad
\sum_e w_e=1,\qquad
\rho=\sum_e w_ea_e>0.
\]

Let
\[
\Delta
=
\sum_{e\in\mathcal E}\lambda_e^2\,\nu_T(\mathcal R_e\cap H)
\]
be the diagonal high-window energy from `mrw-90be6f9a7f88`.  Define
\[
H_2(w)=\sum_e w_e^2,
\qquad
\eta=\max_e w_e.
\]
Then
\[
\frac{\Delta}{M^2/\tau}
=
\frac{\sum_e w_e^2a_e}{\rho^2},
\]
and therefore
\[
\frac{\Delta}{M^2/\tau}
\le
\frac{H_2(w)}{\rho^2},
\qquad
\frac{\Delta}{M^2/\tau}
\le
\frac{\eta}{\rho}.
\]
Equivalently, with
\[
\kappa
=
\min\left\{
\frac{H_2(w)}{\rho^2},
\frac{\eta}{\rho}
\right\},
\]
one has
\[
\Delta\le\kappa\,\frac{M^2}{\tau}.
\]

Assume further that the endpoint-overlap accounting has the total-energy lower
bound and decomposition
\[
\Omega_{\mathrm{tot}}\ge\frac{M^2}{\tau},
\qquad
\Omega_{\mathrm{tot}}
=
\Omega_{\mathcal C}+\Delta+\Omega_{\mathcal N},
\]
where \(\Omega_{\mathcal C}\) is chargeable ordered-pair energy and
\(\Omega_{\mathcal N}\) is distinct nonchargeable ordered-pair energy.  If
\[
\Omega_{\mathcal C}\le\gamma\frac{M^2}{\tau}
\]
and \(\gamma+\kappa<1\), then
\[
\Omega_{\mathcal N}
\ge
(1-\gamma-\kappa)\frac{M^2}{\tau}.
\]
Consequently, some distinct ordered pair \((e,f)\) with \(w_ew_f>0\) is
nonchargeable and satisfies
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
(1-\gamma-\kappa)\rho^2,
\]
and hence
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]

Conversely, if for some \(\delta>0\),
\[
\Delta\ge\delta\frac{M^2}{\tau},
\]
then
\[
H_2(w)\ge\delta\rho^2,
\qquad
\eta\ge\delta\rho.
\]
Thus a diagonal-heavy branch at positive high-window density forces endpoint
weight concentration.

## Proof

Since
\[
\nu_T(\mathcal R_e\cap H)=\tau a_e
\qquad\text{and}\qquad
\lambda_e=\Lambda w_e,
\]
we have
\[
\Delta
=
\sum_e \lambda_e^2\nu_T(\mathcal R_e\cap H)
=
\tau\Lambda^2\sum_e w_e^2a_e.
\]
Also
\[
M
=
\sum_e\lambda_e\nu_T(\mathcal R_e\cap H)
=
\Lambda\tau\sum_e w_ea_e
=
\Lambda\tau\rho.
\]
Therefore
\[
\frac{M^2}{\tau}
=
\tau\Lambda^2\rho^2,
\]
and hence
\[
\frac{\Delta}{M^2/\tau}
=
\frac{\sum_e w_e^2a_e}{\rho^2}.
\]

Because \(0\le a_e\le1\),
\[
\sum_e w_e^2a_e
\le
\sum_e w_e^2
=
H_2(w),
\]
so
\[
\frac{\Delta}{M^2/\tau}
\le
\frac{H_2(w)}{\rho^2}.
\]
Because \(w_e\le\eta\),
\[
w_e^2a_e\le \eta w_ea_e.
\]
Summing gives
\[
\sum_e w_e^2a_e
\le
\eta\sum_e w_ea_e
=
\eta\rho,
\]
so
\[
\frac{\Delta}{M^2/\tau}
\le
\frac{\eta}{\rho}.
\]
The \(\kappa\)-bound follows by taking the smaller of these two estimates.

For the combined branch, use the total-energy lower bound and decomposition:
\[
\frac{M^2}{\tau}
\le
\Omega_{\mathrm{tot}}
=
\Omega_{\mathcal C}+\Delta+\Omega_{\mathcal N}.
\]
The hypotheses give
\[
\Omega_{\mathcal C}
\le
\gamma\frac{M^2}{\tau},
\qquad
\Delta
\le
\kappa\frac{M^2}{\tau}.
\]
Therefore
\[
\Omega_{\mathcal N}
\ge
(1-\gamma-\kappa)\frac{M^2}{\tau}.
\]

For each distinct nonchargeable ordered pair, put
\[
b_{ef}
=
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}.
\]
Let \(\mathcal N\) be the distinct nonchargeable ordered-pair set.  Then
\[
\Omega_{\mathcal N}
=
\tau\Lambda^2
\sum_{(e,f)\in\mathcal N}w_ew_f b_{ef}.
\]
Since
\[
\frac{M^2}{\tau}
=
\tau\Lambda^2\rho^2,
\]
we get
\[
\sum_{(e,f)\in\mathcal N}w_ew_f b_{ef}
\ge
(1-\gamma-\kappa)\rho^2.
\]
Also
\[
\sum_{(e,f)\in\mathcal N}w_ew_f\le1.
\]
Hence some distinct nonchargeable ordered pair \((e,f)\) with \(w_ew_f>0\)
satisfies
\[
b_{ef}\ge(1-\gamma-\kappa)\rho^2.
\]
By nonchargeability,
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]

Finally, if
\[
\Delta\ge\delta\frac{M^2}{\tau},
\]
then the two upper bounds just proved imply
\[
\delta
\le
\frac{\Delta}{M^2/\tau}
\le
\frac{H_2(w)}{\rho^2}
\]
and
\[
\delta
\le
\frac{\Delta}{M^2/\tau}
\le
\frac{\eta}{\rho}.
\]
Thus
\[
H_2(w)\ge\delta\rho^2,
\qquad
\eta\ge\delta\rho.
\]

## Depends on

- `mrw-90be6f9a7f88`: decomposes avoidance energy into diagonal and distinct
  nonchargeable overlap, and gives the selected nonchargeable pair after
  chargeable and diagonal bounds.
- `mrw-ad1f6f41665a`: supplies the total high-window overlap-energy lower
  bound.
- `mrw-20ca89f696f2`: supplies the endpoint interval language used in the
  chargeability and local-shield conclusion.

## Used by

- Future diagonal-branch closures: if endpoint weights are diffuse and
  high-window density \(\rho\) is bounded below, then \(\Delta\) cannot carry a
  positive share of \(M^2/\tau\).
- Future escaped-mass alternatives: after chargeable energy is small, diffuse
  endpoint weights force the distinct nonchargeable-pair branch.
- Future concentration audits: if the diagonal branch remains large, it must
  come with \(H_2(w)\ge\delta\rho^2\) and \(\eta\ge\delta\rho\), so it is an
  endpoint atom/concentration obstruction rather than a diffuse phenomenon.

## Notes

- This proposition is algebraic and does not require \(\nu_T\) to be a product
  measure.  Product structure enters only in later lower-shadow charging tools.
- The concentration conclusion is relative to the high-window density \(\rho\).
  When \(\rho\) is tiny, the forced lower bounds on \(H_2(w)\) and \(\eta\)
  are correspondingly weak.
- No pair-link-free hypothesis is used here.  The final local shield
  \(\mathcal E\cap I_B(e,f)\subseteq\{e,f\}\) is definitional from
  nonchargeability, not a terminal structural theorem.
