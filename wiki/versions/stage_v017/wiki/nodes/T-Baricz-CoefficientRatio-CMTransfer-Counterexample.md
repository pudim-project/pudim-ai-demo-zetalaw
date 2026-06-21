---
id: "T-Baricz-CoefficientRatio-CMTransfer-Counterexample"
type: "theorem"
title: "Baricz coefficient-ratio CM transfer has a two-coefficient counterexample"
status: "proved"
tags: ["baricz", "biernacki-krzyz", "coefficient-extraction", "complete-monotonicity", "endpoint-obstruction", "finite-certificate", "power-series", "proved", "strict-private-app", "theorem", "true"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Endpoint-obstruction-certificate-language", "L-Baricz-GeometricSequence-StrictCM", "L-Baricz-AnalyticQuotient-SecondCoefficientObstruction"]
refs: ["private proof note", "private proof note"]
---

# Theorem: Baricz coefficient-ratio CM transfer has a two-coefficient counterexample

## Statement

Baricz Problem 4.3(c) has a negative answer. There exist entire power series \(f(x)=\sum a_nx^n\) and \(g(x)=\sum b_nx^n\), with \(b_n>0\), such that \(\{a_n/b_n\}_{n\ge0}\) is strictly completely monotone, but \(f/g\) is not completely monotone on any interval \((0,\varepsilon)\). One example is \(g(x)=1+x/4+x^2+\sum_{n\ge3}x^n/n!\) and \(f(x)=g(x/2)\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/L-Baricz-GeometricSequence-StrictCM|Geometric sequences are strictly completely monotone]]
- [[wiki/nodes/L-Baricz-AnalyticQuotient-SecondCoefficientObstruction|Second-coefficient obstruction for analytic quotient CM transfer]]

## Proof and provenance references

- `private proof note`
- `private proof note`

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

_Proof source: `private proof note`._

## Do not claim

- Do not claim the first-order Biernacki--Krzyz monotonicity lemma is false.
- Do not claim a positive transfer theorem under additional hypotheses not in the source.
- Do not public-stage without user request.

## Tags

`baricz`, `biernacki-krzyz`, `coefficient-extraction`, `complete-monotonicity`, `endpoint-obstruction`, `finite-certificate`, `power-series`, `proved`, `strict-private-app`, `theorem`, `true`
