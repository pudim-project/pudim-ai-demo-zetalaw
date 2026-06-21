---
id: "T-Erdos536-rank-block-anti-concentration"
type: "theorem"
title: "Erdos 536 prime biased rank block anti concentration for o sqrt S exact ranks"
status: "proved"
tags: ["erdos-536", "prime-biased-measure", "proved", "rank-anti-concentration", "rank-thin", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["private librarian audit", "private proof note", "wiki/versions/stage_v006/wiki/nodes/mrw-54968b07a069.md"]
---

# Theorem: Erdos 536 prime biased rank block anti concentration for o sqrt S exact ranks

## Statement

For the prime-biased product law \(\nu_k(p_i\in S)=1/p_i\) on \(P_k=\{p_1,\ldots,p_k\}\), let \(S_k=\sum_{i\le k}1/p_i\). If \(R_k\subseteq\{0,1,\ldots,k\}\) has \(|R_k|=o(\sqrt{S_k})\), then \(\nu_k\{S\subseteq P_k: |S|\in R_k\}\to0\). Consequently, any family whose mass is eventually contained, up to \(o(1)\), in \(o(\sqrt{S_k})\) exact cardinality layers has vanishing \(\nu_k\)-mass.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `wiki/versions/stage_v006/wiki/nodes/mrw-54968b07a069.md`

## Proof

\emph{Setup.}
Let
\[
P_k=\{p_1,\ldots,p_k\},\qquad q_i=\frac1{p_i},\qquad
S_k=\sum_{i\le k}q_i,
\]
and let \(\nu_k\) be the product law on \(2^{P_k}\) with
\[
\nu_k(p_i\in S)=q_i.
\]
Put
\[
V_k=\sum_{i\le k}q_i(1-q_i)
=S_k-\sum_{i\le k}\frac1{p_i^2}.
\]
Since \(\sum_p1/p^2<\infty\), one has
\[
V_k=S_k-O(1)\to\infty.
\]

A lower-shadow fork in a family \(\mathcal F\subseteq2^{P_k}\) is a triple
\[
A,B,C\in\mathcal F,\qquad A\ne B,\qquad A,B\subsetneq C,\qquad A\cup B=C.
\]
By the public union-free reformulation mrw-b4075311abd3, this is exactly a
forbidden union triple.

The requested anti-concentration lemma is true.

Let \(R_k\subseteq\{0,1,\ldots,k\}\) be any set of ranks with
\[
|R_k|=o(\sqrt{S_k}).
\]
Then
\[
\nu_k\{S\subseteq P_k:\ |S|\in R_k\}\to0.
\]

Indeed, each exact cardinality layer
\[
\mathcal L_{k,r}=\{S\subseteq P_k:\ |S|=r\}
\]
is an antichain.  The public product-measure antichain estimate used in
mrw-54968b07a069 gives an absolute constant \(C\) such that
\[
\nu_k(\mathcal L_{k,r})
\le
C(1+V_k)^{-1/2}
\]
for every \(r\).  Therefore
\[
\nu_k\{|S|\in R_k\}
\le
C|R_k|(1+V_k)^{-1/2}
=o(1),
\]
because \(V_k=S_k-O(1)\).

More generally, if for every \(\varepsilon>0\) all but \(o(1)\) of
\(\nu_k(\mathcal F_k)\) lies in at most \(\varepsilon\sqrt{S_k}\) exact ranks,
then
\[
\limsup_{k\to\infty}\nu_k(\mathcal F_k)\le C\varepsilon
\]
for every \(\varepsilon>0\), and hence
\[
\nu_k(\mathcal F_k)\to0.
\]

This proves the anti-concentration half of the rank-thin route.

Candidate:
the Erdos536 positive mass fork energy theorem.

For the fork energy \(\Phi_k(\mathcal F_k)\) defined in the AP, one has
\[
\Phi_k(\mathcal F_k)>0
\quad\Longleftrightarrow\quad
\mathcal F_k\text{ contains a lower-shadow fork}.
\]
The implication from right to left holds because every individual subset of a
fixed top set \(C\) has positive \(\mu_C\)-mass.  The reverse implication is
immediate from the definition of the event integrated in \(\Phi_k\).

Thus Candidate 1 is a mass-sensitive reformulation of the Erdos weighted
union-free frontier: a positive-mass union-free family would be exactly a
positive-mass family with \(\Phi_k=0\).  The rank-block lemma does not prove
that \(\Phi_k>0\) for all positive-mass high-support families.  No local proof
or counterexample was found.

Candidate:
the Erdos536 rank thin alternative for fork free families.

The anti-concentration conclusion in this candidate is proved above:
rank-thin families have vanishing \(\nu_k\)-mass.  The hard direction remains:
\[
\Phi_k(\mathcal F_k)=0
\quad\Longrightarrow\quad
\mathcal F_k\text{ is rank-thin}.
\]
Equivalently, one must rule out a rank-diffuse positive-mass high-support
family with no lower-shadow fork.

rank layers are fork-free and can have huge combinatorial chain-cover number,
but they are rank-thin and therefore negligible under \(\nu_k\).  What remains
is a genuinely rank-diffuse fork-free obstruction, if one exists.

Candidate:
the Erdos536 endpoint tower fork energy transfer.

The rank-block lemma also clarifies this endpoint branch.  If terminal fibers
inside a triangle-free endpoint-pair shield are rank-thin, their contribution
vanishes.  But the public endpoint-pair shield node mrw-1b04240e9886 still
blocks endpoint-only triangle arguments: a complete bipartite endpoint graph
can carry positive endpoint mass while remaining triangle-free.

No local proof was found that rank-diffuse terminal fibers transfer positive
mass into \(\Phi_k\).  The missing theorem is still a tower-coherence result:
endpoint conditioning must either preserve a terminal fork in the global
family, or force terminal fibers into the rank-thin negligible case.

the Erdos536 positive mass fork energy theorem: candidate_open;
the Erdos536 rank thin alternative for fork free families: candidate_open;
the Erdos536 endpoint tower fork energy transfer: candidate_open.

New true node proposed:

the Erdos536 rank block anti concentration.

No Erdos 536 theorem was solved in this pass.  The useful progress is that the
rank-thin side of the mass-sensitive fork strategy is now rigorous: any
candidate counterexample must be both positive-mass and rank-diffuse while
having zero fork energy.

around the remaining rank-diffuse fork-free obstruction, including a local
shadow-expansion route, a random-top-set conditioning route, and an
endpoint-tower terminal-fork transfer route.

_Proof source: `private proof note`._

## Tags

`erdos-536`, `prime-biased-measure`, `proved`, `rank-anti-concentration`, `rank-thin`, `theorem`, `true`
