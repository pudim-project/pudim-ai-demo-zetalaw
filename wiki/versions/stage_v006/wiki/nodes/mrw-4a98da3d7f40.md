---
id: mrw-4a98da3d7f40
type: proposition
title: Fair-thinning upward-boundary identity for lower-shadow candidates
aliases: ["mrw-4a98da3d7f40", "Fair-thinning upward-boundary identity for lower-shadow candidates"]
status: proved
tags: ["proposition", "proved", "erdos", "lcm", "squarefree", "biased-measure", "lower-shadow", "union-cover", "deletion-trace", "fair-thinning", "upward-boundary", "support-tail", "patch-gate-audited"]
parents: [mrw-c228258e6ab4, mrw-bf64e9def00c, mrw-d0402aea6f58, mrw-cc4f876149b7, mrw-3c39ca3d1973, mrw-37dbc6aeedf9]
refs: ["references/sources/20260519T085420Z-erdos-536-fair-thinning-boundary-context.md"]
---

# Proposition: Fair-thinning upward-boundary identity for lower-shadow candidates

## Statement

Let \(P\) be a finite set of primes.  Write \(\nu_P\) for the product law on \(2^P\) with \(\nu_P(p\in A)=1/p\), and write \(\widetilde\nu_P\) for the product law with
\[
\widetilde\nu_P(p\in C)=\min(2/p,1).
\]
Sample \(C\sim\widetilde\nu_P\), then obtain \(A\subseteq C\) by keeping each element of \(C\) independently with probability \(1/2\).  Then \(A\sim\nu_P\).

For \(\mathcal F\subseteq2^P\), define its upward closure
\[
\uparrow\mathcal F
=
\{C\subseteq P:\ \exists A\in\mathcal F\text{ with }A\subseteq C\}
\]
and its upward boundary
\[
\partial^+\mathcal F=(\uparrow\mathcal F)\setminus\mathcal F.
\]
Then the exact fair-thinning identity
\[
\nu_P(\mathcal F)
=
\Pr(A\in\mathcal F,\ C\in\mathcal F)
+
\Pr(A\in\mathcal F,\ C\in\partial^+\mathcal F)
\]
holds for every \(\mathcal F\).

Consequently, if \(\mathcal F\) is lower-shadow union-cover-free, then
\[
\Pr(A\in\mathcal F,\ C\in\partial^+\mathcal F)
\ge
\nu_P(\mathcal F)
-
\frac12\,\widetilde\nu_P(\mathcal F)
-
\mathbb E_{\widetilde\nu_P}\!\left[
1_{\mathcal F}(C)2^{-|C|}
\right].
\]
In particular, if \(\mathcal F\subseteq H_{P,\theta}=\{C:|C|>\theta S_P\}\), where \(S_P=\sum_{p\in P}1/p\), and \(\theta>0\), then
\[
\Pr(A\in\mathcal F,\ C\in\partial^+\mathcal F)
\ge
\nu_P(\mathcal F)
-
\left(\frac12+2^{-\theta S_P}\right)
\widetilde\nu_P(\mathcal F).
\]

## Proof

The marginal law of \(A\) is \(\nu_P\): for \(p=2\), \(p\in C\) with probability \(1\) and then survives with probability \(1/2=1/p\); for \(p>2\), \(p\in C\) with probability \(2/p\) and then survives with probability \(1/2\).  Coordinates are independent throughout.

If \(A\in\mathcal F\), then \(A\subseteq C\) by construction, so \(C\in\uparrow\mathcal F\).  Thus
\[
\Pr(A\in\mathcal F,\ C\in\uparrow\mathcal F)=\Pr(A\in\mathcal F)=\nu_P(\mathcal F).
\]
The disjoint decomposition
\[
\uparrow\mathcal F=\mathcal F\sqcup\partial^+\mathcal F
\]
therefore gives
\[
\nu_P(\mathcal F)
=
\Pr(A\in\mathcal F,\ C\in\mathcal F)
+
\Pr(A\in\mathcal F,\ C\in\partial^+\mathcal F),
\]
which is the identity.

If \(\mathcal F\) is lower-shadow union-cover-free, [[wiki/nodes/mrw-c228258e6ab4|Fair-thinning bound for lower-shadow deletion traces]] gives
\[
\Pr(A\in\mathcal F,\ C\in\mathcal F)
\le
\frac12\,\widetilde\nu_P(\mathcal F)
+
\mathbb E_{\widetilde\nu_P}\!\left[
1_{\mathcal F}(C)2^{-|C|}
\right].
\]
Substituting this upper bound into the exact identity proves the first lower bound for the upward-boundary hit probability.  If \(\mathcal F\subseteq H_{P,\theta}\) and \(\theta>0\), then \(2^{-|C|}\le2^{-\theta S_P}\) for every \(C\in\mathcal F\), giving the stated high-support specialization.

## Depends on

- [[wiki/nodes/mrw-c228258e6ab4|Fair-thinning bound for lower-shadow deletion traces]]
- [[wiki/nodes/mrw-bf64e9def00c|Upward-closed high-support families force lower-shadow triples]]
- [[wiki/nodes/mrw-d0402aea6f58|Biased lower-shadow union-cover problem for Erdos 536]]
- [[wiki/nodes/mrw-cc4f876149b7|Intersecting deletion-trace obstruction for lower-shadow union covers]]
- [[wiki/nodes/mrw-3c39ca3d1973|Pair-link shadow criterion for biased squarefree residuals]]
- [[wiki/nodes/mrw-37dbc6aeedf9|Biased squarefree residual problem for Erdos 536]]

## Used by

- Next #536 route: replace the vague "self-overlap gap" by a boundary alternative.  Either prove that a positive-mass high-support lower-shadow-free family cannot hide enough of \(\nu_P(\mathcal F)\) in \(\partial^+\mathcal F\), or construct a genuinely boundary-heavy nonmonotone counterexample and then test the full pair-link intervals.

## Notes

- The proposition is an exact coupling identity plus a consequence of the already proved fair-thinning ceiling.  It is not a proof of the biased lower-shadow union-cover theorem.
- When \(\mathcal F\) is upward-closed, \(\partial^+\mathcal F=\varnothing\), so the identity reduces to \(\Pr(A\in\mathcal F,\ C\in\mathcal F)=\nu_P(\mathcal F)\).  Together with [[wiki/nodes/mrw-bf64e9def00c|Upward-closed high-support families force lower-shadow triples]], this explains why the surviving obstruction must be genuinely nonmonotone.
- A positive-mass counterexample to the lower-shadow route must now be boundary-heavy under the fair-thinning coupling: many thinned members \(A\in\mathcal F\) must extend to \(C\in\uparrow\mathcal F\setminus\mathcal F\).  The next useful invariant is therefore an isoperimetric or container statement for this upward boundary under the \((\nu_P,\widetilde\nu_P)\) coupling.
