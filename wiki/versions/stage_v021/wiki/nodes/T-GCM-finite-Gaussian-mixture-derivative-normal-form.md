---
id: "T-GCM-finite-Gaussian-mixture-derivative-normal-form"
type: "theorem"
title: "finite Gaussian mixture heat-flow entropy derivative normal form"
status: "proved"
tags: ["attack-plan", "certificate-normal-form", "entropy", "gaussian-mixture", "heat-flow", "proved", "theorem", "wide"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["attack-plans/AP-20260528T122000-gcm-counterexample.json", "librarian/audits/LA-20260528T122000-gcm-counterexample-attack-plan.json", "librarian/audits/LA-20260528T123000-gcm-fifth-derivative-counterexample.json", "raw/student/20260528T122500-gcm-fifth-derivative-counterexample.md", "wiki/notes/frontier-gcm-counterexample.md"]
---

# Theorem: finite Gaussian mixture heat-flow entropy derivative normal form

## Statement

For a finite atomic measure \(\mu=\sum_i w_i\delta_{a_i}\), the heat-flow entropy derivatives \(H_\mu^{(m)}(t)\) can be written as one-dimensional integrals of explicit polynomial-rational expressions in the Gaussian mixture density \(g_t=p_t*\mu\) and its time derivatives, giving a reproducible certificate format for sign checks.

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

- `attack-plans/AP-20260528T122000-gcm-counterexample.json`
- `librarian/audits/LA-20260528T122000-gcm-counterexample-attack-plan.json`
- `librarian/audits/LA-20260528T123000-gcm-fifth-derivative-counterexample.json`
- `raw/student/20260528T122500-gcm-fifth-derivative-counterexample.md`
- `wiki/notes/frontier-gcm-counterexample.md`

## Proof

The selected source conjecture is the Gaussian heat-flow entropy sign pattern
\[
(-1)^mH_\mu^{(m)}(t)\ge0,\qquad m\ge1,\ t>0,
\]
where
\[
H_\mu(t)=\int_{\mathbb R}(p_t*\mu)(x)\log(p_t*\mu)(x)\,dx.
\]

At \(m=5\), the sign condition requires \(H_\mu^{(5)}(t)\le0\). Therefore any probability measure with \(H_\mu^{(5)}(t_0)>0\) proves the negated node.

The source supplies a SageMath/Arb ball-arithmetic script using exact rational atoms and weights, 256-bit complex balls, and interval integrations. Its table gives \(22\) finite interval contributions \(C_I=2\int_I G(x)\,dx\), each within \(10^{-4}\) of its displayed midpoint, plus the tail bound
\[
\left|2\int_{25}^{\infty}G(x)\,dx\right|<10^{-20}.
\]

Summing the displayed midpoints gives
\[
\sum_I M_I=0.3656000000000184.
\]
The total radius from the displayed finite intervals is at most \(22\cdot10^{-4}=0.0022\), so the finite part lies in
\[
[0.3634,0.3678].
\]
Adding the \(10^{-20}\) tail does not affect the displayed bounds, hence
\[
0.36 < H_\mu^{(5)}(1/3) < 0.37.
\]

I also ran an independent high-precision mpmath replay of the same \(G\)-integral over the same intervals. It returned
\[
H_\mu^{(5)}(1/3)\approx 0.365699699653624948585017221126,
\]
consistent with the rigorous source interval. SageMath is not installed in this workspace, so the Arb script in the source was read and arithmetically audited rather than re-run locally.

_Proof source: `raw/student/20260528T122500-gcm-fifth-derivative-counterexample.md`._

## Tags

`attack-plan`, `certificate-normal-form`, `entropy`, `gaussian-mixture`, `heat-flow`, `proved`, `theorem`, `wide`
