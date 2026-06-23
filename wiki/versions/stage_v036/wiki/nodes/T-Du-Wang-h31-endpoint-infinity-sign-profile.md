---
id: "T-Du-Wang-h31-endpoint-infinity-sign-profile"
type: "theorem"
title: "Du Wang h31 endpoint infinity sign profile"
status: "proved"
tags: ["du-wang", "endpoint-asymptotic", "gamma", "monotonicity-obstruction", "polygamma", "proved", "theorem"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["attack-plans/AP-20260531T052346-du-wang-h3-outer-windows.json", "oracle/responses/ORACLE-OS-20260531T-du-wang-h3-outer-windows-oracle-response.md", "raw/scout/sources/du-wang-h3-outer-windows-source-status.md", "raw/student/20260531T053900-du-wang-h3-outer-windows.md", "wiki/notes/frontier-du-wang-h3-monotonicity.md"]
---

# Theorem: Du Wang h31 endpoint infinity sign profile

## Statement

For Du-Wang's driver \(h_{31}(t)=-(t-a)^3\psi''(t)+(t-a)^2\psi'(t)-2(t-a)\psi(t)+2\log\Gamma(t)\), one has \(h_{31}(a+)=2\log\Gamma(a)\) and \(h_{31}(t)=(2a-1)\log t+O(1)\) as \(t\to\infty\).

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

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

`du-wang`, `endpoint-asymptotic`, `gamma`, `monotonicity-obstruction`, `polygamma`, `proved`, `theorem`
