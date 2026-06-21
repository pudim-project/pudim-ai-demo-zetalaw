---
id: "T-not-CM-inverse-closure-general"
type: "theorem"
title: "general complete-monotone inverse branch closure is false"
status: "proved"
tags: ["complete-monotonicity", "inverse-branch", "proved", "route-kill", "theorem"]
parents: ["T-Keady-CM-inverse-not-CM-example", "T-Keady-self-bijection-inverse-CM-negative-example", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private proof note", "wiki/notes/frontier-keady-inverse-cm.md"]
---

# Theorem: general complete-monotone inverse branch closure is false

## Statement

It is not true that every strictly completely monotone decreasing function has a completely monotone inverse branch on its natural range.

## Dependencies

- [[wiki/nodes/T-Keady-CM-inverse-not-CM-example|finite exponential mixture has inverse branch not completely monotone]]
- [[wiki/nodes/T-Keady-self-bijection-inverse-CM-negative-example|Keady self-bijection completely monotone inverse not completely monotone example]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-keady-inverse-cm.md`

## Proof

For every \(n\ge0\),
\[
(-1)^n f^{(n)}(x)=99e^{-x}+10^n e^{-10x}>0.
\]
Hence \(f\) is strictly completely monotone, and \(f'<0\), so the inverse branch \(g=f^{-1}\) exists.

For \(y=f(x)\), inverse differentiation gives
\[
g'(y)=\frac1{f'(x)},\qquad
g''(y)=-\frac{f''(x)}{(f'(x))^3},
\]
and
\[
g'''(y)=\frac{3(f''(x))^2-f'''(x)f'(x)}{(f'(x))^5}.
\]
At \(x=0+\),
\[
f'(0+)=-109,\qquad f''(0+)=199,\qquad f'''(0+)=-1099.
\]
Therefore
\[
3(f''(0+))^2-f'''(0+)f'(0+)
=3\cdot199^2-(-1099)(-109)
=-988<0.
\]
Since \((f'(0+))^5<0\), this gives
\[
g'''(100-)>0.
\]
By continuity, \(g'''>0\) on a left-neighborhood of \(100\). Complete monotonicity of \(g\) would require \((-1)^3g'''\ge0\), i.e. \(g'''\le0\). This contradiction proves that \(g\) is not completely monotone.

_Proof source: `private proof note`._

## Tags

`complete-monotonicity`, `inverse-branch`, `proved`, `route-kill`, `theorem`
