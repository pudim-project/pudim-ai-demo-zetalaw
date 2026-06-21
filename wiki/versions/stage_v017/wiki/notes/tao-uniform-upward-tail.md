# Uniform upward tail for Tao's adjoint von Mangoldt chain

Status: bounded source-backed bridge theorem.

This note strengthens the fixed-\(n\) tail asymptotic for the adjoint upward von Mangoldt chain to a uniform logarithmic tail estimate.

For \(n>1\), let
\[
K_n(q)
=
\frac{\nu_\Lambda(nq)}{\nu_\Lambda(n)}
\frac{\Lambda(q)}{\log(nq)}
\]
be the adjoint upward jump-multiplier law. Define
\[
T_n(Q)=\sum_{q\ge Q}K_n(q).
\]
Then, uniformly for all \(n>1\) and \(Q\ge2\),
\[
T_n(Q)\asymp\frac{\log n}{\log(nQ)}.
\]

The proof reduces to
\[
\sum_{q\ge Q}\frac{\Lambda(q)}{q(\log(nq))^2}
\asymp
\frac1{\log(nQ)}.
\]
The upper bound follows from dyadic decomposition and \(\psi(x)\ll x\). The lower bound uses a fixed annulus factor \(B>A/a\), where \(ax\le\psi(x)\le Ax\), so that
\[
\psi(BX)-\psi(X)\ge(aB-A)X.
\]
Summing annular contributions over \(X=QB^j\) gives the matching lower scale.

No PNT is needed; Chebyshev bounds suffice.

Primary artifacts:

- Oracle response: `private Oracle response`
- Student proof: `private proof note`
- Theory node: `private artifact`
