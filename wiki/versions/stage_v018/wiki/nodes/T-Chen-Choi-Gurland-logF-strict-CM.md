---
id: "T-Chen-Choi-Gurland-logF-strict-CM"
type: "theorem"
title: "Chen Choi Gurland log F strictly completely monotone"
status: "proved"
tags: ["chen-choi", "complete-monotonicity", "gurland-ratio", "open-problem-solved", "proved", "theorem"]
parents: ["T-Chen-Choi-Gurland-Euler-sum-normal-form", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["attack-plans/AP-20260531T034500-chen-choi-gurland-logcm.json", "oracle/responses/ORACLE-FI-20260531T-rolling-061-oracle-forage-response.md", "oracle/responses/ORACLE-OS-20260531T-chen-choi-gurland-logcm-oracle-response.md", "raw/scout/sources/chen-choi-gurland-logcm-source-status.md", "raw/source-cache/chen-choi-gurland-ratio/mia-20-43.pdf", "raw/source-cache/chen-choi-gurland-ratio/mia-20-43.txt", "raw/source-cache/chen-choi-gurland-ratio/mia-22-07-yang-zheng.txt", "raw/student/20260531T034500-chen-choi-gurland-logcm.md", "wiki/notes/frontier-chen-choi-gurland-logcm.md"]
---

# Theorem: Chen Choi Gurland log F strictly completely monotone

## Statement

For \(F(x)=\Gamma(1/x)\Gamma(3/x)/\Gamma(2/x)^2\), the function \(x\mapsto\log F(x)\) is strictly completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Chen-Choi-Gurland-Euler-sum-normal-form|Chen Choi Gurland Euler product sum normal form]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `attack-plans/AP-20260531T034500-chen-choi-gurland-logcm.json`
- `oracle/responses/ORACLE-FI-20260531T-rolling-061-oracle-forage-response.md`
- `oracle/responses/ORACLE-OS-20260531T-chen-choi-gurland-logcm-oracle-response.md`
- `raw/scout/sources/chen-choi-gurland-logcm-source-status.md`
- `raw/source-cache/chen-choi-gurland-ratio/mia-20-43.pdf`
- `raw/source-cache/chen-choi-gurland-ratio/mia-20-43.txt`
- `raw/source-cache/chen-choi-gurland-ratio/mia-22-07-yang-zheng.txt`
- `raw/student/20260531T034500-chen-choi-gurland-logcm.md`
- `wiki/notes/frontier-chen-choi-gurland-logcm.md`

## Proof

Let
\[
A(u)=2\log(u+2)-\log(u+1)-\log(u+3).
\]
Then \(A(u)>0\) for \(u>0\), since
\[
A(u)=\log\frac{(u+2)^2}{(u+1)(u+3)}
\]
and the numerator exceeds the denominator by \(1\).
Moreover
\[
A'(u)=\frac2{u+2}-\frac1{u+1}-\frac1{u+3}
=-\frac{2}{(u+1)(u+2)(u+3)}.
\]
Using
\[
\int_0^\infty e^{-ut}e^{-at}\,dt=\frac1{u+a},
\]
we get
\[
-A'(u)=\int_0^\infty e^{-ut}e^{-t}(1-e^{-t})^2\,dt.
\]
Since \(A(u)\to0\) as \(u\to\infty\), integration from \(u\) to infinity gives
\[
A(u)=\int_0^\infty e^{-ut}\frac{e^{-t}(1-e^{-t})^2}{t}\,dt.
\]
The density is positive, locally integrable at \(0\), and exponentially decaying at infinity. Hence \(A\) is strictly completely monotone.

Weierstrass' product gives
\[
\log\Gamma(z)=-\log z-\gamma z-
\sum_{m=1}^{\infty}\left(\log(1+z/m)-z/m\right).
\]
Put \(z=1/x\). In
\[
\log\Gamma(z)+\log\Gamma(3z)-2\log\Gamma(2z),
\]
the linear terms cancel. The logarithmic terms give \(\log(4/3)\). The summand at index \(m\) becomes
\[
\log\frac{(1+2z/m)^2}{(1+z/m)(1+3z/m)}
=\log\frac{(mx+2)^2}{(mx+1)(mx+3)}=A(mx).
\]
Thus
\[
\log F(x)=\log\frac43+\sum_{m=1}^{\infty}A(mx).
\]
For every compact \(x\in[\varepsilon,M]\) and every \(n\ge0\),
\[
\frac{d^n}{dx^n}A(mx)=m^nA^{(n)}(mx)=O_{n,\varepsilon}(m^{-2}),
\]
because the three-point second difference in \(A^{(n)}\) is \(O((mx)^{-n-2})\). Therefore the series may be differentiated termwise locally uniformly.

For \(n=0\), \(\log F(x)>0\) follows from \(\log(4/3)>0\) and \(A(mx)>0\). For \(n\ge1\),
\[
(-1)^n(\log F)^{(n)}(x)=
\sum_{m=1}^{\infty}m^n(-1)^nA^{(n)}(mx)>0.
\]
Therefore \(\log F\) is strictly completely monotone on \((0,\infty)\), proving Chen-Choi Conjecture 1.

_Proof source: `raw/student/20260531T034500-chen-choi-gurland-logcm.md`._

## Tags

`chen-choi`, `complete-monotonicity`, `gurland-ratio`, `open-problem-solved`, `proved`, `theorem`
