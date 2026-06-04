# Incomplete-Beta Tail Bernstein Slice

Oracle forage `ORACLE-FI-20260529T-next-loop-026` selected a bounded incomplete-beta tail slice from the generalized Bernstein-functions source family.

For \(b>0\) and \(0<\lambda\le1\),
\[
I_{b,\lambda}(x)=B(b,\lambda)-B(b,\lambda;e^{-x})
=\int_0^x e^{-bt}(1-e^{-t})^{\lambda-1}\,dt
\]
is Bernstein. Its derivative is completely monotone:
\[
I_{b,\lambda}'(x)=e^{-bx}(1-e^{-x})^{\lambda-1}.
\]
For \(0<\lambda<1\), with \(c=1-\lambda\),
\[
I_{b,\lambda}'(x)=\sum_{n=0}^\infty \frac{(c)_n}{n!}e^{-(b+n)x}.
\]

This is a bridge theorem only. The full Koumandos--Pedersen generalized Bernstein class hierarchy is not locally reproved here.
