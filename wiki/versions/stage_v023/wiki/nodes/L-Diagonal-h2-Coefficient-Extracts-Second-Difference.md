---
id: "L-Diagonal-h2-Coefficient-Extracts-Second-Difference"
type: "lemma"
title: "Diagonal h2 coefficient extracts Bernstein second differences"
status: "proved"
tags: ["bernstein-polynomial", "bridge-lemma", "coefficient-extraction", "finite-difference", "finite-kernel", "lemma", "primitive-growth", "proved", "true"]
parents: ["L-TwoBinomial-Diagonal-Generating-Kernel", "D-q-Monotone-Finite-Difference"]
refs: ["oracle/responses/OS-20260622T1312Z-alr-q2-bernstein-oracle-response.md", "raw/student/20260622T1318-alr-q2-bernstein-converse.md"]
---

# Lemma: Diagonal h2 coefficient extracts Bernstein second differences

## Statement

In the ALR \(q=2\) diagonal perturbation \(x=t+h,y=t-h\), the \(h^2\)-coefficient of the split kernel is \(-n(z-1)^2A_t(z)^{2n-2}\). Evaluated against \(F_k=f(k/(2n))\), the source inequality therefore forces the Bernstein weighted second-difference average \(\sum_{r=0}^{2n-2}p_{2n-2,r}(t)(F_{r+2}-2F_{r+1}+F_r)\ge0\).

## Dependencies

- [[wiki/nodes/L-TwoBinomial-Diagonal-Generating-Kernel|Two-binomial diagonal generating kernel]]
- [[wiki/nodes/D-q-Monotone-Finite-Difference|q-monotone finite-difference convention]]

## Proof and provenance references

- `oracle/responses/OS-20260622T1312Z-alr-q2-bernstein-oracle-response.md`
- `raw/student/20260622T1318-alr-q2-bernstein-converse.md`

## Proof

Assume \(f\in C[0,1]\) satisfies the source \(q=2\) inequality for all \(n\ge1\) and \(x,y\in[0,1]\). Fix \(n\ge1\), set
\[
F_k=f\left(\frac{k}{2n}\right),\qquad 0\le k\le2n,
\]
and define
\[
Q_n(x,y)=\sum_{i,j=0}^{n}p_{n,i}(x)p_{n,j}(y)
f\left(\frac{i+j}{2n}\right).
\]
By binomial convolution,
\[
Q_n(t,t)=\sum_{k=0}^{2n}p_{2n,k}(t)f\left(\frac{k}{2n}\right)
=(B_{2n}f)(t).
\]

For \(t\in(0,1)\), take \(x=t+h\), \(y=t-h\), with \(|h|<\min(t,1-t)\). The source inequality gives
\[
Q_n(t+h,t-h)\le Q_n(t,t).
\]
Let
\[
A_t(z)=1-t+tz,\qquad u=z-1.
\]
The generating function for \(i+j\), where \(i\sim\operatorname{Bin}(n,t+h)\) and \(j\sim\operatorname{Bin}(n,t-h)\), is
\[
(A_t(z)+hu)^n(A_t(z)-hu)^n
=\left(A_t(z)^2-h^2u^2\right)^n
=A_t(z)^{2n}-nh^2u^2A_t(z)^{2n-2}+O(h^4).
\]
Therefore
\[
Q_n(t+h,t-h)
=Q_n(t,t)
-nh^2\sum_{r=0}^{2n-2}p_{2n-2,r}(t)
\left(F_{r+2}-2F_{r+1}+F_r\right)
+O(h^4).
\]
Since \(Q_n(t+h,t-h)\le Q_n(t,t)\) for both positive and negative sufficiently small \(h\), the coefficient of \(h^2\) is nonpositive, hence
\[
\sum_{r=0}^{2n-2}p_{2n-2,r}(t)
\left[
f\left(\frac{r+2}{2n}\right)
-2f\left(\frac{r+1}{2n}\right)
+f\left(\frac{r}{2n}\right)
\right]\ge0.
\]

The Bernstein second derivative identity gives
\[
(B_{2n}f)''(t)=2n(2n-1)
\sum_{r=0}^{2n-2}p_{2n-2,r}(t)
\left[
f\left(\frac{r+2}{2n}\right)
-2f\left(\frac{r+1}{2n}\right)
+f\left(\frac{r}{2n}\right)
\right].
\]
Thus \((B_{2n}f)''(t)\ge0\) for every \(t\in(0,1)\). Since \(B_{2n}f\) is a polynomial, \(B_{2n}f\) is convex on \([0,1]\).

Bernstein's theorem gives \(B_{2n}f\to f\) uniformly on \([0,1]\). A uniform limit of convex functions is convex, so \(f\) is convex. Under the ALR source terminology, \(2\)-monotone means convex. Therefore the continuous \(q=2\) source subcase is affirmative.

_Proof source: `raw/student/20260622T1318-alr-q2-bernstein-converse.md`._

## Tags

`bernstein-polynomial`, `bridge-lemma`, `coefficient-extraction`, `finite-difference`, `finite-kernel`, `lemma`, `primitive-growth`, `proved`, `true`
