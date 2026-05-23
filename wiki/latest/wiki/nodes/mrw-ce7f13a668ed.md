---
id: mrw-ce7f13a668ed
type: proposition
title: Fixed-child endpoint pileup factors through common-core top-cover sections
aliases: ["mrw-ce7f13a668ed", "Fixed-child endpoint pileup factors through common-core top-cover sections"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, endpoint-fiber, endpoint-multiplicity, endpoint-shadow, interval-shadow, interval-pileup, fixed-child, common-core, top-cover, normalized-density, obstruction-split, route-quarantine]
parents: [mrw-8d6210a920bc]
refs: []
  - raw/20260523T102630Z-erdos-536-fixed-child-pileup-normal-form.md
  - raw/20260523T102630Z-erdos536-fixed-child-pileup-normal-form.md
  - raw/20260523T102630Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T102630Z-erdos536-fixed-child-pileup-normal-form-request.md
  - theory/forage/responses/20260523T102630Z-erdos536-fixed-child-pileup-normal-form-response.md
  - oracle/requests/20260523T102630Z-erdos536-fixed-child-pileup-normal-form-oracle-request.md
  - oracle/responses/20260523T102630Z-erdos536-fixed-child-pileup-normal-form-oracle-response.md
---

# Proposition: Fixed-child endpoint pileup factors through common-core top-cover sections

## Statement
Let \(B\) be finite and let \(\pi_B\) be a product probability law on \(2^B\)
with coordinate probabilities \(0<q_b<1\).  Fix \(g\subseteq B\), put
\[
U=B\setminus g,
\]
and write \(\pi_g\) for the restricted product law on \(2^g\).

For \(h\subseteq U\), define
\[
\omega_U(h)
=
\prod_{u\in h}q_u^2
\prod_{u\in U\setminus h}(1-q_u).
\]
For \(x,y\subseteq g\), define
\[
\kappa_g(x,y)
=
\mathbf 1_{x\cup y=g}
\prod_{b\in x\cap y}q_b^2
\prod_{b\in g\setminus(x\cap y)}(1-q_b).
\]

For endpoint families \(\mathcal A,\mathcal C\subseteq2^B\), define their
outside-core sections
\[
\mathcal A_h=\{x\subseteq g:h\cup x\in\mathcal A\},
\qquad
\mathcal C_h=\{y\subseteq g:h\cup y\in\mathcal C\},
\]
and define the top-cover numerator
\[
\Phi_g(\mathcal P,\mathcal Q)
=
\sum_{x\in\mathcal P}\sum_{y\in\mathcal Q}\kappa_g(x,y).
\]

If \(\lambda=\pi_B(\mathcal A)>0\) and
\(\mu=\pi_B(\mathcal C)>0\), then
\[
\lambda\mu D_{\mathcal A,\mathcal C}(g)
=
\sum_{h\subseteq U}\omega_U(h)\Phi_g(\mathcal A_h,\mathcal C_h).
\]
Equivalently, every ordered parent pair \((a,c)\) contributing to the fixed
child \(g\), meaning \(g\in I_B(a,c)\), has the unique form
\[
a=h\cup x,\qquad c=h\cup y,\qquad
h\subseteq U,\quad x,y\subseteq g,\quad x\cup y=g,
\]
and for such a pair
\[
\frac{\pi_B(a)\pi_B(c)}{\pi_B(I_B(a,c))}
=
\omega_U(h)\kappa_g(x,y).
\]

Define the ratio-weighted common-core section weight
\[
W_g(\mathcal A,\mathcal C)
=
\sum_{h\subseteq U}
\omega_U(h)\pi_g(\mathcal A_h)\pi_g(\mathcal C_h).
\]
If \(W_g(\mathcal A,\mathcal C)=0\), then
\[
D_{\mathcal A,\mathcal C}(g)=0.
\]
If \(W_g(\mathcal A,\mathcal C)>0\), set
\[
K_h
=
\frac{\Phi_g(\mathcal A_h,\mathcal C_h)}
{\pi_g(\mathcal A_h)\pi_g(\mathcal C_h)}
\]
on sections with positive denominator and
\[
\theta_h
=
\frac{\omega_U(h)\pi_g(\mathcal A_h)\pi_g(\mathcal C_h)}
{W_g(\mathcal A,\mathcal C)}.
\]
Then
\[
D_{\mathcal A,\mathcal C}(g)
=
\frac{W_g(\mathcal A,\mathcal C)}{\lambda\mu}
\sum_h\theta_hK_h.
\]
Consequently, if \(D_{\mathcal A,\mathcal C}(g)\ge L>0\) and
\(0<\rho\le1\), then either
\[
W_g(\mathcal A,\mathcal C)\ge\rho\lambda\mu,
\]
or there is \(h\subseteq U\) with positive section masses such that
\[
K_h>L/\rho.
\]

The ordered distinct repeated-parent version is as follows.  Let
\[
Z_{\mathcal A}
=
\sum_{\substack{a,c\in\mathcal A\\a\ne c}}\pi_B(a)\pi_B(c)>0.
\]
Define
\[
\Phi_g^{\ne}(\mathcal P)
=
\sum_{\substack{x,y\in\mathcal P\\x\ne y}}\kappa_g(x,y).
\]
Then
\[
Z_{\mathcal A}D_{\mathcal A}^{\ne}(g)
=
\sum_{h\subseteq U}\omega_U(h)\Phi_g^{\ne}(\mathcal A_h).
\]
Define
\[
W_g^{\ne}(\mathcal A)
=
\sum_{h\subseteq U}\omega_U(h)
\sum_{\substack{x,y\in\mathcal A_h\\x\ne y}}\pi_g(x)\pi_g(y).
\]
If \(W_g^{\ne}(\mathcal A)=0\), then
\[
D_{\mathcal A}^{\ne}(g)=0.
\]
If \(W_g^{\ne}(\mathcal A)>0\), the same weighted-average split holds: with
\[
K_h^{\ne}
=
\frac{\Phi_g^{\ne}(\mathcal A_h)}
{\sum_{\substack{x,y\in\mathcal A_h\\x\ne y}}\pi_g(x)\pi_g(y)}
\]
on positive-denominator sections, if
\(D_{\mathcal A}^{\ne}(g)\ge L>0\) and \(0<\rho\le1\), then either
\[
W_g^{\ne}(\mathcal A)\ge\rho Z_{\mathcal A},
\]
or some \(h\subseteq U\) has
\[
K_h^{\ne}>L/\rho.
\]

