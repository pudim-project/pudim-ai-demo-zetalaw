# Tao Erdos #385 semiprime-gap implication

Status: source-conditional bridge.

Let
\[
F(n)=
\max_{\substack{m<n\\ m\ \mathrm{composite}}}
\bigl(m+p(m)\bigr),
\]
where \(p(m)\) is the least prime factor of \(m\).

Fix \(2<u<3\). Suppose restricted semiprimes \(m=pq\in[X,2X]\), with
\[
p,q\in[X^{1/u},(2X)^{1-1/u}],
\]
have maximal gaps
\[
G(X)=o(X^{1/u}).
\]
Then
\[
F(n)-n\to\infty,
\]
and hence \(F(n)>n\) for all sufficiently large \(n\).

Proof sketch: set \(X=n/2\), and use the endpoint-safe interval
\[
[n-2G(X),\,n-G(X)]\subseteq[X,2X].
\]
It contains a restricted semiprime \(m=pq<n\). Then
\[
n-m\le2G(X),
\qquad
p(m)\ge X^{1/u},
\]
so
\[
F(n)-n\ge m+p(m)-n
\ge X^{1/u}-2G(X)\to\infty.
\]

This records Tao's reduction as a formal theorem. It is not an unconditional semiprime-gap theorem.

Primary proof artifact: `.pudim/raw/student/20260604T-tao-erdos385-semiprime-gap-implication.md`.

Oracle artifact: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-erdos385-semiprime-gap-implication-student-response.md`.
