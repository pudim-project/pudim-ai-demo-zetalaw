---
id: "T-not-SnakePolynomial-Chebyshev-ConvexMajorant-Conjecture7-1"
type: "theorem"
title: "Snake-polynomial continuous even convex Chebyshev-positivity conjecture is false"
status: "proved"
tags: ["app-candidate", "chebyshev", "convex-majorant", "counterexample", "finite-certificate", "primitive-growth", "proved", "snake-polynomials", "source-open-solved", "theorem", "true"]
parents: ["D-SnakePolynomial-Chebyshev-Language", "L-SnakePolynomial-Corridor-Alternation-Certificate", "T-Exact-finite-certificate-verification-principle"]
refs: ["librarian/audits/LA-20260613T0202-snake-chebyshev-first-contact.json", "librarian/audits/LA-20260613T0220-snake-chebyshev-counterexample.json", "oracle/responses/OS-20260613Tsnake-chebyshev-finite-cone-oracle-response.md", "raw/student/20260613T0215-snake-chebyshev-counterexample.md"]
---

# Theorem: Snake-polynomial continuous even convex Chebyshev-positivity conjecture is false

## Statement

Conjecture 7.1 for snake polynomials is false as written. For the continuous nonnegative even convex majorant \(\mu(x)=48/223+(175/223)|x|\), the associated degree-four snake polynomial is \(\omega(x)=(6875/1338)x^4-(5825/1338)x^2+48/223\). Its Chebyshev expansion is \(\omega=-(371/10704)T_0+(175/446)T_2+(6875/10704)T_4\), which has a negative coefficient.

## Dependencies

- [[wiki/nodes/D-SnakePolynomial-Chebyshev-Language|Snake polynomials and Chebyshev-expansion language]]
- [[wiki/nodes/L-SnakePolynomial-Corridor-Alternation-Certificate|Snake-polynomial corridor alternation certificate]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `librarian/audits/LA-20260613T0202-snake-chebyshev-first-contact.json`
- `librarian/audits/LA-20260613T0220-snake-chebyshev-counterexample.json`
- `oracle/responses/OS-20260613Tsnake-chebyshev-finite-cone-oracle-response.md`
- `raw/student/20260613T0215-snake-chebyshev-counterexample.md`

## Proof

Let
\[
\mu(x)=\frac{48}{223}+\frac{175}{223}|x|,
\qquad -1\le x\le1.
\]
This majorant is nonnegative, continuous, even, and convex on \([-1,1]\).

Define the degree-four polynomial
\[
\omega(x)=
\frac{6875}{1338}x^4-\frac{5825}{1338}x^2+\frac{48}{223}.
\]
For \(t=|x|\in[0,1]\), exact algebra gives
\[
\mu(t)-\omega(t)
=
\frac{25t(1-t)(275t^2+275t+42)}{1338}\ge0
\]
and
\[
\mu(t)+\omega(t)
=
\frac{(5t-3)^2(275t^2+330t+64)}{1338}\ge0.
\]
Hence \(|\omega(x)|\le \mu(x)\) on \([-1,1]\).

The five contact points \(-1,-3/5,0,3/5,1\) have alternating signs:
\[
\omega(\pm1)=1=\mu(\pm1),
\]
\[
\omega\!\left(\pm\frac35\right)=-\frac{153}{223}
=-\mu\!\left(\pm\frac35\right),
\]
and
\[
\omega(0)=\frac{48}{223}=\mu(0).
\]
Thus \(\omega\) satisfies the corridor bound and the five-point alternation certificate required for the degree-four snake polynomial associated with \(\mu\), up to the source's harmless orientation convention.

Using
\[
x^2=\frac{T_2(x)+T_0(x)}2,\qquad
x^4=\frac{T_4(x)+4T_2(x)+3T_0(x)}8,
\]
we obtain
\[
\omega(x)=
-\frac{371}{10704}T_0(x)
+\frac{175}{446}T_2(x)
+\frac{6875}{10704}T_4(x).
\]
The \(T_0\)-coefficient is strictly negative. Reversing the orientation replaces \(\omega\) by \(-\omega\), which makes the \(T_2\) and \(T_4\) coefficients negative.

Therefore Conjecture 7.1 is false as written.

_Proof source: `raw/student/20260613T0215-snake-chebyshev-counterexample.md`._

## Do not claim

- Do not claim the broader Problem 7.1 is solved.
- Do not claim anything about smooth, strictly convex, or otherwise strengthened majorant classes.
- Do not claim the counterexample works if a future source convention explicitly excludes the \(T_0\) coefficient.

## Tags

`app-candidate`, `chebyshev`, `convex-majorant`, `counterexample`, `finite-certificate`, `primitive-growth`, `proved`, `snake-polynomials`, `source-open-solved`, `theorem`, `true`
