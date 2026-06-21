---
id: "T-not-Erdos536-weighted-defect-EKR-stability-normal-form"
type: "theorem"
title: "not Erdos536 weighted defect EKR stability normal form"
status: "proved"
tags: ["counterexample", "defect-sets", "erdos-536", "proved", "theorem", "true-negation", "weighted-intersecting"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private Oracle audit", "private proof note"]
---

# Theorem: not Erdos536 weighted defect EKR stability normal form

## Statement

There exist finite defect laws \(\lambda_N\) on subsets of a top coordinate set such that \(\lambda_N^{\otimes2}\{D\cap E=\varnothing\}\to0\), but every pairwise-intersecting subfamily has \(\lambda_N\)-mass at most \(1/2\). Hence the claim that small disjoint-pair probability implies an \(o(1)\)-mass deletion to a pairwise-intersecting support is false.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private Oracle audit`
- `private proof note`

## Proof

\emph{Setup.}
The true reduction already admitted is $normal: below an occupied top \(C\), if \(D=C\setminus A\) and \(E=C\setminus B\), then
\[
A\cup B=C\quad\Longleftrightarrow\quad D\cap E=\varnothing.
\]
Thus the remaining problem is to force positive disjoint-defect probability from structural hypotheses on the conditional defect law.

Candidate: $c1.

The overstrong claim says that if a conditional defect law \(\lambda\) has
\[
\lambda^{\otimes2}\{D\cap E=\varnothing\}=o(1),
\]
then, after discarding \(o(1)\) mass, the remaining defect support is pairwise intersecting. This is false even for finite laws on defect subsets.

Fix \(N\). Take \(2N\) abstract defect vertices
\[
X_1,Y_1,
\ldots,
X_N,Y_N
\]
and realize the disjointness graph as a perfect matching: \(X_i\cap Y_i=\varnothing\), while every other pair intersects. Such a set representation is obtained by assigning one private coordinate \(z_{uv}\) to each nonmatched unordered pair \(\{u,v\}\) and putting \(z_{uv}\) in exactly the two sets \(u,v\). No coordinate is assigned to the matched pairs \(\{X_i,Y_i\}\). Then the disjoint pairs are exactly the matched pairs.

Let \(\lambda_N\) be uniform on these \(2N\) defect sets. The ordered disjoint-pair probability is
\[
\lambda_N^{\otimes2}\{D\cap E=\varnothing\}
=\frac{2N}{(2N)^2}=\frac1{2N}\to0.
\]
However any pairwise-intersecting subfamily can contain at most one endpoint from each matched pair, hence has \(\lambda_N\)-mass at most \(1/2\). Therefore one must discard at least \(1/2\) mass to obtain a genuinely pairwise-intersecting support. This contradicts the claimed \(o(1)\)-discard conclusion.

If two separated defect-rank windows are desired, add private filler coordinates to all \(X_i\) and all \(Y_i\) so that the \(X\)-sets and \(Y\)-sets have two prescribed separated cardinalities. Private fillers do not change intersections, so the same matching obstruction persists.

Thus the correct replacement is weaker: small disjoint-pair probability gives a sparse disjointness graph, not closeness to an intersecting support. Any future stability theorem must add assumptions that exclude matching-like or sparse-graph disjointness obstructions.

Candidate: $c2.

The matching construction above can be arranged with two separated rank windows and no global common core. It therefore shows that the words "noncore" and "separated defect windows" are not yet strong enough unless they are formalized to exclude sparse matching-type disjointness graphs. The candidate might still be true under stronger admissibility conditions coming from actual lower traces of positive-mass union-free families, but that admissibility is not present in the AP statement and was not proved in this pass.

The remaining proof obligation is a genuine Erdos536-specific theorem: conditional defect laws induced by positive-mass lower traces cannot have matching-like sparse disjointness without either creating forks elsewhere, becoming rank-thin, or falling into an endpoint/core recursion.

Candidate: $c3.

The matching obstruction is also a fourth template for the contrapositive route: rank-diffuse, no global common core, no endpoint shield, and yet \(\lambda_N^{\otimes2}\{D\cap E=\varnothing\}\to0\). It does not prove that such a law is globally admissible as an Erdos536 lower-trace law, but it prevents promotion of the three-template exhaustion as stated.

The next route should add a fourth branch, or prove an admissibility lemma excluding sparse matching-like disjointness graphs below occupied tops.

$c1: candidate_refuted; add true negation $notC1.
$c2: candidate_open with matching-like obstruction model.
$c3: candidate_open with missing fourth-template/admissibility exclusion.

_Proof source: `private proof note`._

## Tags

`counterexample`, `defect-sets`, `erdos-536`, `proved`, `theorem`, `true-negation`, `weighted-intersecting`
