---
id: "T-Not-RastegarRoitershtein-Condition3-Unnecessary"
type: "counterexample"
title: "Rastegar-Roitershtein condition-removal conjecture is false"
status: "proved"
tags: ["application-candidate", "characteristic-function", "counterexample", "finite-certificate", "functional-equation", "laplace-distribution", "open-problem-solved", "proved", "source-solving", "strict-private-post-v016", "true"]
parents: ["O-RastegarRoitershtein-ExponentialCharacterization-Condition3-source-gate", "L-ReciprocalCharacteristicFunction-FiniteIdentity-Certificate", "D-Finite-dimensional-L1-certificate-language", "T-Exact-finite-certificate-verification-principle"]
refs: ["private Oracle response", "private proof note"]
---

# Counterexample: Rastegar-Roitershtein condition-removal conjecture is false

## Statement

The Rastegar--Roitershtein conjecture that condition (1.3), numbered condition (3) in the preprint, is unnecessary in Theorem 1.1 for \(n\ge3\) is false. For \(n=3\), \(\mu=(1,2,-2/3)\), the source weights are \(\theta=(-3/5,3/2,1/10)\), and the centered Laplace characteristic function \(\varphi(t)=1/(1+a t^2)\), \(a>0\), satisfies the source functional equation identically, while the law is nondegenerate, has mean zero, and is not one-sided exponential.

## Dependencies

- [[wiki/nodes/O-RastegarRoitershtein-ExponentialCharacterization-Condition3-source-gate|Rastegar-Roitershtein exponential characterization condition (3) source gate]]
- [[wiki/nodes/L-ReciprocalCharacteristicFunction-FiniteIdentity-Certificate|Finite reciprocal characteristic-function identity certificate]]
- D-Finite-dimensional-L1-certificate-language
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`

## Proof

The local Sympy audit verified:

\((\theta_1,\theta_2,\theta_3)=(-3/5,3/2,1/10)\);
\(\sum_k\theta_k=1\);
\(\sum_k\theta_k\prod_{j\ne k}(1+a\mu_j^2t^2)=1\) identically;
the original functional-equation difference is identically \(0\);
\(h_2(\mu)-p_2(\mu)=0\).

This is a finite symbolic characteristic-function certificate, not a numerical Taylor match.

The reusable bridge is the finite reciprocal-characteristic certificate:
if a nonzero real vector \(\mu\), the source weights \(\theta_k\), and a positive-definite reciprocal polynomial \(q(t)=1+a t^2\) satisfy
\[
\sum_{k=1}^n\theta_k\prod_{j\ne k}q(\mu_jt)=1
\]
identically, then \(\varphi=1/q\) gives an exact source functional-equation solution. When this \(X\) is not in the source conclusion class, it is a source-level counterexample.

The present \(n=3\) data provide such a certificate.

_Proof source: `private proof note`._

## Do not claim

- Do not claim this contradicts the stated theorem, which assumes condition (1.3)/(3).
- Do not claim a full classification of all defect-zero solutions.
- Do not claim anything about Theorem 1.2 unless separately source-gated.
- Do not assign public APP numbering until staging/registry promotion.
- Do not public-stage without user request.

## Tags

`application-candidate`, `characteristic-function`, `counterexample`, `finite-certificate`, `functional-equation`, `laplace-distribution`, `open-problem-solved`, `proved`, `source-solving`, `strict-private-post-v016`, `true`
