---
id: "T-positive-Mellin-moment-logconvexity-principle"
type: "theorem"
title: "T-positive-Mellin-moment-logconvexity-principle"
status: "proved"
tags: ["application-bridge", "holder", "holder-inequality", "log-convexity", "mellin-transform", "primitive", "principle", "proved", "theorem"]
parents: ["D-Laplace-kernel-and-tilted-moment-language", "D-Mellin-Planck-partition-function"]
refs: ["raw/student/20260605T-bridge-sroysang-holder.md"]
---

# Theorem: T-positive-Mellin-moment-logconvexity-principle

## Statement

If \(M(s)=\int_0^\infty t^{s}\,d\mu(t)\) is finite on an interval for a positive measure \(\mu\), then \(s\mapsto M(s)\) is log-convex on that interval. Equivalently, weighted Holder inequalities hold for positive Mellin moments.

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/D-Mellin-Planck-partition-function|Mellin-Planck partition function]]

## Proof and provenance references

- `raw/student/20260605T-bridge-sroysang-holder.md`

## Proof

Let \(\mu\) be a positive measure and let
\[
M(s)=\int_0^\infty t^s\,d\mu(t)
\]
be finite on an interval. Then \(s\mapsto M(s)\) is log-convex on that interval. Equivalently, for \(\lambda_i\ge0\), \(\sum_i\lambda_i=1\), and admissible \(s_i\),
\[
M\left(\sum_i\lambda_i s_i\right)\le \prod_i M(s_i)^{\lambda_i}.
\]

Indeed,
\[
t^{\sum_i\lambda_i s_i}=\prod_i (t^{s_i})^{\lambda_i}.
\]
Holder's inequality applied to the positive functions \(t^{s_i}\) with weights \(\lambda_i\) gives the displayed inequality. Taking logarithms gives convexity of \(\log M\).

_Proof source: `raw/student/20260605T-bridge-sroysang-holder.md`._

## Tags

`application-bridge`, `holder`, `holder-inequality`, `log-convexity`, `mellin-transform`, `primitive`, `principle`, `proved`, `theorem`
