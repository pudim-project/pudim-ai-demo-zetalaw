# Frontier Note: From Mills-Ratio General-L Bounds

Source: Steven G. From, "Some new upper and lower bounds for the Mills ratio", JMAA 486(1), 123872, 2020.

Pudim source note: `private scout artifact`

## Source Frontier

From's paper asks for a general theorem/proof behind Mills-ratio bounds obtained by replacing \(r(t)\) with \((-1)^L r^{(L)}(t)\) in complete-monotonicity determinant inequalities, uniformly for \(L\ge1\).

Pudim records this as:

- `T-From-Mills-general-L-bound-theorem-open-problem`
- `T-From-Mills-explicit-bound-family-frontier`

## Local Bridge Proved

The bounded Student pass proved the Laplace normal form
\[
r(t)=\int_0^\infty e^{-tu-u^2/2}\,du,
\]
so \(r\) is completely monotone.

It also proved
\[
r'(t)=tr(t)-1
\]
and the recurrence
\[
P_{n+1}=P_n'+tP_n,\qquad Q_{n+1}=Q_n'-P_n
\]
for \(r^{(n)}=P_nr+Q_n\).

Finally, for every \(L\ge0\), the tilted kernel
\[
f_L(t)=(-1)^Lr^{(L)}(t)=\int_0^\infty u^L e^{-tu-u^2/2}\,du
\]
gives
\[
r^{(L+4)}r^{(L)}-4r^{(L+3)}r^{(L+1)}+3(r^{(L+2)})^2\ge0.
\]

The proof reduces the determinant to
\[
\mathbb E[(X-\mu)^4]+3\operatorname{Var}(X)^2\ge0
\]
under the probability measure proportional to \(u^L e^{-tu-u^2/2}du\).

## Status

True:

- `T-From-Mills-Laplace-CM-normal-form`
- `T-From-Mills-derivative-polynomial-recurrence`
- `T-From-Mills-derivative-determinant-all-L`
- `T-From-Mills-all-L-moment-ratio-quadratic-bound`
- `T-From-Mills-all-L-alternating-r-bound-family`
- `T-From-Mills-general-L-bound-theorem-open-problem`

Solved extraction:

For
\[
M_L(t)=(-1)^Lr^{(L)}(t)=\int_0^\infty u^L e^{-tu-u^2/2}\,du,
\]
set \(m_L=M_{L+1}/M_L\). The recurrence \(M_{n+1}=nM_{n-1}-tM_n\), inserted into the all-\(L\) determinant bridge, gives
\[
(t^2+4L+8)m_L^2+t(t^2+4L+7)m_L-(L+1)(t^2+4L+6)<0.
\]
Thus \(m_L<U_L\), where \(U_L\) is the positive root of this quadratic. The recurrence representation \(M_n=(-1)^nP_nr+B_n\) then gives an explicit alternating lower/upper bound family for \(r(t)\). Even \(L\) gives lower bounds; odd \(L\) gives upper bounds. The cases \(L=0\) and \(L=1\) reproduce From's displayed bounds, and the formula works uniformly for every \(L\ge0\).

Rotation note: do not continue by grinding individual \(L\) values. This frontier is solved at the uniform-extractor level. Future Mills work should either stage this as an application when requested or move to a genuinely new source-open Mills problem.
