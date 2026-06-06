---
id: "T-BZ-gamma-quotient-N-single-crossing-one-eight"
type: "theorem"
title: "Bulboaca Zayed gamma quotient numerator has one crossing on one eight"
status: "proved"
tags: ["attack-plan", "critical-window", "gamma", "proved", "psi", "theorem", "wide"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["attack-plans/AP-20260531T211500-bz-gamma-critical-window.json", "librarian/audits/LA-20260531T211500-bz-gamma-critical-window-attack-plan.json", "oracle/responses/ORACLE-OS-20260531T211700-bz-gamma-critical-window-oracle-response.md", "raw/student/20260531T213200-bz-gamma-critical-window.md", "wiki/notes/frontier-bulboaca-zayed-gamma-quotient.md"]
---

# Theorem: Bulboaca Zayed gamma quotient numerator has one crossing on one eight

## Statement

Let \(N(x)\) be the Bulboaca--Zayed derivative-sign numerator from \(T\)-BZ-gamma-quotient-derivative-normal-form. On \([1,8]\), \(N\) has exactly one zero \(\xi\), with \(N(x)<0\) for \(1\le x<\xi\) and \(N(x)>0\) for \(\xi<x\le8\).

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `attack-plans/AP-20260531T211500-bz-gamma-critical-window.json`
- `librarian/audits/LA-20260531T211500-bz-gamma-critical-window-attack-plan.json`
- `oracle/responses/ORACLE-OS-20260531T211700-bz-gamma-critical-window-oracle-response.md`
- `raw/student/20260531T213200-bz-gamma-critical-window.md`
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

`attack-plan`, `critical-window`, `gamma`, `proved`, `psi`, `theorem`, `wide`
