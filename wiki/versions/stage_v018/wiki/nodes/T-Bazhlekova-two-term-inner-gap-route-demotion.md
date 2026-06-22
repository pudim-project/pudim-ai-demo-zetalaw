---
id: "T-Bazhlekova-two-term-inner-gap-route-demotion"
type: "theorem"
title: "Bazhlekova two-term inner gap second derivative concavity obstruction exhausted"
status: "proved"
tags: ["bazhlekova", "concavity", "not-staging-application", "proved", "route-demotion", "theorem", "two-term"]
parents: ["T-Pointwise-obstruction-certificate-principle", "T-sqrt-two-term-symbol-exact-concavity-criterion"]
refs: ["attack-plans/AP-20260531T081500-two-term-sqrt-concavity.json", "librarian/audits/LA-20260531T081500-two-term-sqrt-concavity.json", "raw/student/20260531T081500-two-term-sqrt-concavity.md", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md", "wiki/notes/two-term-square-root-concavity-criterion.md"]
---

# Theorem: Bazhlekova two-term inner gap second derivative concavity obstruction exhausted

## Statement

In the Bazhlekova two-term inner gap \(1<a<2\), \(0<b<a-1\), \((a-1)^2+(b-1)^2\le1\), the second-derivative concavity obstruction for \(\sqrt{c s^a+d s^b}\) is exhausted and cannot decide the remaining propagation positivity problem.

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]
- [[wiki/nodes/T-sqrt-two-term-symbol-exact-concavity-criterion|exact concavity criterion for sqrt(c s^a + d s^b) two-term power symbol]]

## Proof and provenance references

- `attack-plans/AP-20260531T081500-two-term-sqrt-concavity.json`
- `librarian/audits/LA-20260531T081500-two-term-sqrt-concavity.json`
- `raw/student/20260531T081500-two-term-sqrt-concavity.md`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`
- `wiki/notes/two-term-square-root-concavity-criterion.md`

## Proof

Write \(f(s)=c s^a+d s^b\). Then
\[
h''(s)=\frac{2f(s)f''(s)-f'(s)^2}{4f(s)^{3/2}}.
\]
A direct expansion gives
\[
4h(s)^3h''(s)
=c^2 a(a-2)s^{2a-2}
+2cd\bigl(a^2+b^2-ab-a-b\bigr)s^{a+b-2}
+d^2b(b-2)s^{2b-2}.
\]
If \(a=b\), then \(h(s)=\sqrt{c+d}\,s^{a/2}\), so \(h\) is concave on \((0,\infty)\) exactly when \(0\le a\le2\).

Assume now \(a\ne b\), and set
\[
t=\frac cd\,s^{a-b}.
\]
As \(s\) ranges over \((0,\infty)\), so does \(t\). The sign of \(h''\) is therefore the sign of
\[
Q(t)=A t^2+2D t+C,\qquad t>0,
\]
where
\[
A=a(a-2),\qquad C=b(b-2),\qquad D=a^2+b^2-ab-a-b.
\]

Thus \(h\) is concave exactly when \(Q(t)\le0\) for every \(t>0\).

The condition \(Q(t)\le0\) on \((0,\infty)\) first forces
\[
A\le0,\qquad C\le0,
\]
by taking \(t\to\infty\) and \(t\to0^+\). These are equivalent to \(a,b\in[0,2]\).

If \(D\le0\), then all three coefficients of \(Q\) are nonpositive, hence \(Q(t)\le0\) for every \(t>0\).

If \(D>0\), the concave quadratic has its maximum at
\[
t_*=-\frac DA>0
\]
when \(A<0\); endpoint cases \(A=0\) are included by continuity and by the same final inequality. The maximum condition is
\[
Q(t_*)=C-\frac{D^2}{A}\le0.
\]
Since \(A<0\), this is equivalent to
\[
D^2\le AC.
\]
When \(A=0\) and \(D>0\), the function \(Q(t)=2Dt+C\) eventually becomes positive, and \(D^2\le AC=0\) fails. The \(C=0\) endpoint is symmetric. Hence no endpoint exception is missing.

Therefore, for \(a\ne b\), \(h\) is concave on \((0,\infty)\) if and only if
\[
A\le0,\qquad C\le0,\qquad
\left(D\le0\quad\text{or}\quad D^2\le AC\right).
\]

Equivalently,
\[
a(a-2)\le0,\qquad b(b-2)\le0,
\]
and
\[
a^2+b^2-ab-a-b\le0
\]
or
\[
\bigl(a^2+b^2-ab-a-b\bigr)^2
\le a(a-2)b(b-2).
\]

In the Bazhlekova two-term gap regime
\[
1<a<2,\qquad 0<b<a-1,
\]
the two exponents straddle \(1\). In this regime,
\[
D^2-AC=(a-b)^2\left((a-1)^2+(b-1)^2-1\right).
\]
Thus the inner disk condition
\[
(a-1)^2+(b-1)^2\le1
\]
is exactly the condition under which the second-derivative concavity obstruction is absent. The remaining question there is not a concavity question; it requires testing whether \(\sqrt g\) is Bernstein by higher derivatives or proving sign change in the inverse Laplace transform.

_Proof source: `raw/student/20260531T081500-two-term-sqrt-concavity.md`._

## Tags

`bazhlekova`, `concavity`, `not-staging-application`, `proved`, `route-demotion`, `theorem`, `two-term`
