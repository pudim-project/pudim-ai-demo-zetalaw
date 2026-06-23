# Baskakov Higher-Power Seed

## Source

Abel--Gawronski--Neuschel, arXiv:1411.7945, defines the higher-power functions
\[
f^{[r]}_\alpha(x)
=(1+x)^{-r\alpha}\sum_{k=0}^{\infty}
\binom{-\alpha}{k}^{r}\left(\frac{x}{1+x}\right)^{rk}
\]
and conjectures complete monotonicity for every even integer \(r>1\) and every \(\alpha>0\).

## Local Result

For the first nontrivial seed \((r,\alpha)=(4,1)\),
\[
f^{[4]}_1(x)=\frac{1}{(1+x)^4-x^4}.
\]
The partial-fraction identity gives
\[
f^{[4]}_1(x)
=\int_0^\infty e^{-xt}e^{-t/2}\left(1-\cos\frac{t}{2}\right)\,dt.
\]
The density is nonnegative, so \(f^{[4]}_1\) is completely monotone.

The same proof gives the diagonal Baskakov corollary
\[
\psi^{[4]}_{n,n}(x)=f^{[4]}_1(nx)\in CM(0,\infty).
\]

## Boundary

This is a seed-only solution inside the source conjecture. It does not solve the full even-\(r\), all-\(\alpha\) conjecture and should not be public-staged as a full application without an explicit editorial decision.

The next elegant frontier is the \(\alpha=1\) even line
\[
f^{[2m]}_1(x)=\frac{1}{(1+x)^{2m}-x^{2m}},
\qquad m\ge2,
\]
where positivity of the inverse Laplace density is nontrivial for \(m\ge3\).

## Advisor plan `20260601T000500-0300`

After the Du--Wang \(h_3\) solve, Advisor selected the \(\alpha=1\) even line
as a fresh low-hanging source-backed target in the Laplace-density layer.  This
is not a repeat of the solved \(r=4,\alpha=1\) seed; the old seed is used only
as the \(m=2\) normalization check.

`AP-20260601T000500-baskakov-alpha1-even-line` introduces three candidates:

- \(T\)-Baskakov-alpha1-even-line-positive-Laplace-density: prove that every
  \(f^{[2m]}_1\) has a nonnegative inverse-Laplace density;
- \(T\)-Baskakov-alpha1-even-line-Fejer-density-factorization: strengthen the
  density route by writing the density as \(e^{-t/2}\) times a nonnegative
  Fejer-type or sine-square trigonometric factor;
- \(T\)-Baskakov-alpha1-even-line-density-sign-diagnostic: if the positivity
  route fails, certify the first genuine sign obstruction rather than relying
  on numerical plotting.

The intended source-solving path is
\[
T\text{-Baskakov-alpha1-even-line-Fejer-density-factorization}
\Rightarrow
T\text{-Baskakov-alpha1-even-line-positive-Laplace-density}
\Rightarrow
T\text{-Baskakov-alpha1-even-r-frontier-open}.
\]

The next Student pass must begin with the Student Oracle gate on this concrete
Baskakov \(\alpha=1\) even-line target, then derive the residue/inverse-Laplace
density and audit its sign structure.

## Student outcome `20260601T002500-0300`

Student Oracle `ORACLE-OS-20260601T001000-baskakov-alpha1-even-line` completed
live and identified a sign obstruction in the inverse-Laplace density.  The
local audit verified the source normalization: for \(\alpha=1\) and \(r=2m\),
\[
f^{[2m]}_1(x)=\frac{1}{(1+x)^{2m}-x^{2m}}.
\]

For
\[
D_m(x)=(1+x)^{2m}-x^{2m},
\]
the poles are
\[
\lambda_{k,m}=-\frac12-\frac{i}{2}\cot\frac{\pi k}{2m},
\qquad k=1,\ldots,2m-1,
\]
with residues
\[
R_{k,m}
=\frac{(-1)^{m+k}}{2m}
\left(2\sin\frac{\pi k}{2m}\right)^{2m-2}.
\]
Thus
\[
\rho_m(t)
=\frac{e^{-t/2}}{2m}
\left[
2^{2m-2}
+2\sum_{k=1}^{m-1}
(-1)^{m+k}
\left(2\sin\frac{\pi k}{2m}\right)^{2m-2}
\cos\left(\frac t2\cot\frac{\pi k}{2m}\right)
\right]
\]
is the inverse-Laplace density.

The \(m=3\) case is positive:
\[
\rho_3(t)=
\frac43 e^{-t/2}
\left(1-\cos\frac{t}{2\sqrt3}\right)^2
\left(2+\cos\frac{t}{2\sqrt3}\right).
\]
But the \(m=4\) case is negative at \(t=10\pi\).  If
\(h_4(t)=e^{t/2}\rho_4(t)\), then
\[
h_4(10\pi)=6+10\cos(5\pi\sqrt2)<0.
\]
Therefore \(f^{[8]}_1\) is not completely monotone.  The \(\alpha=1\) even
line is solved negatively, and the full source conjecture is refuted at
\(\alpha=1,r=8\).  This is a local source-open solve, not a public staging
event.
