---
id: "T-not-AB-reciprocal-LCM-route-internal-Gini"
type: "theorem"
title: "Alzer Berg reciprocal quotient LCM positive kernel route fails for strict internal Gini means"
status: "proved"
tags: ["alzer-berg", "gamma-quotient", "kernel-sign", "logarithmically-completely-monotone", "proved", "route-demotion", "theorem"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-ab-reciprocal-gini-gamma-quotient.md"]
---

# Theorem: Alzer Berg reciprocal quotient LCM positive kernel route fails for strict internal Gini means

## Statement

For \(v>u>0\), \(d=v-u\), and any strict internal Gini mean value \(u<G_{a,b}(u,v)<v\), the natural positive-kernel route to logarithmic complete monotonicity of \(Q_{a,b}=1/P_{a,b}\) fails: the kernel of \(-\partial_x\log Q_{a,b}\), namely \((dte^{-Gt}-(e^{-ut}-e^{-vt}))/(1-e^{-t})\), is eventually negative.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-ab-reciprocal-gini-gamma-quotient.md`

## Proof

Differentiating gives
\[
-\partial_x\log Q_{a,b}(u,v;x)
=d\psi'(x+G)-(\psi(x+v)-\psi(x+u)).
\]
Using the standard kernels
\[
\psi'(x+G)=\int_0^\infty
\frac{t e^{-(x+G)t}}{1-e^{-t}}\,dt
\]
and
\[
\psi(x+v)-\psi(x+u)
=\int_0^\infty
\frac{e^{-(x+u)t}-e^{-(x+v)t}}{1-e^{-t}}\,dt,
\]
we obtain
\[
-\partial_x\log Q_{a,b}(u,v;x)
=
\int_0^\infty e^{-xt}
\frac{d\,t e^{-Gt}-(e^{-ut}-e^{-vt})}{1-e^{-t}}\,dt.
\]

Let
\[
N(t)=d\,t e^{-Gt}-e^{-ut}+e^{-vt}.
\]
If \(u<G<v\), then
\[
e^{ut}N(t)
=d\,t e^{-(G-u)t}-1+e^{-(v-u)t}
\to -1
\qquad(t\to\infty).
\]
Therefore \(N(t)<0\) for all sufficiently large \(t\). Since \(1-e^{-t}>0\), the displayed log-derivative kernel is eventually negative.

Thus the standard positive-kernel route proving logarithmic complete monotonicity cannot work for any strict internal Gini mean. This includes every nontrivial finite-parameter Gini mean slice \(v>u>0\).

For \(a=b=0\), \(G_{0,0}(u,v)=\sqrt{uv}\), so \(u<G<v\). The same tail obstruction applies.

Moreover, near \(t=0\),
\[
N(t)
=d\left(\frac{u+v}{2}-G\right)t^2+O(t^3).
\]
For \(G=\sqrt{uv}\),
\[
\frac{u+v}{2}-\sqrt{uv}
=\frac{(\sqrt v-\sqrt u)^2}{2}>0.
\]
Thus the geometric log-kernel is positive near \(0\) and negative for large \(t\), so it changes sign.

_Proof source: `private proof note`._

## Tags

`alzer-berg`, `gamma-quotient`, `kernel-sign`, `logarithmically-completely-monotone`, `proved`, `route-demotion`, `theorem`
