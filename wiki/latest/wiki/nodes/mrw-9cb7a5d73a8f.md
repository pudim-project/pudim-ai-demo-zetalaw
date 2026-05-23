---
id: mrw-9cb7a5d73a8f
type: proposition
title: Large endpoint-defect residual forces a shifted terminal-core residual
aliases: ["mrw-9cb7a5d73a8f", "Large endpoint-defect residual forces a shifted terminal-core residual"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, iterated-tower, occupancy-defect, occupancy-pattern, product-measure, support-tail, residual-reduction, terminal-residual, averaging, self-similar-obstruction, cross-core-coherence]
parents: [mrw-05f82d03b190]
refs: []
---

# Proposition: Large endpoint-defect residual forces a shifted terminal-core residual

## Statement

Use the endpoint-tower notation and the defect-pattern residual budget of
[[mrw-05f82d03b190]].  Thus
\[
\mathcal R_{\mathrm{def}}(L)
=
\sum_{m=0}^{|\mathcal B|}
\Pi_m^{\mathrm{def}}\,\mathfrak M_{P_r}(L-m),
\]
where \(\Pi_m^{\mathrm{def}}\ge 0\) is the product-measure mass of defect
endpoint patterns selecting exactly \(m\) endpoint coordinates, and
\[
\Pi_{\mathrm{def}}
=
\sum_{m=0}^{|\mathcal B|}\Pi_m^{\mathrm{def}}
\le 1 .
\]
Let
\[
\mathcal M_{\mathrm{def}}(L)
=
\max\{\mathfrak M_{P_r}(L-m):
0\le m\le |\mathcal B|,\ \Pi_m^{\mathrm{def}}>0\},
\]
with the convention that the maximum is \(0\) if there is no active defect
layer.

Then, for every real threshold \(L\),
\[
\mathcal R_{\mathrm{def}}(L)
\le
\Pi_{\mathrm{def}}\,\mathcal M_{\mathrm{def}}(L)
\le
\mathcal M_{\mathrm{def}}(L).
\]
Consequently, if \(\mathcal R_{\mathrm{def}}(L)\ge \delta>0\), then
\(\Pi_{\mathrm{def}}>0\), and there is an active endpoint-cardinality
\(m\) such that
\[
\mathfrak M_{P_r}(L-m)
\ge
\frac{\mathcal R_{\mathrm{def}}(L)}{\Pi_{\mathrm{def}}}
\ge
\delta .
\]
Also, for some endpoint-cardinality \(m\),
\[
\Pi_m^{\mathrm{def}}\,\mathfrak M_{P_r}(L-m)
\ge
\frac{\mathcal R_{\mathrm{def}}(L)}{|\mathcal B|+1}.
\]
Equivalently, if all active shifted terminal residuals satisfy
\(\mathfrak M_{P_r}(L-m)\le \varepsilon\), then
\[
\mathcal R_{\mathrm{def}}(L)\le \varepsilon\Pi_{\mathrm{def}}\le\varepsilon .
\]
In the prime-biased high-support specialization, the same conclusions hold
with \(L=\theta S_P\).

## Proof

The coefficients \(\Pi_m^{\mathrm{def}}\) are nonnegative and have total mass
\(\Pi_{\mathrm{def}}\le1\).  On every active layer,
\[
\mathfrak M_{P_r}(L-m)\le \mathcal M_{\mathrm{def}}(L).
\]
Multiplying by \(\Pi_m^{\mathrm{def}}\) and summing over \(m\) gives
\[
\mathcal R_{\mathrm{def}}(L)
=
\sum_m\Pi_m^{\mathrm{def}}\mathfrak M_{P_r}(L-m)
\le
\sum_m\Pi_m^{\mathrm{def}}\mathcal M_{\mathrm{def}}(L)
=
\Pi_{\mathrm{def}}\mathcal M_{\mathrm{def}}(L).
\]
Since \(\Pi_{\mathrm{def}}\le1\), this also gives
\(\mathcal R_{\mathrm{def}}(L)\le\mathcal M_{\mathrm{def}}(L)\).

If \(\mathcal R_{\mathrm{def}}(L)\ge\delta>0\), then not all
\(\Pi_m^{\mathrm{def}}\) vanish, so \(\Pi_{\mathrm{def}}>0\).  Dividing the
previous inequality by \(\Pi_{\mathrm{def}}\) gives
\[
\mathcal M_{\mathrm{def}}(L)
\ge
\frac{\mathcal R_{\mathrm{def}}(L)}{\Pi_{\mathrm{def}}}.
\]
By the definition of the finite maximum, some active \(m\) attains this
maximum, and \(\Pi_{\mathrm{def}}\le1\) implies
\[
\frac{\mathcal R_{\mathrm{def}}(L)}{\Pi_{\mathrm{def}}}
\ge
\mathcal R_{\mathrm{def}}(L)
\ge
\delta .
\]

The layer pigeonhole statement follows from the same nonnegative sum:
\(\mathcal R_{\mathrm{def}}(L)\) is the sum of at most
\(|\mathcal B|+1\) terms
\(\Pi_m^{\mathrm{def}}\mathfrak M_{P_r}(L-m)\).  Hence one term is at least
\(\mathcal R_{\mathrm{def}}(L)/(|\mathcal B|+1)\).

Finally, if every active shifted residual is at most \(\varepsilon\), then
\[
\mathcal R_{\mathrm{def}}(L)
\le
\sum_m\Pi_m^{\mathrm{def}}\varepsilon
=
\varepsilon\Pi_{\mathrm{def}}
\le
\varepsilon .
\]
The prime-biased version is just the substitution \(L=\theta S_P\); no
additional product-measure or pair-link argument is used.

## Depends on

- [[mrw-05f82d03b190]]

## Used by

## Notes

- This proposition isolates the terminal-core-residual branch of the
  defect-pattern alternative.  A large defect residual budget cannot remain
  distributed over endpoint patterns unless at least one shifted terminal
  core residual is already large.
- The result is only an averaging reduction.  It does not prove decay of
  \(\mathfrak M_{P_r}(L-m)\), does not create pointwise mixed incidence, and
  does not prove an \(R_P(\theta)\) lift.
- The remaining route must either prove a genuine shifted terminal-core
  residual theorem for \(P_r\), or use cross-pattern constraints not seen by
  the one-sided endpoint-pattern budget to force positive \(\Xi\) and then
  charge coherent-component defect through [[mrw-7f0eb8d1648c]].
