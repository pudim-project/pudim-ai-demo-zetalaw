---
id: "T-Erdos536-lower-trace-poor-source-geometry-three-exit-fork"
type: "theorem"
title: "Erdos536 lower trace poor source geometry three exit fork"
status: "proved"
tags: ["erdos-536", "lower-trace-poor", "proved", "source-geometry", "student-proof", "theorem", "trichotomy", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private Oracle audit", "private proof note"]
---

# Theorem: Erdos536 lower trace poor source geometry three exit fork

## Statement

Lower-trace-poor source-geometry three-exit fork: after discarding only separately proved negligible rank-thin or top-thin mass, any positive-mass high-support lower-trace-poor admissible branch must be handled by one of three explicit exits: an antichain-cover exit with \(M_k=o(\sqrt{V_k})\), a deletion-transport exit with multiplicity/deletion ratio \(M_k/L_k\to0\) or an averaged analogue, or a residual union-free moving-base high-multiplicity obstruction not captured by the first two exits.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private Oracle audit`
- `private proof note`

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

_Proof source: `private proof note`._

## Tags

`erdos-536`, `lower-trace-poor`, `proved`, `source-geometry`, `student-proof`, `theorem`, `trichotomy`, `true`
