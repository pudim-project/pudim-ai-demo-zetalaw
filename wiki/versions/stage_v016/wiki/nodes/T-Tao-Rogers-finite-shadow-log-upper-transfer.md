---
id: "T-Tao-Rogers-finite-shadow-log-upper-transfer"
type: "theorem"
title: "Tao Rogers finite shadow logarithmic upper density transfer"
status: "proved"
tags: ["bridge-lemma", "finite-shadow", "logarithmic-density", "proved", "rogers-theorem", "sieving", "tao-framed", "theorem"]
parents: ["T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260604T-tao-rogers-finite-shadow-log-upper-transfer.json", "oracle/responses/ORACLE-FC-20260604T-tao-rogers-finite-shadow-response.md", "raw/student/20260604T-tao-rogers-finite-shadow-log-upper-transfer.md", "wiki/notes/tao-rogers-finite-shadow-log-upper-transfer.md"]
---

# Theorem: Tao Rogers finite shadow logarithmic upper density transfer

## Statement

For any infinite one-residue-per-modulus sieve, let delta_N(a) be the finite-shadow survivor density for the first N arbitrary residue classes and delta_N(0) the corresponding zero-residue finite-shadow survivor density. Then delta_N(a) <= delta_N(0) for every N, and the logarithmic upper density of the arbitrary-residue avoided set is at most lim_N delta_N(0). If the zero-residue avoided set has logarithmic density equal to lim_N delta_N(0), then the arbitrary-residue logarithmic upper density is at most that zero-residue logarithmic density; if the arbitrary-residue logarithmic density exists, it satisfies the same inequality.

## Dependencies

- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260604T-tao-rogers-finite-shadow-log-upper-transfer.json`
- `oracle/responses/ORACLE-FC-20260604T-tao-rogers-finite-shadow-response.md`
- `raw/student/20260604T-tao-rogers-finite-shadow-log-upper-transfer.md`
- `wiki/notes/tao-rogers-finite-shadow-log-upper-transfer.md`

## Proof

Fix \(N\).  In the finite cyclic group \(G_N=\mathbb Z/L_N\mathbb Z\), the
congruence condition \(r\equiv a_i\pmod {n_i}\) is the coset
\[
a_i+H_i,
\qquad
H_i=\{r\in G_N:\ r\equiv0\pmod {n_i}\}.
\]
Thus the deleted finite-prefix set is \(\bigcup_{i\le N}(a_i+H_i)\), while
the zero-residue deleted set is \(\bigcup_{i\le N}H_i\).  Rogers' theorem in
Tao's finite cyclic form gives
\[
\left|\bigcup_{i\le N}(a_i+H_i)\right|
\ge
\left|\bigcup_{i\le N}H_i\right|.
\]
Taking complements in \(G_N\) gives
\[
|C_N(a)|\le |C_N(0)|,
\]
and division by \(L_N\) proves
\[
\delta_N(a)\le\delta_N(0).
\]

Now let
\[
B_N(a)=
\{m\in\mathbb N:\ m<n_i
\text{ or }m\not\equiv a_i\pmod {n_i}\text{ for every }i\le N\}.
\]
The local finite-shadow reduction proves
\[
\lim_{x\to\infty}
\frac1{\log x}\sum_{\substack{m<x\\m\in B_N(a)}}\frac1m
=\delta_N(a).
\]
Since \(B(a)\subseteq B_N(a)\) for every \(N\),
\[
\overline d_{\log}B(a)\le \delta_N(a)\le\delta_N(0)
\qquad(N\ge1).
\]
The sequence \(\delta_N(0)\) is nonincreasing and bounded below by \(0\), so
it has a limit.  Taking the infimum over \(N\) yields
\[
\overline d_{\log}B(a)\le\lim_{N\to\infty}\delta_N(0).
\]
The two displayed density comparisons follow immediately when the relevant
logarithmic densities exist and equal their finite-shadow limits.

_Proof source: `raw/student/20260604T-tao-rogers-finite-shadow-log-upper-transfer.md`._

## Tags

`bridge-lemma`, `finite-shadow`, `logarithmic-density`, `proved`, `rogers-theorem`, `sieving`, `tao-framed`, `theorem`
