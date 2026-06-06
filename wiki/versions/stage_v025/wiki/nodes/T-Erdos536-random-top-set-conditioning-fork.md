---
id: "T-Erdos536-random-top-set-conditioning-fork"
type: "theorem"
title: "Erdos 536 random top set conditioning gives positive conditional fork probability"
status: "open"
tags: ["conditioning", "erdos-536", "fork-energy", "open", "random-top-set", "theorem"]
parents: ["T-Erdos536-prime-biased-weighted-union-free-frontier"]
refs: ["attack-plans/AP-20260531T182600-erdos536-rank-diffuse-fork-free.json", "librarian/audits/LA-20260531T182600-erdos536-rank-diffuse-fork-free-attack-plan.json", "raw/student/20260531T182200-erdos536-mass-sensitive-fork.md", "theory/nodes/T-Erdos536-positive-mass-fork-energy-theorem.json", "wiki/versions/stage_v006/wiki/nodes/mrw-b4075311abd3.md"]
---

# Theorem: Erdos 536 random top set conditioning gives positive conditional fork probability

## Statement

For every fixed \(0<\theta<1\) and \(\eta>0\), if \(\mathcal F_k\subseteq H_{k,\theta}\) has \(\nu_k(\mathcal F_k)\ge\eta\) and is not rank-thin, then a random top set \(C\) drawn from \(\nu_k\) conditioned on \(\mathcal F_k\) has positive conditional fork probability for all sufficiently large \(k\): with \(\mathcal L_{\mathcal F_k}(C)=\{A\in\mathcal F_k:A\subsetneq C\}\) and \(\mu_C\) the prime-biased product law on subsets of \(C\), one has \(\mu_C^{\otimes2}\{(A,B)\in\mathcal L_{\mathcal F_k}(C)^2:A\ne B,\ A\cup B=C\}>0\) for a positive \(\nu_k\)-mass set of tops \(C\).

## Dependencies

- [[wiki/nodes/T-Erdos536-prime-biased-weighted-union-free-frontier|Erdos 536 prime biased high support union free theorem frontier]]

## Proof and provenance references

- `attack-plans/AP-20260531T182600-erdos536-rank-diffuse-fork-free.json`
- `librarian/audits/LA-20260531T182600-erdos536-rank-diffuse-fork-free-attack-plan.json`
- `raw/student/20260531T182200-erdos536-mass-sensitive-fork.md`
- `theory/nodes/T-Erdos536-positive-mass-fork-energy-theorem.json`
- `wiki/versions/stage_v006/wiki/nodes/mrw-b4075311abd3.md`

## Tags

`conditioning`, `erdos-536`, `fork-energy`, `open`, `random-top-set`, `theorem`
