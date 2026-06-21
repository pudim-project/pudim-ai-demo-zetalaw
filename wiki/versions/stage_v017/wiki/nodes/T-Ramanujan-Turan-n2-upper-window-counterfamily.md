---
id: "T-Ramanujan-Turan-n2-upper-window-counterfamily"
type: "theorem"
title: "Ramanujan Turan n two upper window has small x counterfamily"
status: "proved"
tags: ["complete-monotonicity", "counterexample", "moment-ratio", "proved", "ramanujan-integral", "source-open-solved", "theorem", "turan"]
parents: ["T-Finite-combinatorial-packing-shadow-principle"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-ramanujan-turan-gap-refutation.md"]
---

# Theorem: Ramanujan Turan n two upper window has small x counterfamily

## Statement

For the Ramanujan integral Turan gap, there are parameters \(\alpha\in(0,1/2)\) such that \(H_2(x;\alpha)<0\) for some \(x>0\); specifically, with \(x=e^{-L}\) and \(\alpha_L=1/2-1/(4L)\), this holds for all sufficiently large \(L\).

## Dependencies

- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-ramanujan-turan-gap-refutation.md`

## Proof

Put
\[
A_k(x)=(-1)^k I_R^{(k)}(x)
=\int_0^\infty e^{-xt}\frac{t^{k-1}}{\pi^2+\log^2 t}\,dt
\qquad (k\ge1).
\]
Then
\[
H_2(x;\alpha)=A_2(x)^2-\alpha A_1(x)A_3(x).
\]

We study \(x=e^{-L}\) as \(L\to\infty\). With \(y=xt\),
\[
A_k(e^{-L})
=
e^{kL}\int_0^\infty
\frac{e^{-y}y^{k-1}}
{\pi^2+(L+\log y)^2}\,dy.
\]

For fixed \(k=1,2,3\),
\[
A_k(e^{-L})
=
e^{kL}L^{-2}\Gamma(k)
\left(1-\frac{2\psi(k)}{L}+O(L^{-2})\right),
\]
where \(\psi\) is the digamma function. To justify the expansion, split the \(y\)-integral into the central region \(|\log y|\le L^{2/3}\) and its complement. On the central interval, with \(z=\log y\), expand uniformly:
\[
\frac{1}{\pi^2+(L+\log y)^2}
=
L^{-2}\left(1-\frac{2\log y}{L}+O\left(\frac{1+\log^2 y}{L^2}\right)\right),
\]
and integrate against \(e^{-y}y^{k-1}\). The lower complement \(0<y<e^{-L^{2/3}}\) is \(O(e^{-cL^{2/3}})\) for \(k=1,2,3\) after the change \(y=e^{-u}\), and the upper complement \(y>e^{L^{2/3}}\) is super-exponentially small because of \(e^{-y}\). These errors are \(o(L^{-N})\) for every fixed \(N\), which is more than needed for the displayed expansion.

Therefore
\[
\frac{A_2(e^{-L})^2}{A_1(e^{-L})A_3(e^{-L})}
=
\frac{\Gamma(2)^2}{\Gamma(1)\Gamma(3)}
\left(
1+\frac{2(\psi(1)+\psi(3)-2\psi(2))}{L}+O(L^{-2})
\right).
\]
Using
\[
\psi(1)=-\gamma,\qquad
\psi(2)=1-\gamma,\qquad
\psi(3)=\frac32-\gamma,
\]
we get
\[
\psi(1)+\psi(3)-2\psi(2)=-\frac12,
\]
so
\[
\frac{A_2(e^{-L})^2}{A_1(e^{-L})A_3(e^{-L})}
=
\frac12-\frac{1}{2L}+O(L^{-2}).
\]

Choose
\[
\alpha_L=\frac12-\frac{1}{4L}.
\]
For all sufficiently large \(L\), \(\alpha_L\in(0,1/2)\) and
\[
\frac{A_2(e^{-L})^2}{A_1(e^{-L})A_3(e^{-L})}<\alpha_L.
\]
Consequently
\[
H_2(e^{-L};\alpha_L)
=
A_2(e^{-L})^2-\alpha_L A_1(e^{-L})A_3(e^{-L})
<0.
\]

Complete monotonicity would imply nonnegativity at order zero. Hence \(H_2(\cdot;\alpha_L)\) is not completely monotone for these fixed parameters \(\alpha_L\in(0,1/2)\). The source's universal Turan-window statement is false already in the \(n=2\) upper window.

the Ramanujan Turan n2 upper window counterfamily
the Ramanujan Turan window negative answer

The new mechanism is a logarithmic-density moment-ratio asymptotic obstruction for quadratic Laplace-moment Turan gaps. It is distinct from the public APP-0014 Stieltjes/complete-Bernstein classification of \(I_R\).

_Proof source: `private proof note`._

## Tags

`complete-monotonicity`, `counterexample`, `moment-ratio`, `proved`, `ramanujan-integral`, `source-open-solved`, `theorem`, `turan`
