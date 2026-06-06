---
id: "T-Baricz-AA-zero-balanced-concavity-source-subproblem"
type: "theorem"
title: "Baricz zero balanced hypergeometric arithmetic arithmetic concavity source subproblem"
status: "proved"
tags: ["arithmetic-arithmetic", "baricz", "hypergeometric", "means", "proved", "source-open-solved-scoped", "source-subproblem", "source-subproblem-solved", "theorem"]
parents: ["T-Pointwise-obstruction-certificate-principle"]
refs: ["librarian/audits/LA-20260605T-baricz-AA-concavity-threshold-strict-app.json", "oracle/direct/OFC-20260605T-baricz-AA-concavity-source-response.md", "raw/oracle/RO-OFC-20260605T-baricz-AA-concavity-source.json", "raw/scout/sources/topics-special-functions-iii-1209.1696/tsf320130325.tex", "raw/student/20260605T-baricz-AA-concavity-threshold.md", "wiki/notes/frontier-baricz-hypergeometric-means.md"]
---

# Theorem: Baricz zero balanced hypergeometric arithmetic arithmetic concavity source subproblem

## Statement

In Baricz's hypergeometric bivariate-means open problem, decide the arithmetic/arithmetic slice: for which \(c>0\) does \((F_{a_1}(r)+F_{a_2}(r))/2\le F_{(a_1+a_2)/2}(r)\) hold for all \(a_1,a_2\in(0,c)\) and \(r\in(0,1)\), where \(F_a(r)={}_2F_1(a,c-a;c;r)\)?

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260605T-baricz-AA-concavity-threshold-strict-app.json`
- `oracle/direct/OFC-20260605T-baricz-AA-concavity-source-response.md`
- `raw/oracle/RO-OFC-20260605T-baricz-AA-concavity-source.json`
- `raw/scout/sources/topics-special-functions-iii-1209.1696/tsf320130325.tex`
- `raw/student/20260605T-baricz-AA-concavity-threshold.md`
- `wiki/notes/frontier-baricz-hypergeometric-means.md`

## Proof

For \(c>0\), set
\[
F_a(r)={}_2F_1(a,c-a;c;r),\qquad 0<a<c,\quad 0<r<1.
\]
The Baricz arithmetic/arithmetic source slice asks when
\[
\frac{F_{a_1}(r)+F_{a_2}(r)}2\le F_{(a_1+a_2)/2}(r)
\]
holds for all \(a_1,a_2\in(0,c)\) and all \(r\in(0,1)\).

The answer is exactly \(0<c\le1\).

The existing local node the Hypergeometric Fa geometric mean logconvex slice imports Baricz's theorem:
\[
\sqrt{F_{a_1}(r)F_{a_2}(r)}
\le
\frac{F_{a_1}(r)+F_{a_2}(r)}2
\le
F_{(a_1+a_2)/2}(r)
\]
for \(0<c\le1\), \(a_1,a_2\in(0,c)\), and \(0<r<1\). This proves the A/A inequality on that range.

Fix \(c>1\). For \(0<r<1\),
\[
F_a(r)=\sum_{k=0}^{\infty}
\frac{(a)_k(c-a)_k}{(c)_k}\frac{r^k}{k!}.
\]
For \(k\ge1\), as \(a\to0\),
\[
(a)_k=a(k-1)!\left(1+aH_{k-1}+O(a^2)\right)
\]
and
\[
\frac{(c-a)_k}{(c)_k}
=
1-a\sum_{j=0}^{k-1}\frac1{c+j}+O(a^2).
\]
Hence
\[
\frac{(a)_k(c-a)_k}{(c)_k k!}
=
\frac ak+\frac{a^2}{k}
\left(
H_{k-1}-\sum_{j=0}^{k-1}\frac1{c+j}
\right)
 +O(a^3).
\]
For fixed \(r<1\), normal convergence of the differentiated hypergeometric series justifies termwise expansion, so
\[
F_a(r)=1+aL(r)+a^2M_c(r)+O(a^3),
\]
where
\[
L(r)=\sum_{k\ge1}\frac{r^k}{k}=-\log(1-r)
\]
and
\[
M_c(r)=
\sum_{k\ge1}
\left(
H_{k-1}-\sum_{j=0}^{k-1}\frac1{c+j}
\right)\frac{r^k}{k}.
\]
The bracket is
\[
B_{c,k}
=
\psi(k)+\gamma-\psi(c+k)+\psi(c),
\]
so
\[
B_{c,k}\to \gamma+\psi(c).
\]
Because \(c>1\), \(\psi(c)>\psi(1)=-\gamma\), and therefore \(\gamma+\psi(c)>0\). Thus \(B_{c,k}\ge\eta>0\) for all sufficiently large \(k\), and
\[
M_c(r)\to+\infty\qquad (r\uparrow1).
\]
Choose \(r_0\in(0,1)\) with \(M_c(r_0)>0\). Then
\[
\partial_a^2F_a(r_0)\to 2M_c(r_0)>0
\qquad (a\downarrow0).
\]
For some sufficiently small interior \(a_0\in(0,c)\), \(\partial_a^2F_{a_0}(r_0)>0\). By continuity, \(\partial_a^2F_a(r_0)>0\) on a small interval around \(a_0\). Taking \(h>0\) small enough that \(a_0\pm h\in(0,c)\), Taylor's theorem gives
\[
\frac{F_{a_0-h}(r_0)+F_{a_0+h}(r_0)}2>F_{a_0}(r_0).
\]
Since \(a_0=((a_0-h)+(a_0+h))/2\), the A/A inequality fails.

Therefore the source A/A inequality holds uniformly if and only if \(0<c\le1\).

_Proof source: `raw/student/20260605T-baricz-AA-concavity-threshold.md`._

## Tags

`arithmetic-arithmetic`, `baricz`, `hypergeometric`, `means`, `proved`, `source-open-solved-scoped`, `source-subproblem`, `source-subproblem-solved`, `theorem`
