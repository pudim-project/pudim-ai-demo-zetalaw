---
id: mrw-0db1ed17aa9a
type: theorem
title: Complete monotonicity of reciprocal digamma product curvature
aliases: ["mrw-0db1ed17aa9a", "Complete monotonicity of reciprocal digamma product curvature"]
status: proved
tags: ["scout-forage", "theorem", "proved", "gamma", "digamma", "polygamma", "complete-monotonicity", "non-tail"]
parents: [mrw-2650caac5236, mrw-48a67678d0c1]
refs: []
---

# Theorem: Complete monotonicity of reciprocal digamma product curvature

## Statement

Let
\[
P_0(x)=\psi(x)\psi(1/x),\qquad x>0,
\]
where \(\psi=\Gamma'/\Gamma\) is the digamma function. Then \(-P_0''\) is strictly completely monotonic on \((0,\infty)\). Equivalently,
\[
(-1)^r\frac{d^r}{dx^r}\bigl(-P_0''(x)\bigr)>0
\]
for every integer \(r\ge0\) and every \(x>0\). In particular, \(P_0\) is strictly concave on \((0,\infty)\).

More precisely,
\[
-P_0''(x)=\int_0^\infty e^{-xt}K(t)\,dt,
\]
where
\[
\begin{aligned}
K(t)=t^2\Bigg[
&1-\gamma+(t-1)e^{-t}\\
&+\sum_{n=2}^{\infty}
\frac{n(1-e^{-t/n})-\psi(1-1/n)e^{-t/n}}{n^2}
+\sum_{m=2}^{\infty}\bigl(m+\psi(1-1/m)\bigr)e^{-mt}
\Bigg],
\end{aligned}
\]
and \(K(t)>0\) for \(t>0\).

## Proof

Direct differentiation gives
\[
\begin{aligned}
P_0''(x)
=&\psi''(x)\psi(1/x)
-\frac{2}{x^2}\psi'(x)\psi'(1/x)\\
&+\frac{2}{x^3}\psi(x)\psi'(1/x)
+\frac{1}{x^4}\psi(x)\psi''(1/x).
\end{aligned}
\]
Use the shifted Weierstrass expansion
\[
\psi(x)=-\gamma-\frac1x+\sum_{m=1}^{\infty}a_m(x),
\qquad
a_m(x)=\frac{x}{m(m+x)},
\]
and, after substituting \(1/x\),
\[
\psi(1/x)=-\gamma-x+\sum_{n=1}^{\infty}b_n(x),
\qquad
b_n(x)=\frac1{n(nx+1)}.
\]
On every compact subinterval of \((0,\infty)\), the series for \(a_m\), \(b_n\), and their first two derivatives are uniformly summable; the differentiated double products are dominated by products of these summable majorants. Hence the product may be differentiated twice term by term.

Put \(A_0(x)=-\gamma-1/x\) and \(B_0(x)=-\gamma-x\). The base term contributes
\[
-\frac{d^2}{dx^2}\bigl(A_0(x)B_0(x)\bigr)=-\frac{2\gamma}{x^3},
\]
whose Laplace kernel is \(-\gamma t^2\). For \(n\ge1\),
\[
-\frac{d^2}{dx^2}\bigl(A_0(x)b_n(x)\bigr)
\longleftrightarrow
t^2\frac{n+(\gamma-n)e^{-t/n}}{n^2},
\]
where \(\longleftrightarrow\) means equality after applying the Laplace transform
\(\int_0^\infty e^{-xt}(\cdot)\,dt\). Similarly, for \(m\ge1\),
\[
-\frac{d^2}{dx^2}\bigl(B_0(x)a_m(x)\bigr)
\longleftrightarrow
t^2(m-\gamma)e^{-mt}.
\]
For \(mn>1\),
\[
-\frac{d^2}{dx^2}\bigl(a_m(x)b_n(x)\bigr)
\longleftrightarrow
t^2\left[
\frac{e^{-t/n}}{mn^2(mn-1)}
-\frac{e^{-mt}}{n(mn-1)}
\right].
\]
The exceptional term is \(a_1(x)b_1(x)=x/(x+1)^2\), and
\[
-\frac{d^2}{dx^2}\frac{x}{(x+1)^2}
\longleftrightarrow
t^2(t-1)e^{-t}.
\]
These four identities are elementary consequences of
\[
\frac1{(x+c)^3}=\int_0^\infty e^{-xt}\frac{t^2}{2}e^{-ct}\,dt,
\qquad
\frac1{(x+c)^4}=\int_0^\infty e^{-xt}\frac{t^3}{6}e^{-ct}\,dt,
\]
and direct rational differentiation.

It remains to sum the double-product coefficients. For \(n\ge2\),
\[
\sum_{m=1}^{\infty}\frac1{m(mn-1)}
=-\psi(1-1/n)-\gamma,
\]
and for \(m\ge2\),
\[
\sum_{n=1}^{\infty}\frac1{n(mn-1)}
=-\psi(1-1/m)-\gamma.
\]
These follow from the standard identity
\[
\psi(z+1)+\gamma=\sum_{k=1}^{\infty}\frac{z}{k(k+z)}
\]
with \(z=-1/n\) or \(z=-1/m\). Adding the base, one-body, exceptional, and grouped two-body contributions gives the displayed kernel \(K\).

Now prove \(K(t)>0\). Since \(\psi\) is increasing and \(1-1/n\in[1/2,1)\),
\[
-\psi(1-1/n)>0
\]
for \(n\ge2\). Also
\[
m+\psi(1-1/m)>0\qquad(m\ge2),
\]
because \(\psi(1-1/m)\ge\psi(1/2)=-\gamma-2\log2\) and
\[
2-\gamma-2\log2>0.
\]
Thus the \(m\)-sum is positive and every \(n\)-summand is positive. The only possible negative part is \(1-\gamma+(t-1)e^{-t}\).

For \(n\ge2\),
\[
-\psi(1-1/n)
=\gamma+\int_{1-1/n}^{1}\psi'(u)\,du
>\gamma+\int_{1-1/n}^{1}\frac{du}{u^2}
=\gamma+\frac1{n-1}.
\]
Therefore the \(n\)-sum is bounded below by
\[
e^{-t/2}\sum_{n=2}^{\infty}
\left(\frac{\gamma}{n^2}+\frac1{n^2(n-1)}\right)
=Ae^{-t/2},
\]
where
\[
A=\gamma(\zeta(2)-1)+2-\zeta(2).
\]
It is enough to show
\[
f(t)=1-\gamma+(t-1)e^{-t}+Ae^{-t/2}>0.
\]
At \(t=0\),
\[
f(0)=A-\gamma=(2-\zeta(2))(1-\gamma)>0,
\]
and \(f(t)\to1-\gamma>0\) as \(t\to\infty\). Moreover
\[
f'(t)=e^{-t}\left(2-t-\frac{A}{2}e^{t/2}\right),
\]
and the factor in parentheses is strictly decreasing. Hence \(f\) has at most one critical point, and if it exists it is a maximum. The minimum on \([0,\infty)\) is therefore attained at an endpoint, so \(f(t)>0\) for all \(t\ge0\). This proves \(K(t)>0\) for \(t>0\).

Consequently
\[
-P_0''(x)=\int_0^\infty e^{-xt}K(t)\,dt
\]
is the Laplace transform of a strictly positive kernel. Differentiating under the integral gives
\[
(-1)^r\frac{d^r}{dx^r}\bigl(-P_0''(x)\bigr)
=\int_0^\infty t^r e^{-xt}K(t)\,dt>0,
\]
which proves strict complete monotonicity. The case \(r=0\) gives \(-P_0''(x)>0\), or \(P_0''(x)<0\), so \(P_0\) is strictly concave.

## Source References

- Feng Qi, Dongkyu Lim, and Kwara Nantomah, "Monotonicity and positivity of several functions involving ratios and products of polygamma functions", Journal of Inequalities and Applications 2025, article 5. DOI: https://doi.org/10.1186/s13660-024-03245-8

## Depends on

- [[wiki/nodes/mrw-2650caac5236|Concavity or complete monotonicity of the polygamma product P0]]
- [[wiki/nodes/mrw-48a67678d0c1|Complete monotonicity of reciprocal-Gamma curvature]]

## Used by

- [[wiki/nodes/mrw-0e9002ec3122|Pointwise reduction for reciprocal-digamma beta windows]]

## Notes

- This proves Qi--Lim--Nantomah Open Problem 1 in its stronger complete-monotonicity form.
- Oracle supplied the grouped-kernel attack. The algebraic Laplace pieces, regrouping identities, and numerical sign checks were locally audited in `calculations/verify_p0_concavity_cm.py` before promotion.
