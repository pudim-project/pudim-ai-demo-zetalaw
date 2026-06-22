---
id: "T-Baskakov-r4-alpha1-Laplace-density-seed"
type: "theorem"
title: "Baskakov higher power seed r=4 alpha=1 has positive Laplace density and is completely monotone"
status: "proved"
tags: ["baskakov", "complete-monotonicity", "laplace-density", "proved", "seed-only", "theorem", "theory-growth"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["librarian/audits/LA-20260531T005500-baskakov-r4-alpha1-seed.json", "oracle/responses/ORACLE-OS-20260531T-baskakov-r4-alpha1-seed-oracle-response.md", "raw/student/20260531T005500-baskakov-r4-alpha1-seed.md", "wiki/notes/frontier-baskakov-r4-alpha1-seed.md"]
---

# Theorem: Baskakov higher power seed r=4 alpha=1 has positive Laplace density and is completely monotone

## Statement

For Abel--Gawronski--Neuschel's higher-power Baskakov function, \(f^{[4]}_1(x)=1/((1+x)^4-x^4)=\int_0^\infty e^{-xt}e^{-t/2}(1-\cos(t/2))\,dt\); hence \(f^{[4]}_1\) is completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `librarian/audits/LA-20260531T005500-baskakov-r4-alpha1-seed.json`
- `oracle/responses/ORACLE-OS-20260531T-baskakov-r4-alpha1-seed-oracle-response.md`
- `raw/student/20260531T005500-baskakov-r4-alpha1-seed.md`
- `wiki/notes/frontier-baskakov-r4-alpha1-seed.md`

## Proof

For \(\alpha=1\),
\[
\binom{-1}{k}=(-1)^k,
\qquad
\binom{-1}{k}^{4}=1.
\]
Therefore, for \(x>0\),
\[
f^{[4]}_1(x)
=(1+x)^{-4}\sum_{k=0}^{\infty}
\left(\frac{x}{1+x}\right)^{4k}
=\frac{1}{(1+x)^4-x^4}.
\]
Since
\[
(1+x)^4-x^4=(2x+1)(2x^2+2x+1),
\]
partial fractions give
\[
\frac{1}{(1+x)^4-x^4}
=\frac{2}{2x+1}-\frac{2x+1}{2x^2+2x+1}.
\]
Writing \(a=x+\frac12\), this is
\[
\frac{1}{a}-\frac{a}{a^2+(1/2)^2}.
\]
Using
\[
\int_0^\infty e^{-xt}e^{-t/2}\,dt=\frac{1}{x+1/2}
\]
and
\[
\int_0^\infty e^{-xt}e^{-t/2}\cos(t/2)\,dt
=\frac{x+1/2}{(x+1/2)^2+(1/2)^2},
\]
we obtain
\[
f^{[4]}_1(x)
=\int_0^\infty e^{-xt}e^{-t/2}\left(1-\cos\frac{t}{2}\right)\,dt.
\]
The density \(e^{-t/2}(1-\cos(t/2))\) is nonnegative on \([0,\infty)\). By Bernstein's theorem, \(f^{[4]}_1\) is completely monotone on \((0,\infty)\).

From the source definition
\[
p^{[c]}_{n,k}(x)=\binom{-n/c}{k}(-cx)^k(1+cx)^{-n/c-k},
\]
one has
\[
\psi^{[r]}_{n,c}(x)=\sum_{k=0}^{\infty}\left(p^{[c]}_{n,k}(x)\right)^r
=f^{[r]}_{n/c}(cx)
\]
for even \(r\). Hence, for \(c=n\),
\[
\psi^{[4]}_{n,n}(x)=f^{[4]}_1(nx).
\]
Positive scaling preserves complete monotonicity, so \(\psi^{[4]}_{n,n}\) is completely monotone for every positive integer \(n\).

_Proof source: `raw/student/20260531T005500-baskakov-r4-alpha1-seed.md`._

## Tags

`baskakov`, `complete-monotonicity`, `laplace-density`, `proved`, `seed-only`, `theorem`, `theory-growth`
