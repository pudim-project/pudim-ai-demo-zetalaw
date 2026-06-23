# Frontier: Yin--Huang--Lin k-Digamma Weighted Complete Monotonicity

Scout forage `FI-20260528T-next-loop-009` selected Open Problem 4.1 from Yin--Huang--Lin, "Complete monotonicity of some functions involving \(k\)-digamma function with application", Journal of Mathematical Inequalities 15(1), 2021.

The source asks for parameters \(\alpha,k,a,b,c,d\), with \(k,a,b,c,d>0\), such that
\[
x^\alpha\left[\psi_k(ax+b)-k\log(cx+d)\right]
\]
is completely monotonic on \((0,\infty)\).

The source also proves the base case
\[
B(x)=\psi_k(ax+b)-k\log(cx+d)
\]
is completely monotonic if and only if
\[
\mu=kc+ad-bc\le \frac{kc}{2}.
\]

This node is admitted as a bounded bridge patch rather than as a full parameter-classification campaign. The immediate Student target is the positive-\(\alpha\) endpoint obstruction; the remaining \(\alpha\le0\) classification should be left open and reconsidered only if it offers clear theory growth.

## Student/Librarian outcome `20260528T135000Z`

Student recorded the source-backed \(\alpha=0\) classification and proved the positive-\(\alpha\) endpoint obstruction.

For \(\alpha>0\), define
\[
F_\alpha(x)=x^\alpha B(x).
\]
Because \(b,d>0\), \(B(0^+)\) is finite and therefore
\[
\lim_{x\to0^+}F_\alpha(x)=0.
\]
If \(F_\alpha\) is completely monotonic, then \(F_\alpha\ge0\) and \(F_\alpha'\le0\), so for \(0<x<y\),
\[
0\le F_\alpha(y)\le F_\alpha(x).
\]
Letting \(x\to0^+\) gives \(F_\alpha(y)=0\) for every \(y>0\). Thus the positive-\(\alpha\) branch has only the degenerate zero case.

The source Open Problem 4.1 remains open because the \(\alpha<0\) singular-weight classification was not attempted. Rotate rather than grind this parameter family.

## Strict-APP recheck `20260603T153900Z`

Scout first-contact Oracle `RO-OFC-20260603T-yhl-weighted-cm-strict-app-rerun` verified that the exact source problem remains source-open to the checked later-literature standard. Student Oracle `RO-OS-20260603T-yhl-weighted-cm-strict-app-temp` advised that the \(\alpha<0\) converse is the real obstruction, not a routine product-closure step.

The admitted non-APP theory growth is the sufficient region
\[
\alpha\le0,\qquad \mu=kc+ad-bc\le \frac{kc}{2}
\quad\Longrightarrow\quad
x^\alpha\left[\psi_k(ax+b)-k\log(cx+d)\right]\in CM(0,\infty).
\]

For \(\alpha<0\), write \(\alpha=-r\). The proof is only that \(x^{-r}\) is completely monotonic and products of completely monotonic functions are completely monotonic, applied to the source-imported \(\alpha=0\) bracket classification.

This is not a strict APP solve. The full source problem still needs the converse for \(\alpha<0\), or a different exact classification. The kernel obstruction is that multiplying by \(x^{-r}\) corresponds to fractional integration of the bracket's Laplace kernel, so positivity after fractional integration need not force positivity of the original kernel.
