---
id: "T-Erdos536-large-defect-local-trace-shield-zero-coverage"
type: "theorem"
title: "Erdos 536 large defect local trace shield has zero pair coverage and high mass under sparse product laws"
status: "proved"
tags: ["coverage-avoidance", "diagnostic", "erdos-536", "local-trace", "proved", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T185247-erdos536-two-statistic-lower-trace-student.json", "raw/student/20260531T185247-erdos536-two-statistic-lower-trace.md"]
---

# Theorem: Erdos 536 large defect local trace shield has zero pair coverage and high mass under sparse product laws

## Statement

Let \(C_m\) be a finite set with \(|C_m|=m\), and let \(\mathcal T_m=\{A\subseteq C_m: |A|\le m/2-1\}\). Then no two members of \(\mathcal T_m\) have union \(C_m\). Moreover, for any product law \(\mu_m\) on \(C_m\) with \(\mathbf E_{\mu_m}|A|=o(m)\), one has \(\mu_m(\mathcal T_m)\to1\).

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T185247-erdos536-two-statistic-lower-trace-student.json`
- `raw/student/20260531T185247-erdos536-two-statistic-lower-trace.md`

## Proof

\emph{Setup.}
Let
\[
S_k=\sum_{i\le k}\frac1{p_i},
\qquad
\nu_k(p_i\in S)=\frac1{p_i},
\qquad
H_{k,\theta}=\{S\subseteq P_k: |S|>\theta S_k\}.
\]
For \(C\subseteq P_k\), let \(\mu_C\) be the prime-biased product law on subsets of \(C\), and let
\[
\mathcal L_{\mathcal F_k}(C)=\{A\in\mathcal F_k:A\subsetneq C\}.
\]
The AP separated two different lower-trace quantities:

a lower-trace mass quantity, \(\mu_C(\mathcal L_{\mathcal F_k}(C))\);
an existential coordinate-coverage quantity,
\[
\Omega_k(C)=\mu_C^{\otimes2}
\{(A,B)\in\mathcal L_{\mathcal F_k}(C)^2:
A\ne B,\ A\cup B=C\}.
\]

The first quantity is measure-size information. The second quantity is mostly support information: because every finite atom of \(\mu_C\) has positive mass, \(\Omega_k(C)>0\) exactly when a covering pair exists below \(C\).

Candidate:
the Erdos536 lower trace mass positive on rank diffuse tops.

This candidate is refuted. The refutation is the full high-support family
\[
\mathcal F_k=H_{k,\theta}.
\]
First, \(\nu_k(H_{k,\theta})\to1\). Indeed, \(\mathbf E_{\nu_k}|S|=S_k\) and
\[
\operatorname{Var}_{\nu_k}(|S|)
=\sum_{i\le k}\frac1{p_i}\left(1-\frac1{p_i}\right)
\le S_k,
\]
so Chebyshev gives
\[
\nu_k(|S|\le\theta S_k)
\le \frac{1}{(1-\theta)^2S_k}\to0
\]
for fixed \(0<\theta<1\). This family is not rank-thin: any \(o(\sqrt{S_k})\) collection of exact ranks carries \(o(1)\) mass by the Erdos536 rank block anti concentration, while \(H_{k,\theta}\) has mass tending to one.

Now condition on \(C\in H_{k,\theta}\). Put
\[
W(C)=\sum_{p_i\in C}\frac1{p_i}.
\]
If \(A\sim\mu_C\), then \(\mathbf E_{\mu_C}|A|=W(C)\), hence Markov's inequality gives
\[
\mu_C(\mathcal L_{H_{k,\theta}}(C))
\le
\mu_C(|A|>\theta S_k)
\le
\frac{W(C)}{\theta S_k}.
\]
Under the outer law \(C\sim\nu_k\),
\[
\mathbf E_{\nu_k}W(C)
=\sum_{i\le k}\frac1{p_i^2}
\le \sum_p\frac1{p^2}
<\infty.
\]
Therefore
\[
\mathbf E_{\nu_k}\!\left[
\mu_C(\mathcal L_{H_{k,\theta}}(C))
\mid C\in H_{k,\theta}
\right]
\le
\frac{\sum_{i\le k}p_i^{-2}}
{\theta S_k\,\nu_k(H_{k,\theta})}
\to0.
\]
Consequently, for every fixed \(\delta>0\),
\[
\nu_k\!\left(
C\in H_{k,\theta}:
\mu_C(\mathcal L_{H_{k,\theta}}(C))\ge\delta
\mid C\in H_{k,\theta}
\right)\to0.
\]
Thus a positive-mass, non-rank-thin family can have vanishing biased lower-trace mass below typical occupied tops. The lower-trace mass statistic in this AP is the wrong strength: the source problem only needs existence of covering pairs, not nonnegligible \(\mu_C\)-mass of the lower trace.

Admitted true nodes:
\[
the Erdos536 full high support family has vanishing biased lower trace mass,
\quad
T\text{-not-Erdos536-lower-trace-mass-positive-on-rank-diffuse-tops}.
\]

Candidate:
the Erdos536 coordinate coverage lower trace forces fork.

No proof was found. The refutation of Candidate 1 does not refute this route, because \(\Omega_k(C)>0\) is an existential condition. The covering pair can have extremely small \(\mu_C^{\otimes2}\)-mass and still contradict union-freeness.

The full high-support family illustrates the distinction. If \(C\in H_{k,\theta}\) and \(|C|>\theta S_k+1\), then for distinct \(x,y\in C\),
\[
A=C\setminus\{x\},
\qquad
B=C\setminus\{y\}
\]
both lie in \(H_{k,\theta}\), are proper subsets of \(C\), and satisfy \(A\cup B=C\). Thus \(H_{k,\theta}\) has coordinate coverage even though its biased lower-trace mass tends to zero.

For a general positive-mass non-rank-thin family, the missing theorem is still open:
\[
\text{broad rank support}
\quad\Longrightarrow\quad
\exists C\in\mathcal F_k,\ \exists A,B\in\mathcal F_k,\ A,B\subsetneq C,\ A\cup B=C.
\]
Equivalently, for some occupied top \(C\), the complement family
\[
\mathcal U_C=\{C\setminus A:A\in\mathcal L_{\mathcal F_k}(C)\}
\]
must contain two disjoint members. I could not prove that positive mass and non-rank-thinness force this.

Candidate:
the Erdos536 diagnostic many fiber coverage avoidance construction.

A precise local coverage-avoidance shield was found, but it is not a source counterexample and does not fully settle the candidate's many-fiber/global requirements.

Let \(C_m\) be a set of \(m\) coordinates and define
\[
\mathcal T_m=\{A\subseteq C_m: |A|\le m/2-1\}.
\]
For \(A,B\in\mathcal T_m\), the complements
\[
C_m\setminus A,
\qquad
C_m\setminus B
\]
both have size at least \(m/2+1\), so they intersect. Hence
\[
A\cup B\ne C_m
\]
for all \(A,B\in\mathcal T_m\). Equivalently,
\[
\mu_m^{\otimes2}\{(A,B)\in\mathcal T_m^2:A\ne B,\ A\cup B=C_m\}=0
\]
for every product law \(\mu_m\) on \(C_m\).

If the product law has \(\mathbf E_{\mu_m}|A|=o(m)\), then Markov gives
\[
\mu_m(\mathcal T_m^c)
=\mu_m(|A|\ge m/2)
\le \frac{2\mathbf E_{\mu_m}|A|}{m}
\to0.
\]
Thus \(\mathcal T_m\) can have asymptotically full local trace mass and zero pair coverage. This is not an exact-rank layer, not an \(o(\sqrt{S_k})\) rank block as a support template, not a chain, and not an endpoint-pair shield. It is a complement-intersection shield.

However, this is only a local trace model. It does not build a global high-support union-free family of positive \(\nu_k\)-mass. In particular, the global family generated by such low-side traces has many internal forks, and the construction does not enforce the source condition across different tops.

\[
the Erdos536 large defect local trace shield zero coverage.
\]

the Erdos536 lower trace mass positive on rank diffuse tops: candidate_refuted;
the Erdos536 coordinate coverage lower trace forces fork: candidate_open;
the Erdos536 diagnostic many fiber coverage avoidance construction: candidate_open, with a local true shield admitted.

No Erdos 536 theorem was solved and no source counterexample was constructed. The main correction is conceptual: biased lower-trace mass is too strong and can vanish even for the full high-support family. The next proof route should use support-level lower shadows and complement-intersection structure, not \(\mu_C\)-mass lower bounds.

_Proof source: `raw/student/20260531T185247-erdos536-two-statistic-lower-trace.md`._

## Tags

`coverage-avoidance`, `diagnostic`, `erdos-536`, `local-trace`, `proved`, `theorem`, `true`
