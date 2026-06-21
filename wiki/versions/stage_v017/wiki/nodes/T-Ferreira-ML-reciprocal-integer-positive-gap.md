---
id: "T-Ferreira-ML-reciprocal-integer-positive-gap"
type: "theorem"
title: "Ferreira Mittag Leffler reciprocal integer positive exponential gap"
status: "proved"
tags: ["bridge-subcase", "ferreira", "laplace-divergence", "mittag-leffler", "proved", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "T-Ferreira-ML-all-alpha-elementary-divergence-frontier-open"]
refs: ["private attack plan", "private Oracle response", "private Oracle response", "private scout artifact", "raw/source-cache/ferreira-complete-monotonicity-discrete-equations/Ferreira.pdf", "raw/source-cache/ferreira-complete-monotonicity-discrete-equations/Ferreira.txt", "private proof note", "wiki/notes/frontier-ferreira-ml-reciprocal-divergence.md"]
---

# Theorem: Ferreira Mittag Leffler reciprocal integer positive exponential gap

## Statement

For every integer \(m\ge2\) and every \(t>0\), \(E_{1/m}(t^{1/m})>e^t\), where \(E_\alpha(z)=\sum_{k\ge0}z^k/\Gamma(\alpha k+1)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/T-Ferreira-ML-all-alpha-elementary-divergence-frontier-open|Ferreira Mittag Leffler all alpha elementary divergence frontier]]

## Proof and provenance references

- `private attack plan`
- `private Oracle response`
- `private Oracle response`
- `private scout artifact`
- `raw/source-cache/ferreira-complete-monotonicity-discrete-equations/Ferreira.pdf`
- `raw/source-cache/ferreira-complete-monotonicity-discrete-equations/Ferreira.txt`
- `private proof note`
- `wiki/notes/frontier-ferreira-ml-reciprocal-divergence.md`

## Proof

Split the series by residue classes modulo \(m\):
\[
E_{1/m}(t^{1/m})
=\sum_{k=0}^{\infty}\frac{t^{k/m}}{\Gamma(k/m+1)}
=\sum_{r=0}^{m-1}\sum_{j=0}^{\infty}
\frac{t^{j+r/m}}{\Gamma(j+r/m+1)}.
\]
The \(r=0\) class is
\[
\sum_{j=0}^{\infty}\frac{t^j}{\Gamma(j+1)}=
\sum_{j=0}^{\infty}\frac{t^j}{j!}=e^t.
\]
For \(1\le r\le m-1\), every term is strictly positive when \(t>0\), because \(\Gamma(x)>0\) for \(x>0\). Hence
\[
E_{1/m}(t^{1/m})=e^t+
\sum_{r=1}^{m-1}\sum_{j=0}^{\infty}
\frac{t^{j+r/m}}{\Gamma(j+r/m+1)}>e^t.
\]

Now let \(a=-\lambda\ge1\). Since the coefficients of \(E_{1/m}\) are positive on positive arguments,
\[
E_{1/m}(a t^{1/m})
\ge \sum_{j=0}^{\infty}\frac{a^{mj}t^j}{\Gamma(j+1)}
=e^{a^m t}.
\]
If \(a>1\), then
\[
e^{-t}E_{1/m}(a t^{1/m})\ge e^{(a^m-1)t},
\]
whose integral over \([0,\infty)\) diverges. If \(a=1\), the strict inequality already proved gives
\[
e^{-t}E_{1/m}(t^{1/m})>1
\]
for every \(t>0\), so the integral again diverges.

The proof uses the exact exponential subsequence \(k=mj\), where \(\Gamma(k/m+1)=\Gamma(j+1)=j!\). For a general rational \(\alpha=p/q\) with \(p>1\), the analogous \(q\)-step subsequence gives denominators \(\Gamma(1+pj)\), not \(j!\). Thus this proof is a sparse-lattice bridge, not a dense-rational or all-\(\alpha\) argument.

_Proof source: `private proof note`._

## Tags

`bridge-subcase`, `ferreira`, `laplace-divergence`, `mittag-leffler`, `proved`, `theorem`
