---
id: "T-Q2-tail-404-173-gate"
type: "theorem"
title: "Z3(1/x)>x^(404/173) on (0,1), so L2 <= 404/173 and [404/173,3] subset I2"
status: "proved"
tags: ["attack-plan", "mixed", "overshoot-relaxation", "progress-route", "proved", "tail-gate", "theorem"]
parents: ["T-Finite-combinatorial-packing-shadow-principle"]
refs: ["raw/student/20260525T180514-q2-terminal-ap.md", "wiki/notes/frontier-q2-endpoint.md"]
---

# Theorem: Z3(1/x)>x^(404/173) on (0,1), so L2 <= 404/173 and [404/173,3] subset I2

## Statement

For all \(0<x<1\), \(Z_3(1/x)>x^{404/173}\); consequently \(L_2\le404/173<397/170\) and \([404/173,3]\subseteq\mathcal I_2\).

## Dependencies

- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `raw/student/20260525T180514-q2-terminal-ap.md`
- `wiki/notes/frontier-q2-endpoint.md`

## Proof

Use the Euler--Maclaurin lower gate already staged in the public vault:
\[
Z_3(1/x)>
\frac12x^2+\frac12x^3+\frac14x^4-\frac1{12}x^6
\qquad(0<x<1).
\]
Set \(y=x^{1/173}\). After multiplying the desired lower bound by the positive factor \(12y^{-346}\), it is enough to show
\[
P(y)=6+6y^{173}+3y^{346}-y^{692}-12y^{58}>0
\qquad(0<y<1).
\]

Compute
\[
P'(y)=2y^{57}H(y),
\]
where
\[
H(y)=519y^{115}+519y^{288}-346y^{634}-348.
\]
Also
\[
H'(y)=y^{114}J(y^{173}),
\]
with
\[
J(z)=59685+149472z-219364z^3.
\]
Since
\[
J'(z)=149472-658092z^2,
\]
the function \(J\) increases once and then decreases on \([0,1]\). With \(J(0)>0\) and \(J(1)<0\), \(J\) has one zero. Thus \(H\) increases and then decreases. Since \(H(0)=-348<0\) and \(H(1)=344>0\), \(H\) has exactly one zero in \((0,1)\). Hence \(P\) decreases once and then increases once, so its unique minimum occurs at the unique zero of \(H\).

Let
\[
A=\frac{99407}{100000},\qquad B=\frac{99408}{100000}.
\]
Exact rational arithmetic gives
\[
H(A)<0<H(B).
\]
Therefore the unique minimum of \(P\) lies in \((A,B)\). For \(y\in[A,B]\),
\[
P(y)\ge
6+6A^{173}+3A^{346}-B^{692}-12B^{58}.
\]
Exact rational arithmetic gives
\[
6+6A^{173}+3A^{346}-B^{692}-12B^{58}>0,
\]
with decimal value approximately
\[
0.007136631269815171.
\]
Therefore \(P(y)>0\) for all \(0<y<1\), proving the \(404/173\) tail gate.

For \(x\ge1\), the first term gives
\[
Z_3(1/x)>x^3\ge x^{404/173}.
\]
Combining this with the standard \(n=2\) reduction used in the staged tail-gate nodes gives
\[
\left[\frac{404}{173},3\right]\subseteq\mathcal I_2.
\]

_Proof source: `raw/student/20260525T180514-q2-terminal-ap.md`._

## Tags

`attack-plan`, `mixed`, `overshoot-relaxation`, `progress-route`, `proved`, `tail-gate`, `theorem`
