---
id: "T-BZ-gamma-quotient-critical-window-reduction"
type: "theorem"
title: "Bulboaca-Zayed gamma quotient critical window reduction"
status: "proved"
tags: ["attack-plan", "gamma", "interval-certificate", "mixed", "proved", "psi", "theorem"]
parents: ["T-BZ-gamma-quotient-polygamma-envelope-critical-certificate", "T-BZ-gamma-quotient-N-single-crossing-one-eight"]
refs: ["private attack plan", "private attack plan", "private librarian audit", "private librarian audit", "private proof note", "wiki/notes/frontier-bulboaca-zayed-gamma-quotient.md"]
---

# Theorem: Bulboaca-Zayed gamma quotient critical window reduction

## Statement

There is a rational interval \(J\) around \(1.126207061\ldots\) such that \(\widetilde F'<0\) on \((-1,\inf J]\), \(\widetilde F'>0\) on \([\sup J,\infty)\), and \(\widetilde F'\) has exactly one zero inside \(J\).

## Dependencies

- [[wiki/nodes/T-BZ-gamma-quotient-polygamma-envelope-critical-certificate|Bulboaca Zayed gamma quotient finite polygamma envelope critical certificate]]
- [[wiki/nodes/T-BZ-gamma-quotient-N-single-crossing-one-eight|Bulboaca Zayed gamma quotient numerator has one crossing on one eight]]

## Proof and provenance references

- `private attack plan`
- `private attack plan`
- `private librarian audit`
- `private librarian audit`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`attack-plan`, `gamma`, `interval-certificate`, `mixed`, `proved`, `psi`, `theorem`
