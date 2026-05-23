---
id: mrw-9afb17b1b84a
type: note
title: Binary-choice squarefree obstruction to pointwise support envelopes
aliases: ["mrw-9afb17b1b84a", "Binary-choice squarefree obstruction to pointwise support envelopes"]
status: proved
tags: ["note", "proved", "erdos", "lcm", "squarefree", "support-tail", "obstruction", "finite-prime", "patch-gate-audited"]
parents: [mrw-277fbbb4ccb9, mrw-e80e409bf536, mrw-f835f9671070, mrw-4daa694d9526]
refs: []
---

# Note: Binary-choice squarefree obstruction to pointwise support envelopes

## Statement

Let \(P_m=\{p_1,\ldots,p_{2m}\}\) be the first \(2m\) primes, grouped into pairs
\[
\{p_1,p_2\},\{p_3,p_4\},\ldots,\{p_{2m-1},p_{2m}\}.
\]
In the squarefree cube \(\{0,1\}^{P_m}\), define the binary-choice family
\[
\mathcal B_m
=
\left\{
\alpha\in\{0,1\}^{P_m}:
\alpha_{p_{2i-1}}+\alpha_{p_{2i}}=1
\text{ for }1\le i\le m
\right\}.
\]
Then \(|\mathcal B_m|=2^m\), every \(\alpha\in\mathcal B_m\) has support size \(m\), and \(\mathcal B_m\) contains no grid-bad triple.

Consequently, for fixed \(0\le\theta<1\), high support alone cannot imply a pointwise envelope
\[
g_{P_m}(t)\le L_{P_m,\theta}(t)
\]
or any comparable cardinality-only support bound.  More precisely, if
\[
T_m=\prod_{i=1}^{m}p_{2i},
\]
then
\[
g_{P_m}(T_m)\ge 2^m
\]
while
\[
L_{P_m,\theta}(T_m)
\le
\sum_{r\le \lfloor\theta S_{P_m}\rfloor}\binom{2m}{r}
=\exp(O_\theta((\log m)^2))
=o(2^m).
\]
Thus
\[
g_{P_m}(T_m)-L_{P_m,\theta}(T_m)>0
\]
for all sufficiently large \(m\), with exponentially large pointwise excess.

However, this is not a genuine obstruction to the residual condition \(R_P(\theta)\to0\).  The harmonic mass of the binary-choice family satisfies
\[
\mu_{P_m}(\mathcal B_m)
=
\delta_{P_m}
\prod_{i=1}^m
\left(\frac1{p_{2i-1}}+\frac1{p_{2i}}\right)
\le
\frac1{m!}
\to0.
\]
Therefore the construction blocks support-only pointwise arguments, but it does not by itself prove that \(R_{P_m}(\theta)\) stays bounded away from zero.

More generally, if \(P\) is partitioned into \(r\) nonempty blocks \(B_1,\ldots,B_r\), then the squarefree block-transversal family
\[
\mathcal T(B_1,\ldots,B_r)
=
\{S\subseteq P:\ |S\cap B_j|=1\text{ for every }j\}
\]
is grid-bad-free, every member has support \(r\), and its harmonic support mass is at most \(e^{-r}\).

## Proof

The cardinality and support assertions are immediate from the definition: each of the \(m\) prime pairs contributes exactly one binary choice, so there are \(2^m\) vectors and every vector has exactly one nonzero coordinate in each pair.

We next prove that \(\mathcal B_m\) is grid-bad-free.  Let \(\alpha,\beta,\gamma\in\mathcal B_m\) be distinct.  Since they are not all equal, there is an index \(i\) for which their choices inside the pair \(\{p_{2i-1},p_{2i}\}\) are not all the same.  Among three binary choices in a two-element pair, one of the two primes is chosen by exactly one of \(\alpha,\beta,\gamma\).  In that coordinate, the coordinatewise maximum is \(1\), and it is attained uniquely.  By the valuation criterion and squarefree cosunflower criterion, a grid-bad triple requires every coordinate maximum to be attained at least twice.  Hence \(\alpha,\beta,\gamma\) is not grid-bad.

