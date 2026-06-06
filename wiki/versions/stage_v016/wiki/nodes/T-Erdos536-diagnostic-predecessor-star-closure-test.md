---
id: "T-Erdos536-diagnostic-predecessor-star-closure-test"
type: "theorem"
title: "Erdos 536 diagnostic predecessor star closure test for linear window obstruction"
status: "proved"
tags: ["closure-test", "diagnostic", "erdos-536", "predecessor-star", "proved", "theorem", "true"]
parents: ["T-Finite-combinatorial-packing-shadow-principle", "T-Erdos536-full-predecessor-window-closure-has-forks"]
refs: ["attack-plans/AP-20260531T203012-erdos536-predecessor-obstruction.json", "librarian/audits/LA-20260531T203012-erdos536-predecessor-obstruction-attack-plan.json", "librarian/audits/LA-20260531T203844-erdos536-predecessor-obstruction-student.json", "raw/student/20260531T202634-erdos536-locally-unique-centers.md", "raw/student/20260531T203844-erdos536-predecessor-obstruction.md", "theory/nodes/T-Erdos536-diagnostic-locally-unique-positive-mass-code-obstruction.json", "theory/nodes/T-Erdos536-full-predecessor-window-closure-has-forks.json", "theory/nodes/T-Erdos536-linear-window-predecessor-star-code-avoids-pushforward.json"]
---

# Theorem: Erdos 536 diagnostic predecessor star closure test for linear window obstruction

## Statement

Diagnostic predecessor-star closure test: start from the true linear-window predecessor-star top code `T-Erdos536-linear-window-predecessor-star-code-avoids-pushforward`, then impose the actual moving-star family closure expected in the Erdos 536 frontier: occupied tops, their singleton predecessor traces, any required lower traces of those predecessors, and nearby central top windows. Determine whether this closure remains positive-mass and fork-free with locally unique centers, or whether it necessarily creates a fork, becomes rank-thin, loses positive \(\nu_k\)-mass, or produces nondegenerate lower-rank mass. This route is diagnostic only and should record the precise failure mode.

## Dependencies

- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]
- [[wiki/nodes/T-Erdos536-full-predecessor-window-closure-has-forks|Erdos 536 full predecessor rank window closure contains union forks]]

## Proof and provenance references

- `attack-plans/AP-20260531T203012-erdos536-predecessor-obstruction.json`
- `librarian/audits/LA-20260531T203012-erdos536-predecessor-obstruction-attack-plan.json`
- `librarian/audits/LA-20260531T203844-erdos536-predecessor-obstruction-student.json`
- `raw/student/20260531T202634-erdos536-locally-unique-centers.md`
- `raw/student/20260531T203844-erdos536-predecessor-obstruction.md`
- `theory/nodes/T-Erdos536-diagnostic-locally-unique-positive-mass-code-obstruction.json`
- `theory/nodes/T-Erdos536-full-predecessor-window-closure-has-forks.json`
- `theory/nodes/T-Erdos536-linear-window-predecessor-star-code-avoids-pushforward.json`

## Proof

\emph{Setup.}
Use the prime-biased product law
\[
\nu_k(p_i\in S)=\frac1{p_i},\qquad
S_k=\sum_{i\le k}\frac1{p_i},\qquad
H_{k,\theta}=\{S\subseteq P_k: |S|>\theta S_k\}.
\]
The input from the previous pass is the local uniqueness lemma
the Erdos536 same top two star centers force fork: a fork-free occupied top
cannot carry two different full threshold-sharp EKR star centers at the same
lower rank. Thus the remaining obstruction is cross-top, not same-top.

Candidate:
the Erdos536 locally unique star union pushforward hitting.

The full hitting lemma remains open. I could not prove that local uniqueness,
nonsparse close central ranks, and positive top-code mass force the union
push-forward to hit the occupied top code.

There is a diagnostic reason this route is hard. Local uniqueness and positive
rank mass alone do not force hitting. Fix constants
\[
\theta<a<1<b<2a,
\]
and put
\[
\mathcal T_k=\{C\subseteq P_k: aS_k\le |C|\le bS_k\}.
\]
For every fixed \(\theta<1\), such constants can be chosen. By Chebyshev's
inequality, \(\nu_k(\mathcal T_k)\to1\), because \(\mathbb E|S|=S_k\) and
\(\operatorname{Var}(|S|)\le S_k\). Each \(C\in\mathcal T_k\) is in
\(H_{k,\theta}\) for large \(k\).

