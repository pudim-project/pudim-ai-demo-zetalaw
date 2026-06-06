# Frontier Note: Ma-Weigert Log-Function Derivative Chain

## Status

Solved locally, pending any later public staging/review decision.

## Source Frontier

Ma and Weigert's Conjecture 4.6 asks for the derivative-sign regions \(D_k\) in
\[
\mathcal F_{1,n}=\left\{x\mapsto\frac{p(\log x)}{x}:p\in\mathbb R[y]_n\right\}
\]
to form a descending chain.

## Local Proof

Let \(L=-d/dx\).  For every \(f\in\mathcal F_{1,n}\),
\[
L^k f(x)=x^{-k-1}p_k(\log x)
\]
for a polynomial \(p_k\).  Hence \(L^k f(x)\to0\) as \(x\to\infty\).

If \(L^{k+1}f\ge0\), then
\[
L^k f(x)=\int_x^\infty L^{k+1}f(t)\,dt\ge0.
\]
Therefore \(D_{k+1}\subseteq D_k\).

## Boundary

This proves the nesting part of Conjecture 4.6.  It does not replace the source's semialgebraic complete-monotonicity cone description; it supplies a simple monotone-chain proof for the derivative-sign regions.
