---
id: "T-not-Gaussian-entropy-heat-flow-CM-conjecture"
type: "theorem"
title: "negation of Gaussian heat-flow entropy complete monotonicity conjecture"
status: "proved"
tags: ["candidate-negation", "complete-monotonicity", "entropy", "fresh-forage", "gcm", "heat-flow", "proved", "theorem"]
parents: ["T-GCM-fifth-derivative-counterexample-certificate", "T-Logconcave-GCM-explicit-failure-order", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Exact-finite-certificate-verification-principle"]
refs: ["librarian/audits/LA-20260528T122000-gcm-counterexample-attack-plan.json", "librarian/audits/LA-20260528T123000-gcm-fifth-derivative-counterexample.json", "raw/scout/sources/gu-sellke-gcm-counterexample-2605.11656/main.tex", "raw/student/20260528T122500-gcm-fifth-derivative-counterexample.md", "scout/forage/inbox/FI-20260528T-next-loop-005.json", "wiki/notes/frontier-gcm-counterexample.md"]
---

# Theorem: negation of Gaussian heat-flow entropy complete monotonicity conjecture

## Statement

not(For every probability measure \(\mu\) on \(\mathbb R\) for which the heat-flow entropy \(H_\mu(t)=\int_{\mathbb R}(p_t*\mu)(x)\log(p_t*\mu)(x)\,dx\) is finite, one has \((-1)^mH_\mu^{(m)}(t)\ge0\) for every \(m\ge1\) and \(t>0\).)

## Dependencies

- [[wiki/nodes/T-GCM-fifth-derivative-counterexample-certificate|Gu Sellke finite symmetric atomic measure has positive fifth heat-flow entropy derivative at t=1/3]]
- [[wiki/nodes/T-Logconcave-GCM-explicit-failure-order|explicit log-concave Gaussian heat-flow entropy complete monotonicity failure order]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `librarian/audits/LA-20260528T122000-gcm-counterexample-attack-plan.json`
- `librarian/audits/LA-20260528T123000-gcm-fifth-derivative-counterexample.json`
- `raw/scout/sources/gu-sellke-gcm-counterexample-2605.11656/main.tex`
- `raw/student/20260528T122500-gcm-fifth-derivative-counterexample.md`
- `scout/forage/inbox/FI-20260528T-next-loop-005.json`
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

`candidate-negation`, `complete-monotonicity`, `entropy`, `fresh-forage`, `gcm`, `heat-flow`, `proved`, `theorem`
