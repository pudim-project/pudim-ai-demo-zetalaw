---
id: "T-incomplete-beta-tail-derivative-CM-certificate"
type: "theorem"
title: "incomplete beta tail derivative has positive discrete Laplace representation for lambda at most one"
status: "proved"
tags: ["bernstein-function", "bridge-patch", "complete-monotonicity", "incomplete-beta", "laplace-transform", "proved", "theorem"]
parents: ["T-incomplete-beta-tail-BF-slice"]
refs: ["attack-plans/AP-20260529T-next-loop-incomplete-beta-tail.json", "librarian/audits/LA-20260529T-next-loop-incomplete-beta-tail-student.json", "raw/oracle/ORACLE-FI-20260529T-next-loop-026.md", "raw/student/20260529T-next-loop-incomplete-beta-tail.md", "scout/forage/responses/FR-20260529T-next-loop-026-oracle-response.md", "wiki/notes/frontier-incomplete-beta-tail-bernstein.md"]
---

# Theorem: incomplete beta tail derivative has positive discrete Laplace representation for lambda at most one

## Statement

For \(b>0\) and \(0<\lambda\le1\), the derivative of \(I_{b,\lambda}(x)=B(b,\lambda)-B(b,\lambda;e^{-x})\) is completely monotone; for \(0<\lambda<1\), \(I_{b,\lambda}'(x)=\sum_{n=0}^\infty (1-\lambda)_n e^{-(b+n)x}/n!\).

## Dependencies

- [[wiki/nodes/T-incomplete-beta-tail-BF-slice|incomplete beta tail is Bernstein for b positive and lambda between zero and one]]

## Proof and provenance references

- `attack-plans/AP-20260529T-next-loop-incomplete-beta-tail.json`
- `librarian/audits/LA-20260529T-next-loop-incomplete-beta-tail-student.json`
- `raw/oracle/ORACLE-FI-20260529T-next-loop-026.md`
- `raw/student/20260529T-next-loop-incomplete-beta-tail.md`
- `scout/forage/responses/FR-20260529T-next-loop-026-oracle-response.md`
- `wiki/notes/frontier-incomplete-beta-tail-bernstein.md`

## Tags

`bernstein-function`, `bridge-patch`, `complete-monotonicity`, `incomplete-beta`, `laplace-transform`, `proved`, `theorem`
