---
id: "L-BF-Integer-Increments-Are-Hausdorff-CM"
type: "lemma"
title: "Bernstein function integer first differences Hausdorff moment sequence"
status: "proved"
tags: ["bernstein-function", "bridge-lemma", "hausdorff-moment", "laplace-transform", "lemma", "primitive-growth", "proved", "true"]
parents: ["T-Bernstein-derivative-complete-monotonicity-criterion", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-grws-sectorii-bernstein-interpolation.md"]
---

# Lemma: Bernstein function integer first differences Hausdorff moment sequence

## Statement

If \(F\) is a Bernstein function and \(a_n=F(n)\), then the first differences \(d_n=a_{n+1}-a_n\) form a Hausdorff moment sequence on \([0,1]\).

## Dependencies

- [[wiki/nodes/T-Bernstein-derivative-complete-monotonicity-criterion|T-Bernstein-derivative-complete-monotonicity-criterion]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-grws-sectorii-bernstein-interpolation.md`

## Proof

A Bernstein function has the representation
\[
F(x)=c+bx+\int_{(0,\infty)}(1-e^{-xt})\,d\mu(t),
\]
where \(b\ge0\), \(\mu\ge0\), and \(\int(1\wedge t)\,d\mu(t)<\infty\). Hence
\[
d_n=F(n+1)-F(n)
=b+\int_{(0,\infty)}e^{-nt}(1-e^{-t})\,d\mu(t).
\]
Pushing forward \((1-e^{-t})\,d\mu(t)\) under \(s=e^{-t}\), and adding the atom \(b\delta_1\), gives a finite positive measure \(\rho\) on \([0,1]\) such that
\[
d_n=\int_{[0,1]}s^n\,d\rho(s).
\]
Finiteness follows from \(1-e^{-t}\asymp 1\wedge t\).

Let a sequence \((d_n)\) have a finite signed representing measure \(\sigma\) on \([0,1]\). If \(\sigma\) has a negative atom at some point \(r\in(0,1]\), then \((d_n)\) has no positive representing measure on \([0,1]\).

The Hausdorff moment problem on the compact interval \([0,1]\) is determinate for finite signed measures. Therefore any finite positive representing measure would have to equal \(\sigma\), contradicting the negative mass at \(r\). If moments are indexed only for \(n\ge1\), the possible ambiguity is an atom at \(0\), which does not affect a negative atom at \(r>0\).

Set \(q=p^{-1}\in(0,1)\). Then
\[
a_n=\frac{p^n+N}{p^n+D}
=\frac{1+Nq^n}{1+Dq^n}.
\]
The first differences are
\[
\begin{aligned}
d_n
&=a_{n+1}-a_n\\
&=\frac{1+Nq^{n+1}}{1+Dq^{n+1}}
  -\frac{1+Nq^n}{1+Dq^n}\\
&=(D-N)(1-q)\frac{q^n}{(1+Dq^n)(1+Dq^{n+1})}.
\end{aligned}
\]
For \(u=q^n\),
\[
\frac{(1-q)u}{(1+Du)(1+Dqu)}
=\frac1D\left(\frac1{1+Dqu}-\frac1{1+Du}\right).
\]
Since \(0<D\le -N<1\), the geometric expansions converge absolutely, and
\[
d_n
=(D-N)\sum_{m\ge1}(1-q^m)(-D)^{m-1}q^{mn}.
\]
Thus \((d_n)\) has the finite signed Hausdorff representation
\[
\sigma
=(D-N)\sum_{m\ge1}(1-q^m)(-D)^{m-1}\delta_{q^m}.
\]
The total variation is finite because
\[
\sum_{m\ge1}(1-q^m)D^{m-1}\le \frac1{1-D}.
\]
The atom at \(q^2\) has mass
\[
\sigma(\{q^2\})=-(D-N)D(1-q^2)<0.
\]
By the signed-atom obstruction, \((d_n)\) is not a Hausdorff moment sequence of a positive measure.

For \(p>1\), \(-1<N<0\), and \(0<D\le -N\), the sequence
\[
a_n=\frac{p^n+N}{p^n+D}
\]
is not interpolated by any Bernstein function.

If such a Bernstein function \(F\) existed, the first bridge lemma would force \(d_n=a_{n+1}-a_n\) to be a Hausdorff moment sequence for a finite positive measure on \([0,1]\). The explicit GRWS expansion gives the unique finite signed representing measure for \((d_n)\), and that measure has negative mass at \(q^2\). This contradicts positivity.

The boundary \(D=-N\) is included: then \(D-N=2D>0\), \(0<D<1\), and the negative atom remains \(-2D^2(1-q^2)\). The boundary \(D=0\) is excluded: there the negative atom disappears and
\[
d_n=(-N)(1-q)q^n
\]
has a positive one-atom representation.

_Proof source: `private proof note`._

## Tags

`bernstein-function`, `bridge-lemma`, `hausdorff-moment`, `laplace-transform`, `lemma`, `primitive-growth`, `proved`, `true`
