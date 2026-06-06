---
id: "T-Du-Wang-h3-not-monotone-outer-windows"
type: "theorem"
title: "Du Wang h3 not monotone outer parameter windows"
status: "proved"
tags: ["du-wang", "gamma", "monotonicity-obstruction", "partial-source-progress", "polygamma", "proved", "theorem"]
parents: ["T-Du-Wang-h31-endpoint-infinity-sign-profile"]
refs: ["attack-plans/AP-20260531T052346-du-wang-h3-outer-windows.json", "oracle/responses/ORACLE-OS-20260531T-du-wang-h3-outer-windows-oracle-response.md", "raw/scout/sources/du-wang-h3-outer-windows-source-status.md", "raw/student/20260531T053900-du-wang-h3-outer-windows.md", "wiki/notes/frontier-du-wang-h3-monotonicity.md"]
---

# Theorem: Du Wang h3 not monotone outer parameter windows

## Statement

For \(0<a<1/2\) or \(1<a<2\), Du-Wang's function \(h_3\) is not monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Du-Wang-h31-endpoint-infinity-sign-profile|Du Wang h31 endpoint infinity sign profile]]

## Proof and provenance references

- `attack-plans/AP-20260531T052346-du-wang-h3-outer-windows.json`
- `oracle/responses/ORACLE-OS-20260531T-du-wang-h3-outer-windows-oracle-response.md`
- `raw/scout/sources/du-wang-h3-outer-windows-source-status.md`
- `raw/student/20260531T053900-du-wang-h3-outer-windows.md`
- `wiki/notes/frontier-du-wang-h3-monotonicity.md`

## Proof

Open Problem 2 asks for the monotonicity property of
\[
h_3(x)=\frac{-x^2\psi'(x+a)+2x\psi(x+a)-2\log\Gamma(x+a)}{x}
\]
on \((0,\infty)\) for \(0<a<2\). The source proves strict increase for \(a\ge2\).

The admitted local partial result uses the source driver
\[
h_3'(x)=\frac{h_{31}(x+a)}{x^2},
\]
where
\[
h_{31}(t)=-(t-a)^3\psi''(t)+(t-a)^2\psi'(t)-2(t-a)\psi(t)+2\log\Gamma(t).
\]
The endpoint and infinity profile is
\[
h_{31}(a+)=2\log\Gamma(a),
\qquad
h_{31}(t)=(2a-1)\log t+O(1).
\]
Thus \(h_3\) is not monotone on \((0,\infty)\) for
\[
0<a<\frac12
\quad\text{or}\quad
1<a<2.
\]

Remaining frontier:
\[
\frac12\le a\le1.
\]
This note is partial theory growth only. Do not stage as a full application unless the middle window is solved or the source question is explicitly narrowed.

_Proof source: `wiki/notes/frontier-du-wang-h3-monotonicity.md`._

## Tags

`du-wang`, `gamma`, `monotonicity-obstruction`, `partial-source-progress`, `polygamma`, `proved`, `theorem`
