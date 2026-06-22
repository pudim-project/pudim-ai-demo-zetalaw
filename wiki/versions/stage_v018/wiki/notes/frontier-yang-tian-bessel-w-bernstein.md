# Frontier: Yang--Tian Bessel \(W_\nu\) Bernstein Conjecture

Source: Zhen-Hang Yang and Jing-Feng Tian, "Convexity of ratios of the modified Bessel functions of the first kind with applications", Revista Matemática Complutense, 2022.

Source note: `raw/scout/sources/yang-tian-bessel-w-bernstein-conjecture.md`

## Source Conjecture

The source defines
\[
W_\nu(x)=\frac{xI_\nu(x)}{I_{\nu+1}(x)}.
\]
Conjecture 3 asks whether for every \(\tau\in(0,1/2]\) and \(\nu>-1\), the function
\[
x\mapsto W_\nu(x^\tau)
\]
is a Bernstein function on \((0,\infty)\).

## Bounded Slice

The explicit boundary order \(\nu=-1/2\) gives
\[
W_{-1/2}(x)=x\coth x.
\]
The bounded Student target is
\[
0<\tau\le\frac12
\quad\Longrightarrow\quad
x\mapsto x^\tau\coth(x^\tau)\text{ is Bernstein}.
\]

## Mechanism

Use the partial fraction expansion
\[
z\coth z=1+2z^2\sum_{n=1}^\infty\frac1{z^2+\pi^2n^2}.
\]
For \(g(s)=\sqrt{s}\coth\sqrt{s}\), this implies
\[
g'(s)=2\sum_{n=1}^\infty\frac{\pi^2n^2}{(s+\pi^2n^2)^2},
\]
which is completely monotone. Thus \(g\) is Bernstein. Since \(x^{2\tau}\) is Bernstein for \(0<2\tau\le1\) and Bernstein functions are closed under composition, \(g(x^{2\tau})=x^\tau\coth(x^\tau)\) is Bernstein.

## Status

The boundary slice \(\nu=-1/2\) is solved by `raw/student/20260528T173000-yang-tian-bessel-w-boundary.md` and audited in `librarian/audits/LA-20260528T173000-yang-tian-bessel-student.json`:
\[
0<\tau\le\frac12
\quad\Longrightarrow\quad
x\mapsto W_{-1/2}(x^\tau)=x^\tau\coth(x^\tau)
\text{ is Bernstein}.
\]

The same proof records the sharpness of the source exponent for this boundary order:
\[
\tau>\frac12
\quad\Longrightarrow\quad
x^\tau\coth(x^\tau)
\text{ is not Bernstein}.
\]

## 20260603 Full Conjecture Update

Student pass `20260603T-yang-tian-bessel-w-full-conjecture` upgrades the boundary slice to all \(\nu>-1\). With \(\mu=\nu+1>0\), the Bessel product for \(I_\mu\) and the recurrence \(I_\mu'=I_{\mu-1}-\mu I_\mu/z\) give
\[
W_\nu(z)
=2(\nu+1)+2\sum_{n=1}^{\infty}\frac{z^2}{z^2+j_{\nu+1,n}^2}.
\]
Therefore \(G_\nu(s)=W_\nu(\sqrt s)\) has
\[
G_\nu'(s)
=2\sum_{n=1}^{\infty}\frac{j_{\nu+1,n}^2}{(s+j_{\nu+1,n}^2)^2},
\]
a completely monotone derivative. Hence \(G_\nu\) is Bernstein, and \(W_\nu(x^\tau)=G_\nu(x^{2\tau})\) is Bernstein for \(0<\tau\le1/2\) by Bernstein-function composition. Audit `LA-20260603T-yang-tian-bessel-w-full-conjecture` promotes the source conjecture true and makes this a post-APP-0030 application candidate.
