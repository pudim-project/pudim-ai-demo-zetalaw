# Zeta-Law Entropy, Gamma Curvature, and Laplace-Measure Applications

Powered by the [Pudim AI Project](https://github.com/pudim-project/pudim-project).

This repository contains the public staged theory for the zetalaw-demov2 research track. The latest snapshot is `THEORY_v015`, staged on 2026-06-05.

## Public Theory

- Latest TeX: [`theory/latest/THEORY.tex`](theory/latest/THEORY.tex)
- Latest PDF: [`theory/latest/THEORY.pdf`](theory/latest/THEORY.pdf)
- Versioned TeX: [`theory/versions/v015/THEORY_v015.tex`](theory/versions/v015/THEORY_v015.tex)
- Versioned PDF: [`theory/versions/v015/THEORY_v015.pdf`](theory/versions/v015/THEORY_v015.pdf)

## Abstract

We study the Riemann zeta function as the partition function of the probability law \(\rho_\beta(n)=n^{-\beta}/\zeta(\beta)\) on the positive integers. This normalization turns zeta ratios into moments, logarithmic derivatives into energy cumulants, divisor identities into probabilistic decompositions, and zeta tails into reciprocal partition problems.

The public theory develops a common positivity calculus for zeta, gamma, polygamma, Mills-ratio, Ramanujan-integral, Bessel, Stieltjes, Bernstein, determinant, moment-ratio, endpoint-obstruction, and finite Weyl-algebra applications. Its reusable mechanisms include Laplace kernels, moment-ratio reductions, determinant compression, stable subordination, triangular coefficient extraction, endpoint obstructions, exact rational certificates, and Wick-dual extremal functionals.

The public ledger for `v015` contains 50 solved applications, `APP-0001` through `APP-0050`, with immutable APP identifiers and source references.

## Applications

All entries below are `Solved`; detailed statements, proofs, and review notes are in [`APPLICATIONS.md`](APPLICATIONS.md).

| APP id | Summary | Stated problem | Source reference |
| --- | --- | --- | --- |
| APP-0001 | Alzer-Kwong convexity and concavity problem | Alzer-Kwong convexity and concavity problem | [Horst Alzer, On the concavity and convexity of \(1/\zeta\)](https://doi.org/10.1142/S1793042125500897) |
| APP-0002 | Nantomah zeta positivity problem | Nantomah zeta positivity problem | [ResearchGate](https://www.researchgate.net/publication/384676538_Open_Problem_on_Riemann_Zeta_Function) |
| APP-0003 | Sroysang generalized Holder problem | Sroysang generalized Holder problem | [PDF](https://arastirmax.com/en/system/files/dergiler/135290/makaleler/3/1/arastirmax-two-inequalities-riemann-zeta-functions.pdf) |
| APP-0004 | Complete monotonicity of \((\log\Gamma(x)+\log\Gamma(1/x))''\) | Complete monotonicity of \((\log\Gamma(x)+\log\Gamma(1/x))''\) | [and Kwara Nantomah, Monotonicity and positivity of several functions involving ratios and products of polygamma functions](https://doi.org/10.1186/s13660-024-03245-8) |
| APP-0005 | Exact inverse-tail floor formula at s=7 | Exact inverse-tail floor formula at \(s=7\) | [https://link.springer.com/article/10.1186/s13660-018-1743-6](https://link.springer.com/article/10.1186/s13660-018-1743-6) |
| APP-0006 | Exact inverse-tail floor formula at s=8 | Exact inverse-tail floor formula at \(s=8\) | [https://link.springer.com/article/10.1186/s13660-018-1743-6](https://link.springer.com/article/10.1186/s13660-018-1743-6) |
| APP-0007 | Concavity or complete monotonicity of the polygamma product P0 | Concavity or complete monotonicity of the polygamma product \(P_0\) | [and Kwara Nantomah, Monotonicity and positivity of several functions involving ratios and products of polygamma functions](https://doi.org/10.1186/s13660-024-03245-8) |
| APP-0008 | Higher-order monotonicity of polygamma products Pn | Higher-order monotonicity of polygamma products \(P_n\) | [and Kwara Nantomah, Monotonicity and positivity of several functions involving ratios and products of polygamma functions](https://doi.org/10.1186/s13660-024-03245-8) |
| APP-0009 | Sharp reciprocal Gamma-product monotonicity threshold | Sharp reciprocal Gamma-product monotonicity threshold | [Teodor Bulboaca, Monotonic nature of the Gamma function](https://doi.org/10.1186/s13660-025-03425-0) |
| APP-0010 | Nielsen \(k\)-beta derivative-ratio monotonicity | Nielsen \(k\)-beta derivative-ratio monotonicity | [arXiv](https://arxiv.org/abs/2502.15852) |
| APP-0011 | Exact \(n=2\) beta-window endpoint | Exact \(n=2\) beta-window endpoint | [and Kwara Nantomah, Monotonicity and positivity of several functions involving ratios and products of polygamma functions](https://doi.org/10.1186/s13660-024-03245-8) |
| APP-0012 | Baricz \(V_q\) strict \(q\)-log-convexity | Baricz \(V_q\) strict \(q\)-log-convexity | [PDF](https://dea.lib.unideb.hu/bitstreams/bdd4469f-1b1e-4996-9b90-73f5e1a6b0e8/download) |
| APP-0013 | Yin \((p,k)\)-digamma sharp \(\alpha\)-necessity | Yin \((p,k)\)-digamma sharp \(\alpha\)-necessity | [PDF](https://www.ijopcm.org/Vol/2018/2.9.pdf) |
| APP-0014 | Ramanujan integral is Stieltjes and has a complete Bernstein primitive | Classify the Ramanujan integral by a standard positive-kernel transform rather than only by inequalities. | source recorded |
| APP-0015 | Sibisi-Prabhakar measure is a stable-subordination push-forward | Give a canonical probabilistic representation of the Prabhakar Q-measure in the strict Pollard range. | source recorded |
| APP-0016 | From's Mills-ratio bound extends to every derivative level | Lift the published Mills-ratio bound to the full derivative hierarchy. | source recorded |
| APP-0017 | Baricz gamma-quotient Bernstein-for-all problem has a rational counterexample | Decide whether the gamma quotient is Bernstein throughout the full parameter range. | source recorded |
| APP-0018 | Qi-Guo tau threshold has a supremum-corrected exact value | Find the optimal uniform threshold for the tau expression in Open Problem 3. | source recorded |
| APP-0019 | Wakrim W-symbol Bernstein range closes the beta gap | Close the open Bernstein-symbol range for the W-operator when 0<beta<=1. | source recorded |
| APP-0020 | Qi's degree-four conjecture for h_lambda is refuted at the endpoint | Test the conjectured complete-monotonic degree four for h_lambda and -h_mu. | source recorded |
| APP-0021 | Szabo's cutoff problem has \(\alpha_0=1\) | Determine the exact cutoff alpha_0 for y^alpha H_d(y). | source recorded |
| APP-0022 | Chen-Choi Gurland gamma-ratio conjecture is logarithmically completely monotone | Prove logarithmic complete monotonicity of the Gurland gamma ratio conjectured in the source. | source recorded |
| APP-0023 | Sokal generalized-Stieltjes lambda-derivatives have a triangular nonnegative compression | Explain the lambda-derivative structure of Sokal's generalized-Stieltjes Hankel-type expressions. | source recorded |
| APP-0024 | Simon gamma quotient is Bernstein | Determine whether Simon's gamma quotient \(F_\alpha(x)=\Gamma(x+\alpha)/(\Gamma(x)x^\alpha)\) is Bernstein for \(0<\alpha<1\). | source recorded |
| APP-0025 | Du-Wang \(h_3\) monotonicity is classified | Classify Du-Wang's \(h_3\) monotonicity on \((0,\infty)\) for \(0<a<2\). | source recorded |
| APP-0026 | Baskakov even-power complete-monotonicity conjecture is false | Decide the Abel-Gawronski-Neuschel complete-monotonicity conjecture for all even powers in the Baskakov family. | source recorded |
| APP-0027 | Ma-Weigert derivative regions form a descending chain | Prove the Ma-Weigert derivative-region descending-chain assertion for log-functions. | source recorded |
| APP-0028 | Qi-Agarwal/Yin divisor-polygamma parity is corrected | Decide the Qi-Agarwal/Yin divisor-polygamma parity problem. | source recorded |
| APP-0029 | Bulboaca-Zayed Gamma quotient has one critical point | Prove the Bulboaca-Zayed analytic one-critical-point pattern for their Gamma quotient. | source recorded |
| APP-0030 | Ramanujan integral Turan window is false | Decide the Mishra-Swaminathan Ramanujan integral Turan-window complete-monotonicity problem. | source recorded |
| APP-0031 | Baricz gamma-quotient Bernstein test is false | Decide whether Baricz's gamma-quotient is Bernstein for every \(a,b>0\). | source recorded |
| APP-0032 | From's all-\(L\) Mills-ratio bound family is explicit | Solve From's open all-\(L\) Mills-ratio bound problem from Remark 6.5. | source recorded |
| APP-0033 | Ramanujan antiderivative is complete Bernstein | Resolve whether the Ramanujan integral antiderivative is a complete Bernstein function. | source recorded |
| APP-0034 | Bulboaca-Zayed gamma-quotient monotonicity solved | Solve the Bulboaca-Zayed one-critical-point monotonicity statement for the gamma quotient. | source recorded |
| APP-0035 | Keady self-bijection inverse-CM question is negative | Ask whether a CM self-bijection \((0,\infty)\to(0,\infty)\) must have a CM inverse (Keady Q3). | source recorded |
| APP-0036 | Baskakov even-line complete-monotonicity fails at \(r=8\) | Decide the even-line Baskakov complete-monotonicity conjecture at \(r=8\). | source recorded |
| APP-0037 | Du-Wang \(h_3\) is increasing exactly on \(\frac12\le a\le1\) | Classify Du-Wang \(h_3\) monotonicity on \((0,\infty)\). | source recorded |
| APP-0038 | Ma-Weigert derivative-sign regions form a chain | Prove the Ma-Weigert derivative-region descending chain. | source recorded |
| APP-0039 | Ramanujan Turan-window complete-monotonicity interval is false | Decide the Ramanujan Turan-window complete-monotonicity interval. | source recorded |
| APP-0040 | Yang-Tian Bessel-\(W\) power-Bernstein conjecture is true | Solve Yang and Tian's Bessel-\(W\) power-Bernstein conjecture on the source interval. | source recorded |
| APP-0041 | Qi \(h_\lambda\) degree-four complete-monotonicity conjecture is false | Settle Qi's degree-four complete-monotonicity conjecture for \(h_\lambda\). | [Feng Qi, Completely monotonic degree of a function involving trigamma and tetragamma functions](https://doi.org/10.3934/math.2020219) |
| APP-0042 | Modified Bessel square-root log-concavity fails | Decide whether \(u\mapsto\sqrt u I_\nu(u)\) is strictly log-concave for every \(\nu\ge0\). | [Mihaly Baricz, Pietro Ponnusamy, and Matti Vuorinen, Functional inequalities for modified ...](https://doi.org/10.1016/j.exmath.2011.07.001) |
| APP-0043 | Riccati log-concavity inequality for \(I_\nu\) is false | Decide the universal Riccati log-concavity inequality for \(I_\nu\). | [Mihaly Baricz, Pietro Ponnusamy, and Matti Vuorinen, Functional inequalities for modified ...](https://doi.org/10.1016/j.exmath.2011.07.001) |
| APP-0044 | Bessel ratio quadratic lower bound is false | Decide the Bessel-ratio quadratic lower bound. | [Mihaly Baricz, Pietro Ponnusamy, and Matti Vuorinen, Functional inequalities for modified ...](https://doi.org/10.1016/j.exmath.2011.07.001) |
| APP-0045 | Three-regime Bessel log-concavity certificate route is refuted | Decide whether a three-regime certificate proves universal Bessel Riccati log-concavity. | [Mihaly Baricz, Pietro Ponnusamy, and Matti Vuorinen, Functional inequalities for modified ...](https://doi.org/10.1016/j.exmath.2011.07.001) |
| APP-0046 | Tao--Sawin finite Weyl l1 minimum is exact | Decide the Tao--Sawin finite Weyl-algebra homogeneous \(\ell^1\) minimum. | [Terence Tao, Commutators close to the identity,](https://terrytao.wordpress.com/2018/04/11/commutators-close-to-the-identity/) |
| APP-0047 | BPV noncentral chi-square HCM range has no positive noncentrality | Determine the positive-noncentrality HCM range for BPV noncentral chi-square densities. | [Baricz--Prabhu--Singh--Vijesh, Infinitely divisible modified Bessel distributions, Pacific...](https://doi.org/10.2140/pjm.2026.343.261) |
| APP-0048 | BMR tau-Gauss ordinary concavity is false | Decide the ordinary-concavity alternative in the Bansal--Mehrez--Raina tau-Gauss open problem. | [Deepak Bansal, Khaled Mehrez, and Ravinder Krishna Raina, Certain functional inequalities ...](https://www.ilirias.com/jiasf/repository/docs/JIASF12-3-4.pdf) |
| APP-0049 | Baricz arithmetic/arithmetic zero-balanced hypergeometric threshold | Determine the arithmetic/arithmetic zero-balanced hypergeometric concavity threshold in Baricz's mean problem. | source recorded |
| APP-0050 | Stolarsky shifted power means with \(p>1\) are not Bernstein | Decide the \(p>1\) unequal-shift power-mean subfamily of the Chen--Qi/Bessenyei shifted Stolarsky problem. | [Adam Bessenyei, On complete monotonicity of some functions related to means, Mathematical ...](https://files.ele-math.com/articles/mia-16-17.pdf) |

See [`APPLICATIONS.md`](APPLICATIONS.md) for the detailed public application ledger and source references.

## Public Vault Note

The latest staged theory snapshot is `stage_v015`.
The public wiki vault is synchronized at [`wiki/latest`](wiki/latest), with the immutable snapshot stored under [`wiki/versions/stage_v015`](wiki/versions/stage_v015).

## Reading Notes

Start with the PDF for the paper narrative and the LaTeX source for exact formulas. Human and agent ingestion notes are in [`HUMANS.md`](HUMANS.md) and [`AGENTS.md`](AGENTS.md).

Repository URL: https://github.com/pudim-project/pudim-ai-demo-zetalaw
