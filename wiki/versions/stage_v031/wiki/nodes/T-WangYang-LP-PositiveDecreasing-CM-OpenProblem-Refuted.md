---
id: "T-WangYang-LP-PositiveDecreasing-CM-OpenProblem-Refuted"
type: "theorem"
title: "Wang-Yang LP positive-decreasing coefficient problem is false"
status: "proved"
tags: ["app-0085-candidate", "app-candidate", "complete-monotonicity", "finite-certificate", "finite-difference", "laguerre-polya", "negative-answer", "primitive-growth", "proved", "source-open-solved", "theorem", "true"]
parents: ["O-WangYang-LP-PositiveDecreasing-CM-source-gate", "D-LP-EGF-Coefficient-Sequence", "D-ForwardDifference-CompleteMonotone-Sequence", "L-LP-OneFactor-Exponential-Atom", "L-EGF-OneFactor-Atom-Coefficient-Extraction", "L-EGF-OneFactor-Atom-Decreasing-Window", "L-EGF-OneFactor-Atom-SecondDifference-Defect"]
refs: ["librarian/audits/LA-20260622T1128-wangyang-lp-cm-first-contact.json", "librarian/audits/LA-20260622T1152-wangyang-lp-cm-strict-app.json", "oracle/responses/OS-20260622T1142Z-wangyang-lp-cm-repair-oracle-response.md", "raw/oracle/RO-OS-20260622T1142Z-wangyang-lp-cm-repair.json", "raw/student/20260622T1148-wangyang-lp-cm-counterexample.md"]
---

# Theorem: Wang-Yang LP positive-decreasing coefficient problem is false

## Statement

The Wang--Yang open problem after Conjectures 1.10--1.11 has a negative answer. The Laguerre--Polya function \(\psi(x)=(1+4x/15)e^{2x/3}=\sum_{n\ge0}\gamma_n x^n/n!\) has positive strictly decreasing coefficients \(\gamma_n=(1+2n/5)(2/3)^n\), but under the source convention \(\Delta=E-1\), \(\Delta^2\gamma_1=-2/135<0\).

## Dependencies

- [[wiki/nodes/O-WangYang-LP-PositiveDecreasing-CM-source-gate|Wang-Yang Laguerre-Polya coefficient complete-monotonicity source gate]]
- [[wiki/nodes/D-LP-EGF-Coefficient-Sequence|Laguerre-Polya EGF coefficient sequence]]
- [[wiki/nodes/D-ForwardDifference-CompleteMonotone-Sequence|Forward-difference complete monotone sequence]]
- [[wiki/nodes/L-LP-OneFactor-Exponential-Atom|One-factor exponential atom is Laguerre-Polya]]
- [[wiki/nodes/L-EGF-OneFactor-Atom-Coefficient-Extraction|One-factor atom EGF coefficient extraction]]
- [[wiki/nodes/L-EGF-OneFactor-Atom-Decreasing-Window|One-factor atom decreasing coefficient window]]
- [[wiki/nodes/L-EGF-OneFactor-Atom-SecondDifference-Defect|One-factor atom second-difference defect]]

## Proof and provenance references

- `librarian/audits/LA-20260622T1128-wangyang-lp-cm-first-contact.json`
- `librarian/audits/LA-20260622T1152-wangyang-lp-cm-strict-app.json`
- `oracle/responses/OS-20260622T1142Z-wangyang-lp-cm-repair-oracle-response.md`
- `raw/oracle/RO-OS-20260622T1142Z-wangyang-lp-cm-repair.json`
- `raw/student/20260622T1148-wangyang-lp-cm-counterexample.md`

## Proof

Let
\[
\psi(x)=\left(1+\frac{4x}{15}\right)e^{2x/3}.
\]
This is in the Laguerre--Polya class: it is an exponential times a real-zero linear factor with zero \(-15/4\). In the source product normalization,
\[
\left(1+\frac{4x}{15}\right)e^{2x/3}
=e^{14x/15}\left(1+\frac{x}{15/4}\right)e^{-x/(15/4)}.
\]

For a one-factor atom
\[
(1+a x)e^{q x}=\sum_{n\ge0}\gamma_n\frac{x^n}{n!},
\]
the EGF coefficients are
\[
\gamma_n=q^n+a n q^{n-1}
=q^n\left(1+\frac{a}{q}n\right).
\]
With \(q=2/3\) and \(a=4/15\),
\[
\gamma_n=\left(1+\frac{2n}{5}\right)\left(\frac23\right)^n.
\]

The coefficients are positive. They are strictly decreasing because
\[
\gamma_n-\gamma_{n+1}
=\left(\frac23\right)^n\frac{2n+1}{15}>0
\qquad(n\ge0).
\]

The second source-forward difference is
\[
\Delta^2\gamma_n=\gamma_{n+2}-2\gamma_{n+1}+\gamma_n
=\left(\frac23\right)^n\frac{2n-3}{45}.
\]
In particular,
\[
\gamma_1=\frac{14}{15},\qquad
\gamma_2=\frac45,\qquad
\gamma_3=\frac{88}{135},
\]
and hence
\[
\Delta^2\gamma_1
=\frac{88}{135}-2\cdot\frac45+\frac{14}{15}
=-\frac{2}{135}<0.
\]
Since \((-1)^2\Delta^2\gamma_1=\Delta^2\gamma_1\), the proposed universal positivity fails already at \(r=2,n=1\).

_Proof source: `raw/student/20260622T1148-wangyang-lp-cm-counterexample.md`._

## Do not claim

- Do not claim a result about Riemann Xi coefficients themselves.
- Do not claim a result about the logarithmic coefficient Conjecture 1.11.
- Do not use the off-target Student run RO-OS-20260622T1131Z-wangyang-lp-cm as proof evidence.
- Do not public-stage without explicit user request.

## Tags

`app-0085-candidate`, `app-candidate`, `complete-monotonicity`, `finite-certificate`, `finite-difference`, `laguerre-polya`, `negative-answer`, `primitive-growth`, `proved`, `source-open-solved`, `theorem`, `true`
