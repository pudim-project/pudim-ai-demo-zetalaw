# Frontier: Alzer--Berg Reciprocal Gini Gamma Quotient

Scout forage `FI-20260530T-elegance-029` selected the Alzer--Berg reciprocal \(P_{a,b}\) problem as a source-open, domain-fit frontier. The source defines the Gini mean \(G_{a,b}\), the quotient \(P_{a,b}\), proves the direct complete-monotonicity region for \(P_{a,b}\), and states that the reciprocal problem remains open.

Student proved a bounded diagonal obstruction. If
\[
Q_{a,b}(u,v;x)=\frac1{P_{a,b}(u,v;x)}
\]
is completely monotone in \(x\) for every \(v>u>0\), then
\[
a+b\le\frac13.
\]

The proof uses the diagonal expansion
\[
G_{a,b}(u,u+h)=u+\frac h2+\frac{a+b-1}{8u}h^2+O(h^3)
\]
and the corresponding log-expansion
\[
\log Q_{a,b}(u,u+h;x)
=h^3\left(
\frac{\psi''(y)}{24}
-\frac{a+b-1}{8u}\psi'(y)
\right)+O(h^4),
\qquad y=x+u.
\]
Complete monotonicity forces \(Q\ge1\), hence the leading coefficient is nonnegative. Letting \(u\uparrow y\) and then \(y\downarrow0\) gives the gate \(a+b\le1/3\).

This is not the full parameter classification, but it is a clean necessary condition and a reusable diagonal-test normal form for reciprocal Gamma-quotient frontiers.

## LCM Route Demotion

The next bounded Student pass tested the overstrong logarithmic-complete-monotonicity route. For
\[
Q_{a,b}(u,v;x)=1/P_{a,b}(u,v;x),
\qquad d=v-u,
\qquad G=G_{a,b}(u,v),
\]
one has
\[
-\partial_x\log Q_{a,b}(u,v;x)
=
\int_0^\infty e^{-xt}
\frac{d\,t e^{-Gt}-(e^{-ut}-e^{-vt})}{1-e^{-t}}\,dt.
\]
If \(u<G<v\), then the numerator is eventually negative after multiplying by \(e^{ut}\):
\[
d\,t e^{-(G-u)t}-1+e^{-(v-u)t}\to -1.
\]
So this natural positive log-kernel route cannot prove LCM. For the geometric slice \(a=b=0\), the kernel is positive near \(0\) but negative in the tail, hence sign-changing. This is only a route demotion; it does not show that \(Q_{a,b}\) is not completely monotone.
