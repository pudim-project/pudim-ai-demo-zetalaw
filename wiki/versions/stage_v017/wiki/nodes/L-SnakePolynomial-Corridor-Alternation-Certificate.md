---
id: "L-SnakePolynomial-Corridor-Alternation-Certificate"
type: "lemma"
title: "Snake-polynomial corridor alternation certificate"
status: "proved"
tags: ["alternation", "finite-certificate", "lemma", "proved", "snake-polynomials", "source-definition", "true"]
parents: ["D-SnakePolynomial-Chebyshev-Language", "T-Exact-finite-certificate-verification-principle"]
refs: ["private librarian audit", "private Oracle response", "private proof note"]
---

# Lemma: Snake-polynomial corridor alternation certificate

## Statement

In the source convention for degree \(n\) snake polynomials, a polynomial \(p\in\mathcal P_n\) with \(|p(x)|\le\mu(x)\) on \([-1,1]\) and \(n+1\) alternating contact points \(p(\tau_i)=\pm\mu(\tau_i)\) is the associated snake polynomial, up to orientation.

## Dependencies

- [[wiki/nodes/D-SnakePolynomial-Chebyshev-Language|Snake polynomials and Chebyshev-expansion language]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`

## Proof

Let \(\mu(x)=48/223+(175/223)|x|\) on \([-1,1]\), and define
\[
\omega(x)=\frac{6875}{1338}x^4-\frac{5825}{1338}x^2+\frac{48}{223}.
\]
For \(t=|x|\), exact factorization gives
\[
\mu(t)-\omega(t)=\frac{25t(1-t)(275t^2+275t+42)}{1338}\ge0
\]
and
\[
\mu(t)+\omega(t)=\frac{(5t-3)^2(275t^2+330t+64)}{1338}\ge0.
\]
Thus \(|\omega(x)|\le\mu(x)\). The five points \(-1,-3/5,0,3/5,1\) are alternating contact points, since \(\omega(\pm1)=\mu(\pm1)\), \(\omega(\pm3/5)=-\mu(\pm3/5)\), and \(\omega(0)=\mu(0)\). This verifies the degree-four corridor/alternation certificate. Finally, using \(x^2=(T_2+T_0)/2\) and \(x^4=(T_4+4T_2+3T_0)/8\),
\[
\omega=-\frac{371}{10704}T_0+\frac{175}{446}T_2+\frac{6875}{10704}T_4,
\]
so the Chebyshev expansion has a negative coefficient.

_Proof source: `private proof note`._

## Do not claim

- Do not use this criterion without verifying the corridor inequality and all alternation contacts.
- Do not treat arbitrary polynomials with Chebyshev coefficients as snake polynomials unless the associated majorant certificate is present.

## Tags

`alternation`, `finite-certificate`, `lemma`, `proved`, `snake-polynomials`, `source-definition`, `true`
