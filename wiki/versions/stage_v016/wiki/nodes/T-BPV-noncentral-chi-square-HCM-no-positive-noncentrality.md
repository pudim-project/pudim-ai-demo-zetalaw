---
id: "T-BPV-noncentral-chi-square-HCM-no-positive-noncentrality"
type: "theorem"
title: "BPV noncentral chi square HCM no positive noncentrality"
status: "proved"
tags: ["HCM", "app-0047-candidate", "application-candidate", "baricz-prabhu-singh-vijesh", "laguerre", "modified-bessel", "noncentral-chi-square", "proved", "source-open-solved", "source-solving-tool", "theorem"]
parents: ["T-BPV-noncentral-chi-square-HCM-leading-Bell-obstruction-chain", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Hyperbolically-completely-monotone-language"]
refs: ["librarian/audits/LA-20260531T062900-noncentral-chi-square-hcm.json", "librarian/audits/LA-20260604T-noncentral-chi-square-higher-small-u-obstructions.json", "librarian/audits/LA-20260605T-bpv-noncentral-chi-square-laguerre-total-obstruction.json", "raw/oracle/RO-ORACLE-OS-20260531T-noncentral-chi-square-hcm.json", "raw/scout/sources/bpv-noncentral-chi-square-hcm-source-status.md", "raw/student/20260605T-bpv-noncentral-chi-square-laguerre-total-obstruction.md", "wiki/notes/frontier-noncentral-chi-square-hcm.md"]
---

# Theorem: BPV noncentral chi square HCM no positive noncentrality

## Statement

For every \(\mu>0\) and every positive noncentrality \(\lambda>0\), the noncentral chi-square density \(\chi_{\mu,\lambda}\) is not hyperbolically completely monotone. Equivalently, the BPV optimal HCM range for positive noncentrality is empty; if the central case \(\lambda=0\) is adjoined, the remaining HCM range is exactly the central gamma line.

## Dependencies

- [[wiki/nodes/T-BPV-noncentral-chi-square-HCM-leading-Bell-obstruction-chain|noncentral chi square HCM leading Bell obstruction chain]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Hyperbolically-completely-monotone-language|Hyperbolically completely monotone density]]

## Proof and provenance references

- `librarian/audits/LA-20260531T062900-noncentral-chi-square-hcm.json`
- `librarian/audits/LA-20260604T-noncentral-chi-square-higher-small-u-obstructions.json`
- `librarian/audits/LA-20260605T-bpv-noncentral-chi-square-laguerre-total-obstruction.json`
- `raw/oracle/RO-ORACLE-OS-20260531T-noncentral-chi-square-hcm.json`
- `raw/scout/sources/bpv-noncentral-chi-square-hcm-source-status.md`
- `raw/student/20260605T-bpv-noncentral-chi-square-laguerre-total-obstruction.md`
- `wiki/notes/frontier-noncentral-chi-square-hcm.md`

## Proof

Let \(a=\mu/2>0\). The complete Bell generating function is
\[
\sum_{n\ge0}\frac{B_nz^n}{n!}
=\exp\left(\sum_{j\ge1}\frac{c_jz^j}{j!}\right)
=e^{-z/2}S_\mu(\lambda z).
\]
Indeed \(b_1(\mu)=1/(2\mu)\), so the \(j=1\) term of \(\log S_\mu(\lambda z)\) contributes \(\lambda z/(2\mu)\), and the exponential factor \(e^{-z/2}\) supplies the remaining \(-z/2\).

Define
\[
A_n=\frac{(-1)^nB_n}{n!}.
\]
Then
\[
\sum_{n\ge0}A_nt^n
=e^{t/2}S_\mu(-\lambda t)
=e^{t/2}\,{}_0F_1\left(;a;-\frac{\lambda t}{4}\right).
\]
Equivalently,
\[
A_n=\frac{2^{-n}}{(a)_n}L_n^{a-1}\left(\frac{\lambda}{2}\right),
\]
so the leading HCM signs are exactly the fixed-argument Laguerre signs.

Use the classical identity
\[
{}_0F_1\left(;a;-\frac{x^2}{4}\right)
=\Gamma(a)\left(\frac{x}{2}\right)^{1-a}J_{a-1}(x).
\]
Since \(a>0\), the Bessel function \(J_{a-1}\) has a positive real zero \(j_{a-1,1}>0\). For \(\lambda>0\), set
\[
t_0=\frac{j_{a-1,1}^2}{\lambda}>0.
\]
Then
\[
e^{t_0/2}{}_0F_1\left(;a;-\frac{\lambda t_0}{4}\right)=0.
\]
If every leading HCM sign were nonnegative, then all coefficients \(A_n\) would be nonnegative and \(A_0=1\), forcing
\[
\sum_{n\ge0}A_nt_0^n>0,
\]
contradicting the displayed zero. Therefore, for every \(\mu>0\) and \(\lambda>0\), there is an integer \(n\ge1\) such that
\[
(-1)^nB_n<0.
\]

The leading expansion gives, for any fixed compact \(w\)-window,
\[
\frac{1}{H_u(w)}\frac{d^n}{dw^n}H_u(w)
=B_nu^n+O(u^{n+1})
\qquad(u\downarrow0).
\]
Choosing \(u>0\) sufficiently small yields
\[
(-1)^n\frac{d^n}{dw^n}H_u(w)<0,
\]
which violates complete monotonicity of \(w\mapsto H_u(w)\).

\emph{Conclusion.}
For every \(\mu>0\) and every positive noncentrality \(\lambda>0\),
\[
\chi_{\mu,\lambda}\notin HCM.
\]
Thus the BPV optimal HCM range for positive noncentrality is empty. If one adjoins the central case \(\lambda=0\), the remaining density is a gamma density and is HCM; hence the extended closed range is exactly the central line \(\lambda=0\).

Strict APP status: candidate for the next APP slot after APP-0046 because the source explicitly asks the optimal range, the local theorem answers it, and the result is not among public APP-0001--APP-0045.

_Proof source: `raw/student/20260605T-bpv-noncentral-chi-square-laguerre-total-obstruction.md`._

## Tags

`HCM`, `app-0047-candidate`, `application-candidate`, `baricz-prabhu-singh-vijesh`, `laguerre`, `modified-bessel`, `noncentral-chi-square`, `proved`, `source-open-solved`, `source-solving-tool`, `theorem`