## Proof
The condition \(g\in I_B(a,c)\) is
\[
a\triangle c\subseteq g\subseteq a\cup c.
\]
If \(u\in U=B\setminus g\), then \(u\notin g\), so \(u\notin a\triangle c\);
therefore \(a\) and \(c\) agree outside \(g\).  Let their common outside trace
be \(h\subseteq U\).  If \(b\in g\), then \(g\subseteq a\cup c\) forces at
least one of \(a,c\) to contain \(b\).  Writing
\[
x=a\cap g,\qquad y=c\cap g,
\]
we obtain \(x\cup y=g\).  This gives the unique representation
\[
a=h\cup x,\qquad c=h\cup y,\qquad x\cup y=g.
\]

For such a pair,
\[
\pi_B(a)\pi_B(c)
=
\left(\prod_{u\in h}q_u^2
\prod_{u\in U\setminus h}(1-q_u)^2\right)
\left(\prod_{b\in x\cap y}q_b^2
\prod_{b\in x\triangle y}q_b(1-q_b)\right).
\]
The interval \(I_B(a,c)\) forces the coordinates in \(U\setminus h\) to be
absent and the coordinates in \(x\triangle y\) to be present, while the
coordinates in \(h\cup(x\cap y)\) are free.  Hence
\[
\pi_B(I_B(a,c))
=
\left(\prod_{u\in U\setminus h}(1-q_u)\right)
\left(\prod_{b\in x\triangle y}q_b\right).
\]
Since \(x\cup y=g\), one has
\[
x\triangle y=g\setminus(x\cap y).
\]
Dividing the last two displays gives
\[
\frac{\pi_B(a)\pi_B(c)}{\pi_B(I_B(a,c))}
=
\omega_U(h)\kappa_g(x,y).
\]
Summing over all contributing pairs grouped by the unique outside core \(h\)
proves the displayed formula for
\(\lambda\mu D_{\mathcal A,\mathcal C}(g)\).

If \(W_g(\mathcal A,\mathcal C)=0\), then every section pair has
\(\pi_g(\mathcal A_h)\pi_g(\mathcal C_h)=0\).  Full support implies this is
equivalent to \(\mathcal A_h=\emptyset\) or \(\mathcal C_h=\emptyset\), so
\(\Phi_g(\mathcal A_h,\mathcal C_h)=0\) for every \(h\).  Therefore
\[
D_{\mathcal A,\mathcal C}(g)=0.
\]
If \(W_g>0\), insert
\[
\Phi_g(\mathcal A_h,\mathcal C_h)
=
\pi_g(\mathcal A_h)\pi_g(\mathcal C_h)K_h
\]
on positive sections and divide by \(\lambda\mu\).  This gives
\[
D_{\mathcal A,\mathcal C}(g)
=
\frac{W_g}{\lambda\mu}\sum_h\theta_hK_h.
\]
If \(D_{\mathcal A,\mathcal C}(g)\ge L\) and
\(W_g<\rho\lambda\mu\), then
\[
\sum_h\theta_hK_h
=
\frac{\lambda\mu}{W_g}D_{\mathcal A,\mathcal C}(g)
>
L/\rho.
\]
Thus at least one positive-denominator section satisfies \(K_h>L/\rho\).

For the repeated-parent density, the same fixed-child normal form applies.
Since both parents share the same outside core \(h\), the ambient endpoints
\[
a=h\cup x,\qquad c=h\cup y
\]
are distinct if and only if \(x\ne y\).  Thus the ordered distinct summation
is exactly \(\Phi_g^{\ne}(\mathcal A_h)\) after grouping by \(h\).  The
\(W_g^{\ne}=0\) boundary and the weighted-average split are the same algebra
with \(Z_{\mathcal A}\) in place of \(\lambda\mu\).

## Depends on
- `mrw-8d6210a920bc` for the normalized endpoint interval-pileup framework
  and notation.

## Used by
- Future classification of high normalized endpoint interval-pair pileup.
- Future attempts to distinguish common-core/separator residual branches from
  genuine top-cover section pileup branches.

## Notes
- This is a local algebraic normal form, not terminal Erdos 536 evidence.
- \(W_g\) is a ratio-weighted common-core section weight, not the ordinary
  probability of ordered parent pairs with common outside core.  The actual
  common-core pair probability would use \(\pi_U(h)^2\) instead of
  \(\omega_U(h)\).
- If \(g=\emptyset\), the cross formula reduces to the case \(a=c=h\); the
  repeated distinct density is zero at \(g=\emptyset\), as expected.
- If \(g=B\), then \(U=\emptyset\), and the formula is purely the top-cover
  identity on \(B\).
- Oracle accepted the factorization after correcting the weighted-average
  formula, adding \(W_g=0\Rightarrow D=0\), and clarifying that the split uses
  strict \(K_h>L/\rho\) when the common-core alternative fails.  Scout remained
  a scaffold response and was ingested raw-only.
