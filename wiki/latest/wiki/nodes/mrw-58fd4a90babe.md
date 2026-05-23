---
id: mrw-58fd4a90babe
type: proposition
title: Terminal separators quarantine comparable upper mixed shadows
aliases: ["mrw-58fd4a90babe", "Terminal separators quarantine comparable upper mixed shadows"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, endpoint-fiber, terminal-separator, comparable-pairs, upper-mixed-shadow, top-union-free, product-measure, terminal-residual, residual-obstruction, route-quarantine]
parents: [mrw-0c0cd605a52a, mrw-dda277c43571, mrw-740b9e5c6cff, mrw-20ca89f696f2]
refs: []
  - raw/20260523T042600Z-erdos-536-terminal-separator-obstruction.md
  - raw/20260523T042600Z-erdos536-terminal-separator-obstruction.md
  - raw/20260523T042600Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T042600Z-erdos536-terminal-separator-obstruction-request.md
  - theory/forage/responses/20260523T042600Z-erdos536-terminal-separator-obstruction-response.md
  - oracle/requests/20260523T042600Z-erdos536-terminal-separator-obstruction-oracle-request.md
  - oracle/responses/20260523T042600Z-erdos536-terminal-separator-obstruction-oracle-response.md
---

# Proposition: Terminal separators quarantine comparable upper mixed shadows

## Statement
Let \(P=B\sqcup T\), let \(f,u\subseteq B\) with
\[
f\subsetneq u,
\]
and let
\[
\mathcal A,\mathcal V\subseteq2^T.
\]
Suppose there is a terminal separator \(Z\subseteq T\) such that
\[
A\cap Z\ne\emptyset \qquad(A\in\mathcal A),
\]
and
\[
V\cap Z=\emptyset \qquad(V\in\mathcal V).
\]
If both \(\mathcal A\) and \(\mathcal V\) are terminal pair-link-free, then
the two-fiber assembly
\[
\mathcal F=
\{f\cup A:A\in\mathcal A\}
\cup
\{u\cup V:V\in\mathcal V\}
\subseteq2^P
\]
is pair-link-free.

More precisely, with
\[
\mathsf J_T(\mathcal V)
=
\bigcup_{\substack{V_1,V_2\in\mathcal V\\V_1\ne V_2}}
I_T(V_1,V_2),
\]
one has
\[
\mathcal A\cap\mathsf J_T(\mathcal V)=\emptyset.
\]
Also, for every \(A\in\mathcal A\) and \(V\in\mathcal V\),
\[
\mathcal V\cap I_T(A,V)=\emptyset.
\]
Thus the comparable upper mixed-shadow exclusion is strict: the upper child
fiber contains no terminal point in the interval, not merely no new point.

Consequently, all sectionwise top-union-free constraints imposed by lower
parents in \(\mathcal A\) on the upper fiber \(\mathcal V\) are simultaneously
satisfied by the product separator obstruction
\[
\text{lower parents hit }Z,\qquad\text{upper sets avoid }Z.
\]

If \(\nu_T\) is a terminal product law and
\[
\mathcal V^{\setminus Z}
=
\{W\subseteq T\setminus Z:W\in\mathcal V\},
\]
then for every real \(h\),
\[
\nu_T(\mathcal V\cap\{|R|>h\})
=
\left(\prod_{z\in Z}(1-q_z)\right)
\nu_{T\setminus Z}(\mathcal V^{\setminus Z}\cap\{|W|>h\}).
\]
Hence an upper fiber supported on \(T\setminus Z\) is exactly a smaller-core
terminal residual with coefficient
\[
\nu_T(R\cap Z=\emptyset)=\prod_{z\in Z}(1-q_z),
\]
and with no support cutoff shift.

In particular, for the full two-fiber assembly under the product law
\(\nu_P=\pi_B\otimes\nu_T\),
\[
\nu_P(\mathcal F\cap\{|S|>L\})
=
\pi_B(f)\nu_T(\mathcal A\cap\{|R|>L-|f|\})
\]
\[
\quad+
\pi_B(u)
\left(\prod_{z\in Z}(1-q_z)\right)
\nu_{T\setminus Z}(\mathcal V^{\setminus Z}\cap\{|W|>L-|u|\}).
\]

## Proof
First note the two forced terminal exclusions.  If \(V_1,V_2\in\mathcal V\),
then
\[
V_1\cup V_2\subseteq T\setminus Z.
\]
Therefore every terminal set in
\[
I_T(V_1,V_2)
\]
also avoids \(Z\).  Every member of \(\mathcal A\) meets \(Z\), so
\[
\mathcal A\cap I_T(V_1,V_2)=\emptyset
\]
for all \(V_1\ne V_2\), and hence
\[
\mathcal A\cap\mathsf J_T(\mathcal V)=\emptyset.
\]

