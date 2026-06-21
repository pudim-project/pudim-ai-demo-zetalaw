---
id: "T-not-Baskakov-higher-power-even-conjecture"
type: "theorem"
title: "not Abel Gawronski Neuschel higher even power Baskakov complete monotonicity conjecture"
status: "proved"
tags: ["application-candidate", "baskakov", "proved", "refutation", "source-open-solved", "theorem"]
parents: ["T-Baskakov-alpha1-r8-not-CM", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "raw/source-cache/baskakov-1411.7945/BaskakovFunctionsV6.tex", "private proof note", "wiki/notes/frontier-baskakov-r4-alpha1-seed.md"]
---

# Theorem: not Abel Gawronski Neuschel higher even power Baskakov complete monotonicity conjecture

## Statement

Abel--Gawronski--Neuschel's even-power Baskakov complete-monotonicity conjecture is false; it fails at \(\alpha=1\), \(r=8\).

## Dependencies

- [[wiki/nodes/T-Baskakov-alpha1-r8-not-CM|Baskakov alpha one r eight rational function is not completely monotone]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `raw/source-cache/baskakov-1411.7945/BaskakovFunctionsV6.tex`
- `private proof note`
- `wiki/notes/frontier-baskakov-r4-alpha1-seed.md`

## Proof

Set
\[
D_m(x)=(1+x)^{2m}-x^{2m}.
\]
The roots are obtained from
\[
\frac{1+x}{x}=\omega_k,\qquad
\omega_k=e^{\pi i k/m},\qquad k=1,\ldots,2m-1.
\]
Thus
\[
\lambda_{k,m}
=\frac{1}{\omega_k-1}
=-\frac12-\frac{i}{2}\cot\frac{\pi k}{2m}.
\]
At this root,
\[
D_m'(\lambda_{k,m})
=2m\lambda_{k,m}^{2m-1}(\omega_k^{-1}-1),
\]
and direct simplification gives the real residue
\[
R_{k,m}
=\frac{1}{D_m'(\lambda_{k,m})}
=\frac{(-1)^{m+k}}{2m}
\left(2\sin\frac{\pi k}{2m}\right)^{2m-2}.
\]
Consequently the inverse-Laplace density is
\[
\rho_m(t)
=\sum_{k=1}^{2m-1}R_{k,m}e^{\lambda_{k,m}t}.
\]
Pairing conjugate roots gives
\[
\rho_m(t)
=\frac{e^{-t/2}}{2m}
\left[
2^{2m-2}
+2\sum_{k=1}^{m-1}
(-1)^{m+k}
\left(2\sin\frac{\pi k}{2m}\right)^{2m-2}
\cos\!\left(
\frac{t}{2}\cot\frac{\pi k}{2m}
\right)
\right].
\]

This proves the finite trigonometric density formula used by the diagnostic
candidate.

For \(m=2\), this gives
\[
\rho_2(t)=e^{-t/2}\left(1-\cos\frac t2\right)
=2e^{-t/2}\sin^2\frac t4\ge0,
\]
recovering the previously admitted \(r=4,\alpha=1\) seed.

For \(m=3\),
\[
\rho_3(t)
=\frac{e^{-t/2}}6
\left[
16+2\cos\left(\frac{\sqrt3\,t}{2}\right)
-18\cos\left(\frac{t}{2\sqrt3}\right)
\right].
\]
Set \(u=t/(2\sqrt3)\).  Since
\(\cos(3u)=4\cos^3u-3\cos u\),
\[
\rho_3(t)
=\frac{4}{3}e^{-t/2}(1-\cos u)^2(2+\cos u)\ge0.
\]
Thus \(r=6,\alpha=1\) is completely monotone by an explicit positive density.

For \(m=4\), write \(h_4(t)=e^{t/2}\rho_4(t)\).  The density formula gives
\[
h_4(t)
=8+2\cos\frac t2
-\frac{(2-\sqrt2)^3}{4}
\cos\left(\frac{1+\sqrt2}{2}t\right)
-\frac{(2+\sqrt2)^3}{4}
\cos\left(\frac{\sqrt2-1}{2}t\right).
\]
At \(t=10\pi\),
\[
\cos(t/2)=\cos(5\pi)=-1,
\]
and both other cosine terms equal \(-\cos(5\pi\sqrt2)\).  Since
\[
(2-\sqrt2)^3+(2+\sqrt2)^3=40,
\]
we obtain
\[
h_4(10\pi)=6+10\cos(5\pi\sqrt2).
\]
Now
\[
0<5\sqrt2-7<\frac14
\]
because \(7/5<\sqrt2<29/20\).  Hence, with
\(\delta=5\sqrt2-7\),
\[
\cos(5\pi\sqrt2)=\cos(7\pi+\pi\delta)=-\cos(\pi\delta)
<-\cos\frac\pi4=-\frac{\sqrt2}{2}<-\frac35.
\]
Therefore
\[
h_4(10\pi)<6+10\left(-\frac35\right)=0,
\]
and
\[
\rho_4(10\pi)=e^{-5\pi}h_4(10\pi)<0.
\]
Since the inverse-Laplace transform is unique for measures on
\([0,\infty)\), \(f^{[8]}_1(x)=1/((1+x)^8-x^8)\) cannot be completely monotone.

_Proof source: `private proof note`._

## Tags

`application-candidate`, `baskakov`, `proved`, `refutation`, `source-open-solved`, `theorem`
