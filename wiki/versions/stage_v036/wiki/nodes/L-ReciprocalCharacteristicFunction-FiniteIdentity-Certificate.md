---
id: "L-ReciprocalCharacteristicFunction-FiniteIdentity-Certificate"
type: "lemma"
title: "Finite reciprocal characteristic-function identity certificate"
status: "proved"
tags: ["bridge", "characteristic-function", "finite-certificate", "functional-equation", "lemma", "proved", "strict-private-post-v016", "true"]
parents: ["D-Finite-dimensional-L1-certificate-language", "T-Exact-finite-certificate-verification-principle"]
refs: ["oracle/responses/OS-20260620T2240Z-rr-condition3-oracle-response.md", "raw/student/20260620T2250-rr-condition3-laplace-counterexample.md"]
---

# Lemma: Finite reciprocal characteristic-function identity certificate

## Statement

Let \(\varphi\) be a characteristic function with reciprocal \(q=1/\varphi\) on a neighborhood of the origin, let \(\mu_1,\ldots,\mu_n\) be distinct nonzero real numbers, and let \(\theta_k=\prod_{j\ne k}\mu_k/(\mu_k-\mu_j)\). If the finite identity \(\sum_{k=1}^n\theta_k\prod_{j\ne k}q(\mu_jt)=1\) holds for all real \(t\), then \(\varphi\) satisfies the Rastegar--Roitershtein functional equation \(\prod_j\varphi(\mu_jt)=\sum_k\theta_k\varphi(\mu_kt)\).

## Dependencies

- D-Finite-dimensional-L1-certificate-language
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `oracle/responses/OS-20260620T2240Z-rr-condition3-oracle-response.md`
- `raw/student/20260620T2250-rr-condition3-laplace-counterexample.md`

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

_Proof source: `raw/student/20260620T2250-rr-condition3-laplace-counterexample.md`._

## Do not claim

- Do not claim this characterizes all solutions of the source functional equation.
- Do not use without verifying that the proposed reciprocal q is positive definite through 1/q.
- Do not public-stage without user request.

## Tags

`bridge`, `characteristic-function`, `finite-certificate`, `functional-equation`, `lemma`, `proved`, `strict-private-post-v016`, `true`
