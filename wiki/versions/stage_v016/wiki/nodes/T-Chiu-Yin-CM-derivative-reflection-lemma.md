---
id: "T-Chiu-Yin-CM-derivative-reflection-lemma"
type: "theorem"
title: "negative derivative of completely monotone function is completely monotone"
status: "proved"
tags: ["chiu-yin", "closure", "complete-monotonicity", "derivative", "proved", "standard-tool", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260531T112500-chiu-yin-classical-converse.json", "oracle/responses/ORACLE-OS-20260531T-chiu-yin-classical-converse-oracle-response.md", "raw/student/20260531T112500-chiu-yin-classical-converse.md", "wiki/notes/frontier-chiu-yin-compound-geometric-converse.md"]
---

# Theorem: negative derivative of completely monotone function is completely monotone

## Statement

If \(g\) is completely monotone on \((0,\infty)\), then \(-g'\) is completely monotone wherever the derivative exists.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260531T112500-chiu-yin-classical-converse.json`
- `oracle/responses/ORACLE-OS-20260531T-chiu-yin-classical-converse-oracle-response.md`
- `raw/student/20260531T112500-chiu-yin-classical-converse.md`
- `wiki/notes/frontier-chiu-yin-compound-geometric-converse.md`

## Proof

Chiu--Yin Remark 3.5 conjectures the converse of Lemma 3.1: in the Sparre Andersen model, complete monotonicity of the ascending ladder-height density should imply complete monotonicity of the claim-size density. This pass proves only the classical Cramer--Lundberg/equilibrium-ladder slice.

\emph{Setup.}
In the classical Cramer--Lundberg/equilibrium formulation, let \(H\) be the claim-size distribution, let
\[
\overline H(x)=1-H(x),
\]
and assume \(H\) is absolutely continuous on \((0,\infty)\). Let
\[
m=\int_0^\infty \overline H(u)\,du
\]
be the finite mean, with \(0<m<\infty\). The equilibrium excess cdf and density are
\[
F_e(x)=\frac1m\int_0^x\overline H(u)\,du,
\qquad
f_e(x)=F_e'(x)=\frac{\overline H(x)}{m}.
\]
In the classical ladder normalization under discussion, the ascending ladder-height density is this equilibrium density:
\[
f_+(x)=f_e(x)=\frac{\overline H(x)}{m}.
\]

If \(g\) is completely monotone on \((0,\infty)\), then for every \(n\ge0\),
\[
(-1)^n g^{(n)}(x)\ge0.
\]
Therefore
\[
(-1)^n(-g')^{(n)}(x)=(-1)^{n+1}g^{(n+1)}(x)\ge0,
\]
so \(-g'\) is completely monotone.

Assume \(f_+\) is completely monotone. Then \(\overline H=m f_+\) is completely monotone. Define the smooth density representative
\[
h_*(x)=-\overline H'(x)=-m f_+'(x).
\]
By the reflection lemma, \(-f_+'\) is completely monotone; multiplying by \(m>0\) preserves complete monotonicity. Hence \(h_*\) is completely monotone.

Since densities are a.e. representatives, the conclusion is that \(H\) admits a completely monotone density version \(h_*\). Thus the converse of Chiu--Yin Lemma 3.1 is true in the classical equilibrium-ladder slice in this density-version sense.

This does not solve the full Sparre Andersen converse in Remark 3.5. The general case includes the weak descending-ladder renewal factor in the representation of \(F^+\), so the original claim density is not recovered by a single derivative of the ladder-height density.

_Proof source: `raw/student/20260531T112500-chiu-yin-classical-converse.md`._

## Tags

`chiu-yin`, `closure`, `complete-monotonicity`, `derivative`, `proved`, `standard-tool`, `theorem`
