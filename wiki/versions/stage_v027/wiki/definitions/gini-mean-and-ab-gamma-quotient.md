# Gini Mean And Alzer--Berg Gamma Quotient

For \(a,b\in\mathbb R\), the two-variable Gini mean is
\[
G_{a,b}(u,v)=
\left(\frac{u^a+v^a}{u^b+v^b}\right)^{1/(a-b)}
\qquad (a\ne b),
\]
with the diagonal parameter case \(a=b\) defined by continuity:
\[
G_{a,a}(u,v)
=\exp\left(
\frac{u^a\log u+v^a\log v}{u^a+v^a}
\right).
\]

Alzer--Berg define
\[
P_{a,b}(u,v;x)
=\frac{\Gamma(x+u)}{\Gamma(x+v)}
\exp\{(v-u)\psi(x+G_{a,b}(u,v))\},
\]
for \(v>u>0\). They determine the parameters for complete monotonicity of \(P_{a,b}\) and leave the reciprocal complete-monotonicity problem for \(1/P_{a,b}\) open.
