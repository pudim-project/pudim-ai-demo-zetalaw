---
id: mrw-4a33f7d04fc3
type: corollary
title: Locally shielded pairs force endpoint interval-gap bounds
aliases: ["mrw-4a33f7d04fc3", "Locally shielded pairs force endpoint interval-gap bounds"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, endpoint-fiber, endpoint-interval, local-shield, nonchargeable-pairs, active-mass, interval-gap, product-measure, branch-filter, escaped-mass]
parents: [mrw-0cbd2c0086d7, mrw-45819fa8022f, mrw-20ca89f696f2]
refs: []
  - raw/20260522T190535Z-erdos-536-local-shield-upset-exclusion.md
  - raw/20260522T190535Z-erdos536-local-shield-upset-exclusion.md
  - raw/20260522T190535Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T190535Z-erdos536-local-shield-upset-exclusion-request.md
  - theory/forage/responses/20260522T190535Z-erdos536-local-shield-upset-exclusion-response.md
  - oracle/requests/20260522T190535Z-erdos536-local-shield-upset-exclusion-oracle-request.md
  - oracle/responses/20260522T190535Z-erdos536-local-shield-upset-exclusion-oracle-response.md
---

# Corollary: Locally shielded pairs force endpoint interval-gap bounds

## Statement
Let \(B\) be finite with endpoint product law
\[
\pi_B(a)=\prod_{b\in a}q_b\prod_{b\notin a}(1-q_b),
\qquad 0<q_b<1.
\]
For distinct endpoint patterns \(e,f\subseteq B\), define
\[
I_B(e,f)=\{g\subseteq B:e\triangle f\subseteq g\subseteq e\cup f\},
\]
and the shield gap
\[
S(e,f)=I_B(e,f)\setminus\{e,f\}.
\]
Then
\[
\pi_B(I_B(e,f))
=
\prod_{b\in e\triangle f}q_b
\prod_{b\notin e\cup f}(1-q_b),
\]
and
\[
\pi_B(S(e,f))
=
\pi_B(I_B(e,f))
-\mathbf 1_{f\subsetneq e}\pi_B(e)
-\mathbf 1_{e\subsetneq f}\pi_B(f).
\]

If \(\mathcal E\subseteq2^B\) satisfies the local shield
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\},
\]
then
\[
\Lambda=\pi_B(\mathcal E)\le1-\pi_B(S(e,f)).
\]
Consequently, in any active configuration with \(M\ge\eta\tau\), hence \(\Lambda\ge\eta\), every locally shielded selected pair satisfies
\[
\pi_B(S(e,f))\le1-\eta.
\]

Under the full active hypotheses of `mrw-0cbd2c0086d7`, including \(M\ge\eta\tau\) and \(P_0(B)<\delta\eta\), at least one of the following holds.

1. The chargeable overlap branch of `mrw-0cbd2c0086d7` holds.

2. There exists a distinct nonchargeable ordered pair \((e,f)\) such that
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge(1-\gamma-\delta)\eta^2,
\]
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\},
\]
and
\[
\pi_B(S(e,f))\le1-\eta.
\]

Equivalently in the restricted contrapositive form: if every distinct nonchargeable ordered pair \((e,f)\in\mathcal E^2\) satisfying
\[
\frac{\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)}{\tau}
\ge(1-\gamma-\delta)\eta^2
\]
and
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}
\]
has
\[
\pi_B(S(e,f))>1-\eta,
\]
then the distinct nonchargeable shield branch is impossible, so the chargeable overlap branch holds.

In particular, the stronger condition that every distinct endpoint pair with terminal common high-window overlap at least \((1-\gamma-\delta)\eta^2\) has \(\pi_B(S(e,f))>1-\eta\) also eliminates the nonchargeable shield branch.

## Proof
Partition \(B\) into \(e\triangle f\), \(e\cap f\), and \(B\setminus(e\cup f)\).  For \(g\in I_B(e,f)\), all coordinates in \(e\triangle f\) are forced to be present, all coordinates outside \(e\cup f\) are forced to be absent, and the coordinates in \(e\cap f\) are free.  Therefore
\[
\begin{aligned}
\pi_B(I_B(e,f))
&=
\sum_{u\subseteq e\cap f}
\prod_{b\in e\triangle f}q_b
\prod_{b\in u}q_b
\prod_{b\in(e\cap f)\setminus u}(1-q_b)
\prod_{b\notin e\cup f}(1-q_b)\\
&=
\prod_{b\in e\triangle f}q_b
\prod_{b\notin e\cup f}(1-q_b).
\end{aligned}
\]

For distinct \(e,f\),
\[
e\in I_B(e,f)\quad\Longleftrightarrow\quad f\subsetneq e,
\]
and
\[
f\in I_B(e,f)\quad\Longleftrightarrow\quad e\subsetneq f.
\]
Thus subtracting exactly the endpoint atoms that actually lie in \(I_B(e,f)\) gives the displayed formula for \(\pi_B(S(e,f))\).  If \(e,f\) are incomparable, neither endpoint lies in the interval and \(S(e,f)=I_B(e,f)\).

If
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\},
\]
then \(\mathcal E\cap S(e,f)=\varnothing\), hence
\[
\mathcal E\subseteq2^B\setminus S(e,f).
\]
Therefore
\[
\Lambda=\pi_B(\mathcal E)\le1-\pi_B(S(e,f)).
\]
If \(M\ge\eta\tau\), `mrw-45819fa8022f` gives \(\Lambda\ge\eta\), so \(\pi_B(S(e,f))\le1-\eta\).

Finally, under the active hypotheses of `mrw-0cbd2c0086d7`, the empty branch is excluded.  That node gives either the chargeable overlap branch or a distinct nonchargeable ordered pair with the stated high-window overlap and local shield.  In the latter case, the preceding interval-gap bound gives \(\pi_B(S(e,f))\le1-\eta\).  The restricted contrapositive and the stronger sufficient condition are immediate.

## Depends on
- `mrw-0cbd2c0086d7` for the active quantified chargeable-or-nonchargeable branch alternative.
- `mrw-45819fa8022f` for \(M\ge\eta\tau\Rightarrow\Lambda\ge\eta\).
- `mrw-20ca89f696f2` for the symmetric-difference endpoint interval convention.

## Used by
- Pending: branch filters that try to eliminate locally shielded nonchargeable pairs by proving lower bounds on \(\pi_B(S(e,f))\).

## Notes
- This is a branch filter, not terminal Erdos 536 evidence.  The bound \(\pi_B(S(e,f))\le1-\eta\) may be weak or vacuous.
- The exact interval formula works for all \(0<q_b<1\); no \(q_b\le1/2\) hypothesis is used.
- The ordered nature of the nonchargeable branch is harmless because \(I_B(e,f)=I_B(f,e)\) and \(S(e,f)=S(f,e)\).
- Oracle accepted the result after replacing the unrestricted "equivalently" clause with a restricted contrapositive plus a stronger sufficient condition.
- Scout returned only a scaffold response and was ingested raw-only.
