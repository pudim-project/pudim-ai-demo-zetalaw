---
id: "T-not-ArsinhSquare-log-derivative-Stieltjes"
type: "theorem"
title: "arsinh square logarithmic derivative not Stieltjes wrong boundary sign on negative cut"
status: "proved"
tags: ["app-candidate", "boundary-sign", "negative-answer", "primitive-growth", "proved", "source-open-solved", "stieltjes", "theorem", "thorin-bernstein", "true"]
parents: ["T-ArsinhSquare-log-derivative-completely-monotone", "T-Pointwise-obstruction-certificate-principle"]
refs: ["librarian/audits/LA-20260612T1810-arsinh-square-stieltjes-negative-answer.json", "oracle/responses/OS-20260612T1750Z-arsinh-square-stieltjes-log-derivative-oracle-response.md", "raw/student/20260612T1800-arsinh-square-log-derivative-not-stieltjes.md", "wiki/notes/frontier-arsinh-square-thorin-bernstein.md"]
---

# Theorem: arsinh square logarithmic derivative not Stieltjes wrong boundary sign on negative cut

## Statement

For \(\varphi(x)=\operatorname{arsinh}^2\sqrt{x}\), the logarithmic derivative \(\varphi'(x)/\varphi(x)=1/(\sqrt{x}\sqrt{1+x}\operatorname{arsinh}\sqrt{x})\) is not a Stieltjes function; its upper boundary value on \((-\infty,-1)\) has strictly positive imaginary part.

## Dependencies

- [[wiki/nodes/T-ArsinhSquare-log-derivative-completely-monotone|arsinh square logarithmic derivative completely monotone not Stieltjes bridge]]
- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260612T1810-arsinh-square-stieltjes-negative-answer.json`
- `oracle/responses/OS-20260612T1750Z-arsinh-square-stieltjes-log-derivative-oracle-response.md`
- `raw/student/20260612T1800-arsinh-square-log-derivative-not-stieltjes.md`
- `wiki/notes/frontier-arsinh-square-thorin-bernstein.md`

## Proof

A Stieltjes function
\[
F(z)=\frac{a}{z}+b+\int_0^\infty \frac{1}{z+s}\,d\mu(s),
\qquad a,b\ge0,\quad \mu\ge0,
\]
maps the upper half-plane into the lower half-plane:
\[
\operatorname{Im}F(z)\le0,\qquad \operatorname{Im}z>0.
\]

Let \(z=-t+i0\) with \(t>1\). On principal branches,
\[
\sqrt{z}=i\sqrt t,\qquad \sqrt{1+z}=i\sqrt{t-1}.
\]
Also
\[
\operatorname{arsinh}(i\sqrt t)
=\log\left(i\sqrt t+i\sqrt{t-1}\right)
=A(t)+\frac{\pi i}{2},
\]
where
\[
A(t)=\operatorname{arcosh}\sqrt t=\log(\sqrt t+\sqrt{t-1})>0.
\]
Therefore
\[
h(-t+i0)
=-\frac{1}{\sqrt{t(t-1)}\left(A(t)+\frac{\pi i}{2}\right)}
=-\frac{A(t)-\frac{\pi i}{2}}
{\sqrt{t(t-1)}\left(A(t)^2+\frac{\pi^2}{4}\right)}.
\]
Thus
\[
\operatorname{Im}h(-t+i0)
=\frac{\pi/2}
{\sqrt{t(t-1)}\left(A(t)^2+\frac{\pi^2}{4}\right)}>0
\]
for every \(t>1\). This contradicts the Stieltjes half-plane sign condition. Hence \(h\) is not Stieltjes.

Equivalently, the forced Stieltjes inversion density on \((1,\infty)\) would be
\[
\rho_h(t)=-\frac{1}{\pi}\operatorname{Im}h(-t+i0)
=-\frac{1}
{2\sqrt{t(t-1)}\left(A(t)^2+\frac{\pi^2}{4}\right)}<0.
\]

Although \(h\) is not Stieltjes, it is completely monotone on \((0,\infty)\).

Put
\[
a(x)=\operatorname{arsinh}\sqrt{x}.
\]
Then
\[
a'(x)=\frac{1}{2\sqrt{x}\sqrt{1+x}},
\]
a product of completely monotone factors. Hence \(a\) is a Bernstein function. The reciprocal of a positive Bernstein function is completely monotone, so \(1/a\) is completely monotone. Therefore
\[
h(x)=2a'(x)\frac1{a(x)}
\]
is a product of completely monotone functions, and is completely monotone.

_Proof source: `raw/student/20260612T1800-arsinh-square-log-derivative-not-stieltjes.md`._

## Tags

`app-candidate`, `boundary-sign`, `negative-answer`, `primitive-growth`, `proved`, `source-open-solved`, `stieltjes`, `theorem`, `thorin-bernstein`, `true`
