---
id: "T-Alzer-Kwong-reciprocal-zeta-convexity-concavity-pattern"
type: "theorem"
title: "T-Alzer-Kwong-reciprocal-zeta-convexity-concavity-pattern"
status: "proved"
tags: ["application-bridge", "concavity", "convexity", "proved", "reciprocal-zeta", "source-open-solved", "theorem", "zeta"]
parents: ["T-zeta-free-energy-uniform-curvature-bound"]
refs: ["private proof note", "theory/latest/THEORY.tex#thm:alzer-kwong"]
---

# Theorem: T-Alzer-Kwong-reciprocal-zeta-convexity-concavity-pattern

## Statement

Let \(F(x)=1/\zeta(x)\). For every integer \(n\ge1\), \(F''(x)>0\) on \((-4n,-4n+2)\), and \(F''(x)<0\) on \((-4n-2,-4n)\).

## Dependencies

- [[wiki/nodes/T-zeta-free-energy-uniform-curvature-bound|T-zeta-free-energy-uniform-curvature-bound]]

## Proof and provenance references

- `private proof note`
- `theory/latest/THEORY.tex#thm:alzer-kwong`

## Proof

The theory proves the zeta-law free-energy curvature bound \((\log\zeta)''(s)=\operatorname{Var}_s(\log N)<1/3\) for \(s\ge3\). On the negative axis, the functional equation rewrites \(1/\zeta(-u)\) as a signed copy of a positive function \(G(u)\). Its logarithmic second derivative is bounded below by \(\pi^2/4-1/2-1/3>0\), using the curvature bound, the elementary trigamma estimate, and \(\csc^2(\pi u/2)\ge1\). Hence \(G''(u)>0\). The sign of \(\sin(\pi u/2)\) then transfers this positive convexity to alternating convexity and concavity intervals for \(F(x)=1/\zeta(x)\).

_Proof source: `private proof note`._

## Tags

`application-bridge`, `concavity`, `convexity`, `proved`, `reciprocal-zeta`, `source-open-solved`, `theorem`, `zeta`
