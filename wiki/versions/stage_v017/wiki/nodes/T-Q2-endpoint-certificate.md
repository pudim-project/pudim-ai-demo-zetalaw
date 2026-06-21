---
id: "T-Q2-endpoint-certificate"
type: "theorem"
title: "exists certified Q2 endpoint frontier advance below 397/170 or exact critical point determination"
status: "proved"
tags: ["current-source", "n-2", "open", "open-problem-4", "proved", "theorem"]
parents: ["T-Q2-critical-sign-certificate", "T-endpoint-log-derivative-monotonicity-principle", "T-Q2-interval-derivative-certificate", "T-Q2-tail-404-173-gate", "T-Q2-seven-thirds-tail-gate"]
refs: ["private librarian audit", "private proof note", "wiki/notes/frontier-q2-endpoint.md"]
---

# Theorem: exists certified Q2 endpoint frontier advance below 397/170 or exact critical point determination

## Statement

There exists a local certificate advancing the \(n=2\) endpoint frontier: either it determines \(L_2\) from the critical-point equation, or it proves an explicit strict improvement \(L_2\le\theta<397/170\).

## Dependencies

- [[wiki/nodes/T-Q2-critical-sign-certificate|unique G zero in B and global Q2 maximum at xi]]
- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]
- [[wiki/nodes/T-Q2-interval-derivative-certificate|finite rational interval certificate proves one crossing and outside Q2 bounds]]
- [[wiki/nodes/T-Q2-tail-404-173-gate|Z3(1/x)>x^(404/173) on (0,1), so L2 <= 404/173 and [404/173,3] subset I2]]
- [[wiki/nodes/T-Q2-seven-thirds-tail-gate|Z3(1/x)>x^(7/3) on (0,1), so L2 <= 7/3 and [7/3,3] subset I_2]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`current-source`, `n-2`, `open`, `open-problem-4`, `proved`, `theorem`
