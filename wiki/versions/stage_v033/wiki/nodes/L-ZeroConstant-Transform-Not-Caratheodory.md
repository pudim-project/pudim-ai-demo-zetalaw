---
id: "L-ZeroConstant-Transform-Not-Caratheodory"
type: "lemma"
title: "Zero-constant transforms cannot enter the normalized Caratheodory class"
status: "proved"
tags: ["analytic-functions", "bridge-lemma", "caratheodory", "coefficient-extraction", "endpoint-obstruction", "lemma", "normalization-obstruction", "primitive-growth", "proved", "true"]
parents: ["D-Analytic-Unit-Disk-Classes", "D-Caratheodory-Class-Normalization", "D-Determinant-triangular-compression-language", "D-Endpoint-obstruction-certificate-language"]
refs: ["librarian/audits/LA-20260622T1802-sangal-komatu-literal-strict-app.json", "oracle/responses/OS-20260622T1801Z-sangal-komatu-literal-student-repair-oracle-response.md", "raw/student/20260622T1802-sangal-komatu-literal-refutation.md"]
---

# Lemma: Zero-constant transforms cannot enter the normalized Caratheodory class

## Statement

Let \(T\) be a transform on \(\mathcal A\) such that \((Tf)(0)=0\) for every \(f\in\mathcal A\). Then \(Tf\notin\mathcal P\) for every \(f\in\mathcal A\), where \(\mathcal P\) is the normalized Caratheodory class. If the target class is interpreted as strict positive real part, the same conclusion holds because \(\operatorname{Re}(Tf)(0)=0\) is not strictly positive.

## Dependencies

- [[wiki/nodes/D-Analytic-Unit-Disk-Classes|Analytic unit-disk normalization classes]]
- [[wiki/nodes/D-Caratheodory-Class-Normalization|Caratheodory class normalization]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]

## Proof and provenance references

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

## Tags

`analytic-functions`, `bridge-lemma`, `caratheodory`, `coefficient-extraction`, `endpoint-obstruction`, `lemma`, `normalization-obstruction`, `primitive-growth`, `proved`, `true`
