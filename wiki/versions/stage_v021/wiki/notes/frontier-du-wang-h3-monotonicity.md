# Frontier Note: Du-Wang h3 Monotonicity

Source: Peipei Du and Gendi Wang, *Monotonicity, convexity, and inequalities for functions involving gamma function*, arXiv:2205.12530.

Open Problem 2 asks for the monotonicity property of
\[
h_3(x)=\frac{-x^2\psi'(x+a)+2x\psi(x+a)-2\log\Gamma(x+a)}{x}
\]
on \((0,\infty)\) for \(0<a<2\). The source proves strict increase for \(a\ge2\).

The admitted local partial result uses the source driver
\[
h_3'(x)=\frac{h_{31}(x+a)}{x^2},
\]
where
\[
h_{31}(t)=-(t-a)^3\psi''(t)+(t-a)^2\psi'(t)-2(t-a)\psi(t)+2\log\Gamma(t).
\]
The endpoint and infinity profile is
\[
h_{31}(a+)=2\log\Gamma(a),
\qquad
h_{31}(t)=(2a-1)\log t+O(1).
\]
Thus \(h_3\) is not monotone on \((0,\infty)\) for
\[
0<a<\frac12
\quad\text{or}\quad
1<a<2.
\]

Remaining frontier:
\[
\frac12\le a\le1.
\]
This note is partial theory growth only. Do not stage as a full application unless the middle window is solved or the source question is explicitly narrowed.

## Advisor plan `20260531T214000-0300`

After the Bulboaca--Zayed compact-window solve, Advisor selected the remaining
Du--Wang middle window as a fresh low-hanging Gamma/\(\psi\) target away from
Erdos and already-public application material.  The source and first-contact
status are already satisfied by the cached Du--Wang source audit, so the new
nodes are internal refinements of the admitted \(h_{31}\) driver.

`AP-20260531T214000-du-wang-h3-middle-window` introduces three candidates:

- \(T\)-Du-Wang-h3-middle-window-increasing: prove that \(h_3\) is increasing
  for every \(1/2\le a\le1\);
- \(T\)-Du-Wang-h31-middle-window-u-monotonicity: set
  \(H_a(u)=h_{31}(a+u)\) and prove \(H_a'(u)\ge0\) from the nonnegative
  endpoint \(H_a(0+)=2\log\Gamma(a)\);
- \(T\)-Du-Wang-polygamma-ratio-halfline-bound: prove the reusable bound
  \[
  -\frac{2\psi''(t)}{\psi'''(t)}\ge t-\frac12,\qquad t>\frac12.
  \]

The intended chain is
\[
T\text{-Du-Wang-polygamma-ratio-halfline-bound}
\Rightarrow
T\text{-Du-Wang-h31-middle-window-u-monotonicity}
\Rightarrow
T\text{-Du-Wang-h3-middle-window-increasing}
\Rightarrow
T\text{-Du-Wang-h3-middle-window-open}.
\]

The next Student pass must begin with the Student Oracle gate for this concrete
Du--Wang middle-window target, then attack the derivative identity and
polygamma-ratio lemma analytically.

## Student outcome `20260531T220000-0300`

Student Oracle `ORACLE-OS-20260531T214200-du-wang-h3-middle-window` completed
live and proposed the halfline polygamma-ratio proof.  The local audit verified
the constants and the source derivative reduction.

For \(t>1/2\),
\[
-\frac{2\psi''(t)}{\psi'''(t)}>t-\frac12.
\]
Indeed, with \(S_m(t)=\sum_{n=0}^\infty(n+t)^{-m}\), one has
\(\psi''(t)=-2S_3(t)\) and \(\psi'''(t)=6S_4(t)\).  After writing
\(t=y+1/2\) and \(K(x)=(2\sinh(x/2))^{-1}\), the inequality reduces to the
positivity of
\[
\int_0^\infty e^{-yx}\frac{x^2K(x)}2
\left(\frac x2\coth\frac x2-1\right)\,dx,
\]
which follows from \(z\coth z>1\) for \(z>0\).

For \(1/2\le a\le1\) and \(H_a(u)=h_{31}(a+u)\),
\[
H_a'(u)=-u^2\{2\psi''(a+u)+u\psi'''(a+u)\}>0,
\]
because \(u=t-a\le t-1/2\).  Also
\[
H_a(0+)=2\log\Gamma(a)\ge0.
\]
Thus \(h_{31}(x+a)\ge0\), and the source identity
\[
h_3'(x)=\frac{h_{31}(x+a)}{x^2}
\]
proves that \(h_3\) is increasing on \((0,\infty)\) for every
\(1/2\le a\le1\).

Combining this middle-window theorem with the earlier outer-window theorem
classifies Du--Wang Open Problem 2:
\[
h_3 \text{ is increasing on }(0,\infty)
\quad\Longleftrightarrow\quad
\frac12\le a\le1,
\]
while \(h_3\) is not monotone for \(0<a<1/2\) or \(1<a<2\).  Local Theory node
`T-Du-Wang-h3-open-problem-2-classification` records the full source solve.
