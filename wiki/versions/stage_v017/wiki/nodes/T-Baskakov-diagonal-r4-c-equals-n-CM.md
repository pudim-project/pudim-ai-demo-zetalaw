---
id: "T-Baskakov-diagonal-r4-c-equals-n-CM"
type: "theorem"
title: "Baskakov diagonal r=4 c=n generalized sum is completely monotone"
status: "proved"
tags: ["baskakov", "complete-monotonicity", "diagonal-slice", "proved", "seed-only", "theorem", "theory-growth"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "T-Baskakov-r4-alpha1-Laplace-density-seed", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-baskakov-r4-alpha1-seed.md"]
---

# Theorem: Baskakov diagonal r=4 c=n generalized sum is completely monotone

## Statement

For every positive integer \(n\), the diagonal generalized Baskakov sum \(\psi^{[4]}_{n,n}(x)=\sum_{k=0}^{\infty}(p^{[n]}_{n,k}(x))^4\) is completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/T-Baskakov-r4-alpha1-Laplace-density-seed|Baskakov higher power seed r=4 alpha=1 has positive Laplace density and is completely monotone]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`baskakov`, `complete-monotonicity`, `diagonal-slice`, `proved`, `seed-only`, `theorem`, `theory-growth`
