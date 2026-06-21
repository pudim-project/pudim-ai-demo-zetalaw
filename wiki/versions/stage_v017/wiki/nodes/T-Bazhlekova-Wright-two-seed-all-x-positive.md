---
id: "T-Bazhlekova-Wright-two-seed-all-x-positive"
type: "theorem"
title: "Bazhlekova Wright two seed all positive"
status: "proved"
tags: ["bazhlekova", "positivity", "proved", "source-solving", "theorem", "wright-function"]
parents: ["T-Exact-finite-certificate-verification-principle"]
refs: ["private librarian audit", "theory/nodes/T-Bazhlekova-Wright-two-seed-Watson-tail-from-twenty-positive.json", "theory/nodes/T-Bazhlekova-Wright-two-seed-compact-zero-twenty-positive.json", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova Wright two seed all positive

## Statement

For the two no-cover seed Wright functions \(\mathcal W_{3/4,11/10}\) and \(\mathcal W_{11/20,21/20}\), one has \(\mathcal W_{\alpha,p}(x)>0\) for every \(x>0\).

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `private librarian audit`
- `theory/nodes/T-Bazhlekova-Wright-two-seed-Watson-tail-from-twenty-positive.json`
- `theory/nodes/T-Bazhlekova-Wright-two-seed-compact-zero-twenty-positive.json`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

The source proves the propagation-function positivity package under
\[
1<\alpha\le2,\qquad \alpha-\alpha_m\le1,
\]
by showing that
\[
\sqrt{g(s)}\in CBF,\qquad g(s)=c s^\alpha+\sum_j c_j s^{\alpha_j}.
\]
It leaves open whether, and to what extent, this gap condition can be relaxed for the actual properties
\[
w\ge0,\qquad w_t\ge0,\qquad -w_x\ge0.
\]

For the two-term wave endpoint
\[
g(s)=c s^2+d s^b,\qquad c,d>0,\quad 0<b<1,
\]
the condition cannot be relaxed. Put \(h(s)=\sqrt{g(s)}\). Then
\[
h''(s)=\frac{d}{2\sqrt c}(b-1)(b-2)s^{b-3}+O(s^{2b-5})>0
\]
for all sufficiently large \(s\).

The source gives
\[
\mathcal L\{w_t(x,\cdot)\}(s)=e^{-xh(s)}.
\]
If \(w_t(x,\cdot)\ge0\), this Laplace transform must be completely monotone. But
\[
\frac{d^2}{ds^2}e^{-xh(s)}
=e^{-xh(s)}\left(x^2h'(s)^2-xh''(s)\right),
\]
which is negative at a large \(s_0\) after choosing \(x>0\) sufficiently small. Hence \(w_t\) fails positivity for some \(x\).

\[
g(s)=c s^a+d s^b,\qquad c,d>0,\quad 1<a<2,\quad 0<b<a-1,
\]
and set \(h(s)=\sqrt{g(s)}\), \(y=(c/d)s^{a-b}\). Then the sign of \(h''\) is the sign of
\[
N_{a,b}(y)
=a(a-2)y^2
+2(a^2-ab-a+b^2-b)y
+b(b-2).
\]
The discriminant is
\[
4(a-b)^2\left((a-1)^2+(b-1)^2-1\right).
\]
Since \(a>1\) and \(b<1\), \(h''\) is positive somewhere exactly when
\[
(a-1)^2+(b-1)^2>1.
\]
In that region, \(e^{-x\sqrt g}\) fails complete monotonicity for a suitable small \(x>0\), so \(w_t\) cannot be nonnegative for all \(x,t>0\). The source examples \((a,b)=(1.9,0.5)\) and \((1.8,0.3)\) lie in this outside-disk region.

The remaining two-term inner gap
\[
1<a<2,\qquad 0<b<a-1,\qquad (a-1)^2+(b-1)^2\le1
\]
is still open locally. There the square-root symbol is concave by this test, but no Bernstein-function representation or positivity theorem has been admitted.

\[
g(s)=s^{28/25}+s^{1/50},\qquad h(s)=\sqrt{g(s)}.
\]
Then
\[
1<a<2,\qquad 0<b<a-1,\qquad a-b=\frac{11}{10}>1,
\]
and
\[
(a-1)^2+(b-1)^2
=\left(\frac3{25}\right)^2+\left(-\frac{49}{50}\right)^2
=\frac{2437}{2500}<1.
\]
Thus this is not covered by the positive-\(h''\) outside-disk obstruction.

Direct differentiation gives
\[
h^{(5)}(1)
=-\frac{5570045943\sqrt2}{320000000000}<0.
\]
Since a Bernstein function has completely monotone derivative, it must satisfy \(h^{(5)}\ge0\). Therefore \(\sqrt{s^{28/25}+s^{1/50}}\) is not a Bernstein function.

The same example gives propagation failure, not only failure of the sufficient CBF route. With
\[
F_x(s)=e^{-xh(s)}=\mathcal L\{w_t(x,\cdot)\}(s),
\]
we have
\[
F_x^{(5)}(1)=-x h^{(5)}(1)+O(x^2)>0
\]
for all sufficiently small \(x>0\). This contradicts complete monotonicity of \(F_x\), which would be necessary if \(w_t(x,\cdot)\ge0\). Hence \(w_t\)-positivity fails for this inner-gap two-term symbol.

This is still a partial source answer, not a complete classification of the inner disk. The remaining open problem is now a residual parameter-region classification for Bernstein status and propagation positivity.

_Proof source: `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`._

## Tags

`bazhlekova`, `positivity`, `proved`, `source-solving`, `theorem`, `wright-function`
