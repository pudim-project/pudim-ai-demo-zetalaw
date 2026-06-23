---
id: "L-Baricz-GeometricSequence-StrictCM"
type: "lemma"
title: "Geometric sequences are strictly completely monotone"
status: "proved"
tags: ["coefficient-extraction", "complete-monotonicity", "finite-difference", "lemma", "proved", "sequence", "true"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["raw/student/20260613T0815-baricz-coeffratio-cm-transfer-counterexample.md", "raw/student/20260614T-v016-baricz-coeffratio-public.md"]
---

# Lemma: Geometric sequences are strictly completely monotone

## Statement

For \(0<t<1\), the sequence \(c_n=t^n\) is strictly completely monotone under the forward-difference convention \(\Delta c_n=c_n-c_{n+1}\): for every \(n,k\ge0\), \(\Delta^kc_n=(1-t)^kt^n>0\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `raw/student/20260613T0815-baricz-coeffratio-cm-transfer-counterexample.md`
- `raw/student/20260614T-v016-baricz-coeffratio-public.md`

## Proof

Define
\[
g(x)=1+\frac{x}{4}+x^2+\sum_{n\ge3}\frac{x^n}{n!},
\qquad
f(x)=g(x/2).
\]
Then \(g\) and \(f\) are entire. The coefficients of \(g\) are
\[
b_0=1,\qquad b_1=\frac14,\qquad b_2=1,\qquad b_n=\frac1{n!}\quad(n\ge3),
\]
so \(b_n>0\) for every \(n\). Since \(f(x)=g(x/2)\), its coefficients satisfy
\[
a_n=b_n2^{-n}.
\]
Thus
\[
c_n=\frac{a_n}{b_n}=2^{-n}.
\]
For every \(n,k\ge0\),
\[
\Delta^k c_n=(1-\tfrac12)^k2^{-n}=2^{-n-k}>0.
\]
Hence \(\{a_n/b_n\}_{n\ge0}\) is strictly completely monotone, and therefore completely monotone, in the source sense.

Now write the quotient near the left endpoint. More generally, if
\[
g(x)=1+px+qx^2+O(x^3),\qquad 0<t<1,\qquad f(x)=g(tx),
\]
then
\[
\frac{f(x)}{g(x)}
=1+p(t-1)x+(1-t)\{p^2-q(1+t)\}x^2+O(x^3).
\]
In the present example \(p=1/4\), \(q=1\), and \(t=1/2\). Therefore
\[
[x^2]\frac{f(x)}{g(x)}
=\frac12\left(\frac1{16}-\frac32\right)
=-\frac{23}{32},
\]
so
\[
\left(\frac{f}{g}\right)''(0)=-\frac{23}{16}<0.
\]
By analyticity, \((f/g)''(x)<0\) for all sufficiently small \(x>0\). A completely monotone function on \((0,\varepsilon)\) must satisfy \(F''(x)\ge0\), so \(f/g\) is not completely monotone on any interval \((0,\varepsilon)\). It is therefore not strictly completely monotone either.

_Proof source: `raw/student/20260613T0815-baricz-coeffratio-cm-transfer-counterexample.md`._

## Tags

`coefficient-extraction`, `complete-monotonicity`, `finite-difference`, `lemma`, `proved`, `sequence`, `true`
