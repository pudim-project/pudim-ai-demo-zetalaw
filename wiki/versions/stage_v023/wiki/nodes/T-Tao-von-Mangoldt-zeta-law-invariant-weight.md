---
id: "T-Tao-von-Mangoldt-zeta-law-invariant-weight"
type: "theorem"
title: "Tao von Mangoldt chain invariant weight as a zeta-law balance"
status: "accepted_local_node"
tags: ["accepted_local_node", "theorem"]
parents: ["D-Riemann-zeta-probability-law"]
refs: [".pudim/attack-plans/AP-20260604T-tao-von-mangoldt-zeta-invariance.json", ".pudim/librarian/audits/LA-20260604T-tao-von-mangoldt-zeta-invariant-weight.json", ".pudim/raw/student/20260604T-tao-von-mangoldt-zeta-invariant-weight.md", ".pudim/wiki/notes/tao-von-mangoldt-zeta-invariant-weight.md"]
---

# Theorem: Tao von Mangoldt chain invariant weight as a zeta-law balance

## Statement

For n > 1, the weight nu_Lambda(n)=int_1^infty log(n)/(zeta(s)n^s) ds is invariant under parent inflow for Tao's downward von Mangoldt transition P(nq -> n)=Lambda(q)/log(nq).
\[
nu_Lambda(n)=sum_{q>=2} nu_Lambda(nq)Lambda(q)/log(nq), n>1
\]

## Dependencies

- [[wiki/nodes/D-Riemann-zeta-probability-law|Riemann zeta probability law]]

## Proof and provenance references

- `.pudim/attack-plans/AP-20260604T-tao-von-mangoldt-zeta-invariance.json`
- `.pudim/librarian/audits/LA-20260604T-tao-von-mangoldt-zeta-invariant-weight.json`
- `.pudim/raw/student/20260604T-tao-von-mangoldt-zeta-invariant-weight.md`
- `.pudim/wiki/notes/tao-von-mangoldt-zeta-invariant-weight.md`

## Do not claim

- Do not claim this solves Erdos Problem #1196.
- Do not claim novelty over Tao or the 2026 arXiv paper.
- Do not use the identity at n=1 without an absorbing-boundary convention.

## Tags

`accepted_local_node`, `theorem`
