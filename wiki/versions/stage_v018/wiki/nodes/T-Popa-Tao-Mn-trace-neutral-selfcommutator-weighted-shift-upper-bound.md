---
id: "T-Popa-Tao-Mn-trace-neutral-selfcommutator-weighted-shift-upper-bound"
type: "theorem"
title: "T-Popa-Tao-Mn-trace-neutral-selfcommutator-weighted-shift-upper-bound"
status: "proved"
tags: ["proved", "theorem"]
parents: ["T-Popa-Tao-Mn-trace-neutral-selfcommutator-Horn-invariant", "T-Finite-matrix-spectral-certificate-principle"]
refs: ["oracle/responses/ORACLE-OS-20260604T-tao-popa-finite-selfcommutator-Mn-student-response.md", "raw/student/20260604T-tao-popa-finite-selfcommutator-Mn.md", "wiki/notes/tao-popa-finite-selfcommutator-Mn.md"]
---

# Theorem: T-Popa-Tao-Mn-trace-neutral-selfcommutator-weighted-shift-upper-bound

## Statement

For any ordering of the eigenvalues mu_1,...,mu_n of trace-zero Hermitian H, with partial sums S_k, one has alpha(H)<=max_k S_k-min_k S_k. This is realized by a nilpotent weighted shift after shifting the partial sums to be nonnegative.

## Scope

- Constructive finite-dimensional upper bound for trace-neutral self-commutator norm.

## Dependencies

- [[wiki/nodes/T-Popa-Tao-Mn-trace-neutral-selfcommutator-Horn-invariant|T-Popa-Tao-Mn-trace-neutral-selfcommutator-Horn-invariant]]
- [[wiki/nodes/T-Finite-matrix-spectral-certificate-principle|Finite matrix spectral certificate principle]]

## Proof and provenance references

- `oracle/responses/ORACLE-OS-20260604T-tao-popa-finite-selfcommutator-Mn-student-response.md`
- `raw/student/20260604T-tao-popa-finite-selfcommutator-Mn.md`
- `wiki/notes/tao-popa-finite-selfcommutator-Mn.md`

## Proof

If \(H=VV^*-V^*V\), then \(B=VV^*\) and \(Q=V^*V\) are positive, have the same eigenvalues \(\beta\), and
\[
H=B-Q=B+(-Q).
\]
Thus \(\lambda(H)\) lies in the Horn polytope for spectra
\[
\beta
\quad\text{and}\quad
(-\beta_n,\ldots,-\beta_1),
\]
and \(\|V\|^2=\beta_1\).

Conversely, if \(\beta\) is feasible in the displayed Horn condition, then there are Hermitian matrices \(B\ge0\) and \(Y\le0\) with spectra
\[
\lambda(B)=\beta,
\qquad
\lambda(Y)=(-\beta_n,\ldots,-\beta_1),
\]
such that \(B+Y\) has the same spectrum as \(H\). Put \(Q=-Y\). Then \(Q\ge0\) and \(Q\) has the same spectrum as \(B\). After unitary conjugacy we may assume
\[
H=B-Q.
\]
Since \(B,Q\ge0\) have the same spectrum, there is a unitary \(U\) with
\[
Q=U^*BU.
\]
Set
\[
V=B^{1/2}U.
\]
Then
\[
VV^*=B,\qquad V^*V=U^*BU=Q,
\]
so
\[
VV^*-V^*V=H,
\]
and
\[
\|V\|^2=\|B\|=\beta_1.
\]

Let \((\mu_1,\ldots,\mu_n)\) be any ordering of the eigenvalues of \(H\). Define partial sums
\[
S_0=0,\qquad S_k=\sum_{j=1}^k\mu_j.
\]
If
\[
0\le S_k\le T
\]
for all \(k\), then the nilpotent weighted shift with squared weights
\[
S_1,S_2,\ldots,S_{n-1}
\]
satisfies
\[
VV^*-V^*V=\operatorname{diag}(\mu_1,\ldots,\mu_n),
\qquad
\|V\|^2\le T.
\]
After shifting all partial sums by a constant, this gives
\[
\alpha(H)
\le
\min_{\pi\in S_n}
\left(
\max_{0\le k\le n}S_k^\pi-\min_{0\le k\le n}S_k^\pi
\right).
\]
For \(H_0\), the ordering
\[
\left(\frac45,-\frac35,\frac45,-\frac12,-\frac12\right)
\]
has partial sums
\[
0,\frac45,\frac15,1,\frac12,0,
\]
so the weighted-shift bound gives \(\alpha(H_0)\le1\), which is sharp by the Horn lower bound above.

The \(M_3\) spectral-radius theorem does not extrapolate to all \(n\). In dimension \(5\), intermediate Horn inequalities impose constraints invisible to the endpoint eigenvalues. The correct finite trace-neutral self-commutator norm is a Horn feasibility invariant, with weighted shifts providing constructive upper bounds.

This is finite-dimensional source-model progress adjacent to Tao's \(3\times3\) commutator model. It does not solve the infinite \(B(H)\) \(v^*\)-block problem.

_Proof source: `raw/student/20260604T-tao-popa-finite-selfcommutator-Mn.md`._

## Tags

`proved`, `theorem`
