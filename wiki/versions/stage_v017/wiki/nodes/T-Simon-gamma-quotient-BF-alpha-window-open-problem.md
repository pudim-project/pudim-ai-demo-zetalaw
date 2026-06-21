---
id: "T-Simon-gamma-quotient-BF-alpha-window-open-problem"
type: "theorem"
title: "Simon gamma quotient is Bernstein for alpha in (0,1)"
status: "proved"
tags: ["bernstein", "gamma-quotient", "proved", "simon", "source-open-solved", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "T-Simon-gamma-quotient-complete-Bernstein-strengthening", "T-Simon-gamma-quotient-derivative-positive-laplace-density", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private attack plan", "private librarian audit", "private librarian audit", "private Oracle response", "private Oracle response", "private scout artifact", "private proof note", "private proof note", "wiki/notes/frontier-simon-gamma-quotient-bernstein.md"]
---

# Theorem: Simon gamma quotient is Bernstein for alpha in (0,1)

## Statement

For every \(0<\alpha<1\), the function \(F_\alpha(x)=\Gamma(x+\alpha)/(\Gamma(x)x^\alpha)\) is a Bernstein function on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/T-Simon-gamma-quotient-complete-Bernstein-strengthening|Simon gamma quotient is CBF for alpha in (0,1)]]
- [[wiki/nodes/T-Simon-gamma-quotient-derivative-positive-laplace-density|Simon gamma quotient derivative is CM with positive Laplace density]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private librarian audit`
- `private Oracle response`
- `private Oracle response`
- `private scout artifact`
- `private proof note`
- `private proof note`
- `wiki/notes/frontier-simon-gamma-quotient-bernstein.md`

## Proof

For \(\alpha,\beta>0\), \(s,t\ge0\), and \(x>0\), the beta identity gives
\[
(x+s)^{-\alpha}(x+t)^{-\beta}
=
\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}
\int_0^1
\frac{u^{\alpha-1}(1-u)^{\beta-1}}
{\bigl(x+us+(1-u)t\bigr)^{\alpha+\beta}}
\,du.
\]

If
\[
f(x)=\int_{[0,\infty)}(x+s)^{-\alpha}\,d\mu(s),
\qquad
g(x)=\int_{[0,\infty)}(x+t)^{-\beta}\,d\nu(t),
\]
then Tonelli gives
\[
f(x)g(x)=\int_{[0,\infty)}(x+r)^{-(\alpha+\beta)}\,d\kappa(r),
\]
where \(\kappa\) is the positive pushforward measure defined by
\[
\int \varphi(r)\,d\kappa(r)
=
\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}
\int\!\!\int\!\!\int_0^1
\varphi\bigl(us+(1-u)t\bigr)
u^{\alpha-1}(1-u)^{\beta-1}
\,du\,d\mu(s)\,d\nu(t).
\]

Thus pure generalized Stieltjes transforms satisfy
\[
\mathcal S_\alpha^{0}\mathcal S_\beta^{0}\subseteq \mathcal S_{\alpha+\beta}^{0}.
\]
With the usual nonnegative constant term convention, constants and lower-order terms require the standard order-lift convention already recorded in the source vocabulary; no application should rely on constants being absorbed unless that convention is explicitly cited.

For \(0<\alpha<1\), set
\[
F_\alpha(x)=\frac{\Gamma(x+\alpha)}{\Gamma(x)x^\alpha},
\qquad
L_\alpha(x)=\log F_\alpha(x).
\]
Then
\[
L_\alpha'(x)
=
\psi(x+\alpha)-\psi(x)-\frac{\alpha}{x}
=
\int_0^\infty e^{-xt}
\left(
\frac{1-e^{-\alpha t}}{1-e^{-t}}-\alpha
\right)\,dt.
\]
The kernel is positive for \(t>0\), because \(u\mapsto 1-e^{-ut}\) is strictly concave on \([0,1]\), hence
\[
1-e^{-\alpha t}>\alpha(1-e^{-t}).
\]
Therefore \(L_\alpha'\) is completely monotone, and \(1/F_\alpha\) is logarithmically completely monotone.

This does not prove that \(F_\alpha\) is a Bernstein function. Simon's source explicitly states that the Bernstein character of the corresponding \(\Phi(\lambda)=\Gamma(1-t+\lambda)/(\lambda^{1-t}\Gamma(\lambda))\) is a puzzling question, and also says the reciprocal LCM property is necessary but not sufficient.

_Proof source: `private proof note`._

## Tags

`bernstein`, `gamma-quotient`, `proved`, `simon`, `source-open-solved`, `theorem`
