---
id: mrw-d83f21b84e5c
type: corollary
title: Endpoint-weighted separator forests force endpoint residual or overlap escape
aliases: ["mrw-d83f21b84e5c", "Endpoint-weighted separator forests force endpoint residual or overlap escape"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, endpoint-fiber, terminal-separator, separator-forest, endpoint-weighted, branch-volume, endpoint-residual, pointwise-multiplicity, active-mass, overlap-escape, chargeable-pairs, nonchargeable-pairs, route-quarantine]
parents: [mrw-a20438d5edf8, mrw-baa182012831, mrw-0cbd2c0086d7, mrw-20ca89f696f2]
refs: []
  - raw/20260523T070609Z-erdos-536-endpoint-weighted-separator-forest-escape.md
  - raw/20260523T070609Z-erdos536-endpoint-weighted-separator-forest-escape.md
  - raw/20260523T070609Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T070609Z-erdos536-endpoint-weighted-separator-forest-escape-request.md
  - theory/forage/responses/20260523T070609Z-erdos536-endpoint-weighted-separator-forest-escape-response.md
  - oracle/requests/20260523T070609Z-erdos536-endpoint-weighted-separator-forest-escape-oracle-request.md
  - oracle/responses/20260523T070609Z-erdos536-endpoint-weighted-separator-forest-escape-oracle-response.md
---

# Corollary: Endpoint-weighted separator forests force endpoint residual or overlap escape

## Statement
Let \(P=B\sqcup T\) be finite with product law
\[
\nu_P=\pi_B\otimes\nu_T,
\]
where
\[
0<q_b\le\frac12\quad(b\in B),
\qquad
0<q_t<1\quad(t\in T).
\]
Let \(\mathcal E\subseteq2^B\).  For each \(e\in\mathcal E\), let
\[
C_e\subseteq T,
\qquad
\mathcal V_e\subseteq2^{T\setminus C_e},
\]
and define the lifted terminal leaf fiber
\[
\mathcal U_e
=
\{R\subseteq T:
R\cap C_e=\emptyset,\ R\cap(T\setminus C_e)\in\mathcal V_e\}.
\]
Equivalently, \(C_e\) may be the removed-coordinate union along a finite
separator chain ending at \(T\setminus C_e\).

Let
\[
\mathcal F
=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal U_e\}
\subseteq2^P.
\]
For a real \(h\), set
\[
H=H_h(T)=\{R\subseteq T:|R|>h\},
\qquad
\tau=\nu_T(H),
\]
and
\[
M_H=\sum_{e\in\mathcal E}\pi_B(e)\nu_T(\mathcal U_e\cap H).
\]

For each \(e\), write
\[
\Gamma_e=\prod_{z\in C_e}(1-q_z).
\]
Then the endpoint-weighted separator-forest branch-volume identity is
\[
M_H
=
\sum_{e\in\mathcal E}
\pi_B(e)\Gamma_e
\nu_{T\setminus C_e}(\mathcal V_e\cap H_h(T\setminus C_e)).
\]

For each \(R\subseteq T\), define the endpoint multiplicity fiber
\[
\mathcal E_R=\{e\in\mathcal E:R\in\mathcal U_e\}.
\]
Then
\[
M_H
=
\sum_{R\in H}\nu_T(R)\pi_B(\mathcal E_R).
\]
If \(\mathcal F\) is pair-link-free, then every \(\mathcal E_R\) is ordinary
endpoint pair-link-free.  Consequently, if
\[
\tau>0
\qquad\text{and}\qquad
M_H\ge\eta\tau
\quad(\eta>0),
\]
then there is some \(R\in H\) such that
\[
\pi_B(\mathcal E_R)\ge\eta,
\]
and this \(\mathcal E_R\) is ordinary endpoint pair-link-free.  Conversely, if
every \(R\in H\) has
\[
\pi_B(\mathcal E_R)<\eta,
\]
then
\[
M_H<\eta\tau.
\]

Now assume, in addition, that the overlap-accounting and diagonal-quarantine
hypotheses of `mrw-0845a9abe5b6` hold for the endpoint fibers
\[
\mathcal R_e=\mathcal U_e
\]
and the terminal window \(H\).  Fix
\[
0<\eta\le1,\qquad 0<\gamma<1,\qquad 0<\delta<1-\gamma.
\]
If
\[
\tau>0,\qquad
M_H\ge\eta\tau,
\qquad
P_0(B)=\prod_{b\in B}(1-q_b)<\delta\eta,
\]
then the empty-atom branch is impossible, and at least one of the following
overlap alternatives holds.

1. Chargeable overlap:
   there are distinct \(e,f,g\in\mathcal E\), with
   \[
   g\in I_B(e,f),
   \]
   such that
   \[
   \frac{\nu_T(\mathcal U_e\cap\mathcal U_f\cap H)}{\tau}
   \ge
   \gamma\eta^2.
   \]
   Since \(T\) is finite, \(\nu_T\) is a product law,
   \(H=H_h(T)\), and \(\mathcal F\) is pair-link-free, the witness \(g\) can
   be chosen so that
   \[
   \nu_T(\mathcal U_g)\le1-\gamma\eta^2.
   \]

2. Distinct nonchargeable shield:
   there is a distinct nonchargeable ordered pair \((e,f)\) such that
   \[
   \frac{\nu_T(\mathcal U_e\cap\mathcal U_f\cap H)}{\tau}
   \ge
   (1-\gamma-\delta)\eta^2
   \]
   and
   \[
   \mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
   \]

