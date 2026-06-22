---
id: "T-Qi-LogConcaveConvolution-StrictImprovement-Example"
type: "example"
title: "Qi log-concave convolution strict improvement example"
status: "proved"
tags: ["convolution", "example", "log-concavity", "proved", "qi", "strictness-witness", "true"]
parents: ["T-Qi-LogConcaveConvolution-VertexChord-LowerBound"]
refs: ["librarian/audits/LA-20260613T0405-qi-logconcave-convolution-strict-app.json", "oracle/responses/OS-20260613Tqi-logconcave-convolution-vertex-bound-oracle-response.md", "raw/student/20260613T0400-qi-logconcave-convolution-vertex-bound.md"]
---

# Example: Qi log-concave convolution strict improvement example

## Statement

For \(n=2\), \(f_1(t)=e^t\), and \(f_2(t)=1\), the vertex-chord lower bound equals the convolution \(e^x-1\), while Qi's baseline bound is \(xe^{x/2}\). Thus the new max-bound is strictly larger than the baseline for every \(x>0\).

## Dependencies

- [[wiki/nodes/T-Qi-LogConcaveConvolution-VertexChord-LowerBound|Qi log-concave convolution vertex-chord lower bound]]

## Proof and provenance references

- `librarian/audits/LA-20260613T0405-qi-logconcave-convolution-strict-app.json`
- `oracle/responses/OS-20260613Tqi-logconcave-convolution-vertex-bound-oracle-response.md`
- `raw/student/20260613T0400-qi-logconcave-convolution-vertex-bound.md`

## Proof

status: strict private APP candidate; registry pending

Let \(n\ge2\), \(x>0\), and let \(f_i:[0,x]\to(0,\infty)\) be logarithmically concave. Write
\[
\phi_i(u)=\log f_i(u)
\]
and
\[
\Delta_{n-1}=\{\theta_i\ge0:\theta_1+\cdots+\theta_n=1\}.
\]
For \(1\le k\le n\), define
\[
A_k(x)=\phi_k(x)+\sum_{j\ne k}\phi_j(0)
=\log\left(f_k(x)\prod_{j\ne k}f_j(0)\right).
\]
Set
\[
B_{\rm VC}(x)=x^{n-1}\int_{\Delta_{n-1}}
\exp\left(\sum_{k=1}^n\theta_kA_k(x)\right)\,d\theta,
\]
where \(d\theta\) is the standard \((n-1)\)-dimensional simplex measure.

The convolution has the simplex form
\[
(f_1*\cdots*f_n)(x)
=x^{n-1}\int_{\Delta_{n-1}}\prod_{i=1}^n f_i(x\theta_i)\,d\theta.
\]
Since each \(\phi_i\) is concave,
\[
\phi_i(x\theta_i)\ge (1-\theta_i)\phi_i(0)+\theta_i\phi_i(x).
\]
Summing over \(i\) gives
\[
\sum_i\phi_i(x\theta_i)\ge\sum_i\theta_i A_i(x).
\]
Exponentiating and integrating proves
\[
(f_1*\cdots*f_n)(x)\ge B_{\rm VC}(x).
\]

This answers the literal source question by giving a valid stronger lower bound under logarithmic concavity. It does not claim optimality or characterize the largest possible lower bound. If a future audit interprets the source as asking for an optimal extremal bound, this result should be demoted to a bridge theorem.

_Proof source: `raw/student/20260613T0400-qi-logconcave-convolution-vertex-bound.md`._

## Tags

`convolution`, `example`, `log-concavity`, `proved`, `qi`, `strictness-witness`, `true`
