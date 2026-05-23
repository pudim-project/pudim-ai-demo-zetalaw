---
id: mrw-5df7f8135e2c
type: corollary
title: Strict-deletion residuals iterate to terminal or second-overfull alternatives
aliases: ["mrw-5df7f8135e2c", "Strict-deletion residuals iterate to terminal or second-overfull alternatives"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, iterated-tower, overfull-incidence, strict-deletion, retowering, terminal-residual, residual-iteration, second-overfull, support-tail, cross-core-coherence]
parents: [mrw-3dde1053699f, mrw-c82229c73d8d, mrw-59f327fd233e]
refs: []
  - raw/20260521T152927Z-erdos-536-strict-deletion-residuals-iterate-to-terminal-or-s.md
  - raw/20260521T152712Z-erdos536-strict-deletion-residual-iteration.md
  - theory/forage/requests/20260521T152712Z-erdos536-strict-deletion-residual-iteration-request.md
  - theory/forage/responses/20260521T152712Z-erdos536-strict-deletion-residual-iteration-response.md
  - oracle/requests/20260521T152927Z-erdos536-strict-deletion-iteration-oracle-request.md
  - oracle/responses/20260521T152927Z-erdos536-strict-deletion-iteration-oracle-response.md
---

# Corollary: Strict-deletion residuals iterate to terminal or second-overfull alternatives

## Statement

Use the endpoint-tower notation
\[
P=P_0\supseteq P_1\supseteq\cdots\supseteq P_r,
\qquad
P_{j-1}=P_j\sqcup X_j\sqcup Y_j,
\]
and the same-class endpoint-pair set
\[
\mathcal E_{\mathrm{ov}}
=
\bigcup_{j=1}^r
\left(\binom{X_j}{2}\cup\binom{Y_j}{2}\right)
\]
of [[mrw-c82229c73d8d]].  For \(e=\{p,q\}\in\mathcal E_{\mathrm{ov}}\), put
\(q_e=q_pq_q\), and let
\[
P_e=P\setminus e.
\]
Let the induced endpoint tower on \(P_e\) be the tower constructed in
[[mrw-3dde1053699f]], with length \(\ell_e\), terminal core \(T_e\), exact
endpoint probability \(\Gamma_e\), and endpoint-defect residual
\(\mathcal R_{\mathrm{def}}^e\).  If \(\ell_e\ge1\), let
\(\pi_{\mathrm{ov}}^e\) be the product-measure probability, in the induced
tower on \(P_e\), that at least one retained endpoint class contains two or
more selected coordinates.  If \(\ell_e=0\), set
\[
\pi_{\mathrm{ov}}^e=0,\qquad \beta_e=0;
\]
and use the length-zero convention \(T_e=P_e\) and \(\Gamma_e=1\).  Otherwise
set \(\beta_e=1\).

Then, for every real threshold \(U\),
\[
\mathfrak M_{P_e}(U)
\le
\left(\Gamma_e+\beta_e\right)
\mathfrak M_{T_e}(U-2\ell_e)
+
\pi_{\mathrm{ov}}^e .
\]
Consequently, for every pair-link-free family \(\mathcal F\subseteq2^P\) and
every real threshold \(L\),
\[
\nu_P(\mathcal F\cap H_L)
\le
\mathfrak M_{P_r}(L-2r)
+
\sum_{e\in\mathcal E_{\mathrm{ov}}}
q_e
\left[
\left(\Gamma_e+\beta_e\right)
\mathfrak M_{T_e}(L-2-2\ell_e)
+
\pi_{\mathrm{ov}}^e
\right],
\]
where \(H_L=\{S\subseteq P:|S|>L\}\).

More explicitly, split \(\mathcal E_{\mathrm{ov}}\) into surviving and
collapsed deletions.  If \(e\subseteq C_j\in\{X_j,Y_j\}\) and
\(C_j\setminus e\ne\varnothing\), then
\[
\ell_e=r,\qquad T_e=P_r,
\]
so the \(e\)-summand is
\[
q_e\left[
\left(\Gamma_e+1\right)\mathfrak M_{P_r}(L-2-2r)
+
\pi_{\mathrm{ov}}^e
\right].
\]
If \(C_j=e\) and \(r>1\), then
\[
\ell_e=r-1,\qquad T_e=P_r\cup D_j,
\]
where \(D_j\) is the opposite endpoint class at level \(j\), and the
\(e\)-summand is
\[
q_e\left[
\left(\Gamma_e+1\right)\mathfrak M_{P_r\cup D_j}(L-2r)
+
\pi_{\mathrm{ov}}^e
\right].
\]
If \(C_j=e\) and \(r=j=1\), the induced tower has length zero and the
corresponding residual is already terminal:
\[
\mathfrak M_{P_e}(L-2)
=
\mathfrak M_{T_e}(L-2).
\]

