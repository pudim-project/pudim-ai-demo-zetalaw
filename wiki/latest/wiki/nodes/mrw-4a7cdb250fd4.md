---
id: mrw-4a7cdb250fd4
type: corollary
title: Endpoint intensity quarantines the empty-atom branch
aliases: ["mrw-4a7cdb250fd4", "Endpoint intensity quarantines the empty-atom branch"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, endpoint-fiber, prime-biased-endpoints, high-window, empty-atom, endpoint-intensity, branch-quarantine, trichotomy, escaped-mass]
parents: [mrw-0845a9abe5b6, mrw-c79041553496]
refs: []
  - raw/20260522T133021Z-erdos-536-empty-atom-branch-quarantine.md
  - raw/20260522T133021Z-erdos536-empty-atom-branch-quarantine.md
  - raw/20260522T133021Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T133021Z-erdos536-empty-atom-branch-quarantine-request.md
  - theory/forage/responses/20260522T133021Z-erdos536-empty-atom-branch-quarantine-response.md
  - oracle/requests/20260522T133021Z-erdos536-empty-atom-branch-quarantine-oracle-request.md
  - oracle/responses/20260522T133021Z-erdos536-empty-atom-branch-quarantine-oracle-response.md
---

# Corollary: Endpoint intensity quarantines the empty-atom branch

## Statement

Assume the endpoint-fiber hypotheses and notation of `mrw-0845a9abe5b6`.
Thus \(B\) carries the product law
\[
\pi_B(e)=\prod_{b\in e}q_b\prod_{b\notin e}(1-q_b),
\qquad
0<q_b\le\frac12,
\]
and
\[
P_0(B)=\prod_{b\in B}(1-q_b),
\qquad
Q(B)=\sum_{b\in B}q_b.
\]
Let
\[
\tau=\nu_T(H)>0,
\qquad
M=\sum_{e\in\mathcal E}\pi_B(e)\nu_T(\mathcal R_e\cap H).
\]
Fix the trichotomy parameters
\[
0\le\gamma<1,
\qquad
0<\varepsilon<1-\gamma.
\]

If the empty-atom branch of `mrw-0845a9abe5b6` holds, namely
\[
M\le\frac{P_0(B)\tau}{\varepsilon},
\]
then
\[
\frac{M}{\tau}\le\frac{e^{-Q(B)}}{\varepsilon}.
\]

Consequently, for any \(m>0\), if
\[
M\ge m\tau
\qquad\text{and}\qquad
Q(B)>\log\frac1{m\varepsilon},
\]
then the empty-atom branch is impossible.  Under the full trichotomy of
`mrw-0845a9abe5b6`, at least one of the two remaining branches must hold:
the chargeable-energy branch or the distinct nonchargeable shield branch.

For a sequence of endpoint-fiber configurations with fixed
\(\varepsilon>0\), \(\tau_n>0\), and \(Q(B_n)\to\infty\), every subsequence
on which the empty-atom branch holds satisfies
\[
\frac{M_n}{\tau_n}
\le
\frac{e^{-Q(B_n)}}{\varepsilon}
\to0.
\]
Thus any uniform positive relative high-window mass condition
\[
M_n\ge m\tau_n
\qquad(m>0)
\]
eventually excludes the empty-atom branch.

## Proof

Since \(0<q_b<1\),
\[
\log P_0(B)=\sum_{b\in B}\log(1-q_b).
\]
Using the elementary inequality
\[
\log(1-x)\le -x
\qquad(0<x<1),
\]
we obtain
\[
\log P_0(B)\le-\sum_{b\in B}q_b=-Q(B).
\]
Therefore
\[
P_0(B)\le e^{-Q(B)}.
\]
If the empty-atom branch holds, then
\[
M\le\frac{P_0(B)\tau}{\varepsilon}
\le
\frac{e^{-Q(B)}\tau}{\varepsilon}.
\]
Dividing by \(\tau>0\) gives
\[
\frac{M}{\tau}\le\frac{e^{-Q(B)}}{\varepsilon}.
\]

If also \(M\ge m\tau\), then the empty-atom branch would imply
\[
m\le\frac{M}{\tau}\le\frac{e^{-Q(B)}}{\varepsilon}.
\]
Equivalently,
\[
Q(B)\le\log\frac1{m\varepsilon}.
\]
Hence, when
\[
Q(B)>\log\frac1{m\varepsilon},
\]
the empty-atom branch cannot hold.  Applying `mrw-0845a9abe5b6` and deleting
the impossible branch leaves at least one of the chargeable-energy branch or
the distinct nonchargeable shield branch.

The sequence statement follows by applying the displayed estimate pointwise:
if \(Q(B_n)\to\infty\) and \(\varepsilon\) is fixed, then
\[
e^{-Q(B_n)}/\varepsilon\to0.
\]

## Depends on

- `mrw-0845a9abe5b6`: empty-atom mass or chargeable-or-shield trichotomy.
- `mrw-c79041553496`: diagonal empty-atom quarantine and the same endpoint
  intensity notation.

## Used by

- Future branch control: in any endpoint block with large \(Q(B)\), a positive
  lower bound on \(M/\tau\) removes the empty-atom branch and forces one of
  the two overlap branches from `mrw-0845a9abe5b6`.
- Future prime-coordinate applications: along endpoint blocks with diverging
  prime-biased endpoint intensity, an empty-atom-branch contribution has
  vanishing relative high-window mass.

## Notes

- This is a branch-elimination and quarantine corollary, not terminal Erdos
  536 evidence.
- The assumption \(q_b\le1/2\) is inherited from the endpoint law used in the
  preceding nodes.  The estimate \(P_0(B)\le e^{-Q(B)}\) only needs
  \(0<q_b<1\).
- The branch reduction is inclusive: after the empty-atom branch is excluded,
  at least one of the chargeable-energy branch or the distinct nonchargeable
  shield branch holds.  The two remaining branches need not be mutually
  exclusive.
- If \(\varepsilon\) varies in a sequence, the same proof requires
  \(e^{-Q(B_n)}/\varepsilon_n\to0\), not merely \(Q(B_n)\to\infty\).