Thus active endpoint-weighted separator-forest mass always gives a large
pointwise ordinary endpoint residual certificate; under the existing active
overlap package and empty-atom exclusion, the same mass also escapes into the
\(\eta^2\)-scale chargeable or nonchargeable overlap alternatives.

## Proof
For fixed \(e\), the event \(\mathcal U_e\) is
\[
R\cap C_e=\emptyset,
\qquad
R\cap(T\setminus C_e)\in\mathcal V_e.
\]
On this event, \(R\subseteq T\setminus C_e\), so
\[
R\in H_h(T)
\quad\Longleftrightarrow\quad
R\cap(T\setminus C_e)\in H_h(T\setminus C_e).
\]
Product independence gives
\[
\nu_T(\mathcal U_e\cap H)
=
\Gamma_e
\nu_{T\setminus C_e}(\mathcal V_e\cap H_h(T\setminus C_e)).
\]
Multiplying by \(\pi_B(e)\) and summing over \(e\) proves the
endpoint-weighted branch-volume identity.

Since \(T\) is finite,
\[
M_H
=
\sum_{e\in\mathcal E}\pi_B(e)
\sum_{R\in H\cap\mathcal U_e}\nu_T(R)
=
\sum_{R\in H}\nu_T(R)
\sum_{e:R\in\mathcal U_e}\pi_B(e)
=
\sum_{R\in H}\nu_T(R)\pi_B(\mathcal E_R).
\]

Assume \(\mathcal F\) is pair-link-free.  Fix \(R\subseteq T\).  If
\(\mathcal E_R\) were not ordinary endpoint pair-link-free, then there would
be pairwise distinct \(e_1,e_2,e_3\in\mathcal E_R\) such that
\[
e_3\in I_B(e_1,e_2).
\]
Since \(R\in\mathcal U_{e_i}\) for every \(i\), the ambient sets
\[
S_i=e_i\cup R
\]
all lie in \(\mathcal F\).  They are pairwise distinct because their endpoint
parts are pairwise distinct.  Also
\[
R\in I_T(R,R).
\]
By endpoint-terminal interval factorization from `mrw-20ca89f696f2`,
\[
S_3\in I_P(S_1,S_2),
\]
contradicting pair-link-freeness.  Hence \(\mathcal E_R\) is ordinary endpoint
pair-link-free.

If \(\tau>0\) and \(M_H\ge\eta\tau\), then the finite weighted average
\[
\frac{M_H}{\tau}
=
\frac{1}{\tau}\sum_{R\in H}\nu_T(R)\pi_B(\mathcal E_R)
\]
is at least \(\eta\).  Therefore some \(R\in H\) has
\[
\pi_B(\mathcal E_R)\ge\eta.
\]
If every \(R\in H\) had \(\pi_B(\mathcal E_R)<\eta\), finiteness of \(H\)
would give \(M_H<\eta\tau\).

For the active escape, apply `mrw-0cbd2c0086d7` with
\[
\mathcal R_e=\mathcal U_e,
\qquad
M=M_H,
\qquad
H=H_h(T).
\]
Its hypotheses include the overlap-accounting and diagonal-quarantine
assumptions inherited here.  The inequalities
\[
\tau>0,\qquad M_H\ge\eta\tau,\qquad P_0(B)<\delta\eta
\]
exclude the empty-atom branch and yield either the chargeable overlap
alternative or the distinct nonchargeable shield alternative.  The strong
third-fiber conclusion in the chargeable branch is exactly the product
high-window, pair-link-free conclusion of `mrw-0cbd2c0086d7`, again with
\(\mathcal R_g=\mathcal U_g\).

## Depends on
- `mrw-a20438d5edf8`: terminal separator forest branches factor with
  coefficient \(\Gamma_e\); path intensity alone does not control branch
  unions.
- `mrw-baa182012831`: the pointwise endpoint residual viewpoint; the proof
  repeats its diagonal terminal argument for the lifted separator fibers.
- `mrw-0cbd2c0086d7`: active high-window mass, after empty-atom exclusion,
  forces chargeable overlap or a distinct nonchargeable shield.
- `mrw-20ca89f696f2`: endpoint-terminal interval factorization.

## Used by
- Future leaf-volume control: endpoint-weighted separator mass is exactly a
  terminal average of ordinary endpoint residual multiplicities.
- Future escape theorems: if the endpoint residual multiplicity branch is not
  acceptable, active mass has already been converted to the known
  \(\eta^2\)-scale overlap alternatives.

## Notes
- This is routing and branch accounting, not terminal Erdos 536 evidence.
- The pointwise endpoint residual certificate is not exclusive with the
  overlap alternatives.  Under active mass it always exists; under the
  additional active-overlap hypotheses, one also obtains a chargeable or
  nonchargeable overlap alternative.
- If \(\tau=0\) or \(H=\emptyset\), the identities remain true, but no divided
  active conclusion is asserted.
- If \(h<0\), then \(H=2^T\).  If \(h\ge |T|\), then \(H=\emptyset\).
- If \(C_e=\emptyset\), then \(\Gamma_e=1\) and
  \(\mathcal U_e=\mathcal V_e\).  If \(\mathcal V_e=\emptyset\), the branch
  contributes zero.
- If \(\mathcal E=\emptyset\), then \(M_H=0\), so the active hypothesis is
  impossible when \(\tau>0\) and \(\eta>0\).
- Oracle accepted the corollary after making \(\tau>0\) explicit in active
  claims, allowing \(C_e\subseteq T\) to stand for the final removed set, and
  rephrasing the final summary to avoid an exclusive dichotomy.  Scout
  returned only a scaffold response and was ingested raw-only.
