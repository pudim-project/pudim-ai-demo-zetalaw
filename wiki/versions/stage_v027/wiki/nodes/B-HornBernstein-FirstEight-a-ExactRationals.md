---
id: "B-HornBernstein-FirstEight-a-ExactRationals"
type: "lemma"
title: "Horn-Bernstein first eight exact values"
status: "proved"
tags: ["bridge-lemma", "exact-rational-certificate", "finite-certificate", "hausdorff-moment", "horn-bernstein", "lemma", "moment-sequence", "proved", "true"]
parents: ["T-Exact-finite-certificate-verification-principle", "O-BergPedersen-HornBernstein-Hausdorff-source-gate"]
refs: ["librarian/audits/LA-20260622T0430-hornbernstein-strict-app.json", "oracle/responses/OS-20260622T042303Z-oracle-response.md", "raw/student/20260622T0428-hornbernstein-seventh-difference.md"]
---

# Lemma: Horn-Bernstein first eight exact values

## Statement

For the Berg--Pedersen Horn-Bernstein recurrence, the derived sequence \(a_0=1\), \(a_n=1/t_n-1/t_{n-1}\) has first values \(1,1/2,3/10,72/335,4185/24857,75492/543515,36295938/306303665,1860116400/17972811841\).

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]
- [[wiki/nodes/O-BergPedersen-HornBernstein-Hausdorff-source-gate|Berg-Pedersen Horn-Bernstein Hausdorff moment source gate]]

## Proof and provenance references

- `librarian/audits/LA-20260622T0430-hornbernstein-strict-app.json`
- `oracle/responses/OS-20260622T042303Z-oracle-response.md`
- `raw/student/20260622T0428-hornbernstein-seventh-difference.md`

## Proof

The proof below uses the source recurrence and exact rational arithmetic

appendix code,
\[
\rho_0=1,\qquad
\rho_n=\sum_{k=0}^{n-1}\rho_k
\frac{2(-1)^{n-1-k}}{(n-k+1)(n-k+2)},\qquad n\ge1,
\]
\[
s_n=1+2\sum_{k=1}^n(-1)^k\rho_k,\qquad
t_n=\sum_{k=0}^n(-1)^k\binom nk s_k.
\]
Exact rational arithmetic gives
\[
\begin{array}{c|c|c}
n&t_n&a_n\\
\hline
0&1&1\\
1&2/3&1/2\\
2&5/9&3/10\\
3&67/135&72/335\\
4&371/810&4185/24857\\
5&1465/3402&75492/543515\\
6&209081/510300&36295938/306303665\\
7&85961/218700&1860116400/17972811841
\end{array}
\]

The local replay computed the same table from the recurrence:

\begin{verbatim}
rho= ['1', '1/3', '-1/18', '7/270', '-5/324', '353/34020', '-7669/1020600', '17519/3061800']
s= ['1', '1/3', '2/9', '23/135', '113/810', '202/1701', '52931/510300', '10091/109350']
t= ['1', '2/3', '5/9', '67/135', '371/810', '1465/3402', '209081/510300', '85961/218700']
a= ['1', '1/2', '3/10', '72/335', '4185/24857', '75492/543515', '36295938/306303665', '1860116400/17972811841']
H7= -28629387882812/1395498975394445
target_match= True
\end{verbatim}

If \(a_n=\int_0^1 x^n\,d\mu(x)\) for a positive measure \(\mu\), then for
all \(m,n\ge0\)
\[
H_m(n):=\sum_{j=0}^m(-1)^j\binom mj a_{n+j}
=\int_0^1 x^n(1-x)^m\,d\mu(x)\ge0.
\]
Equivalently, \(H_m(n)=(-1)^m\Delta^m a_n\) for
\(\Delta a_n=a_{n+1}-a_n\).

For the Berg--Pedersen sequence,
\[
\begin{aligned}
H_7(0)
&=a_0-7a_1+21a_2-35a_3+35a_4-21a_5+7a_6-a_7\\
&=-\frac{28629387882812}{1395498975394445}<0.
\end{aligned}
\]
This single finite Hausdorff-difference violation proves that \((a_n)\) is
not a Hausdorff moment sequence, giving a negative answer to the exact source
question.

This is an exact finite obstruction. It does not decide any question about
\((t_n^c)\) other than invalidating the source's proposed route through
Hausdorffness of \((a_n)\).

_Proof source: `raw/student/20260622T0428-hornbernstein-seventh-difference.md`._

## Tags

`bridge-lemma`, `exact-rational-certificate`, `finite-certificate`, `hausdorff-moment`, `horn-bernstein`, `lemma`, `moment-sequence`, `proved`, `true`
