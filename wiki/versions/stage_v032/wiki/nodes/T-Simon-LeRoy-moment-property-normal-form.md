---
id: "T-Simon-LeRoy-moment-property-normal-form"
type: "theorem"
title: "Simon moment property gives entire moment generating normal form"
status: "proved"
tags: ["attack-plan", "complete-monotonicity", "gamma-ratio", "mellin-transform", "mittag-leffler", "proved", "stieltjes-moment", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle"]
refs: ["attack-plans/AP-20260528T154000-simon-leroy-ml-cm.json", "librarian/audits/LA-20260528T154500-simon-leroy-student.json", "raw/student/20260528T154500-simon-leroy-ml-cm.md", "wiki/notes/frontier-simon-leroy-mittag-leffler-cm.md"]
---

# Theorem: Simon moment property gives entire moment generating normal form

## Statement

For \(\alpha,\beta,\gamma>0\), if Simon's moment property \(M_{\alpha,\beta,\gamma}\) holds for a positive random variable \(X\), then \((\Gamma(\beta))^\gamma F^{(\gamma)}_{\alpha,\beta}(z)={\bf E}[e^{zX}]\) for every \(z\in\mathbb C\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `attack-plans/AP-20260528T154000-simon-leroy-ml-cm.json`
- `librarian/audits/LA-20260528T154500-simon-leroy-student.json`
- `raw/student/20260528T154500-simon-leroy-ml-cm.md`
- `wiki/notes/frontier-simon-leroy-mittag-leffler-cm.md`

## Proof

\emph{Setup.}
Let
\[
F^{(\gamma)}_{\alpha,\beta}(z)
=\sum_{n\ge0}\frac{z^n}{\Gamma(\beta+\alpha n)^\gamma},
\qquad \alpha,\beta,\gamma>0.
\]

Assume Simon's moment property \(M_{\alpha,\beta,\gamma}\): there is a positive random variable \(X\) with
\[
{\bf E}[X^s]
=\Gamma(1+s)\left(\frac{\Gamma(\beta)}{\Gamma(\beta+\alpha s)}\right)^\gamma,
\qquad s>0.
\]

For \(n\ge0\), this gives
\[
{\bf E}[X^n]
=n!\left(\frac{\Gamma(\beta)}{\Gamma(\beta+\alpha n)}\right)^\gamma.
\]

Set
\[
a_n=\left(\frac{\Gamma(\beta)}{\Gamma(\beta+\alpha n)}\right)^\gamma.
\]
By the standard Gamma-ratio asymptotic,
\[
\frac{a_{n+1}}{a_n}
=\left(\frac{\Gamma(\beta+\alpha n)}{\Gamma(\beta+\alpha(n+1))}\right)^\gamma
\sim (\alpha n)^{-\alpha\gamma}\to0.
\]
Hence \(\sum_{n\ge0}a_n z^n\) has infinite radius of convergence.

For \(t\ge0\), monotone convergence gives
\[
{\bf E}[e^{tX}]
=\sum_{n\ge0}\frac{t^n{\bf E}[X^n]}{n!}
=\sum_{n\ge0}a_n t^n
=(\Gamma(\beta))^\gamma F^{(\gamma)}_{\alpha,\beta}(t).
\]
The right-hand side is finite for every \(t\ge0\). Therefore \(e^{|z|X}\) is integrable for every \(z\in\mathbb C\), and dominated convergence gives
\[
{\bf E}[e^{zX}]
=\sum_{n\ge0}\frac{z^n{\bf E}[X^n]}{n!}
=(\Gamma(\beta))^\gamma F^{(\gamma)}_{\alpha,\beta}(z),
\qquad z\in\mathbb C.
\]

This proves the Simon LeRoy moment property normal form.

For \(x>0\), substituting \(z=-x\) yields
\[
F^{(\gamma)}_{\alpha,\beta}(-x)
=\Gamma(\beta)^{-\gamma}{\bf E}[e^{-xX}].
\]
This is a positive Laplace transform. More explicitly, for every \(k\ge0\),
\[
(-1)^k\frac{d^k}{dx^k}F^{(\gamma)}_{\alpha,\beta}(-x)
=\Gamma(\beta)^{-\gamma}{\bf E}[X^k e^{-xX}]\ge0,
\]
where differentiating under the expectation is justified on compact subintervals of \((0,\infty)\) by the finite moment \({\bf E}[X^k]\).

Thus \(x\mapsto F^{(\gamma)}_{\alpha,\beta}(-x)\) is completely monotone on \((0,\infty)\). This proves the Simon LeRoy moment property implies CM.

_Proof source: `raw/student/20260528T154500-simon-leroy-ml-cm.md`._

## Tags

`attack-plan`, `complete-monotonicity`, `gamma-ratio`, `mellin-transform`, `mittag-leffler`, `proved`, `stieltjes-moment`, `theorem`
