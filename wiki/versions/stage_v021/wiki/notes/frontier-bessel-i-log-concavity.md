# Frontier: Bessel \(I_\nu\) Square-Root Log-Concavity

## Source Node

The fresh source node is
\[
T\text{-Bessel-I-sqrt-log-concavity-nu-ge-0}:
\qquad
\forall \nu\ge0,\quad u\mapsto \sqrt{u}\,I_\nu(u)
\text{ is strictly log-concave on }(0,\infty).
\]

It came from Scout forage item `FI-20260526T122752Z-C001`, grounded in the modified-Bessel open-problems source `arXiv:1009.4814`. No external solution is imported.

## Advisor Attack Plans

`AP-20260526T123243-Bessel-I-log-concavity` creates three open candidates:

1. `T-Bessel-I-Riccati-log-concavity-inequality`.
   Let \(r_\nu(u)=I_\nu'(u)/I_\nu(u)\). Prove
   \[
   1+\frac{\nu^2-\frac12}{u^2}-\frac{r_\nu(u)}{u}-r_\nu(u)^2<0.
   \]
   This is the wide/equivalent normal form exposed by the modified-Bessel differential equation.

2. `T-Bessel-I-ratio-quadratic-bound`.
   Let \(q_\nu(u)=I_{\nu+1}(u)/I_\nu(u)\). Prove
   \[
   q_\nu(u)^2+\frac{2\nu+1}{u}q_\nu(u)+\frac{\nu+\frac12}{u^2}>1.
   \]
   This is the Turan/log-derivative route, using \(r_\nu=q_\nu+\nu/u\).

3. `T-Bessel-I-split-regime-log-concavity-certificate`.
   Prove the Riccati inequality by a small-\(u\), large-\(u\), and certified compact-middle split.

The first Student execution should verify the Riccati equivalence and then try the ratio-bound route before falling back to split-regime certification.

## Student Refutation

Student roll `20260526T124356` refutes the source node at \(\nu=0,u=10\). With
\[
r_0(10)=\frac{I_1(10)}{I_0(10)},
\]
the exact rational certificate proves
\[
r_0(10)<\frac{9487}{10000}.
\]
Therefore
\[
\left(\log(\sqrt u I_0(u))\right)''\bigg|_{u=10}
=
\frac{199}{200}-\frac{r_0(10)}{10}-r_0(10)^2
>
\frac{9831}{100000000}>0.
\]
So \(u\mapsto\sqrt u I_0(u)\) is locally convex in logarithmic scale at \(u=10\), and the universal strict log-concavity statement is false.

The same bound also refutes the ratio candidate:
\[
\left(\frac{I_1(10)}{I_0(10)}\right)^2
+\frac{1}{10}\frac{I_1(10)}{I_0(10)}
+\frac1{200}
<
1.
\]

Promoted true negation nodes:

- `T-not-Bessel-I-sqrt-log-concavity-nu-ge-0`
- `T-not-Bessel-I-Riccati-log-concavity-inequality`
- `T-not-Bessel-I-ratio-quadratic-bound`
- `T-not-Bessel-I-split-regime-log-concavity-certificate`

## Scout Result

Literature audit `20260526T130914` found no prior matching counterexample or erratum, but did find a conflicting 2019 positive claim for a broader \(t^\mu I_\nu(t)\) log-concavity theorem. A later Librarian pass demoted the result from an application label to an adjacent scout result: it resolves the 2011 \(\nu\ge0\) extension question locally, but the proof does not use the staged zeta-law theory or an admitted bridge layer. It is not part of immutable `stage_v006`.
