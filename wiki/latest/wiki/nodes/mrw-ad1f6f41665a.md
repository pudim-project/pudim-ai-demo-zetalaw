---
id: mrw-ad1f6f41665a
type: corollary
title: Chargeable endpoint pairs capture high-window overlap energy or force shielded concentration
aliases: ["mrw-ad1f6f41665a", "Chargeable endpoint pairs capture high-window overlap energy or force shielded concentration"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, terminal-product-measure, high-window, overlap-energy, chargeable-pairs, cauchy, fubini, common-fiber, lower-shadow, charging-lemma, shielded-concentration, escaped-mass]
parents: [mrw-108414b9dce7, mrw-82f19bf75c98, mrw-20ca89f696f2, mrw-baa182012831]
refs: []
  - raw/20260522T093007Z-erdos-536-chargeable-overlap-energy-alternative.md
  - raw/20260522T093007Z-erdos536-chargeable-overlap-energy-alternative.md
  - raw/20260522T093007Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T093007Z-erdos536-chargeable-overlap-energy-alternative-request.md
  - theory/forage/responses/20260522T093007Z-erdos536-chargeable-overlap-energy-alternative-response.md
  - oracle/requests/20260522T093007Z-erdos536-chargeable-overlap-energy-alternative-oracle-request.md
  - oracle/responses/20260522T093007Z-erdos536-chargeable-overlap-energy-alternative-oracle-response.md
---

# Corollary: Chargeable endpoint pairs capture high-window overlap energy or force shielded concentration

## Statement

Let \(T\) be finite with a product probability law \(\nu_T\), let
\[
H=H_h(T)=\{R\subseteq T:|R|>h\},
\qquad
\tau=\nu_T(H)>0,
\]
and let \(\mathcal E\subseteq2^B\) be a finite endpoint-pattern set.  Let
\(\lambda_e\ge0\) be endpoint weights with
\[
\Lambda=\sum_{e\in\mathcal E}\lambda_e>0,
\]
and let \(\mathcal R_e\subseteq2^T\) be terminal fibers.  Define
\[
M=\sum_{e\in\mathcal E}\lambda_e\,\nu_T(\mathcal R_e\cap H),
\qquad
\rho=\frac{M}{\Lambda\tau}.
\]

Call an ordered pair \((e,f)\in\mathcal E^2\) chargeable if \(e\ne f\) and
there exists \(g\in\mathcal E\setminus\{e,f\}\) such that
\[
g\in I_B(e,f).
\]
Let \(\mathcal C\) be the chargeable ordered-pair set.  Define
\[
\Omega_{\mathcal C}
=
\sum_{(e,f)\in\mathcal C}
\lambda_e\lambda_f\,\nu_T(\mathcal R_e\cap\mathcal R_f\cap H),
\]
and
\[
\Omega_{\mathcal U}
=
\sum_{(e,f)\notin\mathcal C}
\lambda_e\lambda_f\,\nu_T(\mathcal R_e\cap\mathcal R_f\cap H).
\]
Then
\[
\Omega_{\mathcal C}+\Omega_{\mathcal U}
\ge
\frac{M^2}{\tau}.
\]
Consequently, for every \(0\le\gamma\le1\), either
\[
\Omega_{\mathcal C}\ge \gamma\frac{M^2}{\tau},
\]
or
\[
\Omega_{\mathcal U}\ge (1-\gamma)\frac{M^2}{\tau}.
\]

Moreover, if \(\Omega_{\mathcal C}>0\), then there is a chargeable ordered
pair \((e,f)\in\mathcal C\) and a witness
\[
g\in\mathcal E\setminus\{e,f\},
\qquad
g\in I_B(e,f),
\]
such that
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
\frac{\Omega_{\mathcal C}}{\Lambda^2\tau}.
\]
In particular, if \(M>0\), \(0<\gamma\le1\), and
\[
\Omega_{\mathcal C}\ge\gamma\frac{M^2}{\tau},
\]
then the pair and witness can be chosen so that
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
\gamma\rho^2.
\]

If, in addition,
\[
\mathcal F
=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
\subseteq2^{B\sqcup T}
\]
is pair-link-free, then for such a witness \(g\),
\[
\nu_T(\mathcal R_g)\le1-\gamma\rho^2.
\]

