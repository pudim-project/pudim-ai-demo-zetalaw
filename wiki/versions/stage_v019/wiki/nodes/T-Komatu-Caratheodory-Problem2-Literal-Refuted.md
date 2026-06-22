---
id: "T-Komatu-Caratheodory-Problem2-Literal-Refuted"
type: "theorem"
title: "Sangal-Swaminathan printed Komatu Problem 2 has empty literal parameter set"
status: "proved"
tags: ["app-0090-candidate", "app-candidate", "caratheodory", "coefficient-extraction", "hadamard-product", "komatu-operator", "negative-answer", "normalization-obstruction", "primitive-growth", "proved", "sangal-swaminathan", "source-open-solved", "theorem", "true"]
parents: ["O-SangalSwaminathan-Komatu-Caratheodory-Problem2-Literal-source-gate", "D-SangalSwaminathan-Komatu-Problem2-Literal", "L-ZeroConstant-Transform-Not-Caratheodory", "T-Exact-finite-certificate-verification-principle"]
refs: ["librarian/audits/LA-20260622T1754-sangal-komatu-literal-first-contact.json", "librarian/audits/LA-20260622T1802-sangal-komatu-literal-strict-app.json", "oracle/responses/OS-20260622T1801Z-sangal-komatu-literal-student-repair-oracle-response.md", "raw/student/20260622T1802-sangal-komatu-literal-refutation.md"]
---

# Theorem: Sangal-Swaminathan printed Komatu Problem 2 has empty literal parameter set

## Statement

The literal printed Sangal--Swaminathan Problem 2 has a negative answer. Under the source-gated reading in which \(f\in\mathcal A\), \(L[\eta]f(z)=\phi_{p,q}(a,b;z)*f(z)\), and the target is the normalized Caratheodory class, there are no admissible parameters \(p,q,a,b\) for which \(L[\eta]f\) itself belongs to the Caratheodory class for every \(f\in\mathcal A\).

## Dependencies

- [[wiki/nodes/O-SangalSwaminathan-Komatu-Caratheodory-Problem2-Literal-source-gate|Sangal-Swaminathan printed Komatu Caratheodory Problem 2 literal source gate]]
- [[wiki/nodes/D-SangalSwaminathan-Komatu-Problem2-Literal|Sangal-Swaminathan printed Komatu Problem 2 vocabulary]]
- [[wiki/nodes/L-ZeroConstant-Transform-Not-Caratheodory|Zero-constant transforms cannot enter the normalized Caratheodory class]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `librarian/audits/LA-20260622T1754-sangal-komatu-literal-first-contact.json`
- `librarian/audits/LA-20260622T1802-sangal-komatu-literal-strict-app.json`
- `oracle/responses/OS-20260622T1801Z-sangal-komatu-literal-student-repair-oracle-response.md`
- `raw/student/20260622T1802-sangal-komatu-literal-refutation.md`

## Proof

This proof addresses only the literal printed Sangal--Swaminathan Problem 2:
find conditions on \(p,q,a,b\) such that the printed operator
\[
L[\eta]f(z)=\phi_{p,q}(a,b;z)*f(z)
\]
itself belongs to the Caratheodory class for \(f\in\mathcal A\).

It does not address any corrected or intended variant such as
\[
1+L[\eta]f(z)/z,\qquad L[\eta]f(z)/z,
\]
kernel membership for \(\Phi_{p,q}\), or normalized partial sums.

Let
\[
\mathcal A=\{f(z)=z+\sum_{n\ge 2}a_nz^n\}
\]
and let
\[
\mathcal P=\{p(z)=1+\sum_{n\ge 1}c_nz^n:\operatorname{Re}p(z)>0
\text{ on }\mathbb D\}.
\]
If a transform \(T\) maps every \(f\in\mathcal A\) to an analytic function
with constant term \(0\), then \(Tf\notin\mathcal P\) for every
\(f\in\mathcal A\). Indeed, membership in \(\mathcal P\) requires
\((Tf)(0)=1\).

The same zero-origin argument also rules out the unnormalized strict
positive-real class \(\operatorname{Re}g>0\), since then
\(\operatorname{Re}(Tf)(0)=0\) is not strictly positive.

_Proof source: `raw/student/20260622T1802-sangal-komatu-literal-refutation.md`._

## Do not claim

- Do not claim a solution to \(1+L[\eta]f/z\), \(L[\eta]f/z\), kernel Caratheodory membership, or normalized partial sums.
- Do not public-stage without explicit user request.

## Tags

`app-0090-candidate`, `app-candidate`, `caratheodory`, `coefficient-extraction`, `hadamard-product`, `komatu-operator`, `negative-answer`, `normalization-obstruction`, `primitive-growth`, `proved`, `sangal-swaminathan`, `source-open-solved`, `theorem`, `true`
