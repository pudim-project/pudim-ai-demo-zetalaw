---
id: "T-YHL-k-digamma-alpha-le0-sufficient-CM-region"
type: "theorem"
title: "YHL weighted k-digamma alpha <= 0 sufficient CM region mu <= kc/2"
status: "proved"
tags: ["alpha-nonpositive", "complete-monotonicity", "k-digamma", "non-app-theory-growth", "proved", "student-audit", "sufficient-region", "theorem", "weighted"]
parents: ["T-Special-function-normal-form-calculus-principle", "T-YHL-k-digamma-base-alpha0-CM-classification"]
refs: ["librarian/audits/LA-20260603T153900-yhl-k-digamma-strict-app-audit.json", "raw/oracle/RO-OFC-20260603T-yhl-weighted-cm-strict-app-rerun.json", "raw/oracle/RO-OS-20260603T-yhl-weighted-cm-strict-app-temp.json", "raw/student/20260603T153900-yhl-k-digamma-strict-app-audit.md", "wiki/notes/frontier-yhl-k-digamma-weighted-cm.md"]
---

# Theorem: YHL weighted k-digamma alpha <= 0 sufficient CM region mu <= kc/2

## Statement

For positive \(k,a,b,c,d\), let \(B(x)=\psi_k(ax+b)-k\log(cx+d)\) and \(F_\alpha(x)=x^\alpha B(x)\). If \(\alpha\le0\) and \(\mu=kc+ad-bc\le kc/2\), then \(F_\alpha\) is completely monotonic on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]
- [[wiki/nodes/T-YHL-k-digamma-base-alpha0-CM-classification|YHL alpha zero k-digamma bracket CM iff mu <= kc/2]]

## Proof and provenance references

- `librarian/audits/LA-20260603T153900-yhl-k-digamma-strict-app-audit.json`
- `raw/oracle/RO-OFC-20260603T-yhl-weighted-cm-strict-app-rerun.json`
- `raw/oracle/RO-OS-20260603T-yhl-weighted-cm-strict-app-temp.json`
- `raw/student/20260603T153900-yhl-k-digamma-strict-app-audit.md`
- `wiki/notes/frontier-yhl-k-digamma-weighted-cm.md`

## Proof

This pass does not solve Yin--Huang--Lin Open Problem 4.1 and is not a strict APP candidate.

The admitted theory growth is the one-sided sufficient region:
\[
\alpha\le0,\qquad \mu=kc+ad-bc\le \frac{kc}{2}
\quad\Longrightarrow\quad
x^\alpha\left[\psi_k(ax+b)-k\log(cx+d)\right]\in CM(0,\infty).
\]

The full \(\alpha<0\) converse remains open.

Let
\[
B(x)=\psi_k(ax+b)-k\log(cx+d).
\]
The existing source-imported theorem the YHL k digamma base alpha0 CM classification states that \(B\) is completely monotonic if and only if
\[
\mu=kc+ad-bc\le \frac{kc}{2}.
\]

If \(\alpha=0\), this is exactly the source theorem.

If \(\alpha<0\), write \(\alpha=-r\) with \(r>0\). Then
\[
(-1)^n\frac{d^n}{dx^n}x^{-r}=(r)_n x^{-r-n}\ge0,
\]
so \(x^{-r}\) is completely monotonic. Products of completely monotonic functions are completely monotonic; therefore
\[
x^\alpha B(x)=x^{-r}B(x)
\]
is completely monotonic whenever \(B\) is.

For \(\alpha<0\), the converse would require
\[
x^{-r}B(x)\in CM(0,\infty)\quad\Longrightarrow\quad B(x)\in CM(0,\infty),
\]
or an equivalent kernel-level replacement. This implication is false for general functions and is not proved for the special \(k\)-digamma/log bracket.

\[
B(x)=\int_0^\infty e^{-xt}K(t)\,dt,
\]
then multiplication by \(x^{-r}\) corresponds formally to the fractional integral
\[
L_r(u)=\frac1{\Gamma(r)}\int_0^u (u-t)^{r-1}K(t)\,dt.
\]
Complete monotonicity of \(x^{-r}B(x)\) can follow from \(L_r\ge0\), which does not generally force \(K\ge0\). Thus the \(\alpha<0\) region may be strictly larger than the \(\alpha=0\) source region.

_Proof source: `raw/student/20260603T153900-yhl-k-digamma-strict-app-audit.md`._

## Tags

`alpha-nonpositive`, `complete-monotonicity`, `k-digamma`, `non-app-theory-growth`, `proved`, `student-audit`, `sufficient-region`, `theorem`, `weighted`
