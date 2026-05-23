---
id: mrw-ba29cdf1fd30
type: proposition
title: Finite-shadow reduction for Erdos residue-class logarithmic density
aliases: ["mrw-ba29cdf1fd30", "Finite-shadow reduction for Erdos residue-class logarithmic density"]
status: proved
tags: ["proposition", "proved", "erdos", "logarithmic-density", "modular-residue", "finite-shadow", "sieve"]
parents: [mrw-3d524c92103b, mrw-538319137c76, mrw-1ac4e44cbbad]
refs: ["references/sources/20260518T173138Z-erdos-residue-log-density.md", "references/sources/20260518T181156Z-davenport-erdos-multiples-benchmark.md"]
---

# Proposition: Finite-shadow reduction for Erdos residue-class logarithmic density

## Statement

Let
\[
1\le n_1<n_2<\cdots
\]
and choose one residue class \(a_i\pmod {n_i}\) for each \(i\).  Define
\[
B=\{m\in\mathbb N:\ m<n_i\text{ or }m\not\equiv a_i\pmod {n_i}\text{ for every }i\}.
\]
For \(N\ge1\), put
\[
B_N=\{m\in\mathbb N:\ m<n_i\text{ or }m\not\equiv a_i\pmod {n_i}\text{ for every }1\le i\le N\},
\]
let
\[
L_N=\operatorname{lcm}(n_1,\ldots,n_N),
\]
and let \(C_N\subseteq\mathbb Z/L_N\mathbb Z\) be the set of residue classes \(r\) satisfying
\[
r\not\equiv a_i\pmod {n_i}\qquad(1\le i\le N).
\]
For a set \(S\subseteq\mathbb N\), define the harmonic logarithmic average
\[
\mu_x(S)=\frac1{\log x}\sum_{\substack{m<x\\m\in S}}\frac1m.
\]
Then the finite-shadow logarithmic density
\[
\delta_N=\lim_{x\to\infty}\mu_x(B_N)
\]
exists and is
\[
\delta_N=\frac{|C_N|}{L_N}.
\]
Moreover, \((\delta_N)\) is nonincreasing, so
\[
\delta=\lim_{N\to\infty}\delta_N
\]
exists.  The full set \(B\) always satisfies
\[
\overline d_{\log}(B):=\limsup_{x\to\infty}\mu_x(B)\le\delta.
\]
Consequently, if \(\delta=0\), then \(B\) has logarithmic density \(0\).

Finally, if the tail defect
\[
E_N=B_N\setminus B
\]
satisfies
\[
\lim_{N\to\infty}\limsup_{x\to\infty}\mu_x(E_N)=0,
\]
then \(B\) has logarithmic density \(\delta\).

## Proof

Fix \(N\).  For \(m\ge n_N\), all finite restrictions in the definition of \(B_N\) are active, and therefore
\[
m\in B_N
\quad\Longleftrightarrow\quad
m\bmod L_N\in C_N.
\]
The discrepancy between \(B_N\) and this periodic residue set is contained in the finite interval \(\{1,\ldots,n_N-1\}\), whose contribution to \(\mu_x\) is \(O_N(1/\log x)\).

It remains to recall the elementary harmonic density of a fixed set of residue classes.  If \(L\ge1\) and \(C\subseteq\mathbb Z/L\mathbb Z\), then
\[
\sum_{\substack{m<x\\m\bmod L\in C}}\frac1m
=\frac{|C|}{L}\log x+O_L(1).
\]
Indeed, for each class \(r\), the sum over \(m\equiv r\pmod L\) is, up to a bounded initial convention when \(r=0\),
\[
\sum_{k\le x/L}\frac1{Lk+r}
=\frac1L\log x+O_L(1).
\]
Summing over \(r\in C\) and dividing by \(\log x\) gives
\[
\lim_{x\to\infty}\mu_x(B_N)=\frac{|C_N|}{L_N}.
\]

Since \(B_{N+1}\subseteq B_N\), we have \(C_{N+1}\) projecting into \(C_N\), and the densities satisfy \(\delta_{N+1}\le\delta_N\).  Thus \(\delta=\inf_N\delta_N\) exists.  Also \(B\subseteq B_N\) for every \(N\), so
\[
\limsup_{x\to\infty}\mu_x(B)
\le
\lim_{x\to\infty}\mu_x(B_N)=\delta_N.
\]
Taking the infimum over \(N\) gives
\[
\overline d_{\log}(B)\le\delta.
\]
If \(\delta=0\), this forces \(\mu_x(B)\to0\), proving logarithmic density \(0\).

For the tail criterion, write
\[
B=B_N\setminus E_N.
\]
Then
\[
\mu_x(B)=\mu_x(B_N)-\mu_x(E_N).
\]
Taking lower limits in \(x\) gives
\[
\liminf_{x\to\infty}\mu_x(B)
\ge
\delta_N-\limsup_{x\to\infty}\mu_x(E_N).
\]
Letting \(N\to\infty\) and using the assumed vanishing tail defect yields
\[
\liminf_{x\to\infty}\mu_x(B)\ge\delta.
\]
Together with the upper bound \(\limsup_x\mu_x(B)\le\delta\), this proves that the logarithmic density of \(B\) exists and equals \(\delta\).

## Depends on

- [[wiki/nodes/mrw-3d524c92103b|Erdos residue-class logarithmic-density problem]]
- [[wiki/nodes/mrw-538319137c76|Modular residue distribution and successor entropy]]
- [[wiki/nodes/mrw-1ac4e44cbbad|Zeta-law successor entropy and modular resolution]]

## Used by

- [[wiki/nodes/mrw-f92c897044c4|Union-tail criterion for Erdos residue-class logarithmic density]]
- [[wiki/nodes/mrw-171478aeed08|Essential-index tail criterion for Erdos residue-class logarithmic density]]
- [[wiki/nodes/mrw-e0778085804e|Block-uniform first-hit criterion for Erdos residue-class logarithmic density]]
- [[wiki/nodes/mrw-536639208ce1|Escaping first-hit mass obstruction for finite-shadow decrement control]]

## Notes

- This does not solve Erdos Problem #25 in full.  It solves the zero finite-shadow case and reduces the positive finite-shadow case to a tail-continuity problem.
- The obstruction is not finite computation of \(\delta_N\); the obstruction is passing from fixed finite shadows \(B_N\) to the infinite intersection \(B\).
- The block-uniform criterion shows one sufficient way to pass from finite-shadow decrements to the infinite tail.  The escaping-mass obstruction shows why the decrement sequence alone cannot justify this passage without uniformity.
