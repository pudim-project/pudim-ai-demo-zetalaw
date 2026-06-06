# Frontier: Karp--Prilepkina Balanced Hypergeometric Stieltjes Measures

Scout forage `FI-20260528T-next-loop-011` selected Karp--Prilepkina's balanced generalized Stieltjes representing-measure problem for
\[
{}_{q+1}F_q(\sigma,A;B;-z)
=\int_{[0,1]}\frac{d\rho(t)}{(1+tz)^\sigma}.
\]

The source treats the case
\[
\Delta=\sum_{k=1}^q(b_k-a_k)>0
\]
and remarks that the balanced case \(\Delta=0\) leaves the representing measure open in general. It records the \(q=1\) Dirac mass \(\delta_1\) and gives a balanced \(q=2\) limiting formula with an atom at \(t=1\) plus a continuous hypergeometric density.

This branch is not a zeta-tail parameter increment and is not a continuation of the recent YHL, GGPS, Bulboaca--Zayed, Baricz, or Yang--Tian branches. It grows the local Theory toward generalized Stieltjes transforms, positive measure representations, and complete monotonicity through hypergeometric kernels.

The bounded Student target is only to prove the \(q=1\) Dirac representation, record the source's \(q=2\) bridge formula, and leave the general \(q\) problem open.

## Student/Librarian outcome `20260528T143000Z`

Student proved the balanced \(q=1\) case:
\[
{}_{2}F_1(\sigma,a;a;-z)
=\sum_{n=0}^{\infty}\frac{(\sigma)_n}{n!}(-z)^n
=(1+z)^{-\sigma}
=\int_{[0,1]}\frac{d\delta_1(t)}{(1+tz)^\sigma}.
\]

The \(q=2\) balanced formula was recorded as a source-dependent bridge: under the source's admissibility assumptions and \(b_1+b_2=a_1+a_2\), the representing measure has an atom at \(t=1\) and a continuous density proportional to
\[
t^{a_2-1}
{}_{2}F_1(b_1-a_1+1,b_2-a_1+1;2;1-t).
\]

The general balanced \(q\) representing-measure problem remains open. Rotate rather than attempt a general Meijer-\(G\) measure extraction in this pass.
