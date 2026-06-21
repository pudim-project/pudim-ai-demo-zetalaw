---
id: "T-Logconcave-GCM-nu39-explicit-logconcave-candidate"
type: "theorem"
title: "Gu Sellke heat shifted atomic measure nu39 is explicit log concave candidate"
status: "proved"
tags: ["explicit-candidate", "gcm", "heat-flow", "log-concave", "not-application", "proved", "theorem"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["private librarian audit", "private Oracle response", "private Oracle audit", "private proof note", "wiki/notes/frontier-gcm-counterexample.md"]
---

# Theorem: Gu Sellke heat shifted atomic measure nu39 is explicit log concave candidate

## Statement

For the Gu--Sellke atomic measure mu_0 with mass 2/1000 at 0 and masses c_j/1000 at +/- (9/5+j), c=(34,93,134,123,75,31,8,1), the heat-regularized measure nu_39=mu_0*gamma_78 has a log-concave density.

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private Oracle audit`
- `private proof note`
- `wiki/notes/frontier-gcm-counterexample.md`

## Proof

Let
\[
\mu_0
=
\frac{2}{1000}\delta_0
+
\sum_{j=0}^{7}\frac{c_j}{1000}
\left(\delta_{9/5+j}+\delta_{-(9/5+j)}\right),
\qquad
c=(34,93,134,123,75,31,8,1).
\]
All atoms lie in \([-44/5,44/5]\).

For the heat convention
\[
g_t(x)=\sum_i w_i(4\pi t)^{-1/2}
\exp\left(-\frac{(x-a_i)^2}{4t}\right),
\]
define
\[
\nu_{39}:=\mu_0*\gamma_{78}.
\]

For \(A\sim\mu_0\), the posterior-variance identity gives
\[
(\log g_S)''(x)
=
-\frac1{2S}
+\frac{\operatorname{Var}(A\mid x)}{4S^2}.
\]
Since \(\operatorname{Var}(A\mid x)\le (44/5)^2\), \(g_S\) is log-concave whenever
\[
S\ge \frac{(44/5)^2}{2}=\frac{968}{25}.
\]
Thus \(S=39\) is a strict explicit choice and \(\nu_{39}\) has a log-concave density.

This proves the Logconcave GCM nu39 explicit logconcave candidate.

For \(\nu_{39}\),
\[
H_{\nu_{39}}^{(m)}(t)=H_{\mu_0}^{(m)}(39+t).
\]
Therefore an explicit log-concave sign failure can be certified by evaluating
\[
(-1)^mH_{\mu_0}^{(m)}(39+t)
\]
for \(m\ge6\) and \(t>0\).

The Gu--Sellke finite-mixture derivative recursion applies unchanged. Let
\[
K_n=\frac{\partial_t^n g_t}{g_t},
\qquad
L_n=\partial_t^n\log g_t.
\]
Then
\[
L_n
=
K_n-\sum_{r=1}^{n-1}\binom{n-1}{r-1}L_rK_{n-r},
\]
and
\[
H^{(m)}(t)
=
\int_{\mathbb R}
g_t(x)
\sum_{r=0}^{m}\binom{m}{r}K_r(x,t)L_{m-r}(x,t)\,dx.
\]
On any bounded rectangle \(6\le m\le M\), \(0\le t\le T\), finite \(x\)-block interval integration plus a Gaussian tail bound gives an auditable certificate route.

This proves the Logconcave GCM explicit order finite search reduction.

A non-rigorous Gauss--Hermite search was run for \(\nu_{39}\) by evaluating the signs of
\[
(-1)^mH_{\mu_0}^{(m)}(T)
\]
at sampled \(T=39+t\). A coarse scan through \(m=30\) found no negative sign. A higher-order double-precision scan showed possible negative values near \(m=76,\ldots,80\), but the signs changed when the Gauss--Hermite order was varied. This is numerical instability, not a certificate.

No explicit \((m,t_0)\) witness is admitted.

_Proof source: `private proof note`._

## Tags

`explicit-candidate`, `gcm`, `heat-flow`, `log-concave`, `not-application`, `proved`, `theorem`
