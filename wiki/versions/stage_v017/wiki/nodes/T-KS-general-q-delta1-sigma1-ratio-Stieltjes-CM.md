---
id: "T-KS-general-q-delta1-sigma1-ratio-Stieltjes-CM"
type: "theorem"
title: "Karp Sitnik sigma one delta one shifted generalized hypergeometric ratio is Stieltjes and completely monotone"
status: "proved"
tags: ["bridge-patch", "complete-monotonicity", "hypergeometric", "karp-sitnik", "proved", "stieltjes", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "T-CBF-difference-quotient-Stieltjes", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-karp-sitnik-shifted-ratio.md"]
---

# Theorem: Karp Sitnik sigma one delta one shifted generalized hypergeometric ratio is Stieltjes and completely monotone

## Statement

For \(q\ge1\) and \(b_i>a_i>0\), the shifted ratio \({}_{q+1}F_q(1,a_1+1,\ldots,a_q+1;b_1+1,\ldots,b_q+1;-x)/{}_{q+1}F_q(1,a_1,\ldots,a_q;b_1,\ldots,b_q;-x)\) is a Stieltjes function, hence completely monotone, on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/T-CBF-difference-quotient-Stieltjes|complete Bernstein finite origin difference quotient is Stieltjes]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-karp-sitnik-shifted-ratio.md`

## Proof

Karp--Sitnik's positive-density representation gives a compact-support Stieltjes form for \(F\):
\[
F(x)=\int_0^1 \frac{d\mu(s)}{1+sx},
\qquad \mu\ge0,
\qquad \mu([0,1])=F(0)=1.
\]
Thus \(F\) is a nonzero Stieltjes function.

By the standard Stieltjes/complete-Bernstein duality, if \(F\) is nonzero Stieltjes, then
\[
G(x)=\frac1{F(x)}
\]
is a complete Bernstein function. Since \(G(0)=1\), the complete Bernstein representation gives
\[
G(x)=1+\alpha x+\int_0^\infty \frac{x}{x+t}\,d\nu(t),
\qquad \alpha\ge0,\quad \nu\ge0.
\]
Therefore
\[
\frac{G(x)-1}{x}
=\alpha+\int_0^\infty \frac{1}{x+t}\,d\nu(t)
\]
is Stieltjes.

Karp--Sitnik's contiguous defect identity for \(\sigma=1,\delta=1\) is
\[
1-F(x)
=x\,{}_{q+1}F_q(1,a_1+1,\ldots,a_q+1;b_1+1,\ldots,b_q+1;-x)
\prod_{i=1}^q\frac{a_i}{b_i}.
\]
Hence
\[
R(x)=
\prod_{i=1}^q\frac{b_i}{a_i}\,
\frac{1-F(x)}{xF(x)}
=
\prod_{i=1}^q\frac{b_i}{a_i}\,
\frac{G(x)-1}{x}.
\]
A positive scalar multiple of a Stieltjes function is Stieltjes. Thus \(R\) is Stieltjes and completely monotone.

Finally,
\[
xR(x)=\prod_{i=1}^q\frac{b_i}{a_i}\,(G(x)-1).
\]
Since subtracting the finite value \(G(0)=1\) from a complete Bernstein function leaves the same nonnegative drift and Levy measure part, \(G(x)-1\) is complete Bernstein. Hence \(xR(x)\) is complete Bernstein up to the stated positive scalar.

the KS Lemma1 Stieltjes normal form
the Stieltjes reciprocal CBF
the CBF difference quotient Stieltjes
the KS general q delta1 sigma1 ratio Stieltjes CM
the KS Gauss beta delta1 sigma1 ratio Stieltjes CM
the KS shift ratio times x CBF

the KS Gauss beta general sigma ratio CM open
the KS Gauss beta arbitrary delta ratio CM open
the KS parameter relaxation source vocabulary

This is a strong local theorem and a reusable Stieltjes/CBF bridge. The subsequent primary-source wording audit did not find an explicit Karp--Sitnik open problem asking for the CM/Stieltjes/CBF upgrade, so this result is bridge-only unless a separate source asks for exactly this strengthening.

_Proof source: `private proof note`._

## Tags

`bridge-patch`, `complete-monotonicity`, `hypergeometric`, `karp-sitnik`, `proved`, `stieltjes`, `theorem`
