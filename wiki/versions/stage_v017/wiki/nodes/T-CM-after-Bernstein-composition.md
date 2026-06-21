---
id: "T-CM-after-Bernstein-composition"
type: "theorem"
title: "complete monotone after Bernstein composition remains complete monotone"
status: "proved"
tags: ["bernstein-function", "complete-monotonicity", "composition", "proved", "standard-closure", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private librarian audit", "private proof note", "private proof note", "wiki/notes/frontier-wakrim-w-symbol-bernstein-gap.md"]
---

# Theorem: complete monotone after Bernstein composition remains complete monotone

## Statement

If \(f\) is completely monotone on \((0,\infty)\) and \(g\) is a Bernstein function mapping \((0,\infty)\) into \((0,\infty)\), then \(f\circ g\) is completely monotone.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private librarian audit`
- `private proof note`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`bernstein-function`, `complete-monotonicity`, `composition`, `proved`, `standard-closure`, `theorem`
