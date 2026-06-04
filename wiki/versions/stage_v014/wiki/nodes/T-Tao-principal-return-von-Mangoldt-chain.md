---
id: "T-Tao-principal-return-von-Mangoldt-chain"
type: "theorem"
title: "Principal-return trace theorem for the ideal von Mangoldt chain"
status: "proved"
tags: ["proved", "theorem"]
parents: []
refs: [".pudim/attack-plans/AP-20260604T-tao-principal-return-chain.json", ".pudim/oracle/responses/ORACLE-FC-20260604T-tao-principal-return-chain-response.md", ".pudim/oracle/responses/ORACLE-OS-20260604T-tao-principal-return-chain-student-response.md", ".pudim/raw/student/20260604T-tao-principal-return-chain.md", ".pudim/wiki/notes/tao-principal-return-chain.md"]
---

# Theorem: Principal-return trace theorem for the ideal von Mangoldt chain

## Statement

For a fixed number field, the first-return trace of the full ideal von Mangoldt chain on principal ideals is a stochastic principal-ideal chain whose strict upward reversal has hitting weight nu_K and yields the principal-ideal antichain tail bound.
\[
P_hat_up(b to a)=nu_K(a) P_hat_down(a to b)/nu_K(b), strict blocks only; P_hat_up from (1) hits a with probability nu_K(a).
\]

## Scope

- K is a fixed number field
- state space is nonzero principal integral ideals
- transitions are first-return blocks through the full ideal chain
- upward reversal excludes the absorbing self-loop at the unit ideal
- not an element-level non-UFD theorem

## Proof and provenance references

- `.pudim/attack-plans/AP-20260604T-tao-principal-return-chain.json`
- `.pudim/oracle/responses/ORACLE-FC-20260604T-tao-principal-return-chain-response.md`
- `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-principal-return-chain-student-response.md`
- `.pudim/raw/student/20260604T-tao-principal-return-chain.md`
- `.pudim/wiki/notes/tao-principal-return-chain.md`

## Do not claim

- Do not claim source_open_solved_scoped.
- Do not claim a local one-primepower principal-only chain.
- Do not claim an element-level non-UFD extension.
- Do not claim a sharper principal-density constant.

## Tags

`proved`, `theorem`
