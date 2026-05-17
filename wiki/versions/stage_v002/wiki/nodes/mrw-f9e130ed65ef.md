---
id: mrw-f9e130ed65ef
type: theorem
title: Affirmative solution of Nantomah zeta positivity problem
aliases: ["mrw-f9e130ed65ef", "Affirmative solution of Nantomah zeta positivity problem"]
status: proved
tags: [zeta-law, theorem, proved, nantomah]
parents: [mrw-eb9a71666a04, mrw-43596105b428]
refs: ["raw/20260517T155448Z-build-a-raw-pudim-wiki-for-the-zeta-law-entropy-modular-reso-bootstrap-import.md", "bootstrap/20260517T155423Z-zeta-law-pdf-extract.md"]
---

# Theorem: Affirmative solution of Nantomah zeta positivity problem

## Statement

For every \(n\in\mathbb N\),
\[
(n+2)\zeta(n+1)\zeta(n+3)
-(n+1)\zeta(n+2)^2
-\zeta(n+1)\zeta(n+2)>0.
\]

## Proof

Put \(s=n+1\ge2\) and \(Z_s=\zeta(s)\). The expression is
\[
K_s=(s+1)Z_sZ_{s+2}-sZ_{s+1}^2-Z_sZ_{s+1}.
\]
Let \(X(m)=1/m\) under the zeta law \(\rho_s\). Then
\[
\mathbb E_s[X]=\frac{Z_{s+1}}{Z_s},
\qquad
\mathbb E_s[X^2]=\frac{Z_{s+2}}{Z_s},
\]
so
\[
\frac{K_s}{Z_s^2}
=(s+1)\mathbb E_s[X^2]
-s\mathbb E_s[X]^2
-\mathbb E_s[X]
=(s+1)\operatorname{Var}_s(X)
+\mathbb E_s[X]^2-\mathbb E_s[X].
\]

For a direct positivity proof, write
\[
a=\zeta(s)-1,\qquad b=\zeta(s+1)-1,\qquad c=\zeta(s+2)-1.
\]
Then
\[
K_s=L_s+Q_s,
\qquad
L_s=sa+(s+1)c-(2s+1)b,
\qquad
Q_s=(s+1)ac-sb^2-ab.
\]
The linear part is positive term by term:
\[
L_s=\sum_{m=2}^{\infty}
m^{-s}
\left(s-\frac{2s+1}{m}+\frac{s+1}{m^2}\right)
=
\sum_{m=2}^{\infty}
m^{-s}
\frac{(m-1)(s(m-1)-1)}{m^2}.
\]
For \(s\ge2\) and \(m\ge2\), each summand is positive; in particular
\[
L_s\ge 2^{-s}\frac{s-1}{4}.
\]
Since \(b\le a/2\) and \(c\ge0\),
\[
Q_s\ge -sb^2-ab\ge -\frac{s+2}{4}a^2.
\]
For \(s\ge4\),
\[
a=\sum_{m=2}^{\infty}m^{-s}
\le
2^{-s}+\int_2^\infty x^{-s}\,dx
=2^{-s}\left(1+\frac2{s-1}\right).
\]
Therefore
\[
K_s\ge
\frac14\left[
2^{-s}(s-1)
-(s+2)2^{-2s}\left(1+\frac2{s-1}\right)^2
\right].
\]
It is enough to prove
\[
2^s(s-1)>(s+2)\left(1+\frac2{s-1}\right)^2.
\]
Equivalently,
\[
F(s)=\frac{2^s(s-1)^3}{(s+2)(s+1)^2}>1.
\]
Now \(F(4)=72/25>1\), and
\[
\frac{d}{ds}\log F(s)
=\log2+\frac3{s-1}-\frac1{s+2}-\frac2{s+1}>0
\qquad(s\ge4).
\]
Thus \(K_s>0\) for \(s\ge4\).

It remains to check \(s=2\) and \(s=3\). For \(s=2\),
\[
K_2=3\zeta(2)\zeta(4)-2\zeta(3)^2-\zeta(2)\zeta(3).
\]
Using \(\zeta(3)<5/4\), \(\zeta(2)=\pi^2/6\), and \(\zeta(4)=\pi^4/90\),
\[
K_2>\frac{\pi^6}{180}-\frac{5\pi^2}{24}-\frac{25}{8}.
\]
The right side is increasing for \(\pi\ge3\), and \(\pi>313/100\) gives
\[
K_2>
\frac{10415360504209}{180000000000000}>0.
\]
For \(s=3\), use
\[
\zeta(3)>\frac{251}{216},
\qquad
\zeta(5)>\frac{8051}{7776},
\qquad
\zeta(4)<\frac{13}{12}.
\]
Then
\[
K_3
> \frac{251}{216}
\left(4\cdot\frac{8051}{7776}-\frac{13}{12}\right)
-3\left(\frac{13}{12}\right)^2
=\frac{13783}{419904}>0.
\]
Therefore \(K_s>0\) for every integer \(s\ge2\), which proves the statement.

## Source References

- Kwara Nantomah, "Open Problem on Riemann Zeta Function", ResearchGate problem note, October 2024. https://www.researchgate.net/publication/384676538_Open_Problem_on_Riemann_Zeta_Function

## Depends on

- [[wiki/nodes/mrw-eb9a71666a04|Nantomah zeta positivity problem]]
- [[wiki/nodes/mrw-43596105b428|Riemann zeta probability law]]

## Used by

- [[wiki/nodes/mrw-593af0548f67|Four-layer zeta-law framework]]

## Notes

- Promoted to `proved` by ingesting the original theory PDF proof. The small cases \(s=2,3\) use the elementary numerical bounds displayed above.
