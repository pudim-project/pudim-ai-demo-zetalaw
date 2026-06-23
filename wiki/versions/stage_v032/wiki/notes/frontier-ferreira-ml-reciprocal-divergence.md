# Frontier Note: Ferreira Reciprocal-Integer Mittag-Leffler Divergence

Status: solved reciprocal-integer bridge; all-\(\alpha\) elementary problem remains open.

Ferreira asks for an elementary proof, avoiding complex analytic methods and the known integral representation, of the divergence of
\[
\int_0^\infty e^{-t}E_\alpha(-\lambda t^\alpha)\,dt
\]
for \(\lambda\le -1\). The source highlights the inequality
\[
E_\alpha(t^\alpha)>e^t \qquad (t>0)
\]
as the key comparison.

For \(\alpha=1/m\), \(m\ge2\), the series splits into residue classes modulo \(m\):
\[
E_{1/m}(t^{1/m})=e^t+
\sum_{r=1}^{m-1}\sum_{j=0}^{\infty}
\frac{t^{j+r/m}}{\Gamma(j+r/m+1)}.
\]
The residual sum is strictly positive for \(t>0\), so
\[
E_{1/m}(t^{1/m})>e^t.
\]
For \(\lambda\le -1\), write \(a=-\lambda\ge1\). If \(a>1\), the \(k=mj\) subsequence gives
\[
E_{1/m}(a t^{1/m})\ge e^{a^m t},
\]
and the Laplace integral diverges. If \(a=1\), the strict inequality gives an integrand greater than \(1\).

The mechanism is intentionally not promoted to the full all-\(\alpha\) problem. For \(\alpha=p/q\) with \(p>1\), the obvious subsequence has denominators \(\Gamma(1+pj)\), not \(j!\), so the direct exponential block is lost.
