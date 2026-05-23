---
id: mrw-6f8a9d8c0ea7
type: corollary
title: Heavy endpoint atoms force endpoint-shadow child loss
aliases: ["mrw-6f8a9d8c0ea7", "Heavy endpoint atoms force endpoint-shadow child loss"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, endpoint-multiplicity, endpoint-atoms, interval-shadow, endpoint-shadow, mass-loss, terminal-interval, heavy-atoms, cross-r, route-quarantine]
parents: [mrw-e64516fca3bd, mrw-e3fec03bf987, mrw-d83f21b84e5c, mrw-20ca89f696f2]
refs: []
  - raw/20260523T090621Z-erdos-536-heavy-endpoint-atoms-shadow-loss.md
  - raw/20260523T090621Z-erdos536-heavy-endpoint-atoms-shadow-loss.md
  - raw/20260523T090621Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T090621Z-erdos536-heavy-endpoint-atoms-shadow-loss-request.md
  - theory/forage/responses/20260523T090621Z-erdos536-heavy-endpoint-atoms-shadow-loss-response.md
  - oracle/requests/20260523T090621Z-erdos536-heavy-endpoint-atoms-shadow-loss-oracle-request.md
  - oracle/responses/20260523T090621Z-erdos536-heavy-endpoint-atoms-shadow-loss-oracle-response.md
---

# Corollary: Heavy endpoint atoms force endpoint-shadow child loss

## Statement
Let \(B\) be finite and let \(\pi_B\) be a product probability law on
\(2^B\) with coordinate probabilities \(0<q_b<1\).  For
\(a,b\subseteq B\), define
\[
I_B(a,b)=\{g\subseteq B:a\triangle b\subseteq g\subseteq a\cup b\}.
\]
Then
\[
\pi_B(I_B(a,b))\ge \pi_B(a)\pi_B(b).
\]

For endpoint families \(\mathcal A,\mathcal C\subseteq2^B\), define
\[
\mathsf I_B(\mathcal A,\mathcal C)
=
\bigcup_{x\in\mathcal A,\ y\in\mathcal C}I_B(x,y),
\]
and, for one endpoint family \(\mathcal A\), define
\[
\mathsf J_B(\mathcal A)
=
\bigcup_{\substack{x,y\in\mathcal A\\x\ne y}}I_B(x,y).
\]
Let \(0\le \alpha,\beta\le1\).  If \(a\in\mathcal A\),
\(c\in\mathcal C\), and
\[
\pi_B(a)\ge\alpha,\qquad \pi_B(c)\ge\beta,
\]
then
\[
\pi_B(\mathsf I_B(\mathcal A,\mathcal C))\ge\alpha\beta.
\]
If \(\mathcal A\) contains distinct \(a,c\) with
\[
\pi_B(a)\ge\alpha,\qquad \pi_B(c)\ge\beta,
\]
then
\[
\pi_B(\mathsf J_B(\mathcal A))\ge\alpha\beta.
\]

Now let \(P=B\sqcup T\), let \(\nu_T\) be a terminal probability law on
\(2^T\), and let
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
Then the conditional mass-loss bounds from `mrw-e64516fca3bd` have the following
heavy-atom forms.

1. If \(R_1\ne R_2\),
\[
\mathcal C\subseteq I_T(R_1,R_2)\setminus\{R_1,R_2\},
\]
and there are endpoint atoms \(a\in\mathcal E_{R_1}\) and
\(b\in\mathcal E_{R_2}\) satisfying
\[
\pi_B(a)\ge\alpha,\qquad \pi_B(b)\ge\beta,
\]
then
\[
\sum_{R_3\in\mathcal C}
\nu_T(R_3)\pi_B(\mathcal E_{R_3})
\le
(1-\alpha\beta)\nu_T(\mathcal C).
\]
Here \(a=b\) is allowed.

2. If \(R\subseteq T\),
\[
\mathcal D\subseteq\{R_0\subseteq T:R_0\subsetneq R\},
\]
and \(\mathcal E_R\) contains distinct endpoint atoms \(a\ne b\) satisfying
\[
\pi_B(a)\ge\alpha,\qquad \pi_B(b)\ge\beta,
\]
then
\[
\sum_{R_0\in\mathcal D}
\nu_T(R_0)\pi_B(\mathcal E_{R_0})
\le
(1-\alpha\beta)\nu_T(\mathcal D).
\]

