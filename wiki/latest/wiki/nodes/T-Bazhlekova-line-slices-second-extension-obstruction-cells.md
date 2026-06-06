---
id: "T-Bazhlekova-line-slices-second-extension-obstruction-cells"
type: "theorem"
title: "Bazhlekova line slices second extension obstruction cells Q5 Q7 Q9 Q13"
status: "proved"
tags: ["bazhlekova", "finite-certificate", "inner-gap", "line-split", "proved", "theorem"]
parents: ["T-Pointwise-obstruction-certificate-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260601T033000-bazhlekova-topcap-island-map-student.json", "oracle/responses/ORACLE-OS-20260601T033000-bazhlekova-topcap-island-map-oracle-response.md", "raw/student/20260601T033000-bazhlekova-topcap-island-map.md", "raw/student/20260601T033000-bazhlekova-topcap-island-map.py", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova line slices second extension obstruction cells Q5 Q7 Q9 Q13

## Statement

Exact rational interval arithmetic gives four additional Bazhlekova line-slice obstruction cells: on \(a=3/2\), \(Q_7(6)<0\) for \(b\in[2199/10000,2201/10000]\), \(Q_9(8)<0\) for \(b\in[28/125,113/500]\), and \(Q_{13}(13)<0\) for \(b\in[2349/10000,2351/10000]\); on \(a=11/10\), \(Q_5(1)<0\) for \(b\in[7/500,2/125]\). Each cell gives uniform small-\(x\) complete-monotonicity failure for all \(c,d>0\).

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260601T033000-bazhlekova-topcap-island-map-student.json`
- `oracle/responses/ORACLE-OS-20260601T033000-bazhlekova-topcap-island-map-oracle-response.md`
- `raw/student/20260601T033000-bazhlekova-topcap-island-map.md`
- `raw/student/20260601T033000-bazhlekova-topcap-island-map.py`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

Use the normalized form
\[
h(s)=s^\beta(1+s^p)^{1/2},\qquad
\beta=\frac b2,\qquad p=a-b,\qquad \alpha=\frac a2=\beta+\frac p2 .
\]
Equivalently, with \(y=s^p\),
\[
h(s)=s^\alpha(1+y^{-1})^{1/2}
=\sum_{j\ge0}\binom{1/2}{j}s^{\alpha-pj}.
\]
The derivative expansion gives
\[
h^{(n)}(s)
=s^{\beta-n}(1+y)^{1/2-n}Q_n(y),
\]
and hence, for the signed polynomial \(R_n(y)=(-1)^{n-1}Q_n(y)\), fixed top-depth coefficients are controlled by
\[
[y^{n-\ell}]Q_n(y)
=
\sum_{j=0}^{\ell}
\binom{1/2}{j}
(\alpha-pj)_{\underline n}
\binom{n-\frac12}{\ell-j}.
\]
For fixed \(\ell\ge1\), the \(j=\ell\) summand dominates the lower \(j\)-terms by powers of \(n^{p-1}\), because \(p>1\). After multiplying by the signing factor in \(R_n\), the eventual sign is
\[
\operatorname{sgn}[y^{n-\ell}]R_n(y)=(-1)^\ell .
\]
Thus every fixed odd top depth eventually becomes negative. This explains the earlier \(R_{4482}\) coefficient break and permanently rules out any future attempt to repair the single-negative-coefficient induction.

This theorem does not decide whether \(R_n(y)>0\) on \(y>0\). It only describes a fixed-depth top cap of the coefficient vector.

the Bazhlekova no cover seeds top cap Wright dichotomy remains open, but the fixed top-cap coefficient asymptotic is true local progress.

The same expansion gives the formal pointwise limit, for \(y=n^p\lambda\),
\[
W_{\alpha,p}(\lambda)
=
1-
\frac{\Gamma(1-\alpha)}{\alpha}
\sum_{j\ge1}
\binom{1/2}{j}
\frac{\lambda^{-j}}{\Gamma(pj-\alpha)} .
\]
The script ran a high-precision numerical scan only on a stable compact log-grid. It found positive numerical minima:
\[
(a,b)=\left(\frac32,\frac25\right):
\quad W_{\alpha,p}(\lambda)\gtrsim 0.5468,
\]
near \(\lambda\approx0.8353\), and
\[
(a,b)=\left(\frac{11}{10},\frac1{20}\right):
\quad W_{\alpha,p}(\lambda)\gtrsim0.0988,
\]
near \(\lambda\approx0.2952\).

This is evidence only. No positivity theorem for \(W_{\alpha,p}\), no uniform tail bound, and no transfer theorem back to large finite \(n\) was proved.

The line-map extension branch produced four additional exact rational obstruction cells beyond the previously admitted cells.

For \(a=3/2\):
\[
b\in\left[\frac{2199}{10000},\frac{2201}{10000}\right],
\qquad Q_7(6)<0,
\]
\[
b\in\left[\frac{28}{125},\frac{113}{500}\right],
\qquad Q_9(8)<0,
\]
and
\[
b\in\left[\frac{2349}{10000},\frac{2351}{10000}\right],
\qquad Q_{13}(13)<0.
\]
For \(a=11/10\):
\[
b\in\left[\frac7{500},\frac2{125}\right],
\qquad Q_5(1)<0.
\]
Each is certified by exact rational interval arithmetic. Since the orders are odd, \(R_n=Q_n\), and the admitted odd-derivative small-\(x\) criterion converts each cell into uniform \(w_t\)-positivity failure for all \(c,d>0\) in the cell.

the Bazhlekova line slices certified extension map beyond current cells remains open as a full map problem, with true partial progress.

The normalized derivative is
\[
h'(s)
=
s^{\beta-1}(1+s^p)^{-1/2}\left(\beta+\alpha s^p\right).
\]
Thus the plain Bernstein side of the island is exactly the complete monotonicity of this derivative. If \(h'\) is not completely monotone, then some derivative sign fails for \(h\), and the leading small-\(x\) term in \(e^{-x h(s)}\) gives a finite-\(x\) complete-monotonicity obstruction.

No inverse-Laplace density sign theorem and no finite-\(x\) obstruction was proved here.

the Bazhlekova no cover seeds inverse laplace density dichotomy remains candidate_open.

Fixed top-cap coefficient theorem: for every fixed \(\ell\ge1\), \([y^{n-\ell}]R_n\) has eventual sign \((-1)^\ell\) when \(p=a-b>1\).
Four additional certified rational obstruction cells on the \(a=3/2\) and \(a=11/10\) line slices.
Plain BF/density reduction to complete monotonicity of \(h'\).

_Proof source: `raw/student/20260601T033000-bazhlekova-topcap-island-map.md`._

## Tags

`bazhlekova`, `finite-certificate`, `inner-gap`, `line-split`, `proved`, `theorem`
