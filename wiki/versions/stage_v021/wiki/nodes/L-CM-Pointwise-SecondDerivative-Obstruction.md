---
id: "L-CM-Pointwise-SecondDerivative-Obstruction"
type: "lemma"
title: "Pointwise second derivative obstruction to complete monotonicity"
status: "proved"
tags: ["bridge-lemma", "complete-monotonicity", "endpoint-obstruction", "finite-certificate", "lemma", "primitive-growth", "proved", "true"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Endpoint-obstruction-certificate-language"]
refs: ["raw/student/20260622T1539-nantomah-pbeta-finite-refutation.md"]
---

# Lemma: Pointwise second derivative obstruction to complete monotonicity

## Statement

If a \(C^\infty\) function \(F\) on an interval is completely monotone, then \(F''(x)\ge0\) at every interior point. Consequently, one exact point \(x_0\) with \(F''(x_0)<0\) refutes complete monotonicity.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]

## Proof and provenance references

- `raw/student/20260622T1539-nantomah-pbeta-finite-refutation.md`

## Proof

Take \(p=1\) and \(n=1\). Then
\[
\beta_1(x)={1\over x}-{1\over x+1}+{1\over x+2}-{1\over x+3},
\]
and
\[
F(x):=x^2|\beta_1'(x)|
=1-\left({x\over x+1}\right)^2
+\left({x\over x+2}\right)^2
-\left({x\over x+3}\right)^2.
\]
Equivalently,
\[
F(x)=
{2(2x+3)(x^4+6x^3+15x^2+18x+6)
\over (x+1)^2(x+2)^2(x+3)^2}.
\]

Exact differentiation gives
\[
F''(x)=
{4P(x)\over (x+1)^4(x+2)^4(x+3)^4},
\]
where
\[
P(x)=2x^9+21x^8+112x^7+450x^6+1392x^5+2847x^4
+3264x^3+1440x^2-546x-558.
\]
At \(x=1/3\),
\[
F''(1/3)=-{27738747\over 192080000}<0.
\]

\emph{Conclusion.}
A completely monotone \(C^\infty\) function on \((0,\infty)\) must satisfy
\[
(-1)^m f^{(m)}(x)\ge0
\]
for every \(m\ge0\) and \(x>0\). In particular, \(f''(x)\ge0\). The exact rational value above violates this at an admissible point for the source expression. Therefore Nantomah's Section 3 complete-monotonicity open problem is false.

The endpoint check is consistent:
\[
F(x)=1-{31\over36}x^2+{197\over108}x^3-{1231\over432}x^4+O(x^5),
\]
so \(F''(x)<0\) also holds for all sufficiently small positive \(x\).

_Proof source: `raw/student/20260622T1539-nantomah-pbeta-finite-refutation.md`._

## Tags

`bridge-lemma`, `complete-monotonicity`, `endpoint-obstruction`, `finite-certificate`, `lemma`, `primitive-growth`, `proved`, `true`
