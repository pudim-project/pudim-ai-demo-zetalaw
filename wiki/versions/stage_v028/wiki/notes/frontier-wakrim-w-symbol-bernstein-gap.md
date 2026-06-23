# Frontier: Wakrim W-Symbol Bernstein Gap

## Source Status

Mohamed Wakrim's arXiv preprint "The W-Operator: A Volterra Fractional Time Operator with Non-Bernstein Symbol" introduces
\[
\Phi_{\alpha,\beta}(s)
=s^\alpha\left(1+(1-\alpha)s^{\alpha-1}\right)^{-\beta},
\qquad 0<\alpha<1,\quad \beta\ge0.
\]
The source proves that the standard Bernstein product mechanism does not apply for \(\beta>0\), proves non-Bernstein behavior for \(\beta>1\), and explicitly leaves the Bernstein status for \(0<\beta\le1\) open.

Primary source: https://arxiv.org/abs/2601.02876

## Local Resolution

For \(a=1-\alpha\), the local proof rewrites
\[
\Phi_{\alpha,\beta}(s)
=\frac{s^{1-a+a\beta}}{(s^a+a)^\beta}
\]
and factors the derivative as follows.  Put
\[
p=1-a+a\beta=\alpha+a\beta.
\]
Differentiation gives
\[
\begin{aligned}
\Phi_{\alpha,\beta}'(s)
&=s^{p-1}(s^a+a)^{-\beta-1}
  \{p(s^a+a)-\beta a s^a\} \\
&=s^{p-1}(s^a+a)^{-\beta-1}
  \{\alpha s^a+\alpha a+a^2\beta\} \\
&=s^{p-1}(s^a+a)^{-\beta}
  \left(\alpha+\frac{a^2\beta}{s^a+a}\right).
\end{aligned}
\]
Since \(p-1=a(\beta-1)\), writing \(y=s^a\) gives
\[
\Phi_{\alpha,\beta}'(s)=H(s^a),
\]
where
\[
H(y)=
y^{\beta-1}(y+a)^{-\beta}
\left(\alpha+\frac{a^2\beta}{y+a}\right).
\]

For \(0\le\beta\le1\), each factor is completely monotone with the following explicit interpretation:

- \(y^{\beta-1}=y^{-(1-\beta)}\), and \(1-\beta\ge0\).
- \((y+a)^{-\beta}\) is completely monotone for \(\beta>0\) by
  \[
  (y+a)^{-\beta}
  =
  \frac{1}{\Gamma(\beta)}
  \int_0^\infty e^{-yt}e^{-at}t^{\beta-1}\,dt,
  \]
  while for \(\beta=0\) it is the constant \(1\).
- \(\alpha+a^2\beta/(y+a)\) is a positive constant plus a nonnegative multiple of the completely monotone resolvent \((y+a)^{-1}\).

Products and nonnegative sums preserve complete monotonicity, so \(H\) is completely monotone.  The boundary \(\beta=1\) is explicit:
\[
H(y)=\frac{\alpha}{y+a}+\frac{a^2}{(y+a)^2},
\]
so no limiting argument is needed.  The boundary \(\beta=0\) is also direct because \(\Phi_{\alpha,0}(s)=s^\alpha\).

The standard composition theorem for Bernstein functions says that if \(f\) is completely monotone and \(g\) is a Bernstein function mapping \((0,\infty)\) into itself, then \(f\circ g\) is completely monotone.  Let \(g(s)=s^a\).  Since \(g\) is Bernstein for \(0<a<1\), \(\Phi_{\alpha,\beta}'=H\circ g\) is completely monotone. Thus \(\Phi_{\alpha,\beta}\) is Bernstein for \(0\le\beta\le1\).

Combining with the source's \(\beta>1\) obstruction gives the exact range:
\[
\Phi_{\alpha,\beta}\in BF
\quad\Longleftrightarrow\quad
0\le\beta\le1.
\]

## Author-Feedback Expansion

After author feedback on APP-0019, the next public staging must not compress this proof into a one-line closure claim.  The public theorem should display the derivative calculation, the complete-monotonicity interpretation of \(y^{\beta-1}\), the Laplace representation for \((y+a)^{-\beta}\), the Bernstein-composition theorem, and the \(\beta=1\) boundary case explicitly.

## Theory Impact

This adds a compact fractional-symbol theorem and makes the \(CM\circ BF\) closure lemma explicit in the local Theory. It is source-open and solved locally.  Public staging should preserve the detailed proof expansion above.
