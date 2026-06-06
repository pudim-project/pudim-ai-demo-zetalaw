---
id: "T-Tao-Leja-Chebyshev-complement-L1-pivot-identity"
type: "theorem"
title: "Complement L1-to-pivot identity for Chebyshev-Leja next-pivot Lebesgue values"
status: "proved"
tags: ["proved", "theorem"]
parents: ["Q_n(t)=prod_{u in X_n}(t-u)=2^{1-n}T_n(t)", "|Q_n'(cos theta)|=2^{1-n}n/sin theta", "Complement factorization Q_n=omega_A omega_B"]
refs: [".pudim/attack-plans/AP-20260604T-tao-leja-residual-identity.json", ".pudim/oracle/responses/ORACLE-OS-20260604T-tao-leja-next-pivot-lebesgue-student-response.md", ".pudim/raw/student/20260604T-tao-leja-residual-identity.md", ".pudim/wiki/notes/tao-leja-residual-identity.md"]
---

# Theorem: Complement L1-to-pivot identity for Chebyshev-Leja next-pivot Lebesgue values

## Statement

At a Chebyshev-Leja step, 1 plus the prefix Lebesgue function at the next pivot equals a weighted residual L1-to-pivot ratio over the complement.
\[
1+lambda_A(y)=sum_{u in X_n} sin(theta_u)|chi_C(u)| /(sin(theta_y)|chi_C(y)|).
\]

## Dependencies

- Q_n(t)=prod_{u in X_n}(t-u)=2^{1-n}T_n(t)
- |Q_n'(cos theta)|=2^{1-n}n/sin theta
- Complement factorization Q_n=omega_A omega_B

## Proof and provenance references

- `.pudim/attack-plans/AP-20260604T-tao-leja-residual-identity.json`
- `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-leja-next-pivot-lebesgue-student-response.md`
- `.pudim/raw/student/20260604T-tao-leja-residual-identity.md`
- `.pudim/wiki/notes/tao-leja-residual-identity.md`

## Do not claim

- Do not claim the averaged residual bound is proved.
- Do not claim source_open_solved_scoped.

## Tags

`proved`, `theorem`
