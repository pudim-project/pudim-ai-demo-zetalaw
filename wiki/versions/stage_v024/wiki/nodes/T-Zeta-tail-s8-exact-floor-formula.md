---
id: "T-Zeta-tail-s8-exact-floor-formula"
type: "theorem"
title: "T-Zeta-tail-s8-exact-floor-formula"
status: "proved"
tags: ["application-bridge", "inverse-tail-floor", "proved", "source-open-solved", "telescoping-certificate", "theorem", "zeta-tail"]
parents: ["D-Tail-zeta-partition-function", "T-Zeta-tail-inverse-asymptotic-telescoping-template"]
refs: ["raw/student/20260605T-bridge-zeta-tail-s8-floor.md", "theory/latest/THEORY.tex#thm:tail-s8-floor"]
---

# Theorem: T-Zeta-tail-s8-exact-floor-formula

## Statement

For \(T_8(n)=\zeta_n(8)=\sum_{k=n}^\infty k^{-8}\), the exact formula \(\lfloor T_8(n)^{-1}\rfloor=\lfloor A_8(n)\rfloor\) holds for every \(n\ge6\), with the finite table \(0,245,5844,53503,291407\) for \(1\le n\le5\), where \(A_8\) is the rational approximant displayed in the staged APP-0006 theorem.

## Dependencies

- [[wiki/nodes/D-Tail-zeta-partition-function|Tail zeta partition function]]
- [[wiki/nodes/T-Zeta-tail-inverse-asymptotic-telescoping-template|reusable Euler Maclaurin inverse-tail approximant plus telescoping sign certificate template]]

## Proof and provenance references

- `raw/student/20260605T-bridge-zeta-tail-s8-floor.md`
- `theory/latest/THEORY.tex#thm:tail-s8-floor`

## Proof

The proof instantiates the inverse-tail asymptotic telescoping template at \(s=8\) with the explicit adjacent rational approximants \(A_8\) and \(B_8\). The template provides the recursive telescoping bounds that force \(\lfloor T_8(n)^{-1}\rfloor=\lfloor A_8(n)\rfloor=\lfloor B_8(n)\rfloor\), and the gap inequality \(B_8-A_8<1\).  The finite seed table \(0,245,5844,53503,291407\) is handled separately for \(1\le n\le5\), yielding the global floor statement for every \(n\ge1\).

_Proof source: `raw/student/20260605T-bridge-zeta-tail-s8-floor.md`._

## Tags

`application-bridge`, `inverse-tail-floor`, `proved`, `source-open-solved`, `telescoping-certificate`, `theorem`, `zeta-tail`
