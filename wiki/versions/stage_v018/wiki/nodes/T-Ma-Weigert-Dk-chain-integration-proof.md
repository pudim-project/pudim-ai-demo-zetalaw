---
id: "T-Ma-Weigert-Dk-chain-integration-proof"
type: "theorem"
title: "tail integration proves adjacent derivative sign region inclusion for Ma Weigert log functions"
status: "proved"
tags: ["complete-monotonicity", "integration-principle", "log-functions", "ma-weigert", "proved", "signed-derivatives", "theorem"]
parents: ["D-Log-function-derivative-chain-language", "T-log-function-signed-derivative-tail-vanishing"]
refs: ["attack-plans/AP-20260529T-next-loop-ma-weigert-log-chain.json", "librarian/audits/LA-20260529T-next-loop-ma-weigert-student.json", "raw/student/20260529T-next-loop-ma-weigert-log-chain.md", "wiki/notes/frontier-ma-weigert-log-function-chain.md"]
---

# Theorem: tail integration proves adjacent derivative sign region inclusion for Ma Weigert log functions

## Statement

For \(f\in\mathcal F_{1,n}\), if \(L^{k+1}f\ge0\) on \((0,\infty)\), then \(L^k f\ge0\) on \((0,\infty)\), because \(L^k f(x)=\int_x^\infty L^{k+1}f(t)\,dt\).

## Dependencies

- [[wiki/nodes/D-Log-function-derivative-chain-language|Log-function derivative-sign regions]]
- [[wiki/nodes/T-log-function-signed-derivative-tail-vanishing|log function signed derivative polynomial normal form and tail vanishing]]

## Proof and provenance references

- `attack-plans/AP-20260529T-next-loop-ma-weigert-log-chain.json`
- `librarian/audits/LA-20260529T-next-loop-ma-weigert-student.json`
- `raw/student/20260529T-next-loop-ma-weigert-log-chain.md`
- `wiki/notes/frontier-ma-weigert-log-function-chain.md`

## Proof

We first prove that for each \(k\ge0\),
\[
L^k f(x)=x^{-k-1}p_k(\log x)
\]
for some polynomial \(p_k\).

For \(k=0\), this is the definition with \(p_0=p\).  Suppose
\[
L^k f(x)=x^{-k-1}p_k(\log x).
\]
Then
\[
\begin{aligned}
L^{k+1}f(x)
&=-\frac{d}{dx}\left(x^{-k-1}p_k(\log x)\right)\\
&=x^{-k-2}\left((k+1)p_k(\log x)-p_k'(\log x)\right).
\end{aligned}
\]
Thus \(p_{k+1}(y)=(k+1)p_k(y)-p_k'(y)\), which is again a polynomial.

Since every polynomial in \(\log x\) grows slower than every positive power of \(x\),
\[
x^{-k-1}p_k(\log x)\to0
\qquad (x\to\infty).
\]
Therefore
\[
\lim_{x\to\infty}L^k f(x)=0
\]
for every \(k\ge0\).

Assume \(f\in D_{k+1}\).  Then
\[
L^{k+1}f(x)\ge0
\]
on \((0,\infty)\).  Put
\[
g(x)=L^k f(x).
\]
By definition of \(L\),
\[
-g'(x)=L^{k+1}f(x)\ge0.
\]
Using \(g(x)\to0\) as \(x\to\infty\), integrate from \(x\) to \(R\):
\[
g(x)-g(R)=\int_x^R L^{k+1}f(t)\,dt.
\]
Letting \(R\to\infty\) gives
\[
L^k f(x)=g(x)=\int_x^\infty L^{k+1}f(t)\,dt\ge0.
\]
Hence \(f\in D_k\).  Therefore
\[
D_{k+1}\subseteq D_k
\]
for all \(k\ge0\) and all \(n\).

_Proof source: `raw/student/20260529T-next-loop-ma-weigert-log-chain.md`._

## Tags

`complete-monotonicity`, `integration-principle`, `log-functions`, `ma-weigert`, `proved`, `signed-derivatives`, `theorem`
