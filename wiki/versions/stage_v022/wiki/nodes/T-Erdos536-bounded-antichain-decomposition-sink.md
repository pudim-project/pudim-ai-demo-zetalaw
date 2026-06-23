---
id: "T-Erdos536-bounded-antichain-decomposition-sink"
type: "theorem"
title: "Erdos536 bounded antichain decomposition sink"
status: "proved"
tags: ["antichain-decomposition", "erdos-536", "prime-biased", "proved", "student-proof", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["attack-plans/AP-20260606T2240-erdos536-lym-reduction-multiplicity.json", "librarian/audits/LA-20260606T2252-erdos536-lym-reduction-multiplicity-depletion-student.json", "oracle/responses/OS-20260606T234056Z-oracle-response.md", "raw/oracle/RO-OS-20260606T234056Z.json", "raw/student/20260606T2252-erdos536-lym-reduction-multiplicity-depletion.md"]
---

# Theorem: Erdos536 bounded antichain decomposition sink

## Statement

Bounded antichain-decomposition sink: under the prime-biased product law, if \(\mathcal F_k\) is a union of \(M_k\) antichains and \(M_k=o(\sqrt{V_k})\), with \(V_k=\sum_{i\le k}(1/p_i)(1-1/p_i)\), then \(\nu_k(\mathcal F_k)=o(1)\).

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `attack-plans/AP-20260606T2240-erdos536-lym-reduction-multiplicity.json`
- `librarian/audits/LA-20260606T2252-erdos536-lym-reduction-multiplicity-depletion-student.json`
- `oracle/responses/OS-20260606T234056Z-oracle-response.md`
- `raw/oracle/RO-OS-20260606T234056Z.json`
- `raw/student/20260606T2252-erdos536-lym-reduction-multiplicity-depletion.md`

## Proof

Node promoted: the Erdos536 weighted antichain sink prime biased product law.

Let \(a_i=q_i/(1-q_i)>0\), \(a(S)=\prod_{i\in S}a_i\), and
\[
e_r(a)=\sum_{|S|=r}a(S).
\]
The weighted LYM inequality says that every antichain \(\mathcal A\subseteq2^{[k]}\) satisfies
\[
\sum_{S\in\mathcal A}{a(S)\over e_{|S|}(a)}\le1.
\]
For integer weights this follows by replacing coordinate \(i\) with a rank-one star having \(a_i\) atoms and applying the ordinary LYM inequality for products of normal ranked posets. Rational and real positive weights follow by scaling and approximation.

For the product law \(\nu_k\),
\[
\nu_k(S)= {a(S)\over\prod_{i\le k}(1+a_i)},
\qquad
\nu_k(|S|=r)= {e_r(a)\over\prod_{i\le k}(1+a_i)}.
\]
Thus
\[
\nu_k(\mathcal A)
=\sum_r\nu_k(|S|=r)\sum_{S\in\mathcal A, |S|=r}{a(S)\over e_r(a)}
\le \sup_r\nu_k(|S|=r).
\]
For \(q_i=1/p_i\), the already proved rank anti-concentration gives
\[
\sup_r\nu_k(|S|=r)\le C V_k^{-1/2},
\qquad
V_k=\sum_{i\le k}{1\over p_i}\left(1-{1\over p_i}\right)\to\infty.
\]
Therefore every antichain has \(\nu_k\)-mass \(o(1)\).

Node promoted: the Erdos536 bounded antichain decomposition sink.

If \(\mathcal F_k=\bigcup_{j=1}^{M_k}\mathcal A_{k,j}\) is a union of antichains, then
\[
\nu_k(\mathcal F_k)\le \sum_{j=1}^{M_k}\nu_k(\mathcal A_{k,j})
\le M_k C V_k^{-1/2}.
\]
Hence \(M_k=o(\sqrt{V_k})\) implies \(\nu_k(\mathcal F_k)=o(1)\). This is the usable intermediate sink when source admissibility gives bounded height or bounded antichain decomposition rather than a single antichain.

Node promoted: the Erdos536 finite core conditional antichain sink.

Fix a finite coordinate set \(J\) and condition on any pattern inside \(J\). The tail coordinates \(i\notin J\) remain independent with probabilities \(1/p_i\), and
\[
\sum_{J<i\le k}{1\over p_i}\left(1-{1\over p_i}\right)\to\infty.
\]
Applying the weighted antichain sink to the tail shows that every tail antichain has conditional mass \(o(1)\). Thus a fixed finite-core shield cannot by itself produce a positive-mass high-support antichain obstruction; it is a core/shield descent state.

Node introduced open: the Erdos536 moving base high multiplicity obstruction schema.

The clean antichain obstruction is now closed. The uncontrolled multiplicity block model is still only a product-measure toy unless it can avoid three sinks: weighted antichain decay, bounded antichain-decomposition decay, and finite-core conditional antichain decay. A genuine obstruction must therefore use moving bases, source admissibility, high support, non-rank-thinness, and unbounded lower-trace multiplicity not reducible to fixed-core stars or bounded antichain decompositions.

Candidate: the Erdos536 weighted LYM normalized matching resolution.

The weighted LYM inequality and rank anti-concentration prove the weighted antichain sink for the prime-biased product law. No positive-mass antichain counterexample exists under \(\nu_k\).

Candidate: the Erdos536 lower trace poor residual union free reduction.

The product-measure antichain sink is now available, but this pass did not prove that lower-trace-poor admissibility reduces to antichain or bounded antichain decomposition after removing rank-thin/top-thin mass. The residual source-specific union-free/lower-trace condition remains to be named precisely.

Candidate: the Erdos536 uncontrolled multiplicity block admissibility test.

The finite-core conditional sink shows that fixed finite-core stars are not terminal antichain obstructions. However, this pass did not prove that the uncontrolled multiplicity block model is source-forbidden, rank-thin, shielded, or admissible. The remaining obstruction must be a moving-base high-multiplicity model if it exists.

the Erdos536 weighted antichain sink prime biased product law: true.
the Erdos536 bounded antichain decomposition sink: true.
the Erdos536 finite core conditional antichain sink: true.
the Erdos536 moving base high multiplicity obstruction schema: open.
the Erdos536 weighted LYM normalized matching resolution: depleted by the true weighted antichain sink.
the Erdos536 lower trace poor residual union free reduction: candidate_open.
the Erdos536 uncontrolled multiplicity block admissibility test: candidate_open.
the Erdos536 coordinate coverage lower trace forces fork: remains open.
the Erdos536 prime biased weighted union free frontier: remains open.

_Proof source: `raw/student/20260606T2252-erdos536-lym-reduction-multiplicity-depletion.md`._

## Tags

`antichain-decomposition`, `erdos-536`, `prime-biased`, `proved`, `student-proof`, `theorem`, `true`
