# Frontier Note: Szabo Psi-Difference Threshold

Source: V. E. S. Szabo, *Completely monotone functions in general and some applications*, arXiv:2411.17670.

Szabo discusses the function
\[
f_\alpha(x)=(x+a)^\alpha\left[\psi(x+b)-\psi(x+a)-\frac{b-a}{x+a}\right],
\]
where \(a\ge0\), \(b>0\), and \(0<b-a<1\), and asks for the sharp \(\alpha_0\) such that \(f_\alpha\) is strictly completely monotone on \((-a,\infty)\) iff \(\alpha\le\alpha_0\).

The local partial result sets \(d=b-a\), \(y=x+a\), and
\[
k_d(t)=\frac{1-e^{-dt}}{1-e^{-t}}-d.
\]
Then
\[
\psi(y+d)-\psi(y)-\frac{d}{y}=\int_0^\infty e^{-yt}k_d(t)\,dt.
\]
For the endpoint \(\alpha=2\), the inverse Laplace distribution is
\[
\frac{d(1-d)}2\delta_0+k_d''(t)\,dt,
\]
and \(k_d''(t)=-d^2e^{-dt}+O(e^{-t})<0\) eventually. Hence the endpoint \(\alpha=2\) is not completely monotone for any \(0<d<1\).

Status update 2026-05-31: solved by `T-Szabo-psi-difference-alpha0-exact-one`. The endpoint Laurent expansion proves all \(\alpha>1\) inadmissible, and Szabo's source supplies the accepted sufficiency direction for \(\alpha\le1\). Hence \(\alpha_0=1\). See `wiki/notes/frontier-szabo-alpha0-exact.md`.
