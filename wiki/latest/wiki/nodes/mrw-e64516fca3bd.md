---
id: mrw-e64516fca3bd
type: corollary
title: Terminal interval children lose endpoint-shadow mass
aliases: ["mrw-e64516fca3bd", "Terminal interval children lose endpoint-shadow mass"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, terminal-fiber, endpoint-multiplicity, cross-r, interval-shadow, endpoint-shadow, mass-loss, terminal-interval, separator-forest, route-quarantine]
parents: [mrw-e3fec03bf987, mrw-d83f21b84e5c, mrw-20ca89f696f2, mrw-baa182012831]
refs: []
  - raw/20260523T082620Z-erdos-536-terminal-interval-child-shadow-loss.md
  - raw/20260523T082620Z-erdos536-terminal-interval-child-shadow-loss.md
  - theory/forage/requests/20260523T082620Z-erdos536-terminal-interval-child-shadow-loss-request.md
  - theory/forage/responses/20260523T082620Z-erdos536-terminal-interval-child-shadow-loss-response.md
  - oracle/requests/20260523T082620Z-erdos536-terminal-interval-child-shadow-loss-oracle-request.md
  - oracle/responses/20260523T082620Z-erdos536-terminal-interval-child-shadow-loss-oracle-response.md
---

# Corollary: Terminal interval children lose endpoint-shadow mass

## Statement

Let \(P=B\sqcup T\) be finite.  Let \(\pi_B\) be an endpoint probability law on
\(2^B\), let \(\nu_T\) be a terminal probability law on \(2^T\), and let
\[
\mathcal F
=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal U_e\}
\subseteq2^P
\]
be pair-link-free.  For each \(R\subseteq T\), set
\[
\mathcal E_R=\{e\in\mathcal E:R\in\mathcal U_e\}.
\]

For endpoint families \(\mathcal A,\mathcal B\subseteq2^B\), define
\[
\mathsf I_B(\mathcal A,\mathcal B)
=
\bigcup_{a\in\mathcal A,\ b\in\mathcal B} I_B(a,b),
\]
and for one endpoint family \(\mathcal A\), define
\[
\mathsf J_B(\mathcal A)
=
\bigcup_{\substack{a,b\in\mathcal A\\a\ne b}}I_B(a,b).
\]

Then the following conditional mass-loss bounds hold.

1. Cross-terminal interval children.  If \(R_1\ne R_2\) and
\[
\mathcal C\subseteq I_T(R_1,R_2)\setminus\{R_1,R_2\},
\]
then
\[
\sum_{R_3\in\mathcal C}
\nu_T(R_3)\pi_B(\mathcal E_{R_3})
\le
\left(
1-\pi_B(\mathsf I_B(\mathcal E_{R_1},\mathcal E_{R_2}))
\right)
\nu_T(\mathcal C).
\]
In particular, if \(0\le\sigma\le1\) and
\[
\pi_B(\mathsf I_B(\mathcal E_{R_1},\mathcal E_{R_2}))\ge\sigma,
\]
then
\[
\sum_{R_3\in\mathcal C}
\nu_T(R_3)\pi_B(\mathcal E_{R_3})
\le
(1-\sigma)\nu_T(\mathcal C).
\]

2. Repeated-parent lower-shadow children.  If \(R\subseteq T\) and
\[
\mathcal D\subseteq\{R_0\subseteq T:R_0\subsetneq R\},
\]
then
\[
\sum_{R_0\in\mathcal D}
\nu_T(R_0)\pi_B(\mathcal E_{R_0})
\le
\left(
1-\pi_B(\mathsf J_B(\mathcal E_R))
\right)
\nu_T(\mathcal D).
\]
In particular, if \(0\le\sigma\le1\) and
\[
\pi_B(\mathsf J_B(\mathcal E_R))\ge\sigma,
\]
then
\[
\sum_{R_0\in\mathcal D}
\nu_T(R_0)\pi_B(\mathcal E_{R_0})
\le
(1-\sigma)\nu_T(\mathcal D).
\]

## Proof

For the cross-terminal bound, fix \(R_3\in\mathcal C\).  Because
\[
R_1\ne R_2
\qquad\text{and}\qquad
R_3\in I_T(R_1,R_2)\setminus\{R_1,R_2\},
\]
the terminal points \(R_1,R_2,R_3\) are pairwise distinct.  By
`mrw-e3fec03bf987`,
\[
\mathcal E_{R_3}
\cap
\mathsf I_B(\mathcal E_{R_1},\mathcal E_{R_2})
=
\emptyset.
\]
Therefore
\[
\pi_B(\mathcal E_{R_3})
\le
1-\pi_B(\mathsf I_B(\mathcal E_{R_1},\mathcal E_{R_2})).
\]
Multiplying by \(\nu_T(R_3)\) and summing over \(R_3\in\mathcal C\) gives
the first displayed inequality.  The \(\sigma\)-form follows immediately from
the endpoint-shadow lower bound.

For the repeated-parent bound, fix \(R_0\in\mathcal D\).  Since
\[
R_0\subsetneq R,
\]
the repeated-parent consequence of `mrw-e3fec03bf987` gives
\[
\mathcal E_{R_0}
\cap
\mathsf J_B(\mathcal E_R)
=
\emptyset.
\]
Here \(\mathsf J_B\) uses only distinct endpoint parents; this is necessary
because pair-link-freeness does not exclude a repeated ambient parent.  Hence
\[
\pi_B(\mathcal E_{R_0})
\le
1-\pi_B(\mathsf J_B(\mathcal E_R)).
\]
Multiplying by \(\nu_T(R_0)\) and summing over \(R_0\in\mathcal D\) proves the
second displayed inequality.  Again the \(\sigma\)-form follows immediately.

## Depends on

- `mrw-e3fec03bf987`: cross-terminal endpoint multiplicity interval-shadow
  exclusions.
- `mrw-d83f21b84e5c`: endpoint-weighted separator forests route active mass to
  terminal averages of endpoint multiplicity fibers.
- `mrw-20ca89f696f2`: endpoint-terminal interval factorization.
- `mrw-baa182012831`: pointwise endpoint residual conditioning context.

## Used by

- Future terminal-interval abundance arguments: once endpoint interval shadows
  have non-negligible \(\pi_B\)-mass, terminal child mass in the corresponding
  interval loses that same factor.
- Future obstruction classification: if this mass loss is weak, the endpoint
  families must have small interval-shadow mass and should be classified as
  shielded, product-tower, or separator residual structures.

## Notes

- This is a conditional charging corollary, not terminal Erdos 536 evidence.
- No universal positive lower bound for
  \(\pi_B(\mathsf I_B(\mathcal E_{R_1},\mathcal E_{R_2}))\) or
  \(\pi_B(\mathsf J_B(\mathcal E_R))\) is asserted.
- The cross-terminal child statement requires \(R_1\ne R_2\).  The diagonal
  repeated-parent case uses \(\mathsf J_B\), not the larger
  \(\mathsf I_B(\mathcal E_R,\mathcal E_R)\).
- If \(\mathcal C=\emptyset\) or \(\mathcal D=\emptyset\), the corresponding
  inequality is vacuous.
- If an endpoint shadow has full endpoint measure, the corresponding
  endpoint-weighted child mass is zero.  Under full-support endpoint and
  terminal atoms, this also forces the positive-terminal-weight child fibers
  to be empty.
- Oracle accepted the corollary after requiring \(R_1\ne R_2\), replacing
  "equivalently" by "in particular" in the \(\sigma\)-forms, and weakening the
  full-mass boundary wording to mass-zero.  Scout returned only a scaffold and
  was ingested raw-only.
