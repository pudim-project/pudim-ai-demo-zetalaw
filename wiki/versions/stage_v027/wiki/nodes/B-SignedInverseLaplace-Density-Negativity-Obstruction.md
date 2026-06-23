---
id: "B-SignedInverseLaplace-Density-Negativity-Obstruction"
type: "theorem"
title: "Negative signed inverse-Laplace density obstruction"
status: "proved"
tags: ["bernstein-widder", "bridge-theorem", "complete-monotonicity", "endpoint-obstruction", "laplace-uniqueness", "primitive-support", "proved", "signed-density", "theorem", "true"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language", "T-positive-Laplace-kernel-complete-monotonicity-principle", "D-Endpoint-obstruction-certificate-language"]
refs: ["librarian/audits/LA-20260622T0324-dulacsimon-tsallis-gammaratio-strict-app.json", "oracle/responses/OS-20260622T031636Z-oracle-response.md", "raw/student/20260622T0323-dulacsimon-tsallis-gammaratio-density-obstruction.md"]
---

# Theorem: Negative signed inverse-Laplace density obstruction

## Statement

Let \(F(s)=\int_0^\infty e^{-st}K(t)\,dt\) for \(s>0\), where \(K(t)\,dt\) is a locally finite signed measure of exponential order. If \(K<0\) on a set of positive Lebesgue measure, and this signed measure is the unique inverse-Laplace measure after exponential weighting, then \(F\) is not completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]

## Proof and provenance references

- `librarian/audits/LA-20260622T0324-dulacsimon-tsallis-gammaratio-strict-app.json`
- `oracle/responses/OS-20260622T031636Z-oracle-response.md`
- `raw/student/20260622T0323-dulacsimon-tsallis-gammaratio-density-obstruction.md`

## Proof

Dulac--Simon Remark 11(c) asks whether
\[
\Phi(s)=\frac{(s+1)^2}{2s^2(2s+1)}
\left(1-\frac{\Gamma(s+1)^2}{\Gamma(2s+1)}\right)
\]
is completely monotone on \((-1/2,\infty)\). It is enough to refute complete
monotonicity on the subinterval \((0,\infty)\).

For \(s>0\),
\[
B(s+1,s+1)=\int_0^1 [x(1-x)]^s\,dx .
\]
Set \(a=\log 4\) and \(t=-\log(x(1-x))\). For \(t>a\) the two branches are
\[
x=\frac{1\pm\sqrt{1-4e^{-t}}}{2}.
\]
The two branch Jacobians give
\[
B(s+1,s+1)
=\int_a^\infty e^{-st} w(t)\,dt,\qquad
w(t)=\frac{2e^{-t}}{\sqrt{1-4e^{-t}}}.
\]
Near \(t=a+\varepsilon\),
\[
w(a+\varepsilon)\sim \frac{1}{2\sqrt{\varepsilon}}.
\]

The cancellation
\[
\frac{\Gamma(s+1)^2}{\Gamma(2s+1)}
=(2s+1)B(s+1,s+1)
\]
is used before inversion. Since
\[
\frac{(s+1)^2}{2s^2(2s+1)}
=\frac{1}{2s^2}+\frac{1}{2(2s+1)}
\]
and
\[
\frac{(s+1)^2}{2s^2}
=\frac12+\frac1s+\frac{1}{2s^2},
\]
we have
\[
\Phi(s)=
\frac{1}{2s^2}+\frac{1}{2(2s+1)}
-\left(\frac12+\frac1s+\frac{1}{2s^2}\right)B(s+1,s+1).
\]
Thus \(\Phi(s)=\int_0^\infty e^{-st}K(t)\,dt\), where
\[
K(t)=\frac{t}{2}+\frac14e^{-t/2}
-1_{t>a}\left[
\frac12 w(t)+\int_a^t w(u)\,du
+\frac12\int_a^t(t-u)w(u)\,du
\right].
\]

Let \(y(t)=\sqrt{1-4e^{-t}}\). Then \(y'(t)=w(t)\), so
\[
\int_a^t w(u)\,du=y(t).
\]
Also
\[
\int_a^t(t-u)w(u)\,du
=\int_a^t y(u)\,du
=\log\left(\frac{1+y(t)}{1-y(t)}\right)-2y(t).
\]
Therefore, for \(t>a\),
\[
K(t)=\frac{t}{2}+\frac14e^{-t/2}
-\frac{e^{-t}}{\sqrt{1-4e^{-t}}}
-\frac12\log\left(\frac{1+\sqrt{1-4e^{-t}}}
{1-\sqrt{1-4e^{-t}}}\right).
\]

At \(t=a+\varepsilon\),
\[
1-4e^{-t}=1-e^{-\varepsilon}\sim\varepsilon,
\]
so
\[
\frac{e^{-t}}{\sqrt{1-4e^{-t}}}
\sim\frac{1}{4\sqrt{\varepsilon}}.
\]
The logarithm is \(O(\sqrt{\varepsilon})\), and the remaining terms stay finite.
Hence
\[
K(\log4+\varepsilon)
\sim -\frac{1}{4\sqrt{\varepsilon}}
\qquad(\varepsilon\downarrow0).
\]
Thus \(K\) is negative on a right-neighborhood of \(\log4\).

_Proof source: `raw/student/20260622T0323-dulacsimon-tsallis-gammaratio-density-obstruction.md`._

## Tags

`bernstein-widder`, `bridge-theorem`, `complete-monotonicity`, `endpoint-obstruction`, `laplace-uniqueness`, `primitive-support`, `proved`, `signed-density`, `theorem`, `true`
