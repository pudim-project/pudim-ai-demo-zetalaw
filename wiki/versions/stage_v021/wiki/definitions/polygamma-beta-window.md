# Polygamma Beta-Window Definitions

For \(n\ge1\), define
\[
C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x),
\qquad
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x),
\]
and
\[
\mathcal I_n=\{\beta\in\mathbb R:x^\beta C_n(x)-P_n(x)<0\text{ for all }x>0\}.
\]

The remaining active case is \(n=2\). For \(0<x<1\), set
\[
Q_2(x)=\frac{\log(P_2(x)/C_2(x))}{\log x},
\qquad
L_2=\sup_{0<x<1}Q_2(x).
\]

Using \(Z_s(a)=\sum_{k=0}^{\infty}(a+k)^{-s}\), the staged theory records
\[
R(x)=\frac{P_2(x)}{C_2(x)}
=
\frac{2Z_3(x)Z_3(1/x)}{3xZ_4(x)-Z_3(x)}
\]
and
\[
\Lambda(x)=
-\frac{3Z_4(x)}{Z_3(x)}
+\frac{3Z_4(1/x)}{x^2Z_3(1/x)}
-\frac{6Z_4(x)-12xZ_5(x)}
{3xZ_4(x)-Z_3(x)}.
\]

The derivative-sign target is
\[
G(x)=x\log x\,\Lambda(x)-\log R(x).
\]
