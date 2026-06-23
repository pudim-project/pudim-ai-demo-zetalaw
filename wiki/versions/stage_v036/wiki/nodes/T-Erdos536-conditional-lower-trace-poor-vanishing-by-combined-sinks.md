---
id: "T-Erdos536-conditional-lower-trace-poor-vanishing-by-combined-sinks"
type: "theorem"
title: "Erdos536 conditional lower trace poor vanishing by combined sinks"
status: "proved"
tags: ["combined-sinks", "conditional-vanishing", "erdos-536", "lower-trace-poor", "proved", "student-proof", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["attack-plans/AP-20260606T2305-erdos536-source-geometry-vanishing.json", "librarian/audits/LA-20260606T2318-erdos536-source-geometry-vanishing-depletion-student.json", "oracle/responses/OS-20260606T235319Z-oracle-response.md", "raw/oracle/RO-OS-20260606T235319Z.json", "raw/student/20260606T2318-erdos536-source-geometry-vanishing-depletion.md"]
---

# Theorem: Erdos536 conditional lower trace poor vanishing by combined sinks

## Statement

Conditional lower-trace-poor vanishing by combined sinks: if a lower-trace-poor active branch outside negligible rank-thin/top-thin mass splits into an antichain-covered part with \(M_k=o(\sqrt{V_k})\) and a deletion-transport part whose active tops satisfy deletion weight lower bound \(L_k\) and trace multiplicity bound \(M_k^{\prime}\) with \(M_k^{\prime}/L_k\to0\), then the whole branch has \(\nu_k\)-mass tending to zero.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `attack-plans/AP-20260606T2305-erdos536-source-geometry-vanishing.json`
- `librarian/audits/LA-20260606T2318-erdos536-source-geometry-vanishing-depletion-student.json`
- `oracle/responses/OS-20260606T235319Z-oracle-response.md`
- `raw/oracle/RO-OS-20260606T235319Z.json`
- `raw/student/20260606T2318-erdos536-source-geometry-vanishing-depletion.md`

## Proof

Node promoted: the Erdos536 conditional lower trace poor vanishing by combined sinks.

Suppose a lower-trace-poor active branch \(\mathcal F_k\) outside negligible discarded mass decomposes as
\[
\mathcal F_k\subseteq \mathcal F_k^{\mathrm{ac}}\cup\mathcal F_k^{\mathrm{del}},
\]
where \(\mathcal F_k^{\mathrm{ac}}\) is coverable by \(M_k=o(\sqrt{V_k})\) antichains, and \(\mathcal F_k^{\mathrm{del}}\) satisfies the multiplicity-controlled deletion criterion with ratio \(M'_k/L_k\to0\). Then
\[
\nu_k(\mathcal F_k^{\mathrm{ac}})=o(1)
\]
by the bounded antichain-decomposition sink, and
\[
\nu_k(\mathcal F_k^{\mathrm{del}})=o(1)
\]
by multiplicity-controlled deletion decay. Adding back only negligible discarded mass gives
\[
\nu_k(\mathcal F_k)=o(1).
\]
All hypotheses are explicit and conditional. No source-level implication is hidden in the theorem.

Node introduced open: the Erdos536 residual union free moving base high multiplicity frontier.

The remaining obstruction is a positive-mass, high-support, non-rank-thin, lower-trace-poor admissible family that avoids the antichain-cover exit and the deletion-transport exit. It must use a residual source-specific union-free/lower-trace condition, moving bases, and high lower-trace multiplicity while also avoiding finite-core shields. Constructing or excluding this residual condition is now the sharp next frontier.

Candidate: the Erdos536 lower trace poor bounded antichain or residual union free.

A bounded antichain decomposition was not proved from source admissibility. The residual union-free moving-base high-multiplicity frontier was identified as the exact remaining condition not captured by antichain/comparable-pair exclusion.

Candidate: the Erdos536 moving base high multiplicity obstruction or exclusion.

No full moving-base obstruction construction was built, and no exclusion by rank-thinness, shielding, source admissibility, or mass decay was proved. The residual frontier records what such an obstruction must satisfy.

Candidate: the Erdos536 conditional lower trace poor vanishing combined sinks.

The combined conditional theorem was proved with explicit hypotheses: antichain cover decay for one part, multiplicity-controlled deletion decay for the other part, and only negligible discarded mass. It does not solve the terminal source or frontier nodes until the source-reduction and multiplicity-exclusion hypotheses are proved.

the Erdos536 lower trace poor source geometry three exit fork: true proof-state fork.
the Erdos536 conditional lower trace poor vanishing by combined sinks: true conditional theorem.
the Erdos536 residual union free moving base high multiplicity frontier: open obstruction.
the Erdos536 lower trace poor bounded antichain or residual union free: candidate_open with residual identified.
the Erdos536 moving base high multiplicity obstruction or exclusion: candidate_open.
the Erdos536 conditional lower trace poor vanishing combined sinks: depleted by conditional theorem.
the Erdos536 coordinate coverage lower trace forces fork: remains open.
the Erdos536 prime biased weighted union free frontier: remains open.

_Proof source: `raw/student/20260606T2318-erdos536-source-geometry-vanishing-depletion.md`._

## Tags

`combined-sinks`, `conditional-vanishing`, `erdos-536`, `lower-trace-poor`, `proved`, `student-proof`, `theorem`, `true`
