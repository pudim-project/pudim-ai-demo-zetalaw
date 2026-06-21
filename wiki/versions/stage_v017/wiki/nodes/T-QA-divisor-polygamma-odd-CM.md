---
id: "T-QA-divisor-polygamma-odd-CM"
type: "theorem"
title: "Qi-Agarwal divisor-polygamma sums are completely monotone for odd n"
status: "proved"
tags: ["complete-monotonicity", "divisor-sums", "polygamma", "proved", "qi-agarwal", "theorem", "yin"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private scout artifact", "private proof note", "wiki/notes/frontier-qa-divisor-polygamma-parity.md"]
---

# Theorem: Qi-Agarwal divisor-polygamma sums are completely monotone for odd n

## Statement

For every odd positive integer \(n\), the divisor-polygamma sum \(f_n(x)=\sum_{km=n}[\psi^{(k)}(x)]^m\) is completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private scout artifact`
- `private proof note`
- `wiki/notes/frontier-qa-divisor-polygamma-parity.md`

## Proof

For every \(k\ge1\), the standard polygamma sign theorem gives
\[
(-1)^{k+1}\psi^{(k)}(x)
=
\int_0^\infty \frac{t^k e^{-xt}}{1-e^{-t}}\,dt,
\]
so \((-1)^{k+1}\psi^{(k)}\) is completely monotone on \((0,\infty)\).

If \(n\) is odd and \(km=n\), then \(k\) and \(m\) are both odd. Hence \(\psi^{(k)}\) itself is a positive completely monotone function, and
\[
\bigl[\psi^{(k)}(x)\bigr]^m
\]
is completely monotone by finite product closure of positive completely monotone functions. Summing over the finitely many divisor pairs \(km=n\) preserves complete monotonicity. Therefore \(f_n\) is completely monotone for every odd \(n\).

For \(n=2\), the divisor pairs are \((k,m)=(1,2)\) and \((2,1)\), so
\[
f_2(x)=\bigl[\psi'(x)\bigr]^2+\psi''(x).
\]
The same Qi--Agarwal source records the known sharp theorem that
\[
\bigl[\psi'(x)\bigr]^2+\lambda\psi''(x)
\]
is completely monotonic on \((0,\infty)\) if and only if \(\lambda\le1\). Taking \(\lambda=1\) gives \(f_2\in CM(0,\infty)\).

Thus the source's proposed even-parity clause, "\(f_{2\ell}\) is not completely monotonic for all \(\ell\in\mathbb N\)", is false already at \(\ell=1\). The source problem is solved negatively/correctively:

the odd half is true;
the stated even half is false;
the corrected even frontier begins at \(n=4\), not \(n=2\).

_Proof source: `private proof note`._

## Tags

`complete-monotonicity`, `divisor-sums`, `polygamma`, `proved`, `qi-agarwal`, `theorem`, `yin`
