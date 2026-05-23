---
id: mrw-58db958e1bf1
type: theorem
title: Convexity of the reciprocal trigamma product
aliases: ["mrw-58db958e1bf1", "Convexity of the reciprocal trigamma product"]
status: proved
tags: ["theorem", "proved", "polygamma", "trigamma", "convexity", "qi-lim-nantomah", "frontier"]
parents: [mrw-a4339be8da59, mrw-1c9d9f07a4ef, mrw-f0a031feea8e]
refs: ["references/sources/20260518T142240Z-qiln-open-problem-2-refresh.md", "references/sources/20260518T142240Z-dlmf-polygamma-series.md"]
---

# Theorem: Convexity of the reciprocal trigamma product

## Statement

Let
\[
P_1(x)=\psi'(x)\psi'(1/x),\qquad x>0.
\]
Then
\[
P_1''(x)>0\qquad(x>0).
\]
Thus the \(n=1\) case of the convexity part of the reciprocal-polygamma product problem is solved affirmatively.  This theorem does not assert complete monotonicity of \(P_1''\).

## Proof

For \(m\ge1\), write
\[
A_m(x)=(-1)^{m+1}\psi^{(m)}(x).
\]
Then \(A_m(x)>0\) on \((0,\infty)\), \(A_m'(x)=-A_{m+1}(x)\), and
\[
A_m(x)=\int_0^\infty \frac{t^m e^{-xt}}{1-e^{-t}}\,dt.
\]
Define
\[
U(x)=\frac{xA_2(x)}{A_1(x)},\qquad
V(x)=\frac{xA_3(x)}{A_2(x)}.
\]
By [[wiki/nodes/mrw-a4339be8da59|Ratio-normal-form reduction for P1 convexity]],
\[
P_1''(x)=\frac{A_1(x)A_1(1/x)}{x^2}\Phi(x),
\]
where
\[
\Phi(x)=U(x)V(x)+U(1/x)V(1/x)-2U(x)U(1/x)-2U(1/x).
\]
The prefactor is strictly positive, so it remains to prove \(\Phi(x)>0\).

First,
\[
U(x)<2
\]
because
\[
2A_1(x)-xA_2(x)
=2\sum_{k=0}^{\infty}\frac{k}{(x+k)^3}>0.
\]
Also,
\[
U(x)>1.
\]
Indeed, with \(f_2(t)=t^2/(1-e^{-t})\) and \(f_1(t)=t/(1-e^{-t})\), integration by parts gives
\[
xA_2(x)-A_1(x)
=\int_0^\infty e^{-xt}\bigl(f_2'(t)-f_1(t)\bigr)\,dt.
\]
A direct simplification yields
\[
f_2'(t)-f_1(t)
=\frac{t e^t(e^t-1-t)}{(e^t-1)^2}>0
\]
for \(t>0\).  Hence
\[
1<U(x)<2\qquad(x>0).
\]

Next set
\[
Q(x)=U(x)\bigl(V(x)-U(x)-1\bigr).
\]
Differentiating \(U=xA_2/A_1\) gives
\[
xU'(x)=U(x)\bigl(1+U(x)-V(x)\bigr),
\]
so \(Q(x)=-xU'(x)\).  We need a lower bound for \(Q\).  The inequality
\[
Q(x)\ge (U(x)-1)(2-U(x))
\]
is equivalent, after substituting \(U=xA_2/A_1\) and \(V=xA_3/A_2\), to
\[
x^2A_3(x)-4xA_2(x)+2A_1(x)\ge0.
\]
Let \(f_j(t)=t^j/(1-e^{-t})\).  Since the boundary terms vanish at \(0\) and \(\infty\), integration by parts gives
\[
x^2A_3(x)-4xA_2(x)+2A_1(x)
=\int_0^\infty e^{-xt}\left(f_3''(t)-4f_2'(t)+2f_1(t)\right)\,dt.
\]
The kernel simplifies to
\[
f_3''(t)-4f_2'(t)+2f_1(t)
=\frac{t^2e^t}{(e^t-1)^3}\left[t(e^t+1)-2(e^t-1)\right].
\]
If \(h(t)=t(e^t+1)-2(e^t-1)\), then
\[
h(0)=0,\qquad h'(0)=0,\qquad h''(t)=te^t>0
\]
for \(t>0\).  Therefore \(h(t)>0\) for \(t>0\), and the kernel above is positive.  Hence
\[
Q(x)\ge (U(x)-1)(2-U(x)).
\]

Now abbreviate
\[
u=U(x),\qquad \bar u=U(1/x),\qquad
B=u-1,\qquad C=2-\bar u.
\]
The range \(1<U<2\) gives \(B,C\in(0,1)\), and
\[
u-\bar u=B+C-1.
\]
Using \(uv=u(u+1)+Q(x)\) and \(\bar u\bar v=\bar u(\bar u+1)+Q(1/x)\), where \(v=V(x)\) and \(\bar v=V(1/x)\), we obtain
\[
\Phi(x)=(u-\bar u)^2+(u-\bar u)+Q(x)+Q(1/x).
\]
Applying the lower bound for \(Q\) at \(x\) and \(1/x\),
\[
\begin{aligned}
\Phi(x)
&\ge (B+C-1)^2+(B+C-1)+B(1-B)+C(1-C)\\
&=2BC>0.
\end{aligned}
\]
Thus \(\Phi(x)>0\), and therefore \(P_1''(x)>0\) for every \(x>0\).

## Depends on

- [[wiki/nodes/mrw-a4339be8da59|Ratio-normal-form reduction for P1 convexity]]
- [[wiki/nodes/mrw-1c9d9f07a4ef|P1 trigamma product complete-monotonicity frontier]]
- [[wiki/nodes/mrw-f0a031feea8e|Higher-order monotonicity of polygamma products Pn]]

## Used by

## Notes

- This proves only the convexity part for \(P_1\).  The stronger complete-monotonicity question for \(P_1''\) remains open.
- The proof deliberately avoids independent pole-family positivity, which is impossible by [[wiki/nodes/mrw-5a84b7d9f2c1|Pole-family obstruction for the P1 kernel route]].
