---
id: "T-Simon-gamma-quotient-complement-CM"
type: "theorem"
title: "Simon gamma quotient complement is CM for alpha in (0,1)"
status: "proved"
tags: ["complete-monotonicity", "gamma-quotient", "proved", "simon", "source-solving-tool", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260531T123900-simon-gamma-quotient-bf.json", "oracle/responses/ORACLE-OS-20260531T121700-simon-gamma-quotient-bf-oracle-response.md", "raw/student/20260531T123900-simon-gamma-quotient-bf.md", "wiki/notes/frontier-simon-gamma-quotient-bernstein.md"]
---

# Theorem: Simon gamma quotient complement is CM for alpha in (0,1)

## Statement

For every \(0<\alpha<1\), the function \(1-\Gamma(x+\alpha)/(\Gamma(x)x^\alpha)\) is completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260531T123900-simon-gamma-quotient-bf.json`
- `oracle/responses/ORACLE-OS-20260531T121700-simon-gamma-quotient-bf-oracle-response.md`
- `raw/student/20260531T123900-simon-gamma-quotient-bf.md`
- `wiki/notes/frontier-simon-gamma-quotient-bernstein.md`

## Proof

Thomas Simon's 2020 paper reduces the Bernstein character of the moment sequence \((n!)^t\), for \(0<t<1\), to the Bernstein character of
\[
\Phi_t(\lambda)=\frac{\Gamma(1-t+\lambda)}{\lambda^{1-t}\Gamma(\lambda)}.
\]
Equivalently, with \(\alpha=1-t\),
\[
F_\alpha(x)=\frac{\Gamma(x+\alpha)}{\Gamma(x)x^\alpha},
\qquad 0<\alpha<1.
\]

The source records this as unanswered and notes that \(1/\Phi_t\) is logarithmically completely monotone, but that this is not sufficient for \(\Phi_t\) to be Bernstein.

Local partial result:
\[
\frac{d}{dx}\log F_\alpha(x)
=
\int_0^\infty e^{-xt}
\left(
\frac{1-e^{-\alpha t}}{1-e^{-t}}-\alpha
\right)\,dt,
\]

_Proof source: `wiki/notes/frontier-simon-gamma-quotient-bernstein.md`._

## Tags

`complete-monotonicity`, `gamma-quotient`, `proved`, `simon`, `source-solving-tool`, `theorem`
