---
id: "T-Popa-Tao-low-dimensional-selfcommutator-threshold"
type: "theorem"
title: "T-Popa-Tao-low-dimensional-selfcommutator-threshold"
status: "proved"
tags: ["proved", "theorem"]
parents: ["T-Popa-Tao-M3-trace-neutral-self-commutator-normal-form", "T-Popa-Tao-M4-selfcommutator-spectral-radius-formula", "T-Popa-Tao-M5-trace-neutral-selfcommutator-spectral-radius-counterexample", "T-Finite-matrix-spectral-certificate-principle"]
refs: ["oracle/responses/ORACLE-OS-20260604T-tao-popa-M4-selfcommutator-classification-student-response.md", "raw/student/20260604T-tao-popa-M4-selfcommutator-classification.md", "wiki/notes/tao-popa-M4-selfcommutator-classification.md"]
---

# Theorem: T-Popa-Tao-low-dimensional-selfcommutator-threshold

## Statement

For trace-zero Hermitian finite self-commutators, the spectral-radius norm formula holds in dimensions 3 and 4, but fails in dimension 5.

## Scope

- Summary theorem combining the M3 theorem, M4 theorem, and M5 counterexample.

## Dependencies

- [[wiki/nodes/T-Popa-Tao-M3-trace-neutral-self-commutator-normal-form|Popa-Tao M3 trace-neutral self-commutator normal form]]
- [[wiki/nodes/T-Popa-Tao-M4-selfcommutator-spectral-radius-formula|T-Popa-Tao-M4-selfcommutator-spectral-radius-formula]]
- [[wiki/nodes/T-Popa-Tao-M5-trace-neutral-selfcommutator-spectral-radius-counterexample|T-Popa-Tao-M5-trace-neutral-selfcommutator-spectral-radius-counterexample]]
- [[wiki/nodes/T-Finite-matrix-spectral-certificate-principle|Finite matrix spectral certificate principle]]

## Proof and provenance references

- `oracle/responses/ORACLE-OS-20260604T-tao-popa-M4-selfcommutator-classification-student-response.md`
- `raw/student/20260604T-tao-popa-M4-selfcommutator-classification.md`
- `wiki/notes/tao-popa-M4-selfcommutator-classification.md`

## Proof

Provenance:

Parent target: the Popa Tao M4 selfcommutator spectral radius classification.
Classification: finite-dimensional source-model progress.

For every trace-zero Hermitian \(H\in M_4(\mathbb C)\),
\[
\alpha(H):=
\inf\{\|V\|^2:\ H=VV^*-V^*V\}
=
\max(\lambda_{\max}(H),-\lambda_{\min}(H)).
\]

Thus the spectral-radius formula holds in \(M_4\). Combined with the \(M_5\) counterexample, the first possible failure occurs after dimension \(4\).

If
\[
H=VV^*-V^*V
\]
and \(t=\|V\|^2\), then
\[
H\le VV^*\le tI,
\qquad
-H\le V^*V\le tI.
\]
Therefore
\[
\lambda_{\max}(H)\le t,
\qquad
-\lambda_{\min}(H)\le t,
\]
so
\[
\alpha(H)\ge M:=\max(\lambda_{\max}(H),-\lambda_{\min}(H)).
\]

Normalize to \(M=1\). The zero case is trivial. Since \(\alpha(-H)=\alpha(H)\), it is enough to handle the case
\[
\lambda_1=1.
\]
Write the decreasing eigenvalue list as
\[
\lambda=(1,a,b,c),
\qquad
c=-1-a-b,
\]
with
\[
1\ge a\ge b\ge c\ge-1.
\]
The ordering and trace condition imply
\[
b\le0,\qquad
a+b\le0,\qquad
a+b+1\ge0,\qquad
a+2b+1\ge0.
\]

We use the Horn-orbit criterion for self-commutators. It is enough to exhibit
\[
1\ge\beta_1\ge\beta_2\ge\beta_3\ge\beta_4\ge0
\]
such that
\[
\lambda\in
\operatorname{Horn}\bigl(\beta,(-\beta_4,-\beta_3,-\beta_2,-\beta_1)\bigr).
\]

Set
\[
\beta=(1,-b,-a-b,0).
\]
Then \(\beta\) is decreasing and lies in \([0,1]^4\). The negative reversed spectrum is
\[
(-\beta_4,-\beta_3,-\beta_2,-\beta_1)
=
(0,a+b,b,-1),
\]
which is also decreasing.

Substitution into the full \(n=4\) Horn list reduces every Horn deficit to one of
\[
\begin{gathered}
0,\ 1,\ a,\ 2a,\ 1-a,\ -b,\ 1+b,\ 2+2b,\\
-a-b,\ 1+a,\ 1+a+b,\ a-b,\\
-a-2b,\ 1+a+2b,\ 1-2a-b,\ 1+2a+2b.
\end{gathered}
\]
Each term is nonnegative under the domain inequalities above and \(a\ge0\). Hence the Horn condition holds.

Set
\[
\beta=(1,-a-b,-b,0).
\]
Then \(\beta\) is decreasing and lies in \([0,1]^4\). The negative reversed spectrum is
\[
(-\beta_4,-\beta_3,-\beta_2,-\beta_1)
=
(0,b,a+b,-1),
\]
which is decreasing because \(a\le0\).

Substitution into the full \(n=4\) Horn list reduces every Horn deficit to one of
\[
\begin{gathered}
0,\ 1,\ -a,\ -2a,\ -b,\ -2b,\ -a-b,\ -2a-b,\ -2a-2b,\\
1-a,\ 1-b,\ 1+a,\ 1+a+b,\ a-b,\\
1-a+b,\ 2+a+2b,\ 1+a+2b,\ 1+2a+b,\ 1+2b.
\end{gathered}
\]
Each term is nonnegative under
\[
a\le0,\qquad a\ge b,\qquad b\le0,\qquad b\ge-1,
\qquad
a+b\le0,\qquad a+b+1\ge0,\qquad a+2b+1\ge0.
\]
Hence the Horn condition holds in this case as well.

By the Horn-orbit formula, in both cases there exist \(0\le B\le I\) and a unitary \(U\) such that, up to unitary conjugacy,
\[
H=B-UBU^*.
\]
Taking
\[
V=B^{1/2}U^*
\]
gives
\[
H=VV^*-V^*V,
\qquad
\|V\|^2=\|B\|=1.
\]
Undoing the normalization proves
\[
\alpha(H)\le M.
\]
Together with the lower bound, this proves the theorem.

The finite trace-neutral Hermitian self-commutator norm has the following low-dimensional behavior:

\(M_3\): spectral-radius formula holds.
\(M_4\): spectral-radius formula holds.
\(M_5\): spectral-radius formula fails; the Horn invariant is needed.

This remains finite source-model progress adjacent to Tao's commutator model and does not solve the infinite \(B(H)\) problem.

_Proof source: `raw/student/20260604T-tao-popa-M4-selfcommutator-classification.md`._

## Tags

`proved`, `theorem`
