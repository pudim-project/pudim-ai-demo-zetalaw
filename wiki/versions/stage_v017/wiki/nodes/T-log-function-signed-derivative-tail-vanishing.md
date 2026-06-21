---
id: "T-log-function-signed-derivative-tail-vanishing"
type: "theorem"
title: "log function signed derivative polynomial normal form and tail vanishing"
status: "proved"
tags: ["complete-monotonicity", "log-functions", "ma-weigert", "primitive", "proved", "signed-derivatives", "structural-tool", "tail-vanishing", "theorem"]
parents: ["D-Log-function-derivative-chain-language"]
refs: ["private attack plan", "private librarian audit", "private proof note", "wiki/notes/frontier-ma-weigert-log-function-chain.md"]
---

# Theorem: log function signed derivative polynomial normal form and tail vanishing

## Statement

For every \(f\in\mathcal F_{1,n}\), where \(f(x)=p(\log x)/x\), and every \(k\ge0\), the signed derivative \(L^k f\) with \(L=-d/dx\) has the form \(x^{-k-1}p_k(\log x)\) for a polynomial \(p_k\), and therefore \(L^k f(x)\to0\) as \(x\to\infty\).

## Dependencies

- [[wiki/nodes/D-Log-function-derivative-chain-language|Log-function derivative-sign regions]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`complete-monotonicity`, `log-functions`, `ma-weigert`, `primitive`, `proved`, `signed-derivatives`, `structural-tool`, `tail-vanishing`, `theorem`
