---
id: "T-Parity-classification-assembly-principle"
type: "theorem"
title: "T-Parity-classification-assembly-principle"
status: "proved"
tags: ["application-bridge", "classification-assembly", "method", "parity-principle", "primitive", "principle", "proved", "structural-tool", "theorem"]
parents: []
refs: ["raw/student/20260605T-bridge-parity-classification-assembly-principle.md"]
---

# Theorem: T-Parity-classification-assembly-principle

## Statement

Suppose a source parity classification is split into two disjoint parity classes. If the positive class is proved by one theorem and the claimed negative class is refuted by one admissible counterexample, then the corrected parity classification is the conjunction of those two upstream results.

## Proof and provenance references

- `raw/student/20260605T-bridge-parity-classification-assembly-principle.md`

## Proof

Let a classification problem split a family \(\mathcal F\) into two disjoint classes \(\mathcal F_0\) and \(\mathcal F_1\). Suppose one theorem proves the asserted positive property for every member of \(\mathcal F_1\), and another theorem or counterexample determines that the proposed universal assertion on \(\mathcal F_0\) must be corrected. Then the corrected classification is obtained by taking the conjunction of the two upstream results.

The two classes are disjoint and exhaustive, so every member of \(\mathcal F\) lies in exactly one class. The first upstream result decides all cases in \(\mathcal F_1\), and the second decides the corrected status of \(\mathcal F_0\). Hence their conjunction is a complete classification for \(\mathcal F\).

_Proof source: `raw/student/20260605T-bridge-parity-classification-assembly-principle.md`._

## Tags

`application-bridge`, `classification-assembly`, `method`, `parity-principle`, `primitive`, `principle`, `proved`, `structural-tool`, `theorem`
