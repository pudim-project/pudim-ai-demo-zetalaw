# Frontier Note: Noncentral Chi-Square HCM Range

Source: Baricz--Prabhu--Singh--Vijesh, *Infinitely divisible modified Bessel distributions*, arXiv:2406.17721v2.

The source asks for the optimal parameter range in which
\[
\chi_{\mu,\lambda}(x)
=\frac12 e^{-(x+\lambda)/2}
\left(\frac{x}{\lambda}\right)^{\mu/4-1/2}
I_{\mu/2-1}(\sqrt{\lambda x})
\]
is hyperbolically completely monotone.

The local small-\(u\) hyperbolic-product expansion is
\[
\log\{\chi_{\mu,\lambda}(uv)\chi_{\mu,\lambda}(u/v)\}
=C_u+\frac{u}{2}\left(\frac{\lambda}{\mu}-1\right)w
-\frac{\lambda^2u^2}{4\mu^2(\mu+2)}(w^2-2)
+O(u^3),
\qquad w=v+v^{-1}.
\]

Consequences:
\[
\lambda>\mu\quad\Longrightarrow\quad \chi_{\mu,\lambda}\notin HCM,
\]
and
\[
(\lambda-\mu)^2<\frac{2\lambda^2}{\mu+2}
\quad\Longrightarrow\quad
\chi_{\mu,\lambda}\notin HCM.
\]

Equivalently, inside \(0<\lambda\le\mu\), the second obstruction excludes
\[
\frac{\lambda}{\mu}>
\frac{1}{1+\sqrt{2/(\mu+2)}}.
\]

Remaining frontier:
\[
0<\lambda\le\mu,\qquad
(\lambda-\mu)^2\ge\frac{2\lambda^2}{\mu+2}.
\]

This note is partial theory growth only. Do not stage as a solved application unless the full optimal HCM range is proved or the source problem is explicitly narrowed.
