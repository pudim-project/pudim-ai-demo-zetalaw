---
id: mrw-0d6b8cbd7ced
type: note
title: Bounded-deletion rank-congruence obstruction for union-free containers
aliases: ["mrw-0d6b8cbd7ced", "Bounded-deletion rank-congruence obstruction for union-free containers"]
status: proved
tags: [note, proved, erdos-536, union-free, bounded-deletion, rank-congruence, obstruction, support-tail, container]
parents: [mrw-bf35ac1a9ad3, mrw-55a8d9eddd2e, mrw-d0402aea6f58, mrw-cc4f876149b7, mrw-3c39ca3d1973]
refs: ["references/sources/20260519T133426Z-bounded-deletion-container-context.md"]
  - raw/20260519T133426Z-erdos536-cross-fiber-container.md
  - references/requests/20260519T133426Z-bounded-deletion-erudition-gate.md
  - references/sources/20260519T133426Z-bounded-deletion-container-context.md
  - oracle/responses/20260519T133426Z-erdos536-bounded-deletion-oracle-response.md
---

# Note: Bounded-deletion rank-congruence obstruction for union-free containers

## Statement

Let \(d\ge1\) be fixed.  Let \(P_k=\{p_1,\ldots,p_k\}\) be the first \(k\)
primes, put
\[
q_i=\frac1{p_i},\qquad
S_k=\sum_{i\le k}q_i,
\]
and let \(\nu_k\) be the product law on \(2^{P_k}\) with
\(\nu_k(p_i\in S)=q_i\).  Define the bounded-deletion union hypergraph
\(\mathcal H_{\le d}(P_k)\) to have edges
\(\{A,B,C\}\) such that
\[
A,B\subsetneq C,\qquad A\ne B,\qquad A\cup B=C,
\]
and
\[
1\le |C\setminus A|\le d,\qquad
1\le |C\setminus B|\le d.
\]

Put \(m=d+1\).  For any residue \(a\in\{0,\ldots,m-1\}\), the rank-congruence
family
\[
\mathcal R_{k,a}^{(m)}
=
\{S\subseteq P_k:\ |S|\equiv a\pmod m\}
\]
is independent in \(\mathcal H_{\le d}(P_k)\).  Moreover, for every fixed
\(0\le\theta<1\),
\[
\nu_k\bigl(\mathcal R_{k,a}^{(m)}\cap H_{k,\theta}\bigr)
\longrightarrow \frac1m,
\qquad
H_{k,\theta}=\{S:\ |S|>\theta S_k\}.
\]

Consequently, the fixed-\(d\) bounded-deletion hypergraph
\(\mathcal H_{\le d}(P_k)\) does not have the prime-biased high-support
supersaturation needed to prove the weighted union-free theorem
[[mrw-55a8d9eddd2e]].  In particular, the two-spare-tail faces
\[
T\cup\{x\},\qquad T\cup\{y\},\qquad T\cup\{x,y\}
\]
correspond to fixed \(d=1\) and are avoided by a parity-rank family of
asymptotic high-support mass \(1/2\).

## Proof

First prove independence.  Suppose that \(A,B,C\in\mathcal R_{k,a}^{(m)}\)
formed an edge of \(\mathcal H_{\le d}(P_k)\).  Then
\[
|C|-|A|=|C\setminus A|
\]
is a positive integer at most \(d\).  Since \(|A|\equiv |C|\pmod m\), this
difference is divisible by \(m=d+1\), which is impossible.  Hence no edge of
\(\mathcal H_{\le d}(P_k)\) is contained in \(\mathcal R_{k,a}^{(m)}\).

It remains to compute the biased rank-residue mass.  Let
\[
X_k=|S|,\qquad S\sim\nu_k.
\]
For \(\omega=e^{2\pi i/m}\) and \(1\le r<m\), independence gives
\[
\mathbb E\,\omega^{rX_k}
=
\prod_{i\le k}(1-q_i+q_i\omega^r).
\]
Since \(\omega^r\ne1\), there is \(c_m>0\) such that
\[
|1-q+q\omega^r|\le \exp(-c_m q)
\qquad(0\le q\le1/2).
\]
By the divergence of the reciprocal-prime sum, \(S_k=\sum_{i\le k}q_i\to\infty\).
It follows that
\[
\mathbb E\,\omega^{rX_k}\to0
\qquad(1\le r<m).
\]
Fourier inversion on \(\mathbb Z/m\mathbb Z\) therefore gives
\[
\nu_k(X_k\equiv a\pmod m)
=
\frac1m\sum_{r=0}^{m-1}\omega^{-ar}\mathbb E\,\omega^{rX_k}
\longrightarrow \frac1m.
\]

Finally, \(X_k\) has mean \(S_k\) and variance
\[
V_k=\sum_{i\le k}q_i(1-q_i)\le S_k.
\]
If \(0\le\theta<1\), Chebyshev's inequality gives
\[
\nu_k(X_k\le\theta S_k)
\le
\frac{V_k}{(1-\theta)^2S_k^2}
\le
\frac1{(1-\theta)^2S_k}
\to0.
\]
Thus deleting the low-support event from a fixed rank residue does not change
its limiting mass, and
\[
\nu_k\bigl(\mathcal R_{k,a}^{(m)}\cap H_{k,\theta}\bigr)\to\frac1m.
\]
This proves the claim.

## Depends on

- [[mrw-bf35ac1a9ad3]] Core-fiber decomposition for union-free families
- [[mrw-55a8d9eddd2e]] Prime-biased weighted union-free theorem
- [[mrw-d0402aea6f58]] Biased lower-shadow union-cover problem for Erdos 536
- [[mrw-cc4f876149b7]] Intersecting deletion-trace obstruction for lower-shadow
  union covers
- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree
  residuals
- Standard input: \(\sum_p 1/p=\infty\).

## Used by

- Next container/deletion-trace route: any proof must use unbounded deletion
  traces, a genuine product-measure container for the full union hypergraph, or
  a mechanism that turns bounded-deletion resistance into a full pair-link
  triple.  A fixed-\(d\) bounded-deletion supersaturation theorem alone is
  insufficient.

## Notes

The rank-congruence families are not counterexamples to the full union-free
theorem.  For \(k\) large enough they contain ordinary union triples with
large deletion sizes: choose a set \(C\) of size \(c\equiv a\pmod m\) and two
disjoint nonempty deletion sets \(D,E\subseteq C\) with \(|D|=|E|=m\); then
\[
A=C\setminus D,\qquad B=C\setminus E
\]
lie in the same residue class and satisfy \(A\cup B=C\).  Thus the obstruction
is not to [[mrw-55a8d9eddd2e]] itself, but to any attempted proof whose
terminal obstruction is a fixed bounded menu of local deletion faces.  If
\(d=d(k)\to\infty\), the residue-class mass \(1/(d(k)+1)\) may vanish and the
Fourier estimate would need a separate uniform audit; this note deliberately
records only the fixed-\(d\) obstruction.
