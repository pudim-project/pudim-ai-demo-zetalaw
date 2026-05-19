---
id: mrw-28bcccec471e
type: theorem
title: Exact inverse-tail floor formula at s=7
aliases: ["mrw-28bcccec471e", "Exact inverse-tail floor formula at s=7"]
status: proved
tags: ["scout-forage", "theorem", "proved", "tail-zeta", "inverse-tail"]
parents: [mrw-900d84ddee24, mrw-6ad81d0b87f7]
refs: []
---

# Theorem: Exact inverse-tail floor formula at s=7

## Statement

For \(n\ge1\), put
\[
T_7(n)=\zeta_n(7)=\sum_{k=n}^{\infty}\frac1{k^7}.
\]
Define
\[
Q(n)=120n^6-360n^5+660n^4-720n^3+354n^2-54n+375,
\qquad
P(n)=\frac{Q(n)}{20}.
\]
Then, for every \(n\ge28\),
\[
\left\lfloor T_7(n)^{-1}\right\rfloor=\left\lfloor P(n)\right\rfloor.
\]
For \(1\le n\le27\), the exact values are:
\[
\begin{array}{c|rrrrrrrrrrrrrrrrrrrrrrrrrrr}
n&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16&17&18&19&20&21&22&23&24&25&26&27\\
\hline
\lfloor T_7(n)^{-1}\rfloor&
0&119&1862&12573&54069&175597&471118&1100904&2317459&
4495760&8167814&14061542&23143975&36668777&56228085&
83808666&121852400&173321080&241765529&331399044&
447175152&594869693&781167220&1013751716&1301401638&
1654089273&2083084422
\end{array}.
\]

## Proof

First note that \(Q(n)>0\) for \(n\ge1\), since
\[
\begin{aligned}
Q(n)
&=120(n-1)^6+360(n-1)^5+660(n-1)^4+720(n-1)^3\\
&\qquad +354(n-1)^2+54(n-1)+375.
\end{aligned}
\]
For \(k\ge1\), direct expansion gives
\[
\frac1{k^7}
-\left(\frac{20}{Q(k)}-\frac{20}{Q(k+1)}\right)
=
\frac{9(60284k^4+29176k^2+15625)}
{k^7Q(k)Q(k+1)}>0.
\]
Summing over \(k\ge n\) gives
\[
T_7(n)>\frac{20}{Q(n)}=\frac1{P(n)},
\]
and hence \(T_7(n)^{-1}<P(n)\).

For \(k\ge28\), another direct expansion gives
\[
\left(\frac{20}{Q(k)-3}-\frac{20}{Q(k+1)-3}\right)
-\frac1{k^7}
=
\frac{36(20k^6-14961k^4-7235k^2-3844)}
{k^7(Q(k)-3)(Q(k+1)-3)}.
\]
The numerator is positive for \(k\ge28\). Indeed, after writing \(k=m+28\), it becomes
\[
20m^6+3360m^5+220239m^4+7105168m^3
+114013021m^2+751143512m+436261580,
\]
which has positive coefficients for \(m\ge0\). Therefore, for every \(n\ge28\),
\[
T_7(n)<\frac{20}{Q(n)-3}=\frac1{P(n)-3/20},
\]
so
\[
P(n)-\frac3{20}<T_7(n)^{-1}<P(n).
\]
Modulo \(20\),
\[
Q(n)\equiv 14n^2-14n+15\pmod {20}.
\]
Since \(n(n-1)\pmod {10}\) is one of \(0,2,6\), we have
\[
Q(n)\pmod {20}\in\{3,15,19\}.
\]
Thus the fractional part of \(P(n)\) is always one of \(3/20,15/20,19/20\). If \(a=\lfloor P(n)\rfloor\), then
\[
P(n)-\frac3{20}\ge a
\]
and the preceding strict inequalities give
\[
a<T_7(n)^{-1}<a+1.
\]
Hence \(\lfloor T_7(n)^{-1}\rfloor=a=\lfloor P(n)\rfloor\) for \(n\ge28\).

It remains only to certify \(1\le n\le27\). For \(n=1\), \(T_7(1)>1\), so \(0<T_7(1)^{-1}<1\). For \(2\le n\le27\), let \(M_n\) be the value displayed in the table. With \(N=1500\), exact rational arithmetic verifies
\[
\sum_{k=n}^{N}\frac1{k^7}>\frac1{M_n+1}
\]
and, using the monotone integral tail bound,
\[
\sum_{k=n}^{N}\frac1{k^7}+\frac1{6N^6}<\frac1{M_n}.
\]
Since
\[
\sum_{k=N+1}^{\infty}\frac1{k^7}<\int_N^\infty x^{-7}\,dx=\frac1{6N^6},
\]
we get
\[
\frac1{M_n+1}<T_7(n)<\frac1{M_n}.
\]
Therefore \(M_n<T_7(n)^{-1}<M_n+1\), and the finite table follows. The exact rational verification is recorded in `calculations/verify_s7_inverse_tail.py`.

## Source References

- Donggyun Kim and Kyunghwan Song, "The inverses of tails of the Riemann zeta function", Journal of Inequalities and Applications 2018, article 157. https://link.springer.com/article/10.1186/s13660-018-1743-6
- Zhenjiang Pan and Zhengang Wu, "The inverse of tails of Riemann zeta function, Hurwitz zeta function and Dirichlet L-function", AIMS Mathematics 9(6), 16564-16585, 2024. DOI: https://doi.org/10.3934/math.2024803

## Depends on

- [[wiki/nodes/mrw-900d84ddee24|Exact inverse-tail floor formula at s=7]]
- [[wiki/nodes/mrw-6ad81d0b87f7|Tail zeta partition function]]

## Notes

- This proves the first scout-forage candidate. It does not solve the broader problem of exact inverse-tail formulas for every integer \(s>6\).
- The source-status check found the 2018 open-status statement and a 2024 asymptotic paper, but no exact \(s=7\) floor formula in the bounded primary-source search.
