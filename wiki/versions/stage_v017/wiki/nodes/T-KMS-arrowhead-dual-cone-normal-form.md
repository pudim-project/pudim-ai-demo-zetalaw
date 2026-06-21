---
id: "T-KMS-arrowhead-dual-cone-normal-form"
type: "theorem"
title: "KMS arrowhead cone dual normal form under zw pairing"
status: "proved"
tags: ["bridge-seed", "dual-cone", "normal-form", "proved", "spectrahedral", "theorem"]
parents: ["T-Convex-duality-curvature-principle", "T-KMS-arrowhead-riesz-kernel-pminus2"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-spectrahedral-riesz-arrowhead.md"]
---

# Theorem: KMS arrowhead cone dual normal form under zw pairing

## Statement

For \(C=\{(x,y,z):x>0,xy>z^2\}\) and pairing \(xu+yv+zw\), the dual cone is \(C^*=\{(u,v,w):u\ge0,v\ge0,4uv\ge w^2\}\).

## Dependencies

- [[wiki/nodes/T-Convex-duality-curvature-principle|Convex duality and curvature principle]]
- [[wiki/nodes/T-KMS-arrowhead-riesz-kernel-pminus2|KMS arrowhead spectrahedral determinant p minus 2 explicit Riesz kernel]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-spectrahedral-riesz-arrowhead.md`

## Proof

Let
\[
p(x,y,z)=x(xy-z^2),
\qquad
C=\{(x,y,z):x>0,\ xy>z^2\}.
\]
Use the pairing \(xu+yv+zw\). Define
\[
K(u,v,w)=
\frac{4\sqrt v}{15\pi}
\left(u-\frac{w^2}{4v}\right)^{5/2}
\mathbf 1_{\{v>0,\ u>w^2/(4v)\}}.
\]
Then, for \((x,y,z)\in C\),
\[
\int_{\mathbb R^3}e^{-xu-yv-zw}K(u,v,w)\,du\,dv\,dw
=\frac{1}{x^2(xy-z^2)^2}
=p(x,y,z)^{-2}.
\]

Set
\[
s=u-\frac{w^2}{4v}.
\]
Then \(u=s+w^2/(4v)\), \(s>0\), \(v>0\), and the transform equals
\[
\frac{4}{15\pi}\int_0^\infty\int_{-\infty}^{\infty}\int_0^\infty
e^{-xs-xw^2/(4v)-yv-zw}\sqrt v\,s^{5/2}\,ds\,dw\,dv.
\]
The \(s\)-integral is
\[
\int_0^\infty e^{-xs}s^{5/2}\,ds
=\Gamma(7/2)x^{-7/2}
=\frac{15\sqrt\pi}{8}x^{-7/2}.
\]
The \(w\)-integral is
\[
\int_{-\infty}^{\infty}\exp\left(-\frac{xw^2}{4v}-zw\right)\,dw
=2\sqrt{\frac{\pi v}{x}}\exp\left(\frac{vz^2}{x}\right).
\]
Therefore the transform becomes
\[
x^{-4}\int_0^\infty v\exp\left[-v\left(y-\frac{z^2}{x}\right)\right]\,dv.
\]
Since \((x,y,z)\in C\), \(y-z^2/x>0\), and
\[
\int_0^\infty ve^{-av}\,dv=a^{-2}.
\]
Thus
\[
x^{-4}\left(y-\frac{z^2}{x}\right)^{-2}
=\frac{1}{x^2(xy-z^2)^2}
=p(x,y,z)^{-2}.
\]

Identify
\[
(x,y,z)\leftrightarrow
\begin{pmatrix}x&z\\ z&y\end{pmatrix},
\qquad
(u,v,w)\leftrightarrow
\begin{pmatrix}u&w/2\\ w/2&v\end{pmatrix}.
\]
Then \(\operatorname{tr}(AB)=xu+yv+zw\). Hence the dual cone is
\[
C^*=\{u\ge0,\ v\ge0,\ 4uv\ge w^2\}.
\]
The formula uses the coordinate \(w=2B_{12}\). In the raw symmetric-matrix coordinate \(s=B_{12}\), the density becomes
\[
\frac{8\sqrt v}{15\pi}
\left(u-\frac{s^2}{v}\right)^{5/2}
\mathbf 1_{\{v>0,\ u>s^2/v\}}.
\]

_Proof source: `private proof note`._

## Tags

`bridge-seed`, `dual-cone`, `normal-form`, `proved`, `spectrahedral`, `theorem`
