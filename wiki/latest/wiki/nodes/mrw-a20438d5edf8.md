---
id: mrw-a20438d5edf8
type: proposition
title: Separator forests require branch-volume accounting
aliases: ["mrw-a20438d5edf8", "Separator forests require branch-volume accounting"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, endpoint-fiber, terminal-separator, separator-forest, separator-tree, branch-volume, product-measure, route-quarantine, residual-obstruction, leaf-entropy, rank-layer-obstruction]
parents: [mrw-ff32abc524eb, mrw-789506d08385]
refs: []
  - raw/20260523T062608Z-erdos-536-separator-forest-branch-volume.md
  - raw/20260523T062608Z-erdos536-separator-forest-branch-volume.md
  - raw/20260523T062608Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T062608Z-erdos536-separator-forest-branch-volume-request.md
  - theory/forage/responses/20260523T062608Z-erdos536-separator-forest-branch-volume-response.md
  - oracle/requests/20260523T062608Z-erdos536-separator-forest-branch-volume-oracle-request.md
  - oracle/responses/20260523T062608Z-erdos536-separator-forest-branch-volume-oracle-response.md
---

# Proposition: Separator forests require branch-volume accounting

## Statement
Let \(T\) be finite with product law \(\nu_T\) and coordinate probabilities
\[
0<q_t<1.
\]
For each leaf \(\ell\) in a finite index set \(\mathcal L\), choose a finite
separator chain
\[
T_{\ell,0}=T,\qquad
Z_{\ell,i}\subseteq T_{\ell,i-1},\qquad
T_{\ell,i}=T_{\ell,i-1}\setminus Z_{\ell,i}
\quad(1\le i\le r_\ell).
\]
Set
\[
C_\ell=\bigcup_{i=1}^{r_\ell}Z_{\ell,i}.
\]
Because the blocks are chosen successively inside the current core, they are
disjoint along the leaf, so
\[
T_{\ell,r_\ell}=T\setminus C_\ell.
\]
Define
\[
\Gamma_\ell
=
\prod_{i=1}^{r_\ell}\prod_{z\in Z_{\ell,i}}(1-q_z)
=
\prod_{z\in C_\ell}(1-q_z),
\]
and
\[
Q_\ell
=
\sum_{i=1}^{r_\ell}\sum_{z\in Z_{\ell,i}}q_z
=
\sum_{z\in C_\ell}q_z.
\]

Let \(\mathcal V_\ell\subseteq2^{T_{\ell,r_\ell}}\).  Its lifted residual
branch in \(T\) is
\[
\mathcal U_\ell
=
\{R\subseteq T:
R\cap C_\ell=\emptyset,\ R\cap T_{\ell,r_\ell}\in\mathcal V_\ell\}.
\]
For real \(h\), write
\[
H_h(S)=\{R\subseteq S:|R|>h\}.
\]
Then
\[
\nu_T(\mathcal U_\ell\cap H_h(T))
=
\Gamma_\ell\,
\nu_{T_{\ell,r_\ell}}(\mathcal V_\ell\cap H_h(T_{\ell,r_\ell})).
\]
Consequently, for
\[
\mathcal U=\bigcup_{\ell\in\mathcal L}\mathcal U_\ell,
\]
one has
\[
\nu_T(\mathcal U\cap H_h(T))
\le
\sum_{\ell\in\mathcal L}
\Gamma_\ell\,
\nu_{T_{\ell,r_\ell}}(\mathcal V_\ell\cap H_h(T_{\ell,r_\ell}))
\le
\sum_{\ell\in\mathcal L}\Gamma_\ell.
\]
If the high-window pieces
\[
\mathcal U_\ell\cap H_h(T)
\]
are disjoint, then the first inequality is an equality.  In particular,
disjointness of the full lifted branches \(\mathcal U_\ell\) is sufficient.

