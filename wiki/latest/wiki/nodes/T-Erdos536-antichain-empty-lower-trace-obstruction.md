---
id: "T-Erdos536-antichain-empty-lower-trace-obstruction"
type: "theorem"
title: "Erdos536 antichain empty lower trace obstruction"
status: "proved"
tags: ["antichain", "erdos-536", "lower-trace", "obstruction", "proved", "student-proof", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private Oracle audit", "private proof note"]
---

# Theorem: Erdos536 antichain empty lower trace obstruction

## Statement

Antichain empty-lower-trace obstruction: if \(\mathcal A\subseteq2^{P_k}\) is an antichain, then \(\mathcal L_{\mathcal A}(C)=\varnothing\) for every \(C\in\mathcal A\). Thus lower traces cannot be inferred from positive family membership alone.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private Oracle audit`
- `private proof note`

## Proof

For \(\mathcal F_k\subseteq 2^{P_k}\) and occupied top \(C\in\mathcal F_k\), write
\[
\mathcal L_{\mathcal F_k}(C)=\{A\in\mathcal F_k:A\subsetneq C\}.
\]
When this set is nonempty and a lower-trace law \(\mu_C\) is chosen, let \(\lambda_C\) be the push-forward under \(A\mapsto C\setminus A\), and use the already true conditional coverage statistic
\[
\Omega_k(C)=\lambda_C^{\otimes2}\{(D,E):D\cap E=\varnothing\}.
\]

Node promoted: the Erdos536 lower trace rich poor dichotomy.

For any choice of top law \(\tau_k\) on occupied tops and any threshold \(\delta_k\ge0\), exactly one of the following alternatives holds:
\[
\tau_k\{C:\mathcal L_{\mathcal F_k}(C)\ne\varnothing\}<\delta_k
\]
or
\[
\tau_k\{C:\mathcal L_{\mathcal F_k}(C)\ne\varnothing\}\ge\delta_k.
\]
In the first branch, defect laws are not available on enough tops and the family must be handled by a lower-trace-poor comparable-pair/entropy argument. In the second branch, one may condition \(\tau_k\) on the nonempty lower-trace event and begin the defect-law program.

This is a tautological but important partition. It prevents using defect laws before their support exists. It does not prove either branch favorable for Erdos536.

Node promoted: the Erdos536 antichain empty lower trace obstruction.

If \(\mathcal A\subseteq2^{P_k}\) is an antichain, then
\[
\mathcal L_{\mathcal A}(C)=\varnothing
\quad\text{for every } C\in\mathcal A.
\]
Indeed, a lower trace \(A\in\mathcal A\) with \(A\subsetneq C\) would be a comparable pair in \(\mathcal A\), contradicting the antichain property.

Consequently, exact-rank families and any genuine antichain template show that lower traces cannot be inferred from family membership alone. This does not refute the Erdos536 frontier, because exact-rank or narrow-rank mass may be negligible or rank-thin under the intended prime-biased law. It refutes only the invalid proof step "positive mass alone gives lower traces."

Node promoted: the Erdos536 core shield lexicographic complexity well founded.

For a finite model, any lexicographic tuple
\[
\mathcal C=(\ell_{\mathrm{end}}, w_{\mathrm{core}}, m_{\mathrm{avail}}, r_{\mathrm{width}})
\in\mathbb N^4
\]
ordered lexicographically is well-founded. Therefore, if a core/shield descent proof defines these four nonnegative integer quantities and proves strict lexicographic decrease at every descent step, then the descent terminates.

This promotes only the bookkeeping lemma. It does not prove that fixed cores, moving cores, or endpoint shields actually decrease this complexity.

Candidate: the Erdos536 lower trace abundance or few comparables countertemplate.

The lower-trace-rich/poor dichotomy and antichain obstruction were proved, but the AP candidate demanded more: either a positive lower-trace abundance theorem for every admissible positive-mass non-rank-thin family, or a full positive-mass non-rank-thin few-comparables countertemplate.

Neither side was completed. The exact-rank antichain obstruction is structurally valid, but it may be rank-thin and measure-negligible in the target regime. Thus it is not yet the requested positive-mass non-rank-thin countertemplate.

Candidate: the Erdos536 terminating core shield descent complexity.

The well-founded complexity bookkeeping is true. However, no branch proof was found showing that common-core, moving-core, or endpoint-shield normalization strictly decreases
\[
(\ell_{\mathrm{end}}, w_{\mathrm{core}}, m_{\mathrm{avail}}, r_{\mathrm{width}}).
\]
Thus the descent theorem remains open. The next proof must define these quantities from the actual lower-trace-rich model and prove decrease in at least one branch.

Candidate: the Erdos536 separated window disjointness or sparse matching construction.

No separated-window disjointness theorem was proved, and no actual sparse-matching lower-trace family was constructed. The correct ordering is now clear: this candidate should only be attacked inside the lower-trace-rich branch, after common-core and endpoint-shield concentration have either been excluded or explicitly included in the hypotheses.

The abstract matching obstruction remains a valid warning but is secondary to the lower-trace existence gate.

the Erdos536 lower trace rich poor dichotomy: true.
the Erdos536 antichain empty lower trace obstruction: true.
the Erdos536 core shield lexicographic complexity well founded: true.
the Erdos536 lower trace abundance or few comparables countertemplate: candidate_open.
the Erdos536 terminating core shield descent complexity: candidate_open.
the Erdos536 separated window disjointness or sparse matching construction: candidate_open.
the Erdos536 coordinate coverage lower trace forces fork: remains open.
the Erdos536 prime biased weighted union free frontier: remains open.

_Proof source: `private proof note`._

## Tags

`antichain`, `erdos-536`, `lower-trace`, `obstruction`, `proved`, `student-proof`, `theorem`, `true`
