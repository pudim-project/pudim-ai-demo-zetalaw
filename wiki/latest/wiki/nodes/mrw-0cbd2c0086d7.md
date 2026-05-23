---
id: mrw-0cbd2c0086d7
type: corollary
title: Active high-window mass forces quantified overlap branches
aliases: ["mrw-0cbd2c0086d7", "Active high-window mass forces quantified overlap branches"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, endpoint-fiber, prime-biased-endpoints, high-window, active-mass, overlap-energy, chargeable-pairs, nonchargeable-pairs, empty-atom, endpoint-intensity, local-shield, lower-shadow, branch-routing, escaped-mass]
parents: [mrw-0845a9abe5b6, mrw-45819fa8022f, mrw-4a7cdb250fd4, mrw-108414b9dce7]
refs: []
  - raw/20260522T170530Z-erdos-536-active-mass-overlap-branch.md
  - raw/20260522T170530Z-erdos536-active-mass-overlap-branch.md
  - raw/20260522T170530Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T170530Z-erdos536-active-mass-overlap-branch-request.md
  - theory/forage/responses/20260522T170530Z-erdos536-active-mass-overlap-branch-response.md
  - oracle/requests/20260522T170530Z-erdos536-active-mass-overlap-branch-oracle-request.md
  - oracle/responses/20260522T170530Z-erdos536-active-mass-overlap-branch-oracle-response.md
---

# Corollary: Active high-window mass forces quantified overlap branches

## Statement
Let \(B\) be finite with endpoint product law
\[
\pi_B(e)=\prod_{b\in e}q_b\prod_{b\notin e}(1-q_b),
\qquad 0<q_b\le\frac12,
\]
and define
\[
P_0(B)=\prod_{b\in B}(1-q_b),
\qquad
Q(B)=\sum_{b\in B}q_b.
\]
Let \(T\) carry a probability law \(\nu_T\), let \(H\subseteq2^T\) satisfy \(\tau=\nu_T(H)>0\), and let \(\mathcal E\subseteq2^B\) have terminal fibers \(\mathcal R_e\subseteq2^T\). Define
\[
M=\sum_{e\in\mathcal E}\pi_B(e)\nu_T(\mathcal R_e\cap H),
\qquad
\Lambda=\sum_{e\in\mathcal E}\pi_B(e).
\]
Assume the overlap accounting and diagonal quarantine hypotheses of `mrw-0845a9abe5b6`, so that for \(0<\gamma<1\) and \(0<\delta<1-\gamma\) its empty-atom, chargeable, or distinct nonchargeable shield branches hold with their extraction conclusions.

Fix \(0<\eta\le1\). If
\[
M\ge\eta\tau
\qquad\text{and}\qquad
P_0(B)<\delta\eta,
\]
then the empty-atom branch is impossible. In particular, this holds under the sufficient endpoint-intensity condition
\[
Q(B)>\log\frac1{\delta\eta}.
\]
Consequently at least one of the following alternatives holds.

1. Chargeable overlap branch:
\[
\Omega_{\mathcal C}\ge\gamma\frac{M^2}{\tau}.
\]
Moreover, there are distinct \(e,f,g\in\mathcal E\), with \(g\in I_B(e,f)\), such that
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge\gamma\eta^2.
\]
If additionally \(T\) is finite, \(\nu_T\) is a product law, \(H=H_h(T)=\{R\subseteq T:|R|>h\}\), and the lifted family
\[
\mathcal F
=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
\]
is pair-link-free, then \(g\) may be chosen so that
\[
\nu_T(\mathcal R_g)\le1-\gamma\eta^2.
\]

2. Distinct nonchargeable shield branch:
\[
\Omega_{\mathcal N}\ge(1-\gamma-\delta)\frac{M^2}{\tau}.
\]
Moreover, there is a distinct nonchargeable ordered pair \((e,f)\) such that
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge(1-\gamma-\delta)\eta^2
\]
and
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]

## Proof
The empty-atom branch from `mrw-0845a9abe5b6` gives
\[
M\le \frac{P_0(B)\tau}{\delta}.
\]
If \(P_0(B)<\delta\eta\), then
\[
\frac{P_0(B)\tau}{\delta}<\eta\tau\le M,
\]
which is a contradiction. Therefore the empty-atom branch is impossible.

For the endpoint-intensity sufficient condition, use \(1-q_b\le e^{-q_b}\) to get
\[
P_0(B)=\prod_{b\in B}(1-q_b)\le e^{-Q(B)}.
\]
Thus \(Q(B)>\log(1/(\delta\eta))\) implies \(P_0(B)\le e^{-Q(B)}<\delta\eta\).

Since \(M\ge\eta\tau>0\), one has \(M>0\) and therefore \(\Lambda>0\). Also
\[
M\le \Lambda\tau,
\qquad
\Lambda\le1.
\]
Hence, with \(\rho=M/(\Lambda\tau)\),
\[
\rho=\frac{M/\tau}{\Lambda}\ge \frac{M}{\tau}\ge\eta.
\]
Equivalently, this is the active-mass consequence of `mrw-45819fa8022f`.

With the empty branch excluded, the trichotomy of `mrw-0845a9abe5b6` leaves only the chargeable or distinct nonchargeable branches. In the chargeable branch, its extraction conclusion gives distinct \(e,f,g\in\mathcal E\) with \(g\in I_B(e,f)\) and
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge \gamma\rho^2.
\]
Since \(\rho\ge\eta\), this is at least \(\gamma\eta^2\). Under the additional product/high-window and pair-link-free hypotheses, the same trichotomy together with the lower-shadow charging input `mrw-108414b9dce7` gives
\[
\nu_T(\mathcal R_g)\le1-\gamma\rho^2\le1-\gamma\eta^2.
\]

In the distinct nonchargeable branch, `mrw-0845a9abe5b6` gives a distinct nonchargeable ordered pair \((e,f)\) with
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge(1-\gamma-\delta)\rho^2
\ge(1-\gamma-\delta)\eta^2,
\]
and the local shield
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]
This proves the claim.

## Depends on
- `mrw-0845a9abe5b6` for the empty-atom, chargeable-overlap, and distinct nonchargeable shield trichotomy.
- `mrw-45819fa8022f` for the active-mass implication \(M\ge\eta\tau\Rightarrow\rho\ge\eta\).
- `mrw-4a7cdb250fd4` for the empty-atom endpoint-intensity quarantine \(P_0(B)\le e^{-Q(B)}\).
- `mrw-108414b9dce7` for the product/high-window lower-shadow third-fiber bound in the chargeable branch.

## Used by
- Pending: escaped-mass arguments that need a concrete \(\eta^2\)-scale chargeable overlap or nonchargeable shielded pair.

## Notes
- This is a conditional routing lemma, not terminal Erdos 536 evidence.
- The strict condition \(P_0(B)<\delta\eta\) is necessary for contradiction against the non-strict empty-atom upper bound.
- The \(Q(B)\) condition is sufficient, not equivalent; small \(P_0(B)\) may hold without the displayed \(Q(B)\) lower bound.
- The third-fiber bound requires \(T\) finite, \(\nu_T\) product, \(H\) a support high window, and pair-link-freeness of the lifted family.
- Scout returned only a scaffold response; Oracle accepted the corrected statement with minor tightening.
