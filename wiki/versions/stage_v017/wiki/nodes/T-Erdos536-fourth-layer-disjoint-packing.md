---
id: "T-Erdos536-fourth-layer-disjoint-packing"
type: "theorem"
title: "Erdos 536 fourth valuation layer disjoint LCM-triangle packing"
status: "proved"
tags: ["erdos-536", "lcm", "packing", "partial-progress", "proved", "theorem", "valuation-residue"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["private attack plan", "private librarian audit", "private proof note", "wiki/notes/frontier-erdos536-lcm-triangle-packing.md"]
---

# Theorem: Erdos 536 fourth valuation layer disjoint LCM-triangle packing

## Statement

The LCM-triangle family \(\{11m,13m,143m\}\), with \(v_2(m)\equiv v_3(m)\equiv0\pmod4\) and \(v_5(m),v_7(m),v_{11}(m),v_{13}(m)\equiv0\pmod2\), is pairwise disjoint from the three public Erdos 536 packing layers and has density \(1/640\).

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-erdos536-lcm-triangle-packing.md`

## Proof

Consider triples
\[
\{11m,13m,143m\}
\]
where
\[
143m\le N,
\]
and
\[
v_2(m)\equiv0\pmod4,\quad v_3(m)\equiv0\pmod4,\quad
v_5(m)\equiv v_7(m)\equiv v_{11}(m)\equiv v_{13}(m)\equiv0\pmod2.
\]

Each such triple is an LCM-triangle because
\[
[11m,13m]=[11m,143m]=[13m,143m]=143m.
\]

For a prime \(p\), the density of integers \(m\) with \(v_p(m)\equiv0\pmod k\) is
\[
\sum_{j\ge0}\left(\frac1{p^{kj}}-\frac1{p^{kj+1}}\right)
=\frac{1-1/p}{1-p^{-k}}.
\]
Therefore the fourth-layer density is
\[
\frac1{143}\cdot\frac{8}{15}\cdot\frac{27}{40}\cdot
\frac56\cdot\frac78\cdot\frac{11}{12}\cdot\frac{13}{14}
=\frac1{640}.
\]

The first public layer occupies valuation parities
\[
(v_2,v_3)\equiv(1,0),(0,1),(1,1)\pmod2.
\]
Every element of the fourth layer has \(v_2\equiv v_3\equiv0\pmod2\), so it is disjoint from the first layer.

The second public layer occupies signatures
\[
(v_2\bmod4,v_3\bmod2,v_5\bmod2)
=(2,0,0),(0,0,1),(2,0,1).
\]
Every element of the fourth layer has
\[
v_2\equiv0\pmod4,\quad v_3\equiv0\pmod2,\quad v_5\equiv0\pmod2,
\]
so it is disjoint from the second layer.

The third public layer occupies signatures, under
\[
v_2\equiv0\pmod4,\quad v_5\equiv0\pmod2,
\]
given by
\[
(v_3\bmod4,v_7\bmod2)=(0,1),(2,0),(2,1).
\]
Every element of the fourth layer has
\[
v_3\equiv0\pmod4,\quad v_7\equiv0\pmod2,
\]
so it is disjoint from the third layer.

Inside the fourth layer, the three roles have distinct \((v_{11},v_{13})\bmod2\) signatures:
\[
(1,0),\quad(0,1),\quad(1,1).
\]
Thus different roles cannot collide.  If the same role collides, the multiplier is the same and hence \(m\) is the same.  Therefore the fourth-layer triples are pairwise disjoint.

An LCM-triangle-free set must omit at least one element from each pairwise-disjoint forbidden triple.  Combining the three public layers with the fourth layer gives
\[
\frac1{12}+\frac1{60}+\frac1{240}+\frac1{640}
=\frac{203}{1920}
\]
pairwise-disjoint forbidden triples per \(N\), up to \(o(N)\).  Hence
\[
f(N)\le
\left(1-\frac{203}{1920}+o(1)\right)N
=\left(\frac{1717}{1920}+o(1)\right)N.
\]

_Proof source: `private proof note`._

## Tags

`erdos-536`, `lcm`, `packing`, `partial-progress`, `proved`, `theorem`, `valuation-residue`
