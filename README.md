# Zeta-Law Entropy, Gamma Curvature, and Laplace-Measure Applications

Powered by the [Pudim AI Project](https://github.com/pudim-project/pudim-project).

This repository contains the public staged theory for the zetalaw-demov2
research track.  The latest snapshot is `THEORY_v009`, staged on 2026-05-31.

## Public Theory

- Latest TeX: [`theory/latest/THEORY.tex`](theory/latest/THEORY.tex)
- Latest PDF: [`theory/latest/THEORY.pdf`](theory/latest/THEORY.pdf)
- Versioned TeX: [`theory/versions/v009/THEORY_v009.tex`](theory/versions/v009/THEORY_v009.tex)
- Versioned PDF: [`theory/versions/v009/THEORY_v009.pdf`](theory/versions/v009/THEORY_v009.pdf)

## Abstract

We study the Riemann zeta function as the partition function of the probability
law \(\rho_\beta(n)=n^{-\beta}/\zeta(\beta)\) on the positive integers. This
normalization turns zeta ratios into moments, logarithmic derivatives into
energy cumulants, divisor identities into probabilistic decompositions, and
zeta tails into reciprocal partition problems. The first structural layer
identifies the microscopic successor entropy of the zeta law with limits and
suprema of finite modular successor entropies; for prime moduli these modular
shadows are explicit nonlinear functionals of Dirichlet \(L\)-values. The second
structural layer rewrites zeta energy through a von Mangoldt-weighted
Euler-score divisibility average.

The theory then develops a common positivity calculus. Mellin-Planck kernels
convert generalized Holder inequalities into integral norm inequalities,
Gamma and digamma curvature problems are reduced to Laplace kernels, and
complete monotonicity becomes the organizing language for transporting
inequalities across quotient, product, and derivative constructions. Earlier
stages solved reciprocal-zeta, zeta-tail, Gamma-product, polygamma-product,
Nielsen beta, beta-window, \(q\)-log-convexity, and \((p,k)\)-digamma
necessity problems.

Version v009 adds a new Laplace-transport layer. The added applications are
organized by a common method: isolate a positive kernel or transform-normalized
measure, then apply a permanence operation such as Stieltjes transformation,
complete-Bernstein integration, stable subordination, determinant compression,
or triangular coefficient extraction. This layer solves ten additional public
source problems:
Ramanujan-integral Stieltjes classification, Prabhakar measure subordination,
all-level Mills-ratio extraction, a gamma-quotient Bernstein counterexample,
the Qi-Guo tau supremum, the Wakrim W-symbol Bernstein range, Qi's
\(h_\lambda\) degree-four conjecture, Szabo's cutoff problem, the Chen-Choi
Gurland log-complete-monotonicity conjecture, and Sokal's generalized-Stieltjes
lambda-derivative compression.

The public ledger now contains twenty-three applications with uniform status
`Solved`.

## Applications

| id | source problem | staged result | source reference | status |
| --- | --- | --- | --- | --- |
| APP-0001 | Alzer-Kwong ask for the alternating convexity/concavity pattern of reciprocal zeta on negative real intervals (2025). | Functional-equation transport plus positive-axis curvature proves the full sign pattern. | [Alzer-Kwong, IJNT 2025](https://doi.org/10.1142/S1793042125500897) | Solved |
| APP-0002 | Nantomah asks whether a three-zeta expression is positive for every positive integer input (2024). | A moment split and tail bounds prove the expression is strictly positive. | [Nantomah problem note](https://www.researchgate.net/publication/384676538_Open_Problem_on_Riemann_Zeta_Function) | Solved |
| APP-0003 | Sroysang asks how the zeta Holder inequality changes under the generalized exponent condition (2013). | The Mellin-Planck kernel gives the generalized Holder inequality directly. | [Sroysang, Mathematica Aeterna 2013](https://arastirmax.com/en/system/files/dergiler/135290/makaleler/3/1/arastirmax-two-inequalities-riemann-zeta-functions.pdf) | Solved |
| APP-0004 | Qi-Lim-Nantomah ask for the complete-monotonicity behavior of reciprocal-Gamma curvature (2025). | A Weierstrass-product Laplace kernel proves complete monotonicity. | [Qi-Lim-Nantomah, JIA 2025](https://doi.org/10.1186/s13660-024-03245-8) | Solved |
| APP-0005 | Kim-Song and Pan-Wu motivate exact reciprocal-tail floor formulas; the first staged special case is \(s=7\) (2018). | A rational telescoping enclosure gives the exact floor formula. | [Kim-Song, JIA 2018](https://doi.org/10.1186/s13660-018-1743-6); [Pan-Wu, AIMS Math. 2024](https://doi.org/10.3934/math.2024803) | Solved |
| APP-0006 | The second staged reciprocal-tail special case asks for the exact floor formula at \(s=8\) (2018). | Adjacent corrected asymptotic truncations give the exact floor formula. | [Kim-Song, JIA 2018](https://doi.org/10.1186/s13660-018-1743-6); [Pan-Wu, AIMS Math. 2024](https://doi.org/10.3934/math.2024803) | Solved |
| APP-0007 | Qi-Lim-Nantomah ask whether the reciprocal-digamma product curvature is concave or completely monotone (2025). | A grouped Laplace kernel proves complete monotonicity of the negative second derivative. | [Qi-Lim-Nantomah, JIA 2025](https://doi.org/10.1186/s13660-024-03245-8) | Solved |
| APP-0008 | Qi-Lim-Nantomah ask for higher-polygamma product curvature and the stronger complete-monotonicity property (2025). | Dominant-summand and interval certificates refute the stronger complete-monotonicity claim. | [Qi-Lim-Nantomah, JIA 2025](https://doi.org/10.1186/s13660-024-03245-8) | Solved |
| APP-0009 | Bulboaca-Zayed ask for the sharp threshold in reciprocal Gamma-product monotonicity examples (2026). | The endpoint logarithmic-derivative criterion gives the exact threshold. | [Bulboaca-Zayed, JIA 2026](https://doi.org/10.1186/s13660-025-03425-0) | Solved |
| APP-0010 | Yin-Zhang ask for a Nielsen \(k\)-beta derivative-ratio monotonicity law (2025). | A complete-monotone Laplace moment-ratio bridge gives the parity-refined theorem. | [Yin-Zhang, arXiv:2502.15852](https://arxiv.org/abs/2502.15852) | Solved |
| APP-0011 | Qi-Lim-Nantomah leave the \(n=2\) beta-window endpoint as the remaining small case (2025). | A certified rational endpoint calculation gives the exact endpoint. | [Qi-Lim-Nantomah, JIA 2025](https://doi.org/10.1186/s13660-024-03245-8) | Solved |
| APP-0012 | Baricz asks for strict parameter log-convexity of the \(V_q\) special-function family (2008). | A positive Laplace representation proves strict log-convexity in the parameter. | [Baricz thesis, 2008](https://dea.lib.unideb.hu/bitstreams/bdd4469f-1b1e-4996-9b90-73f5e1a6b0e8/download) | Solved |
| APP-0013 | Yin asks whether the published \((p,k)\)-digamma sufficiency range is also necessary (2018). | A near-zero obstruction proves the sharp necessity \(\alpha\le1\). | [Yin, IJOPCM 2018](https://www.ijopcm.org/Vol/2018/2.9.pdf) | Solved |
| APP-0014 | Mishra-Swaminathan develop Ramanujan-integral inequalities and leave room for a standard transform classification (2025). | The density is completely monotone; the integral is Stieltjes and its primitive is complete Bernstein. | [Mishra-Swaminathan, arXiv:2511.07443](https://arxiv.org/abs/2511.07443) | Solved |
| APP-0015 | Sibisi's Prabhakar-measure framework calls for a canonical probabilistic representation in the strict Pollard range (2023). | The Q-measure is the stable-subordination push-forward of the transform-normalized Pollard measure. | [Sibisi, arXiv:2301.01466](https://arxiv.org/abs/2301.01466) | Solved |
| APP-0016 | From discusses determinant-based Mills-ratio bounds and the need for a uniform derivative-level extraction (2020). | The level-\(L\) determinant inequality gives an explicit all-\(L\) Mills-ratio bound family. | [From, JMAA 2020](https://doi.org/10.1016/j.jmaa.2020.123872) | Solved |
| APP-0017 | Baricz's hypergeometric Turan paper leaves gamma-quotient Bernstein-type possibilities at the parameter boundary (2008). | The \(a=2,b=3\) rational quotient gives a derivative-sign obstruction to a Bernstein-for-all claim. | [Baricz, Proc. AMS 2008](https://doi.org/10.1090/S0002-9939-08-09353-2) | Solved |
| APP-0018 | Qi-Guo Open Problem 3 asks for the optimal tau threshold in their Gamma-digamma monotonicity framework (2004). | The exact value is a nonattained supremum determined by \(e^{a_*}=1+a_*+a_*^2\). | [Qi-Guo, RGMIA 2004](https://vuir.vu.edu.au/18037/) | Solved |
| APP-0019 | Wakrim proves non-Bernstein behavior beyond \(\beta>1\) and leaves the \(0<\beta\le1\) W-symbol range open (2026). | A derivative factorization plus Bernstein composition proves the exact range \(0\le\beta\le1\). | [Wakrim, arXiv:2601.02876](https://arxiv.org/abs/2601.02876) | Solved |
| APP-0020 | Qi conjectures complete-monotonic degree four for \(h_\lambda\) and \(-h_\mu\) in stated ranges (2020). | The degree-four transforms fail the first-derivative test near zero, refuting the conjecture. | [Qi, AIMS Math. 2020](https://doi.org/10.3934/math.2020219) | Solved |
| APP-0021 | Szabo asks for the exact cutoff for complete monotonicity of \(y^\alpha H_d(y)\) (2024). | The source sufficiency plus the singular expansion at zero gives the exact cutoff \(\alpha_0=1\). | [Szabo, arXiv:2411.17670](https://arxiv.org/abs/2411.17670) | Solved |
| APP-0022 | Chen-Choi conjecture logarithmic complete monotonicity of a Gurland gamma ratio (2017). | The Weierstrass product reduces the logarithm to a sum of strictly completely monotone second differences. | [Chen-Choi, MIA 2017](https://doi.org/10.7153/mia-20-43) | Solved |
| APP-0023 | Sokal's generalized-Stieltjes characterization leaves a lambda-derivative compression structure implicit (2009). | The exponential generating function gives a triangular nonnegative convolution for every lambda derivative. | [Sokal, arXiv:0902.0065](https://arxiv.org/abs/0902.0065) | Solved |

See [`APPLICATIONS.md`](APPLICATIONS.md) for the detailed public application
ledger and source references.

## Public Vault Note

The latest staged theory snapshot is `stage_v009`.  The public wiki vault may
lag the staged theory and should be regenerated separately before being treated
as the current public node graph.

## Reading Notes

Start with the PDF for the paper narrative and the LaTeX source for exact
formulas. Human and agent ingestion notes are in [`HUMANS.md`](HUMANS.md) and
[`AGENTS.md`](AGENTS.md).

Repository URL: https://github.com/pudim-project/pudim-ai-demo-zetalaw
