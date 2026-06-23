---
id: "L-Bounded-BF-Ratio-Residual-Finite-Mass-Gate"
type: "lemma"
title: "Bounded Bernstein integer values have finite residual moment mass"
status: "proved"
tags: ["bernstein-function", "finite-mass-obstruction", "hausdorff-moment", "integer-values", "lemma", "primitive-bridge", "proved", "simon-binomial-raney", "true"]
parents: ["L-BF-Integer-Increments-Hausdorff-Finite", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: [".pudim/attack-plans/AP-20260612T1245-simon-binomial-raney-p2-hausdorff-increment.json", ".pudim/librarian/audits/LA-20260612T1310-simon-p2-bridge-slices.json", ".pudim/oracle/responses/OS-20260612T1255Z-simon-binomial-raney-p2-live-oracle-response.md"]
---

# Lemma: Bounded Bernstein integer values have finite residual moment mass

## Statement

If \(\Phi\) is a Bernstein function, \(\Phi(n)\to L<\infty\), and \(R_n=\Phi(n)\), then there is a finite positive measure \(\mu\) on \([0,1]\) such that \(L-R_n=\int_{[0,1]}u^n\,d\mu(u)\) for every \(n\ge1\), and \(\mu([0,1])\le L\).

## Dependencies

- [[wiki/nodes/L-BF-Integer-Increments-Hausdorff-Finite|Bernstein integer increments are finite Hausdorff moments]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `.pudim/attack-plans/AP-20260612T1245-simon-binomial-raney-p2-hausdorff-increment.json`
- `.pudim/librarian/audits/LA-20260612T1310-simon-p2-bridge-slices.json`
- `.pudim/oracle/responses/OS-20260612T1255Z-simon-binomial-raney-p2-live-oracle-response.md`

## Proof source health

_No extractable public proof fragment was found for this proved theorem-like node._

- .pudim/attack-plans/AP-20260612T1245-simon-binomial-raney-p2-hausdorff-increment.json: not a public proof-fragment source

## Tags

`bernstein-function`, `finite-mass-obstruction`, `hausdorff-moment`, `integer-values`, `lemma`, `primitive-bridge`, `proved`, `simon-binomial-raney`, `true`
