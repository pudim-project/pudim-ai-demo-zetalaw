---
id: "T-Yang-Detemple-R-n0-CM-certificate"
type: "theorem"
title: "Yang Detemple R normalized n0 complete monotonicity certificate"
status: "proved"
tags: ["application-candidate", "complete-monotonicity", "detemple-sequence", "digamma", "laplace-kernel", "partial-progress", "proved", "source-slice-solved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["attack-plans/AP-20260529T-next-loop-yang-detemple-n0.json", "librarian/audits/LA-20260529T-next-loop-yang-detemple-student.json", "raw/student/20260529T-next-loop-yang-detemple-n0.md", "wiki/notes/frontier-yang-detemple-R-n0.md"]
---

# Theorem: Yang Detemple R normalized n0 complete monotonicity certificate

## Statement

The function \(F_0(x)=\left(24x^2+21/5\right)(\psi(x+1/2)-\log x)-1\) is completely monotone on \((0,\infty)\), with nonzero finite tail coefficient \(2071/33600\) at order \(x^{-4}\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `attack-plans/AP-20260529T-next-loop-yang-detemple-n0.json`
- `librarian/audits/LA-20260529T-next-loop-yang-detemple-student.json`
- `raw/student/20260529T-next-loop-yang-detemple-n0.md`
- `wiki/notes/frontier-yang-detemple-R-n0.md`

## Proof

The standard asymptotic expansion of \(\psi\) gives
\[
R(x)=\frac{1}{24x^2}-\frac{7}{960x^4}+O(x^{-6}).
\]
For the normalized \(n=0\) expression
\[
F(x)=(a_0+24x^2)R(x)-b_0
\]
to have a finite nonzero \(x^{-4}\) first tail term, the constant and \(x^{-2}\) terms must vanish.  Hence
\[
b_0=1,
\]
and
\[
\frac{a_0}{24}+24\left(-\frac{7}{960}\right)=0,
\]
so
\[
a_0=\frac{21}{5}.
\]
Thus the normalized candidate is
\[
F_0(x)=\left(24x^2+\frac{21}{5}\right)R(x)-1.
\]

Using
\[
\psi(z)=\int_0^\infty\left(\frac{e^{-t}}{t}-\frac{e^{-zt}}{1-e^{-t}}\right)dt
\]
and
\[
\log x=\int_0^\infty\frac{e^{-t}-e^{-xt}}{t}\,dt,
\]
we get
\[
R(x)=\int_0^\infty e^{-xt}r(t)\,dt,
\qquad
r(t)=\frac1t-\frac{1}{2\sinh(t/2)}.
\]
The kernel has \(r(0)=0\) and \(r'(0)=1/24\).  Twice integrating by parts gives
\[
x^2R(x)-\frac1{24}=\int_0^\infty e^{-xt}r''(t)\,dt.
\]
Therefore
\[
F_0(x)=\int_0^\infty e^{-xt}K(t)\,dt,
\qquad
K(t)=24r''(t)+\frac{21}{5}r(t).
\]

It remains to prove \(K(t)\ge0\).

Put \(y=t/2\) and \(h(y)=1/y-\operatorname{csch}y\).  Since \(r(t)=h(y)/2\) and \(d/dt=(1/2)d/dy\),
\[
K(t)=3h''(y)+\frac{21}{10}h(y).
\]
With
\[
h''(y)=\frac{2}{y^3}-\operatorname{csch}y\,\coth^2y-\operatorname{csch}^3y
\]
and \(\coth^2y=1+\operatorname{csch}^2y\), this is equivalent to
\[
K(t)=
\frac{
S(y)
}{
10y^3\sinh^3y
},
\]
where
\[
S(y)=(60+21y^2)\sinh^3y-51y^3\sinh^2y-60y^3.
\]

Using
\[
\sinh^3y=\frac{\sinh3y-3\sinh y}{4},
\qquad
\sinh^2y=\frac{\cosh2y-1}{2},
\]
one obtains the power series
\[
S(y)=\sum_{m=4}^{\infty} c_my^{2m+1},
\]
where
\[
c_m=
\frac{
15(3^{2m+1}-3)
+\frac{21}{4}(3^{2m-1}-3)(2m)(2m+1)
-\frac{51}{2}2^{2m-2}(2m-1)(2m)(2m+1)
}{
(2m+1)!}.
\]
The first coefficients are already positive:
\[
c_4=\frac{2071}{2520},\qquad
c_5=\frac{1909}{10080}.
\]
For \(m\ge6\), the positive \(3^{2m-1}\)-terms dominate the \(2^{2m-2}\) term; explicitly, after multiplying by \((2m+1)!\), the ratio of the positive part to the negative part is increasing from \(m=6\) onward and is already \(>1\) at \(m=6\).  Thus \(c_m>0\) for every \(m\ge4\).

Hence \(S(y)>0\) for \(y>0\), and therefore \(K(t)>0\) for \(t>0\).

By Bernstein's theorem,
\[
F_0(x)=\left(24x^2+\frac{21}{5}\right)(\psi(x+1/2)-\log x)-1
\]
is completely monotone on \((0,\infty)\).

Since \(K(t)=\frac{2071}{201600}t^3+O(t^5)\), Watson's lemma gives
\[
F_0(x)=\frac{2071}{33600}x^{-4}+O(x^{-6}).
\]
This verifies the nonzero finite tail condition for \(n=0\).

_Proof source: `raw/student/20260529T-next-loop-yang-detemple-n0.md`._

## Tags

`application-candidate`, `complete-monotonicity`, `detemple-sequence`, `digamma`, `laplace-kernel`, `partial-progress`, `proved`, `source-slice-solved`, `theorem`