Give each \(C\in\mathcal T_k\) one locally unique center \(q(C)\in C\), for
example the least element of \(C\), and take the threshold-sharp predecessor
star at rank \(r=|C|-1\):
\[
\mathcal A_{|C|-1,q(C)}(C)=\{C\setminus\{q(C)\}\}.
\]
This is a full EKR star of size \(\binom{|C|-1}{|C|-1}=1\), so it is
threshold-sharp and locally unique.

Now draw two independent tops \(C_1,C_2\) from \(\nu_k\) conditioned on
\(\mathcal T_k\), and set \(D_i=C_i\setminus\{q(C_i)\}\). If
\(D_1\cup D_2\in\mathcal T_k\), then
\[
|D_1\cap D_2|
\ge |D_1|+|D_2|-bS_k
\ge (2a-b)S_k-2.
\]
But for two independent unconditioned prime-biased sets,
\[
\mathbb E|C_1\cap C_2|=\sum_{i\le k}\frac1{p_i^2}\le M<\infty.
\]
Since \(\nu_k(\mathcal T_k)\to1\), the same expectation under conditioning on
\(\mathcal T_k\times\mathcal T_k\) remains \(O(1)\). Markov's inequality then
gives
\[
\mathbb P(D_1\cup D_2\in\mathcal T_k\mid C_1,C_2\in\mathcal T_k)
\le
\frac{O(1)}{(2a-b)S_k-2}\to0.
\]
Thus the union push-forward of these locally unique predecessor stars has
negligible intersection with the positive-mass top code.

This does not refute the full hitting lemma as a theorem about genuine
fork-free coherent moving-star obstructions, because the construction above is
a top-code model and does not prove that the entire induced family is
fork-free. It does show that the hitting lemma cannot be proved from local
uniqueness, nonsparse central ranks, and positive top-code mass alone.

Candidate:
the Erdos536 weighted center map regularity locally unique stars.

The theorem remains open. The linear-window predecessor-star construction also
shows why a center-map regularity statement must include a genuine occupancy
or fork-free coherence condition. The center map \(C\mapsto q(C)\) can be
perfectly regular and locally unique, while the union push-forward avoids the
central top window simply because two independent predecessor stars have
nearly doubled rank.

The regularity route still looks plausible if it can prove more than
regularity of the center map: it must either force lower ranks away from the
degenerate predecessor regime \(r=|C|-1\), or use fork-free coherence to show
that the positive-mass top code cannot be isolated in a narrow linear window
while carrying only predecessor stars. I did not prove such a theorem.

Candidate:
the Erdos536 diagnostic locally unique positive mass code obstruction.

This diagnostic route succeeded at the top-code level. The construction above
is a positive-mass occupied top code with nonsparse close ranks, locally unique
threshold-sharp predecessor stars, and negligible occupied hits under the
lower-star union push-forward.

Admitted true construction node:
\[
the Erdos536 linear window predecessor star code avoids pushforward.
\]
This node should be read as a diagnostic counterpressure, not as a source
counterexample to Erdos 536: it does not establish that the full set family is
coherence condition explicitly.

the Erdos536 locally unique star union pushforward hitting: candidate_open;
the Erdos536 weighted center map regularity locally unique stars: candidate_open;
the Erdos536 diagnostic locally unique positive mass code obstruction: candidate_true.

Admitted true node:
\[
the Erdos536 linear window predecessor star code avoids pushforward.
\]

Promoted diagnostic node:
\[
the Erdos536 diagnostic locally unique positive mass code obstruction.
\]

No Erdos 536 theorem was solved and no source counterexample was constructed.
The terminal Erdos 536 frontier remains open.

around excluding the linear-window predecessor-star obstruction: one
nondegenerate-lower-rank theorem, one fork-free coherence theorem linking top
windows to lower-star ranks, and one diagnostic predecessor-star closure test.

_Proof source: `raw/student/20260531T202634-erdos536-locally-unique-centers.md`._

## Tags

`closure-test`, `diagnostic`, `erdos-536`, `predecessor-star`, `proved`, `theorem`, `true`
