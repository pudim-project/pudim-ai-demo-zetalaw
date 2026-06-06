# Qi--Agarwal/Yin Divisor-Polygamma Parity Problem

For \(n\in\mathbb N\), define
\[
f_n(x)=\sum_{km=n}\bigl[\psi^{(k)}(x)\bigr]^m.
\]
Qi--Agarwal Problem 12.6 asks to prove an odd/even parity law:

- \(f_{2\ell-1}\) should be completely monotonic;
- \(f_{2\ell}\) should not be completely monotonic.

The odd half is true. If \(n\) is odd and \(km=n\), then \(k,m\) are odd. Since \(\psi^{(k)}\) is positive completely monotone for odd \(k\), every summand \([\psi^{(k)}]^m\) is completely monotone by finite product closure, and the finite sum is completely monotone.

The even half is false as stated:
\[
f_2(x)=[\psi'(x)]^2+\psi''(x).
\]
The same source records the theorem that \([\psi']^2+\lambda\psi''\) is completely monotone if and only if \(\lambda\le1\). Therefore \(f_2\) is completely monotone.

Current status:

- true: \(f_n\in CM(0,\infty)\) for every odd \(n\);
- true: \(f_2\in CM(0,\infty)\);
- true: the source even-parity clause is refuted at \(n=2\);
- open: whether \(f_n\notin CM(0,\infty)\) for every even \(n\ge4\).

The corrected frontier is useful because it isolates a divisor-indexed polygamma CM mechanism and a likely asymptotic obstruction for even orders.
