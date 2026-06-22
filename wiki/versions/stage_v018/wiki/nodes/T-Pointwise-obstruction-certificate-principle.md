---
id: "T-Pointwise-obstruction-certificate-principle"
type: "theorem"
title: "T-Pointwise-obstruction-certificate-principle"
status: "proved"
tags: ["application-bridge", "counterexample-principle", "endpoint-obstruction", "logic", "primitive", "principle", "proof-step", "proved", "structural-tool", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Endpoint-obstruction-certificate-language"]
refs: ["raw/student/20260605T-bridge-pointwise-obstruction-principle.md"]
---

# Theorem: T-Pointwise-obstruction-certificate-principle

## Statement

If a universal sign, convexity, monotonicity, or complete-monotonicity source claim has been reduced to a pointwise inequality on a domain, then one certified admissible point with the opposite sign refutes the universal claim.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]

## Proof and provenance references

- `raw/student/20260605T-bridge-pointwise-obstruction-principle.md`

## Proof

Let \(D\) be a domain and let a universal claim require a sign condition \(F(x)\ge0\) for all \(x\in D\). More generally, allow any equivalent sign condition obtained by multiplying by a known positive factor or by moving all terms to one side. If there exists a certified admissible point \(x_0\in D\) with the opposite sign, then the universal claim is false.

The proof is the elementary logic of a universal quantifier. The point \(x_0\) satisfies the hypotheses of the universal statement, while the certified sign computation violates the asserted conclusion. Multiplication by a positive factor preserves signs, so any equivalent reduced inequality has the same counterexample. Therefore the original universal sign, convexity, monotonicity, or complete-monotonicity claim is refuted.

_Proof source: `raw/student/20260605T-bridge-pointwise-obstruction-principle.md`._

## Tags

`application-bridge`, `counterexample-principle`, `endpoint-obstruction`, `logic`, `primitive`, `principle`, `proof-step`, `proved`, `structural-tool`, `theorem`