Since
\[
\Gamma_\ell\le e^{-Q_\ell},
\]
if every leaf has \(Q_\ell\ge L\), then
\[
\nu_T(\mathcal U\cap H_h(T))
\le
e^{-L}
\sum_{\ell\in\mathcal L}
\nu_{T_{\ell,r_\ell}}(\mathcal V_\ell\cap H_h(T_{\ell,r_\ell})).
\]
Thus the missing quantity in a branching separator contraction is the
unweighted residual leaf-volume budget
\[
B_h(\mathcal L)
=
\sum_{\ell\in\mathcal L}
\nu_{T_{\ell,r_\ell}}(\mathcal V_\ell\cap H_h(T_{\ell,r_\ell})),
\]
or, more sharply, the exact branch-volume sum
\[
\sum_{\ell\in\mathcal L}
\Gamma_\ell\,
\nu_{T_{\ell,r_\ell}}(\mathcal V_\ell\cap H_h(T_{\ell,r_\ell})).
\]

In particular, a separator-tree theorem cannot depend only on the lower bound
\(\min_\ell Q_\ell\) unless it also controls a leaf-volume, branch-entropy, or
structural substitute.

Sharpness obstruction.  Let
\[
T_n=\{1,\ldots,n\}
\]
with \(q_t=1/2\) for every \(t\).  Fix \(k\).  Let the leaves be indexed by
\(k\)-subsets \(W\subseteq T_n\).  For the leaf \(W\), take one separator
\[
Z_W=T_n\setminus W,
\qquad
T_{W,1}=W,
\qquad
\mathcal V_W=\{W\}.
\]
Then
\[
\mathcal U_W=\{W\}.
\]
The lifted branches are disjoint, and their union is the \(k\)-th rank layer.
For every \(h<k\),
\[
\nu_{T_n}\!\left(
\bigcup_{|W|=k}\mathcal U_W\cap H_h(T_n)
\right)
=
\binom nk2^{-n}.
\]
For each leaf,
\[
\Gamma_W=2^{-(n-k)},
\qquad
Q_W=\frac{n-k}{2},
\qquad
\nu_W(\mathcal V_W)=2^{-k}.
\]
Therefore the exact forest sum is
\[
\sum_{|W|=k}\Gamma_W\nu_W(\mathcal V_W)
=
\binom nk2^{-n}.
\]

Taking \(n=2m\) and \(k=m\),
\[
\binom{2m}{m}2^{-2m}\ge\frac1{2m+1},
\]
while each leaf has
\[
Q_W=\frac m2,
\qquad
\Gamma_W=2^{-m}\le e^{-m/2}.
\]
Thus the union mass is polynomially large, while every individual path has an
exponentially small coefficient and an exponentially small intensity bound.
The branch-volume sum is essential.

## Proof
For a fixed leaf \(\ell\), the event \(\mathcal U_\ell\) is exactly
\[
R\cap C_\ell=\emptyset,
\qquad
R\cap T_{\ell,r_\ell}\in\mathcal V_\ell.
\]
Since \(T_{\ell,r_\ell}=T\setminus C_\ell\), on this event
\[
R=R\cap T_{\ell,r_\ell},
\qquad
|R|=|R\cap T_{\ell,r_\ell}|.
\]
Therefore the high-window cutoff has no shift.  Product independence gives
\[
\nu_T(\mathcal U_\ell\cap H_h(T))
=
\left(\prod_{z\in C_\ell}(1-q_z)\right)
\nu_{T_{\ell,r_\ell}}(\mathcal V_\ell\cap H_h(T_{\ell,r_\ell}))
=
\Gamma_\ell
\nu_{T_{\ell,r_\ell}}(\mathcal V_\ell\cap H_h(T_{\ell,r_\ell})).
\]

Subadditivity gives
\[
\nu_T(\mathcal U\cap H_h(T))
\le
\sum_{\ell\in\mathcal L}\nu_T(\mathcal U_\ell\cap H_h(T)).
\]
If the high-window pieces are disjoint, this is equality.  The bound by
\(\sum_\ell\Gamma_\ell\) follows because the induced residual measures are at
most \(1\).

