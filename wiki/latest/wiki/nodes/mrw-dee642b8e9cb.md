---
id: mrw-dee642b8e9cb
type: theorem
title: Counterexample to complete monotonicity of higher-order polygamma product curvature
aliases: ["mrw-dee642b8e9cb", "Counterexample to complete monotonicity of higher-order polygamma product curvature"]
status: proved
tags: ["theorem", "proved", "polygamma", "complete-monotonicity", "counterexample", "non-tail"]
parents: [mrw-f0a031feea8e]
refs: []
---

# Theorem: Counterexample to complete monotonicity of higher-order polygamma product curvature

## Statement

Let
\[
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x),\qquad x>0.
\]
The assertion that \(P_n''\) is completely monotone on \((0,\infty)\) for every \(n\in\mathbb N\) is false. In fact, for every \(n\ge29\),
\[
P_n'''(2)>0,
\]
so \(P_n''\) cannot be completely monotone. In addition, the earlier counterexample
\[
P_7^{(6)}(3)<0.
\]
gives a lower-order obstruction to the same complete-monotonicity assertion.

## Proof

For \(m\ge1\), set
\[
A_m(x)=(-1)^{m+1}\psi^{(m)}(x)
=m!\sum_{k=0}^{\infty}(x+k)^{-m-1}.
\]
Then \(P_n(x)=A_n(x)A_n(1/x)\) and \(A_m'(x)=-A_{m+1}(x)\).  Direct differentiation gives
First prove the infinite counterfamily.  Put \(p=n+1\), and normalize by
\[
Q_p(x)=\frac{P_n(x)}{(n!)^2}
=\sum_{m,\ell\ge0}\left(\frac{x}{(x+m)(1+\ell x)}\right)^p.
\]
At \(x=2\), the constant term \((m,\ell)=(0,0)\) has zero derivatives, and the unique largest nonconstant base is \((m,\ell)=(1,0)\), namely \(2/3\).  Write
\[
Q_p(x)=1+\left(\frac{x}{x+1}\right)^p+R_p(x).
\]
For \(h(x)=x/(x+1)\), direct differentiation gives
\[
\left(h(x)^p\right)'''
=p\left(\frac{x}{x+1}\right)^p
\frac{p^2-6px-3p+6x^2+6x+2}{x^3(x+1)^3}.
\]
At \(x=2\),
\[
\left(h(x)^p\right)'''_{|x=2}
=\frac{p(p^2-15p+38)}{216}\left(\frac23\right)^p.
\]
For \(p\ge30\), this is at least
\[
\frac{p^3}{432}\left(\frac23\right)^p.
\]

For a general summand
\[
F_{m,\ell}(x)=\left(\frac{x}{(x+m)(1+\ell x)}\right)^p,
\]
write \(u_{m,\ell}=d(\log F_{m,\ell}^{1/p})/dx\).  At \(x=2\), one has
\[
|u_{m,\ell}|\le\frac12,\qquad |u_{m,\ell}'|\le\frac14,\qquad |u_{m,\ell}''|\le\frac14,
\]
and therefore \(|F_{m,\ell}'''(2)|\le p^3F_{m,\ell}(2)\) for \(p\ge2\).  The remaining mass satisfies
\[
\sum_{(m,\ell)\ne(0,0),(1,0)}F_{m,\ell}(2)<8\cdot2^{-p}.
\]
Indeed, the \(m\ge2,\ell=0\) mass is bounded by \(3\cdot2^{-p}\), the \(\ell\ge1\) mass by \(2\cdot2^{-p}\) times \(1+(2/3)^p+3\cdot2^{-p}\), and this is \(<8\cdot2^{-p}\) for \(p\ge3\).  Hence
\[
Q_p'''(2)\ge
p^3 2^{-p}\left[
\frac1{432}\left(\frac43\right)^p-8
\right].
\]
Since \((4/3)^{30}>432\cdot8\), it follows that \(Q_p'''(2)>0\) for \(p\ge30\).  Thus \(P_n'''(2)>0\) for every \(n\ge29\).  Complete monotonicity of \(P_n''\) would require \((P_n'')'=P_n'''\le0\), so \(P_n''\) is not completely monotone for \(n\ge29\).

For completeness, we also record the lower-order obstruction at \(n=7\).  Direct differentiation gives
\[
\begin{aligned}
P_n''(x)=&
A_{n+2}(x)A_n(1/x)
-\frac{2}{x^2}A_{n+1}(x)A_{n+1}(1/x)\\
&-\frac{2}{x^3}A_n(x)A_{n+1}(1/x)
+\frac{1}{x^4}A_n(x)A_{n+2}(1/x).
\end{aligned}
\]

Introduce the finite symbolic terms
\[
T_{p,i,j}(x)=x^{-p}A_i(x)A_j(1/x).
\]
The differentiation rule is
\[
\frac{d}{dx}T_{p,i,j}(x)
=-pT_{p+1,i,j}(x)-T_{p,i+1,j}(x)+T_{p+2,i,j+1}(x).
\]
Starting from the four-term formula for \(P_n''\), applying this rule four times with \(n=7\) gives an exact finite linear combination of \(22\) terms \(T_{p,i,j}(3)\).  The calculation is symbolic; no numerical differentiation is used.

It remains only to certify the sign.  For rational \(x>0\), the defining series for \(A_m(x)\) has rational terms.  For \(N\ge1\), monotone integral comparison gives the rational interval
\[
m!\left(\sum_{k=0}^{N-1}(x+k)^{-m-1}+\frac{(x+N)^{-m}}{m}\right)
\le A_m(x)
\]
and
\[
A_m(x)\le
m!\left(\sum_{k=0}^{N-1}(x+k)^{-m-1}+\frac{(x+N)^{-m}}{m}+(x+N)^{-m-1}\right).
\]
Using \(N=80\) for every \(A_m(3)\) and \(A_m(1/3)\) appearing in the exact \(22\)-term expression, and using interval arithmetic with the correct sign for each coefficient, gives
\[
-74998.154649422399828421756528409981771664439555587
<
P_7^{(6)}(3)
\]
and
\[
P_7^{(6)}(3)
<
-74997.331312439140215056900814096498575289999496021.
\]
In particular \(P_7^{(6)}(3)<0\).  Therefore \(P_7''\) is not completely monotone.  The complete-monotonicity strengthening in Open Problem 2 is consequently false in both an infinite high-order family and already at \(n=7\).

## Depends on

- [[wiki/nodes/mrw-f0a031feea8e|Higher-order monotonicity of polygamma products Pn]]

## Used by

## Notes

- This result does not refute the weaker convexity question for \(P_n\).  It refutes only the stronger assertion that \(P_n''\) is completely monotone for all \(n\ge1\).
- The high-order \(n\ge29\) obstruction and the \(n=7\) certificate were locally checked before inclusion.
- The elementary threshold inequalities for the high-order counterfamily are audited in `calculations/verify_high_order_pn_counterfamily.py`.
- The rational interval certificate is implemented in `calculations/certify_p7_complete_monotonicity_counterexample.py`.