Next fix \(A\in\mathcal A\) and \(V\in\mathcal V\).  Choose
\[
z\in A\cap Z.
\]
Since \(V\cap Z=\emptyset\), the coordinate \(z\) lies in
\[
A\triangle V.
\]
Thus every terminal set \(C\in I_T(A,V)\) must contain \(z\).  But every
member of \(\mathcal V\) avoids \(Z\), so
\[
\mathcal V\cap I_T(A,V)=\emptyset.
\]

We now verify pair-link-freeness of \(\mathcal F\).  By the endpoint/terminal
factorization in `mrw-20ca89f696f2`, a pair-link triple in \(\mathcal F\)
would have endpoint patterns
\[
(e_1,e_2,e_3)\in\{f,u\}^3
\]
with
\[
e_3\in I_B(e_1,e_2),
\]
and terminal patterns satisfying the corresponding terminal interval relation.

The admissible endpoint triples are exactly
\[
(f,f,f),\quad (u,u,u),\quad (u,u,f),\quad (f,u,u),\quad (u,f,u).
\]
Indeed,
\[
I_B(f,f)=2^f,
\qquad
I_B(u,u)=2^u,
\]
and
\[
I_B(f,u)=I_B(u,f)=\{g:u\setminus f\subseteq g\subseteq u\}.
\]
Thus \(u\in I_B(f,u)=I_B(u,f)\), while \(f\notin I_B(f,u)\) because
\(u\setminus f\not\subseteq f\); also \(u\notin I_B(f,f)\) because
\(u\not\subseteq f\).

The constant endpoint triples \((f,f,f)\) and \((u,u,u)\) are excluded by
terminal pair-link-freeness of \(\mathcal A\) and \(\mathcal V\), respectively.

For \((u,u,f)\), the two \(u\)-parents have terminal parts in
\(\mathcal V\), and a terminal \(f\)-child would have to lie in
\(\mathcal A\cap\mathsf J_T(\mathcal V)\), which is empty.

For \((f,u,u)\) and \((u,f,u)\), a terminal \(u\)-child would have to lie in
\[
\mathcal V\cap I_T(A,V)
\]
for some \(A\in\mathcal A\), \(V\in\mathcal V\), which is empty by the strict
upper mixed-shadow exclusion above.  These cases exhaust all admissible
endpoint triples, so no pairwise distinct ambient pair-link triple exists in
\(\mathcal F\).

It remains to prove the product-law factorization.  Under the terminal product
law,
\[
\nu_T=\nu_Z\otimes\nu_{T\setminus Z}.
\]
Since every member of \(\mathcal V\) avoids \(Z\),
\[
\mathcal V\cap\{|R|>h\}
=
\{R\cap Z=\emptyset\}
\cap
\{R\cap(T\setminus Z)\in\mathcal V^{\setminus Z},\ |R\cap(T\setminus Z)|>h\}.
\]
Independence gives
\[
\nu_T(\mathcal V\cap\{|R|>h\})
=
\prod_{z\in Z}(1-q_z)\,
\nu_{T\setminus Z}(\mathcal V^{\setminus Z}\cap\{|W|>h\}).
\]
The two-fiber mass identity follows by decomposing the two disjoint endpoint
fibers \(f\) and \(u\) and applying the same factorization to the upper fiber.

## Depends on
- `mrw-0c0cd605a52a`: individual high-support cover caps become weak, so any
  aggregate theorem must account for residual/product obstructions.
- `mrw-dda277c43571`: comparable upper mixed-shadow exclusion is sectionwise
  top-union-free.
- `mrw-740b9e5c6cff`: the nonempty star escape split whose comparable branch
  contains the upper mixed-shadow scheme.
- `mrw-20ca89f696f2`: endpoint/terminal interval factorization.

## Used by
- Future aggregate cover-cap attempts: a common terminal separator blocks
  aggregation unless the argument rules out small-cost separator products.
- Future residual classification: the upper fiber becomes a smaller-core
  terminal residual on \(T\setminus Z\), multiplied by
  \(\prod_{z\in Z}(1-q_z)\).

## Notes
- This is a residual/product obstruction, not terminal Erdos 536 evidence.
- If \(Z=\emptyset\), then the hypothesis \(A\cap Z\ne\emptyset\) forces
  \(\mathcal A=\emptyset\), and the statement reduces to terminal
  pair-link-freeness of \(\mathcal V\).
- If \(\mathcal A=\emptyset\) or \(\mathcal V=\emptyset\), the mixed-shadow
  conclusions are vacuous.
- The product-law factorization is valid for every real \(h\), including
  \(h<0\); in that boundary case the support cutoff is automatic on the
  induced core.
- Oracle accepted the proposition with the \(\mathsf J_T\) convention, induced
  \(T\setminus Z\) notation, and boundary cases made explicit.  Scout returned
  only a scaffold response and was ingested raw-only.
