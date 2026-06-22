---
id: "B-Mohle-CountableSimplex-TruncationClosure"
type: "lemma"
title: "Countable simplex truncation closure"
status: "proved"
tags: ["bridge-lemma", "countable-simplex", "dominated-convergence", "finite-support-reduction", "lemma", "primitive-support", "proved", "true"]
parents: ["B-Mohle-BinomialCollisionKernel-Integral", "D-Mohle-BlockCounting-Problem63-Language", "T-Exact-finite-certificate-verification-principle"]
refs: ["librarian/audits/LA-20260622T1100-mohle-problem63-strict-app.json", "raw/student/20260622T1058-mohle-problem63-finite-kernel.md"]
---

# Lemma: Countable simplex truncation closure

## Statement

For fixed \(n\), the Mohle source formula for \(p_n(u)\) is the limit of its finite-support truncations on \(\Delta\). The one-coordinate terms are dominated by multiples of \(u_i\), and the ordered-pair collision term is absolutely dominated by \(n(n-1)\sum_{i\ne j}u_i u_j\).

## Dependencies

- [[wiki/nodes/B-Mohle-BinomialCollisionKernel-Integral|Binomial collision kernel integral]]
- [[wiki/nodes/D-Mohle-BlockCounting-Problem63-Language|Mohle block-counting Problem 6.3 language]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `librarian/audits/LA-20260622T1100-mohle-problem63-strict-app.json`
- `raw/student/20260622T1058-mohle-problem63-finite-kernel.md`

## Proof

The case \(n=1\) is source-recorded:
\[
p_1(u)=|u|(1-|u|)\ge0.
\]
Assume \(n\ge2\). First suppose \(u\) has finite support. Set
\[
s=|u|,\qquad
A=\sum_i\bigl(1-(1-u_i)^n\bigr),\qquad
B=\sum_i u_i(1-u_i)^{n-1}.
\]
The source formula for \(p_n\) is
\[
p_n(u)=\frac{n-1}{n^2}A-\frac{s(1-s)}n+\frac{2(1-s)}nB
+\frac1{n^2}\sum_{i\ne j}\Bigl((1-u_i)^n+(1-u_j)^n-1-(1-u_i-u_j)^n\Bigr),
\]
where the off-diagonal sum is ordered.

For \(0\le x,y\) with \(x+y\le1\),
\[
(1-x)^n+(1-y)^n-1-(1-x-y)^n
=-n(n-1)\int_0^x\int_0^y(1-r-t)^{n-2}\,dr\,dt.
\]
Also
\[
1-(1-x)^n=n\int_0^x(1-t)^{n-1}\,dt.
\]
Define
\[
S=\sum_i\int_0^{u_i}(1-t)^{n-1}\,dt
\]
and
\[
T=\sum_{i\ne j}\int_0^{u_i}\int_0^{u_j}(1-t-r)^{n-2}\,dr\,dt .
\]
Then
\[
p_n(u)=\frac{n-1}{n}(S-T)+\frac{1-s}{n}(2B-s).
\]

For fixed \(i\) and \(0\le t\le u_i\),
\[
\sum_{j\ne i}\int_0^{u_j}(1-t-r)^{n-2}\,dr
\le (s-u_i)(1-t)^{n-2}.
\]
Indeed \(t+r\le u_i+u_j\le s\le1\), so the integrand is nonnegative, and \(r\ge0\) gives \(1-t-r\le1-t\). Hence
\[
\begin{aligned}
S-T
&\ge \sum_i\int_0^{u_i}
\left((1-t)^{n-1}-(s-u_i)(1-t)^{n-2}\right)\,dt\\
&=\sum_i\int_0^{u_i}(1-t)^{n-2}(1-t-s+u_i)\,dt\\
&=\sum_i\int_0^{u_i}(1-t)^{n-2}\bigl((1-s)+(u_i-t)\bigr)\,dt\\
&\ge \frac{1-s}{n-1}\sum_i\bigl(1-(1-u_i)^{n-1}\bigr).
\end{aligned}
\]
Substituting this into the expression for \(p_n\) gives
\[
p_n(u)\ge
\frac{1-s}{n}\sum_i
\left(1-(1-u_i)^{n-1}+2u_i(1-u_i)^{n-1}-u_i\right).
\]
For each summand set \(q=1-u_i\). The bracket is
\[
q+q^{n-1}-2q^n
=q\left(1-q^{n-2}(2q-1)\right).
\]
If \(q\le1/2\), the factor in parentheses is at least \(1\). If \(q\ge1/2\), then \(0\le q^{n-2}(2q-1)\le1\). Thus every summand is nonnegative, and since \(1-s\ge0\), \(p_n(u)\ge0\) for finitely supported \(u\).

For countably supported \(u\), let \(u^{(m)}=(u_1,\ldots,u_m,0,0,\ldots)\). The one-coordinate sums converge because
\[
0\le 1-(1-u_i)^n\le n u_i,\qquad 0\le u_i(1-u_i)^{n-1}\le u_i.
\]
The ordered-pair term is absolutely dominated by
\[
n(n-1)\sum_{i\ne j}u_i u_j<\infty,
\]
using the double-integral identity and the bound \((1-t-r)^{n-2}\le1\). Therefore \(p_n(u^{(m)})\to p_n(u)\). Passing the finite-support inequality to the limit proves \(p_n(u)\ge0\) for all \(u\in\Delta\).

The reusable bridge is a finite-simplex ordered-pair kernel certificate: negative pair-collision terms can be dominated by one-body integrals whenever the simplex constraint \(s\le1\) leaves a residual factor \(1-s\). This is distinct from the source theorem and can be reused for finite occupancy and concentration expressions built from \((1-x)^n\) and \((1-x-y)^n\).

The proof solves the exact source-open Problem 6.3 affirmatively. This is a strict private APP candidate APP-0084, pending only future public staging requested by the user.

_Proof source: `raw/student/20260622T1058-mohle-problem63-finite-kernel.md`._

## Tags

`bridge-lemma`, `countable-simplex`, `dominated-convergence`, `finite-support-reduction`, `lemma`, `primitive-support`, `proved`, `true`
