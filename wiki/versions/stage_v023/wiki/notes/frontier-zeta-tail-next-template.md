# Frontier: Reciprocal Zeta-Tail Floor Template Beyond s=8

## Source

Kim and Song, "The inverses of tails of the Riemann zeta function", Journal of Inequalities and Applications 2018, article 157.

Source URL: https://link.springer.com/article/10.1186/s13660-018-1743-6

Pan and Wu, "The inverse of tails of Riemann zeta function, Hurwitz zeta function and Dirichlet L-function", AIMS Mathematics 9(6), 16564--16585, 2024.

Source URL: https://doi.org/10.3934/math.2024803

The staged Theory already proves exact floor formulas for \(\lfloor\zeta_n(7)^{-1}\rfloor\) and \(\lfloor\zeta_n(8)^{-1}\rfloor\). The remaining useful target is not merely "do \(s=9\)", but extract a reusable enclosure template for further integer exponents.

## Current Tools

The staged \(s=7\) proof uses a rational telescoping window
\[
P(n)-\varepsilon<T_7(n)^{-1}<P(n)
\]
and a residue gap argument for \(\lfloor P(n)\rfloor\).

The staged \(s=8\) proof uses adjacent asymptotic approximants \(A_8(n)<T_8(n)^{-1}<B_8(n)\), exact telescoping inequalities for \(1/A_8\) and \(1/B_8\), and a finite-plus-modular gap check.

## Attack Policy

Admit C004 only if the next run searches for a reusable mechanism:

- an Euler--Maclaurin inverse-tail approximant generator;
- a deterministic telescoping sign-certificate generator;
- a modular or finite gap trap showing the interval between \(A_s(n)\) and \(B_s(n)\) contains no integer.

A one-off \(s=9\) formula without reusable certificate machinery should be treated as too routine for this forage rotation.

## Student Outcome

The Student pass produced the reusable template and the next exact case. It symbolically inverted the Euler--Maclaurin tail series, recovered the staged \(s=8\) approximant coefficients, and generated \(A_9,B_9\) with exact telescoping residual certificates.

For
\[
T_9(n)=\zeta_n(9),
\]
the new formula is
\[
\left\lfloor T_9(n)^{-1}\right\rfloor=\lfloor A_9(n)\rfloor
\qquad(n\ge9),
\]
where
\[
\begin{aligned}
A_9(n)=&8n^8-32n^7+80n^6-128n^5+120n^4-64n^3
+\frac{624}{7}n^2-\frac{512}{7}n-\frac{3324}{7}\\
&+\frac{90304}{21n^2}+\frac{90304}{21n^3}
-\frac{10280944}{245n^4}-\frac{64846304}{735n^5}
+\frac{109940976}{245n^6}.
\end{aligned}
\]
For \(1\le n\le8\), the exact floors are
\[
\begin{array}{c|rrrrrrrr}
n&1&2&3&4&5&6&7&8\\
\hline
\lfloor T_9(n)^{-1}\rfloor&0&497&18093&224086&1543530&7360226&27295287&84349541.
\end{array}
\]

Replay artifacts:

- `raw/student/20260527T233000-zeta-tail-template.md`
- `raw/student/20260527T233000-zeta-tail-template-check.py`
- `librarian/audits/LA-20260527T234000-zeta-tail-s9-ingest.json`
