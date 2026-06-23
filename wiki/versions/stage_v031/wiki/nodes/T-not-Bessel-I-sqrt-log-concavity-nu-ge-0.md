---
id: "T-not-Bessel-I-sqrt-log-concavity-nu-ge-0"
type: "theorem"
title: "exists nu >= 0 and u > 0 such that second derivative of log(sqrt(u) I_nu(u)) is nonnegative"
status: "proved"
tags: ["application-bridge", "application-candidate", "bessel", "counterexample", "proved", "refutation", "source-open-solved", "terminal", "theorem"]
parents: ["T-Pointwise-obstruction-certificate-principle"]
refs: ["librarian/audits/LA-20260526T124356-student-ingest.json", "raw/student/20260526T124356-bessel-i-log-concavity-counterexample.md", "raw/student/20260526T124356-bessel-i-log-concavity-counterexample.py", "wiki/notes/frontier-bessel-i-log-concavity.md", "wiki/notes/scout-bessel-i-log-concavity-counterexample.md"]
---

# Theorem: exists nu >= 0 and u > 0 such that second derivative of log(sqrt(u) I_nu(u)) is nonnegative

## Statement

not(For every \(\nu\ge0\), the function \(u\mapsto \sqrt{u}\,I_\nu(u)\) is strictly log-concave on \((0,\infty)\).)

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260526T124356-student-ingest.json`
- `raw/student/20260526T124356-bessel-i-log-concavity-counterexample.md`
- `raw/student/20260526T124356-bessel-i-log-concavity-counterexample.py`
- `wiki/notes/frontier-bessel-i-log-concavity.md`
- `wiki/notes/scout-bessel-i-log-concavity-counterexample.md`

## Proof

Let
\[
g_\nu(u)=\log(\sqrt u\,I_\nu(u)),
\qquad
r_\nu(u)=\frac{I_\nu'(u)}{I_\nu(u)}.
\]
Then
\[
g_\nu''(u)=r_\nu'(u)-\frac{1}{2u^2}.
\]
The modified Bessel equation
\[
u^2I_\nu''(u)+uI_\nu'(u)-(u^2+\nu^2)I_\nu(u)=0
\]
gives
\[
\frac{I_\nu''(u)}{I_\nu(u)}
=1+\frac{\nu^2}{u^2}-\frac{r_\nu(u)}{u}.
\]
Since
\[
r_\nu'(u)=\frac{I_\nu''(u)}{I_\nu(u)}-r_\nu(u)^2,
\]
we get
\[
g_\nu''(u)
=
1+\frac{\nu^2-\frac12}{u^2}
-\frac{r_\nu(u)}{u}
-r_\nu(u)^2.
\]
Thus the Bessel I Riccati log concavity inequality is exactly the strict log-concavity condition \(g_\nu''(u)<0\).

For \(\nu=0\),
\[
r_0(u)=\frac{I_0'(u)}{I_0(u)}=\frac{I_1(u)}{I_0(u)}.
\]
At \(u=10\), the Riccati expression is
\[
g_0''(10)=\frac{199}{200}-\frac{r_0(10)}{10}-r_0(10)^2.
\]
It is enough to prove
\[
r_0(10)<\frac{9487}{10000},
\]
because
\[
\frac{199}{200}
-\frac{1}{10}\frac{9487}{10000}
-\left(\frac{9487}{10000}\right)^2
=\frac{9831}{100000000}>0.
\]

\[
I_0(10)=\sum_{k=0}^{\infty}\frac{25^k}{(k!)^2},
\qquad
I_1(10)=\sum_{k=0}^{\infty}\frac{5\cdot25^k}{k!(k+1)!}.
\]
With \(N=20\), set
\[
L_0=\sum_{k=0}^{20}\frac{25^k}{(k!)^2}<I_0(10).
\]
For the \(I_1\) tail after \(N=20\), the term ratio is bounded by
\[
q=\frac{25}{22\cdot23}<1,
\]
so the script computes an exact rational upper bound \(U_1>I_1(10)\) and verifies
\[
10000\,U_1<9487\,L_0.
\]
Therefore \(I_1(10)/I_0(10)<9487/10000\), and hence
\[
g_0''(10)>0.
\]

This proves the Bessel-\(I\) log-concavity counterexample to \(T\)-\(I\) sqrt-log concavity for \(\nu>0\), and the counterexample to \(T\)-\(I\) Riccati log-concavity inequality.

_Proof source: `raw/student/20260526T124356-bessel-i-log-concavity-counterexample.md`._

## Tags

`application-bridge`, `application-candidate`, `bessel`, `counterexample`, `proved`, `refutation`, `source-open-solved`, `terminal`, `theorem`
