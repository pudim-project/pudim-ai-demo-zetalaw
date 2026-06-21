---
id: "T-Sroysang-generalized-Holder-zeta-inequality"
type: "theorem"
title: "T-Sroysang-generalized-Holder-zeta-inequality"
status: "proved"
tags: ["application-bridge", "holder", "log-convexity", "mellin-transform", "proved", "source-open-solved", "theorem", "zeta"]
parents: ["T-positive-Mellin-moment-logconvexity-principle"]
refs: ["private proof note", "theory/latest/THEORY.tex#thm:sroysang-holder"]
---

# Theorem: T-Sroysang-generalized-Holder-zeta-inequality

## Statement

Sroysang's generalized Holder inequality for the Riemann zeta function holds: the weighted Holder inequality for \(M(s)=\Gamma(s)\zeta(s)\) implies the stated upper bound for \(\zeta(T)\) after division by \(\Gamma(T)\).

## Dependencies

- [[wiki/nodes/T-positive-Mellin-moment-logconvexity-principle|T-positive-Mellin-moment-logconvexity-principle]]

## Proof and provenance references

- `private proof note`
- `theory/latest/THEORY.tex#thm:sroysang-holder`

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

_Proof source: `private proof note`._

## Tags

`application-bridge`, `holder`, `log-convexity`, `mellin-transform`, `proved`, `source-open-solved`, `theorem`, `zeta`
