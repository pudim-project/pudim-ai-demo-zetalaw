---
id: mrw-30aae977a4b6
type: proposition
title: Finite-core high-support cylinders force lower-shadow triples
aliases: ["mrw-30aae977a4b6", "Finite-core high-support cylinders force lower-shadow triples"]
status: proved
tags: ["proposition", "proved", "erdos", "lcm", "squarefree", "biased-measure", "lower-shadow", "union-cover", "finite-junta", "support-tail", "patch-gate-audited"]
parents: [mrw-d0402aea6f58, mrw-cc4f876149b7, mrw-37dbc6aeedf9]
refs: []
---

# Proposition: Finite-core high-support cylinders force lower-shadow triples

## Statement

Let \(0\le\theta<1\).  Let \(Q\) be a fixed finite set of primes and let \(\mathcal G\subseteq2^Q\) be nonempty.  For a finite prime set \(P\supseteq Q\), define the finite-core high-support cylinder
\[
\mathcal C_{P,Q,\mathcal G,\theta}
=
\{S\subseteq P:\ S\cap Q\in\mathcal G,\ |S|>\theta S_P\},
\qquad
S_P=\sum_{p\in P}\frac1p.
\]
If \(P_k=\{p_1,\ldots,p_k\}\) and \(Q\subseteq P_k\) for all large \(k\), then \(\mathcal C_{P_k,Q,\mathcal G,\theta}\) contains a lower-shadow union-cover triple for all sufficiently large \(k\).  That is, for all sufficiently large \(k\), there are \(A,B,C\in\mathcal C_{P_k,Q,\mathcal G,\theta}\) such that
\[
A,B\subsetneq C,\qquad A\ne B,\qquad A\cup B=C.
\]

## Proof

Choose \(U\in\mathcal G\).  For \(P=P_k\), put \(R=P\setminus Q\).  Since every prime is at least \(2\),
\[
S_P\le \frac{|P|}{2}.
\]
Because \(\theta<1\) and \(Q\) is fixed, for all sufficiently large \(k\) there is an integer \(r\) satisfying
\[
r+|U|>\theta S_P
\qquad\text{and}\qquad
r+2\le |R|.
\]
For example, take \(r=\max(0,\lfloor\theta S_P\rfloor+1-|U|)\); the second inequality holds for large \(k\) since \(|R|=k-|Q|\) grows linearly while \(S_P\le k/2\).

Choose \(T\subseteq R\) with \(|T|=r\), and choose two distinct primes \(x,y\in R\setminus T\).  Define
\[
A=U\cup T\cup\{x\},\qquad
B=U\cup T\cup\{y\},\qquad
C=U\cup T\cup\{x,y\}.
\]
All three sets have the same trace \(U\) on \(Q\), so all satisfy the finite-core condition.  They also all have size greater than \(\theta S_P\), because \(U\cup T\) already has size greater than \(\theta S_P\).  Thus \(A,B,C\in\mathcal C_{P,Q,\mathcal G,\theta}\).

Finally,
\[
A,B\subsetneq C,\qquad A\ne B,\qquad A\cup B=C,
\]
so they form the required lower-shadow union-cover triple.

## Depends on

- [[wiki/nodes/mrw-d0402aea6f58|Biased lower-shadow union-cover problem for Erdos 536]]
- [[wiki/nodes/mrw-cc4f876149b7|Intersecting deletion-trace obstruction for lower-shadow union covers]]
- [[wiki/nodes/mrw-37dbc6aeedf9|Biased squarefree residual problem for Erdos 536]]

## Used by

- Rules out fixed finite-junta and tail-insensitive cylinder counterexamples to the biased lower-shadow route.

## Notes

- This proposition is deterministic; it does not require a positive biased mass lower bound.
- The result is not a junta theorem.  It only says that a family whose membership depends on finitely many core coordinates, together with the high-support cutoff, cannot itself be lower-shadow union-cover-free once enough tail primes are available.
- Any genuine positive-mass counterexample must therefore use tail-sensitive structure, not only a fixed finite core pattern.
