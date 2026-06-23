---
id: "T-Bazhlekova-wave-endpoint-two-term-no-relaxation"
type: "theorem"
title: "Bazhlekova two-term wave endpoint alpha=2 alpha_m=b<1 no relaxation positivity package fails"
status: "proved"
tags: ["bazhlekova", "bernstein-function", "complete-monotonicity", "diffusion-wave", "no-relaxation-slice", "not-staging-application", "proved", "source-facing-partial", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "T-sqrt-wave-symbol-eventual-convexity-blt1"]
refs: ["attack-plans/AP-20260531T073000-bazhlekova-wave-endpoint.json", "librarian/audits/LA-20260531T073000-bazhlekova-wave-endpoint.json", "raw/student/20260531T073000-bazhlekova-wave-endpoint.md", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova two-term wave endpoint alpha=2 alpha_m=b<1 no relaxation positivity package fails

## Statement

For the two-term wave-endpoint symbol \(g(s)=c s^2+d s^b\) with \(c,d>0\) and \(0<b<1\), Bazhlekova's propagation positivity package cannot hold for all \(x,t>0\); in fact \(w_t(x,\cdot)\) is not nonnegative for some \(x>0\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/T-sqrt-wave-symbol-eventual-convexity-blt1|sqrt(c s^2+d s^b) eventually convex for c,d>0 and 0<b<1]]

## Proof and provenance references

- `attack-plans/AP-20260531T073000-bazhlekova-wave-endpoint.json`
- `librarian/audits/LA-20260531T073000-bazhlekova-wave-endpoint.json`
- `raw/student/20260531T073000-bazhlekova-wave-endpoint.md`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

Let
\[
h(s)=\sqrt{c s^2+d s^b},\qquad c,d>0,\quad 0<b<1.
\]
As \(s\to\infty\),
\[
h(s)=\sqrt c\,s\left(1+\frac{d}{c}s^{b-2}\right)^{1/2}.
\]
Since \(b-2<0\), the analytic expansion of \((1+u)^{1/2}\) at \(u=0\), with differentiated remainder, gives
\[
h(s)=\sqrt c\,s+\frac{d}{2\sqrt c}s^{b-1}+O(s^{2b-3}).
\]
Differentiating twice,
\[
h''(s)=\frac{d}{2\sqrt c}(b-1)(b-2)s^{b-3}+O(s^{2b-5}).
\]
Because \(0<b<1\), \((b-1)(b-2)>0\). The error has strictly lower order, since \(2b-5 < b-3\). Hence
\[
h''(s)>0
\]
for all sufficiently large \(s\). Candidate 1 is true.

For the two-term wave-endpoint equation, the Laplace transform calculation in the source gives
\[
\widehat{w}(x,s)=\frac1s e^{-x h(s)},
\qquad h(s)=\sqrt{c s^2+d s^b}.
\]
Therefore
\[
\mathcal L\{w_t(x,\cdot)\}(s)=s\widehat w(x,s)-w(x,0)=e^{-x h(s)}.
\]
If \(w_t(x,t)\ge0\) for every \(t>0\), then \(F_x(s)=e^{-x h(s)}\) must be completely monotone in \(s\), so in particular \(F_x''(s)\ge0\) for every \(s>0\).

But
\[
F_x''(s)=e^{-x h(s)}\left(x^2h'(s)^2-xh''(s)\right).
\]
Choose \(s_0\) large enough that \(h''(s_0)>0\). Since \(h'(s_0)>0\), choose
\[
0<x<\frac{h''(s_0)}{h'(s_0)^2}.
\]
Then
\[
F_x''(s_0)<0,
\]
contradicting complete monotonicity. Thus \(w_t(x,\cdot)\) is not nonnegative for some \(x>0\).

Consequently, when \(\alpha=2\), \(c,d>0\), and \(0<\alpha_m=b<1\), the source positivity package cannot hold. The source condition is sharp in this two-term wave-endpoint slice: \(2-b\le1\) is necessary there.

Candidate 2 is true.

The broader two-term gap question
\[
g(s)=c s^a+d s^b,\qquad 1<a\le2,\quad a-b>1,
\]
is left open. The endpoint proof uses the linear leading term at \(a=2\), and the same asymptotic sign argument does not immediately cover every \(a<2\). Under the no-stalling rule, rotate after admitting the endpoint slice.

_Proof source: `raw/student/20260531T073000-bazhlekova-wave-endpoint.md`._

## Tags

`bazhlekova`, `bernstein-function`, `complete-monotonicity`, `diffusion-wave`, `no-relaxation-slice`, `not-staging-application`, `proved`, `source-facing-partial`, `theorem`
