---
id: mrw-bf35ac1a9ad3
type: proposition
title: Core-fiber decomposition for union-free families
aliases: ["mrw-bf35ac1a9ad3", "Core-fiber decomposition for union-free families"]
status: proved
tags: [proposition, proved, erdos-536, union-free, decomposition, junta, fiber, lower-shadow, support-tail]
parents: [mrw-3474bf5c904f, mrw-55a8d9eddd2e, mrw-b4075311abd3, mrw-30aae977a4b6]
refs: []
  - raw/20260519T125425Z-erdos536-union-aware-decomposition.md
  - references/requests/20260519T125425Z-union-aware-decomposition-erudition-gate.md
  - references/sources/20260519T125425Z-union-aware-decomposition-context.md
  - calculations/20260519T125425Z-erdos536-small-k-union-free-audit.md
  - oracle/responses/20260519T125425Z-erdos536-core-fiber-oracle-response.md
---

# Proposition: Core-fiber decomposition for union-free families

## Statement

Let \(P=Q\sqcup R\) be a finite disjoint decomposition.  For
\(\mathcal F\subseteq2^P\) and \(U\subseteq Q\), define the \(U\)-fiber
\[
\mathcal F_U=\{T\subseteq R:\ U\cup T\in\mathcal F\}.
\]

If \(\mathcal F\) is union-free, then the fibers satisfy the exact cross-fiber
constraint:

whenever \(U,V,W\subseteq Q\), \(A\in\mathcal F_U\),
\(B\in\mathcal F_V\), and \(C\in\mathcal F_W\) obey
\[
U\cup V=W,
\qquad
A\cup B=C,
\]
the three full sets
\[
U\cup A,\qquad V\cup B,\qquad W\cup C
\]
are not pairwise distinct.

Conversely, this cross-fiber obstruction detects every union-free violation:
if three pairwise distinct members \(X,Y,Z\in\mathcal F\) satisfy
\(X\cup Y=Z\), then their traces on \(Q\) and \(R\) give
\[
U\cup V=W,
\qquad
A\cup B=C
\]
with \(X=U\cup A\), \(Y=V\cup B\), and \(Z=W\cup C\).

In particular, every single fiber \(\mathcal F_U\) is itself union-free as a
family in \(2^R\).

Consequently, exact core cylinders cannot be union-free once the tail has
enough room above the high-support cutoff.  More explicitly, let
\(0\le\theta<1\), let \(\nu_P\) be the prime-biased product law, put
\[
S_P=\sum_{p\in P}\frac1p,
\]
and let
\[
\mathcal C_{P,Q,\mathcal G,\theta}
=
\{S\subseteq P:\ S\cap Q\in\mathcal G,\ |S|>\theta S_P\}
\]
for some nonempty \(\mathcal G\subseteq2^Q\).  If there is \(U\in\mathcal G\)
such that
\[
|P\setminus Q|\ge2
\qquad\text{and}\qquad
|U|+|P\setminus Q|-1>\theta S_P,
\]
then \(\mathcal C_{P,Q,\mathcal G,\theta}\) contains three distinct members
\(A,B,C\) with
\[
A\cup B=C.
\]
Thus it is not union-free.

## Proof

Assume \(\mathcal F\) is union-free and fix
\[
U,V,W\subseteq Q,\qquad
A\in\mathcal F_U,\quad B\in\mathcal F_V,\quad C\in\mathcal F_W
\]
with \(U\cup V=W\) and \(A\cup B=C\).  By the definition of the fibers,
\[
U\cup A,\qquad V\cup B,\qquad W\cup C
\]
are members of \(\mathcal F\).  Their union relation is
\[
(U\cup A)\cup(V\cup B)
=(U\cup V)\cup(A\cup B)
=W\cup C.
\]
Since \(\mathcal F\) is union-free, these three members cannot be pairwise
distinct.  This proves the cross-fiber constraint.

Conversely, if \(X,Y,Z\in\mathcal F\) are pairwise distinct and
\(X\cup Y=Z\), write
\[
X=U\cup A,\qquad Y=V\cup B,\qquad Z=W\cup C
\]
according to the decomposition \(P=Q\sqcup R\).  Then necessarily
\[
U\cup V=W,
\qquad
A\cup B=C,
\]
so every union triple is recorded by the same cross-fiber relation.

For the single-fiber claim, take \(U=V=W\).  If
\(\mathcal F_U\) contained three distinct \(A,B,C\subseteq R\) with
\[
A\cup B=C,
\]
then \(U\cup A\), \(U\cup B\), and \(U\cup C\) would be three distinct members
of \(\mathcal F\) whose first two have union equal to the third, contradicting
union-freeness.  Hence \(\mathcal F_U\) is union-free.

Now prove the cylinder consequence.  Put \(R=P\setminus Q\), choose
\(U\in\mathcal G\), and suppose
\[
|R|\ge2
\qquad\text{and}\qquad
|U|+|R|-1>\theta S_P.
\]
Choose distinct \(x,y\in R\), put \(T=R\setminus\{x,y\}\), and define
\[
A=U\cup T\cup\{x\},
\qquad
B=U\cup T\cup\{y\},
\qquad
C=U\cup T\cup\{x,y\}.
\]
All three sets have trace \(U\) on \(Q\), and their sizes exceed
\(\theta S_P\): indeed \(|A|=|B|=|U|+|R|-1\) and
\(|C|=|U|+|R|\).  Hence
\(A,B,C\in\mathcal C_{P,Q,\mathcal G,\theta}\).  They are pairwise distinct
and satisfy
\[
A\cup B=C.
\]
Therefore the cylinder is not union-free.

## Depends on

- [[mrw-3474bf5c904f]] Union-aware weighted compression problem for
  prime-biased union-free families
- [[mrw-55a8d9eddd2e]] Prime-biased weighted union-free theorem
- [[mrw-b4075311abd3]] Union-free reformulation of the biased lower-shadow route
- [[mrw-30aae977a4b6]] Finite-core high-support cylinders force
  lower-shadow triples

## Used by

- The next junta/container route: any exact core decomposition must preserve
  the cross-fiber union constraint, and any full positive core cylinder with
  enough tail room is immediately forbidden.

## Notes

This proposition does not prove \(U_k(\theta)\to0\).  It sharpens the
replacement for ordinary shifting: a valid junta or container proof cannot
merely approximate \(\mathcal F\) by core cylinders.  It must either preserve
the cross-fiber union constraint after conditioning on a core, or quantify the
error caused by deleting most of the high-support tail from each core cell.
The first local draft used a weaker and edge-case-false cylinder threshold;
the Oracle audit caught the missing two-tail-coordinate condition, and the
statement above records the corrected locally checked version.
