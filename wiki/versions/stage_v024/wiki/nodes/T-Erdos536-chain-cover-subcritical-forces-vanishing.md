---
id: "T-Erdos536-chain-cover-subcritical-forces-vanishing"
type: "theorem"
title: "Erdos 536 subcritical weighted maximum fiber chain cover number forces vanishing high support mass"
status: "proved"
tags: ["chain-cover", "erdos-536", "max-fiber", "product-measure", "proved", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T181100-erdos536-fork-width-frontier-student.json", "raw/student/20260531T181100-erdos536-fork-width-frontier.md", "wiki/versions/stage_v006/wiki/nodes/mrw-265ec9f57561.md"]
---

# Theorem: Erdos 536 subcritical weighted maximum fiber chain cover number forces vanishing high support mass

## Statement

For the prime-biased product law \(\nu_k(p_i\in S)=1/p_i\), let \(c_{m,k}\) be the least number of chains covering the maximum fiber \(\mathcal F_{k,m}\), and put \(C_k(\theta)=\sum_{T_m>\theta S_k/2}w_{m,k}c_{m,k}\). For every fixed \(0<\theta<1\), if \(C_k(\theta)=o(\sqrt{S_k})\), then \(\nu_k(\mathcal F_k\cap H_{k,	heta})\to0\).

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T181100-erdos536-fork-width-frontier-student.json`
- `raw/student/20260531T181100-erdos536-fork-width-frontier.md`
- `wiki/versions/stage_v006/wiki/nodes/mrw-265ec9f57561.md`

## Proof

Extend \(\mathcal C\) to a maximal chain determined by an ordering
\(\pi\) of the coordinates.  Its measure is
\[
\prod_{i\le m}(1-q_i)
\sum_{r=0}^{m}\prod_{j\le r}\frac{q_{\pi(j)}}{1-q_{\pi(j)}}.
\]
The prefix-product sum is maximized by ordering the ratios
\[
\frac{q_i}{1-q_i}=\frac1{p_i-1}
\]
in decreasing order; an adjacent swap changes the local contribution by the
sign of the difference between the two ratios.  Thus the maximum is bounded by
\[
\sum_{r=0}^{m}\prod_{i=1}^{r}\frac1{p_i-1}
\le K.
\]
The series defining \(K\) converges, for example because \(p_i-1\ge i\) for
large \(i\), so the products are eventually bounded by \(1/r!\).  Finally,
\[
\prod_{i\le m}(1-q_i)\le e^{-S_m}.
\]

Consequently, if \(c_{m,k}\) is the least number of chains covering the maximum
fiber \(\mathcal F_{k,m}\), then the high-maximum contribution satisfies
\[
\sum_{T_m>\theta S_k/2}w_{m,k}\,
\mu_{m-1}(\mathcal F_{k,m}\cap\{|X|+1>\theta S_k\})
\le
K e^{-\theta S_k/2}
\sum_{T_m>\theta S_k/2}w_{m,k}c_{m,k}.
\]
The low-maximum contribution is still exponentially small by the same Chernoff
argument used in the public max-fiber theorem.  Hence
\[
C_k(\theta):=\sum_{T_m>\theta S_k/2}w_{m,k}c_{m,k}=o(\sqrt{S_k})
\quad\Longrightarrow\quad
\nu_k(\mathcal F_k\cap H_{k,\theta})\to0.
\]

This proves a true chain-cover sufficiency lemma.  It does not prove that
union-free families have subcritical \(C_k(\theta)\).

Candidate:
the Erdos536 union free chain cover subcritical.

This candidate is false as stated.  Fix \(0<\theta<1\), and set
\[
r_k=\lfloor \theta S_k\rfloor+1.
\]
Let
\[
\mathcal R_k=\{S\subseteq P_k:\ |S|=r_k\}.
\]
Then \(\mathcal R_k\subseteq H_{k,\theta}\), and \(\mathcal R_k\) is
union-free: all members have the same cardinality, so no three distinct members
can satisfy \(A\cup B=C\).

However the maximum fiber at \(m=k\) contains every \((r_k-1)\)-subset of
\(\{p_1,\ldots,p_{k-1}\}\).  This fiber is an antichain of size
\[
\binom{k-1}{r_k-1},
\]
so its chain-cover number is exactly this binomial coefficient.  Therefore
\[
C_k(\theta)\ge
w_{k,k}\binom{k-1}{r_k-1}
=
\frac1{p_k}\binom{k-1}{r_k-1}.
\]
Using \(p_k\sim k\log k\) and \(r_k\asymp \log\log k\), this lower bound tends
to infinity, in particular it is not \(o(\sqrt{S_k})\).  Thus a high-support
union-free family can have supercritical chain-cover number while having only
negligible rank-layer mass.

The refutation is not an Erdos counterexample, because
\(\nu_k(\mathcal R_k)\to0\).  It shows that the chain-cover invariant must be
mass-sensitive, not purely combinatorial.

Candidate:
the Erdos536 supercritical chain cover forces fork.

The exact-rank family above would refute this candidate if the positive-mass
subsequence hypothesis were removed: it has supercritical chain-cover number
and no fork.  Because its measure tends to zero, it does not refute the stated
candidate.

The proof remains open.  A valid theorem must use positive mass to rule out the
rank-layer obstruction and then force a lower-shadow fork from many occupied
chain components.

Candidate:
the Erdos536 endpoint tower chain cover coherence.

No proof was found.  The chain-measure lemma helps only after the endpoint
tower is reduced to subcritical chain-cover mass.  The public triangle-free
endpoint-pair shield still blocks endpoint-only triangle arguments, so the
missing theorem remains cross-level coherence: either the terminal fibers are
chain-cover negligible, or a fork is forced across tower levels.

the Erdos536 union free chain cover subcritical: candidate_refuted;
the Erdos536 supercritical chain cover forces fork: candidate_open;
the Erdos536 endpoint tower chain cover coherence: candidate_open.

New true nodes proposed:

the Erdos536 chain cover subcritical forces vanishing;
the corresponding result.

number \(C_k(\theta)\) by a mass-sensitive fork statistic that ignores exact
rank layers but still detects positive-mass branching.

_Proof source: `raw/student/20260531T181100-erdos536-fork-width-frontier.md`._

## Tags

`chain-cover`, `erdos-536`, `max-fiber`, `product-measure`, `proved`, `theorem`, `true`
