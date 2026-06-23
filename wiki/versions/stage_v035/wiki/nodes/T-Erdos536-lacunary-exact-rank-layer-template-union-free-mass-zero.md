---
id: "T-Erdos536-lacunary-exact-rank-layer-template-union-free-mass-zero"
type: "theorem"
title: "Erdos 536 lacunary exact rank layer template is union free but has zero prime biased mass in central windows"
status: "proved"
tags: ["erdos-536", "exact-rank-layers", "lacunary-ranks", "mass-zero", "proved", "theorem", "true", "union-free"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T193516-erdos536-central-window-moving-center-student.json", "raw/student/20260531T193516-erdos536-central-window-moving-center.md", "theory/nodes/T-Erdos536-central-lacunary-rank-windows-are-rank-thin.json"]
---

# Theorem: Erdos 536 lacunary exact rank layer template is union free but has zero prime biased mass in central windows

## Statement

Let \(R_k\subseteq\{0,1,\ldots,k\}\) be \(2\)-lacunary, meaning every \(r<s\) in \(R_k\) satisfies \(s>2r\). Then the exact rank-layer family \(\mathcal L_{R_k}=\{A\subseteq P_k: |A|\in R_k\}\) is union-free: it contains no distinct \(A,B,C\) with \(A\cup B=C\). If, in addition, the ranks are central-lacunary in the sense of `T-Erdos536-central-lacunary-rank-windows-are-rank-thin`, then \(\nu_k(\mathcal L_{R_k}\cap H_{k,\theta})\to0\) for each fixed \(0\le\theta<1\).

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T193516-erdos536-central-window-moving-center-student.json`
- `raw/student/20260531T193516-erdos536-central-window-moving-center.md`
- `theory/nodes/T-Erdos536-central-lacunary-rank-windows-are-rank-thin.json`

## Proof

\emph{Setup.}
Use the prime-biased product law
\[
\nu_k(p_i\in S)=\frac1{p_i},
\qquad
S_k=\sum_{i\le k}\frac1{p_i},
\qquad
H_{k,\theta}=\{S\subseteq P_k: |S|>\theta S_k\}.
\]
The previous pass proved that full fixed-center toggle templates with close
ranks contain forks. The remaining problem is whether moving centers can use
close central ranks without creating cross-top occupied unions.

Candidate:
the Erdos536 central window close rank drift forces fork.

No proof was found. The fixed-center close-rank proof has a simple full-layer
core: if \(r<s\le2r\), an \(s\)-set \(C\) contains two distinct \(r\)-subsets
\(A,B\) with \(A\cup B=C\). The moving-center problem is not this local
combinatorics; it is the occupancy step. Current tools prove that disjoint
defects below an occupied top give a fork, but they do not force the union of
two lower traces with incompatible centers to be an occupied top.

Thus the missing lemma is a density-to-coverage statement:
nonnegligible lower-trace mass on close central ranks, together with
incompatible moving centers, should force an occupied union top. I could not
prove this from the existing coherent-shadow hypotheses.

Candidate:
the Erdos536 sparse close rank moving center mass collapse.

The full candidate remains open because the AP's sparse alternative is stated
in terms of lower-trace density and center profiles, not just rank support.
However, the rank-bookkeeping part can be made precise.

Let \(R_k\subseteq\{0,1,\ldots,k\}\). If \(R_k\cap[1,MS_k]\) has no two ranks
\(r<s\le2r\), then its positive ranks grow by factors larger than \(2\).
Therefore
\[
|R_k\cap[1,MS_k]|\le 1+\lceil\log_2(MS_k)\rceil
=O_M(\log S_k)=o(\sqrt{S_k}).
\]
By the Erdos536 rank block anti concentration, the product mass of these ranks
inside the fixed central window tends to \(0\). The Markov bound
\[
\nu_k(|S|>MS_k)\le \frac1M
\]
then removes the upper tail after \(M\to\infty\). This proves the true node
\[
the Erdos536 central lacunary rank windows are rank thin.
\]

There is also a diagnostic exact-rank template. If \(R_k\) is \(2\)-lacunary,
meaning every \(r<s\) in \(R_k\) satisfies \(s>2r\), then
\[
\mathcal L_{R_k}=\{A\subseteq P_k: |A|\in R_k\}
\]
is union-free. Indeed, for \(A,B\in\mathcal L_{R_k}\) with
\(|A|\le |B|=r\), either \(A\cup B=B\), which cannot give a distinct third
witness, or \(|A\cup B|>r\). The next allowed rank in \(R_k\) is larger than
\(2r\), while \(|A\cup B|\le |A|+|B|\le2r\). Hence
\(|A\cup B|\notin R_k\). If the ranks are central-lacunary, the preceding
rank-thin lemma gives vanishing mass. This proves
\[
the Erdos536 lacunary exact rank layer template union free mass zero.
\]

These lemmas explain why lacunary rank spacing can avoid forks only by losing
product mass. They do not yet prove the full sparse-close-rank moving-center
collapse, because a moving-center system may have many ranks while being sparse
only in its lower-trace center profiles.

Candidate:
the Erdos536 diagnostic randomized moving center central window construction.

No positive-mass construction was found. The natural randomized templates split
into two regimes.

Dense close-rank templates behave like the full-layer model: once two close
central ranks carry enough lower traces, random or drifting center choices make
it difficult to prevent the union of two lower traces from landing in an
occupied top. I did not turn this into a second-moment or container theorem.

Sparse randomized-star templates can avoid many local forks, but the avoidance
appears to force exactly the sparse-close-rank behavior from Candidate 2. The
only clean deterministic construction found in this direction is the lacunary
exact-rank layer template above, and it has vanishing mass.

the Erdos536 central window close rank drift forces fork: candidate_open;
the Erdos536 sparse close rank moving center mass collapse: candidate_open;
the Erdos536 diagnostic randomized moving center central window construction: candidate_open.

Admitted true nodes:
\[
the Erdos536 central lacunary rank windows are rank thin,
\qquad
the Erdos536 lacunary exact rank layer template union free mass zero.
\]

No Erdos 536 theorem was solved and no source counterexample was constructed.
turn close central-rank lower-trace density and center drift into an occupied
union top, or construct a sparse random-code obstruction showing why that bridge
fails.

around close-rank density-to-coverage in moving-center systems: one occupied
union coverage theorem, one center-profile regularization theorem, and one
sparse random-code obstruction construction.

_Proof source: `raw/student/20260531T193516-erdos536-central-window-moving-center.md`._

## Tags

`erdos-536`, `exact-rank-layers`, `lacunary-ranks`, `mass-zero`, `proved`, `theorem`, `true`, `union-free`
