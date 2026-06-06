# Tao/Rogers finite-shadow log-upper transfer

## Status

Bounded Tao-framed bridge lemma, locally proved in
`raw/student/20260604T-tao-rogers-finite-shadow-log-upper-transfer.md`.

Oracle first-contact/advisory response accepted the target as a bridge lemma:
`oracle/responses/ORACLE-FC-20260604T-tao-rogers-finite-shadow-response.md`.

## Source

Terence Tao's blog post "Rogers' theorem on sieving" states Rogers' finite
sieve theorem: for fixed moduli \(q_i\), the finite survivor density after
deleting residue classes \(a_i\pmod {q_i}\) is maximized when all \(a_i=0\).

Source URL:
https://terrytao.wordpress.com/2026/01/19/rogers-theorem-on-sieving/

## Local theorem

For finite prefixes of an infinite residue sieve, write
\[
\delta_N(a)=\frac{1}{L_N}
\left|\{r\in\mathbb Z/L_N\mathbb Z:
r\not\equiv a_i\pmod {n_i}\text{ for }i\le N\}\right|.
\]
Then Rogers' theorem gives
\[
\delta_N(a)\le\delta_N(0)
\qquad(N\ge1).
\]
Combining this prefix inequality with the local finite-shadow reduction gives
\[
\overline d_{\log}B(a)\le \lim_{N\to\infty}\delta_N(0).
\]
If \(B(0)\) has logarithmic density equal to its finite-shadow limit, then
\[
\overline d_{\log}B(a)\le d_{\log}B(0).
\]
If \(B(a)\) also has logarithmic density, then
\[
d_{\log}B(a)\le d_{\log}B(0).
\]

## Boundaries

This result is an upper comparison only.  It does not prove that \(B(a)\) has
logarithmic density, and it does not solve Erdos Problem #25 in the remaining
positive-shadow case.  Future #25 progress still requires an actual
tail-continuity mechanism such as a residue-overlap, projection-balance, or
projection-energy invariant.