## Proof
The interval measure factors coordinatewise as
\[
\pi_B(I_B(a,b))
=
\prod_{x\in a\triangle b}q_x
\prod_{x\notin a\cup b}(1-q_x),
\]
because coordinates in \(a\cap b\) are unrestricted.  The atom product is
\[
\pi_B(a)\pi_B(b)
=
\prod_{x\in a\cap b}q_x^2
\prod_{x\in a\triangle b}q_x(1-q_x)
\prod_{x\notin a\cup b}(1-q_x)^2.
\]
For every coordinate,
\[
q_x^2\le1,\qquad q_x(1-q_x)\le q_x,\qquad
(1-q_x)^2\le1-q_x.
\]
Multiplying these coordinatewise inequalities gives
\[
\pi_B(a)\pi_B(b)\le\pi_B(I_B(a,b)).
\]

If \(a\in\mathcal A\) and \(c\in\mathcal C\), then
\[
I_B(a,c)\subseteq \mathsf I_B(\mathcal A,\mathcal C),
\]
so
\[
\pi_B(\mathsf I_B(\mathcal A,\mathcal C))
\ge
\pi_B(I_B(a,c))
\ge
\pi_B(a)\pi_B(c)
\ge
\alpha\beta.
\]
If \(a\ne c\) are both in \(\mathcal A\), then
\[
I_B(a,c)\subseteq\mathsf J_B(\mathcal A),
\]
and the same argument gives
\[
\pi_B(\mathsf J_B(\mathcal A))\ge\alpha\beta.
\]

For the cross-terminal child bound, apply `mrw-e64516fca3bd` with
\[
\sigma=\alpha\beta.
\]
The endpoint-shadow lower bound just proved gives
\[
\pi_B(\mathsf I_B(\mathcal E_{R_1},\mathcal E_{R_2}))\ge\alpha\beta.
\]
The equality \(a=b\) of endpoint atoms is harmless here because \(R_1\ne R_2\)
and \(R_3\in I_T(R_1,R_2)\setminus\{R_1,R_2\}\) make the terminal parts of the
two parents and the child pairwise distinct.

For the repeated-parent bound, the distinct endpoint atoms \(a\ne b\) give
\[
\pi_B(\mathsf J_B(\mathcal E_R))\ge\alpha\beta.
\]
Applying the repeated-parent lower-shadow part of `mrw-e64516fca3bd` with
\(\sigma=\alpha\beta\) proves the displayed inequality.  The distinctness
\(a\ne b\) is necessary for this route because \(\mathsf J_B\) uses distinct
endpoint parents only.

## Depends on
- `mrw-e64516fca3bd` for the conditional terminal child-loss inequalities once
  an endpoint-shadow lower bound is available.
- `mrw-e3fec03bf987` for the underlying cross-terminal endpoint multiplicity
  interval-shadow exclusions.
- `mrw-d83f21b84e5c` for the endpoint-weighted separator forest context that
  routes active mass to endpoint multiplicity fibers.
- `mrw-20ca89f696f2` for endpoint/terminal interval factorization.

## Used by
- Future terminal interval abundance arguments in which large endpoint
  multiplicity fibers contain heavy endpoint atoms.
- Future obstruction classification: if the heavy-atom hypothesis fails, the
  endpoint shadow can still be small only through a diffuse/small-atom,
  interval-shielded, product-tower, or separator residual branch.

## Notes
- This is a conditional local charging corollary, not terminal Erdos 536
  evidence.
- No \(q_b\le1/2\) hypothesis is used; \(0<q_b<1\) is enough for the
  coordinatewise atom-interval inequality.
- The cross-terminal statement allows the same endpoint atom in both parent
  multiplicity fibers.  The repeated-parent statement requires distinct
  endpoint atoms because repeated ambient parents are not forbidden by
  pair-link-freeness.
- The corollary gives no useful lower bound in the diffuse or all-atoms-small
  regime.  That branch remains a separate endpoint-shadow classification
  problem.
- Oracle accepted the result after adding \(0\le\alpha,\beta\le1\), explicitly
  allowing equal cross-terminal endpoint atoms, and retaining endpoint
  distinctness in the repeated-parent \(\mathsf J_B\) case.
- Scout remained a scaffold response in this loop and was ingested raw-only.
