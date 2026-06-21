---
id: "T-Erdos536-multiplicity-controlled-deletion-decay-criterion"
type: "theorem"
title: "Erdos536 multiplicity controlled deletion decay criterion"
status: "proved"
tags: ["deletion-transport", "erdos-536", "lower-trace", "multiplicity", "proved", "student-proof", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private Oracle audit", "private proof note"]
---

# Theorem: Erdos536 multiplicity controlled deletion decay criterion

## Statement

Multiplicity-controlled deletion decay criterion: for an actual lower-trace relation \(R\subseteq\{(C,A,D):A=C\setminus D\}\), let \(W(C)=\sum_{D:(C,C\setminus D,D)\in R}\prod_{i\in D}(p_i-1)\). If every lower trace has multiplicity at most \(M_k\) and active tops satisfy \(W(C)\ge L_k\), then their \(\nu_k\)-mass is at most \(M_k/L_k\). In particular, if \(M_k/L_k\to0\), the active-top mass vanishes.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private Oracle audit`
- `private proof note`

## Proof

Node promoted: the Erdos536 multiplicity controlled deletion decay criterion.

Let
\[
R\subseteq\{(C,A,D):A=C\setminus D\}
\]
be an actual lower-trace relation and define
\[
W(C)=\sum_{D:(C,C\setminus D,D)\in R}\prod_{i\in D}(p_i-1).
\]
By product deletion mass transport,
\[
\sum_C\nu_k(C)W(C)=\sum_{(C,A,D)\in R}\nu_k(A).
\]
If each lower trace \(A\) has multiplicity at most \(M_k\), then
\[
\sum_{(C,A,D)\in R}\nu_k(A)
\le M_k\sum_A\nu_k(A)
\le M_k.
\]
If active tops satisfy \(W(C)\ge L_k\), their mass is therefore at most \(M_k/L_k\). Thus \(M_k/L_k\to0\) forces active-top mass to vanish.

This is a conditional sink. It proves decay only after multiplicity is controlled relative to deletion weight.

Node promoted: the Erdos536 prime biased rank level anticoncentration.

Let \(B_i\sim\operatorname{Bernoulli}(q_i)\) independently with \(q_i=1/p_i\), and set
\[
X_k=\sum_{i\le k}B_i,
\qquad
V_k=\sum_{i\le k}q_i(1-q_i).
\]
Because \(q_i\le1/2\), \(V_k\asymp\sum_{i\le k}1/p_i\to\infty\). For the characteristic function \(\phi(t)=\mathbb E e^{itX_k}\),
\[
|1-q_i+q_i e^{it}|^2
=1-2q_i(1-q_i)(1-\\cos t).
\]
Using \(1-u\le e^{-u}\),
\[
|\phi(t)|\le \exp(-c V_k t^2)
\]
for \(|t|\le\pi\), with an absolute constant \(c>0\) after using \(1-
\cos t\gg t^2\) on \([-\pi,\pi]\). Fourier inversion gives
\[
\sup_m\mathbb P(X_k=m)
\le {1\over2\pi}\int_{-\pi}^{\pi}|\phi(t)|\,dt
\le C V_k^{-1/2}.
\]
Hence every single rank level has \(\nu_k\)-mass \(o(1)\).

This is not yet the full weighted antichain sink: an antichain may mix ranks unless a weighted LYM/normalized-matching theorem is audited.

Node promoted: the Erdos536 uncontrolled multiplicity block model.

Choose a tail block \(I_k\) of large prime indices such that
\[
1\le \sum_{i\in I_k}{1\over p_i}\le2,
\qquad
\max_{i\in I_k}{1\over p_i}\to0.
\]
For any base family \(\mathcal B_k\) on coordinates outside \(I_k\), define tops
\[
C=A\cup\{i\},\qquad A\in\mathcal B_k,\\ i\in I_k,
\]
and delete \(D=\{i\}\), so every such top maps to the trace \(A\). Thus each trace \(A\) has multiplicity \(|I_k|\), which tends to infinity along such tail blocks.

The tail event of selecting exactly one coordinate in \(I_k\) has probability
\[
\sum_{i\in I_k}{1\over p_i}\prod_{j\in I_k\setminus\{i\}}\left(1-{1\over p_j}\right),
\]
which is bounded below by a positive absolute constant because the total tail weight is in \([1,2]\) and the maximum atom tends to zero. Therefore uncontrolled multiplicity can coexist with positive product-measure mass at the product-measure model level.

This model is not claimed to satisfy Erdos536 admissibility. It proves that multiplicity escape is a real product-measure phenomenon that must be excluded by source structure, rank-thinness, or shielding.

Node introduced open: the Erdos536 weighted LYM normalized matching gap.

Rank-level anti-concentration proves small mass for each level. It does not by itself prove that every antichain has small mass under unequal Bernoulli weights. The remaining product-measure step is a weighted LYM or normalized-matching theorem for the rank-conditioned prime-biased measure. The remaining source step is a separate reduction from lower-trace-poor admissibility to antichain or comparable-pair exclusion.

Candidate: the Erdos536 multiplicity controlled deletion sink or uncontrolled multiplicity.

The multiplicity-controlled deletion decay criterion proves the conditional sink. The uncontrolled multiplicity block model proves that uncontrolled multiplicity is not artificial at the product-measure level. The candidate remains open because no Erdos536-specific multiplicity upper bound was proved and the block model was not shown admissible, high-support, non-rank-thin, and lower-trace-poor in the exact source geometry.

Candidate: the Erdos536 prime biased weighted antichain sink reduction.

Rank-level anti-concentration was proved. The full weighted antichain sink was not promoted because this pass did not prove the needed weighted LYM/normalized-matching inequality for unequal Bernoulli measures. The source-specific reduction from lower-trace-poor admissibility to antichain/comparable-pair exclusion also remains unproved.

Candidate: the Erdos536 design moving coordinate multiplicity fork.

The conditional deletion criterion and uncontrolled multiplicity model clarify the fork: design near-top shadows and moving-coordinate escapes vanish under subcritical multiplicity and divergent deletion weights, but can evade mass transport through uncontrolled multiplicity. This pass did not prove endpoint shielding, rank-thinness, source admissibility failure, or a full obstruction model for spread designs or moving cores.

the Erdos536 multiplicity controlled deletion decay criterion: true conditional sink.
the Erdos536 prime biased rank level anticoncentration: true rank-level anti-concentration.
the Erdos536 uncontrolled multiplicity block model: true product-measure obstruction model.
the Erdos536 weighted LYM normalized matching gap: open obstruction.
the Erdos536 multiplicity controlled deletion sink or uncontrolled multiplicity: candidate_open.
the Erdos536 prime biased weighted antichain sink reduction: candidate_open.
the Erdos536 design moving coordinate multiplicity fork: candidate_open.
the Erdos536 coordinate coverage lower trace forces fork: remains open.
the Erdos536 prime biased weighted union free frontier: remains open.

_Proof source: `private proof note`._

## Tags

`deletion-transport`, `erdos-536`, `lower-trace`, `multiplicity`, `proved`, `student-proof`, `theorem`, `true`