Every vector in \(\mathcal B_m\) lies in \(\Gamma_{P_m}(T_m)\), because in the \(i\)-th pair the selected prime is at most \(p_{2i}\).  Since \(\mathcal B_m\) is grid-bad-free,
\[
g_{P_m}(T_m)\ge |\mathcal B_m|=2^m.
\]
On the other hand,
\[
S_{P_m}=\sum_{j=1}^{2m}\frac1{p_j}
\le
\sum_{j=1}^{2m}\frac1j
\le
1+\log(2m).
\]
Hence \(K_m=\lfloor\theta S_{P_m}\rfloor=O_\theta(\log m)\).  The low-support count at \(T_m\) is bounded by the total number of squarefree supports of size at most \(K_m\), so
\[
L_{P_m,\theta}(T_m)
\le
\sum_{r=0}^{K_m}\binom{2m}{r}.
\]
For \(m\) large enough that \(1\le K_m\le m\), the standard binomial estimate gives
\[
\sum_{r=0}^{K_m}\binom{2m}{r}
\le
(K_m+1)\left(\frac{2em}{K_m}\right)^{K_m}
=
\exp(O_\theta((\log m)^2)).
\]
Since \((\log m)^2=o(m)\), this is \(o(2^m)\).  Thus the pointwise excess over the low-support envelope is eventually positive and exponentially large.

Finally, compute the harmonic exponent-measure mass of \(\mathcal B_m\).  Using the measure from [[wiki/nodes/mrw-4daa694d9526|Low-support growing-prime criterion for Erdos 536]],
\[
\mu_{P_m}(\mathcal B_m)
=
\delta_{P_m}
\prod_{i=1}^m
\left(\frac1{p_{2i-1}}+\frac1{p_{2i}}\right).
\]
Since \(\delta_{P_m}\le1\), \(p_{2i}\ge p_{2i-1}\), and \(p_{2i-1}\ge 2i\),
\[
\mu_{P_m}(\mathcal B_m)
\le
\prod_{i=1}^m \frac{2}{p_{2i-1}}
\le
\prod_{i=1}^m \frac1i
=
\frac1{m!}.
\]
This tends to zero.  Thus the construction's own weighted contribution is negligible, even though its pointwise cardinality spike is huge.  The squarefree diagnostic therefore identifies the exact failed transfer: high support and large pointwise rank do not imply nonvanishing \(R_P(\theta)\).  A future proof or obstruction for \(R_P(\theta)\) must use the harmonic weighted prefix integral, not only support cardinality.

The same argument applies to arbitrary block transversals.  If three distinct transversals are chosen, then in some block their choices are not all identical, and a coordinate chosen by exactly one of the three transversals gives a unique maximum.  Hence the family is grid-bad-free.  Its harmonic mass factors by blocks:
\[
\mu_P(\mathcal T(B_1,\ldots,B_r))
=
\prod_{j=1}^{r}
\left[
\prod_{p\in B_j}\left(1-\frac1p\right)
\sum_{p\in B_j}\frac1p
\right].
\]
Writing \(s_j=\sum_{p\in B_j}1/p\), the \(j\)-th factor is at most
\[
s_j\exp(-s_j)\le e^{-1}.
\]
Therefore
\[
\mu_P(\mathcal T(B_1,\ldots,B_r))\le e^{-r}.
\]
This quarantines the most obvious block-transversal high-support spikes as harmless for the weighted residual metric.

## Depends on

- [[wiki/nodes/mrw-277fbbb4ccb9|Erdos equal pairwise least-common-multiple problem]]
- [[wiki/nodes/mrw-e80e409bf536|Squarefree cosunflower criterion for equal pairwise lcm triples]]
- [[wiki/nodes/mrw-f835f9671070|Finite-prime weighted-grid reduction for Erdos 536]]
- [[wiki/nodes/mrw-4daa694d9526|Low-support growing-prime criterion for Erdos 536]]

## Used by

- Next #536 route: biased-measure or container/junta control of the high-support residual \(R_P(\theta)\).

## Notes

- This note is a route obstruction, not a solution or refutation of Erdos #536.
- It does not prove \(R_{P_m}(\theta)\not\to0\).  The promoted conclusion is narrower: pointwise support-only envelopes are false, and the remaining target must be measure-sensitive.
- The construction is the squarefree analogue of a block-transversal family: one choice from each pair.
- The block-transversal mass bound shows that exact-one-per-block pseudo-sunflower-type obstructions decay exponentially in support under the harmonic product measure.
