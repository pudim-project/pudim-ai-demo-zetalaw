---
id: mrw-4b9f5c2e6a1d
type: proposition
title: Near-total-root visibility is terminal-equivalent to the weighted union-free problem
aliases: ["mrw-4b9f5c2e6a1d", "Near-total-root visibility is terminal-equivalent to weighted union-free"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, union-free, near-total-root, root-consistency, outside-variance, terminal-equivalence, padding, support-tail]
parents: [mrw-a92d7b6e4031, mrw-9e0b4f1a5c33, mrw-55a8d9eddd2e, mrw-d0402aea6f58, mrw-b4075311abd3, mrw-cc4f876149b7, mrw-3c39ca3d1973]
refs: ["references/sources/20260519T165434Z-near-total-root-context.md"]
  - raw/20260519T165434Z-erdos536-near-total-root-equivalence.md
  - references/requests/20260519T165434Z-near-total-root-erudition-gate.md
  - references/sources/20260519T165434Z-near-total-root-context.md
  - theory/forage/requests/20260519T165434Z-erdos536-near-total-root-equivalence-request.md
  - theory/forage/responses/20260519T165434Z-erdos536-near-total-root-equivalence-response.md
  - raw/20260519T170907Z-scout-forage-ingest.md
  - oracle/requests/20260519T165434Z-erdos536-near-total-root-equivalence-oracle-request.md
  - oracle/responses/20260519T165434Z-erdos536-near-total-root-equivalence-oracle-response.md
---

# Proposition: Near-total-root visibility is terminal-equivalent to the weighted union-free problem

## Statement

Let
\[
P_k=\{p_1,\ldots,p_k\},\qquad q_i=\frac1{p_i},
\]
and let \(\nu_k\) be the product law on \(2^{P_k}\) with
\[
\nu_k(p_i\in S)=q_i.
\]
Put
\[
S_k=\sum_{i\le k}q_i,\qquad
H_{k,\theta}=\{S\subseteq P_k: |S|>\theta S_k\}.
\]
Let \(U_k(\theta)\) be the supremum of \(\nu_k(\mathcal F)\) over all
union-free families \(\mathcal F\subseteq H_{k,\theta}\).

For \(B\ge0\), let \(U_k^{\mathrm{vis},B}(\theta)\) be the same supremum with
the extra requirement that there is a root set \(J\subseteq P_k\) such that
\[
W_k(J)=\sum_{p_i\notin J}q_i(1-q_i)\le B
\]
and
\[
A,C\in\mathcal F,\qquad A\subsetneq C
\quad\Longrightarrow\quad
(C\setminus A)\cap J\ne\varnothing.
\]
Then
\[
U_k^{\mathrm{vis},B}(\theta)=U_k(\theta)
\tag{1}
\]
for every \(k\), every \(0\le\theta<1\), and every \(B\ge0\).

