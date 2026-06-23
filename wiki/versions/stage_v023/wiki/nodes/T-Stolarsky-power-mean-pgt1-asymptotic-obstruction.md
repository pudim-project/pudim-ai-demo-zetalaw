---
id: "T-Stolarsky-power-mean-pgt1-asymptotic-obstruction"
type: "theorem"
title: "p greater than 1 shifted power mean positive curvature and asymptotic obstruction"
status: "proved"
tags: ["asymptotic-obstruction", "attack-plan", "bernstein-function", "power-means", "proved", "stolarsky-means", "theorem"]
parents: ["T-Pointwise-obstruction-certificate-principle", "D-Endpoint-obstruction-certificate-language"]
refs: ["attack-plans/AP-20260528T181500-stolarsky-power-mean-sharpness.json", "librarian/audits/LA-20260528T182000-stolarsky-student.json", "raw/student/20260528T182000-stolarsky-power-mean-sharpness.md", "wiki/notes/frontier-stolarsky-power-mean-sharpness.md"]
---

# Theorem: p greater than 1 shifted power mean positive curvature and asymptotic obstruction

## Statement

For \(p>1\), \(d\ne0\), and \(y>|d|\), the shifted power mean \(G(y)=H_p(y+d,y-d)\) satisfies \(G''(y)>0\). In particular, \(G(y)=y+\frac{(p-1)d^2}{2y}+O(y^{-3})\) as \(y\to\infty\), so \(G'\) is eventually increasing.

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]

## Proof and provenance references

- `attack-plans/AP-20260528T181500-stolarsky-power-mean-sharpness.json`
- `librarian/audits/LA-20260528T182000-stolarsky-student.json`
- `raw/student/20260528T182000-stolarsky-power-mean-sharpness.md`
- `wiki/notes/frontier-stolarsky-power-mean-sharpness.md`

## Proof

Let
\[
c=\frac{a+b}{2},\qquad d=\frac{a-b}{2}.
\]
Since \(a,b>0\) and \(a\ne b\), we have \(c>|d|>0\). Put \(y=x+c\). Then on the natural half-line \(y>|d|\),
\[
F(x)=G(y),
\qquad
G(y)=\left(\frac{(y+d)^p+(y-d)^p}{2}\right)^{1/p}.
\]
Translation does not affect the sign pattern of derivatives, so it is enough to show that \(G\) is not Bernstein.

For \(|t|<1\), define
\[
\phi_p(t)=H_p(1+t,1-t)
=2^{-1/p}\left((1+t)^p+(1-t)^p\right)^{1/p}.
\]
By homogeneity,
\[
G(y)=y\phi_p(d/y).
\]
Let
\[
A=1+t,\qquad B=1-t,\qquad N=A^p+B^p.
\]
Then \(\phi_p(t)=2^{-1/p}N^{1/p}\). Differentiating twice gives
\[
\phi_p''(t)
=2^{-1/p}(p-1)N^{1/p-2}
\left(N(A^{p-2}+B^{p-2})-(A^{p-1}-B^{p-1})^2\right).
\]
The bracket simplifies to
\[
A^{p-2}B^{p-2}(A+B)^2,
\]
because
\[
(A^p+B^p)(A^{p-2}+B^{p-2})-(A^{p-1}-B^{p-1})^2
=A^{p-2}B^{p-2}(A^2+2AB+B^2).
\]
For \(p>1\) and \(|t|<1\), all factors are positive, so
\[
\phi_p''(t)>0.
\]
Since \(t=d/y\),
\[
G'(y)=\phi_p(t)-t\phi_p'(t)
\]
and
\[
G''(y)=\frac{t^2}{y}\phi_p''(t)
=\frac{d^2}{y^3}\phi_p''(d/y)>0
\]
for every \(y>|d|\).

For \(|u|<1\), define
\[
A(u)=\frac{(1+u)^p+(1-u)^p}{2}.
\]
The odd terms cancel in the binomial expansion, giving
\[
A(u)=1+\frac{p(p-1)}{2}u^2+O(u^4)
\qquad (u\to0).
\]
Since \(z\mapsto z^{1/p}\) is analytic near \(z=1\),
\[
A(u)^{1/p}
=1+\frac1p\cdot\frac{p(p-1)}{2}u^2+O(u^4)
=1+\frac{p-1}{2}u^2+O(u^4).
\]
With \(u=d/y\), this yields
\[
G(y)
=yA(d/y)^{1/p}
=y+\frac{(p-1)d^2}{2y}+O(y^{-3})
\qquad (y\to\infty).
\]
Differentiating the same analytic expansion gives
\[
G'(y)
=1-\frac{(p-1)d^2}{2y^2}+O(y^{-4}),
\]
and hence
\[
G''(y)
=\frac{(p-1)d^2}{y^3}+O(y^{-5}).
\]
Because \(p>1\) and \(d\ne0\), the leading coefficient is positive. This recovers the tail obstruction from the exact curvature certificate above.

If \(G\) were a Bernstein function, then \(G'\) would be completely monotone. In particular,
\[
(G')'(y)=G''(y)\le0
\]
throughout the interval. This contradicts the positivity of \(G''(y)\) proved above.

Thus \(G\), and equivalently \(F\), is not a Bernstein function.

_Proof source: `raw/student/20260528T182000-stolarsky-power-mean-sharpness.md`._

## Tags

`asymptotic-obstruction`, `attack-plan`, `bernstein-function`, `power-means`, `proved`, `stolarsky-means`, `theorem`
