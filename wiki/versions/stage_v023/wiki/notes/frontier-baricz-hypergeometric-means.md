# Frontier: Baricz Hypergeometric Bivariate Means

Scout forage `FI-20260528T-next-loop-006` selected the Baricz problem recorded in Anderson--Vuorinen--Zhang, arXiv:1209.1696.

The source asks for conditions on bivariate means \(m_1,m_2\), parameters \(a_1,a_2>0\), and \(c>0\) such that
\[
m_1(F_{a_1}(r),F_{a_2}(r))\le(\ge)F_{m_2(a_1,a_2)}(r)
\]
for all \(r\in(0,1)\), where
\[
F_a(r)={}_2F_1(a,c-a;c;r).
\]

The local Theory fit is through Gamma/Beta normalization, Euler positive-kernel integrals, parameter convexity, and mean inequalities. This is admitted as a broad frontier only; Student should first do a status check and then attempt at most one bounded slice.

## Student/Librarian outcome `20260528T125000Z`

The bounded Student pass confirmed that the broad bivariate-mean classification should stay open locally. The pass did promote two reusable facts:

\[
F_a(r)=
\frac{\Gamma(c)}{\Gamma(a)\Gamma(c-a)}
\int_0^1 t^{a-1}(1-t)^{c-a-1}(1-rt)^{a-c}\,dt
\]

for \(0<a<c\), \(0<r<1\), and the known Baricz \(0<c\le1\) slice

\[
\sqrt{F_{a_1}(r)F_{a_2}(r)}
\le
\frac{F_{a_1}(r)+F_{a_2}(r)}2
\le
F_{(a_1+a_2)/2}(r).
\]

This is useful Theory growth through beta kernels and parameter concavity, but it is not a solution of the full Baricz mean-classification problem. Under the diversity rule, the active loop rotates rather than spending a long run on this broad family.
