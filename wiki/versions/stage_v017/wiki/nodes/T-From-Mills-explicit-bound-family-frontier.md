---
id: "T-From-Mills-explicit-bound-family-frontier"
type: "theorem"
title: "From Mills ratio explicit all-L bound family solved after determinant bridge"
status: "proved"
tags: ["complete-monotonicity", "mills-ratio", "no-parameter-grind", "proved", "source-solving", "theorem"]
parents: ["T-From-Mills-all-L-alternating-r-bound-family", "D-Determinant-triangular-compression-language", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["private attack plan", "private librarian audit", "private librarian audit", "private Oracle response", "private proof note", "private proof note", "wiki/notes/frontier-from-mills-ratio.md"]
---

# Theorem: From Mills ratio explicit all-L bound family solved after determinant bridge

## Statement

After the Mills-ratio Laplace/complete-monotone normal form, derivative recurrence, and all-\(L\) determinant bridge, the remaining From frontier is solved by a closed, explicit alternating upper/lower bound family valid uniformly for all \(L\ge1\).

## Dependencies

- [[wiki/nodes/T-From-Mills-all-L-alternating-r-bound-family|From Mills ratio explicit alternating all-L upper and lower bound family]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `private proof note`
- `wiki/notes/frontier-from-mills-ratio.md`

## Proof

For the standard normal Mills ratio, the normalizing constants cancel:
\[
r(t)=\frac{\int_t^\infty e^{-z^2/2}\,dz}{e^{-t^2/2}}
=e^{t^2/2}\int_t^\infty e^{-z^2/2}\,dz.
\]
Put \(z=t+u\). Then
\[
r(t)=\int_0^\infty e^{-tu-u^2/2}\,du.
\]
For \(t>0\), differentiating under the integral gives
\[
(-1)^n r^{(n)}(t)=\int_0^\infty u^n e^{-tu-u^2/2}\,du>0.
\]
Thus \(r\) is completely monotone on \((0,\infty)\).

From the same integral,
\[
r'(t)=-\int_0^\infty u e^{-tu-u^2/2}\,du.
\]
Since
\[
\frac{d}{du}e^{-tu-u^2/2}=-(t+u)e^{-tu-u^2/2},
\]
integration over \([0,\infty)\) gives
\[
\int_0^\infty (t+u)e^{-tu-u^2/2}\,du=1.
\]
Therefore \(\int_0^\infty u e^{-tu-u^2/2}\,du=1-tr(t)\), and
\[
r'(t)=tr(t)-1.
\]

Set \(P_0=1\), \(Q_0=0\), and suppose
\[
r^{(n)}(t)=P_n(t)r(t)+Q_n(t).
\]
Differentiating and using \(r'=tr-1\),
\[
r^{(n+1)}(t)=(P_n'(t)+tP_n(t))r(t)+(Q_n'(t)-P_n(t)).
\]
Thus
\[
P_{n+1}=P_n'+tP_n,\qquad Q_{n+1}=Q_n'-P_n.
\]
This inductively gives the claimed polynomial recurrence.

For each integer \(L\ge0\), define
\[
f_L(t)=(-1)^L r^{(L)}(t)=\int_0^\infty u^L e^{-tu-u^2/2}\,du.
\]
This is a positive Laplace transform. Let
\[
a_j(t)=(-1)^j f_L^{(j)}(t)=\int_0^\infty u^{L+j}e^{-tu-u^2/2}\,du.
\]
Normalize the positive measure \(u^L e^{-tu-u^2/2}du\) to a probability law \(X\). Up to the positive factor \(a_0(t)^2\), the determinant expression is
\[
\mathbb E[X^4]-4\mathbb E[X^3]\mathbb E[X]+3\mathbb E[X^2]^2.
\]
With \(\mu=\mathbb E[X]\), this equals
\[
\mathbb E[(X-\mu)^4]+3\operatorname{Var}(X)^2\ge0.
\]
Hence
\[
f_L^{(4)}f_L-4f_L^{(3)}f_L'+3(f_L'')^2\ge0.
\]
Since \(f_L^{(j)}=(-1)^L r^{(L+j)}\), this is exactly
\[
r^{(L+4)}r^{(L)}-4r^{(L+3)}r^{(L+1)}+3(r^{(L+2)})^2\ge0.
\]

_Proof source: `private proof note`._

## Tags

`complete-monotonicity`, `mills-ratio`, `no-parameter-grind`, `proved`, `source-solving`, `theorem`