For \(\ell_e\ge1\), the second-overfull probability satisfies the induced
pair-union bound
\[
\pi_{\mathrm{ov}}^e
\le
\sum_{C\in\mathcal C_e}
\sum_{\{a,b\}\subseteq C}q_aq_b
\le
\frac12\sum_{C\in\mathcal C_e}Q(C)^2,
\qquad
Q(C)=\sum_{a\in C}q_a,
\]
where \(\mathcal C_e\) is the set of retained endpoint classes in the induced
tower on \(P_e\).

## Proof

Fix \(e\in\mathcal E_{\mathrm{ov}}\).  If \(\ell_e=0\), then by
[[mrw-3dde1053699f]] the induced terminal core is \(T_e=P_e\), with
\(\Gamma_e=1\) and \(\mathcal R_{\mathrm{def}}^e=0\).  Hence
\[
\mathfrak M_{P_e}(U)=\mathfrak M_{T_e}(U),
\]
which is the stated inequality with \(\beta_e=\pi_{\mathrm{ov}}^e=0\).

Assume now that \(\ell_e\ge1\).  Applying [[mrw-3dde1053699f]] gives
\[
\mathfrak M_{P_e}(U)
\le
\Gamma_e\mathfrak M_{T_e}(U-2\ell_e)
+
\mathcal R_{\mathrm{def}}^e(U).
\]
Apply [[mrw-59f327fd233e]] to the induced tower on \(P_e\).  Its
endpoint-defect residual obeys
\[
\mathcal R_{\mathrm{def}}^e(U)
\le
\mathfrak M_{T_e}(U-2\ell_e)+\pi_{\mathrm{ov}}^e .
\]
Combining the two displayed inequalities proves
\[
\mathfrak M_{P_e}(U)
\le
(\Gamma_e+1)\mathfrak M_{T_e}(U-2\ell_e)+\pi_{\mathrm{ov}}^e,
\]
which is the asserted bound because \(\beta_e=1\) in the nondegenerate case.

Substituting \(U=L-2\), multiplying by \(q_e\), and summing over
\(\mathcal E_{\mathrm{ov}}\), then using [[mrw-c82229c73d8d]], gives the
global high-support estimate for \(\nu_P(\mathcal F\cap H_L)\).

The surviving/collapsed split is exactly the split from
[[mrw-3dde1053699f]].  In the surviving case the induced tower keeps length
\(r\) and terminal core \(P_r\).  In the collapsed case with \(r>1\), the
induced tower skips level \(j\), has length \(r-1\), and has terminal core
\(P_r\cup D_j\).  The boundary case \(r=j=1\) is the length-zero convention
already handled above.

It remains only to record the displayed estimate for
\(\pi_{\mathrm{ov}}^e\).  In any endpoint class \(C\) of the induced tower,
the event \(|S\cap C|\ge2\) is contained in the union of the events
\(\{a,b\}\subseteq S\) over unordered pairs \(\{a,b\}\subseteq C\).  The
product law gives probability \(q_aq_b\) to each such pair event, so the union
bound yields
\[
\Pr(|S\cap C|\ge2)
\le
\sum_{\{a,b\}\subseteq C}q_aq_b.
\]
Summing over the retained induced endpoint classes gives the first bound, and
\[
\sum_{\{a,b\}\subseteq C}q_aq_b
\le
\frac12\left(\sum_{a\in C}q_a\right)^2
\]
gives the second.

## Depends on

- [[mrw-3dde1053699f]]
- [[mrw-c82229c73d8d]]
- [[mrw-59f327fd233e]]

## Used by

## Notes

- This corollary is the promised one-step residual iteration after
  [[mrw-3dde1053699f]].  It converts the weighted strict-deletion residual sum
  into induced terminal residuals plus second-generation overfull endpoint
  probabilities.
- The result is still nonterminal.  It does not prove that the induced
  terminal residuals vanish and does not prove an \(R_P(\theta)\) lift.  Its
  value is that the remaining obstruction is now explicit: surviving
  deletions return to \(P_r\), while collapsed deletions create enlarged
  terminal cores \(P_r\cup D_j\).
- In the collapsed case \(D_j\) is no longer an endpoint class of the induced
  tower; it is part of the terminal core.  Thus \(\pi_{\mathrm{ov}}^e\) counts
  only overfull events in retained endpoint classes, not pairs inside \(D_j\).
- Focused Oracle passed the proof and requested only that the length-zero
  convention \(T_e=P_e,\Gamma_e=1\) be explicit in the statement; this is now
  patched.
