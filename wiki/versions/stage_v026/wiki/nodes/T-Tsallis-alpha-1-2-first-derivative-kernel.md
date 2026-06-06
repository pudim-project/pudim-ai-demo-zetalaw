---
id: "T-Tsallis-alpha-1-2-first-derivative-kernel"
type: "theorem"
title: "Tsallis alpha in (1,2) first entropy derivative has positive Laplace-kernel square-gradient representation"
status: "proved"
tags: ["first-derivative", "heat-flow", "positive-kernel", "proved", "theorem", "true-helper", "tsallis"]
parents: []
refs: ["librarian/audits/LA-20260528T121500-tsallis-first-derivative-kernel.json", "raw/oracle/OS-20260528T120500-renyi-tsallis.md", "raw/student/20260528T120500-tsallis-alpha2-noise-stability.md", "wiki/notes/frontier-renyi-tsallis-heat-flow-cm.md"]
---

# Theorem: Tsallis alpha in (1,2) first entropy derivative has positive Laplace-kernel square-gradient representation

## Statement

For a one-dimensional positive heat-flow density \(p(x,t)=T_t f(x)\) and \(1<\alpha<2\), the first derivative of the Tsallis entropy has the positive-kernel representation \(\partial_t\hat h_\alpha(p)=\frac{\alpha}{2\Gamma(2-\alpha)}\int_0^\infty \lambda^{1-\alpha}\int e^{-\lambda p(x,t)}p_x(x,t)^2\,dx\,d\lambda\), equivalently \(\partial_t\hat h_\alpha(p)=\frac{2\alpha}{\Gamma(2-\alpha)}\int_0^\infty \lambda^{-1-\alpha}\|\partial_x e^{-\lambda p(\cdot,t)/2}\|_2^2\,d\lambda\).

## Proof and provenance references

- `librarian/audits/LA-20260528T121500-tsallis-first-derivative-kernel.json`
- `raw/oracle/OS-20260528T120500-renyi-tsallis.md`
- `raw/student/20260528T120500-tsallis-alpha2-noise-stability.md`
- `wiki/notes/frontier-renyi-tsallis-heat-flow-cm.md`

## Tags

`first-derivative`, `heat-flow`, `positive-kernel`, `proved`, `theorem`, `true-helper`, `tsallis`
