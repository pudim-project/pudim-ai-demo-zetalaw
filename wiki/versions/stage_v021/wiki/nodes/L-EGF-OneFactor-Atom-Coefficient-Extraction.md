---
id: "L-EGF-OneFactor-Atom-Coefficient-Extraction"
type: "lemma"
title: "One-factor atom EGF coefficient extraction"
status: "proved"
tags: ["bridge-lemma", "coefficient-extraction", "egf", "finite-certificate", "lemma", "primitive-growth", "proved", "true"]
parents: ["D-LP-EGF-Coefficient-Sequence", "T-Exact-finite-certificate-verification-principle"]
refs: ["oracle/responses/OS-20260622T1142Z-wangyang-lp-cm-repair-oracle-response.md", "raw/student/20260622T1148-wangyang-lp-cm-counterexample.md"]
---

# Lemma: One-factor atom EGF coefficient extraction

## Statement

For \(a,q>0\), if \((1+a x)e^{q x}=\sum_{n\ge0}\gamma_n x^n/n!\), then \(\gamma_n=q^n+a n q^{n-1}=q^n(1+(a/q)n)\).

## Dependencies

- [[wiki/nodes/D-LP-EGF-Coefficient-Sequence|Laguerre-Polya EGF coefficient sequence]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `oracle/responses/OS-20260622T1142Z-wangyang-lp-cm-repair-oracle-response.md`
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

## Tags

`bridge-lemma`, `coefficient-extraction`, `egf`, `finite-certificate`, `lemma`, `primitive-growth`, `proved`, `true`
