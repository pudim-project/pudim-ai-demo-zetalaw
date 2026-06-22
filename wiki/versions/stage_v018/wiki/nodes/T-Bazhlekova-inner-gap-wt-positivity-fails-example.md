---
id: "T-Bazhlekova-inner-gap-wt-positivity-fails-example"
type: "theorem"
title: "Bazhlekova two-term inner gap exact example where wt positivity fails"
status: "proved"
tags: ["bazhlekova", "diffusion-wave", "inner-gap", "laplace-transform-obstruction", "not-staging-application", "partial-source-answer", "proved", "theorem", "two-term"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-sqrt-two-term-inner-gap-fifth-derivative-counterexample"]
refs: ["attack-plans/AP-20260531T110500-bazhlekova-inner-gap-fifth-derivative.json", "librarian/audits/LA-20260531T110500-bazhlekova-inner-gap-fifth-derivative.json", "oracle/responses/ORACLE-OS-20260531T-bazhlekova-inner-gap-fifth-derivative-oracle-response.md", "raw/student/20260531T110500-bazhlekova-inner-gap-fifth-derivative.md", "raw/student/20260531T110500-bazhlekova-inner-gap-fifth-derivative.py", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova two-term inner gap exact example where wt positivity fails

## Statement

For \(g(s)=s^{28/25}+s^{1/50}\), which lies in the Bazhlekova two-term inner gap, the propagation property \(w_t\ge0\) fails for some \(x>0\). Equivalently, \(e^{-x\sqrt{g(s)}}\) is not completely monotone for all sufficiently small positive \(x\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-sqrt-two-term-inner-gap-fifth-derivative-counterexample|Bazhlekova two-term inner gap exact fifth derivative counterexample to Bernstein square root]]

## Proof and provenance references

- `attack-plans/AP-20260531T110500-bazhlekova-inner-gap-fifth-derivative.json`
- `librarian/audits/LA-20260531T110500-bazhlekova-inner-gap-fifth-derivative.json`
- `oracle/responses/ORACLE-OS-20260531T-bazhlekova-inner-gap-fifth-derivative-oracle-response.md`
- `raw/student/20260531T110500-bazhlekova-inner-gap-fifth-derivative.md`
- `raw/student/20260531T110500-bazhlekova-inner-gap-fifth-derivative.py`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

\[
(a-1)^2+(b-1)^2\le 1
\]
in the straddling gap \(1<a<2\), \(0<b<a-1\). This pass tests the remaining inner gap with a higher derivative.

Let
\[
g(s)=s^{28/25}+s^{1/50},\qquad h(s)=\sqrt{g(s)}.
\]
Then \(a=28/25\), \(b=1/50\), so
\[
1<a<2,\qquad 0<b<a-1,\qquad a-b=\frac{11}{10}>1.
\]
Moreover
\[
(a-1)^2+(b-1)^2
=\left(\frac3{25}\right)^2+\left(-\frac{49}{50}\right)^2
=\frac{2437}{2500}<1.
\]
Thus this example is inside the previous concavity inner disk, not in the outside-disk concavity-loss region.

For general
\[
h_{a,b}(s)=\sqrt{s^a+s^b},
\]
direct differentiation at \(s=1\) gives
\[
\sqrt2\,h_{a,b}^{(5)}(1)
=\frac{(a+b-8)Q(a,b)}{512},
\]
where
\[
\begin{aligned}
Q(a,b)=&\,a^4+84a^3b-352a^3-154a^2b^2+224a^2b+1104a^2\\
&+84ab^3+224ab^2-992ab-768a\\
&+b^4-352b^3+1104b^2-768b .
\end{aligned}
\]
Substituting \(a=28/25\), \(b=1/50\) yields the exact value
\[
h^{(5)}(1)
=-\frac{5570045943\sqrt2}{320000000000}<0.
\]

Since a Bernstein function \(h\) must have \(h'\) completely monotone, its derivatives must satisfy
\[
h''\le0,\qquad h'''\ge0,\qquad h^{(4)}\le0,\qquad h^{(5)}\ge0,\ldots
\]
on \((0,\infty)\). The displayed fifth derivative violates this necessary condition, so \(h(s)=\sqrt{s^{28/25}+s^{1/50}}\) is not a Bernstein function.

The Bazhlekova source gives
\[
\mathcal L\{w_t(x,\cdot)\}(s)=F_x(s)=e^{-xh(s)}.
\]
If \(w_t(x,\cdot)\ge0\), then \(F_x\) must be completely monotone in \(s\). In particular,
\[
F_x^{(5)}(1)\le0.
\]
However, expanding in small \(x\),
\[
F_x(s)=1-xh(s)+O(x^2)
\]
locally with all needed \(s\)-derivatives continuous. Therefore
\[
F_x^{(5)}(1)=-x h^{(5)}(1)+O(x^2).
\]
Because \(h^{(5)}(1)<0\), the leading coefficient \(-h^{(5)}(1)\) is positive. Hence \(F_x^{(5)}(1)>0\) for all sufficiently small \(x>0\), contradicting complete monotonicity. Thus \(w_t(x,\cdot)\) fails positivity for some \(x>0\).

_Proof source: `raw/student/20260531T110500-bazhlekova-inner-gap-fifth-derivative.md`._

## Tags

`bazhlekova`, `diffusion-wave`, `inner-gap`, `laplace-transform-obstruction`, `not-staging-application`, `partial-source-answer`, `proved`, `theorem`, `two-term`
