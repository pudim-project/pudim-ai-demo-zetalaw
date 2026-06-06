---
id: "T-Erdos536-fixed-coordinate-toggle-layer-template-union-free-rank-thin"
type: "theorem"
title: "Erdos 536 fixed coordinate two layer toggle template is union free coherent intersecting shadow and rank thin"
status: "proved"
tags: ["diagnostic", "erdos-536", "fixed-center", "proved", "rank-thin", "theorem", "true"]
parents: ["T-Finite-combinatorial-packing-shadow-principle"]
refs: ["librarian/audits/LA-20260531T191459-erdos536-coherent-intersecting-shadows-student.json", "raw/student/20260531T191459-erdos536-coherent-intersecting-shadows.md", "theory/nodes/T-Erdos536-disjoint-defect-shadow-equivalent-fork.json", "theory/nodes/T-Erdos536-rank-block-anti-concentration.json"]
---

# Theorem: Erdos 536 fixed coordinate two layer toggle template is union free coherent intersecting shadow and rank thin

## Statement

Fix \(q\in P_k\) and an integer \(r\). The two-layer toggle family \(\mathcal T_{k,r,q}=\{A\subseteq P_k\setminus\{q\}: |A|=r\}\cup\{A\cup\{q\}: A\subseteq P_k\setminus\{q\}, |A|=r\}\) is union-free, every occupied-top defect shadow has no disjoint defect pair, and \(\mathcal T_{k,r,q}\) is contained in the two exact ranks \(r\) and \(r+1\). Hence its \(\nu_k\)-mass tends to zero by `T-Erdos536-rank-block-anti-concentration`.

## Dependencies

- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `librarian/audits/LA-20260531T191459-erdos536-coherent-intersecting-shadows-student.json`
- `raw/student/20260531T191459-erdos536-coherent-intersecting-shadows.md`
- `theory/nodes/T-Erdos536-disjoint-defect-shadow-equivalent-fork.json`
- `theory/nodes/T-Erdos536-rank-block-anti-concentration.json`

## Proof

\emph{Setup.}
Let
\[
S_k=\sum_{i\le k}\frac1{p_i},
\qquad
\nu_k(p_i\in S)=\frac1{p_i},
\qquad
H_{k,\theta}=\{S\subseteq P_k: |S|>\theta S_k\}.
\]
For \(C\in\mathcal F_k\), the occupied-top defect shadow is
\[
\mathsf D_{\mathcal F_k}(C)
=
\{C\setminus A:A\in\mathcal F_k,\ A\subsetneq C\}.
\]
The true lemma
the Erdos536 disjoint defect shadow equivalent fork says that a disjoint
defect pair below \(C\) is exactly a lower-shadow fork \(A\cup B=C\). Thus a
fork-free family has every occupied-top defect shadow intersecting.

Candidate:
the Erdos536 cross top union forcing coherent defect shadows.

No proof was found. The candidate asks for the remaining global step:
\[
\text{positive mass + broad rank support + all top shadows intersecting}
\quad\Longrightarrow\quad
\text{some cross-top union fork}.
\]
The currently available true tools prove the local equivalence between
non-intersecting top shadows and forks, but not the cross-top forcing principle.

The fixed-coordinate toggle template below is a useful boundary test. It has
coherent intersecting shadows and no forks, so cross-top forcing cannot hold
without the positive-mass/non-rank-thin hypotheses. In that template the
obstruction collapses to two ranks, exactly as the rank-profile route predicts.

Candidate:
the Erdos536 rank profile collapse coherent intersecting shadows.

No proof was found, but every tested coherent template was rank-thin.

The clean diagnostic template is the fixed-coordinate toggle layer. Fix a
coordinate \(q\in P_k\) and an integer \(r\). Define
\[
\mathcal T_{k,r,q}
=
\{A\subseteq P_k\setminus\{q\}: |A|=r\}
\cup
\{A\cup\{q\}: A\subseteq P_k\setminus\{q\}, |A|=r\}.
\]
When \(r>\theta S_k\), this family is contained in \(H_{k,\theta}\).

It is union-free. If two members both omit \(q\), their union omits \(q\) and
is either one of the operands or has rank \(>r\), so it is not a third member
of \(\mathcal T_{k,r,q}\). If two members both contain \(q\), their union is
either one operand or has rank \(>r+1\), so it is not a third member. If
\[
X\subseteq P_k\setminus\{q\},\quad |X|=r,
\qquad
Y\cup\{q\}\in\mathcal T_{k,r,q},
\]
then \(X\cup(Y\cup\{q\})\) is either \(Y\cup\{q\}\), one of the operands, or
has rank \(>r+1\). Hence no three distinct members satisfy \(A\cup B=C\).

Its occupied-top defect shadows are coherent and intersecting. A rank-\(r\)
top omitting \(q\) has no lower trace inside \(\mathcal T_{k,r,q}\). A
rank-\(r+1\) top \(Y\cup\{q\}\) has exactly one lower trace \(Y\), so its
defect shadow is \(\{\{q\}\}\). Thus every occupied-top shadow has no disjoint
defect pair.

However, the template is rank-thin: it is contained in the two exact ranks
\[
\{r,r+1\}.
\]
By the Erdos536 rank block anti concentration, its \(\nu_k\)-mass tends to
zero uniformly for any choice of \(r=r_k\). This proves that fixed-center
coherence is not a positive-mass obstruction.

Admitted true node:
\[
the Erdos536 fixed coordinate toggle layer template union free rank thin.
\]

The full rank-profile collapse theorem remains open because I could not prove
that every coherent intersecting-shadow system reduces to fixed-coordinate
toggle layers or similarly rank-thin templates.

Candidate:
the Erdos536 diagnostic coherent positive mass intersecting shadow system.

No positive-mass coherent system was constructed.

Template tests:

Fixed centers give the toggle-layer template above: coherent, fork-free, but
  rank-thin and vanishing.
Full local large-defect shields have high local trace mass and zero top
  coverage, but the Erdos536 naive large defect downset shield has internal forks
  shows the full downset already has internal forks.
Exact-rank or few-rank variants avoid internal forks but are rank-thin.
Moving centers are the unresolved case. They are the first template that
  might spread mass across many ranks, but moving centers also create the
  expected cross-top-union risk: lower traces selected under different top
  centers may unite to an occupied top.

the Erdos536 cross top union forcing coherent defect shadows: candidate_open;
the Erdos536 rank profile collapse coherent intersecting shadows: candidate_open;
the Erdos536 diagnostic coherent positive mass intersecting shadow system: candidate_open.

Admitted true diagnostic node:
\[
the Erdos536 fixed coordinate toggle layer template union free rank thin.
\]

No Erdos 536 theorem was solved and no source counterexample was constructed.
The frontier is narrower: fixed-center coherent shadows are harmless because
they collapse to two ranks, while full local shields are killed by internal
forks. The remaining obstruction, if any, must use moving centers or a more
subtle many-rank coordination without creating cross-top unions.

around center drift in coherent intersecting-shadow systems: one fixed-center
collapse theorem, one moving-center cross-top fork theorem, and one diagnostic
lacunary/moving-center construction route.

_Proof source: `raw/student/20260531T191459-erdos536-coherent-intersecting-shadows.md`._

## Tags

`diagnostic`, `erdos-536`, `fixed-center`, `proved`, `rank-thin`, `theorem`, `true`
