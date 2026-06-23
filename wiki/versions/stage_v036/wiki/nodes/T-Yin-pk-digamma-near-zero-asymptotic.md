---
id: "T-Yin-pk-digamma-near-zero-asymptotic"
type: "theorem"
title: "Yin p,k-digamma bracket near zero asymptotic x inverse"
status: "proved"
tags: ["attack-plan", "complete-monotonicity", "digamma", "endpoint-asymptotic", "proved", "theorem"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["attack-plans/AP-20260528T170500-yin-pk-digamma-alpha-necessity.json", "librarian/audits/LA-20260528T171000-yin-pk-student.json", "raw/student/20260528T171000-yin-pk-digamma-alpha-necessity.md", "wiki/notes/frontier-yin-pk-digamma-alpha-necessity.md"]
---

# Theorem: Yin p,k-digamma bracket near zero asymptotic x inverse

## Statement

For fixed \(p\in\mathbb N\) and \(k>0\), the Yin bracket satisfies \(B_{p,k}(x)=x^{-1}+O(|\log x|)\) as \(x\to0^+\). Consequently \(x^\alpha B_{p,k}(x)\sim x^{\alpha-1}\).

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `attack-plans/AP-20260528T170500-yin-pk-digamma-alpha-necessity.json`
- `librarian/audits/LA-20260528T171000-yin-pk-student.json`
- `raw/student/20260528T171000-yin-pk-digamma-alpha-necessity.md`
- `wiki/notes/frontier-yin-pk-digamma-alpha-necessity.md`

## Proof

\emph{Setup.}
Fix \(p\in\mathbb N\) and \(k>0\). Define
\[
B_{p,k}(x)=
\frac1k\log\frac{pkx}{x+k(p+1)}-\psi_{p,k}(x),
\qquad
\delta_{p,k,\alpha}(x)=x^\alpha B_{p,k}(x).
\]

The source gives the finite formula
\[
\psi_{p,k}(x)=\frac1k\log(pk)-\sum_{n=0}^p\frac1{x+nk}.
\]
Therefore
\[
\begin{aligned}
B_{p,k}(x)
&=
\frac1k\log\frac{pkx}{x+k(p+1)}
-\frac1k\log(pk)
+\sum_{n=0}^p\frac1{x+nk}  \\
&=
\frac1k\log\frac{x}{x+k(p+1)}
+\sum_{n=0}^p\frac1{x+nk}.
\end{aligned}
\]

This normal form also gives positivity directly. Put \(t=x/k\). Then
\[
B_{p,k}(x)
=\frac1k\left[
\sum_{n=0}^p\frac1{t+n}
+\log\frac{t}{t+p+1}
\right].
\]
Since
\[
\log\frac{t+p+1}{t}=\int_0^{p+1}\frac{du}{t+u},
\]
and \(u\mapsto(t+u)^{-1}\) is strictly decreasing, the left Riemann sum dominates:
\[
\sum_{n=0}^p\frac1{t+n}
>
\int_0^{p+1}\frac{du}{t+u}.
\]
Hence \(B_{p,k}(x)>0\) for \(x>0\).

This yields \(B_{p,k}(x)>0\) for all \(x>0\), i.e. the finite-normal-form positivity claim needed for the endpoint obstruction.

From the finite normal form,
\[
B_{p,k}(x)
=\frac1x
+\frac1k\log\frac{x}{x+k(p+1)}
+\sum_{n=1}^p\frac1{x+nk}.
\]

As \(x\to0^+\), the finite sum over \(n\ge1\) is \(O(1)\), and
\[
\frac1k\log\frac{x}{x+k(p+1)}=O(|\log x|).
\]
Thus
\[
B_{p,k}(x)=\frac1x+O(|\log x|)
\qquad (x\to0^+).
\]
Equivalently,
\[
xB_{p,k}(x)\to1.
\]
Therefore
\[
\delta_{p,k,\alpha}(x)
=x^\alpha B_{p,k}(x)
=x^{\alpha-1}(xB_{p,k}(x))
\sim x^{\alpha-1}.
\]

This yields the near-zero asymptotic \(xB_{p,k}(x)\to1\), i.e. \(B_{p,k}(x)\sim x^{-1}\) as \(x\to0^+\).

Assume that \(\delta_{p,k,\alpha}\) is completely monotone on \((0,\infty)\). Then
\[
\delta_{p,k,\alpha}(x)\ge0,\qquad
\delta_{p,k,\alpha}'(x)\le0.
\]
Since \(B_{p,k}(x)>0\), the function \(\delta_{p,k,\alpha}\) is actually positive for every \(x>0\).

Suppose, for contradiction, that \(\alpha>1\). The endpoint asymptotic gives
\[
\lim_{x\to0^+}\delta_{p,k,\alpha}(x)=0.
\]
Fix \(x_0>0\). Positivity gives \(\delta_{p,k,\alpha}(x_0)>0\). Because \(\delta_{p,k,\alpha}(x)\to0\) as \(x\to0^+\), choose \(0<y<x_0\) with
\[
\delta_{p,k,\alpha}(y)<\frac12\delta_{p,k,\alpha}(x_0).
\]
But \(\delta_{p,k,\alpha}'\le0\) means the function is nonincreasing as \(x\) increases, hence for \(0<y<x_0\),
\[
\delta_{p,k,\alpha}(y)\ge\delta_{p,k,\alpha}(x_0),
\]
a contradiction.

Therefore \(\alpha\le1\).

This contradiction argument gives \(\alpha\le1\), and thus the claimed open-problem conclusion follows.

_Proof source: `raw/student/20260528T171000-yin-pk-digamma-alpha-necessity.md`._

## Tags

`attack-plan`, `complete-monotonicity`, `digamma`, `endpoint-asymptotic`, `proved`, `theorem`
