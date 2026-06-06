---
id: "T-nonnegative-negative-power-LCM"
type: "theorem"
title: "nonnegative negative power t^{-eta} is logarithmically completely monotone"
status: "proved"
tags: ["elementary-power", "logarithmically-completely-monotone", "proved", "standard-tool", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260531T071000-ks-qdigamma-theta-family.json", "raw/student/20260531T071000-ks-qdigamma-theta-family.md", "wiki/definitions/logarithmically-completely-monotone.md", "wiki/notes/frontier-ks-qdigamma-theta-family.md"]
---

# Theorem: nonnegative negative power t^{-eta} is logarithmically completely monotone

## Statement

For every \(\eta\ge0\), the function \(t\mapsto t^{-\eta}\) is logarithmically completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260531T071000-ks-qdigamma-theta-family.json`
- `raw/student/20260531T071000-ks-qdigamma-theta-family.md`
- `wiki/definitions/logarithmically-completely-monotone.md`
- `wiki/notes/frontier-ks-qdigamma-theta-family.md`

## Proof

A positive function \(f\) on \((0,\infty)\) is logarithmically completely monotone, abbreviated LCM, if
\[
(-1)^n(\log f)^{(n)}(x)\ge0
\]
for every \(n\ge1\) and every \(x>0\).

_Proof source: `wiki/definitions/logarithmically-completely-monotone.md`._

## Tags

`elementary-power`, `logarithmically-completely-monotone`, `proved`, `standard-tool`, `theorem`
