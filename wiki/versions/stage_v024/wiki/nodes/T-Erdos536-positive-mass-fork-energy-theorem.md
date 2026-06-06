---
id: "T-Erdos536-positive-mass-fork-energy-theorem"
type: "theorem"
title: "Erdos 536 positive mass high support families have positive measured lower shadow fork energy"
status: "open"
tags: ["erdos-536", "fork-energy", "mass-sensitive", "open", "theorem", "union-free"]
parents: ["T-Erdos536-prime-biased-weighted-union-free-frontier"]
refs: ["attack-plans/AP-20260531T181700-erdos536-mass-sensitive-fork.json", "librarian/audits/LA-20260531T181700-erdos536-mass-sensitive-fork-attack-plan.json", "raw/student/20260531T181100-erdos536-fork-width-frontier.md", "wiki/versions/stage_v006/wiki/nodes/mrw-55a8d9eddd2e.md", "wiki/versions/stage_v006/wiki/nodes/mrw-b4075311abd3.md"]
---

# Theorem: Erdos 536 positive mass high support families have positive measured lower shadow fork energy

## Statement

For every fixed \(0<\theta<1\) and \(\eta>0\), every family \(\mathcal F_k\subseteq H_{k,\theta}\) with \(\nu_k(\mathcal F_k)\ge\eta\) has positive mass-sensitive fork energy for all sufficiently large \(k\). More precisely, if for \(C\in\mathcal F_k\) we put \(\mathcal L_{\mathcal F_k}(C)=\{A\in\mathcal F_k:A\subsetneq C\}\), let \(\mu_C\) be the prime-biased product law on subsets of \(C\), and define \(\Phi_k(\mathcal F_k)=\sum_{C\in\mathcal F_k\cap H_{k,\theta}}\nu_k(\{C\})\mu_C^{\otimes2}\{(A,B)\in\mathcal L_{\mathcal F_k}(C)^2:A\ne B,\ A\cup B=C\}\), then \(\Phi_k(\mathcal F_k)>0\).

## Dependencies

- [[wiki/nodes/T-Erdos536-prime-biased-weighted-union-free-frontier|Erdos 536 prime biased high support union free theorem frontier]]

## Proof and provenance references

- `attack-plans/AP-20260531T181700-erdos536-mass-sensitive-fork.json`
- `librarian/audits/LA-20260531T181700-erdos536-mass-sensitive-fork-attack-plan.json`
- `raw/student/20260531T181100-erdos536-fork-width-frontier.md`
- `wiki/versions/stage_v006/wiki/nodes/mrw-55a8d9eddd2e.md`
- `wiki/versions/stage_v006/wiki/nodes/mrw-b4075311abd3.md`

## Tags

`erdos-536`, `fork-energy`, `mass-sensitive`, `open`, `theorem`, `union-free`
