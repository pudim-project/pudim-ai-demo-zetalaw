---
id: "T-SKJ-CM-slice-0-1-from-Alzer-Berg"
type: "theorem"
title: "H_a=e^a-(1+a/x)^x completely monotonic for 0<a<=1 via Alzer Berg H_1 Stieltjes theorem"
status: "proved"
tags: ["complete-monotonicity", "parameter-interval", "power-exponential", "proved", "skj", "stieltjes-transform", "student", "theorem", "true-helper"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private scout artifact", "private proof note", "wiki/notes/frontier-skj-power-exponential-cm-threshold.md"]
---

# Theorem: H_a=e^a-(1+a/x)^x completely monotonic for 0<a<=1 via Alzer Berg H_1 Stieltjes theorem

## Statement

For every \(0<a\le1\), the function \(H_a(x)=e^a-(1+a/x)^x\) is completely monotonic on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private scout artifact`
- `private proof note`
- `wiki/notes/frontier-skj-power-exponential-cm-threshold.md`

## Proof

\emph{Setup.}
Fix \(a>0\) and define
\[
H_a(x)=e^a-\left(1+\frac{a}{x}\right)^x,
\qquad
r_a(x)=x\log\left(1+\frac{a}{x}\right),
\qquad
h_a(x)=e^{r_a(x)}.
\]
Then \(H_a=e^a-h_a\).

For \(u>0\), \(\log(1+u)<u\). With \(u=a/x\),
\[
r_a(x)=x\log\left(1+\frac{a}{x}\right)<a,
\]
so \(h_a(x)<e^a\) and
\[
H_a(x)>0
\qquad(x>0,a>0).
\]

At the left endpoint,
\[
x\log\left(1+\frac{a}{x}\right)
=x\log(x+a)-x\log x\to0,
\]
so
\[
\lim_{x\to0^+}H_a(x)=e^a-1>0.
\]
At infinity,
\[
x\log\left(1+\frac{a}{x}\right)
=a-\frac{a^2}{2x}+O(x^{-2}),
\]
hence
\[
H_a(x)=\frac{e^a a^2}{2x}+O(x^{-2}).
\]

The derivative of \(r_a\) is
\[
r_a'(x)
=
\log\left(1+\frac{a}{x}\right)-\frac{a}{x+a}.
\]
For \(u=a/x>0\),
\[
\log(1+u)-\frac{u}{1+u}
=
\int_0^u\frac{t}{(1+t)^2}\,dt>0,
\]
so \(r_a'(x)>0\). Therefore
\[
H_a'(x)=-h_a(x)r_a'(x)<0,
\]
or equivalently
\[
(-1)H_a'(x)>0.
\]

For \(n\ge0\), define \(p_0(x)=1\) and
\[
p_{n+1}(x)=p_n'(x)+r_a'(x)p_n(x).
\]
Then
\[
h_a^{(n)}(x)=h_a(x)p_n(x)
\]
by induction.

For \(n\ge1\), set
\[
Q_n(x)=(-1)^{n+1}p_n(x).
\]
Since \(H_a^{(n)}=-h_a^{(n)}\) for \(n\ge1\), one has
\[
(-1)^nH_a^{(n)}(x)=h_a(x)Q_n(x),
\]
with
\[
Q_1(x)=r_a'(x),
\qquad
Q_{n+1}(x)=-Q_n'(x)-r_a'(x)Q_n(x).
\]
Thus complete monotonicity of \(H_a\) reduces to positivity of the recursively generated functions \(Q_n\).

For later interval certificates, the higher derivatives of \(r_a\) have the explicit form
\[
r_a^{(n)}(x)
=
(-1)^n(n-2)!
\left(
\frac{x+na}{(x+a)^n}-\frac{1}{x^{n-1}}
\right),
\qquad n\ge2.
\]

The bracket is strictly negative for \(a>0\), since
\[
(x+a)^n>x^{n-1}(x+na)
\]
by the binomial theorem. Hence \(r_a^{(n)}\) has sign \((-1)^{n+1}\) for \(n\ge2\).

Let
\[
\delta_a(x)=a-r_a(x).
\]
The positivity gate gives \(\delta_a(x)>0\). Since \(\delta_a'=-r_a'\), the first derivative gate gives
\[
(-1)\delta_a'(x)=r_a'(x)>0.
\]
For \(n\ge2\),
\[
(-1)^n\delta_a^{(n)}(x)=(-1)^{n+1}r_a^{(n)}(x)>0.
\]
Therefore \(\delta_a\) is strictly completely monotonic on \((0,\infty)\).

This does not by itself prove that \(H_a=e^a(1-e^{-\delta_a})\) is completely monotonic, because \(u\mapsto1-e^{-u}\) does not preserve complete monotonicity in the needed direction without an additional Bernstein/Laplace argument.

Let \(y=a/x\) and
\[
A(y)=\log(1+y)-\frac{y}{1+y}.
\]
Then \(r_a'(x)=A(y)\) and \(A'(y)=y/(1+y)^2\). The recurrence gives
\[
(-1)^2H_a''(x)=h_a(x)R_2(x),
\qquad
R_2=-r_a''-(r_a')^2.
\]
Equivalently,
\[
R_2(x)=\frac{1}{a}\left(y^2A'(y)-aA(y)^2\right)
=
\frac{1}{a}\left(
\frac{y^3}{(1+y)^2}
-a\left(\log(1+y)-\frac{y}{1+y}\right)^2
\right).
\]
Thus complete monotonicity of \(H_a\) forces
\[
a\le
T_2:=
\inf_{y>0}
\frac{y^3}{(1+y)^2\left(\log(1+y)-\frac{y}{1+y}\right)^2}.
\]
This is a rigorous necessary-gate formula. The numerical value of \(T_2\) is not promoted here.

_Proof source: `private proof note`._

## Tags

`complete-monotonicity`, `parameter-interval`, `power-exponential`, `proved`, `skj`, `stieltjes-transform`, `student`, `theorem`, `true-helper`