## Proof

For \(R\in H\), define
\[
W(R)=\sum_{e\in\mathcal E}\lambda_e\,1_{\mathcal R_e}(R).
\]
By Fubini,
\[
\int_H W(R)\,d\nu_T(R)=M,
\]
and
\[
\int_H W(R)^2\,d\nu_T(R)
=
\sum_{e,f\in\mathcal E}
\lambda_e\lambda_f\,\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)
=
\Omega_{\mathcal C}+\Omega_{\mathcal U}.
\]
By Cauchy's inequality on \(H\),
\[
M^2
=
\left(\int_H W\,d\nu_T\right)^2
\le
\nu_T(H)\int_H W^2\,d\nu_T
=
\tau(\Omega_{\mathcal C}+\Omega_{\mathcal U}).
\]
This proves
\[
\Omega_{\mathcal C}+\Omega_{\mathcal U}
\ge
\frac{M^2}{\tau}.
\]
The two-way alternative follows from nonnegativity of
\(\Omega_{\mathcal C}\) and \(\Omega_{\mathcal U}\).

Assume \(\Omega_{\mathcal C}>0\).  Let
\[
W_{\mathcal C}=\sum_{(e,f)\in\mathcal C}\lambda_e\lambda_f.
\]
Then \(W_{\mathcal C}>0\), and by weighted averaging there is
\((e,f)\in\mathcal C\) such that
\[
\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)
\ge
\frac{\Omega_{\mathcal C}}{W_{\mathcal C}}
\ge
\frac{\Omega_{\mathcal C}}{\Lambda^2},
\]
because \(W_{\mathcal C}\le\Lambda^2\).  Dividing by \(\tau\) gives the
first displayed pair conclusion.  If also
\[
\Omega_{\mathcal C}\ge\gamma\frac{M^2}{\tau},
\]
then
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge
\gamma\frac{M^2}{\Lambda^2\tau^2}
=
\gamma\rho^2.
\]
Since \((e,f)\) is chargeable, choose
\[
g\in\mathcal E\setminus\{e,f\}
\quad\text{with}\quad
g\in I_B(e,f).
\]

Now suppose \(\mathcal F\) is pair-link-free.  Applying
`mrw-108414b9dce7` to the endpoint triple \(e,f,g\) and the threshold \(h\)
gives
\[
\nu_T(\mathcal R_g)
\le
1-
\frac{\nu_T((\mathcal R_e\cap\mathcal R_f)\cap H)}{\tau}
\le
1-\gamma\rho^2.
\]

## Depends on

- `mrw-108414b9dce7`: product lower shadows charge common high-window terminal
  mass and bound endpoint-interval third fibers.
- `mrw-82f19bf75c98`: common-fiber lower-shadow exclusion for endpoint
  interval triples.
- `mrw-20ca89f696f2`: endpoint-terminal interval factorization.
- `mrw-baa182012831`: pointwise endpoint residual conditioning, motivating
  the need to recover cross-\(R\) overlap energy.

## Used by

- Future common-overlap production arguments: enough chargeable endpoint-pair
  energy immediately yields a quantitative third-fiber exclusion.
- Future avoidance decompositions: if the chargeable branch fails, then a
  definite amount of high-window endpoint overlap energy is concentrated on
  nonchargeable pairs, including diagonals.

## Notes

- This is an averaging and local charging bridge, not terminal Erdos 536
  evidence.  It does not prove that chargeable endpoint pairs carry a positive
  energy share.
- The unchargeable energy \(\Omega_{\mathcal U}\) includes all diagonal
  terms \((e,e)\), since chargeable pairs require \(e\ne f\).  Thus the
  avoidance branch should be read as nonchargeable-or-diagonal concentration,
  not only distinct shielded-pair concentration.
- The non-vacuity assumptions in the pair-selection conclusion are necessary.
  If \(M=0\), \(\gamma=0\), or \(\Omega_{\mathcal C}=0\), the energy
  alternative may hold without producing any chargeable pair.
- The normalization obeys \(0\le\rho\le1\), because \(M\le\Lambda\tau\).
