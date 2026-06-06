---
id: "T-Sokal-GS-lambda-derivative-generating-function"
type: "theorem"
title: "Sokal generalized Stieltjes tests have formal exponential generating function in k"
status: "proved"
tags: ["bridge-patch", "derivative-test", "generalized-stieltjes", "generating-function", "proved", "sokal", "theorem"]
parents: ["T-Sokal-GS-all-lambda-derivatives-positive-combination", "T-Sokal-GS-first-lambda-derivative-triangular-formula", "T-Sokal-GS-order-monotonicity-direct-triangular-formula"]
refs: ["attack-plans/AP-20260531T090000-sokal-gs-lambda-derivative.json", "librarian/audits/LA-20260531T090000-sokal-gs-lambda-derivative.json", "oracle/responses/ORACLE-OS-20260531T-sokal-gs-lambda-derivative-oracle-response.md", "raw/student/20260531T090000-sokal-gs-lambda-derivative.md", "wiki/notes/frontier-sokal-gs-lambda-derivative-compression.md"]
---

# Theorem: Sokal generalized Stieltjes tests have formal exponential generating function in k

## Statement

For fixed \(n\), Sokal's generalized-Stieltjes tests satisfy the formal exponential generating function \(\sum_{k\ge0}F^{[\lambda]}_{n,k}(x)z^k/k!=(1-z)^{-(n+\lambda)}(-1)^n\sum_{j\ge0}x^j f^{(n+j)}(x)(z/(1-z))^j/j!\).

## Dependencies

- [[wiki/nodes/T-Sokal-GS-all-lambda-derivatives-positive-combination|all lambda derivatives of Sokal generalized Stieltjes tests are nonnegative lower k combinations]]
- [[wiki/nodes/T-Sokal-GS-first-lambda-derivative-triangular-formula|first lambda derivative of Sokal generalized Stieltjes tests is positive triangular combination]]
- [[wiki/nodes/T-Sokal-GS-order-monotonicity-direct-triangular-formula|Sokal generalized Stieltjes test conditions weaken with order by positive triangular transform]]

## Proof and provenance references

- `attack-plans/AP-20260531T090000-sokal-gs-lambda-derivative.json`
- `librarian/audits/LA-20260531T090000-sokal-gs-lambda-derivative.json`
- `oracle/responses/ORACLE-OS-20260531T-sokal-gs-lambda-derivative-oracle-response.md`
- `raw/student/20260531T090000-sokal-gs-lambda-derivative.md`
- `wiki/notes/frontier-sokal-gs-lambda-derivative-compression.md`

## Tags

`bridge-patch`, `derivative-test`, `generalized-stieltjes`, `generating-function`, `proved`, `sokal`, `theorem`
