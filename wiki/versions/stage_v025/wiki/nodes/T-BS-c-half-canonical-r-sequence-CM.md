---
id: "T-BS-c-half-canonical-r-sequence-CM"
type: "theorem"
title: "Bondesson Steutel c=1/2 canonical r sequence completely monotone"
status: "proved"
tags: ["attack-plan", "branching-process", "complete-monotonicity", "hausdorff-moment", "proved", "theorem"]
parents: ["T-BS-c-half-Catalan-Hausdorff-representation", "T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["attack-plans/AP-20260528T151000-bondesson-steutel-shifted-cm.json", "librarian/audits/LA-20260528T151500-bondesson-steutel-student.json", "raw/student/20260528T151500-bondesson-steutel-shifted-cm.md", "wiki/notes/frontier-bondesson-steutel-shifted-cm.md"]
---

# Theorem: Bondesson Steutel c=1/2 canonical r sequence completely monotone

## Statement

For the Bondesson--Steutel distribution at \(c=1/2\), the canonical sequence \(r_n=(n+1/2)P_n(1/2)\) is completely monotone, with \(r_n=\frac{1}{2\pi}\int_0^1 x^{n+1/2}(1-x)^{-1/2}\,dx\).

## Dependencies

- [[wiki/nodes/T-BS-c-half-Catalan-Hausdorff-representation|Bondesson Steutel c=1/2 Catalan beta Hausdorff representation]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `attack-plans/AP-20260528T151000-bondesson-steutel-shifted-cm.json`
- `librarian/audits/LA-20260528T151500-bondesson-steutel-student.json`
- `raw/student/20260528T151500-bondesson-steutel-shifted-cm.md`
- `wiki/notes/frontier-bondesson-steutel-shifted-cm.md`

## Proof

For \(c=1/2\), the source pgf is
\[
P(z)=\frac{1-\sqrt{1-z}}{z}.
\]
Using the Catalan generating function
\[
\sum_{n\ge0}C_n x^n=\frac{1-\sqrt{1-4x}}{2x},
\]
with \(x=z/4\), we get
\[
P(z)=\frac12\sum_{n\ge0}C_n\left(\frac z4\right)^n.
\]
Hence
\[
P_n(1/2)=\frac{C_n}{2\cdot4^n}
=\frac{1}{2\cdot4^n(n+1)}\binom{2n}{n}.
\]

Now
\[
\frac1\pi\int_0^1 x^{n-1/2}(1-x)^{1/2}\,dx
=\frac1\pi B(n+1/2,3/2).
\]
Since \(\Gamma(3/2)=\sqrt\pi/2\) and
\[
\Gamma(n+1/2)=\frac{(2n)!\sqrt\pi}{4^n n!},
\]
this beta integral equals
\[
\frac{(2n)!}{2\cdot4^n n!(n+1)!}
=\frac{C_n}{2\cdot4^n}
=P_n(1/2).
\]
Therefore
\[
P_n(1/2)=\frac1\pi\int_0^1 x^{n-1/2}(1-x)^{1/2}\,dx.
\]
This is a Hausdorff moment representation on \([0,1]\), so \((P_n(1/2))\) is completely monotone as a sequence.

For \(c=1/2\), the canonical sequence is
\[
r_n=(n+1/2)P_n(1/2).
\]
Using the Hausdorff representation,
\[
r_n=\frac{n+1/2}{\pi}\int_0^1 x^{n-1/2}(1-x)^{1/2}\,dx.
\]
Because
\[
\frac{d}{dx}x^{n+1/2}=(n+1/2)x^{n-1/2},
\]
integration by parts gives
\[
r_n
=\frac1\pi\int_0^1 (1-x)^{1/2}\,d(x^{n+1/2})
=\frac{1}{2\pi}\int_0^1 x^{n+1/2}(1-x)^{-1/2}\,dx.
\]
The boundary terms vanish at \(0\) and \(1\). Thus
\[
r_n=\int_0^1 x^n\,d\nu(x),
\qquad
d\nu(x)=\frac{1}{2\pi}x^{1/2}(1-x)^{-1/2}\,dx.
\]
This is a positive finite measure on \([0,1]\). Hence \((r_n)\) is completely monotone.

_Proof source: `raw/student/20260528T151500-bondesson-steutel-shifted-cm.md`._

## Tags

`attack-plan`, `branching-process`, `complete-monotonicity`, `hausdorff-moment`, `proved`, `theorem`
