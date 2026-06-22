---
id: "T-Erdos536-defect-disjointness-coverage-normal-form"
type: "theorem"
title: "Erdos536 defect disjointness coverage normal form"
status: "proved"
tags: ["attack-plan", "coordinate-coverage", "defect-sets", "erdos-536", "fork-energy", "open", "proved", "theorem"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["attack-plans/AP-20260606T180148-erdos536-coordinate-coverage-defect-reduction.json", "librarian/audits/LA-20260606T180148-erdos536-coordinate-coverage-defect-reduction-attack-plan.json", "librarian/audits/LA-20260606T1848-erdos536-defect-disjointness-normal-form-student.json", "raw/oracle/RO-OS-20260606T214430Z.json", "raw/student/20260531T184100-erdos536-lower-trace-visibility.md", "raw/student/20260606T1848-erdos536-defect-disjointness-normal-form.md", "theory/nodes/T-Erdos536-fork-energy-random-top-conditioning-identity.json", "theory/nodes/T-Erdos536-rank-block-anti-concentration.json"]
---

# Theorem: Erdos536 defect disjointness coverage normal form

## Statement

For every fixed \(0<\theta<1\), \(\eta>0\), and every admissible non-rank-thin positive-mass family \(\mathcal F_k\subseteq H_{k,\theta}\), the coordinate-coverage statistic below occupied tops is equivalently the two-sample disjoint-defect statistic. For \(C\in\mathcal F_k\), set \(\mathcal D_C=\{C\setminus A:A\in\mathcal L_{\mathcal F_k}(C)\}\) with the push-forward of \(\mu_C\). Then \(\Omega_k(C)=\mu_C^{\otimes2}\{(D,E)\in\mathcal D_C^2:D\cap E=\varnothing\}\), and \(\mathbf E[\Omega_k(C)\mid C\in\mathcal F_k]>0\) follows once the conditional defect law has positive disjoint-pair probability on a positive-mass set of occupied tops.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `attack-plans/AP-20260606T180148-erdos536-coordinate-coverage-defect-reduction.json`
- `librarian/audits/LA-20260606T180148-erdos536-coordinate-coverage-defect-reduction-attack-plan.json`
- `librarian/audits/LA-20260606T1848-erdos536-defect-disjointness-normal-form-student.json`
- `raw/oracle/RO-OS-20260606T214430Z.json`
- `raw/student/20260531T184100-erdos536-lower-trace-visibility.md`
- `raw/student/20260606T1848-erdos536-defect-disjointness-normal-form.md`
- `theory/nodes/T-Erdos536-fork-energy-random-top-conditioning-identity.json`
- `theory/nodes/T-Erdos536-rank-block-anti-concentration.json`

## Proof

\emph{Setup.}
The previous pass established:

the Erdos536 rank block anti concentration: \(o(\sqrt{S_k})\) exact ranks
  carry \(o(1)\) prime-biased mass.
the Erdos536 fork energy random top conditioning identity: the fork energy is
  the expectation of conditional fork probability over occupied top sets.
the Erdos536 same endpoint terminal fork lifts: a same-endpoint terminal fork
  lifts to a global fork.

Thus any remaining obstruction to the weighted union-free frontier must have
positive mass, be rank-diffuse, and have zero fork energy.  The purpose of this
AP was to test whether rank diffuseness forces lower-trace visibility below
occupied top sets.

Candidate:
the Erdos536 lower trace mass rank diffuse theorem.

No proof was found.  The main gap persists: rank diffuseness is an external
statement about which cardinality layers carry mass, while lower-trace
visibility is an internal statement about the occupied subsets lying below a
typical occupied top \(C\).

The true rank-block anti-concentration theorem rules out concentration on too
few exact ranks, but it does not imply
\[
\mu_C(\mathcal L_{\mathcal F_k}(C))>0
\]
for a positive-mass set of occupied top sets \(C\).  A family can be
rank-diffuse in the ambient product law while the conditional lower trace under
most occupied tops is invisible or concentrated in the wrong coordinates.  The
missing input is a shadow-density theorem connecting ambient rank diffusion to
inside-top lower-trace mass.

Narrowing: the next route should define an explicit lower-trace visibility
statistic, for example
\[
\Lambda_k(\mathcal F_k)
=
\mathbf E\bigl[\mu_C(\mathcal L_{\mathcal F_k}(C))\mid C\in\mathcal F_k\bigr],
\]
and prove a dichotomy: either \(\Lambda_k\) is positive on separated lower-rank
windows, or the family is structurally rank-thin after conditioning on tops.

Candidate:
the Erdos536 fiber selection coherence forces fork.

No proof was found.  Even granting positive lower-trace visibility, there is a
second coherence step:
\[
\text{many visible lower traces below }C
\quad\Longrightarrow\quad
\exists A,B\subsetneq C,\ A\cup B=C.
\]
This is not automatic.  The visible lower traces might be arranged inside a
proper coordinate core of \(C\), or two independently sampled lower traces may
miss a moving set of coordinates.  In that case lower-trace mass is present,
but the two-sample covering event still has zero probability.

The existing random-top conditioning identity shows that the desired conclusion
is exactly positivity of the conditional covering probability
\[
\psi_k(C)=
\mu_C^{\otimes2}
\{(A,B)\in\mathcal L_{\mathcal F_k}(C)^2:
A\ne B,\ A\cup B=C\}.
\]
What remains is a coverage/coherence theorem turning lower-trace mass into
\(\psi_k(C)>0\).

Narrowing: the next route should split lower-trace visibility into two
quantities: trace mass and coordinate coverage.  Trace mass alone is too weak;
the lower traces must cover almost all coordinates of \(C\) in pairs.

Candidate:
the Erdos536 diagnostic rank diffuse zero fork construction.

No positive-mass rank-diffuse zero-fork construction was found.

The standard attempts fail for known reasons:

1. Exact rank layers are fork-free but rank-thin, and vanish by
   the Erdos536 rank block anti concentration.
2. Any \(o(\sqrt{S_k})\)-rank block is still rank-thin and vanishes.
3. Chain templates are fork-free, but their prime-biased mass is killed by the
   chain-measure theorem behind
   the Erdos536 chain cover subcritical forces vanishing unless one uses many
   chains; with many chains, cross-chain unions become the unresolved source of
   forks.
4. Endpoint-pair shields can carry positive endpoint mass by mrw-1b04240e9886,
   but same-endpoint terminal forks lift globally.  To keep zero fork energy,
   terminal fibers must themselves be zero-fork or rank-thin, which pushes the
   problem back to the same rank-diffuse lower-trace obstruction.

Narrowing: the diagnostic obstruction, if it exists, is not an exact-rank,
small-rank-block, single-chain, or naive endpoint-shield object.  It must be a
many-fiber object with positive mass, rank diffusion, and a genuine coverage
avoidance mechanism inside typical top sets.

the Erdos536 lower trace mass rank diffuse theorem: candidate_open;
the Erdos536 fiber selection coherence forces fork: candidate_open;
the Erdos536 diagnostic rank diffuse zero fork construction: candidate_open.

No Erdos 536 theorem was solved and no counterexample was constructed.  The
frontier is sharper: prove lower-trace visibility plus coordinate coverage
inside typical occupied tops, or construct a positive-mass rank-diffuse
zero-fork family with a real coverage-avoidance mechanism.

around a two-statistic lower-trace framework: one for lower-trace mass, one for
coordinate coverage of lower traces inside top sets, and one diagnostic
construction route for many-fiber coverage-avoidance families.

_Proof source: `raw/student/20260531T184100-erdos536-lower-trace-visibility.md`._

## Tags

`attack-plan`, `coordinate-coverage`, `defect-sets`, `erdos-536`, `fork-energy`, `open`, `proved`, `theorem`
