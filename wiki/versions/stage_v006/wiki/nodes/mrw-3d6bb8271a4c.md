---
id: mrw-3d6bb8271a4c
type: corollary
title: Interval-shielded endpoint mixtures reduce to endpoint variational residuals
aliases: ["mrw-3d6bb8271a4c", "Interval-shielded endpoint mixtures reduce to endpoint variational residuals"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, iterated-tower, occupancy-defect, occupancy-pattern, cross-pattern, interval-shield, antichain, terminal-residual, variational-residual, support-tail, cross-core-coherence]
parents: [mrw-20ca89f696f2, mrw-1f23857438d4, mrw-05f82d03b190]
refs: []
  - raw/20260521T194216Z-erdos-536-interval-shielded-endpoint-mixtures.md
  - raw/20260521T194216Z-erdos536-interval-shielded-endpoint-mixtures.md
  - theory/forage/requests/20260521T194216Z-erdos536-interval-shielded-endpoint-mixtures-request.md
  - theory/forage/responses/20260521T194216Z-erdos536-interval-shielded-endpoint-mixtures-response.md
  - oracle/requests/20260521T194216Z-erdos536-interval-shielded-endpoint-mixtures-oracle-request.md
  - oracle/responses/20260521T194216Z-erdos536-interval-shielded-endpoint-mixtures-oracle-response.md
---

# Corollary: Interval-shielded endpoint mixtures reduce to endpoint variational residuals

## Statement

Let \(P=B\sqcup T\) be a finite disjoint product space with product law
\(\nu_P=\nu_B\otimes\nu_T\).  For \(e\subseteq B\), write
\[
\pi_B(e)=\nu_B(\{e\}).
\]
For a real threshold \(L\), let \(\mathfrak M_T(L)\) denote the supremum of
\[
\nu_T(\mathcal R\cap\{R\subseteq T:|R|>L\})
\]
over all pair-link-free terminal families \(\mathcal R\subseteq2^T\).

Call \(\mathcal E\subseteq2^B\) interval-shielded if it has no nonconstant
endpoint interval triple:
\[
e_1,e_2,e_3\in\mathcal E,\qquad e_3\in I_B(e_1,e_2)
\quad\Longrightarrow\quad e_1=e_2=e_3.
\]
Fix an interval-shielded \(\mathcal E\).  Among all endpoint-pattern fiber
unions supported only on this endpoint collection,
\[
\mathcal F
=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
\]
that are pair-link-free in \(2^P\), the exact high-support supremum is
\[
\sup_{\mathcal F}
\nu_P(\mathcal F\cap\{S:|S|>L\})
=
\sum_{e\in\mathcal E}\pi_B(e)\,\mathfrak M_T(L-|e|).
\]
Equivalently, under the interval shield the cross-pattern branch contributes
no extra restriction beyond the independent fixed-pattern terminal residuals.

In the endpoint-tower notation of `mrw-05f82d03b190`, if
\(\mathcal E\subseteq\Omega_{\mathrm{def}}\) is a collection of defect
endpoint patterns whose endpoint-set image
\[
\{E(\omega):\omega\in\mathcal E\}\subseteq 2^{P\setminus P_r}
\]
is interval-shielded, then the exact shielded defect residual is
\[
\mathcal S_{\mathrm{sh}}(L;\mathcal E)
=
\sum_{\omega\in\mathcal E}
\pi(\omega)\,\mathfrak M_{P_r}(L-|E(\omega)|).
\]
Thus any cross-pattern improvement over this residual must use a nonconstant
endpoint interval triple and the terminal cross-fiber exclusion from
`mrw-20ca89f696f2`.

## Proof

First suppose that
\[
\mathcal F=\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
\]
is pair-link-free.  For each fixed \(e\), the fixed-pattern slice
\(\mathcal R_e\) must be pair-link-free on \(T\): any terminal pair-link triple
inside \(\mathcal R_e\) would become the same pair-link triple after adjoining
the common endpoint pattern \(e\).  Therefore
\[
\nu_T(\mathcal R_e\cap\{|R|>L-|e|\})
\le
\mathfrak M_T(L-|e|).
\]
The endpoint slices are disjoint and product measure factors, so
\[
\nu_P(\mathcal F\cap\{|S|>L\})
=
\sum_{e\in\mathcal E}\pi_B(e)\,
\nu_T(\mathcal R_e\cap\{|R|>L-|e|\})
\le
\sum_{e\in\mathcal E}\pi_B(e)\,\mathfrak M_T(L-|e|).
\]

For the reverse inequality, choose for every \(e\in\mathcal E\) a terminal
pair-link-free family \(\mathcal R_e\) attaining the finite-space supremum
\(\mathfrak M_T(L-|e|)\).  Equivalently, the same conclusion follows from
\(\varepsilon\)-near maximizers.  Since \(\mathcal E\) is interval-shielded and
every \(\mathcal R_e\) is pair-link-free, the endpoint shield consequence of
`mrw-20ca89f696f2` implies that the union
\[
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
\]
is pair-link-free.  Its high-support mass is exactly
\[
\sum_{e\in\mathcal E}\pi_B(e)\,\mathfrak M_T(L-|e|),
\]
which gives the reverse inequality.

The endpoint-tower formula is the same argument with \(B\) equal to the union
of endpoint classes, \(T=P_r\), endpoint patterns \(\omega\), endpoint set
\(E(\omega)\), and endpoint probability \(\pi(\omega)\), as in
`mrw-05f82d03b190`.

## Depends on

- [[mrw-20ca89f696f2]] Cross-pattern pair-link intervals factor by endpoint and terminal cores
- [[mrw-1f23857438d4]] Fixed overfull endpoint patterns are terminal residuals
- [[mrw-05f82d03b190]] Endpoint occupancy patterns reduce defect mass to terminal core residuals

## Used by

## Notes

- The corollary is a self-similar reduction, not a terminal estimate.  It does
  not prove \(\mathfrak M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or an
  \(R_P(\theta)\) lift.
- The point is negative but useful: an interval-shielded defect-pattern family,
  considered as an isolated endpoint-support branch, can be optimized
  independently pattern-by-pattern.  Therefore the next route must either
  bound the endpoint variational problem over shielded \(\mathcal E\), or show
  that positive high-support mass forces unshielded endpoint triples and hence
  terminal cross-fiber exclusions.
- This explicitly avoids using ordinary endpoint-pattern pair-link-freeness
  alone.  The shield includes the antichain condition needed to remove
  repeated-endpoint interval obstructions.
