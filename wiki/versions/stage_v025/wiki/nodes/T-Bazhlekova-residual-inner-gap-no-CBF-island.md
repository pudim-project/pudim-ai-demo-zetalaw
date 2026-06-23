---
id: "T-Bazhlekova-residual-inner-gap-no-CBF-island"
type: "theorem"
title: "Bazhlekova residual inner gap no complete Bernstein function island"
status: "proved"
tags: ["bazhlekova", "complete-bernstein", "inner-gap", "pick-function", "proved", "route-demotion", "theorem"]
parents: ["T-Polynomial-root-logderivative-localization-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260601T023000-bazhlekova-inner-gap-next-split-student.json", "oracle/responses/ORACLE-OS-20260601T021500-bazhlekova-inner-gap-next-split-oracle-response.md", "raw/student/20260601T023000-bazhlekova-inner-gap-next-split.md", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova residual inner gap no complete Bernstein function island

## Statement

For every residual two-term Bazhlekova pair with \(1<a<2\), \(0<b<a-1\), and \(p=a-b>1\), the normalized square-root symbol \(z^{b/2}(1+z^p)^{1/2}\) is not a complete Bernstein function, because it fails the upper-half-plane Pick mapping condition.

## Dependencies

- [[wiki/nodes/T-Polynomial-root-logderivative-localization-principle|Polynomial root and logarithmic-derivative localization principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260601T023000-bazhlekova-inner-gap-next-split-student.json`
- `oracle/responses/ORACLE-OS-20260601T021500-bazhlekova-inner-gap-next-split-oracle-response.md`
- `raw/student/20260601T023000-bazhlekova-inner-gap-next-split.md`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

\[
h(s)=\sqrt{c s^a+d s^b},\qquad \Delta=a-b,\qquad B=\frac b2,\qquad y=\frac cd s^\Delta,
\]
one has
\[
h^{(n)}(s)=\sqrt d\,s^{B-n}(1+y)^{1/2-n}Q_n(y),
\]
where
\[
Q_0=1
\]
and
\[
Q_{n+1}
=(B-n)(1+y)Q_n
+
\Delta y\left((1+y)Q_n'+\left(\frac12-n\right)Q_n\right).
\]

The small-\(x\) obstruction criterion is also already admitted: if \(Q_{2q+1}(y_0)<0\), then \(e^{-x h(s)}\) fails complete monotonicity for sufficiently small \(x>0\), and therefore \(w_t\)-positivity fails by the Bazhlekova source transform.

Factoring at infinity gives
\[
h(s)=s^\alpha(1+s^{-p})^{1/2},\qquad
\alpha=\frac a2,\qquad p=a-b.
\]
Formally,
\[
h^{(n)}(s)
=
s^{\alpha-n}\sum_{k\ge0}\binom{1/2}{k}
(\alpha-kp)^{\underline n}s^{-kp}.
\]
For odd \(n\), the expected high-order scaling at \(s=n\lambda^{-1/p}\) is governed by a Wright-type series
\[
W_{\alpha,p}(\lambda)
=
\Gamma(-\alpha)
\sum_{k\ge0}\binom{1/2}{k}
\frac{\lambda^k}{\Gamma(kp-\alpha)}.
\]
If this limit is made uniform and \(W_{\alpha,p}(\lambda)<0\), it should force \(Q_n(y)<0\) for suitable large odd \(n\). This is a useful attack route, but it was not made rigorous in this pass. In particular, no uniform error term or certified sign theorem for all residual \((a,b)\) was proved.

the Bazhlekova inner gap Wright negativity asymptotic remains candidate_open.

The same recurrence gives exact higher-order failures near the no-cover region. At
\[
(a,b)=\left(\frac65,\frac3{50}\right)
\]
one has
\[
(a-1)^2+(b-1)^2=\frac{2309}{2500}<1,
\]
and exact arithmetic gives
\[
Q_{15}(7)
=
-\frac{
434760875594285819585555985243010187013443016125523
}{
10^{30}
}<0.
\]
Sturm checks show that \(Q_5,Q_7,Q_9,Q_{11},Q_{13}\) have no positive roots at this same exponent pair, while \(Q_{15}\) has positive roots.

At
\[
(a,b)=\left(\frac32,\frac6{25}\right)
\]
one has
\[
(a-1)^2+(b-1)^2=\frac{2069}{2500}<1,
\]
and
\[
Q_{17}(18)
=
-\frac{
92346987336079787603307566542588163710044182165813724538743
}{
9536743164062500000000000000
}<0.
\]
Here \(Q_5,Q_7,Q_9,Q_{11},Q_{13},Q_{15}\) have no positive roots, while \(Q_{17}\) has positive roots.

By the admitted odd-derivative small-\(x\) criterion, both exponent pairs give uniform \(w_t\)-positivity failure for all \(c,d>0\).

The no-cover seeds may still lie in a plain Bernstein-function island, but they cannot lie in a complete Bernstein-function island.

Indeed, for the normalized branch
\[
f(z)=z^{b/2}(1+z^p)^{1/2},\qquad p=a-b>1,
\]
take \(z=r e^{i\theta}\) with \(0<\theta<\pi\), \(p\theta>\pi\), and \(r\to\infty\). Since \(1<p<2\) in the residual two-term region, the principal argument of \(1+z^p\) tends to \(p\theta-2\pi\). Hence
\[
\arg f(r e^{i\theta})
\to
\frac b2\theta+\frac{p\theta-2\pi}{2}
=
\frac a2\theta-\pi.
\]
Because \(a/2<1\), choosing \(\theta\) sufficiently close to \(\pi\) keeps this limiting argument negative. Thus \(f\) sends some upper-half-plane points into the lower half-plane and cannot be a Pick function; in particular it is not a complete Bernstein function. This does not rule out plain Bernstein status.

the Bazhlekova no cover neighborhood BF island diagnostic remains candidate_open; the complete-Bernstein subroute is refuted, but the plain Bernstein/inverse-Laplace alternatives remain open.

Finite seed positivity certificate through order \(201\) at \((3/2,2/5)\) and \((11/10,1/20)\).
Exact higher-order obstruction seeds \(Q_{15}^{6/5,3/50}(7)<0\) and \(Q_{17}^{3/2,6/25}(18)<0\).
No complete-Bernstein island for residual \(p=a-b>1\).

_Proof source: `raw/student/20260601T023000-bazhlekova-inner-gap-next-split.md`._

## Tags

`bazhlekova`, `complete-bernstein`, `inner-gap`, `pick-function`, `proved`, `route-demotion`, `theorem`
