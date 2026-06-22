---
id: "T-Dual-certificate-extremal-l1-norm-principle"
type: "theorem"
title: "Finite-dimensional dual certificate for exact l1 representation norm"
status: "proved"
tags: ["application-bridge", "dual-certificate", "extremal-norm", "finite-dimensional-duality", "primitive", "principle", "proof-step", "proved", "structural-tool", "theorem"]
parents: ["D-Finite-dimensional-l1-dual-certificate-language"]
refs: ["raw/student/20260605T-bridge-dual-certificate-extremal-norm.md", "wiki/definitions/finite-dimensional-l1-dual-certificate-language.md"]
---

# Theorem: Finite-dimensional dual certificate for exact l1 representation norm

## Statement

In the finite-dimensional \(\ell^1\) dual-certificate setting, if \(v\) has a primal representation of norm \(M\) and a dual certificate \(\Lambda\) with \(\Lambda(v)=M\), then the exact minimal \(\ell^1\)-representation norm of \(v\) by the coordinate atoms is \(M\).

## Dependencies

- [[wiki/nodes/D-Finite-dimensional-l1-dual-certificate-language|finite dimensional l1 primal representation coordinate atom dual linear functional certificate language]]

## Proof and provenance references

- `raw/student/20260605T-bridge-dual-certificate-extremal-norm.md`
- `wiki/definitions/finite-dimensional-l1-dual-certificate-language.md`

## Proof

Let \(V\) be a real vector space, let \(\mathcal A\subset V\) be a finite coordinate family, and let \(v\in V\). Suppose there is a representation
\[
v=\sum_{a\in\mathcal A} c_a a,
\qquad
\sum_{a\in\mathcal A}|c_a|=M,
\]
and a linear functional \(\Lambda:V\to\mathbb R\) such that
\[
\Lambda(v)=M,
\qquad
|\Lambda(a)|\le 1\quad(a\in\mathcal A).
\]
Then the least \(\ell^1\)-coefficient norm of a representation of \(v\) by elements of \(\mathcal A\) is exactly \(M\).

For any other representation \(v=\sum_{a\in\mathcal A} b_a a\), linearity and the dual bound give
\[
M=\Lambda(v)=\sum_{a\in\mathcal A}b_a\Lambda(a)
\le \sum_{a\in\mathcal A}|b_a|\,|\Lambda(a)|
\le \sum_{a\in\mathcal A}|b_a|.
\]
Thus every representation has norm at least \(M\). The displayed primal representation has norm \(M\), so the minimum is \(M\).

_Proof source: `raw/student/20260605T-bridge-dual-certificate-extremal-norm.md`._

## Tags

`application-bridge`, `dual-certificate`, `extremal-norm`, `finite-dimensional-duality`, `primitive`, `principle`, `proof-step`, `proved`, `structural-tool`, `theorem`
