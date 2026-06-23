---
id: "T-BCG-ExpTransitionPowerBF-finite-signed-moment-recurrence"
type: "lemma"
title: "BCG finite signed-moment recurrence"
status: "proved"
tags: ["beghin-cristofaro-garrappa", "bernstein-function", "coefficient-extraction", "finite-witness", "lemma", "not-app", "proved", "recurrence", "signed-moment"]
parents: ["O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["oracle/responses/OS-20260611T1825Z-bcg-finite-witness-expansion-oracle-response.md", "raw/oracle/RO-OS-20260611T1825Z-bcg-finite-witness-expansion.json", "raw/student/20260611T1835-bcg-finite-signed-moment-recurrence.md"]
---

# Lemma: BCG finite signed-moment recurrence

## Statement

Let x>0, c>0, and alpha1,alpha2 be real. For F(t)=t^((alpha2*c+alpha1*t)/(c+t)), set r=x/(x+c), gamma=c*(alpha2-alpha1)/(x+c), ell=log(x), A_k(r)=sum_{j=1}^k r^(k-j)/j, and b_k=alpha1/k+gamma*(A_k(r)-ell*r^k). Define P_0=1 and m*P_m=-sum_{k=1}^m k*b_k*P_{m-k}. Then P_m=(-1)^m*x^m*F^(m)(x)/(m!*F(x)). In particular, if m>=1 and P_m>0, then F is not a Bernstein function.

## Dependencies

- [[wiki/nodes/O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold|Beghin-Cristofaro-Garrappa exponential-transition power Bernstein threshold]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `oracle/responses/OS-20260611T1825Z-bcg-finite-witness-expansion-oracle-response.md`
- `raw/oracle/RO-OS-20260611T1825Z-bcg-finite-witness-expansion.json`
- `raw/student/20260611T1835-bcg-finite-signed-moment-recurrence.md`

## Proof

Let
\[
H(z)=\frac{F(x(1+z))}{F(x)}
\]
for \(|z|\) small. Since \(F\) is real analytic near \(x>0\),
\[
H(z)=\sum_{m\ge0}\frac{x^mF^{(m)}(x)}{m!\,F(x)}z^m.
\]
Write
\[
W_m=\frac{x^mF^{(m)}(x)}{m!\,F(x)}.
\]
Then \(H(z)=\sum_{m\ge0}W_mz^m\).

The logarithm of \(F\) has the useful form
\[
\log F(t)=\alpha_1\log t+\frac{c(\alpha_2-\alpha_1)\log t}{t+c}.
\]
Therefore
\[
\log H(z)=
\alpha_1\log(1+z)+
\gamma\left(\frac{\ell+\log(1+z)}{1+rz}-\ell\right).
\]
Let
\[
\log H(z)=\sum_{k\ge1}g_kz^k.
\]
For \(k\ge1\), the coefficient of \(\log(1+z)/(1+rz)\) is
\[
(-1)^{k+1}\sum_{j=1}^k\frac{r^{k-j}}{j}
=(-1)^{k+1}A_k(r),
\]
and the coefficient of \(\ell((1+rz)^{-1}-1)\) is
\[
(-1)^k\ell r^k=(-1)^{k+1}(-\ell r^k).
\]
Thus
\[
g_k=(-1)^{k+1}
\left[
\frac{\alpha_1}{k}+\gamma\left(A_k(r)-\ell r^k\right)
\right]
=(-1)^{k+1}b_k.
\]

Since \(H=\exp(\sum_{k\ge1}g_kz^k)\), differentiating gives
\[
H'(z)=\left(\sum_{k\ge1}kg_kz^{k-1}\right)H(z).
\]
Comparing the coefficient of \(z^{m-1}\) gives
\[
mW_m=\sum_{k=1}^m kg_kW_{m-k}.
\]
Set \(P_m=(-1)^mW_m\). Substituting \(g_k=(-1)^{k+1}b_k\) into the last recurrence yields
\[
mP_m=-\sum_{k=1}^m k\,b_k\,P_{m-k}.
\]
This proves the recurrence and the identity
\[
P_m=(-1)^mW_m=(-1)^m\frac{x^mF^{(m)}(x)}{m!\,F(x)}.
\]

If \(F\) were a Bernstein function, then \(F'\) would be completely monotone. Hence, for every \(m\ge1\),
\[
(-1)^{m-1}F^{(m)}(x)\ge0.
\]
Because \(x^m/(m!F(x))>0\), this is equivalent to
\[
(-1)^{m-1}W_m\ge0.
\]
Since \(P_m=(-1)^mW_m\), the Bernstein sign condition is \(P_m\le0\). Therefore \(P_m>0\) is a finite signed-moment obstruction to Bernsteinness.

Using the recurrence with standard-library decimal arithmetic on the fixed line \((\alpha_1,c)=(3/10,2)\):

\(P_{37}(10;0.3,0.9,2)>0\).
\(P_{37}(10;0.3,0.76,2)>0\).
\(P_{107}(30;0.3,0.75,2)>0\).
\(P_{107}(30;0.3,0.759,2)>0\).

These signs match the admitted witnesses in the corresponding result: for odd \(m\), \(P_m>0\) is the same as \(W_m<0\).

This theorem does not classify the full BCG Bernstein region. It also does not imply that the BCG relaxation solution is negative or increasing. It only gives a finite, auditable way to prove that \(F\) is not a Bernstein function at a parameter point or on a parameter box once \(P_m>0\) is certified there.

_Proof source: `raw/student/20260611T1835-bcg-finite-signed-moment-recurrence.md`._

## Do not claim

- Do not claim the full BCG Bernstein threshold is solved.
- Do not claim APP status.
- Do not claim relaxation nonnegativity or monotonicity failure from this Bernstein obstruction alone.
- Do not treat a positive P_m at one witness as a parameter-region classification without a separate interval certificate.

## Tags

`beghin-cristofaro-garrappa`, `bernstein-function`, `coefficient-extraction`, `finite-witness`, `lemma`, `not-app`, `proved`, `recurrence`, `signed-moment`
