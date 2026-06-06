---
id: "T-Zeta-tail-floor-gap-template"
type: "theorem"
title: "finite plus modular gap template for inverse zeta tail floor traps"
status: "proved"
tags: ["attack-plan", "floor-gap", "modular-residue", "proved", "proved-s9", "student", "theorem", "zeta-tail"]
parents: ["D-Tail-zeta-partition-function", "T-endpoint-log-derivative-monotonicity-principle"]
refs: ["librarian/audits/LA-20260527T234000-zeta-tail-s9-ingest.json", "raw/student/20260527T233000-zeta-tail-template-check.py", "raw/student/20260527T233000-zeta-tail-template.md", "wiki/notes/frontier-zeta-tail-next-template.md"]
---

# Theorem: finite plus modular gap template for inverse zeta tail floor traps

## Statement

For rational inverse-tail approximants \(A_s(n)<B_s(n)\), there is a reusable finite-plus-modular gap template proving that no integer lies in \([A_s(n),B_s(n)]\) for all required \(n\), generalizing the staged \(s=7\) residue trap and \(s=8\) finite-plus-modular gap check.

## Dependencies

- [[wiki/nodes/D-Tail-zeta-partition-function|Tail zeta partition function]]
- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260527T234000-zeta-tail-s9-ingest.json`
- `raw/student/20260527T233000-zeta-tail-template-check.py`
- `raw/student/20260527T233000-zeta-tail-template.md`
- `wiki/notes/frontier-zeta-tail-next-template.md`

## Proof

For integer \(s>1\), the Hurwitz-tail Euler--Maclaurin expansion has the form
\[
\zeta_n(s)
=n^{1-s}\left[
\frac1{s-1}+\frac{z}{2}
+\sum_{r\ge1}\frac{B_{2r}}{(2r)!}(s)_{2r-1}z^{2r}
\right],
\qquad z=\frac1n.
\]
Formally inverting the bracket gives
\[
\zeta_n(s)^{-1}\sim n^{s-1}G_s(z).
\]

The replay script
computes \(G_s\) symbolically and verifies two things:

1. For \(s=8\), the coefficients through \(z^{15}\) reproduce the staged \(A_8\) and \(B_8-A_8\) coefficients.
2. For \(s=9\), truncating \(n^8G_9(1/n)\) through \(z^{14}\) gives an \(A_9\), and adding the \(z^{15}\) term gives \(B_9\), with exact telescoping residuals of the expected signs.

The generated \(s=9\) lower approximant is
\[
\begin{aligned}
A_9(n)=&8n^8-32n^7+80n^6-128n^5+120n^4-64n^3
+\frac{624}{7}n^2-\frac{512}{7}n-\frac{3324}{7}\\
&+\frac{90304}{21n^2}+\frac{90304}{21n^3}
-\frac{10280944}{245n^4}-\frac{64846304}{735n^5}
+\frac{109940976}{245n^6}.
\end{aligned}
\]
The upper approximant is
\[
B_9(n)=A_9(n)+\frac{384388288}{245n^7}.
\]

Let \(R_A(n)=1/A_9(n)\) and \(R_B(n)=1/B_9(n)\). Exact denominator clearing gives:
\[
R_A(k)-R_A(k+1)-\frac1{k^9}>0
\qquad(k\ge5),
\]
because the numerator, after substituting \(k=m+5\), has all coefficients positive. Similarly,
\[
\frac1{k^9}-\left(R_B(k)-R_B(k+1)\right)>0
\qquad(k\ge1),
\]
because the denominator-cleared numerator, after substituting \(k=m+1\), has all coefficients positive.

Therefore, for \(n\ge5\),
\[
A_9(n)<\zeta_n(9)^{-1}<B_9(n).
\]

This proves the inverse-window part of the reusable template and promotes the Zeta tail inverse asymptotic telescoping template.

The replay script also verifies the no-integer gap.

Write \(P_9(n)\) for the polynomial part of \(A_9(n)\):
\[
P_9(n)=8n^8-32n^7+80n^6-128n^5+120n^4-64n^3
+\frac{624}{7}n^2-\frac{512}{7}n-\frac{3324}{7}.
\]
Modulo \(7\), the fractional numerator of \(P_9(n)\) is
\[
n^2-n+1\pmod 7,
\]
so the fractional part of \(P_9(n)\) is one of
\[
0,\quad \frac17,\quad \frac37,\quad \frac67.
\]

The correction \(A_9(n)-P_9(n)\) is positive for \(n\ge9\); after denominator clearing and substituting \(n=m+9\), the numerator has all coefficients positive. For \(n\ge174\), the upper correction is bounded by
\[
B_9(n)-P_9(n)
<
\frac{90304}{21n^2}
+\frac{90304}{21n^3}
+\frac{109940976}{245n^6}
+\frac{384388288}{245n^7}
<\frac17.
\]
Therefore \(A_9(n)\) and \(B_9(n)\) cannot straddle an integer for \(n\ge174\). Exact rational arithmetic verifies
\[
\lfloor A_9(n)\rfloor=\lfloor B_9(n)\rfloor
\qquad(9\le n\le173).
\]
Consequently,
\[
\left\lfloor\zeta_n(9)^{-1}\right\rfloor=\lfloor A_9(n)\rfloor
\qquad(n\ge9).
\]

For \(1\le n\le8\), the exact values are
\[
\begin{array}{c|rrrrrrrr}
n&1&2&3&4&5&6&7&8\\
\hline
\lfloor\zeta_n(9)^{-1}\rfloor&0&497&18093&224086&1543530&7360226&27295287&84349541.
\end{array}
\]
For \(n=1\), this follows from \(\zeta(9)>1\). For \(2\le n\le8\), the replay script uses exact rational partial sums through \(N=100\) and the integral tail bound
\[
\sum_{k=N+1}^{\infty}k^{-9}<\frac{1}{8N^8}
\]
to prove
\[
\frac1{M_n+1}<\zeta_n(9)<\frac1{M_n}.
\]

This proves the Zeta tail s9 reusable certificate, the Zeta tail floor gap template, and hence the Zeta tail floor next case.

_Proof source: `raw/student/20260527T233000-zeta-tail-template.md`._

## Tags

`attack-plan`, `floor-gap`, `modular-residue`, `proved`, `proved-s9`, `student`, `theorem`, `zeta-tail`
