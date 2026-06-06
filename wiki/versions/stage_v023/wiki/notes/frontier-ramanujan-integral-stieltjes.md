# Frontier: Ramanujan Integral Stieltjes Behavior

Scout forage `FI-20260530T-elegance-032` selected Mishra--Swaminathan's Ramanujan integral source.

The source defines
\[
I_R(x)=\int_0^\infty e^{-xt}\frac{dt}{t(\pi^2+\log^2 t)},\qquad x>0.
\]
It proves complete monotonicity and studies strong complete monotonicity. For \(n=0\), the source records that a precise Stieltjes conclusion was not available. It also remarks that it remains open whether the antiderivative of \(I_R\) is complete Bernstein.

The local proof uses the identity
\[
\frac{1}{t(\pi^2+\log^2t)}
=\frac{1}{\pi(1+t)}\int_0^1 t^{-a}\sin(\pi a)\,da.
\]
The factors \(t^{-a}\) and \((1+t)^{-1}\) are completely monotone, and the mixture weight is positive. Hence the density is completely monotone. The Laplace transform of a completely monotone density is Stieltjes, so \(I_R\) is Stieltjes. The same density criterion proves that the source's Bernstein antiderivative is complete Bernstein.

The final Turan-window problem for
\[
H_n(x;\alpha)
=\left(I_R^{(n)}(x)\right)^2-\alpha I_R^{(n-1)}(x)I_R^{(n+1)}(x)
\]
in the interval
\[
\frac{n-2}{n-1}<\alpha<\frac{n-1}{n}
\]
remains open.
