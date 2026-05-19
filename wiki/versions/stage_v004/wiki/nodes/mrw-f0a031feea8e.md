---
id: mrw-f0a031feea8e
type: problem
title: Higher-order monotonicity of polygamma products Pn
aliases: ["mrw-f0a031feea8e", "Higher-order monotonicity of polygamma products Pn"]
status: partial
tags: ["scout-forage", "candidate", "partial", "polygamma", "counterexample"]
parents: []
refs: []
---

# Problem: Higher-order monotonicity of polygamma products Pn

## Statement

Problem statement: For \(n\ge 1\), determine convexity, monotonicity, or complete monotonicity properties of
\[
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x).
\]

Literature status: open candidate from the same 2025 polygamma source.

## Source References

- Feng Qi, Dongkyu Lim, and Kwara Nantomah, "Monotonicity and positivity of several functions involving ratios and products of polygamma functions", Journal of Inequalities and Applications 2025, article 5. DOI: https://doi.org/10.1186/s13660-024-03245-8

## Partial Resolution

The stronger complete-monotonicity assertion is refuted by [[wiki/nodes/mrw-dee642b8e9cb|Counterexample to complete monotonicity of higher-order polygamma product curvature]], which proves \(P_n'''(2)>0\) for all \(n\ge29\) and gives an additional lower-order certificate \(P_7^{(6)}(3)<0\). The weaker all-\(n\) convexity question is not settled by this counterexample.

## Notes

- This is a higher-polygamma analogue of partition-function curvature.
