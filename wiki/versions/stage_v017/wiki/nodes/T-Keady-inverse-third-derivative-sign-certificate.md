---
id: "T-Keady-inverse-third-derivative-sign-certificate"
type: "theorem"
title: "Keady self-bijection inverse third derivative sign certificate at f(1/8)"
status: "proved"
tags: ["complete-monotonicity", "derivative-obstruction", "inverse-branch", "keady", "proved", "theorem"]
parents: ["T-Pointwise-obstruction-certificate-principle"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private Oracle response", "private scout artifact", "private proof note", "wiki/notes/frontier-keady-self-bijection-inverse-cm.md"]
---

# Theorem: Keady self-bijection inverse third derivative sign certificate at f(1/8)

## Statement

For \(f(x)=x^{-1}+100e^{-x}\) and \(g=f^{-1}\), the inverse-derivative certificate gives \(g'''(f(1/8))>0\).

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private Oracle response`
- `private scout artifact`
- `private proof note`
- `wiki/notes/frontier-keady-self-bijection-inverse-cm.md`

## Proof

There exists a completely monotone decreasing bijection
\[
f:(0,\infty)\to(0,\infty)
\]
whose inverse is not completely monotone. One explicit example is
\[
f(x)=\frac1x+100e^{-x}.
\]

For every \(n\ge0\),
\[
(-1)^n f^{(n)}(x)=\frac{n!}{x^{n+1}}+100e^{-x}>0.
\]
Thus \(f\) is strictly completely monotone. Also
\[
f'(x)=-x^{-2}-100e^{-x}<0,
\]
so \(f\) is strictly decreasing. Finally,
\[
\lim_{x\downarrow0}f(x)=\infty,
\qquad
\lim_{x\to\infty}f(x)=0.
\]
Therefore \(f\) is a decreasing bijection from \((0,\infty)\) onto \((0,\infty)\).

Let \(g=f^{-1}\) and write \(y=f(x)\). Inverse differentiation gives
\[
g'''(f(x))=\frac{3(f''(x))^2-f'''(x)f'(x)}{(f'(x))^5}.
\]
For \(f_a(x)=x^{-1}+ae^{-x}\), define
\[
N_a(x)=3(f_a''(x))^2-f_a'''(x)f_a'(x).
\]
A direct calculation gives
\[
N_a(x)=\frac6{x^6}+ae^{-x}\left(-\frac6{x^4}+\frac{12}{x^3}-\frac1{x^2}\right)+2a^2e^{-2x}.
\]
At \(a=100\) and \(x_0=1/8\),
\[
N_{100}(1/8)=1{,}572{,}864-1{,}849{,}600e^{-1/8}+20{,}000e^{-1/4}.
\]
Using \(e^{-1/8}>7/8\) and \(e^{-1/4}<1\),
\[
N_{100}(1/8)<1{,}572{,}864-1{,}849{,}600\cdot\frac78+20{,}000=-25{,}536<0.
\]
Since \(f'(1/8)<0\), the denominator \((f'(1/8))^5\) is negative. Hence
\[
g'''(f(1/8))=\frac{N_{100}(1/8)}{(f'(1/8))^5}>0.
\]
A completely monotone function must satisfy \((-1)^3g'''\ge0\), i.e. \(g'''\le0\). Therefore \(g=f^{-1}\) is not completely monotone.

_Proof source: `private proof note`._

## Tags

`complete-monotonicity`, `derivative-obstruction`, `inverse-branch`, `keady`, `proved`, `theorem`
