---
id: "T-Erdos536-fork-energy-random-top-conditioning-identity"
type: "theorem"
title: "Erdos 536 fork energy equals random occupied top set conditional fork probability expectation"
status: "proved"
tags: ["conditioning", "erdos-536", "fork-energy", "proved", "random-top-set", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T183100-erdos536-rank-diffuse-fork-free-student.json", "raw/student/20260531T183100-erdos536-rank-diffuse-fork-free.md"]
---

# Theorem: Erdos 536 fork energy equals random occupied top set conditional fork probability expectation

## Statement

Let \(\mathcal F_k\subseteq H_{k,\theta}\). For \(C\in\mathcal F_k\), put \(\mathcal L_{\mathcal F_k}(C)=\{A\in\mathcal F_k:A\subsetneq C\}\), let \(\mu_C\) be the prime-biased product law on subsets of \(C\), and set \(\psi_k(C)=\mu_C^{\otimes2}\{(A,B)\in\mathcal L_{\mathcal F_k}(C)^2:A\ne B,\ A\cup B=C\}\). Then \(\Phi_k(\mathcal F_k)=\sum_{C\in\mathcal F_k}\nu_k(\{C\})\psi_k(C)\), and \(\mathbf E[\psi_k(C)\mid C\in\mathcal F_k]=\Phi_k(\mathcal F_k)/\nu_k(\mathcal F_k)\) whenever \(\nu_k(\mathcal F_k)>0\).

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T183100-erdos536-rank-diffuse-fork-free-student.json`
- `raw/student/20260531T183100-erdos536-rank-diffuse-fork-free.md`

## Proof

\emph{Setup.}
Use the notation from the previous pass:
\[
P_k=\{p_1,\ldots,p_k\},\qquad q_i=\frac1{p_i},\qquad
S_k=\sum_{i\le k}q_i,
\]
and let \(\nu_k\) be the product law with \(\nu_k(p_i\in S)=q_i\).  A
lower-shadow fork in \(\mathcal F_k\) is a triple
\[
A,B,C\in\mathcal F_k,\qquad A\ne B,\qquad A,B\subsetneq C,\qquad A\cup B=C.
\]
The true rank-block anti-concentration theorem
the Erdos536 rank block anti concentration says that \(o(\sqrt{S_k})\) exact
rank layers carry \(o(1)\) prime-biased mass.  Therefore any remaining
positive-mass fork-free obstruction must be rank-diffuse.

Candidate:
the Erdos536 local shadow expansion rank diffuse fork.

The local shadow-expansion proof was not found.  The main gap is conceptual:
rank diffuseness is a statement about the external distribution of occupied
cardinalities, but a lower-shadow fork requires internal lower-trace visibility
below an occupied top set.  Without an additional visibility theorem, a family
can be spread across many ranks while the lower shadow below a typical occupied
top misses the family.

Equivalently, the desired implication still needs a bridge of the form
\[
\text{rank-diffuse positive mass}
\quad\Longrightarrow\quad
\text{many occupied lower traces below occupied tops}.
\]
The public antichain estimate and the rank-block lemma do not provide this
bridge by themselves.

Narrowing: the next local-shadow route should add a lower-trace visibility or
shadow-density statistic, not merely rank diffuseness.

Candidate:
the Erdos536 random top set conditioning fork.

The conditioning identity behind the route is true.  For \(C\in\mathcal F_k\),
put
\[
\mathcal L_{\mathcal F_k}(C)
=\{A\in\mathcal F_k:A\subsetneq C\},
\]
let \(\mu_C\) be the prime-biased product law on subsets of \(C\), and define
\[
\psi_k(C)
=
\mu_C^{\otimes2}
\{(A,B)\in\mathcal L_{\mathcal F_k}(C)^2:
A\ne B,\ A\cup B=C\}.
\]
Then the fork energy from the previous AP is exactly
\[
\Phi_k(\mathcal F_k)
=
\sum_{C\in\mathcal F_k}\nu_k(\{C\})\psi_k(C).
\]
Since \(\mathcal F_k\subseteq H_{k,\theta}\), if \(C\) is sampled from
\(\nu_k\) conditioned on \(\mathcal F_k\), then
\[
\mathbf E[\psi_k(C)\mid C\in\mathcal F_k]
=
\frac{\Phi_k(\mathcal F_k)}{\nu_k(\mathcal F_k)}.
\]
Thus \(\Phi_k(\mathcal F_k)>0\) if and only if a positive \(\nu_k\)-mass set of
tops \(C\) has \(\psi_k(C)>0\).

This proves the random-top-set conditioning identity.  It does not prove the
candidate theorem, because the hard step remains:
\[
\nu_k(\mathcal F_k)\ge\eta,\quad \mathcal F_k\text{ rank-diffuse}
\quad\Longrightarrow\quad
\mathbf E[\psi_k(C)\mid C\in\mathcal F_k]>0.
\]
That implication still requires a lower-trace visibility theorem.

New true node proposed:
the Erdos536 fork energy random top conditioning identity.

Candidate:
the Erdos536 endpoint tower terminal fork transfer full.

One local transfer lemma is true.  Suppose an endpoint branch has a fixed
endpoint pattern \(e\) and terminal sets \(R_1,R_2,R_3\) with
\[
R_1\ne R_2,\qquad R_1,R_2\subsetneq R_3,\qquad R_1\cup R_2=R_3.
\]
Then the global sets
\[
e\cup R_1,\qquad e\cup R_2,\qquad e\cup R_3
\]
form a lower-shadow fork, because
\[
(e\cup R_1)\cup(e\cup R_2)=e\cup R_3.
\]
Thus same-endpoint terminal forks lift to global forks.

The full endpoint-tower candidate remains open.  The public endpoint-pair
shield mrw-1b04240e9886 shows that triangle-free endpoint patterns can carry
positive endpoint mass.  A terminal fork that occurs inside one fixed endpoint
fiber lifts, but the unresolved endpoint-tower obstruction may distribute mass
over many endpoint pairs with rank-thin terminal fibers, or may have terminal
rank-diffuse fibers whose forks are not coherent across the selected endpoint
patterns.  The missing theorem is a positive-mass fiber selection/coherence
principle.

New true node proposed:
the Erdos536 same endpoint terminal fork lifts.

the Erdos536 local shadow expansion rank diffuse fork: candidate_open;
the Erdos536 random top set conditioning fork: candidate_open;
the Erdos536 endpoint tower terminal fork transfer full: candidate_open.

No Erdos 536 theorem was solved.  The useful local progress is:

fork energy is exactly the expectation of conditional fork probability over
  random occupied top sets;
same-endpoint terminal forks lift to global forks;
the remaining obstruction must be rank-diffuse, zero fork energy, and lack a
  lower-trace visibility/coherence principle.

for lower-trace visibility in rank-diffuse fork-free families: a lower-trace
mass theorem, a fiber-selection/coherence theorem, and a diagnostic construction
attempt for a rank-diffuse zero-fork family.

_Proof source: `raw/student/20260531T183100-erdos536-rank-diffuse-fork-free.md`._

## Tags

`conditioning`, `erdos-536`, `fork-energy`, `proved`, `random-top-set`, `theorem`, `true`
