---
id: "T-Tao-Erdos385-restricted-semiprime-gap-implication"
type: "theorem"
title: "T-Tao-Erdos385-restricted-semiprime-gap-implication"
status: "proved"
tags: ["proved", "theorem"]
parents: ["T-Erdos385-zeta-law-semiprime-parity-shadow", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["private Oracle response", "private proof note", "wiki/notes/tao-erdos385-semiprime-gap-implication.md"]
---

# Theorem: T-Tao-Erdos385-restricted-semiprime-gap-implication

## Statement

Fix 2<u<3. If restricted semiprimes m=pq in [X,2X], with p,q in [X^{1/u},(2X)^{1-1/u}], have maximal gaps G(X)=o(X^{1/u}), then F(n)-n -> infinity for F(n)=max_{m<n, composite}(m+p(m)). In particular F(n)>n eventually.

## Scope

- Conditional implication formalizing Tao's reduction; does not prove the restricted semiprime-gap hypothesis.

## Dependencies

- [[wiki/nodes/T-Erdos385-zeta-law-semiprime-parity-shadow|Erdos 385 zeta-law semiprime parity shadow]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`
- `wiki/notes/tao-erdos385-semiprime-gap-implication.md`

## Proof

Let \(n\) be large and set
\[
X=\frac n2.
\]
Then
\[
[X,2X]=\left[\frac n2,n\right].
\]
To avoid the endpoint issue that a closed interval might return \(m=n\), use the interior interval
\[
I_n=[n-2G(X),\,n-G(X)].
\]
Since \(G(X)=o(X^{1/u})\) and \(1/u<1\), we have \(G(X)=o(X)\), so for all sufficiently large \(n\),
\[
n-2G(X)\ge X.
\]
Thus
\[
I_n\subseteq [X,2X].
\]

By the maximal-gap hypothesis, \(I_n\) contains a restricted semiprime
\[
m=pq.
\]
Then \(m<n\), \(m\) is composite, and
\[
n-m\le 2G(X).
\]
Also, since \(m\) is restricted,
\[
p(m)=p\ge X^{1/u}.
\]
Therefore
\[
m+p(m)-n
=
p(m)-(n-m)
\ge
X^{1/u}-2G(X).
\]
Because
\[
G(X)=o(X^{1/u}),
\]
we have
\[
X^{1/u}-2G(X)\to\infty.
\]

Since \(F(n)\) maximizes \(r+p(r)\) over composite \(r<n\), and \(m<n\) is admissible,
\[
F(n)\ge m+p(m).
\]
Hence
\[
F(n)-n
\ge
\left(\frac n2\right)^{1/u}
-2G\left(\frac n2\right)
\to\infty.
\]
This proves the theorem.

The proof uses only the lower factor bound
\[
p(m)\ge X^{1/u}.
\]
Thus the same implication holds if the restricted semiprime hypothesis is replaced by any hypothesis guaranteeing a composite \(m<n\) in the interval with
\[
p(m)\ge cX^{1/u}
\]
for some fixed \(c>0\), provided the maximal gap still satisfies
\[
G(X)=o(X^{1/u}).
\]
Then
\[
F(n)-n\ge cX^{1/u}-O(G(X))\to\infty.
\]

This formalizes the source reduction Tao describes. It does not prove the actual restricted semiprime-gap estimate, and therefore does not solve Erdos problem #385 unconditionally.

_Proof source: `private proof note`._

## Tags

`proved`, `theorem`
