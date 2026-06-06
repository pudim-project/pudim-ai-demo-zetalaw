---
id: "T-KS-qdigamma-theta-family-open-problem"
type: "theorem"
title: "Krasniqi Shabani q-digamma theta family LCM existential problem has literal admissible solution"
status: "proved"
tags: ["krasniqi-shabani", "literal-existential-solution", "logarithmically-completely-monotone", "not-staging-application", "open-problem-literal-solution", "proved", "q-digamma", "tautological-family", "theorem"]
parents: ["T-KS-qdigamma-power-theta-family-LCM", "T-Finite-combinatorial-packing-shadow-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["attack-plans/AP-20260531T071000-ks-qdigamma-theta-family.json", "librarian/audits/LA-20260531T071000-ks-qdigamma-theta-family.json", "raw/scout/RS-FI-20260531T071000-ks-qdigamma-source.json", "raw/scout/sources/krasniqi-shabani-qdigamma-theta-family.md", "raw/student/20260531T071000-ks-qdigamma-theta-family.md", "wiki/notes/frontier-ks-qdigamma-theta-family.md"]
---

# Theorem: Krasniqi Shabani q-digamma theta family LCM existential problem has literal admissible solution

## Statement

There exists a family \(\theta(t)\) such that the Krasniqi--Shabani q-digamma expression \(t^{t(\psi_q(t)-\log\theta(t))-\gamma}\) is logarithmically completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-KS-qdigamma-power-theta-family-LCM|Krasniqi Shabani q-digamma theta_{q eta} explicit power family is LCM]]
- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `attack-plans/AP-20260531T071000-ks-qdigamma-theta-family.json`
- `librarian/audits/LA-20260531T071000-ks-qdigamma-theta-family.json`
- `raw/scout/RS-FI-20260531T071000-ks-qdigamma-source.json`
- `raw/scout/sources/krasniqi-shabani-qdigamma-theta-family.md`
- `raw/student/20260531T071000-ks-qdigamma-theta-family.md`
- `wiki/notes/frontier-ks-qdigamma-theta-family.md`

## Proof

The definition gives
\[
\log\theta_{q,\eta}(t)=\psi_q(t)+\frac{\eta-\gamma}{t}.
\]
Therefore
\[
t(\psi_q(t)-\log\theta_{q,\eta}(t))-\gamma
=t\left(-\frac{\eta-\gamma}{t}\right)-\gamma
=-\eta.
\]
So \(Q_{q,\eta}(t)=t^{-\eta}\). Its logarithm is
\[
\log Q_{q,\eta}(t)=-\eta\log t.
\]
For every \(n\ge1\),
\[
(\log Q_{q,\eta})^{(n)}(t)
=(-1)^n\eta (n-1)!t^{-n}.
\]
Thus
\[
(-1)^n(\log Q_{q,\eta})^{(n)}(t)
=\eta (n-1)!t^{-n}\ge0,
\]
for all \(t>0\) and all \(n\ge1\). Hence \(Q_{q,\eta}\) is logarithmically completely monotone. The endpoint \(\eta=0\) gives the constant function \(1\), which is also LCM.

_Proof source: `raw/student/20260531T071000-ks-qdigamma-theta-family.md`._

## Tags

`krasniqi-shabani`, `literal-existential-solution`, `logarithmically-completely-monotone`, `not-staging-application`, `open-problem-literal-solution`, `proved`, `q-digamma`, `tautological-family`, `theorem`
