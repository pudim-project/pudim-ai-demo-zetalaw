# APP-0010: Nielsen \(k\)-Beta Derivative-Ratio Monotonicity

## Status

Solved in the local Pudim v2 Theory graph; pending any future user-invoked staging pass.

## Source Problem

Yin--Zhang ask for monotonicity of
\[
\frac{(x\beta_k(x))^{(n+1)}}{(x\beta_k(x))^{(n)}(x\beta_k(x))^{(n+2)}}
\]
for \(k>0\), \(n\in\mathbb N\), and \(x>0\).

## Resolution

The precise parity law is:

- odd \(n\): the ratio is strictly increasing;
- even \(n\): the ratio is strictly decreasing.

The proof depends on the admitted bridge node `T-CM-Laplace-moment-ratio-monotonicity` and the specialization edge `E-CM-moment-ratio-implies-Nielsen-k-beta`.

## Theory Nodes

- `T-CM-Laplace-moment-ratio-monotonicity`
- `T-Nielsen-k-beta-derivative-ratio-monotonicity`
- `T-Yin-Zhang-Nielsen-k-beta-open-problem-resolved`
