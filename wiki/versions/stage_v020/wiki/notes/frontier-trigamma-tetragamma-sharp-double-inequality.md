# Frontier: Trigamma-Tetragamma Sharp Double Inequality

## Source

Qi and Agarwal, "On complete monotonicity of several functions involving the gamma and psi functions", Journal of Inequalities and Applications 2019, article 68.

Source URL: https://journalofinequalitiesandapplications.springeropen.com/counter/pdf/10.1186/s13660-019-1976-z.pdf

The source's seventh open problem asks for the sharp exponent window in a double inequality for
\[
\Delta(x)=(\psi'(x))^2+\psi''(x),\qquad x>0.
\]

Follow-up literature check: Ladislav Matejicka, "A Solution to Qi's Conjecture on a Double Inequality for a Function Involving the Tri- and Tetra-Gamma Functions", Mathematics 7(11), 1098, 2019, DOI https://doi.org/10.3390/math7111098, proves this exact seventh open problem. The article states that the double inequality holds on \((0,\infty)\) if and only if \(\alpha\ge6/5\) and \(\beta\le1\).

Therefore this item is also not a fresh open problem. The local endpoint and rationalized-reduction nodes remain useful theory growth, but the active open-problem run should rotate.

## Normalized Form

Set
\[
A(x)=\frac{x^2+4x+12}{12(x+1)^2},
\qquad
D(x)=x^4\Delta(x).
\]
The source inequality is equivalent to the sharp two-sided bound
\[
A(x)^{6/5}<D(x)<A(x),
\qquad x>0,
\]
plus the endpoint sharpness conditions that force \(\alpha\ge6/5\) and \(\beta\le1\).

Since \(0<A(x)<1\), a Q-style logarithmic normal form is
\[
Q_\Delta(x)=\frac{\log D(x)}{\log A(x)}.
\]
The sharp bound becomes
\[
1<Q_\Delta(x)<\frac65.
\]

Numerical first contact supports the endpoint pattern
\[
\lim_{x\to0^+}Q_\Delta(x)=\frac65,
\qquad
\lim_{x\to\infty}Q_\Delta(x)=1,
\]
with \(Q_\Delta\) decreasing in sampled points. This was useful for a local bridge, but the global source theorem is already closed by Matejicka 2019.

## Rotation Rule

This branch should not consume more open-problem time unless the user explicitly asks to reprove or import Matejicka's theorem. Rotate to the reciprocal zeta-tail candidate and require a reusable enclosure pattern rather than a routine next case.
