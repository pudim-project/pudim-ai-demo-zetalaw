---
id: "T-Keady-finite-range-to-self-range-repair-instance"
type: "theorem"
title: "Keady finite range inverse CM counterexample singular tail self range repair instance"
status: "proved"
tags: ["complete-monotonicity", "keady", "proved", "repair-pattern", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["attack-plans/AP-20260531T030200-keady-self-bijection-inverse-cm.json", "librarian/audits/LA-20260531T030200-keady-self-bijection-inverse-cm.json", "oracle/responses/ORACLE-FI-20260531T-rolling-059-oracle-forage-response.md", "oracle/responses/ORACLE-OS-20260531T-keady-self-bijection-inverse-cm-oracle-response.md", "raw/scout/sources/keady-inverse-self-bijection-source-status.md", "raw/student/20260531T030200-keady-self-bijection-inverse-cm.md", "wiki/notes/frontier-keady-self-bijection-inverse-cm.md"]
---

# Theorem: Keady finite range inverse CM counterexample singular tail self range repair instance

## Statement

In the Keady inverse-CM problem, adding the singular completely monotone tail \(1/x\) in the example \(x^{-1}+100e^{-x}\) repairs the range to \((0,\infty)\) while preserving a third-derivative inverse obstruction.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `attack-plans/AP-20260531T030200-keady-self-bijection-inverse-cm.json`
- `librarian/audits/LA-20260531T030200-keady-self-bijection-inverse-cm.json`
- `oracle/responses/ORACLE-FI-20260531T-rolling-059-oracle-forage-response.md`
- `oracle/responses/ORACLE-OS-20260531T-keady-self-bijection-inverse-cm-oracle-response.md`
- `raw/scout/sources/keady-inverse-self-bijection-source-status.md`
- `raw/student/20260531T030200-keady-self-bijection-inverse-cm.md`
- `wiki/notes/frontier-keady-self-bijection-inverse-cm.md`

## Proof

There exists a completely monotone decreasing bijection
\[
f:(0,\infty)\to(0,\infty)
\]
whose inverse is not completely monotone. One explicit example is
\[
f(x)=\frac1x+100e^{-x}.
\]

For every \(n\ge0\),
\[
(-1)^n f^{(n)}(x)=\frac{n!}{x^{n+1}}+100e^{-x}>0.
\]
Thus \(f\) is strictly completely monotone. Also
\[
f'(x)=-x^{-2}-100e^{-x}<0,
\]
so \(f\) is strictly decreasing. Finally,
\[
\lim_{x\downarrow0}f(x)=\infty,
\qquad
\lim_{x\to\infty}f(x)=0.
\]
Therefore \(f\) is a decreasing bijection from \((0,\infty)\) onto \((0,\infty)\).

Let \(g=f^{-1}\) and write \(y=f(x)\). Inverse differentiation gives
\[
g'''(f(x))=\frac{3(f''(x))^2-f'''(x)f'(x)}{(f'(x))^5}.
\]
For \(f_a(x)=x^{-1}+ae^{-x}\), define
\[
N_a(x)=3(f_a''(x))^2-f_a'''(x)f_a'(x).
\]
A direct calculation gives
\[
N_a(x)=\frac6{x^6}+ae^{-x}\left(-\frac6{x^4}+\frac{12}{x^3}-\frac1{x^2}\right)+2a^2e^{-2x}.
\]
At \(a=100\) and \(x_0=1/8\),
\[
N_{100}(1/8)=1{,}572{,}864-1{,}849{,}600e^{-1/8}+20{,}000e^{-1/4}.
\]
Using \(e^{-1/8}>7/8\) and \(e^{-1/4}<1\),
\[
N_{100}(1/8)<1{,}572{,}864-1{,}849{,}600\cdot\frac78+20{,}000=-25{,}536<0.
\]
Since \(f'(1/8)<0\), the denominator \((f'(1/8))^5\) is negative. Hence
\[
g'''(f(1/8))=\frac{N_{100}(1/8)}{(f'(1/8))^5}>0.
\]
A completely monotone function must satisfy \((-1)^3g'''\ge0\), i.e. \(g'''\le0\). Therefore \(g=f^{-1}\) is not completely monotone.

_Proof source: `raw/student/20260531T030200-keady-self-bijection-inverse-cm.md`._

## Tags

`complete-monotonicity`, `keady`, `proved`, `repair-pattern`, `theorem`
