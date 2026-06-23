---
id: "T-AB-geometric-log-kernel-sign-change"
type: "theorem"
title: "Alzer Berg reciprocal geometric slice logarithmic complete monotonicity kernel changes sign"
status: "proved"
tags: ["alzer-berg", "geometric-mean", "gini-mean", "kernel-sign", "proved", "route-demotion", "theorem"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260530T-ab-reciprocal-lcm-route-student.json", "oracle/responses/ORACLE-OS-20260530T-ab-reciprocal-lcm-oracle-response.md", "raw/student/20260530T-ab-reciprocal-lcm-route-obstruction.md", "wiki/notes/frontier-ab-reciprocal-gini-gamma-quotient.md"]
---

# Theorem: Alzer Berg reciprocal geometric slice logarithmic complete monotonicity kernel changes sign

## Statement

For the geometric Gini slice \(a=b=0\), so \(G_{0,0}(u,v)=\sqrt{uv}\), the log-derivative kernel for \(Q_{0,0}=1/P_{0,0}\) is positive near \(t=0\) and negative for all sufficiently large \(t\); hence it changes sign.

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260530T-ab-reciprocal-lcm-route-student.json`
- `oracle/responses/ORACLE-OS-20260530T-ab-reciprocal-lcm-oracle-response.md`
- `raw/student/20260530T-ab-reciprocal-lcm-route-obstruction.md`
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

_Proof source: `raw/student/20260530T-ab-reciprocal-lcm-route-obstruction.md`._

## Tags

`alzer-berg`, `geometric-mean`, `gini-mean`, `kernel-sign`, `proved`, `route-demotion`, `theorem`
