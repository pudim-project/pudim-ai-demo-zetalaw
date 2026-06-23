# Frontier: Bulboaca--Zayed Gamma Quotient Monotonicity

Scout forage `FI-20260528T-next-loop-007` selected the fresh 2026 Bulboaca--Zayed Gamma quotient problem.

The source proves strict decrease on \((-1,1)\) for
\[
F(x)=
\frac{\log\Gamma(x+1)}
{\log(x^2+6)-\log(x+6)}.
\]

It then asks for an analytic proof of the numerically observed full pattern for the continuous extension \(\widetilde F\) on \((-1,\infty)\): \(\widetilde F'\) should have exactly one zero \(x_m\simeq1.126207061\ldots\), with \(\widetilde F'<0\) to the left and \(\widetilde F'>0\) to the right.

The local Theory fit is through \(\log\Gamma\), \(\psi\), rational derivative signs, endpoint asymptotics, and interval certificates. This is a new author/problem family and is not a zeta-tail parameter increment.

Bounded Student scope: first prove the derivative-sign normal form and attempt at most one right-tail or critical-window certificate. Rotate if the proof turns into a broad global derivative-sign grind.

## Student/Librarian outcome `20260528T131000Z`

Student proved the derivative-sign normal form:
\[
\operatorname{sgn}\widetilde F'(x)
=
\operatorname{sgn}N(x),
\]
where
\[
N(x)=
(x+6)(x^2+6)\psi(x+1)(\log(x^2+6)-\log(x+6))
-(x^2+12x-6)\log\Gamma(x+1).
\]

Student also proved a coarse right-tail certificate:
\[
\widetilde F'(x)>0
\qquad (x\ge8).
\]

The full one-critical-point problem remains open. The compact interval \((-1,8]\) was not attacked in this pass.

## Advisor pivot `20260531T211500-0300`

After the Erdos 536 branch reached a route-unripe state, Advisor selected this
frontier as a low-hanging theory-growth target in the existing
Gamma/\(\psi\)/interval-certificate layer.  The old source-sufficient node
\(T\)-BZ-gamma-quotient-critical-window-reduction is now attacked by
`AP-20260531T211500-bz-gamma-critical-window` with three candidates:

- \(T\)-BZ-gamma-quotient-N-single-crossing-one-eight: prove that the existing
  derivative numerator \(N\) has exactly one crossing on \([1,8]\);
- \(T\)-BZ-gamma-quotient-polygamma-envelope-critical-certificate: build a
  finite rational cover using \(\log\Gamma\), \(\psi\), \(\psi'\), and logarithm
  enclosures;
- \(T\)-BZ-gamma-quotient-critical-window-diagnostic-obstruction-map: if the
  proof stalls, isolate the hard subinterval or a genuine obstruction.

The next Student pass must start with the Student Oracle gate for this concrete
non-blocklisted target before local proof work.

## Student outcome `20260531T213200-0300`

Student Oracle `ORACLE-OS-20260531T211700-bz-gamma-critical-window` completed
live and suggested a ratio-kernel proof.  The local Student audit verified it.
With
\[
G(x)=\log\Gamma(x+1),\qquad
D(x)=\log\frac{x^2+6}{x+6},\qquad
N_0(x)=\psi(x+1)D(x)-G(x)D'(x),
\]
the derivative numerator \(N\) from the earlier normal form is a positive
multiple of \(N_0\) on \(x>1\).  Set
\[
r(x)=\frac{\psi(x+1)}{D'(x)}.
\]
Writing \(P=x^2+12x-6\), \(Q=(x^2+6)(x+6)\), one has
\[
P(x)^2r'(x)=S(x),
\]
where
\[
S(x)=\psi'(x+1)Q(x)P(x)+\psi(x+1)\{Q'(x)P(x)-Q(x)P'(x)\}.
\]
Elementary bounds for \(\psi,\psi'\), and \(\psi''\) show \(S'(x)>0\) on
\([1,8]\), while \(S(1)<0<S(8)\).  Hence \(r\) decreases once and then
increases.  Since \(I(x)=D(x)r(x)-G(x)\) satisfies \(I'(x)=D(x)r'(x)\),
\(\lim_{x\downarrow1}I(x)=0\), and \(I(8)>0\), the numerator \(N\) has exactly
one zero on \((1,8]\).  This proves the compact critical-window reduction.

The source already proves \(\widetilde F'<0\) on \((-1,1)\), and the previous
local theorem proves \(\widetilde F'>0\) for \(x\ge8\).  Therefore
`T-Bulboaca-Zayed-gamma-quotient-full-monotonicity` is now true.  The unique
zero is numerically
\[
x_m=1.12620706105164346558\ldots.
\]
