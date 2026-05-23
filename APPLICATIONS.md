# Applications Changelog

This changelog records staged applications of the theory to externally stated problems. Contact/review notes are intentionally minimal.
The same application ids appear in `theory/latest/THEORY.tex` under the manuscript `Applications` section and in the corresponding theorem names.

| id | date | stated problem | solution | status | review |
| --- | --- | --- | --- | --- | --- |
| APP-0001 | 2026-05-17 | Alzer-Kwong convexity and concavity problem | Alzer-Kwong convexity and concavity pattern for reciprocal zeta | solved at THEORY_v006 | no reply |
| APP-0002 | 2026-05-17 | Nantomah zeta positivity problem | Affirmative solution of Nantomah zeta positivity problem | solved at THEORY_v006 | no reply |
| APP-0003 | 2026-05-17 | Sroysang generalized Holder problem | Generalized Holder inequality for Gamma zeta | solved at THEORY_v006 | no reply |
| APP-0004 | 2026-05-17 | Complete monotonicity of $(\log\Gamma(x)+\log\Gamma(1/x))''$ | Complete monotonicity of reciprocal-Gamma curvature | solved at THEORY_v006 | no reply |
| APP-0005 | 2026-05-17 | Exact inverse-tail floor formula at s=7 | Exact inverse-tail floor formula at s=7 | solved at THEORY_v006 | no reply |
| APP-0006 | 2026-05-17 | Exact inverse-tail floor formula at s=8 | Exact inverse-tail floor formula at s=8 | solved at THEORY_v006 | no reply |
| APP-0007 | 2026-05-19 | Concavity or complete monotonicity of the polygamma product P0 | Complete monotonicity of reciprocal digamma product curvature | solved at THEORY_v006 | no reply |
| APP-0008 | 2026-05-19 | Higher-order monotonicity of polygamma products Pn | Counterexample to complete monotonicity of higher-order polygamma product curvature | solved at THEORY_v006 | no reply |
| APP-0009 | 2026-05-23 | Sharp reciprocal Gamma-product monotonicity threshold | APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity | solved at THEORY_v006 | no contact |

## Application Details

### APP-0001: Alzer-Kwong convexity and concavity problem

- source reference: Horst Alzer and Man Kam Kwong, "On the concavity and convexity of $1/\zeta$", International Journal of Number Theory, Vol. 21, No. 8 (2025), 1825-1835. DOI: [DOI](https://doi.org/10.1142/S1793042125500897)
- solution: Alzer-Kwong convexity and concavity pattern for reciprocal zeta
- solution status: proved
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
- solution status: proved
- problem node: `wiki/nodes/mrw-eb9a71666a04.md`
- solution node: `wiki/nodes/mrw-f9e130ed65ef.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no reply

#### Stated problem

Determine whether, for every \(n\in\mathbb N\), 

\[
(n+2)\zeta(n+1)\zeta(n+3) -(n+1)\zeta(n+2)^2 -\zeta(n+1)\zeta(n+2)>0.
\]

### APP-0003: Sroysang generalized Holder problem

- source reference: Banyat Sroysang, "Two Inequalities for the Riemann Zeta Functions", Mathematica Aeterna, Vol. 3, No. 1 (2013), 21-24. [PDF](https://arastirmax.com/en/system/files/dergiler/135290/makaleler/3/1/arastirmax-two-inequalities-riemann-zeta-functions.pdf)
- solution: Generalized Holder inequality for Gamma zeta
- solution status: proved
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
- solution status: proved
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
- solution status: proved
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
- solution status: proved
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
- solution status: proved
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

- source reference: source: Feng Qi, Dongkyu Lim, and Kwara Nantomah, "Monotonicity and positivity of several functions involving ratios and products of polygamma functions", Journal of Inequalities and Applications 2025, article 5.
- solution: Counterexample to complete monotonicity of higher-order polygamma product curvature
- solution status: proved
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

- source reference: source: Teodor Bulboaca and Hanaa M. Zayed, "Monotonic nature of the Gamma function", Journal of Inequalities and Applications 2026, article 27.
- solution: APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity
- solution status: proved
- problem node: `wiki/nodes/mrw-1396775c6089.md`
- solution node: `wiki/nodes/mrw-0fd149ddc79d.md`
- theory version: `v006`
- stage: `stage_v006`
- review status: no contact

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

 then the optimal condition is \(\rho\ge \rho_*\), where numerically \[ \rho_*=1.258396967085 [truncated]
