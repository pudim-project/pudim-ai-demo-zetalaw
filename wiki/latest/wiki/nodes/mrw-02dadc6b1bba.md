---
id: mrw-02dadc6b1bba
type: proposition
title: Rank-only lower-shadow-free families have vanishing biased mass
aliases: ["mrw-02dadc6b1bba", "Rank-only lower-shadow-free families have vanishing biased mass"]
status: proved
tags: ["proposition", "proved", "erdos", "lcm", "squarefree", "biased-measure", "lower-shadow", "union-cover", "rank-only", "support-tail", "patch-gate-audited"]
parents: [mrw-d0402aea6f58, mrw-cc4f876149b7, mrw-37dbc6aeedf9, mrw-4daa694d9526]
refs: []
---

# Proposition: Rank-only lower-shadow-free families have vanishing biased mass

## Statement

Let \(P\) be a finite set of primes and let \(\nu_P\) be the product probability measure on \(2^P\) with
\[
\nu_P(p\in S)=\frac1p.
\]
Put
\[
S_P=\sum_{p\in P}\frac1p
\]
and, for \(0\le\theta<1\),
\[
H_{P,\theta}=\{S\subseteq P:\ |S|>\theta S_P\}.
\]

For \(T\subseteq\{0,\ldots,|P|\}\), define the rank-only family
\[
\mathcal R_T(P)=\{S\subseteq P:\ |S|\in T\}.
\]
Then \(\mathcal R_T(P)\) is lower-shadow union-cover-free if and only if there are no \(a,b,c\in T\) such that
\[
a<c,\qquad b<c,\qquad a+b\ge c.
\]
In particular, if \(0<t_1<t_2<\cdots\) are the positive ranks in \(T\), then lower-shadow union-cover-freeness implies
\[
t_{i+1}>2t_i
\]
for every \(i\).

Consequently, for any sequence of finite prime sets \(P_j\) with \(S_{P_j}\to\infty\), if \(T_j\subseteq\{0,\ldots,|P_j|\}\) and \(\mathcal R_{T_j}(P_j)\) is lower-shadow union-cover-free, then
\[
\nu_{P_j}\bigl(\mathcal R_{T_j}(P_j)\cap H_{P_j,\theta}\bigr)\to0
\]
for every fixed \(0\le\theta<1\).

## Proof

Fix \(P\) and \(T\).  Suppose first that there are \(a,b,c\in T\) with \(a<c\), \(b<c\), and \(a+b\ge c\).  Choose a set \(C\subseteq P\) of size \(c\).  Choose \(A\subseteq C\) with \(|A|=a\).  Since \(a+b\ge c\), we have \(c-a\le b\).  Choose \(B\subseteq C\) of size \(b\) containing \(C\setminus A\); this is possible because \(b\le c\).  Then
\[
A,B\subsetneq C,\qquad A\ne B,\qquad A\cup B=C,
\]
and \(A,B,C\in\mathcal R_T(P)\).  Thus \(\mathcal R_T(P)\) is not lower-shadow union-cover-free.

Conversely, any lower-shadow union-cover triple \(A,B,C\in\mathcal R_T(P)\) gives ranks
\[
a=|A|,\qquad b=|B|,\qquad c=|C|
\]
with \(a,b,c\in T\), \(a<c\), \(b<c\), and
\[
c=|A\cup B|\le |A|+|B|=a+b.
\]
This proves the rank criterion.  Taking \(a=b=t_i\) and \(c=t_{i+1}\) gives the displayed lacunarity condition.

It remains to prove the biased mass consequence.  Let
\[
X_P=|S|,\qquad S\sim\nu_P.
\]
Write \(q_p=1/p\) and
\[
V_P=\operatorname{Var}(X_P)=\sum_{p\in P}q_p(1-q_p).
\]
Since \(q_p\le1/2\), we have \(V_P\ge S_P/2\), so \(V_{P_j}\to\infty\).

We use a standard Fourier anti-concentration estimate, included for completeness.  If \(\phi_P(t)=\mathbb E e^{itX_P}\), then
\[
|\phi_P(t)|
\le
\exp\{-V_P(1-\cos t)\}
\le
\exp\{-2V_Pt^2/\pi^2\}
\]
for \(|t|\le\pi\).  Fourier inversion gives an absolute constant \(C\) such that
\[
\sup_m \nu_P(X_P=m)
\le
\frac1{2\pi}\int_{-\pi}^{\pi}|\phi_P(t)|\,dt
\le
\frac{C}{\sqrt{V_P}}.
\]

Now fix \(K>1\).  By the rank lacunarity, the number of positive ranks in \(T_j\) lying in
\[
[1,KS_{P_j}]
\]
is \(O(\log(KS_{P_j}))\).  Therefore
\[
\nu_{P_j}\bigl(X_{P_j}\in T_j,\ 1\le X_{P_j}\le KS_{P_j}\bigr)
\le
O(\log(KS_{P_j}))\frac{C}{\sqrt{V_{P_j}}}
\to0.
\]
Finally, Markov's inequality gives
\[
\nu_{P_j}(X_{P_j}>KS_{P_j})\le \frac1K.
\]
Combining these two estimates,
\[
\limsup_{j\to\infty}
\nu_{P_j}\bigl(\mathcal R_{T_j}(P_j)\cap H_{P_j,\theta}\bigr)
\le
\frac1K.
\]
Letting \(K\to\infty\) proves the claimed convergence to \(0\).

## Depends on

- [[wiki/nodes/mrw-d0402aea6f58|Biased lower-shadow union-cover problem for Erdos 536]]
- [[wiki/nodes/mrw-cc4f876149b7|Intersecting deletion-trace obstruction for lower-shadow union covers]]
- [[wiki/nodes/mrw-37dbc6aeedf9|Biased squarefree residual problem for Erdos 536]]
- [[wiki/nodes/mrw-4daa694d9526|Low-support growing-prime criterion for Erdos 536]]

## Used by

- Rules out rank-only positive-mass counterexamples to the biased lower-shadow union-cover route.

## Notes

- This proposition does not prove the full biased lower-shadow union-cover theorem, because an arbitrary family of supports may choose only part of each rank layer.
- The proof is local and does not import any external EKR or union-free theorem.  The source note records the surrounding vocabulary only.
- The anti-concentration estimate is intentionally crude; its only role is that every single rank has \(o(1)\) biased mass when \(S_P\to\infty\).
