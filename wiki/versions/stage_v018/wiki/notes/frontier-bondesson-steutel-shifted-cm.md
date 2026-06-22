# Frontier Note: Bondesson--Steutel Shifted Complete Monotonicity

Source: Lennart Bondesson and Fred Steutel, "A class of infinitely divisible distributions connected to branching processes and random walks", JMAA 295(1), 134--143, 2004.

Pudim source note: `raw/scout/sources/bondesson-steutel-branching-hcm-open-problem.md`

## Source Frontier

The source asks whether a shifted complete-monotonicity property, known in the \(c=1/2\) case and supported numerically, holds for the full family \(c\in(0,1]\) and all shifts \(N\ge0\).

Pudim records this as:

- `T-Bondesson-Steutel-shifted-CM-conjecture`
- `T-BS-all-c-all-N-shifted-frontier`

## Local Bridge Proved

At \(c=1/2\), the pgf
\[
P(z)=\frac{1-\sqrt{1-z}}{z}
\]
has coefficients
\[
P_n(1/2)=\frac{C_n}{2\cdot4^n}.
\]

The Student pass proved the Hausdorff representation
\[
P_n(1/2)=\frac1\pi\int_0^1 x^{n-1/2}(1-x)^{1/2}\,dx.
\]

It also proved complete monotonicity of the canonical \(r\)-sequence:
\[
r_n=(n+1/2)P_n(1/2)
=\frac{1}{2\pi}\int_0^1 x^{n+1/2}(1-x)^{-1/2}\,dx.
\]

Equivalently,
\[
r_n=\int_0^1 x^n\,d\nu(x),
\qquad
d\nu(x)=\frac{1}{2\pi}x^{1/2}(1-x)^{-1/2}\,dx.
\]

## Status

True:

- `T-BS-c-half-Catalan-Hausdorff-representation`
- `T-BS-c-half-canonical-r-sequence-CM`

Open:

- `T-Bondesson-Steutel-shifted-CM-conjecture`
- `T-BS-all-c-all-N-shifted-frontier`

Rotation note: do not continue by proving isolated higher \(N\) or isolated \(c\) cases. A future pass must produce a uniform Buermann--Lagrange/Hausdorff kernel mechanism or forage another source.
