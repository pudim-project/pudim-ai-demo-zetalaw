---
id: "T-Bazhlekova-TwoSeed-SqrtBF-OutsideGap"
type: "theorem"
title: "Bazhlekova two outside-gap square-root symbols are Bernstein"
status: "proved"
tags: ["bazhlekova", "bernstein-function", "fractional-diffusion-wave", "primitive-bridge", "proved", "theorem", "true", "wright-density"]
parents: ["T-Bazhlekova-Wright-density-topcap-bridge-normal-form", "T-Bazhlekova-Wright-two-seed-all-x-positive"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "private proof note"]
---

# Theorem: Bazhlekova two outside-gap square-root symbols are Bernstein

## Statement

Let \(g_1(s)=s^{3/2}+s^{2/5}\) and \(g_2(s)=s^{11/10}+s^{1/20}\). Then \(h_i(s)=\sqrt{g_i(s)}\) is a Bernstein function on \((0,\infty)\) for \(i=1,2\), even though the exponent gaps are \(11/10\) and \(21/20\).

## Dependencies

- [[wiki/nodes/T-Bazhlekova-Wright-density-topcap-bridge-normal-form|Bazhlekova Wright density topcap bridge normal form]]
- [[wiki/nodes/T-Bazhlekova-Wright-two-seed-all-x-positive|Bazhlekova Wright two seed all positive]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `private proof note`

## Proof

For
\[
h(s)=s^\alpha(1+s^{-p})^{1/2},\qquad 0<\alpha-p/2<\alpha<1,\quad 1<p<2,
\]
the the corresponding theorem the Bazhlekova Wright density topcap bridge normal form proves
\[
\mathcal L^{-1}\{h'\}(t)=t^{-\alpha}\mathcal W_{\alpha,p}(t^p),
\]
where
\[
\mathcal W_{\alpha,p}(x)=
-\sum_{m\ge0}\binom{1/2}{m}\frac{x^m}{\Gamma(pm-\alpha)}.
\]
Thus \(\mathcal W_{\alpha,p}(x)>0\) for all \(x>0\) implies \(h'\in CM\), hence \(h\in BF\).

For \(g_1\), \((\alpha,p)=(3/4,11/10)\). For \(g_2\), \((\alpha,p)=(11/20,21/20)\).

The node the Bazhlekova Wright two seed compact zero ten positive proves
\[
\mathcal W_{3/4,11/10}(x)>0,\qquad
\mathcal W_{11/20,21/20}(x)>0
\qquad(0\le x\le10).
\]
Its proof artifacts are:

The node the Bazhlekova Wright two seed post ten derivative positive proves
\[
\mathcal W_{3/4,11/10}'(x)>0,\qquad
\mathcal W_{11/20,21/20}'(x)>0
\qquad(10\le x\le20),
\]
with lower bounds \(0.0201343226217\ldots\) and \(0.00299977163172\ldots\). Since the functions are positive at \(10\), this proves positivity on \([10,20]\). Its proof artifacts are:

The node the Bazhlekova Wright two seed Watson tail from twenty positive proves positivity for \(x\ge20\) by a three-term Watson contour certificate. The replay output at \(x=20\) gives margins
\[
0.732374180856\ldots
\]
for \((3/4,11/10)\), and
\[
0.100568095684\ldots
\]
for \((11/20,21/20)\). Its proof artifacts are:

Combining the three certified ranges gives the the corresponding theorem the Bazhlekova Wright two seed all x positive:
\[
\mathcal W_{3/4,11/10}(x)>0,\qquad
\mathcal W_{11/20,21/20}(x)>0
\qquad(x>0).
\]

This proves that the source condition \(\alpha-\alpha_m\le1\) is not necessary for the positivity/subordination package. It does not classify all relaxations and does not claim \(\sqrt{g_i}\in CBF\); in fact the off-cut zeros for gap \(>1\) block the CBF shortcut.

_Proof source: `private proof note`._

## Do not claim

- Do not claim complete-Bernstein status.
- Do not claim a full relaxed parameter classification.

## Tags

`bazhlekova`, `bernstein-function`, `fractional-diffusion-wave`, `primitive-bridge`, `proved`, `theorem`, `true`, `wright-density`
