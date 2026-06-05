---
id: "T-Dedekind-ideal-von-Mangoldt-chain-invariant-weight"
type: "theorem"
title: "Dedekind-ideal von Mangoldt chain and invariant hitting weight"
status: "proved"
tags: ["proved", "theorem"]
parents: ["unique factorization of nonzero integral ideals into prime ideals", "Dedekind Euler product and -zeta_K'/zeta_K Dirichlet series", "simple pole of zeta_K at s=1", "Tao chain/antichain duality mechanism"]
refs: [".pudim/attack-plans/AP-20260604T-tao-dedekind-ideal-vm-chain.json", ".pudim/oracle/responses/ORACLE-FC-20260604T-tao-dedekind-ideal-chain-response.md", ".pudim/oracle/responses/ORACLE-OS-20260604T-tao-dedekind-ideal-chain-student-response.md", ".pudim/raw/student/20260604T-tao-dedekind-ideal-vm-chain.md", ".pudim/wiki/notes/tao-dedekind-ideal-vm-chain.md"]
---

# Theorem: Dedekind-ideal von Mangoldt chain and invariant hitting weight

## Statement

For every fixed number field K, the monoid of nonzero integral ideals admits a stochastic downward von Mangoldt chain and an adjoint upward chain whose hitting weight is nu_K.
\[
nu_K(a)=int_1^infty log Na/(zeta_K(s)Na^s) ds for Na>1, nu_K((1))=1, and P_up(hit a)=nu_K(a).
\]

## Scope

- fixed number field K
- state space is nonzero integral ideals
- divisibility is ideal divisibility
- does not assert an element-level or principal-ideal-only non-UFD theorem

## Dependencies

- unique factorization of nonzero integral ideals into prime ideals
- Dedekind Euler product and -zeta_K'/zeta_K Dirichlet series
- simple pole of zeta_K at s=1
- Tao chain/antichain duality mechanism

## Proof and provenance references

- `.pudim/attack-plans/AP-20260604T-tao-dedekind-ideal-vm-chain.json`
- `.pudim/oracle/responses/ORACLE-FC-20260604T-tao-dedekind-ideal-chain-response.md`
- `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-dedekind-ideal-chain-student-response.md`
- `.pudim/raw/student/20260604T-tao-dedekind-ideal-vm-chain.md`
- `.pudim/wiki/notes/tao-dedekind-ideal-vm-chain.md`

## Do not claim

- Do not claim the full nontrivial-class-group element problem is solved.
- Do not use the ambiguous phrase primitive ideal without defining ideal antichain.
- Do not assign APP/open-problem-solved status without a separate decision.

## Tags

`proved`, `theorem`
