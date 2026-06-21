# Tao von Mangoldt chain invariant weight

Status: bounded source-backed bridge theorem.

This note records a local zeta-law formalization of the invariant weight in Tao's von Mangoldt-chain framework. It is not a new source-open theorem; the Oracle gate classified it as a clean extraction of Tao/arXiv Example 2.8 with useful endpoint bookkeeping.

For \(s>1\), let
\[
\rho_s(n)=\frac{1}{\zeta(s)n^s}.
\]
For \(n>1\), define
\[
\nu_\Lambda(n)=\int_1^\infty \frac{\log n}{\zeta(s)n^s}\,ds.
\]
The downward transition from \(nq\) to \(n\) is
\[
P(nq\searrow n)=\frac{\Lambda(q)}{\log(nq)},\qquad q\ge2.
\]
Then
\[
\nu_\Lambda(n)
=
\sum_{q\ge2}\nu_\Lambda(nq)\frac{\Lambda(q)}{\log(nq)}
\]
for every \(n>1\).

The proof is the zeta-law Euler-score identity integrated in \(s\). With \(F_n(s)=n^{-s}/\zeta(s)\),
\[
\sum_{q\ge2}\Lambda(q)\rho_s(nq)
=
F_n(s)\left(-\frac{\zeta'}{\zeta}(s)\right)
=
F_n'(s)+(\log n)F_n(s).
\]
Integrating from \(1\) to \(\infty\) kills the boundary term because \(F_n(1^+)=F_n(\infty)=0\) for \(n>1\).

Finite-window form:
\[
\sum_{q\ge2}\nu_{\alpha,\beta}(nq)\frac{\Lambda(q)}{\log(nq)}
=
\nu_{\alpha,\beta}(n)+\rho_\beta(n)-\rho_\alpha(n),
\qquad
1<\alpha<\beta<\infty.
\]

Infinitesimal form:
\[
\partial_s\rho_s(n)
=
\sum_{q\ge2}\Lambda(q)\rho_s(nq)-(\log n)\rho_s(n).
\]

Boundary: the identity is not valid at \(n=1\) without an absorbing-boundary convention. The parent inflow into \(1\) equals \(1\), while the displayed integral gives \(\nu_\Lambda(1)=0\).

Primary artifacts:

- Oracle response: `private Oracle response`
- Student proof: `private proof note`
- Theory node: `private artifact`
