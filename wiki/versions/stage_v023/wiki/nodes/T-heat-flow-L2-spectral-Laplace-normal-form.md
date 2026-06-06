---
id: "T-heat-flow-L2-spectral-Laplace-normal-form"
type: "theorem"
title: "heat flow L2 energy has Fourier spectral positive Laplace representation"
status: "proved"
tags: ["bridge-patch", "entropy", "forage", "heat-flow", "laplace-transform", "plancherel", "proved", "theorem"]
parents: ["T-heat-flow-L2-energy-completely-monotone"]
refs: ["attack-plans/AP-20260529T-next-loop-heat-flow-l2.json", "librarian/audits/LA-20260529T-next-loop-heat-flow-l2-student.json", "raw/oracle/ORACLE-FI-20260529T-next-loop-024-force.md", "raw/student/20260529T-next-loop-heat-flow-l2.md", "scout/forage/responses/FR-20260529T-next-loop-024-oracle-response.md", "wiki/notes/frontier-heat-flow-l2-spectral-laplace.md"]
---

# Theorem: heat flow L2 energy has Fourier spectral positive Laplace representation

## Statement

Let \(\mu\) be a probability measure on \(\mathbb R^d\), let \(\widehat G_t(\xi)=e^{-t|\xi|^2}\), and put \(p_t=G_t*\mu\). Then \(N_2(t)=\int_{\mathbb R^d}p_t(x)^2\,dx\) has the spectral Laplace representation \(N_2(t)=\int_0^\infty e^{-2tr}\,d\nu_\mu(r)\), where \(\nu_\mu\) is the pushforward of \((2\pi)^{-d}|\widehat\mu(\xi)|^2\,d\xi\) under \(\xi\mapsto|\xi|^2\).

## Dependencies

- [[wiki/nodes/T-heat-flow-L2-energy-completely-monotone|heat flow L2 energy is completely monotone in heat time]]

## Proof and provenance references

- `attack-plans/AP-20260529T-next-loop-heat-flow-l2.json`
- `librarian/audits/LA-20260529T-next-loop-heat-flow-l2-student.json`
- `raw/oracle/ORACLE-FI-20260529T-next-loop-024-force.md`
- `raw/student/20260529T-next-loop-heat-flow-l2.md`
- `scout/forage/responses/FR-20260529T-next-loop-024-oracle-response.md`
- `wiki/notes/frontier-heat-flow-l2-spectral-laplace.md`

## Tags

`bridge-patch`, `entropy`, `forage`, `heat-flow`, `laplace-transform`, `plancherel`, `proved`, `theorem`
