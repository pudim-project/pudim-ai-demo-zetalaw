# Applications Changelog

This changelog records staged applications of the theory to externally stated problems. Contact/review notes are intentionally minimal.
`APP-0001`--`APP-0026` appear in `theory/latest/THEORY.tex` under the manuscript `Applications` section and in the corresponding theorem names. Applications through `APP-0026` are staged in `THEORY_v010`.

| id | date | stated problem | solution | status | review |
| --- | --- | --- | --- | --- | --- |
| APP-0001 | 2026-05-17 | Alzer-Kwong convexity and concavity problem | Alzer-Kwong convexity and concavity pattern for reciprocal zeta | Solved | no reply |
| APP-0002 | 2026-05-17 | Nantomah zeta positivity problem | Affirmative solution of Nantomah zeta positivity problem | Solved | confirmed correct |
| APP-0003 | 2026-05-17 | Sroysang generalized Holder problem | Generalized Holder inequality for Gamma zeta | Solved | no reply |
| APP-0004 | 2026-05-17 | Complete monotonicity of \((\log\Gamma(x)+\log\Gamma(1/x))''\) | Complete monotonicity of reciprocal-Gamma curvature | Solved | no reply |
| APP-0005 | 2026-05-17 | Exact inverse-tail floor formula at \(s=7\) | Exact inverse-tail floor formula at \(s=7\) | Solved | no reply |
| APP-0006 | 2026-05-17 | Exact inverse-tail floor formula at \(s=8\) | Exact inverse-tail floor formula at \(s=8\) | Solved | no reply |
| APP-0007 | 2026-05-19 | Concavity or complete monotonicity of the polygamma product \(P_0\) | Complete monotonicity of reciprocal digamma product curvature | Solved | no reply |
| APP-0008 | 2026-05-19 | Higher-order monotonicity of polygamma products \(P_n\) | Counterexample to complete monotonicity of higher-order polygamma product curvature | Solved | no reply |
| APP-0009 | 2026-05-23 | Sharp reciprocal Gamma-product monotonicity threshold | APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity | Solved | no contact |
| APP-0010 | 2026-05-26 | Nielsen \(k\)-beta derivative-ratio monotonicity | Parity law from a complete-monotone Laplace moment-ratio bridge | Solved | no contact |
| APP-0011 | 2026-05-28 | Exact \(n=2\) beta-window endpoint | Exact certified endpoint for the remaining Qi--Lim--Nantomah beta-window case | Solved | no contact |
| APP-0012 | 2026-05-28 | Baricz \(V_q\) strict \(q\)-log-convexity | Positive Laplace representation proving strict parameter log-convexity | Solved | no contact |
| APP-0013 | 2026-05-28 | Yin \((p,k)\)-digamma sharp \(\alpha\)-necessity | Near-zero obstruction proving complete monotonicity forces \(\alpha\le1\) | Solved | no contact |
| APP-0014 | 2026-05-31 | Classify the Ramanujan integral by a standard positive-kernel transform rather than only by inequalities. | The density is completely monotone, so the integral is Stieltjes and its Bernstein primitive is complete Bernstein. | Solved | no reply |
| APP-0015 | 2026-05-31 | Give a canonical probabilistic representation of the Prabhakar Q-measure in the strict Pollard range. | The Q-measure is the alpha-stable subordination of the transform-normalized Pollard measure. | Solved | no reply |
| APP-0016 | 2026-05-31 | Lift the published Mills-ratio bound to the full derivative hierarchy. | The level-\(L\) determinant inequality yields an explicit bound for every derivative quotient and hence for the original Mills ratio. | Solved | no reply |
| APP-0017 | 2026-05-31 | Decide whether the gamma quotient is Bernstein throughout the full parameter range. | The parameters a=2, b=3 give a rational quotient whose derivative is not completely monotone. | Solved | no reply |
| APP-0018 | 2026-05-31 | Find the optimal uniform threshold for the tau expression in Open Problem 3. | The exact threshold is the supremum \(a_*/(1+a_*+a_*^2)\), where \(e^{a_*}=1+a_*+a_*^2\); the value is not attained. | Solved | no reply |
| APP-0019 | 2026-05-31 | Close the open Bernstein-symbol range for the W-operator when \(0<\beta\le1\). | Wakrim's source supplies the \(\beta>1\) obstruction; the staged proof proves the remaining Bernstein range \(0\le\beta\le1\). | Solved | author confirmed; attribution clarified |
| APP-0020 | 2026-05-31 | Test the conjectured complete-monotonic degree four for \(h_\lambda\) and \(-h_\mu\). | The degree-four transforms fail the first derivative test near zero, so the conjecture is false. | Solved | no reply |
| APP-0021 | 2026-05-31 | Determine the exact cutoff \(\alpha_0\) for \(y^\alpha H_d(y)\). | The cutoff is \(\alpha_0=1\): sufficiency is the source theorem and necessity follows from the singular expansion at zero. | Solved | no reply |
| APP-0022 | 2026-05-31 | Prove logarithmic complete monotonicity of the Gurland gamma ratio conjectured in the source. | A Weierstrass product reduces log F to a sum of strictly completely monotone logarithmic second differences. | Solved | no reply |
| APP-0023 | 2026-05-31 | Explain the lambda-derivative structure of Sokal's generalized-Stieltjes Hankel-type expressions. | The exponential generating function gives a triangular nonnegative convolution formula for every lambda derivative. | Solved | no reply |
| APP-0024 | 2026-06-01 | Determine whether Simon's gamma quotient \(F_\alpha(x)=\Gamma(x+\alpha)/(\Gamma(x)x^\alpha)\) is Bernstein for \(0<\alpha<1\). | A complement complete-monotonicity representation proves \(F_\alpha\) is Bernstein. | Solved | no contact |
| APP-0025 | 2026-06-01 | Classify Du-Wang's \(h_3\) monotonicity on \((0,\infty)\) for \(0<a<2\). | A polygamma-ratio kernel proves increasing behavior exactly for \(1/2\le a\le1\), with nonmonotonicity outside. | Solved | no contact |
| APP-0026 | 2026-06-01 | Decide the Abel-Gawronski-Neuschel complete-monotonicity conjecture for all even powers in the Baskakov family. | The \(\alpha=1,r=8\) inverse-Laplace density is negative at \(t=10\pi\), refuting the conjecture. | Solved | no contact |

