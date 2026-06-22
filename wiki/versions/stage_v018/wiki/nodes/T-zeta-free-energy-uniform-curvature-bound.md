---
id: "T-zeta-free-energy-uniform-curvature-bound"
type: "theorem"
title: "T-zeta-free-energy-uniform-curvature-bound"
status: "proved"
tags: ["application-bridge", "curvature", "free-energy", "primitive", "proved", "structural-tool", "theorem", "variance-bound", "zeta-law"]
parents: ["D-Zeta-free-energy"]
refs: ["raw/student/20260605T-bridge-alzer-kwong-reciprocal-zeta.md", "theory/latest/THEORY.tex#lem:uniform-positive-axis-curvature"]
---

# Theorem: T-zeta-free-energy-uniform-curvature-bound

## Statement

For every \(s\ge3\), the zeta free-energy curvature satisfies \((\log\zeta)''(s)=\mathrm{Var}_s(\log N)<1/3\).

## Dependencies

- [[wiki/nodes/D-Zeta-free-energy|Zeta free energy]]

## Proof and provenance references

- `raw/student/20260605T-bridge-alzer-kwong-reciprocal-zeta.md`
- `theory/latest/THEORY.tex#lem:uniform-positive-axis-curvature`

## Proof

The theory proves the zeta-law free-energy curvature bound \((\log\zeta)''(s)=\operatorname{Var}_s(\log N)<1/3\) for \(s\ge3\). On the negative axis, the functional equation rewrites \(1/\zeta(-u)\) as a signed copy of a positive function \(G(u)\). Its logarithmic second derivative is bounded below by \(\pi^2/4-1/2-1/3>0\), using the curvature bound, the elementary trigamma estimate, and \(\csc^2(\pi u/2)\ge1\). Hence \(G''(u)>0\). The sign of \(\sin(\pi u/2)\) then transfers this positive convexity to alternating convexity and concavity intervals for \(F(x)=1/\zeta(x)\).

_Proof source: `raw/student/20260605T-bridge-alzer-kwong-reciprocal-zeta.md`._

## Tags

`application-bridge`, `curvature`, `free-energy`, `primitive`, `proved`, `structural-tool`, `theorem`, `variance-bound`, `zeta-law`
