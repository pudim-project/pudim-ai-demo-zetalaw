# Frontier Note: Ramanujan Integral Turan Window Refutation

Mishra--Swaminathan ask whether
\[
H_n(x;\alpha)
=
\bigl(I_R^{(n)}(x)\bigr)^2
-\alpha I_R^{(n-1)}(x)I_R^{(n+1)}(x)
\]
is completely monotone for \(n\ge2\) and
\[
\frac{n-2}{n-1}<\alpha<\frac{n-1}{n}.
\]

Local answer: negative. Put
\[
A_k(x)=(-1)^k I_R^{(k)}(x)
=\int_0^\infty e^{-xt}\frac{t^{k-1}}{\pi^2+\log^2t}\,dt.
\]
For \(x=e^{-L}\),
\[
\frac{A_2(x)^2}{A_1(x)A_3(x)}
=
\frac12-\frac{1}{2L}+O(L^{-2}).
\]
Thus \(\alpha_L=1/2-1/(4L)\in(0,1/2)\) gives
\[
H_2(e^{-L};\alpha_L)<0
\]
for all sufficiently large \(L\). Since complete monotonicity implies pointwise nonnegativity, the source interval cannot be correct.

Promoted nodes:

- `T-Ramanujan-Turan-n2-upper-window-counterfamily`
- `T-Ramanujan-Turan-window-negative-answer`

This is separate from public APP-0014, which classifies \(I_R\) as Stieltjes and its primitive as complete Bernstein. The new layer is a logarithmic-density moment-ratio obstruction for quadratic Laplace-moment Turan gaps.
