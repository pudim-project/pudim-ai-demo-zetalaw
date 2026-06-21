---
id: "T-KS-qdigamma-power-theta-family-LCM"
type: "theorem"
title: "Krasniqi Shabani q-digamma theta_{q eta} explicit power family is LCM"
status: "proved"
tags: ["inverse-design", "krasniqi-shabani", "literal-existential-solution", "literal-source-solution", "logarithmically-completely-monotone", "not-staging-application", "proved", "q-digamma", "tautological-family", "theorem"]
parents: ["T-Finite-combinatorial-packing-shadow-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private attack plan", "private librarian audit", "private proof note", "wiki/notes/frontier-ks-qdigamma-theta-family.md"]
---

# Theorem: Krasniqi Shabani q-digamma theta_{q eta} explicit power family is LCM

## Statement

For every fixed real-valued q-digamma function \(\psi_q\) on \((0,\infty)\) and every \(\eta\ge0\), the choice \(\theta_{q,\eta}(t)=\exp(\psi_q(t)+(\eta-\gamma)/t)\) makes \(t^{t(\psi_q(t)-\log\theta_{q,\eta}(t))-\gamma}=t^{-\eta}\), hence logarithmically completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`inverse-design`, `krasniqi-shabani`, `literal-existential-solution`, `literal-source-solution`, `logarithmically-completely-monotone`, `not-staging-application`, `proved`, `q-digamma`, `tautological-family`, `theorem`
