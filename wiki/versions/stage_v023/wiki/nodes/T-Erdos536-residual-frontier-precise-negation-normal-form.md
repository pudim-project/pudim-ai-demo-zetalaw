---
id: "T-Erdos536-residual-frontier-precise-negation-normal-form"
type: "theorem"
title: "Erdos536 residual frontier precise negation normal form"
status: "proved"
tags: ["erdos-536", "normal-form", "proved", "residual-frontier", "source-geometry", "student-proof", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["attack-plans/AP-20260606T2331-erdos536-residual-frontier-split.json", "librarian/audits/LA-20260606T2344-erdos536-residual-frontier-split-depletion-student.json", "oracle/responses/OS-20260607T000053Z-oracle-response.md", "raw/oracle/RO-OS-20260607T000053Z.json", "raw/student/20260606T2344-erdos536-residual-frontier-split-depletion.md"]
---

# Theorem: Erdos536 residual frontier precise negation normal form

## Statement

Residual frontier precise-negation normal form: a lower-trace-poor positive-mass high-support non-rank-thin branch is residual only if, after negligible rank-thin/top-thin discards, it has no \(o(\sqrt{V_k})\)-antichain cover, no subcritical deletion-multiplicity ratio \(M_k/L_k\to0\), no fixed finite core, no endpoint/core shield, and no rank-thin mass concentration. Thus every non-residual lower-trace-poor branch supplies at least one already named sink or descent exit.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `attack-plans/AP-20260606T2331-erdos536-residual-frontier-split.json`
- `librarian/audits/LA-20260606T2344-erdos536-residual-frontier-split-depletion-student.json`
- `oracle/responses/OS-20260607T000053Z-oracle-response.md`
- `raw/oracle/RO-OS-20260607T000053Z.json`
- `raw/student/20260606T2344-erdos536-residual-frontier-split-depletion.md`

## Proof

Node promoted: the Erdos536 residual frontier precise negation normal form.

A lower-trace-poor positive-mass, high-support, non-rank-thin branch is genuinely residual only if all previously proved exits fail after negligible rank-thin/top-thin discards:

1. no cover by \(M_k=o(\sqrt{V_k})\) antichains;
2. no deletion-transport exit with subcritical multiplicity ratio \(M_k/L_k\to0\), or its averaged weighted analogue;
3. no fixed finite core, since finite-core conditional antichain sinks apply after conditioning;
4. no endpoint/core shielding exit;
5. no rank-thin mass concentration.

Consequently, every non-residual lower-trace-poor branch supplies at least one named sink or descent exit: antichain-cover decay, multiplicity-controlled deletion decay, finite-core descent, shielding, or rank-thin vanishing. This is a normal form for the current proof state, not a source-level exclusion theorem.

Node promoted: the Erdos536 global frontier split residual ltp or ltr design.

Combine the true lower-trace-poor three-exit fork with the true conditional lower-trace-poor vanishing theorem. Any positive-mass non-rank-thin admissible branch is either lower-trace-poor or lower-trace-rich. In the lower-trace-poor case, every non-residual branch is killed by one of the combined sinks or descent exits. Thus any remaining lower-trace-poor branch must lie in the residual union-free moving-base high-multiplicity frontier.

The other unresolved side is the lower-trace-rich branch, where the existing coordinate-coverage, spread-design, and lower-trace realization nodes remain open. Hence the remaining global frontier splits as:
\[
\text{residual lower-trace-poor moving-base multiplicity}
\quad\text{or}\quad
\text{lower-trace-rich coordinate/design frontier}.
\]
This split is structural and conditional; it does not solve either side.

Candidate: the Erdos536 residual moving base high multiplicity construction or exclusion.

No admissible positive-mass residual moving-base high-multiplicity family was constructed. No exclusion theorem was proved. The missing source axiom records exactly what an exclusion must supply.

Candidate: the Erdos536 global ltp versus ltr design split.

The remaining frontier is now organized as residual lower-trace-poor moving-base multiplicity versus lower-trace-rich coordinate/design obstruction. No terminal source or frontier node is promoted.

the Erdos536 residual frontier precise negation normal form: true proof-state normal form.
the Erdos536 global frontier split residual ltp or ltr design: true structural split.
the Erdos536 missing source axiom for residual multiplicity exclusion: open obstruction.
the Erdos536 residual moving base high multiplicity construction or exclusion: candidate_open.
the Erdos536 source admissibility controls outside residual frontier: depleted by normal form, residual still open.
the Erdos536 global ltp versus ltr design split: depleted by structural split.
the Erdos536 coordinate coverage lower trace forces fork: remains open.
the Erdos536 prime biased weighted union free frontier: remains open.

_Proof source: `raw/student/20260606T2344-erdos536-residual-frontier-split-depletion.md`._

## Tags

`erdos-536`, `normal-form`, `proved`, `residual-frontier`, `source-geometry`, `student-proof`, `theorem`, `true`
