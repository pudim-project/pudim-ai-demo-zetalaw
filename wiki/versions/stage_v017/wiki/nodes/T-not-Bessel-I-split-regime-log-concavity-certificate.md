---
id: "T-not-Bessel-I-split-regime-log-concavity-certificate"
type: "theorem"
title: "no complete three-regime certificate can prove the false all-nu all-u Riccati log-concavity inequality"
status: "proved"
tags: ["attack-plan", "counterexample", "proved", "refutation", "split-regime", "theorem"]
parents: ["T-not-Bessel-I-Riccati-log-concavity-inequality"]
refs: ["private librarian audit", "private proof note", "private proof artifact", "wiki/notes/frontier-bessel-i-log-concavity.md"]
---

# Theorem: no complete three-regime certificate can prove the false all-nu all-u Riccati log-concavity inequality

## Statement

not(There is a three-regime certificate proving the Riccati log-concavity inequality for all \(\nu\ge0\) and \(u>0\): small-\(u\) from the convergent series for \(I_\nu\), large-\(u\) from uniform asymptotics/log-derivative bounds, and the remaining compact region from certified interval inequalities in \((\nu,u)\).)

## Dependencies

- [[wiki/nodes/T-not-Bessel-I-Riccati-log-concavity-inequality|exists nu >= 0 and u > 0 such that Riccati log-concavity expression is nonnegative]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `private proof artifact`
- `wiki/notes/frontier-bessel-i-log-concavity.md`

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

_Proof source: `private proof note`._

## Tags

`attack-plan`, `counterexample`, `proved`, `refutation`, `split-regime`, `theorem`
