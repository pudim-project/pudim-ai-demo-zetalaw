# Qi \(h_\lambda\) Completely-Monotonic Degree Frontier

## Source

Feng Qi, "Completely monotonic degree of a function involving trigamma and tetragamma functions", AIMS Mathematics 5(4), 3391-3407, 2020, DOI 10.3934/math.2020219.

The source defines
\[
\Psi(x)=[\psi'(x)]^2+\psi''(x),
\qquad
h_\lambda(x)=\Psi(x)-\frac{x^2+\lambda x+12}{12x^4(x+1)^2}.
\]
Remark 7.4 conjectures that
\[
\deg_x^{\rm cm}h_\lambda=\deg_x^{\rm cm}(-h_\mu)=4
\quad\Longleftrightarrow\quad
\lambda\le0,\ \mu\ge4.
\]

## Local Result

The conjecture is false. The degree-four transforms fail the first derivative sign test near \(0^+\):
\[
x^4h_\lambda(x)=-\frac{\lambda}{12}x+O(x^2)\quad(\lambda<0),
\]
\[
x^4h_0(x)=\left(\frac{\pi^2}{3}-\frac{37}{12}\right)x^2+O(x^3),
\]
and
\[
x^4(-h_\mu(x))=\frac{\mu}{12}x+O(x^2)\quad(\mu\ge4).
\]
Each corresponding derivative is positive for all sufficiently small \(x>0\), so none of these degree-four transforms is completely monotone.

## Theory Integration

Admitted true node:
\[
T\text{-Qi-hlambda-x4-source-range-not-CM}.
\]

Admitted true negation:
\[
T\text{-not-Qi-hlambda-degree4-conjecture}.
\]

Residual open frontier:
\[
T\text{-Qi-hlambda-exact-degree-frontier-open}.
\]

This is a refutation of a source-open conjecture and a local application candidate. It is not yet publicly staged.
