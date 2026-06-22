---
id: "T-Wakrim-W-symbol-exact-BF-range"
type: "theorem"
title: "Wakrim W symbol Bernstein exact beta range zero to one"
status: "proved"
tags: ["application-bridge", "bernstein-closure", "bernstein-function", "classification-theorem", "exact-range-theorem", "fractional-symbol", "proved", "source-open-solved", "theorem", "w-operator", "wakrim"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Bernstein-derivative-complete-monotonicity-criterion"]
refs: ["librarian/audits/LA-20260530T233500-wakrim-w-symbol-bernstein-gap.json", "librarian/audits/LA-20260601T-wakrim-author-feedback-proof-expansion.json", "oracle/responses/ORACLE-FI-20260530T-elegance-047-oracle-forage-response.md", "raw/student/20260530T233500-wakrim-w-symbol-bernstein-gap.md", "raw/student/20260601T-wakrim-author-feedback-proof-expansion.md", "wiki/notes/frontier-wakrim-w-symbol-bernstein-gap.md"]
---

# Theorem: Wakrim W symbol Bernstein exact beta range zero to one

## Statement

For \(0<\alpha<1\) and \(\beta\ge0\), the Wakrim W-symbol \(\Phi_{\alpha,\beta}(s)=s^\alpha(1+(1-\alpha)s^{\alpha-1})^{-\beta}\) is a Bernstein function on \((0,\infty)\) if and only if \(0\le\beta\le1\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Bernstein-derivative-complete-monotonicity-criterion|T-Bernstein-derivative-complete-monotonicity-criterion]]

## Proof and provenance references

- `librarian/audits/LA-20260530T233500-wakrim-w-symbol-bernstein-gap.json`
- `librarian/audits/LA-20260601T-wakrim-author-feedback-proof-expansion.json`
- `oracle/responses/ORACLE-FI-20260530T-elegance-047-oracle-forage-response.md`
- `raw/student/20260530T233500-wakrim-w-symbol-bernstein-gap.md`
- `raw/student/20260601T-wakrim-author-feedback-proof-expansion.md`
- `wiki/notes/frontier-wakrim-w-symbol-bernstein-gap.md`

## Proof

Set \(a=1-\alpha\in(0,1)\). Then
\[
\Phi_{\alpha,\beta}(s)
=s^{1-a}\left(1+a s^{-a}\right)^{-\beta}
=\frac{s^{1-a+a\beta}}{(s^a+a)^\beta}.
\]
Write
\[
p=1-a+a\beta=\alpha+(1-\alpha)\beta.
\]
Differentiating gives
\[
\Phi_{\alpha,\beta}'(s)
=s^{p-1}(s^a+a)^{-\beta-1}
\left[p(s^a+a)-\beta a s^a\right].
\]
Since \(p-\beta a=1-a=\alpha\),
\[
\Phi_{\alpha,\beta}'(s)
=s^{-a(1-\beta)}(s^a+a)^{-\beta-1}
\left[\alpha s^a+a(\alpha+a\beta)\right].
\]
With \(y=s^a\), this becomes
\[
\Phi_{\alpha,\beta}'(s)=H(s^a),
\]
where
\[
H(y)=
y^{\beta-1}(y+a)^{-\beta}
\left(\alpha+\frac{a^2\beta}{y+a}\right).
\]

For \(0<\beta\le1\), each factor in \(H\) is completely monotone on \((0,\infty)\): \(y^{\beta-1}=y^{-(1-\beta)}\), \((y+a)^{-\beta}\), and the positive sum \(\alpha+a^2\beta/(y+a)\). Therefore \(H\) is completely monotone by product and positive-sum closure.

The map \(s\mapsto s^a\) is Bernstein for \(0<a<1\). The standard composition theorem says that if \(f\) is completely monotone and \(g\) is Bernstein, then \(f\circ g\) is completely monotone. Hence \(\Phi_{\alpha,\beta}'\) is completely monotone, and \(\Phi_{\alpha,\beta}\) is Bernstein for \(0<\beta\le1\). The endpoint \(\beta=0\) is \(\Phi_{\alpha,0}(s)=s^\alpha\), also Bernstein.

Combining this local positive range with Wakrim's source proof that \(\Phi_{\alpha,\beta}\) is not Bernstein for \(\beta>1\), the exact range is
\[
\Phi_{\alpha,\beta}\in BF
\quad\Longleftrightarrow\quad
0\le\beta\le1.
\]

_Proof source: `raw/student/20260530T233500-wakrim-w-symbol-bernstein-gap.md`._

## Tags

`application-bridge`, `bernstein-closure`, `bernstein-function`, `classification-theorem`, `exact-range-theorem`, `fractional-symbol`, `proved`, `source-open-solved`, `theorem`, `w-operator`, `wakrim`