Moreover, even if one forces a proper outside coordinate, any positive-mass
counterexample to \(U_k(\theta)\to0\) pads to a near-total-root visibility
counterexample with outside variance tending to zero.  More precisely, suppose
\(0<\theta<1\), \(0\le\theta'<\theta\), and
\(\mathcal F_k\subseteq H_{k,\theta}\) are union-free with
\[
\limsup_{k\to\infty}\nu_k(\mathcal F_k)>0.
\]
Define
\[
\mathcal G_k=
\{S\subseteq P_{k+1}: p_{k+1}\notin S,\ S\cap P_k\in\mathcal F_k\}.
\]
Then \(\mathcal G_k\subseteq H_{k+1,\theta'}\) for all sufficiently large
\(k\), the families \(\mathcal G_k\) are union-free, and
\[
\nu_{k+1}(\mathcal G_k)
=
\left(1-\frac1{p_{k+1}}\right)\nu_k(\mathcal F_k).
\tag{2}
\]
With root set \(J_k=P_k\subsetneq P_{k+1}\), every proper comparable pair in
\(\mathcal G_k\) is visible through \(J_k\), and
\[
W_{k+1}(J_k)
=
\frac1{p_{k+1}}\left(1-\frac1{p_{k+1}}\right)
\to0.
\tag{3}
\]
For the endpoint \(\theta=0\), the same padding preserves the event
\(H_{k,0}=\{S:|S|>0\}\) with \(\theta'=0\).

## Proof

First prove (1).  The inequality
\[
U_k^{\mathrm{vis},B}(\theta)\le U_k(\theta)
\]
is immediate because \(U_k^{\mathrm{vis},B}\) imposes extra conditions.
Conversely, let \(\mathcal F\subseteq H_{k,\theta}\) be any union-free family.
Choose \(J=P_k\).  Then \(W_k(J)=0\le B\).  If \(A\subsetneq C\), then
\[
(C\setminus A)\cap J=C\setminus A\ne\varnothing,
\]
so the visibility condition is automatic.  Thus every family counted by
\(U_k(\theta)\) is counted by \(U_k^{\mathrm{vis},B}(\theta)\), giving the
reverse inequality and hence (1).

Now prove the padding statement.  The projection map
\[
S\mapsto S\cap P_k
\]
is a bijection from \(\mathcal G_k\) to \(\mathcal F_k\).  If
\(A',B',C'\in\mathcal G_k\) and \(A'\cup B'=C'\), then projecting to \(P_k\)
gives a union triple in \(\mathcal F_k\).  Conversely, every union triple in
\(\mathcal F_k\) embeds into \(\mathcal G_k\) by omitting \(p_{k+1}\).  Hence
\(\mathcal G_k\) is union-free exactly when \(\mathcal F_k\) is union-free.

Independence of the new coordinate gives (2).  Since \(p_{k+1}\to\infty\),
positive limsup mass is preserved.

For the high-support condition, note that \(S_k\to\infty\).  If
\(0\le\theta'<\theta<1\), then for all sufficiently large \(k\),
\[
(\theta-\theta')S_k>\frac{\theta'}{p_{k+1}}.
\]
Therefore
\[
\theta S_k
>
\theta'\left(S_k+\frac1{p_{k+1}}\right)
=
\theta' S_{k+1}.
\]
Thus any \(S\in\mathcal F_k\subseteq H_{k,\theta}\) maps to a set in
\(H_{k+1,\theta'}\).  When \(\theta=0\), nonemptiness is preserved exactly
because the set of old coordinates is unchanged and \(p_{k+1}\) is simply
absent.

Finally choose \(J_k=P_k\) inside \(P_{k+1}\).  If
\(A',C'\in\mathcal G_k\) and \(A'\subsetneq C'\), then both sets omit
\(p_{k+1}\), so
\[
C'\setminus A'\subseteq P_k=J_k
\]
and the difference is nonempty.  Thus visibility holds.  The outside set is
\(\{p_{k+1}\}\), giving (3).

## Depends on

- [[mrw-a92d7b6e4031]] Outside variance controls moving-junta comparable-pair
  visibility
- [[mrw-9e0b4f1a5c33]] Fixed-junta comparable-pair visibility forces vanishing
  mass
- [[mrw-55a8d9eddd2e]] Prime-biased weighted union-free theorem
- [[mrw-d0402aea6f58]] Biased lower-shadow union-cover problem for Erdos 536
- [[mrw-b4075311abd3]] Union-free reformulation of the biased lower-shadow
  route
- [[mrw-cc4f876149b7]] Intersecting deletion-trace obstruction for
  lower-shadow union covers
- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for squarefree cosunflowers

## Used by

- Next #536 route selection: after [[mrw-a92d7b6e4031]], the bounded or
  near-zero outside-variance regime cannot be treated as a smaller structural
  case.  It is equivalent to the original weighted union-free problem unless
  one imposes additional non-vacuous conditions such as root essentiality,
  active use of outside coordinates, a non-adaptive root rule, or divergent
  outside variance.

## Notes

- The equality (1) requires \(B\ge0\).  For \(B<0\), the visible class is empty.
- The one-spare padding does not generally preserve the same positive threshold
  \(\theta\), because \(S_{k+1}>S_k\).  It preserves every fixed
  \(\theta'<\theta\), and it preserves the \(\theta=0\) nonempty-support
  condition exactly.
- This proposition does not prove \(U_k(\theta)\to0\).  It is a route-kill:
  "near-total-root visibility" is not a terminal subproblem distinct from the
  original prime-biased weighted union-free theorem.
