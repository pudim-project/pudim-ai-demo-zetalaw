---
id: "T-Bulboaca-Zayed-gamma-quotient-full-monotonicity"
type: "theorem"
title: "Bulboaca-Zayed gamma quotient full derivative sign pattern"
status: "proved"
tags: ["application-candidate", "forage", "fresh-author", "gamma", "monotonicity", "proved", "psi", "source-open-solved", "theorem"]
parents: ["T-BZ-gamma-quotient-critical-window-reduction"]
refs: ["librarian/audits/LA-20260528T130000-bz-gamma-quotient-attack-plan.json", "librarian/audits/LA-20260531T213200-bz-gamma-critical-window-student.json", "raw/scout/sources/bulboaca-zayed-gamma-monotonicity-2026.md", "raw/student/20260531T213200-bz-gamma-critical-window.md", "scout/forage/inbox/FI-20260528T-next-loop-007.json", "wiki/notes/frontier-bulboaca-zayed-gamma-quotient.md"]
---

# Theorem: Bulboaca-Zayed gamma quotient full derivative sign pattern

## Statement

For the continuous extension \(\widetilde F\) of \(F(x)=\log\Gamma(x+1)/(\log(x^2+6)-\log(x+6))\) on \((-1,\infty)\), prove analytically that \(\widetilde F'\) has a unique zero \(x_m\simeq1.126207061\ldots\), with \(\widetilde F'<0\) on \((-1,x_m)\) and \(\widetilde F'>0\) on \((x_m,\infty)\).

## Dependencies

- [[wiki/nodes/T-BZ-gamma-quotient-critical-window-reduction|Bulboaca-Zayed gamma quotient critical window reduction]]

## Proof and provenance references

- `librarian/audits/LA-20260528T130000-bz-gamma-quotient-attack-plan.json`
- `librarian/audits/LA-20260531T213200-bz-gamma-critical-window-student.json`
- `raw/scout/sources/bulboaca-zayed-gamma-monotonicity-2026.md`
- `raw/student/20260531T213200-bz-gamma-critical-window.md`
- `scout/forage/inbox/FI-20260528T-next-loop-007.json`
- `wiki/notes/frontier-bulboaca-zayed-gamma-quotient.md`

## Proof

proof.

The raw numerator has a removable zero at \(x=1\), since \(G(1)=D(1)=0\).  Its
quadratic leading coefficient is
\[
\lim_{x\downarrow1}\frac{N_0(x)}{(x-1)^2}
=
\frac{7(\pi^2/6-1)-11(1-\gamma)}{98}<0,
\]
again by \(\pi^2<987/100\) and \(\gamma<5773/10000\), which gives
\(-1347/980000<0\).  Therefore any normalization dividing out the removable
\((x-1)^2\) factor is negative at the left endpoint.

The single-crossing candidate is true:
\[
the Bulboaca--Zayed gamma-quotient N single crossing one eight.
\]
Together with the source's theorem on \((-1,1)\) and the previous local
right-tail theorem for \(x\ge8\), this proves the critical-window reduction
\[
the Bulboaca--Zayed gamma-quotient critical window reduction
\]
and then the source problem
\[
the Bulboaca Zayed gamma quotient full monotonicity.
\]

The finite-envelope candidate is not separately promoted: the proof above is a
clean analytic ratio-kernel argument rather than the finite rational cover
specified in that candidate.  The diagnostic obstruction-map candidate is also
not needed after the single-crossing proof.

_Proof source: `raw/student/20260531T213200-bz-gamma-critical-window.md`._

## Tags

`application-candidate`, `forage`, `fresh-author`, `gamma`, `monotonicity`, `proved`, `psi`, `source-open-solved`, `theorem`
