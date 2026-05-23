---
id: mrw-37dbc6aeedf9
type: problem
title: Biased squarefree residual problem for Erdos 536
aliases: ["mrw-37dbc6aeedf9", "Biased squarefree residual problem for Erdos 536"]
status: open
tags: ["problem", "open", "erdos", "lcm", "squarefree", "biased-measure", "support-tail", "finite-prime", "next-frontier"]
parents: [mrw-277fbbb4ccb9, mrw-e80e409bf536, mrw-f835f9671070, mrw-4daa694d9526, mrw-9afb17b1b84a]
refs: ["references/sources/20260519T053417Z-erdos-536-biased-squarefree-context.md"]
---

# Problem: Biased squarefree residual problem for Erdos 536

## Statement

Let \(P\) be a finite set of primes and put
\[
S_P=\sum_{p\in P}\frac1p.
\]
Let \(\nu_P\) be the product law on \(2^P\) under which the events \(p\in S\) are independent and
\[
\nu_P(p\in S)=\frac1p.
\]
Call a family \(\mathcal F\subseteq2^P\) squarefree cosunflower-free if there are no three distinct members \(A,B,C\in\mathcal F\) such that no prime lies in exactly one of \(A,B,C\).  Equivalently,
\[
A\cup B=A\cup C=B\cup C.
\]

For \(0\le\theta<1\), define the biased squarefree residual
\[
M_P(\theta)=
\sup \nu_P(\mathcal F),
\]
where the supremum runs over all squarefree cosunflower-free families \(\mathcal F\subseteq2^P\) such that
\[
|S|>\theta S_P
\qquad\text{for every }S\in\mathcal F.
\]

The problem is to decide whether, for \(P_k=\{p_1,\ldots,p_k\}\), the first \(k\) primes,
\[
M_{P_k}(\theta)\to0
\qquad(k\to\infty)
\]
for every fixed \(0\le\theta<1\).

If this holds, the next required step is a separate lift from squarefree biased support mass to the exponent-grid prefix-rank residual \(R_P(\theta)\).  If it fails, a nonvanishing family for \(M_{P_k}(\theta)\) would be a genuine obstruction to the squarefree support subproblem, unlike the pointwise binary-choice spike from [[wiki/nodes/mrw-9afb17b1b84a|Binary-choice squarefree obstruction to pointwise support envelopes]].  A failure of this squarefree problem would still need a reverse lift before it becomes a lower-bound obstruction to \(R_P(\theta)\).

## Evidence

- The squarefree cosunflower criterion translates equal pairwise lcm triples in the squarefree model into the condition \(A\cup B=A\cup C=B\cup C\).
- The low-support growing-prime criterion proves that \(R_P(\theta)\to0\) along \(S_P\to\infty\) would imply \(f(N)=o(N)\).  The biased squarefree residual is a first support-level test for whether high-support independent mass can persist.
- The binary-choice construction proves that high support and large pointwise cardinality do not force cosunflowers, but its \(\nu_P\)-mass tends to \(0\).  Therefore it is not a counterexample to \(M_{P_k}(\theta)\to0\).
- The ambient sparsity proposition [[wiki/nodes/mrw-053bc325c601|Ambient cosunflower sparsity for biased squarefree supports]] proves that even the full high-support event has vanishing unconditioned cosunflower triple density under \(\nu_P^3\).  Consequently a proof of \(M_{P_k}(\theta)\to0\) cannot rely only on ambient random-triple supersaturation; it needs structural information about the family.

## Pair-link formulation

For \(A,B\subseteq P\), define the pair-link interval
\[
I(A,B)=\{C\subseteq P:\ A\triangle B\subseteq C\subseteq A\cup B\}
\]
and
\[
I^\circ(A,B)=I(A,B)\setminus\{A,B\}.
\]
Then \(A,B,C\) form a squarefree cosunflower if and only if
\[
C\in I(A,B).
\]
Indeed, if a coordinate belongs to exactly one of \(A,B\), then \(C\) must contain it; if it belongs to both, \(C\) may contain it or not; and if it belongs to neither, \(C\) must not contain it.

Thus \(\mathcal F\) is squarefree cosunflower-free if and only if
\[
\mathcal F\cap I^\circ(A,B)=\varnothing
\]
for every pair of distinct \(A,B\in\mathcal F\).  A sharper next target is therefore the biased pair-link supersaturation problem: for fixed \(\eta>0\) and \(0\le\theta<1\), prove or refute that every \(\mathcal F\subseteq H_{P_k,\theta}\) with \(\nu_{P_k}(\mathcal F)\ge\eta\) has some distinct \(A,B\in\mathcal F\) with
\[
\mathcal F\cap I^\circ(A,B)\ne\varnothing
\]
for all sufficiently large \(k\).  A quantitative version at the natural sparse scale would bypass the ambient-density obstruction from [[wiki/nodes/mrw-053bc325c601|Ambient cosunflower sparsity for biased squarefree supports]].

## Depends on

- [[wiki/nodes/mrw-277fbbb4ccb9|Erdos equal pairwise least-common-multiple problem]]
- [[wiki/nodes/mrw-e80e409bf536|Squarefree cosunflower criterion for equal pairwise lcm triples]]
- [[wiki/nodes/mrw-f835f9671070|Finite-prime weighted-grid reduction for Erdos 536]]
- [[wiki/nodes/mrw-4daa694d9526|Low-support growing-prime criterion for Erdos 536]]
- [[wiki/nodes/mrw-9afb17b1b84a|Binary-choice squarefree obstruction to pointwise support envelopes]]

## Used by

- Next #536 route: prove or refute the biased pair-link supersaturation formulation of \(M_{P_k}(\theta)\), then audit whether the result lifts to the prefix-rank residual \(R_P(\theta)\).

## Notes

- This is an open squarefree support problem, not the full \(R_P(\theta)\) problem.
- The high-support condition is relative to the biased mean \(S_P\), not to \(|P|\).  For the first \(k\) primes, \(S_{P_k}\to\infty\) slowly.
- A global squarefree family theorem is not automatically enough for \(R_P(\theta)\), because \(R_P(\theta)\) is a prefix-rank envelope and extremizers may vary with \(t\).
- The parameter \(\theta\) is fixed.  If \(\theta=\theta_P\to1\), the lower-tail estimates require a separate condition such as \((1-\theta_P)^2S_P\to\infty\).
