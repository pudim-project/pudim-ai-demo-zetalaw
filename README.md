# Zeta-Law Entropy, Gamma Curvature, and Laplace-Measure Applications

Powered by the [Pudim AI Project](https://github.com/pudim-project/pudim-project).

This repository contains the public staged theory for the zetalaw-demov2
research track.  The latest snapshot is `THEORY_v011`, staged on 2026-06-03.

## Public Theory

- Latest TeX: [`theory/latest/THEORY.tex`](theory/latest/THEORY.tex)
- Latest PDF: [`theory/latest/THEORY.pdf`](theory/latest/THEORY.pdf)
- Versioned TeX: [`theory/versions/v011/THEORY_v011.tex`](theory/versions/v011/THEORY_v011.tex)
- Versioned PDF: [`theory/versions/v011/THEORY_v011.pdf`](theory/versions/v011/THEORY_v011.pdf)

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

Version v009 added a new Laplace-transport layer. Those applications are
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

Version v011 adds four further applications. The new applications solve the
Ma-Weigert derivative-region chain assertion, correct the Qi-Agarwal/Yin
divisor-polygamma parity problem, prove the Bulboaca-Zayed Gamma quotient
one-critical-point theorem, and refute the Mishra-Swaminathan Ramanujan
integral Turan-window complete-monotonicity interval.

The public ledger now contains thirty applications with uniform status
`Solved`.

## Applications

All entries below are `Solved`; detailed statements, proofs, and review notes
are in [`APPLICATIONS.md`](APPLICATIONS.md).

- `APP-0001`: Alzer-Kwong reciprocal-zeta convexity pattern; [source](https://doi.org/10.1142/S1793042125500897).
- `APP-0002`: Nantomah zeta positivity problem; [source](https://www.researchgate.net/publication/384676538_Open_Problem_on_Riemann_Zeta_Function).
- `APP-0003`: Sroysang generalized Holder inequality; [source](https://arastirmax.com/en/system/files/dergiler/135290/makaleler/3/1/arastirmax-two-inequalities-riemann-zeta-functions.pdf).
- `APP-0004`: reciprocal-Gamma curvature complete monotonicity; [source](https://doi.org/10.1186/s13660-024-03245-8).
- `APP-0005`: reciprocal-tail floor formula at \(s=7\); [source](https://doi.org/10.1186/s13660-018-1743-6).
- `APP-0006`: reciprocal-tail floor formula at \(s=8\); [source](https://doi.org/10.1186/s13660-018-1743-6).
- `APP-0007`: reciprocal-digamma product curvature; [source](https://doi.org/10.1186/s13660-024-03245-8).
- `APP-0008`: higher-polygamma product curvature counterexample; [source](https://doi.org/10.1186/s13660-024-03245-8).
- `APP-0009`: reciprocal Gamma-product sharp threshold; [source](https://doi.org/10.1186/s13660-025-03425-0).
- `APP-0010`: Nielsen \(k\)-beta derivative-ratio law; [source](https://arxiv.org/abs/2502.15852).
- `APP-0011`: exact \(n=2\) beta-window endpoint; [source](https://doi.org/10.1186/s13660-024-03245-8).
- `APP-0012`: Baricz \(V_q\) strict \(q\)-log-convexity; [source](https://dea.lib.unideb.hu/bitstreams/bdd4469f-1b1e-4996-9b90-73f5e1a6b0e8/download).
- `APP-0013`: Yin \((p,k)\)-digamma sharp \(\alpha\)-necessity; [source](https://www.ijopcm.org/Vol/2018/2.9.pdf).
- `APP-0014`: Ramanujan integral Stieltjes and complete-Bernstein classification; [source](https://arxiv.org/abs/2511.07443).
- `APP-0015`: Prabhakar Q-measure stable-subordination representation; [source](https://arxiv.org/abs/2301.01466).
- `APP-0016`: Mills-ratio all-derivative-level bound extractor; [source](https://doi.org/10.1016/j.jmaa.2020.123872).
- `APP-0017`: gamma-quotient Bernstein-for-all counterexample; [source](https://doi.org/10.1090/S0002-9939-08-09353-2).
- `APP-0018`: Qi-Guo tau-threshold supremum correction; [source](https://vuir.vu.edu.au/18037/).
- `APP-0019`: Wakrim W-symbol exact Bernstein range; [source](https://arxiv.org/abs/2601.02876).
- `APP-0020`: Qi \(h_\lambda\) degree-four conjecture refutation; [source](https://doi.org/10.3934/math.2020219).
- `APP-0021`: Szabo digamma-cutoff theorem; [source](https://arxiv.org/abs/2411.17670).
- `APP-0022`: Chen-Choi Gurland gamma-ratio logarithmic complete monotonicity; [source](https://doi.org/10.7153/mia-20-43).
- `APP-0023`: Sokal generalized-Stieltjes lambda-derivative compression; [source](https://arxiv.org/abs/0902.0065).
- `APP-0024`: Simon gamma-quotient Bernstein problem; [source](https://doi.org/10.5802/afst.1640).
- `APP-0025`: Du-Wang \(h_3\) monotonicity classification; [source](https://arxiv.org/abs/2205.12530).
- `APP-0026`: Baskakov even-power complete-monotonicity conjecture refutation; [source](https://arxiv.org/abs/1411.7945).
- `APP-0027`: Ma-Weigert log-function derivative-region chain; [source](https://arxiv.org/abs/2505.04225).
- `APP-0028`: Qi-Agarwal/Yin divisor-polygamma parity correction; [source](https://doi.org/10.1186/s13660-019-1976-z).
- `APP-0029`: Bulboaca-Zayed Gamma quotient one-critical-point theorem; [source](https://doi.org/10.1186/s13660-025-03425-0).
- `APP-0030`: Ramanujan integral Turan-window refutation; [source](https://arxiv.org/abs/2511.07443).

See [`APPLICATIONS.md`](APPLICATIONS.md) for the detailed public application
ledger and source references.

## Public Vault Note

The latest staged theory snapshot is `stage_v011`.  The public wiki vault may
lag the staged theory and should be regenerated separately before being treated
as the current public node graph.

## Reading Notes

Start with the PDF for the paper narrative and the LaTeX source for exact
formulas. Human and agent ingestion notes are in [`HUMANS.md`](HUMANS.md) and
[`AGENTS.md`](AGENTS.md).

Repository URL: https://github.com/pudim-project/pudim-ai-demo-zetalaw
