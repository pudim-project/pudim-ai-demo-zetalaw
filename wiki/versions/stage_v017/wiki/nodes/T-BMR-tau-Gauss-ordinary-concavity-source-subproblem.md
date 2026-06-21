---
id: "T-BMR-tau-Gauss-ordinary-concavity-source-subproblem"
type: "theorem"
title: "BMR tau Gauss ordinary concavity source stated subproblem"
status: "proved"
tags: ["app-0048-candidate", "application-candidate", "bmr", "ordinary-concavity", "proved", "source-open-solved-scoped", "source-solving-tool", "source-subproblem-solved", "tau-hypergeometric", "theorem"]
parents: ["T-Pointwise-obstruction-certificate-principle"]
refs: ["private librarian audit", "oracle/direct/OFC-20260605T-bmr-concavity-source-response.md", "oracle/direct/OS-20260605T-bmr-tau-global-current-response.md", "private Oracle audit", "private Oracle audit", "private scout artifact", "private proof note", "wiki/notes/frontier-bmr-tau-hypergeometric-midpoint.md"]
---

# Theorem: BMR tau Gauss ordinary concavity source stated subproblem

## Statement

In the Bansal--Mehrez--Raina final open problem, decide the ordinary-concavity alternative: whether \(a\mapsto {}_2\phi^\tau_1(a,c-a;c;z)\) is concave on \((0,c)\) for the source parameter range.

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `private librarian audit`
- `oracle/direct/OFC-20260605T-bmr-concavity-source-response.md`
- `oracle/direct/OS-20260605T-bmr-tau-global-current-response.md`
- `private Oracle audit`
- `private Oracle audit`
- `private scout artifact`
- `private proof note`
- `wiki/notes/frontier-bmr-tau-hypergeometric-midpoint.md`

## Proof

For \(0<z<1\), define probability weights
\[
w_k(a,z)=\frac{A_k(a)z^k/k!}{F(a,z)}.
\]
Let
\[
g_k(a)=\partial_a\log A_k(a),
\qquad
h_k(a)=\partial_a^2\log A_k(a).
\]
Then direct differentiation of the log-sum gives
\[
\partial_a^2\log F(a,z)
=
\sum_{k\ge0}w_k(a,z)h_k(a)
+\operatorname{Var}_{w(a,z)}(g_k(a)).
\]
Thus global log-concavity is equivalent to the variance-domination inequality
\[
\operatorname{Var}_{w(a,z)}(g_k(a))
\le
\sum_{k\ge0}w_k(a,z)(-h_k(a))
\]
for all \(0<a<c\), \(c,\tau>0\), and \(0<z<1\). This is the sharp remaining gate; coefficientwise log-concavity alone is insufficient.

Take the classical subcase
\[
c=2,\qquad \tau=1,\qquad z=1-e^{-4}.
\]
Then
\[
F(a,z)=
\sum_{k=0}^{\infty}
\frac{(a)_k(2-a)_k}{(2)_k}\frac{z^k}{k!}.
\]
For \(k\ge1\), as \(a\downarrow0\),
\[
\frac{(a)_k(2-a)_k}{(2)_k\,k!}
=
\frac{a}{k}
+a^2\left(
\frac1k-\frac1{k^2}-\frac1{k(k+1)}
\right)+O(a^3),
\]
with locally uniform summability for fixed \(0<z<1\). Hence
\[
F(a,z)=1+aL(z)+a^2M(z)+O(a^3),
\]
where
\[
L(z)=\sum_{k\ge1}\frac{z^k}{k}=-\log(1-z)
\]
and
\[
M(z)=
\sum_{k\ge1}z^k
\left(
\frac1k-\frac1{k^2}-\frac1{k(k+1)}
\right)
=
\frac{L(z)}{z}-\operatorname{Li}_2(z)-1.
\]
For \(z=1-e^{-4}\), \(L(z)=4\), \(L(z)/z>4\), and \(\operatorname{Li}_2(z)<\pi^2/6<2\). Therefore
\[
M(z)>4-2-1=1>0.
\]
It follows that
\[
F''(a,z)\to2M(z)>0
\qquad(a\downarrow0),
\]
so \(F''(a,z)>0\) for all sufficiently small \(a>0\). Therefore the source function is not concave in \(a\) in general.

_Proof source: `private proof note`._

## Tags

`app-0048-candidate`, `application-candidate`, `bmr`, `ordinary-concavity`, `proved`, `source-open-solved-scoped`, `source-solving-tool`, `source-subproblem-solved`, `tau-hypergeometric`, `theorem`
