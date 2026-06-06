# Frontier: Yang--Tian Bessel Ratio Bernstein Conjecture

Scout forage `FI-20260528T-next-loop-010` selected Conjecture 3 from Yang--Tian on the modified Bessel ratio
\[
W_\nu(x)=\frac{xI_\nu(x)}{I_{\nu+1}(x)}.
\]

The source conjectures that for \(\tau\in(0,1/2]\) and \(\nu>-1\),
\[
x\mapsto W_\nu(x^\tau)
\]
is a Bernstein function on \((0,\infty)\).

This branch is not a continuation of the reciprocal zeta-tail, YHL \(k\)-digamma, GGPS boundary, or Bulboaca--Zayed Gamma quotient problems. It grows the local Theory toward Bessel ratios, Bernstein functions, and endpoint asymptotic obstructions.

The bounded Student target is to prove the small-\(x\) expansion and use it only to show that \(\tau>1/2\) is impossible for nonconstant Bernstein behavior. The full conjectural range \(\tau\in(0,1/2]\) remains open unless a short complete-Bernstein/Stieltjes representation appears immediately.

## Student/Librarian outcome `20260528T141000Z`

Student proved the endpoint expansion
\[
W_\nu(z)=2(\nu+1)+\frac{z^2}{2(\nu+2)}+O(z^4)
\qquad(z\to0^+,\ \nu>-1).
\]
Consequently, for
\[
F_{\nu,\tau}(x)=W_\nu(x^\tau),
\]
one has
\[
F_{\nu,\tau}'(x)=\frac{\tau}{\nu+2}x^{2\tau-1}+O(x^{4\tau-1}).
\]
If \(\tau>1/2\), then \(F_{\nu,\tau}'(0^+)=0\). A Bernstein function has completely monotonic derivative; hence \(F_{\nu,\tau}'\) would be nonnegative and nonincreasing. A nonnegative nonincreasing function with right endpoint limit \(0\) must be identically zero, contradicting the positive local expansion.

Thus \(x\mapsto W_\nu(x^\tau)\) is not a nonconstant Bernstein function for \(\tau>1/2\). This proves sharpness against extending the source's exponent range.

## 20260603 Full Conjecture Update

Student pass `20260603T-yang-tian-bessel-w-full-conjecture` solves the full source range. For every \(\nu>-1\),
\[
W_\nu(\sqrt s)
=2(\nu+1)+2\sum_{n=1}^{\infty}\frac{s}{s+j_{\nu+1,n}^2},
\]
so
\[
\frac{d}{ds}W_\nu(\sqrt s)
=2\sum_{n=1}^{\infty}\frac{j_{\nu+1,n}^2}{(s+j_{\nu+1,n}^2)^2}
\]
is completely monotone. Thus \(W_\nu(\sqrt s)\) is Bernstein, and composition with \(x^{2\tau}\) proves \(x\mapsto W_\nu(x^\tau)\) Bernstein for \(0<\tau\le1/2\). This closes Yang--Tian Conjecture 3 and upgrades the branch from endpoint sharpness to source-open solved.
