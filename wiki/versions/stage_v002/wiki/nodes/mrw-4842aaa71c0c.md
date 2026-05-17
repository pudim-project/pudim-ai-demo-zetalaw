---
id: mrw-4842aaa71c0c
type: proposition
title: Finite Euler-score identity
aliases: ["mrw-4842aaa71c0c", "Finite Euler-score identity"]
status: proved
tags: [zeta-law, proposition, proved, euler-product, finite]
parents: []
refs: ["raw/20260517T155448Z-build-a-raw-pudim-wiki-for-the-zeta-law-entropy-modular-reso-bootstrap-import.md"]
---

# Proposition: Finite Euler-score identity

## Statement

For every \(A\subseteq\{1,\ldots,N\}\),
\[
\sum_{n\in A}\log n
=\sum_{d\le N}\Lambda(d)\sum_{m\le N/d}\mathbf 1_A(md).
\]

## Proof

Reverse the order of summation:
\[
\sum_{d\le N}\Lambda(d)\sum_{m\le N/d}\mathbf 1_A(md)
=\sum_{n\in A}\sum_{d\mid n}\Lambda(d)
=\sum_{n\in A}\log n.
\]

## Depends on

## Used by

## Notes

- This is the finite set version of the Euler-score decomposition.
