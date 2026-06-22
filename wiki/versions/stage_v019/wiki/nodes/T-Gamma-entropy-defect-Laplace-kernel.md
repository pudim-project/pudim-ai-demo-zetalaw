---
id: "T-Gamma-entropy-defect-Laplace-kernel"
type: "theorem"
title: "standardized gamma Gaussian entropy defect has positive Laplace kernel and is completely monotone"
status: "proved"
tags: ["attack-plan", "diagnostic", "entropy", "gamma", "laplace-kernel", "mixed", "proved", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["librarian/audits/LA-20260528T112000-yu-gamma-entropy-kernel.json", "raw/student/20260528T111500-yu-gamma-entropy-kernel.md", "wiki/notes/frontier-yu-entropy-defect-cm.md"]
---

# Theorem: standardized gamma Gaussian entropy defect has positive Laplace kernel and is completely monotone

## Statement

For the standardized gamma law with shape parameter \(\alpha>0\), the Gaussian entropy defect \(D_\Gamma(\alpha)=\frac12\log(2\pi e)-H_g(\alpha)\) has a positive Laplace representation in \(\alpha\), and hence is completely monotone.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `librarian/audits/LA-20260528T112000-yu-gamma-entropy-kernel.json`
- `raw/student/20260528T111500-yu-gamma-entropy-kernel.md`
- `wiki/notes/frontier-yu-entropy-defect-cm.md`

## Proof

Let \(X_\alpha\) have the gamma law \(\Gamma(\alpha,1)\), and let \(G_\alpha=(X_\alpha-\alpha)/\sqrt{\alpha}\). Entropy is translation invariant and scales by the logarithm of the absolute scale, so
\[
H_g(\alpha)
=h(X_\alpha)-\frac12\log\alpha.
\]
The entropy of \(\Gamma(\alpha,1)\) is
\[
h(X_\alpha)=\alpha+\log\Gamma(\alpha)+(1-\alpha)\psi(\alpha),
\]
hence
\[
H_g(\alpha)
=\alpha+\log\Gamma(\alpha)+(1-\alpha)\psi(\alpha)-\frac12\log\alpha.
\]
Define the Gaussian entropy defect
\[
D_\Gamma(\alpha)=\frac12\log(2\pi e)-H_g(\alpha).
\]

Use Binet's formula in the form
\[
\log\Gamma(\alpha)
=\left(\alpha-\frac12\right)\log\alpha-\alpha+\frac12\log(2\pi)
+\int_0^\infty e^{-\alpha t}\frac{A(t)}{t}\,dt,
\]
and
\[
\psi(\alpha)
=\log\alpha-\frac{1}{2\alpha}
-\int_0^\infty e^{-\alpha t}A(t)\,dt,
\]
where
\[
A(t)=\frac{1}{e^t-1}-\frac1t+\frac12.
\]
Substitution and cancellation of all logarithmic terms gives
\[
D_\Gamma(\alpha)
=\frac{1}{2\alpha}
-\int_0^\infty e^{-\alpha t}\frac{A(t)}{t}\,dt
-(\alpha-1)\int_0^\infty e^{-\alpha t}A(t)\,dt.
\]
Since \(A(t)\sim t/12\) as \(t\downarrow0\), integration by parts is legitimate and has no boundary term:
\[
-\alpha\int_0^\infty e^{-\alpha t}A(t)\,dt
=\int_0^\infty A(t)\frac{d}{dt}e^{-\alpha t}\,dt
=-\int_0^\infty e^{-\alpha t}A'(t)\,dt.
\]
Also \(\frac{1}{2\alpha}=\int_0^\infty e^{-\alpha t}\frac12\,dt\). Therefore
\[
D_\Gamma(\alpha)=\int_0^\infty e^{-\alpha t}K(t)\,dt,
\]
with
\[
K(t)=\frac12+A(t)-\frac{A(t)}{t}-A'(t).
\]
Direct simplification gives
\[
K(t)
=\frac{2te^{2t}-3e^{2t}+4e^t-1}
{2t(e^t-1)^2}.
\]

The denominator is positive for \(t>0\). Let
\[
N(t)=2te^{2t}-3e^{2t}+4e^t-1.
\]
Then \(N(0)=0\) and
\[
N'(t)=4e^t\left(e^t(t-1)+1\right).
\]
Set
\[
M(t)=e^t(t-1)+1.
\]
Then \(M(0)=0\) and
\[
M'(t)=te^t>0
\]
for \(t>0\). Hence \(M(t)>0\), so \(N'(t)>0\), so \(N(t)>0\) for every \(t>0\). Thus \(K(t)>0\) for every \(t>0\).

The endpoint behavior is harmless: \(K(t)\to 1/3\) as \(t\downarrow0\), and \(K(t)\to1\) as \(t\to\infty\), so the Laplace integral converges for every \(\alpha>0\).

_Proof source: `raw/student/20260528T111500-yu-gamma-entropy-kernel.md`._

## Tags

`attack-plan`, `diagnostic`, `entropy`, `gamma`, `laplace-kernel`, `mixed`, `proved`, `theorem`
