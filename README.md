# Zeta-Law Entropy, Gamma Curvature, and Laplace-Measure Applications

Powered by the [Pudim AI Project](https://github.com/pudim-project/pudim-project).

This repository contains the public staged theory for the zetalaw-demov2
research track.  The latest snapshot is `THEORY_v014`, staged on 2026-06-04.

## Public Theory

- Latest TeX: [`theory/latest/THEORY.tex`](theory/latest/THEORY.tex)
- Latest PDF: [`theory/latest/THEORY.pdf`](theory/latest/THEORY.pdf)
- Versioned TeX: [`theory/versions/v014/THEORY_v014.tex`](theory/versions/v014/THEORY_v014.tex)
- Versioned PDF: [`theory/versions/v014/THEORY_v014.pdf`](theory/versions/v014/THEORY_v014.pdf)

## Abstract

We study the Riemann zeta function as the partition function of the probability
law \(\rho_\beta(n)=n^{-\beta}/\zeta(\beta)\) on the positive integers. This
normalization turns zeta ratios into moments, logarithmic derivatives into
energy cumulants, divisor identities into probabilistic decompositions, and
zeta tails into reciprocal partition problems.

The public theory develops a common positivity calculus for zeta, gamma,
polygamma, Mills-ratio, Ramanujan-integral, Bessel, Stieltjes, and Bernstein
problems. Its reusable mechanisms include Laplace kernels, moment-ratio
reductions, determinant compression, stable subordination, triangular
coefficient extraction, endpoint obstructions, and exact rational certificates.

The public ledger now contains forty-five solved applications, `APP-0001`
through `APP-0045`, with immutable APP identifiers and source references.

## Applications

All entries below are `Solved`; detailed statements, proofs, and review notes
are in [`APPLICATIONS.md`](APPLICATIONS.md).

| APP id | Summary (Year) | Description | Reference (link) |
| --- | --- | --- | --- |
| APP-0001 | Reciprocal-zeta convexity (2025) | Functional-equation transport proves the alternating sign pattern. | [Alzer-Kwong](https://doi.org/10.1142/S1793042125500897) |
| APP-0002 | Zeta positivity problem (2024) | Moment splitting and tail bounds prove strict positivity. | [Nantomah](https://www.researchgate.net/publication/384676538_Open_Problem_on_Riemann_Zeta_Function) |
| APP-0003 | Generalized Holder inequality (2013) | The Mellin-Planck kernel gives the generalized inequality. | [Sroysang](https://arastirmax.com/en/system/files/dergiler/135290/makaleler/3/1/arastirmax-two-inequalities-riemann-zeta-functions.pdf) |
| APP-0004 | Reciprocal-Gamma curvature (2025) | A Weierstrass-product Laplace kernel proves complete monotonicity. | [Qi-Lim-Nantomah](https://doi.org/10.1186/s13660-024-03245-8) |
| APP-0005 | Zeta-tail floor at s=7 (2018) | Rational telescoping enclosures give the exact floor formula. | [Kim-Song](https://doi.org/10.1186/s13660-018-1743-6) |
| APP-0006 | Zeta-tail floor at s=8 (2018) | Corrected adjacent asymptotic truncations give the exact formula. | [Kim-Song](https://doi.org/10.1186/s13660-018-1743-6) |
| APP-0007 | Digamma product curvature (2025) | A grouped Laplace kernel proves complete monotonicity. | [Qi-Lim-Nantomah](https://doi.org/10.1186/s13660-024-03245-8) |
| APP-0008 | Higher-polygamma curvature (2025) | Dominant-summand certificates refute the stronger CM claim. | [Qi-Lim-Nantomah](https://doi.org/10.1186/s13660-024-03245-8) |
| APP-0009 | Gamma-product threshold (2026) | Endpoint logarithmic derivatives give the exact threshold. | [Bulboaca-Zayed](https://doi.org/10.1186/s13660-025-03425-0) |
| APP-0010 | Nielsen k-beta ratio law (2025) | A Laplace moment-ratio bridge gives the parity-refined theorem. | [Yin-Zhang](https://arxiv.org/abs/2502.15852) |
| APP-0011 | Beta-window endpoint (2025) | A certified rational calculation gives the exact n=2 endpoint. | [Qi-Lim-Nantomah](https://doi.org/10.1186/s13660-024-03245-8) |
| APP-0012 | Baricz Vq log-convexity (2008) | A positive Laplace representation proves strict q-log-convexity. | [Baricz](https://dea.lib.unideb.hu/bitstreams/bdd4469f-1b1e-4996-9b90-73f5e1a6b0e8/download) |
| APP-0013 | pk-digamma necessity (2018) | A near-zero obstruction proves the sharp alpha condition. | [Yin](https://www.ijopcm.org/Vol/2018/2.9.pdf) |
| APP-0014 | Ramanujan integral transform (2025) | The density is CM, so the integral is Stieltjes and its primitive is CBF. | [Mishra-Swaminathan](https://arxiv.org/abs/2511.07443) |
| APP-0015 | Prabhakar Q-measure (2023) | The measure is a stable-subordination push-forward. | [Sibisi](https://arxiv.org/abs/2301.01466) |
| APP-0016 | Mills-ratio derivative bounds (2020) | Determinant inequalities give an all-level bound extractor. | [From](https://doi.org/10.1016/j.jmaa.2020.123872) |
| APP-0017 | Gamma-quotient Bernstein test (2008) | A rational quotient gives a derivative-sign obstruction. | [Baricz](https://doi.org/10.1090/S0002-9939-08-09353-2) |
| APP-0018 | Qi-Guo tau threshold (2004) | The exact value is a nonattained supremum. | [Qi-Guo](https://vuir.vu.edu.au/18037/) |
| APP-0019 | Wakrim W-symbol range (2026) | The remaining Bernstein range closes at beta in [0,1]. | [Wakrim](https://arxiv.org/abs/2601.02876) |
| APP-0020 | Qi h-lambda degree (2020) | Degree-four transforms fail the first-derivative test near zero. | [Qi](https://doi.org/10.3934/math.2020219) |
| APP-0021 | Szabo digamma cutoff (2024) | Source sufficiency plus the zero expansion gives alpha0=1. | [Szabo](https://arxiv.org/abs/2411.17670) |
| APP-0022 | Gurland gamma-ratio LCM (2017) | A Weierstrass product gives a sum of CM second differences. | [Chen-Choi](https://doi.org/10.7153/mia-20-43) |
| APP-0023 | Sokal lambda derivatives (2009) | A generating function gives triangular nonnegative compression. | [Sokal](https://arxiv.org/abs/0902.0065) |
| APP-0024 | Simon gamma quotient (2020) | A complement CM representation proves the quotient is Bernstein. | [Simon](https://doi.org/10.5802/afst.1640) |
| APP-0025 | Du-Wang h3 monotonicity (2022) | A polygamma-ratio kernel gives the exact monotonicity window. | [Du-Wang](https://arxiv.org/abs/2205.12530) |
| APP-0026 | Baskakov even powers (2014) | The alpha=1, r=8 density changes sign, refuting the conjecture. | [Abel-Gawronski-Neuschel](https://arxiv.org/abs/1411.7945) |
| APP-0027 | Ma-Weigert Dk chain (2025) | Tail vanishing and integration prove the derivative-region nesting. | [Ma-Weigert](https://arxiv.org/abs/2505.04225) |
| APP-0028 | Divisor-polygamma parity (2019) | Odd sums are CM, but the even non-CM clause fails at f2. | [Qi-Agarwal](https://doi.org/10.1186/s13660-019-1976-z) |
| APP-0029 | Gamma quotient critical point (2026) | A ratio-kernel proof gives the unique critical point. | [Bulboaca-Zayed](https://doi.org/10.1186/s13660-025-03425-0) |
| APP-0030 | Ramanujan Turan window (2025) | A moment-ratio asymptotic refutes the proposed CM interval. | [Mishra-Swaminathan](https://arxiv.org/abs/2511.07443) |
| APP-0031 | Baricz gamma-quotient Bernstein test (2008) | The universal gamma-quotient Bernstein claim is false via a single explicit counterexample. | [Baricz](https://doi.org/10.1090/S0002-9939-08-09353-2) |
| APP-0032 | From Mills-ratio all-\(L\) bound chain (2020) | A determinant reduction gives alternating explicit bounds for all derivative levels. | [From](https://doi.org/10.1016/j.jmaa.2020.123872) |
| APP-0033 | Ramanujan antiderivative complete Bernstein (2025) | The antiderivative is complete Bernstein. | [Mishra-Swaminathan](https://arxiv.org/abs/2511.07443) |
| APP-0034 | Bulboaca-Zayed gamma quotient monotonicity (2026) | A ratio-kernel proof gives the derivative-sign pattern and critical point behavior on the source interval. | [Bulboaca-Zayed](https://doi.org/10.1186/s13660-025-03425-0) |
| APP-0035 | Keady self-bijection inverse-CM counterexample (2018) | A CM self-bijection with CM inverse failure is given. | [Keady et al.](https://www.ojm.sciendo.com/doi/pdf/10.2478/cogmath-2018-0007) |
| APP-0036 | Baskakov even-line sign-failure (2014) | The \(\alpha=1\), \(r=8\) density in the even-line family changes sign. | [Abel-Gawronski-Neuschel](https://arxiv.org/abs/1411.7945) |
| APP-0037 | Du-Wang \(h_3\) monotonicity classification (2022) | Exact monotonicity window classification on the source interval is established. | [Du-Wang](https://arxiv.org/abs/2205.12530) |
| APP-0038 | Ma-Weigert derivative-sign chain (2025) | Derivative-sign regions for \(L_k\) are nested. | [Ma-Weigert](https://arxiv.org/abs/2505.04225) |
| APP-0039 | Ramanujan Turan window source interval (2025) | The claimed Turan complete-monotonicity interval is false. | [Mishra-Swaminathan](https://arxiv.org/abs/2511.07443) |
| APP-0040 | Yang-Tian Bessel-\(W\) Bernstein conjecture (2022) | The power-Bernstein conjecture is proved on the source interval. | [Yang-Tian](https://doi.org/10.1007/s13163-022-00439-w) |
| APP-0041 | Qi \(h_\lambda\) degree-four conjecture (2020) | Local endpoint expansions refute the degree-four complete-monotonicity conjecture. | [Qi](https://doi.org/10.3934/math.2020219) |
| APP-0042 | Bessel square-root log-concavity (2011) | A rational certificate at \((\nu,u)=(0,10)\) gives positive logarithmic curvature. | [Baricz-Ponnusamy-Vuorinen](https://doi.org/10.1016/j.exmath.2011.07.001) |
| APP-0043 | Bessel Riccati log-concavity inequality (2011) | The same endpoint certificate refutes the universal Riccati inequality. | [Baricz-Ponnusamy-Vuorinen](https://doi.org/10.1016/j.exmath.2011.07.001) |
| APP-0044 | Bessel ratio quadratic lower bound (2011) | The explicit \((\nu,u)=(0,10)\) witness gives the opposite strict inequality. | [Baricz-Ponnusamy-Vuorinen](https://doi.org/10.1016/j.exmath.2011.07.001) |
| APP-0045 | Bessel three-regime certificate route (2011) | The proposed certificate route is refuted because the target inequality is false. | [Baricz-Ponnusamy-Vuorinen](https://doi.org/10.1016/j.exmath.2011.07.001) |

See [`APPLICATIONS.md`](APPLICATIONS.md) for the detailed public application
ledger and source references.

## Public Vault Note

The latest staged theory snapshot is `stage_v014`.  The public wiki vault is
synchronized at [`wiki/latest`](wiki/latest), with the immutable snapshot stored
under [`wiki/versions/stage_v014`](wiki/versions/stage_v014).

## Reading Notes

Start with the PDF for the paper narrative and the LaTeX source for exact
formulas. Human and agent ingestion notes are in [`HUMANS.md`](HUMANS.md) and
[`AGENTS.md`](AGENTS.md).

Repository URL: https://github.com/pudim-project/pudim-ai-demo-zetalaw
