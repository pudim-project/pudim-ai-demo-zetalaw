# Frontier: Yin \(p,k\)-Digamma Alpha Necessity

Source: Li Yin, "Complete monotonicity of a function involving the \((p,k)\)-digamma function", International Journal of Open Problems in Computer Mathematics 11(2), 2018, 103-108.

Source note: `private scout artifact`

## Source Problem

For \(p\in\mathbb N\), \(k>0\), define
\[
B_{p,k}(x)=
\frac1k\log\frac{pkx}{x+k(p+1)}-\psi_{p,k}(x),
\qquad
\delta_{p,k,\alpha}(x)=x^\alpha B_{p,k}(x).
\]

Yin proves that \(\delta_{p,k,\alpha}\) is completely monotone for \(\alpha\le1\), and asks whether complete monotonicity forces \(\alpha\le1\).

## Attack Handle

Using the finite \((p,k)\)-digamma representation,
\[
B_{p,k}(x)=
\frac1k\log\frac{x}{x+k(p+1)}
+\sum_{n=0}^p\frac1{x+nk}.
\]

The \(n=0\) term dominates at \(0^+\), while the logarithmic term is lower order:
\[
B_{p,k}(x)=\frac1x+O(|\log x|).
\]

Thus \(\delta_{p,k,\alpha}(x)\sim x^{\alpha-1}\). Complete monotonicity gives a positive nonincreasing function. If \(\alpha>1\), the endpoint limit would be \(0\), impossible for a positive nonincreasing function on \((0,\infty)\).

## Status

Solved by `private proof note` and audited in `private librarian audit`.

The local result proves the necessity half asked in Yin's Open Problem 4.1:
\[
\delta_{p,k,\alpha}\text{ completely monotone on }(0,\infty)
\quad\Longrightarrow\quad
\alpha\le1.
\]

Together with Yin's already proved sufficiency for \(\alpha\le1\), this closes the sharp exponent threshold for this \((p,k)\)-digamma family.