## Application Details

### APP-0001: Alzer-Kwong convexity and concavity problem

- source reference: Horst Alzer and Man Kam Kwong, "On the concavity and convexity of \(1/\zeta\)", International Journal of Number Theory, Vol. 21, No. 8 (2025), 1825-1835. DOI: [DOI](https://doi.org/10.1142/S1793042125500897)
- solution: Alzer-Kwong convexity and concavity pattern for reciprocal zeta
- solution status: Solved
- problem node: `wiki/nodes/mrw-c9ec61b1c573.md`
- solution node: `wiki/nodes/mrw-6b7d94a697d7.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no reply

#### Stated problem

Alzer and Kwong conjectured the reciprocal zeta function \(F(x)=1/\zeta(x)\) has the sign pattern 

\[
F''(x)>0\quad\text{on }(-4n,-4n+2),
\]

 and 

\[
F''(x)<0\quad\text{on }(-4n-2,-4n),
\]

 for every integer \(n\ge1\).

### APP-0002: Nantomah zeta positivity problem

- source reference: Kwara Nantomah, "Open Problem on Riemann Zeta Function", ResearchGate problem note, October 2024. [ResearchGate](https://www.researchgate.net/publication/384676538_Open_Problem_on_Riemann_Zeta_Function)
- solution: Affirmative solution of Nantomah zeta positivity problem
- solution status: Solved
- problem node: `wiki/nodes/mrw-eb9a71666a04.md`
- solution node: `wiki/nodes/mrw-f9e130ed65ef.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: confirmed correct
- review date: 2026-05-23

#### Stated problem

Determine whether, for every \(n\in\mathbb N\), 

\[
(n+2)\zeta(n+1)\zeta(n+3) -(n+1)\zeta(n+2)^2 -\zeta(n+1)\zeta(n+2)>0.
\]

### APP-0003: Sroysang generalized Holder problem

- source reference: Banyat Sroysang, "Two Inequalities for the Riemann Zeta Functions", Mathematica Aeterna, Vol. 3, No. 1 (2013), 21-24. [PDF](https://arastirmax.com/en/system/files/dergiler/135290/makaleler/3/1/arastirmax-two-inequalities-riemann-zeta-functions.pdf)
- solution: Generalized Holder inequality for Gamma zeta
- solution status: Solved
- problem node: `wiki/nodes/mrw-f95d129327fc.md`
- solution node: `wiki/nodes/mrw-8aa5f1703758.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no reply

#### Stated problem

Sroysang asked how a Holder-type zeta inequality changes when the usual condition 

\[
\sum_{i=1}^m\frac1{p_i}=1
\]

 is replaced by 

\[
\sum_{i=1}^m\frac1{p_i}=\frac1r,\qquad r\ge1.
\]

### APP-0004: Complete monotonicity of \((\log\Gamma(x)+\log\Gamma(1/x))''\)

- source reference: Feng Qi, Dongkyu Lim, and Kwara Nantomah, "Monotonicity and positivity of several functions involving ratios and products of polygamma functions", Journal of Inequalities and Applications 2025, article 5. DOI: [DOI](https://doi.org/10.1186/s13660-024-03245-8)
- solution: Complete monotonicity of reciprocal-Gamma curvature
- solution status: Solved
- problem node: `wiki/nodes/mrw-724ed6e2941c.md`
- solution node: `wiki/nodes/mrw-48a67678d0c1.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no reply

#### Stated problem

Determine the complete monotonicity or related sign pattern of the second derivative 

\[
\left(\log\Gamma(x)+\log\Gamma(1/x)\right)''.
\]

### APP-0005: Exact inverse-tail floor formula at s=7

- source reference: Donggyun Kim and Kyunghwan Song, "The inverses of tails of the Riemann zeta function", Journal of Inequalities and Applications 2018, article 157. [https://link.springer.com/article/10.1186/s13660-018-1743-6](https://link.springer.com/article/10.1186/s13660-018-1743-6); Zhenjiang Pan and Zhengang Wu, "The inverse of tails of Riemann zeta function, Hurwitz zeta function and Dirichlet L-function", AIMS Mathematics 9(6), 16564-16585, 2024. DOI: [DOI](https://doi.org/10.3934/math.2024803)
- solution: Exact inverse-tail floor formula at s=7
- solution status: Solved
- problem node: `wiki/nodes/mrw-900d84ddee24.md`
- solution node: `wiki/nodes/mrw-28bcccec471e.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no reply

#### Stated problem

Find an exact computable formula for 

\[
\left\lfloor \zeta_n(7)^{-1}\right\rfloor, \qquad \zeta_n(s)=\sum_{k=n}^{\infty} k^{-s}.
\]

### APP-0006: Exact inverse-tail floor formula at s=8

- source reference: Donggyun Kim and Kyunghwan Song, "The inverses of tails of the Riemann zeta function", Journal of Inequalities and Applications 2018, article 157. [https://link.springer.com/article/10.1186/s13660-018-1743-6](https://link.springer.com/article/10.1186/s13660-018-1743-6); Zhenjiang Pan and Zhengang Wu, "The inverse of tails of Riemann zeta function, Hurwitz zeta function and Dirichlet L-function", AIMS Mathematics 9(6), 16564-16585, 2024. DOI: [DOI](https://doi.org/10.3934/math.2024803)
- solution: Exact inverse-tail floor formula at s=8
- solution status: Solved
- problem node: `wiki/nodes/mrw-3f583950a960.md`
- solution node: `wiki/nodes/mrw-544506a822b8.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no reply

#### Stated problem

Find an exact computable formula for 

\[
\left\lfloor \zeta_n(8)^{-1}\right\rfloor, \qquad \zeta_n(s)=\sum_{k=n}^{\infty} k^{-s}.
\]

### APP-0007: Concavity or complete monotonicity of the polygamma product P0

- source reference: Feng Qi, Dongkyu Lim, and Kwara Nantomah, "Monotonicity and positivity of several functions involving ratios and products of polygamma functions", Journal of Inequalities and Applications 2025, article 5. DOI: [DOI](https://doi.org/10.1186/s13660-024-03245-8)
- solution: Complete monotonicity of reciprocal digamma product curvature
- solution status: Solved
- problem node: `wiki/nodes/mrw-2650caac5236.md`
- solution node: `wiki/nodes/mrw-0db1ed17aa9a.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no reply

#### Stated problem

Resolve the stated monotonicity or curvature behavior of 

\[
P_0(x)=\psi(x)\psi(1/x).
\]

### APP-0008: Higher-order monotonicity of polygamma products Pn

- source reference: Feng Qi, Dongkyu Lim, and Kwara Nantomah, "Monotonicity and positivity of several functions involving ratios and products of polygamma functions", Journal of Inequalities and Applications 2025, article 5. DOI: [DOI](https://doi.org/10.1186/s13660-024-03245-8)
- solution: Counterexample to complete monotonicity of higher-order polygamma product curvature
- solution status: Solved
- problem node: `wiki/nodes/mrw-f0a031feea8e.md`
- solution node: `wiki/nodes/mrw-dee642b8e9cb.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no reply

#### Stated problem

For \(n\ge 1\), determine convexity, monotonicity, or complete monotonicity properties of 

\[
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x).
\]

### APP-0009: Sharp reciprocal Gamma-product monotonicity threshold

- source reference: Teodor Bulboaca and Hanaa M. Zayed, "Monotonic nature of the Gamma function", Journal of Inequalities and Applications 2026, article 27. DOI: [DOI](https://doi.org/10.1186/s13660-025-03425-0)
- solution: APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity
- solution status: Solved
- problem node: `wiki/nodes/mrw-1396775c6089.md`
- solution node: `wiki/nodes/mrw-0fd149ddc79d.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no reply

#### Stated problem

Bulboaca and Zayed ask for the smallest positive parameter values in their Gamma-product monotonicity examples.  In the base example, the question is to find the optimal \(\rho\) for which 

\[
\varphi_\rho(s)=\frac{1}{\Gamma(s+\rho)\Gamma(s)}
\]

 is strictly decreasing on \([1,\infty)\), equivalently for which 

\[
W_\rho(s)=\Gamma(s+\rho)\Gamma(s)
\]

 is strictly increasing on \([1,\infty)\).  The local theorem Sharp threshold for reciprocal Gamma-product monotonicity solves this base threshold problem.  If 

\[
\psi(1+\rho_*)=\gamma,
\]

 then the optimal condition is \(\rho\ge \rho_*\), where numerically

\[
\rho_*=1.2583969670859318174106234224981693941\ldots .
\]

#### Staged resolution

The staged theorem proves the equivalence by checking the endpoint of

\[
\frac{d}{ds}\log\left(\Gamma(s+\rho)\Gamma(s)\right)=\psi(s+\rho)+\psi(s).
\]

Since \(\psi\) is strictly increasing, the left endpoint \(s=1\) controls the sign. Thus \(\varphi_\rho\) is strictly decreasing on \([1,\infty)\) exactly when \(\psi(1+\rho)\ge\gamma\). The same endpoint argument gives the generalized criterion for \(u(s)/(\Gamma(s+\rho)\Gamma(s))\) when \(u'/u\) is nonincreasing.

### APP-0010: Nielsen \(k\)-beta derivative-ratio monotonicity

- source reference: Li Yin and Jumei Zhang, "On some properties of special functions involving \(k\)-gamma and \(k\)-digamma functions", arXiv:2502.15852. [arXiv](https://arxiv.org/abs/2502.15852)
- solution: parity law from a complete-monotone Laplace moment-ratio bridge
- solution status: Solved
- bridge result: Lemma `laplace-moment-ratio-bridge` in `THEORY_v007`
- solution theorem: Theorem `nielsen-k-beta-derivative-ratio` in `THEORY_v007`
- source problem: Yin--Zhang Nielsen \(k\)-beta derivative-ratio open problem
- theory version: `v007`
- review status: no reply

#### Stated problem

For \(k>0\), determine the monotonicity of

\[
\frac{(x\beta_k(x))^{(n+1)}}{(x\beta_k(x))^{(n)}(x\beta_k(x))^{(n+2)}}
\]

on \(x>0\).

#### Staged resolution

The precise parity law is: the ratio is strictly increasing for odd \(n\), and strictly decreasing for even \(n\). The proof introduces a reusable bridge lemma: if \(a_j(x)=\int_0^\infty t^j e^{-xt}\,d\mu(t)>0\), then \(a_{n+1}(x)/(a_n(x)a_{n+2}(x))\) is strictly increasing. Applying this to

\[
x\beta_k(x)=\frac12+\int_0^\infty e^{-xt}\frac{k e^{-kt}}{(1+e^{-kt})^2}\,dt
\]

solves the source problem.

### APP-0011: Exact \(n=2\) beta-window endpoint

- source reference: Feng Qi, Dongkyu Lim, and Kwara Nantomah, "Monotonicity and positivity of several functions involving ratios and products of polygamma functions", Journal of Inequalities and Applications 2025, article 5. DOI: [DOI](https://doi.org/10.1186/s13660-024-03245-8)
- solution: exact certified endpoint for the remaining Qi--Lim--Nantomah beta-window case
- solution status: Solved
- solution theorem: Theorem `q2-exact-endpoint` in `THEORY_v008`
- source problem: Qi--Lim--Nantomah Open Problem 4, remaining \(n=2\) case
- theory version: `v008`
- review status: no reply

#### Stated problem

For \(n=2\), determine the exact admissible set

\[
\mathcal I_2=\left\{\beta:x^\beta C_2(x)-P_2(x)<0\text{ for all }x>0\right\}.
\]

#### Staged resolution

The staged theorem proves that \(Q_2\) has a unique global maximizer \(\xi\in[287345/1000000,287346/1000000]\). Therefore, with \(L_2=Q_2(\xi)\),

\[
\mathcal I_2=(L_2,3].
\]

### APP-0012: Baricz \(V_q\) strict \(q\)-log-convexity

- source reference: Arpad Baricz, "Turan type inequalities for some special functions", Ph.D. thesis, University of Debrecen, 2008. [PDF](https://dea.lib.unideb.hu/bitstreams/bdd4469f-1b1e-4996-9b90-73f5e1a6b0e8/download)
- solution: positive Laplace representation proving strict parameter log-convexity
- solution status: Solved
- solution theorem: Theorem `baricz-vq-strict-logconvexity` in `THEORY_v008`
- source problem: Baricz \(V_q\) parameter log-convexity problem
- theory version: `v008`
- review status: no contact

#### Stated problem

For fixed \(x>0\), prove that \(q\mapsto V_q(x)\) is log-convex on \((-1,\infty)\), where

\[
V_q(x)=\frac{2e^{x^2}}{\Gamma(q+1)}\int_x^\infty e^{-t^2}(t^2-x^2)^q\,dt.
\]

#### Staged resolution

The staged theorem proves the stronger strict log-convexity statement from

\[
V_q(x)=\frac1{\sqrt\pi}\int_0^\infty s^{-1/2}e^{-x^2s}(1+s)^{-(q+1)}\,ds,
\]

a positive nondegenerate Laplace transform in the parameter \(q+1\).

### APP-0013: Yin \((p,k)\)-digamma sharp \(\alpha\)-necessity

- source reference: Li Yin, "Complete monotonicity of a function involving the \((p,k)\)-digamma function", International Journal of Open Problems in Computer Mathematics 11(2), 103-108, 2018. [PDF](https://www.ijopcm.org/Vol/2018/2.9.pdf)
- solution: near-zero obstruction proving complete monotonicity forces \(\alpha\le1\)
- solution status: Solved
- solution theorem: Theorem `yin-pk-alpha-necessity` in `THEORY_v008`
- source problem: Yin Open Problem 4.1 sharp necessity question for \(\delta_{p,k,\alpha}\)
- theory version: `v008`
- review status: no contact

#### Stated problem

Yin proved sufficiency of \(\alpha\le1\) for complete monotonicity of

\[
\delta_{p,k,\alpha}(x)
=x^\alpha\left[
\frac1k\log\frac{pkx}{x+k(p+1)}-\psi_{p,k}(x)
\right],
\]

and asked whether complete monotonicity implies the same sharp condition.

#### Staged resolution

The staged theorem proves necessity. The bracket is positive and satisfies

\[
\frac1k\log\frac{pkx}{x+k(p+1)}-\psi_{p,k}(x)
=\frac1x+O(|\log x|)
\qquad (x\to0^+).
\]

Thus \(\delta_{p,k,\alpha}(x)\sim x^{\alpha-1}\). If \(\alpha>1\), this tends to \(0\) at the left endpoint, contradicting positivity and nonincreasingness of a nonzero completely monotone function.


## APP-0014--APP-0026 details

### APP-0014 -- Ramanujan integral is Stieltjes and has a complete Bernstein primitive

- source: Mishra and Swaminathan, Inequalities involving a Ramanujan Integral, arXiv:2511.07443.
- problem: Classify the Ramanujan integral by a standard positive-kernel transform rather than only by inequalities.
- solution theorem: `thm:app14-ramanujan-stieltjes` in THEORY_v009.
- solution status: Solved
- public result: The density is completely monotone, so the integral is Stieltjes and its Bernstein primitive is complete Bernstein.
- review status: no reply

### APP-0015 -- Sibisi-Prabhakar measure is a stable-subordination push-forward

- source: Sibisi, A Probabilistic Perspective on Feller, Pollard and the Complete Monotonicity of the Mittag-Leffler Function, arXiv:2301.01466.
- problem: Give a canonical probabilistic representation of the Prabhakar Q-measure in the strict Pollard range.
- solution theorem: `thm:app15-prabhakar-subordination` in THEORY_v009.
- solution status: Solved
- public result: The Q-measure is the alpha-stable subordination of the transform-normalized Pollard measure.
- review status: no reply

### APP-0016 -- From's Mills-ratio bound extends to every derivative level

- source: From, Some new upper and lower bounds for the Mills ratio, J. Math. Anal. Appl. 486 (2020), 123872.
- problem: Lift the published Mills-ratio bound to the full derivative hierarchy.
- solution theorem: `thm:app16-mills-all-l` in THEORY_v009.
- solution status: Solved
- public result: The level-\(L\) determinant inequality yields an explicit bound for every derivative quotient and hence for the original Mills ratio.
- review status: no reply

### APP-0017 -- Baricz gamma-quotient Bernstein-for-all problem has a rational counterexample

- source: Baricz, Turan type inequalities for hypergeometric functions, Proc. Amer. Math. Soc. 136 (2008), 3223--3229.
- problem: Decide whether the gamma quotient is Bernstein throughout the full parameter range.
- solution theorem: `thm:app17-baricz-counterexample` in THEORY_v009.
- solution status: Solved
- public result: The parameters a=2, b=3 give a rational quotient whose derivative is not completely monotone.
- review status: no reply

### APP-0018 -- Qi-Guo tau threshold has a supremum-corrected exact value

- source: Qi and Guo, Complete Monotonicities of Functions Involving Gamma and Digamma Functions, RGMIA Res. Rep. Coll. 7 (2004), Article 8.
- problem: Find the optimal uniform threshold for the tau expression in Open Problem 3.
- solution theorem: `thm:app18-qg-tau` in THEORY_v009.
- solution status: Solved
- public result: The exact threshold is the supremum \(a_*/(1+a_*+a_*^2)\), where \(e^{a_*}=1+a_*+a_*^2\); the value is not attained.
- review status: no reply

### APP-0019 -- Wakrim W-symbol Bernstein range closes the beta gap

- source: Wakrim, The W-Operator: A Volterra Fractional Time Operator with Non-Bernstein Symbol, arXiv:2601.02876.
- problem: Close the open Bernstein-symbol range for the W-operator when \(0<\beta\le1\).
- solution theorem: `thm:app19-w-symbol` in THEORY_v010.
- solution status: Solved
- public result: Wakrim's source supplies the non-Bernstein obstruction for \(\beta>1\); the staged proof proves the remaining Bernstein side \(0\le\beta\le1\) by expanded derivative factorization, complete-monotonicity factors, the composition theorem, and endpoint cases.  No complete-Bernstein or subordination conclusion is claimed.
- review status: author confirmed; attribution clarified in THEORY_v010

### APP-0020 -- Qi's degree-four conjecture for h_lambda is refuted at the endpoint

- source: Qi, Completely monotonic degree of a function involving trigamma and tetragamma functions, AIMS Math. 5 (2020), 3391--3407.
- problem: Test the conjectured complete-monotonic degree four for \(h_\lambda\) and \(-h_\mu\).
- solution theorem: `thm:app20-qi-hlambda` in THEORY_v009.
- solution status: Solved
- public result: The degree-four transforms fail the first derivative test near zero, so the conjecture is false.
- review status: no reply

### APP-0021 -- Szabo's cutoff problem has \(\alpha_0=1\)

- source: Szabo, Completely monotone functions in general and some applications, arXiv:2411.17670.
- problem: Determine the exact cutoff \(\alpha_0\) for \(y^\alpha H_d(y)\).
- solution theorem: `thm:app21-szabo-cutoff` in THEORY_v009.
- solution status: Solved
- public result: The cutoff is \(\alpha_0=1\): sufficiency is the source theorem and necessity follows from the singular expansion at zero.
- review status: no reply

### APP-0022 -- Chen-Choi Gurland gamma-ratio conjecture is logarithmically completely monotone

- source: Chen and Choi, Completely monotonic functions related to Gurland's ratio for the gamma function, Math. Inequal. Appl. 20 (2017), 651--659.
- problem: Prove logarithmic complete monotonicity of the Gurland gamma ratio conjectured in the source.
- solution theorem: `thm:app22-gurland-logcm` in THEORY_v009.
- solution status: Solved
- public result: A Weierstrass product reduces log F to a sum of strictly completely monotone logarithmic second differences.
- review status: no reply

### APP-0023 -- Sokal generalized-Stieltjes lambda-derivatives have a triangular nonnegative compression

- source: Sokal, Real-variables characterization of generalized Stieltjes functions, Expo. Math. 28 (2010), 179--185.
- problem: Explain the lambda-derivative structure of Sokal's generalized-Stieltjes Hankel-type expressions.
- solution theorem: `thm:app23-sokal-lambda` in THEORY_v009.
- solution status: Solved
- public result: The exponential generating function gives a triangular nonnegative convolution formula for every lambda derivative.
- review status: no reply

### APP-0024 -- Simon gamma quotient is Bernstein

- source: Thomas Simon, Moment problems related to Bernstein functions, Ann. Fac. Sci. Toulouse Math. 29 (2020), 577--594.
- problem: Determine whether \(F_\alpha(x)=\Gamma(x+\alpha)/(\Gamma(x)x^\alpha)\) is Bernstein for \(0<\alpha<1\).
- solution theorem: `thm:app24-simon-gamma-quotient` in THEORY_v010.
- solution status: Solved
- public result: \(1-F_\alpha\) is completely monotone; hence \(F_\alpha'\) is completely monotone and \(F_\alpha\) is Bernstein.
- review status: no contact

### APP-0025 -- Du-Wang \(h_3\) monotonicity is classified

- source: Peipei Du and Gendi Wang, Monotonicity, convexity, and inequalities for functions involving gamma function, arXiv:2205.12530.
- problem: Classify the monotonicity of \(h_3\) on \((0,\infty)\) for \(0<a<2\).
- solution theorem: `thm:app25-du-wang-h3` in THEORY_v010.
- solution status: Solved
- public result: \(h_3\) is increasing exactly for \(1/2\le a\le1\), and is not monotone for \(0<a<1/2\) or \(1<a<2\).
- review status: no contact

### APP-0026 -- Baskakov even-power complete-monotonicity conjecture is false

- source: Ulrich Abel, Wolfgang Gawronski, and Thorsten Neuschel, Complete Monotonicity and Zeros of Sums of Squared Baskakov Functions, arXiv:1411.7945.
- problem: Decide the conjectured complete monotonicity of the higher even-power Baskakov family.
- solution theorem: `thm:app26-baskakov-r8` in THEORY_v010.
- solution status: Solved
- public result: The \(\alpha=1,r=8\) member \(1/((1+x)^8-x^8)\) has a sign-changing inverse-Laplace density, so it is not completely monotone.
- review status: no contact
