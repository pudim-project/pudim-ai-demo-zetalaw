---
id: "T-Erdos536-fixed-coordinate-positive-mass-non-escape"
type: "theorem"
title: "Erdos536 fixed coordinate positive mass non escape prime biased"
status: "proved"
tags: ["coordinate-marginal", "erdos-536", "persistence", "prime-biased", "proved", "student-proof", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private Oracle audit", "private proof note"]
---

# Theorem: Erdos536 fixed coordinate positive mass non escape prime biased

## Statement

Fixed-coordinate positive-mass non-escape: if \(\nu_k(\mathcal F_k)\ge\varepsilon\) and a fixed coordinate \(i\) has conditional marginal at least \(\alpha\) on \(\mathcal F_k\), then \(\alpha\varepsilon\le\nu_k(i\in S)=1/p_i\), hence \(p_i\le1/(\alpha\varepsilon)\). Thus a fixed persistent coordinate in a positive-mass branch lies in a bounded prime window.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private Oracle audit`
- `private proof note`

## Proof

Node promoted: the Erdos536 product deletion mass transport.

Let \\(q_i=1/p_i\\) and let
\[
\nu_k(S)=\prod_{i\in S}q_i\prod_{i\notin S}(1-q_i).
\]
If \\(A=C\setminus D\\), then the only coordinates whose product-measure factors change from \\(C\\) to \\(A\\) are the coordinates of \\(D\\). Therefore
\[
\frac{\nu_k(A)}{\nu_k(C)}
=\prod_{i\in D}\frac{1-q_i}{q_i}
=\prod_{i\in D}(p_i-1).
\]
Equivalently,
\[
\nu_k(A)=\nu_k(C)\prod_{i\in D}(p_i-1).
\]

For any actual lower-trace relation \\(R\\subseteq\{(C,A,D):A=C\setminus D\}\\), summing over triples gives
\[
\sum_{(C,A,D)\in R}\nu_k(A)
=
\sum_C\nu_k(C)
  \sum_{D\in\mathcal D_R(C)}\prod_{i\in D}(p_i-1).
\]
If each lower trace \\(A\\) has multiplicity at most \\(M\\) in \\(R\\), then the left side is at most \\(M\nu_k(\mathcal L)\le M\\). Hence active tops with average deletion weight at least \\(L\\) have mass at most \\(M/L\\).

This is an algebraic product-measure lemma. Its Erdos536 power depends on controlling actual lower-trace multiplicity.

Node promoted: the Erdos536 fixed coordinate positive mass non escape.

Let \\(\mathcal F_k\\subseteq2^{[k]}\\) have \\(\nu_k(\mathcal F_k)\ge\varepsilon\\). If a fixed coordinate \\(i\\) has conditional marginal at least \\(\alpha\\) on \\(\mathcal F_k\\), then
\[
\alpha\varepsilon
\le \nu_k(\{S\in\mathcal F_k:i\in S\})
\le \nu_k(i\in S)
=\frac1{p_i}.
\]
Thus
\[
p_i\le\frac1{\alpha\varepsilon}.
\]
A fixed persistent coordinate on a positive-mass branch therefore cannot escape to arbitrarily large primes. This does not solve a top-dependent moving-coordinate branch.

Node promoted: the Erdos536 projective design near top shadow identity.

Let \\(C\\) be the point set of a projective-plane-like design and let \\(D,E\\) be distinct line defects with \\(D\cap E=\{x\}\\). For complement traces \\(A_D=C\setminus D\\) and \\(A_E=C\setminus E\\),
\[
A_D\cup A_E
=(C\setminus D)\cup(C\setminus E)
=C\setminus(D\cap E)
=C\setminus\{x\}.
\]
So every design pair creates a near-top shadow. A positive-mass global realization must explain whether these near-top shadows are occupied, forbidden, endpoint-shielded, or absent from the actual lower-trace relation.

Node introduced open: the Erdos536 lower trace multiplicity control gap.

The deletion mass-transport lemma turns large deletion weights into small top mass only when lower-trace multiplicities are bounded or otherwise controlled. Uncontrolled multiplicity can absorb the large factors \\(\prod_{i\in D}(p_i-1)\\). This gap now separates the clean algebra from the global lower-trace-poor and spread-design branches.

Candidate: the Erdos536 lower trace poor prime biased density dichotomy.

The product deletion mass-transport lemma gives a concrete sink mechanism: if lower-trace-poor admissibility forces actual lower traces with bounded multiplicity and large deletion weights, positive-mass active tops vanish. However, this pass did not prove the weighted comparable-pair/shadow/LYM estimate, did not reduce lower-trace-poor admissibility to antichain or comparable-pair exclusion, and did not construct a positive-mass non-rank-thin lower-trace-poor family. The candidate remains open.

Candidate: the Erdos536 spread design prime biased realization or vanishing.

The near-top shadow identity strengthens the local projective-plane audit beyond the basic comparable/union obstruction. It shows that any real spread-design branch must account for shadows \\(C\setminus\{x\}\\). Combined with product deletion mass transport, high-index or large defects pay large measure factors unless multiplicity or shielding intervenes. This pass did not prove actual positive-mass realization, rank-thin collapse, endpoint shielding, or vanishing. The candidate remains open.

Candidate: the Erdos536 unbounded moving coordinate tightness or descent.

The fixed-coordinate non-escape lemma proves that persistent fixed coordinates in positive-mass branches lie in bounded prime windows. Together with the previous bounded-window persistence pigeonhole, this handles only the fixed-coordinate case. A genuinely top-dependent moving coordinate can still escape every bounded window. No strict core/shield lexicographic descent and no explicit moving-coordinate obstruction construction were proved. The candidate remains open.

the Erdos536 product deletion mass transport: true local product-measure lemma.
the Erdos536 fixed coordinate positive mass non escape: true local product-measure lemma.
the Erdos536 projective design near top shadow identity: true local design identity.
the Erdos536 lower trace multiplicity control gap: open obstruction.
the Erdos536 lower trace poor prime biased density dichotomy: candidate_open.
the Erdos536 spread design prime biased realization or vanishing: candidate_open.
the Erdos536 unbounded moving coordinate tightness or descent: candidate_open.
the Erdos536 coordinate coverage lower trace forces fork: remains open.
the Erdos536 prime biased weighted union free frontier: remains open.

_Proof source: `private proof note`._

## Tags

`coordinate-marginal`, `erdos-536`, `persistence`, `prime-biased`, `proved`, `student-proof`, `theorem`, `true`
