---
id: "T-Polymath15-symmetric-quartic-backward-heat-certificate"
type: "theorem"
title: "T-Polymath15-symmetric-quartic-backward-heat-certificate"
status: "proved"
tags: ["proved", "theorem"]
parents: ["T-Polymath15-quartic-backward-heat-certificate", "T-Exact-finite-certificate-verification-principle"]
refs: ["private Oracle response", "private proof note", "wiki/notes/tao-polymath15-symmetric-quartic-heat-flow.md"]
---

# Theorem: T-Polymath15-symmetric-quartic-backward-heat-certificate

## Statement

For every 0<a<=b, F0(x)=(x^2-a^2)(x^2-b^2) has the property that F_t=e^{-t partial_x^2}F0 has only real zeros for every t>=0.

## Scope

- Finite symmetric quartic heat-flow certificate; not a de Bruijn-Newman Lambda-bound improvement.

## Dependencies

- [[wiki/nodes/T-Polymath15-quartic-backward-heat-certificate|Polymath15 quartic backward-heat certificate]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`
- `wiki/notes/tao-polymath15-symmetric-quartic-heat-flow.md`

## Proof

Let
\[
S=a^2+b^2,\qquad P=a^2b^2.
\]
Then
\[
F_0(x)=x^4-Sx^2+P.
\]
Using
\[
e^{-t\partial_x^2}x^4=x^4-12tx^2+12t^2,
\qquad
e^{-t\partial_x^2}x^2=x^2-2t,
\]
we obtain
\[
F_t(x)
=
x^4-(S+12t)x^2+(P+2St+12t^2).
\]
Put \(u=x^2\). Then
\[
F_t(x)=Q_t(u),
\]
where
\[
Q_t(u)
=
u^2-(S+12t)u+(P+2St+12t^2).
\]
The discriminant of \(Q_t\) is
\[
\Delta_t
=
(S+12t)^2-4(P+2St+12t^2).
\]
Expanding gives
\[
\Delta_t
=
S^2-4P+16St+96t^2.
\]
Since
\[
S^2-4P
=
(a^2+b^2)^2-4a^2b^2
=
(b^2-a^2)^2,
\]
we have
\[
\Delta_t
=
(b^2-a^2)^2+16(a^2+b^2)t+96t^2\ge0.
\]
Thus \(Q_t\) has two real roots.

Their sum is
\[
S+12t>0,
\]
and their product is
\[
P+2St+12t^2>0.
\]
Therefore both roots \(u_1,u_2\) of \(Q_t\) are positive. Hence
\[
F_t(x)=(x^2-u_1)(x^2-u_2)
\]
has only real zeros,
\[
x=\pm\sqrt{u_1},\qquad x=\pm\sqrt{u_2}.
\]

Equivalently, the roots in \(u\) are explicitly
\[
u_\pm(t)
=
\frac{S+12t\pm
\sqrt{(b^2-a^2)^2+16St+96t^2}}2,
\]
and both are positive for \(t\ge0\).

This is a finite heat-flow certificate theorem in the style of Polymath15 zero-dynamics checks. It generalizes the single local example
\[
(x^2-1)(x^2-4).
\]
It does not imply a new upper bound for the de Bruijn-Newman constant.

The next natural target is the symmetric sextic family
\[
\prod_{j=1}^3(x^2-a_j^2),
\]
where the reduction becomes a cubic in \(u=x^2\), and the quartic discriminant argument no longer suffices.

_Proof source: `private proof note`._

## Tags

`proved`, `theorem`
