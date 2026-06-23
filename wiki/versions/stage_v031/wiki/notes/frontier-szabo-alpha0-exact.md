# Frontier Note: Szabo Psi-Difference Exact Cutoff

Status: solved locally, with cited source sufficiency import.

Szabo Open Problem 1.5 asks for the sharp \(\alpha_0\) such that, for \(a\ge0\), \(b>0\), \(0<b-a<1\),
\[
f_\alpha(x)=(x+a)^\alpha\left[\psi(x+b)-\psi(x+a)-\frac{b-a}{x+a}\right]
\]
is strictly completely monotone on \((-a,\infty)\) iff \(\alpha\le\alpha_0\).

Set \(y=x+a\) and \(d=b-a\). Then
\[
H_d(y)=\psi(y+d)-\psi(y)-\frac{d}{y}
=\frac{1-d}{y}+O(1)
\qquad (y\downarrow0).
\]
Thus, for \(\alpha>1\),
\[
\frac{d}{dy}\left(y^\alpha H_d(y)\right)>0
\]
near \(0^+\), contradicting the nonincreasing condition required of completely monotone functions. Therefore every admissible \(\alpha\) satisfies \(\alpha\le1\).

Szabo explicitly records that the older proof of the sufficiency side for \(\alpha\le1\) is correct, while the old necessity proof was invalid. Importing that accepted sufficiency and adding the local endpoint obstruction gives
\[
\alpha_0=1.
\]

The previous local node `T-Szabo-psi-difference-alpha0-below-two` is now subsumed by the exact cutoff. The exact Szabo branch is hard-blocked for future forage; the loop should rotate to different source families.
