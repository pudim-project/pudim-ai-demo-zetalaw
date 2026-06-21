---
id: "T-Erdos536-naive-large-defect-downset-shield-has-internal-forks"
type: "theorem"
title: "Erdos 536 naive large defect downset shield contains internal union forks"
status: "proved"
tags: ["diagnostic", "erdos-536", "internal-fork", "large-defect-shield", "proved", "theorem", "true"]
parents: ["T-Erdos536-two-gate-admissibility-data-schema", "T-Finite-combinatorial-packing-shadow-principle"]
refs: ["private librarian audit", "private proof note", "theory/nodes/T-Erdos536-large-defect-local-trace-shield-zero-coverage.json"]
---

# Theorem: Erdos 536 naive large defect downset shield contains internal union forks

## Statement

For every finite set \(C_m\) with \(|C_m|=m\ge6\), the local large-defect downset \(\mathcal T_m=\{A\subseteq C_m: |A|\le m/2-1\}\) has internal forks: there exist distinct \(A,B,D\in\mathcal T_m\) with \(A\cup B=D\). In particular, the full local shield from `T-Erdos536-large-defect-local-trace-shield-zero-coverage` cannot be globalized by simply taking all shield traces as a union-free family.

## Dependencies

- [[wiki/nodes/T-Erdos536-two-gate-admissibility-data-schema|Erdos536 two gate admissibility data schema]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `theory/nodes/T-Erdos536-large-defect-local-trace-shield-zero-coverage.json`

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
For a family \(\mathcal F_k\) and an occupied top \(C\in\mathcal F_k\), define the support defect shadow
\[
\mathsf D_{\mathcal F_k}(C)
=
\{C\setminus A:A\in\mathcal F_k,\ A\subsetneq C\}.
\]
This is a support-level object. It deliberately ignores the biased mass
\(\mu_C(\mathcal L_{\mathcal F_k}(C))\), which was refuted as too strong in
the corresponding result.

For fixed \(C\in\mathcal F\), the defect shadow \(\mathsf D_{\mathcal F}(C)\)
contains two disjoint nonempty defects if and only if there are distinct
\(A,B,C\in\mathcal F\) with
\[
A\subsetneq C,\qquad B\subsetneq C,\qquad A\cup B=C.
\]
Indeed, if \(X,Y\in\mathsf D_{\mathcal F}(C)\) are disjoint and nonempty, write
\[
X=C\setminus A,\qquad Y=C\setminus B.
\]
Then \(A,B\in\mathcal F\), \(A,B\subsetneq C\), \(A\ne B\), and
\[
C\setminus(A\cup B)
=(C\setminus A)\cap(C\setminus B)
=X\cap Y
=\varnothing,
\]
so \(A\cup B=C\). Conversely, if \(A,B\subsetneq C\) and \(A\cup B=C\), then
\[
X=C\setminus A,\qquad Y=C\setminus B
\]
are nonempty members of \(\mathsf D_{\mathcal F}(C)\), and
\[
X\cap Y=C\setminus(A\cup B)=\varnothing.
\]

Admitted true node:
\[
the Erdos536 disjoint defect shadow equivalent fork.
\]

Candidate:
the Erdos536 occupied top support shadow forces coverage.

No proof was found. After the true support-shadow lemma, this candidate is the
right finite support formulation of the source frontier, with the already true
rank-thin alternative removed by
the Erdos536 rank block anti concentration.

The standard checks do not refute it:

Exact rank layers are fork-free, but their \(\nu_k\)-mass vanishes and they
  are rank-thin.
The full high-support family \(H_{k,\theta}\) has support shadows with
  disjoint defects below every sufficiently large occupied top, for instance
  \(C\setminus\{x\}\) and \(C\setminus\{y\}\) for distinct \(x,y\in C\).
The previously admitted local large-defect shield blocks only the pair
  covering of a chosen top; it is not yet a positive-mass global family.

The remaining missing theorem is global: a positive-mass, non-rank-thin
high-support family should force at least one occupied top with a
non-intersecting defect shadow. I could not prove this from the current tools.

Candidate:
the Erdos536 intersecting complement obstruction dichotomy.

No proof was found. The true support-shadow lemma shows that a fork-free family
has
\[
\mathsf D_{\mathcal F_k}(C)
\quad\text{intersecting for every occupied top }C\in\mathcal F_k.
\]
Thus the candidate asks for a local-to-global theorem:
\[
\text{all occupied-top defect shadows are intersecting}
\quad\Longrightarrow\quad
\mathcal F_k\text{ is rank-thin up to }o(1)\text{ mass}.
\]

The current obstruction is that intersecting defect shadows can be large
locally. The true node
the Erdos536 large defect local trace shield zero coverage gives, on a set
\(C_m\), the family
\[
\mathcal T_m=\{A\subseteq C_m: |A|\le m/2-1\},
\]
whose complements are pairwise intersecting and hence cannot cover \(C_m\) in
pairs. This shows a purely local EKR-style argument is not enough.

What is still missing is a coherence theorem across many occupied tops:
either these intersecting shadows line up so rigidly that the family is
rank-thin, or cross-top unions force a fork. I could not prove that coherence
theorem in this pass.

Candidate:
the Erdos536 diagnostic global lift large defect shields.

No positive-mass global lift was found. The most naive lift already collapses.
For \(m\ge6\), the local downset
\[
\mathcal T_m=\{A\subseteq C_m: |A|\le m/2-1\}
\]
contains internal forks: for distinct \(x,y\in C_m\),
\[
\{x\},\quad \{y\},\quad \{x,y\}\in\mathcal T_m,
\qquad
\{x\}\cup\{y\}=\{x,y\}.
\]
So the local large-defect shield avoids covering the top \(C_m\), but it is not
itself union-free. A global construction that simply installs these full local
shields under many tops fails before the top-covering obstruction is even
reached.

Admitted true diagnostic node:
\[
the Erdos536 naive large defect downset shield has internal forks.
\]

Other attempted lift templates remain unresolved:

Top-only or exact-rank lifts avoid forks locally, but they are rank-thin and
  vanish by the rank-block anti-concentration theorem.
Full large-defect downsets have internal forks.
Many-top shield prescriptions still face cross-top unions: a trace under one
  top and a trace under another can unite to a third occupied top unless there
  is a strong global coordination rule.

No construction achieved positive \(\nu_k\)-mass, broad rank support, and
global union-freeness simultaneously.

the Erdos536 occupied top support shadow forces coverage: candidate_open;
the Erdos536 intersecting complement obstruction dichotomy: candidate_open;
the Erdos536 diagnostic global lift large defect shields: candidate_open.

Admitted true nodes:
\[
the Erdos536 disjoint defect shadow equivalent fork,
\quad
the Erdos536 naive large defect downset shield has internal forks.
\]

No Erdos 536 theorem was solved and no source counterexample was constructed.
The frontier is now cleaner: every remaining positive-mass obstruction must be
a globally coherent family whose occupied-top defect shadows are intersecting,
objective should create exactly three candidates around this coherence problem:
one for a cross-top union forcing lemma, one for a rank-profile collapse theorem
for coherent intersecting shadows, and one diagnostic route for constructing or
blocking globally coherent intersecting-shadow systems.

_Proof source: `private proof note`._

## Tags

`diagnostic`, `erdos-536`, `internal-fork`, `large-defect-shield`, `proved`, `theorem`, `true`
