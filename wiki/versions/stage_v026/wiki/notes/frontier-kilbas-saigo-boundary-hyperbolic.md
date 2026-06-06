# Frontier: Kilbas-Saigo Boundary Hyperbolic Lower Bound

## Source

Boudabsa and Simon, "Some Properties of the Kilbas-Saigo Function", Mathematics 9(3), 217, 2021.

Source URL: https://www.mdpi.com/2227-7390/9/3/217/pdf?version=1611307297

The diversity forage cycle selects Conjecture 3 from this paper as a fresh, author-diverse source target. The source concerns the boundary Kilbas-Saigo function
\[
E_{\alpha,m,m-1/\alpha}(-x)
\]
and asks for a uniform lower hyperbolic bound for \(\alpha\in(0,1]\), \(m>0\), and \(x\ge0\). With
\[
C_{\alpha,m}
=
(\alpha m)^{-\alpha/(m+1)}
\left(\Gamma(1+\alpha)G(1-\alpha;\alpha m)G(1+\alpha;\alpha m)\right)^{-m/(m+1)},
\]
the conjectured bound is
\[
E_{\alpha,m,m-1/\alpha}(-x)
\ge
\left(1+C_{\alpha,m}x\right)^{-1-1/m}.
\]
The source records the \(m=1\) case as known and says the general case remains out of reach.

## Domain Fit

This is not a continuation of the reciprocal zeta-tail sequence. It introduces a different author pair and a new special-function family, but remains inside the current theory's useful neighborhood: Laplace transforms, complete monotonicity, Mellin transforms, Gamma quotients, and sharp hyperbolic bounds.

The bridge layer should treat the right side as the Laplace transform of a Gamma comparison variable. The immediate normal form is a Laplace-order statement between the boundary Kilbas-Saigo random variable and that Gamma variable. A stronger route should look for a Mellin/double-Gamma convex-order certificate.

## Attack Policy

Do not try to grind the full conjecture indefinitely. The first Student pass should:

- verify the source formula and parameter conventions;
- derive the Laplace-order normal form;
- attempt a double-Gamma Mellin-transform certificate only while it yields concrete identities;
- if the full route stalls, prove or refute a nontrivial slice outside the already-known \(m=1\) case, or hand back to Scout for the next diverse candidate.

The zeta-tail \(s=10\) branch is explicitly rejected for this cycle as parameter farming.

## Student Normalization Outcome

The first Student pass proved the Gamma Laplace-transform normalization. If \(p=1+1/m\) and \(Z_{\alpha,m}\sim\Gamma(p,C_{\alpha,m})\), then
\[
\mathbb E e^{-xZ_{\alpha,m}}=(1+C_{\alpha,m}x)^{-p}.
\]
Thus the conjecture is equivalent to the Laplace-order statement
\[
Z_{\alpha,m}\le_{Lt}X_{\alpha,m},
\qquad
\mathbb E e^{-xX_{\alpha,m}}=E_{\alpha,m,m-1/\alpha}(-x).
\]

The same pass checked that the conjectured constant is sharp at infinity. With
\[
D_{\alpha,m}=\Gamma(1+\alpha)G(1-\alpha;\alpha m)G(1+\alpha;\alpha m),
\]
one has
\[
C_{\alpha,m}^{-(1+1/m)}=(\alpha m)^{\alpha/m}D_{\alpha,m},
\]
matching the source asymptotic coefficient.

The full double-Gamma Mellin bridge remains open. Under the diversity/no-stalling rule, this branch should either receive a quick non-\(m=1\) slice certificate or be rotated out in favor of another author/problem.
