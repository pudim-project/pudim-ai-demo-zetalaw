---
id: "T-BZ-gamma-quotient-derivative-normal-form"
type: "theorem"
title: "Bulboaca-Zayed gamma quotient derivative sign normal form"
status: "proved"
tags: ["attack-plan", "gamma", "normal-form", "proved", "psi", "theorem", "wide"]
parents: ["T-Special-function-normal-form-calculus-principle"]
refs: ["attack-plans/AP-20260528T130000-bz-gamma-quotient.json", "librarian/audits/LA-20260528T130000-bz-gamma-quotient-attack-plan.json", "librarian/audits/LA-20260528T131000-bz-gamma-quotient-student.json", "raw/student/20260528T130500-bz-gamma-quotient.md", "wiki/notes/frontier-bulboaca-zayed-gamma-quotient.md"]
---

# Theorem: Bulboaca-Zayed gamma quotient derivative sign normal form

## Statement

For \(x>-1\), away from removable points, the sign of \(\widetilde F'(x)\) is the sign of \(N(x)=(x+6)(x^2+6)\psi(x+1)(\log(x^2+6)-\log(x+6))-(x^2+12x-6)\log\Gamma(x+1)\).

## Dependencies

- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]

## Proof and provenance references

- `attack-plans/AP-20260528T130000-bz-gamma-quotient.json`
- `librarian/audits/LA-20260528T130000-bz-gamma-quotient-attack-plan.json`
- `librarian/audits/LA-20260528T131000-bz-gamma-quotient-student.json`
- `raw/student/20260528T130500-bz-gamma-quotient.md`
- `wiki/notes/frontier-bulboaca-zayed-gamma-quotient.md`

## Proof

Set
\[
P(x)=(x+6)(x^2+6),\qquad Q(x)=x^2+12x-6.
\]
For \(x\ge8\), \(Q(x)>0\). The standard inequalities
\[
\psi(x+1)>\log x
\]
and the Robbins/Stirling upper bound imply
\[
\log\Gamma(x+1)\le x\log x
\qquad (x\ge8).
\]
Indeed the Robbins upper bound gives
\[
\log\Gamma(x+1)
<
\left(x+\frac12\right)\log x-x+\frac12\log(2\pi)+\frac1{12x},
\]
and the remaining excess
\[
\frac12\log x-x+\frac12\log(2\pi)+\frac1{12x}
\]
is already negative at \(x=8\) and decreasing thereafter.

It remains to lower-bound \(D(x)\). Let
\[
u(x)=\frac{x^2+6}{x+6}.
\]
For \(x\ge8\), \(u(x)>1\), so
\[
\log u(x)\ge \frac{2(u(x)-1)}{u(x)+1}.
\]
A direct rational simplification gives
\[
\frac{2(u(x)-1)}{u(x)+1}
-\frac{xQ(x)}{P(x)}
=
\frac{x^2(x^3-3x^2-18x-78)}
{(x^2+x+12)(x+6)(x^2+6)}.
\]
The denominator is positive, and \(x^3-3x^2-18x-78\) is increasing for \(x\ge8\) and has value \(98>0\) at \(x=8\). Hence
\[
D(x)=\log u(x)\ge \frac{xQ(x)}{P(x)}
\qquad (x\ge8).
\]

Combining the three inequalities,
\[
N(x)
=P(x)\psi(x+1)D(x)-Q(x)\log\Gamma(x+1)
>
P(x)(\log x)D(x)-Q(x)x\log x
\ge0.
\]
Therefore \(N(x)>0\), and consequently
\[
\widetilde F'(x)>0
\qquad (x\ge8).
\]

_Proof source: `raw/student/20260528T130500-bz-gamma-quotient.md`._

## Tags

`attack-plan`, `gamma`, `normal-form`, `proved`, `psi`, `theorem`, `wide`
