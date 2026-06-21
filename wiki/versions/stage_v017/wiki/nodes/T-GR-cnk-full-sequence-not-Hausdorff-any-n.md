---
id: "T-GR-cnk-full-sequence-not-Hausdorff-any-n"
type: "theorem"
title: "Girjoaba Rasa c(n,k) full sequence not Hausdorff for any n>=1"
status: "proved"
tags: ["binomial", "complete-monotonicity", "counterexample", "hausdorff-moment", "proved", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-girjoaba-rasa-cnk-hausdorff.md"]
---

# Theorem: Girjoaba Rasa c(n,k) full sequence not Hausdorff for any n>=1

## Statement

For every \(n\ge1\), the full Girjoaba--Rasa sequence \(k\mapsto c(n,k)\), \(0\le k\le2n\), is not a Hausdorff moment sequence in the natural order.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-girjoaba-rasa-cnk-hausdorff.md`

## Proof

The source sequence is
\[
c(n,k)=\binom{2n}{k}^{-2}
\sum_{j=0}^k \binom{n}{j}^2\binom{n}{k-j}^2,
\]
with binomial coefficients outside their natural range interpreted as \(0\).

For \(n=1\):
\[
c(1,0)=\binom20^{-2}\binom10^2\binom10^2=1.
\]
For \(k=1\),
\[
c(1,1)=\binom21^{-2}
\left(\binom10^2\binom11^2+\binom11^2\binom10^2\right)
=\frac14(1+1)=\frac12.
\]
For \(k=2\),
\[
c(1,2)=\binom22^{-2}
\left(\binom11^2\binom11^2\right)=1.
\]
Thus the full \(n=1\) sequence begins
\[
1,\quad \frac12,\quad 1.
\]

If \((h_k)\) is a Hausdorff moment sequence on \([0,1]\), then
\[
h_k=\int_0^1 t^k\,d\mu(t)
\]
for some positive measure \(\mu\).  Since \(0\le t\le1\), we have \(t^{k+1}\le t^k\), and therefore
\[
h_{k+1}=\int_0^1 t^{k+1}\,d\mu(t)
\le
\int_0^1 t^k\,d\mu(t)=h_k.
\]
Every Hausdorff moment sequence is nonincreasing.

The \(n=1\) Girjoaba--Rasa sequence violates this necessary condition because
\[
c(1,2)=1>\frac12=c(1,1).
\]

The obstruction is actually uniform in \(n\ge1\).  At the right endpoint,
\[
c(n,2n)=1,
\]
because only \(j=n\) contributes and \(\binom{2n}{2n}=1\).  At the adjacent point \(k=2n-1\), only \(j=n-1\) and \(j=n\) contribute, so
\[
\sum_{j=0}^{2n-1}\binom{n}{j}^2\binom{n}{2n-1-j}^2
=2n^2.
\]
Since \(\binom{2n}{2n-1}=2n\), this gives
\[
c(n,2n-1)=\frac{2n^2}{(2n)^2}=\frac12.
\]
Thus \(c(n,2n)>c(n,2n-1)\) for every \(n\ge1\), so no full sequence \(0\le k\le2n\) can be Hausdorff moment in the natural order.

_Proof source: `private proof note`._

## Tags

`binomial`, `complete-monotonicity`, `counterexample`, `hausdorff-moment`, `proved`, `theorem`
