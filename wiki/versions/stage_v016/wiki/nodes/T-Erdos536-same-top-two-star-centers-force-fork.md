---
id: "T-Erdos536-same-top-two-star-centers-force-fork"
type: "theorem"
title: "Erdos 536 two distinct full EKR star centers below the same occupied top force a union fork"
status: "proved"
tags: ["center-uniqueness", "ekr-star", "erdos-536", "fork", "proved", "same-top", "theorem", "true"]
parents: ["T-Erdos536-top-local-EKR-trace-threshold-forces-fork", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T201605-erdos536-top-code-occupancy-student.json", "raw/student/20260531T201605-erdos536-top-code-occupancy.md", "theory/nodes/T-Erdos536-top-local-EKR-star-threshold-sharp.json", "theory/nodes/T-Erdos536-top-local-EKR-trace-threshold-forces-fork.json"]
---

# Theorem: Erdos 536 two distinct full EKR star centers below the same occupied top force a union fork

## Statement

Let \(C\) be a finite set of size \(s\), let \(r<s\le2r\), and let \(q_1\ne q_2\in C\). If a finite set family \(\mathcal F\) contains \(C\) and contains both full lower stars \(\{A\subseteq C\setminus\{q_1\}: |A|=r\}\) and \(\{B\subseteq C\setminus\{q_2\}: |B|=r\}\), then there are distinct \(A,B,C\in\mathcal F\) with \(A\cup B=C\). Consequently a fork-free occupied top can carry at most one full threshold-sharp EKR star center at a fixed lower rank.

## Dependencies

- [[wiki/nodes/T-Erdos536-top-local-EKR-trace-threshold-forces-fork|Erdos 536 occupied top local EKR lower trace threshold forces union fork]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T201605-erdos536-top-code-occupancy-student.json`
- `raw/student/20260531T201605-erdos536-top-code-occupancy.md`
- `theory/nodes/T-Erdos536-top-local-EKR-star-threshold-sharp.json`
- `theory/nodes/T-Erdos536-top-local-EKR-trace-threshold-forces-fork.json`

## Proof

\emph{Setup.}
Use the prime-biased product law
\[
\nu_k(p_i\in S)=\frac1{p_i},\qquad
S_k=\sum_{i\le k}\frac1{p_i},\qquad
H_{k,\theta}=\{S\subseteq P_k: |S|>\theta S_k\}.
\]
The active local model is the threshold-sharp EKR star below an occupied top:
if \(|C|=s\), \(r<s\le2r\), and \(q\in C\), then
\[
\mathcal A_{r,q}(C)=\{A\subseteq C\setminus\{q\}: |A|=r\}
\]
has exactly \(\binom{s-1}{r}\) members and contains no two members whose
union is \(C\). The AP asks whether global top-code occupancy, or center
entropy, prevents these sharp local stars from moving across a positive-mass
family without creating forks.

One useful local fact can be proved.

Let \(C\) be a finite set with \(|C|=s\), let \(r<s\le2r\), and let
\(q_1\ne q_2\in C\). Suppose a set family \(\mathcal F\) contains \(C\) and
contains the two full lower \(r\)-stars
\[
\mathcal A_{r,q_1}(C)=\{A\subseteq C\setminus\{q_1\}: |A|=r\},
\qquad
\mathcal A_{r,q_2}(C)=\{A\subseteq C\setminus\{q_2\}: |A|=r\}.
\]
Put \(t=2r-s\ge0\). Since \(r<s\), we have \(t\le s-2\), so choose
\[
I\subseteq C\setminus\{q_1,q_2\},\qquad |I|=t.
\]
The remaining set \(C\setminus(\{q_1,q_2\}\cup I)\) has size
\[
s-2-t=2(s-r-1),
\]
so split it into disjoint sets \(X,Y\) with
\[
|X|=|Y|=s-r-1.
\]
Now set
\[
A=I\cup X\cup\{q_2\},
\qquad
B=I\cup Y\cup\{q_1\}.
\]
Then \(|A|=|B|=r\), \(A\subseteq C\setminus\{q_1\}\), and
\(B\subseteq C\setminus\{q_2\}\). Therefore \(A\) lies in the first star and
\(B\) lies in the second. Also
\[
A\cup B=C.
\]
The three sets \(A,B,C\) are distinct. Hence \(\mathcal F\) contains a fork.

This proves the true node
\[
the Erdos536 same top two star centers force fork.
\]
Equivalently, a fork-free occupied top can carry at most one full
threshold-sharp EKR star center at a fixed lower rank. The remaining
center-entropy problem is therefore genuinely cross-top; it cannot be hidden
inside multiple full stars below a single occupied top.

Candidate:
the Erdos536 star fiber union occupied top density.

The full theorem remains open. The two-center lemma handles only the case
where two full star centers occur below the same occupied top. It does not
prove that unions of lower traces sampled below different occupied tops land
back in the occupied top code.

For two occupied tops \(C_1,C_2\) with centers \(q(C_1),q(C_2)\), the union
push-forward is
\[
(A,B)\mapsto A\cup B,\qquad
A\subseteq C_1\setminus\{q(C_1)\},\quad
B\subseteq C_2\setminus\{q(C_2)\}.
\]
If this push-forward has positive overlap with \(\mathcal F_k\), then the
desired occupied-union fork follows. I could not prove the needed overlap.
The obstruction remains a sparse top-code possibility: a positive-mass
occupied top set might in principle support many local stars while keeping the
union push-forward mostly outside the occupied layer. Existing rank-thin and
lacunary tools do not yet exclude this.

Candidate:
the Erdos536 center entropy compression for star fibers.

The full theorem remains open. The two-center lemma gives one solid
compression rule: in any fork-free threshold-sharp regime, a fixed occupied
top \(C\) and lower rank \(r\) cannot carry two different full star centers.
Thus a center map \(q(C,r)\), when a full threshold star is present, is locally
unique.

However, this local uniqueness does not yet imply a global entropy dichotomy.
The center map may still move across many occupied tops. Low support in exact
rank layers is controlled by the Erdos536 rank block anti concentration, but
low or high entropy in the center coordinate is not currently tied to
\(\nu_k\)-mass strongly enough. I did not prove that high center entropy
forces occupied-union collisions, nor that low center entropy compresses into
only \(o(\sqrt{S_k})\) effective rank/center layers.

Candidate:
the Erdos536 diagnostic sparse top code second moment.

No positive-mass sparse top-code construction was found. The diagnostic
second-moment setup is clearer after the two-center lemma. For a candidate
occupied top code \(\mathcal T_k\), define \(N(C)\) to be the number of pairs
\((A,B)\) of lower star traces, sampled from the selected threshold-star
fibers, such that
\[
A\cup B=C,\qquad C\in\mathcal T_k.
\]
A successful sparse-code obstruction would need positive \(\nu_k\)-mass for
\(\mathcal T_k\), nonsparse close central ranks, locally unique full star
centers, and \(N(C)=0\) or a negligible first moment over occupied tops.

The natural models still collapse in known ways. If the top code is restricted
to multiplicatively lacunary rank sets, the exact-layer template is union-free
but has vanishing mass by
the Erdos536 lacunary exact rank layer template union free mass zero. If the
top code is too dense in close ranks, the first moment of candidate unions
becomes large, but I did not prove a lower bound for occupied hits because
dependence between the top code and the selected centers is uncontrolled.

Thus the diagnostic route remains open, but the next useful target is sharper:
prove a top-code hitting lemma for the union push-forward under a locally
unique center map, or build an explicit positive-mass code violating that
hitting lemma.

the Erdos536 star fiber union occupied top density: candidate_open;
the Erdos536 center entropy compression for star fibers: candidate_open;
the Erdos536 diagnostic sparse top code second moment: candidate_open.

Admitted true node:
\[
the Erdos536 same top two star centers force fork.
\]

No Erdos 536 theorem was solved and no source counterexample was constructed.
The terminal Erdos 536 frontier remains open.

candidates around locally unique moving-star centers: one top-code hitting
lemma for the union push-forward, one weighted center-map regularity theorem,
and one explicit positive-mass code obstruction attempt with locally unique
centers.

_Proof source: `raw/student/20260531T201605-erdos536-top-code-occupancy.md`._

## Tags

`center-uniqueness`, `ekr-star`, `erdos-536`, `fork`, `proved`, `same-top`, `theorem`, `true`
