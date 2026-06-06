---
id: "T-Ramanujan-Turan-window-negative-answer"
type: "theorem"
title: "Ramanujan integral Turan window complete monotonicity problem negative answer"
status: "proved"
tags: ["application-candidate", "complete-monotonicity", "negative-answer", "proved", "ramanujan-integral", "source-open-solved", "theorem", "turan"]
parents: ["T-Ramanujan-Turan-n2-upper-window-counterfamily", "T-Pointwise-obstruction-certificate-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260603T-ramanujan-turan-gap-refutation.json", "raw/student/20260603T-ramanujan-turan-gap-refutation.md", "wiki/notes/frontier-ramanujan-turan-gap-refutation.md"]
---

# Theorem: Ramanujan integral Turan window complete monotonicity problem negative answer

## Statement

The Mishra--Swaminathan Ramanujan integral Turan-window complete-monotonicity problem has a negative answer: the proposed interval already fails for \(n=2\) and suitable \(\alpha\in(0,1/2)\).

## Dependencies

- [[wiki/nodes/T-Ramanujan-Turan-n2-upper-window-counterfamily|Ramanujan Turan n two upper window has small x counterfamily]]
- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260603T-ramanujan-turan-gap-refutation.json`
- `raw/student/20260603T-ramanujan-turan-gap-refutation.md`
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

_Proof source: `raw/student/20260603T-ramanujan-turan-gap-refutation.md`._

## Tags

`application-candidate`, `complete-monotonicity`, `negative-answer`, `proved`, `ramanujan-integral`, `source-open-solved`, `theorem`, `turan`
