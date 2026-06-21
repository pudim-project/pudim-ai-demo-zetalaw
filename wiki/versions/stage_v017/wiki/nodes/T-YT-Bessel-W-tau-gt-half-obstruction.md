---
id: "T-YT-Bessel-W-tau-gt-half-obstruction"
type: "theorem"
title: "tau greater than one half endpoint obstruction for Bessel W_nu power Bernstein property"
status: "proved"
tags: ["attack-plan", "bernstein", "bessel", "endpoint", "obstruction", "proved", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Endpoint-obstruction-certificate-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private attack plan", "private librarian audit", "private proof note", "wiki/notes/frontier-yt-bessel-w-bernstein.md"]
---

# Theorem: tau greater than one half endpoint obstruction for Bessel W_nu power Bernstein property

## Statement

For \(\nu>-1\) and \(\tau>1/2\), the function \(x\mapsto W_\nu(x^\tau)\) is not a nonconstant Bernstein function on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-yt-bessel-w-bernstein.md`

## Proof

This is a bounded pass. It proves the endpoint expansion and the obstruction for \(\tau>1/2\). It does not attempt the full Yang--Tian conjecture for \(\tau\in(0,1/2]\).

Let
\[
W_\nu(z)=\frac{zI_\nu(z)}{I_{\nu+1}(z)}.
\]

For \(\nu>-1\), the modified Bessel series gives
\[
I_\nu(z)
=\frac{(z/2)^\nu}{\Gamma(\nu+1)}
\left(1+\frac{z^2}{4(\nu+1)}+O(z^4)\right)
\]
and
\[
I_{\nu+1}(z)
=\frac{(z/2)^{\nu+1}}{\Gamma(\nu+2)}
\left(1+\frac{z^2}{4(\nu+2)}+O(z^4)\right).
\]
Therefore
\[
\frac{zI_\nu(z)}{I_{\nu+1}(z)}
=2(\nu+1)
\frac{1+z^2/(4(\nu+1))+O(z^4)}
{1+z^2/(4(\nu+2))+O(z^4)}.
\]
Using \((1+A z^2+O(z^4))/(1+B z^2+O(z^4))=1+(A-B)z^2+O(z^4)\),
\[
W_\nu(z)
=2(\nu+1)\left(1+
\left(\frac{1}{4(\nu+1)}-\frac{1}{4(\nu+2)}\right)z^2
+O(z^4)\right).
\]
Hence
\[
W_\nu(z)=2(\nu+1)+\frac{z^2}{2(\nu+2)}+O(z^4).
\]

Let
\[
F_{\nu,\tau}(x)=W_\nu(x^\tau).
\]
Substituting \(z=x^\tau\) in the expansion gives
\[
F_{\nu,\tau}(x)
=2(\nu+1)+\frac{x^{2\tau}}{2(\nu+2)}+O(x^{4\tau}).
\]
Thus
\[
F_{\nu,\tau}'(x)
=\frac{\tau}{\nu+2}x^{2\tau-1}+O(x^{4\tau-1})
\qquad (x\to0^+).
\]
Since \(\nu>-1\), \(\nu+2>0\). If \(\tau>1/2\), then
\[
\lim_{x\to0^+}F_{\nu,\tau}'(x)=0,
\]
and the expansion also shows that \(F_{\nu,\tau}'(x)>0\) for all sufficiently small positive \(x\).

Assume for contradiction that \(F_{\nu,\tau}\) is a Bernstein function. Then \(F_{\nu,\tau}'\) is completely monotonic, so \(F_{\nu,\tau}'\ge0\) and \(F_{\nu,\tau}''\le0\); equivalently, \(F_{\nu,\tau}'\) is nonnegative and nonincreasing.

For any fixed \(y>0\) and \(0<x<y\),
\[
0\le F_{\nu,\tau}'(y)\le F_{\nu,\tau}'(x).
\]
Letting \(x\to0^+\) gives \(F_{\nu,\tau}'(y)=0\). Since \(y\) was arbitrary, \(F_{\nu,\tau}'\equiv0\), contradicting the local expansion, which has \(F_{\nu,\tau}'(x)>0\) near \(0\).

Therefore, for \(\nu>-1\) and \(\tau>1/2\), \(x\mapsto W_\nu(x^\tau)\) is not a nonconstant Bernstein function.

The obstruction proves that the source's upper endpoint \(1/2\) is sharp against extension to \(\tau>1/2\). It does not prove the Bernstein property for any \(\tau\in(0,1/2]\).

_Proof source: `private proof note`._

## Tags

`attack-plan`, `bernstein`, `bessel`, `endpoint`, `obstruction`, `proved`, `theorem`
