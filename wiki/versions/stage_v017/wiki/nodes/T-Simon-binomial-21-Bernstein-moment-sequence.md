---
id: "T-Simon-binomial-21-Bernstein-moment-sequence"
type: "theorem"
title: "Simon binomial p=2 r=1 slice is a Bernstein moment sequence"
status: "proved"
tags: ["bernstein-sequence", "binomial-moment", "bridge-only", "complete-bernstein", "proved", "simon", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private scout artifact", "private proof note", "wiki/notes/frontier-simon-binomial-raney-bernstein.md"]
---

# Theorem: Simon binomial p=2 r=1 slice is a Bernstein moment sequence

## Statement

The binomial sequence \(\mu_n=\binom{2n+1}{n}\) is a Bernstein moment sequence, since \(\mu_n=\prod_{k=1}^n \Phi(k)\) with the complete Bernstein function \(\Phi(x)=4-2/(x+1)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private scout artifact`
- `private proof note`
- `wiki/notes/frontier-simon-binomial-raney-bernstein.md`

## Proof

Since
\[
\mu_n=\frac{(2n+1)!}{n!(n+1)!},
\]
we get, for \(n\ge1\),
\[
\frac{\mu_n}{\mu_{n-1}}
=\frac{(2n)(2n+1)}{n(n+1)}
=4-\frac{2}{n+1}.
\]
Thus \(\mu_n=\prod_{k=1}^n \Phi(k)\) with
\[
\Phi(x)=4-\frac2{x+1}=2+2\frac{x}{x+1}.
\]
The function \(x/(x+1)\) has the Lévy representation
\[
\frac{x}{x+1}=\int_0^\infty (1-e^{-xt})e^{-t}\,dt,
\]
whose density \(e^{-t}\) is completely monotone. Hence \(x/(x+1)\) is a complete Bernstein function, and so is \(2+2x/(x+1)\). Therefore \((\mu_n)\) is a Bernstein moment sequence.

_Proof source: `private proof note`._

## Tags

`bernstein-sequence`, `binomial-moment`, `bridge-only`, `complete-bernstein`, `proved`, `simon`, `theorem`
