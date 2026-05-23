---
id: mrw-1f7c23e5a9d4
type: note
title: Finite-junta deletion traces obstruct trace-local rooted estimates
aliases: ["mrw-1f7c23e5a9d4", "Finite-junta deletion traces obstruct trace-local rooted estimates"]
status: proved
tags: [note, proved, erdos-536, union-free, deletion-trace, intersecting-family, finite-junta, rooted-junta, obstruction, support-tail]
parents: [mrw-6a9d1e4f2c8b, mrw-cc4f876149b7, mrw-55a8d9eddd2e, mrw-d0402aea6f58, mrw-b4075311abd3, mrw-3c39ca3d1973]
refs: ["references/sources/20260519T145428Z-rooted-junta-context.md"]
  - raw/20260519T145428Z-erdos536-root-consistency.md
  - references/requests/20260519T145428Z-rooted-junta-erudition-gate.md
  - references/sources/20260519T145428Z-rooted-junta-context.md
  - oracle/requests/20260519T145428Z-erdos536-root-consistency-oracle-request.md
  - oracle/responses/20260519T145428Z-erdos536-root-consistency-oracle-response.md
---

# Note: Finite-junta deletion traces obstruct trace-local rooted estimates

## Statement

Let \(J\) be a fixed finite set and let
\(\mathcal I\subseteq2^J\) be pairwise intersecting with
\[
\varnothing\notin\mathcal I.
\]
For every finite set \(C\supseteq J\), define the finite-junta deletion trace
\[
\mathcal T_{\mathcal I,J}(C)
=
\{D\subseteq C:\ D\cap J\in\mathcal I\}.
\]
Then \(\mathcal T_{\mathcal I,J}(C)\) is pairwise intersecting.

Moreover, let \(\pi_{C,\lambda}\) be the product law on \(2^C\) under which
each element lies in the deletion set independently with probability
\(0<\lambda<1\).  Then
\[
\pi_{C,\lambda}\bigl(\mathcal T_{\mathcal I,J}(C)\bigr)
=
\pi_{J,\lambda}(\mathcal I).
\]
If \(C_n\supseteq J\), \(|C_n|=n\), and \(L_n\) satisfies
\[
\limsup_{n\to\infty}\frac{L_n}{n}<\lambda,
\]
then
\[
\pi_{C_n,\lambda}
\bigl(\{D\in\mathcal T_{\mathcal I,J}(C_n): |D|\ge L_n\}\bigr)
\longrightarrow
\pi_{J,\lambda}(\mathcal I).
\]

Consequently, a trace-local theorem saying that deletion traces are controlled
by fixed finite intersecting juntas cannot by itself prove vanishing
large-deletion trace mass below the ambient deletion mean \(\lambda |C|\).
The prime-biased weighted union-free theorem [[mrw-55a8d9eddd2e]] still needs a
global root-consistency theorem, a rooted-container theorem preserving the
top/head relation, the full union hypergraph, or the full pair-link hypergraph.

This note is not a counterexample to [[mrw-55a8d9eddd2e]] and not a coherent
realization theorem for deletion traces of a single positive-mass family.

## Proof

If \(D,E\in\mathcal T_{\mathcal I,J}(C)\), then
\[
D\cap J,\ E\cap J\in\mathcal I.
\]
Since \(\mathcal I\) is pairwise intersecting, there is an element in
\[
(D\cap J)\cap(E\cap J).
\]
Thus \(D\cap E\ne\varnothing\), so
\(\mathcal T_{\mathcal I,J}(C)\) is pairwise intersecting.

For the mass identity, observe that under \(\pi_{C,\lambda}\), the random set
\(D\cap J\) has law \(\pi_{J,\lambda}\) and is independent of all coordinates
in \(C\setminus J\).  Membership in \(\mathcal T_{\mathcal I,J}(C)\) depends
only on \(D\cap J\).  Therefore
\[
\pi_{C,\lambda}\bigl(\mathcal T_{\mathcal I,J}(C)\bigr)
=
\pi_{J,\lambda}(\mathcal I).
\]

Now let \(C_n\supseteq J\), \(|C_n|=n\), and
\(\limsup L_n/n<\lambda\).  For each fixed \(I\in\mathcal I\), conditioned on
\[
D\cap J=I,
\]
the deletion size has the distribution
\[
|D|=|I|+\operatorname{Bin}(n-|J|,\lambda).
\]
Since \(J\) and \(I\) are fixed,
\[
\frac{|I|+\operatorname{Bin}(n-|J|,\lambda)}{n}\to\lambda
\]
in probability.  Hence
\[
\Pr_{\pi_{C_n,\lambda}}\bigl(|D|\ge L_n\mid D\cap J=I\bigr)\to1
\]
for every \(I\in\mathcal I\).  Summing over the finite set
\(\mathcal I\) gives
\[
\pi_{C_n,\lambda}
\bigl(\{D\in\mathcal T_{\mathcal I,J}(C_n): |D|\ge L_n\}\bigr)
=
\sum_{I\in\mathcal I}
\pi_{J,\lambda}(I)\,
\Pr\bigl(|D|\ge L_n\mid D\cap J=I\bigr)
\to
\pi_{J,\lambda}(\mathcal I).
\]
This proves the claim.

## Depends on

- [[mrw-6a9d1e4f2c8b]] Star deletion traces obstruct trace-local
  growing-deletion estimates
- [[mrw-cc4f876149b7]] Intersecting deletion-trace obstruction for
  lower-shadow union covers
- [[mrw-55a8d9eddd2e]] Prime-biased weighted union-free theorem
- [[mrw-d0402aea6f58]] Biased lower-shadow union-cover problem for Erdos 536
- [[mrw-b4075311abd3]] Union-free reformulation of the biased lower-shadow
  route
- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree
  residuals

## Used by

- Next route: prove that positive-mass high-support union-free families cannot
  realize positive-mass finite-junta deletion traces coherently across many
  top sets, or construct such a coherent family explicitly and test it against
  the full pair-link shadow.

## Notes

The star obstruction [[mrw-6a9d1e4f2c8b]] is the special case
\[
J=\{x\},\qquad \mathcal I=\{\{x\}\}.
\]
This note records that the same obstruction survives for every fixed finite
intersecting junta with positive \(\pi_{J,\lambda}\)-mass.

The threshold is measured relative to \(|C_n|\).  No claim is made at the
critical scale \(L_n/n\to\lambda\), above the deletion mean, or for thresholds
measured relative to \(S_k=\sum_{i\le k}1/p_i\) without an additional
comparison between \(|C|\) and \(S_k\).

The Oracle browser attachment run for this cycle failed with
`Attachments never reached a clickable send button before timeout`, and the
inline retry returned `You've hit your limit. Please try again later.`  Thus
the Oracle response is retained only as a blocker record; the proof above is
the local audit used for promotion.
