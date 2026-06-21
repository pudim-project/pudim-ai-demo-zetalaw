# Fresh Forage Restart: Special-Function Open Problems

## Context

The prior local branch solved the \(n=2\) Qi--Lim--Nantomah beta-window terminal node. The user requested a Scout forage restart that avoids the same authors' problem list and looks outward through the wiki/theory context: Gamma and polygamma curvature, logarithmic derivative inequalities, complete monotonicity, zeta-adjacent recurrences, and special-function endpoint problems.

Oracle forage was attempted first, but `OF-20260526T121624Z` returned only the scaffold response. Manual Scout forage then used source-grounded web retrieval and TeX-source inspection.

## Sources

- Baricz, Ponnusamy, and Vuorinen, "Functional inequalities for modified Bessel functions", arXiv:1009.4814, journal version in Expositiones Mathematicae. The arXiv abstract notes that the paper ends by posing several open problems.
- Cohl, "Report from the Open Problems Session at OPSFA13", arXiv:1607.06196 / SIGMA 12 (2016), 071. The report records open problems from OPSFA13.
- NIST publication page for the OPSFA13 open-problems report.

## Candidate Ranking

The top accepted candidate is:
\[
T\text{-Bessel-I-sqrt-log-concavity-nu-ge-0}:
\qquad
\forall \nu\ge0,\quad u\mapsto \sqrt{u}\,I_\nu(u)
\text{ is strictly log-concave on }(0,\infty).
\]

This candidate was selected because it is source-grounded, not from the excluded author list, and close enough to the current proof machinery to support immediate Attack Plans. The natural reduction is to the logarithmic derivative
\[
r_\nu(u)=\frac{I_\nu'(u)}{I_\nu(u)}.
\]
Strict log-concavity is equivalent to
\[
r_\nu'(u)-\frac{1}{2u^2}<0.
\]
The modified Bessel equation gives the Riccati identity
\[
r_\nu'(u)=1+\frac{\nu^2}{u^2}-\frac{r_\nu(u)}{u}-r_\nu(u)^2,
\]
so the first Advisor attack should target the inequality
\[
1+\frac{\nu^2-\frac12}{u^2}
-\frac{r_\nu(u)}{u}-r_\nu(u)^2<0.
\]

Deferred candidates:

- Gegenbauer integral positivity threshold from OPSFA13: high conceptual nutrient, slightly farther from existing local tools.
- \(K_\nu'(u)/K_\nu(u)^2\) monotonicity for \(|\nu|<1\): related Bessel candidate but singular endpoint behavior makes it a second choice.
- Zudilin polynomial recurrence/hypergeometric questions: zeta-adjacent but higher difficulty.
- General uniform asymptotics with error bounds for orthogonal polynomials: source-worthy vocabulary, too broad for immediate Student execution.

## Librarian Decision

Candidate 1 is admitted as a fresh open Theory node and next terminal/frontier candidate. No external proof is imported. The other candidates remain raw forage material for later Advisor review.
