# Tao-Sendov annular structural alternatives

Status: partial source progress.

This note continues the Tao-Sendov effectivization branch after the near-origin explicit window. It does not prove a global explicit \(n_0\) and does not prove a true annular Sendov window.

If Sendov fails at a simple zero \(a\), then evaluating the critical-point product identity at \(a\) gives
\[
\prod_{i=2}^n |a-z_i|>n.
\]
This single inequality yields three explicit structural alternatives:

- far-zero count lower bounds;
- order-statistic distance certificates;
- logarithmic opposite-cap forcing near the boundary.

The strongest cap statement is:
\[
\#\left\{i\ge2:\Re(e^{-i\theta}z_i)\le\frac{|a|}{2}\right\}
\ge
\left\lfloor
\frac{\log n}{\log(1+|a|)}
\right\rfloor+1,
\qquad a=|a|e^{i\theta}.
\]
In particular, any near-boundary failure forces at least \(\lfloor\log_2 n\rfloor+1\) other zeros into the fixed opposite cap
\[
\Re(e^{-i\theta}z)\le\frac12.
\]

Next frontier:

\[
T\text{-Tao-Sendov-cap-geometry-to-critical-point}.
\]

The missing step is to turn forced opposite-cap zero geometry into a critical point inside \(\overline{D(a,1)}\).

Artifacts:

- Attack plan: `.pudim/attack-plans/AP-20260604T-tao-sendov-annular-explicit-window.json`
- Oracle Student: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-sendov-annular-student-response.md`
- Proof note: `.pudim/raw/student/20260604T-tao-sendov-annular-structural-alternatives.md`
