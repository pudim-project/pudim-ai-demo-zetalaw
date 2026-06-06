---
id: "T-not-Qi-hlambda-degree4-conjecture"
type: "theorem"
title: "not Qi h_lambda degree four conjecture"
status: "proved"
tags: ["application-candidate", "complete-monotonicity", "degree", "polygamma", "proved", "qi", "refutation", "theorem"]
parents: ["T-Special-function-normal-form-calculus-principle", "T-Qi-hlambda-x4-source-range-not-CM"]
refs: ["librarian/audits/LA-20260531T000800-qi-hlambda-degree-refutation.json", "oracle/responses/ORACLE-OS-20260531T-qi-hlambda-degree-refutation-oracle-response.md", "raw/student/20260531T000800-qi-hlambda-degree-refutation.md", "wiki/notes/frontier-qi-hlambda-degree-refutation.md"]
---

# Theorem: not Qi h_lambda degree four conjecture

## Statement

not(For \(\Psi(x)=[\psi'(x)]^2+\psi''(x)\) and \(h_\lambda(x)=\Psi(x)-(x^2+\lambda x+12)/(12x^4(x+1)^2)\), \(\deg_x^{\rm cm}h_\lambda=\deg_x^{\rm cm}(-h_\mu)=4\) if and only if \(\lambda\le0\) and \(\mu\ge4\).)

## Dependencies

- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]
- [[wiki/nodes/T-Qi-hlambda-x4-source-range-not-CM|Qi h_lambda degree four transforms are not completely monotone on source ranges]]

## Proof and provenance references

- `librarian/audits/LA-20260531T000800-qi-hlambda-degree-refutation.json`
- `oracle/responses/ORACLE-OS-20260531T-qi-hlambda-degree-refutation-oracle-response.md`
- `raw/student/20260531T000800-qi-hlambda-degree-refutation.md`
- `wiki/notes/frontier-qi-hlambda-degree-refutation.md`

## Proof

A completely monotone function must be nonincreasing, so its first derivative cannot be positive at any point.

Use the recurrence expansions at \(x=0^+\):
\[
\psi'(x)=\frac1{x^2}+\zeta(2)-2\zeta(3)x+3\zeta(4)x^2+O(x^3),
\]
and
\[
\psi''(x)=-\frac2{x^3}-2\zeta(3)+6\zeta(4)x+O(x^2).
\]
Therefore
\[
\Psi(x)
=\frac1{x^4}-\frac2{x^3}+\frac{\pi^2}{3x^2}
-\frac{4\zeta(3)}x+O(1).
\]
Also
\[
\frac{x^2+\lambda x+12}{12x^4(1+x)^2}
=\frac1{x^4}+\left(\frac{\lambda}{12}-2\right)\frac1{x^3}
+\left(\frac{37}{12}-\frac{\lambda}{6}\right)\frac1{x^2}
+O(x^{-1}).
\]
Subtracting gives
\[
h_\lambda(x)
=-\frac{\lambda}{12x^3}
+\left(\frac{\lambda}{6}+\frac{\pi^2}{3}-\frac{37}{12}\right)\frac1{x^2}
+O(x^{-1}).
\]

If \(\lambda<0\), then
\[
x^4h_\lambda(x)=-\frac{\lambda}{12}x+O(x^2),
\]
so
\[
\frac{d}{dx}\bigl[x^4h_\lambda(x)\bigr]
=-\frac{\lambda}{12}+O(x)>0
\]
for all sufficiently small \(x>0\). Hence \(x^4h_\lambda\) is not completely monotone.

If \(\lambda=0\), then
\[
x^4h_0(x)
=\left(\frac{\pi^2}{3}-\frac{37}{12}\right)x^2+O(x^3).
\]
Since \(4\pi^2>37\), the leading coefficient is positive, and
\[
\frac{d}{dx}\bigl[x^4h_0(x)\bigr]
=2\left(\frac{\pi^2}{3}-\frac{37}{12}\right)x+O(x^2)>0
\]
for all sufficiently small \(x>0\). Hence \(x^4h_0\) is not completely monotone.

Similarly, for \(\mu\ge4\),
\[
x^4(-h_\mu(x))=\frac{\mu}{12}x+O(x^2),
\]
so
\[
\frac{d}{dx}\bigl[x^4(-h_\mu(x))\bigr]
=\frac{\mu}{12}+O(x)>0
\]
for all sufficiently small \(x>0\). Hence \(x^4(-h_\mu)\) is not completely monotone for every \(\mu\ge4\).

Thus the degree-four transforms required by Qi's conjecture are not completely monotone on the conjectured source ranges. The conjecture in Remark 7.4 is false.

_Proof source: `raw/student/20260531T000800-qi-hlambda-degree-refutation.md`._

## Tags

`application-candidate`, `complete-monotonicity`, `degree`, `polygamma`, `proved`, `qi`, `refutation`, `theorem`
