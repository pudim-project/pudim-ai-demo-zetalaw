# Tao adjoint upward von Mangoldt chain: heavy-tail law

Status: bounded source-backed bridge theorem.

This note records a quantitative corollary of Tao's von Mangoldt-chain framework. It is source-backed by the adjoint-chain construction and the invariant weight, but it is not a source-open primitive-set result.

For \(m>1\),
\[
\nu_\Lambda(m)=\int_1^\infty \frac{\log m}{\zeta(s)m^s}\,ds.
\]
For \(n>1\), the adjoint upward jump from \(n\) to \(nq\) has multiplier law
\[
K_n(q)
=
\frac{\nu_\Lambda(nq)}{\nu_\Lambda(n)}
\frac{\Lambda(q)}{\log(nq)},
\qquad q\ge2.
\]

The invariant-weight identity gives
\[
\sum_{q\ge2}K_n(q)=1.
\]

There are absolute constants \(0<c<C<\infty\) such that
\[
c\,\frac{(\log n)\Lambda(q)}{q(\log(nq))^2}
\le
K_n(q)
\le
C\,\frac{(\log n)\Lambda(q)}{q(\log(nq))^2}.
\]
The input estimate is
\[
\frac{c_0}{m\log m}\le\nu_\Lambda(m)\le\frac1{m\log m},
\qquad m\ge2,
\]
which follows from
\[
\frac{s-1}{s}\le\frac1{\zeta(s)}\le s-1.
\]

Consequently, for every fixed \(n>1\),
\[
\sum_{q\ge2}K_n(q)\log q=\infty.
\]
Indeed, prime jumps \(q=p\ge n\) contribute at least a constant multiple of \((\log n)/p\), and \(\sum_p1/p=\infty\).

Using the prime number theorem, the fixed-\(n\) multiplier tail is
\[
\sum_{q\ge Q}K_n(q)
\sim
\frac{1}{n\nu_\Lambda(n)\log(nQ)}
\qquad(Q\to\infty).
\]

Interpretation: the adjoint upward von Mangoldt chain makes finite jumps almost surely, but its one-step logarithmic jump has infinite expectation.

Primary artifacts:

- Oracle response: `.pudim/oracle/responses/ORACLE-FC-20260604T-tao-adjoint-upward-heavy-tail-response.md`
- Student proof: `.pudim/raw/student/20260604T-tao-adjoint-upward-heavy-tail.md`
- Theory node: `.pudim/theory/nodes/T-Tao-adjoint-von-Mangoldt-upward-chain-heavy-tail.json`