Also,
\[
\Gamma_\ell
=
\prod_{z\in C_\ell}(1-q_z)
\le
\prod_{z\in C_\ell}e^{-q_z}
=
e^{-Q_\ell}.
\]
If \(Q_\ell\ge L\) for every \(\ell\), substitute this into the branch-volume
sum to obtain the displayed \(e^{-L}\)-times-leaf-volume bound.

For the obstruction example, if \(R\in\mathcal U_W\), then
\[
R\cap(T_n\setminus W)=\emptyset
\]
and
\[
R\cap W=W.
\]
Hence \(R=W\), so \(\mathcal U_W=\{W\}\).  Distinct \(k\)-sets give disjoint
singletons, and their union is the \(k\)-th rank layer.  Under the uniform
product law, every subset of \(T_n\) has mass \(2^{-n}\), so the rank layer has
mass
\[
\binom nk2^{-n}.
\]
For each leaf \(W\),
\[
\Gamma_W
=
\prod_{z\in T_n\setminus W}\frac12
=
2^{-(n-k)},
\]
\[
Q_W
=
\sum_{z\in T_n\setminus W}\frac12
=
\frac{n-k}{2},
\]
and the all-present atom \(W\) inside the induced core \(W\) has measure
\[
\nu_W(\{W\})=2^{-k}.
\]
Thus the exact branch-volume sum is
\[
\binom nk2^{-(n-k)}2^{-k}
=
\binom nk2^{-n}.
\]

When \(n=2m\), the central binomial coefficient is maximal among the
\(2m+1\) binomial coefficients.  Since their sum is \(2^{2m}\),
\[
\binom{2m}{m}\ge\frac{2^{2m}}{2m+1},
\]
and so
\[
\binom{2m}{m}2^{-2m}\ge\frac1{2m+1}.
\]
Meanwhile
\[
\Gamma_W=2^{-m}\le e^{-m/2},
\]
because \(\log 2>1/2\).  This proves the obstruction.

## Depends on
- `mrw-ff32abc524eb`: fixed separator chains factor and telescope with no
  support cutoff shift in the avoid-all residual.
- `mrw-789506d08385`: separator coefficients obey the intensity bound
  \(\Gamma_\ell\le e^{-Q_\ell}\) pathwise.

## Used by
- Future separator-tree arguments: any branching theorem must control the
  residual leaf-volume sum, branch entropy, or a structural substitute.
- Future escape alternatives: if such a leaf-volume budget is unavailable, the
  route must use endpoint interval triples, chargeable overlap, or another
  structural constraint rather than path intensity alone.

## Notes
- This is route bookkeeping and an obstruction to a naive separator-tree
  contraction, not terminal Erdos 536 evidence.
- The rank-layer example is not claimed to be pair-link-free.  It only refutes
  separator-tree bounds that use path intensity while ignoring branch count or
  induced residual volume.
- The exact coefficient is \(\Gamma_\ell\); the estimate \(e^{-Q_\ell}\) is
  only an upper bound and may be weaker.
- If \(r_\ell=0\), then \(C_\ell=\emptyset\), \(\Gamma_\ell=1\),
  \(Q_\ell=0\), and \(\mathcal U_\ell=\mathcal V_\ell\).
- If \(\mathcal V_\ell=\emptyset\), the branch contributes zero.
- If \(h<0\), the high-window cutoff is automatic; if \(h\ge |T|\), it is
  empty.
- Oracle accepted the proposition after making \(T_{\ell,r_\ell}=T\setminus
  C_\ell\) explicit, distinguishing \(\Gamma_\ell\) from \(e^{-Q_\ell}\), and
  naming the residual leaf-volume budget.  Scout returned only a scaffold
  response and was ingested raw-only.
