---
id: "L-Affine-Laplace-Density-Threshold"
type: "lemma"
title: "Affine Laplace density threshold"
status: "proved"
tags: ["affine-multiplier", "complete-monotonicity", "consolidated-primitive", "consolidation-primitive", "laplace-density", "lemma", "primitive", "primitive-bait", "proved"]
parents: []
refs: ["oracle/responses/OS-20260609T1520Z-buric-elezovic-attachment-oracle-response.md", "raw/student/20260609T1518-buric-elezovic-affine-density-threshold.md", "wiki/notes/buric-elezovic-best-b-threshold.md"]
---

# Lemma: Affine Laplace density threshold

## Statement

Let \(A\in C^1((0,\infty))\) be positive, with enough endpoint decay and local integrability that \(h(x)=\int_0^\infty e^{-xt}A(t)\,dt\), integration by parts, and signed-measure Laplace uniqueness are valid on \((0,\infty)\). Then \((x+b)h(x)\) is completely monotone if and only if \(A'(t)+bA(t)\ge0\) for all \(t>0\). Equivalently, \(b\ge\sup_{t>0}-A'(t)/A(t)\).

## Proof and provenance references

- `oracle/responses/OS-20260609T1520Z-buric-elezovic-attachment-oracle-response.md`
- `raw/student/20260609T1518-buric-elezovic-affine-density-threshold.md`
- `wiki/notes/buric-elezovic-best-b-threshold.md`

## Proof

The standard integral representation for \(\psi\), combined with Frullani's formula for \(\log x\), gives
\[
\psi\left(x+\frac12\right)-\log x
=\int_0^\infty e^{-xt}
\left(\frac1t-\frac{1}{2\sinh(t/2)}\right)\,dt
=\int_0^\infty e^{-xt}A(t)\,dt.
\]
The density is positive because \(2\sinh(t/2)>t\) for \(t>0\). Moreover
\[
A(t)=\frac{t}{24}+O(t^3)\quad(t\downarrow0),
\qquad
A(t)=\frac1t+O(e^{-t/2})\quad(t\to\infty).
\]
Thus the integration-by-parts boundary term \(e^{-xt}A(t)\) vanishes at both endpoints for each \(x>0\), and
\[
x\int_0^\infty e^{-xt}A(t)\,dt
=\int_0^\infty e^{-xt}A'(t)\,dt.
\]
Therefore
\[
f_b(x)=\int_0^\infty e^{-xt}\bigl(A'(t)+bA(t)\bigr)\,dt.
\]

If \(b\ge b_*\), then \(A'(t)+bA(t)\ge0\) for all \(t>0\). Hence, for every integer \(n\ge0\),
\[
(-1)^n f_b^{(n)}(x)
=\int_0^\infty t^n e^{-xt}\bigl(A'(t)+bA(t)\bigr)\,dt\ge0,
\]
so \(f_b\) is completely monotone.

Conversely, if \(b<b_*\), then by continuity there is a nonempty open interval \(I\subset(0,\infty)\) such that
\[
A'(t)+bA(t)<0\qquad(t\in I).
\]
The signed density \((A'(t)+bA(t))\,dt\) is locally finite and has a finite Laplace transform for every \(x>0\). If \(f_b\) were completely monotone, Bernstein's theorem would represent it as the Laplace transform of a positive Radon measure. Laplace-transform uniqueness for locally finite signed measures would force that positive measure to equal the signed density measure above, impossible because the signed density is negative on \(I\). Therefore \(f_b\) is not completely monotone.

Finally,
\[
\frac{-A'(t)}{A(t)}\sim-\frac1t\quad(t\downarrow0),
\qquad
\frac{-A'(t)}{A(t)}\sim\frac1t\quad(t\to\infty),
\]
so the supremum defining \(b_*\) is finite.

_Proof source: `raw/student/20260609T1518-buric-elezovic-affine-density-threshold.md`._

## Do not claim

- Do not use this lemma when integration by parts or signed-measure uniqueness has not been verified.
- Do not treat numerical optimization of the threshold as proved by this lemma.

## Tags

`affine-multiplier`, `complete-monotonicity`, `consolidated-primitive`, `consolidation-primitive`, `laplace-density`, `lemma`, `primitive`, `primitive-bait`, `proved`
