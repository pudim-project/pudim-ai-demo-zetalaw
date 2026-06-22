---
id: "N-BuricElezovic-BestB-Threshold"
type: "note"
title: "Buric-Elezovic best-b threshold"
status: "local-proved-bridge-not-app"
tags: ["complete-monotonicity", "digamma", "laplace-density", "bridge-result", "not-app", "source-restatement-required", "literature-closure-risk"]
parents: ["L-Affine-Laplace-Density-Threshold"]
refs: ["raw/student/20260609T1518-buric-elezovic-affine-density-threshold.md", "oracle/responses/OS-20260609T1520Z-buric-elezovic-attachment-oracle-response.md"]
---

# Buric-Elezovic best-b threshold

## Local theorem

Let
\[
A(t)=\frac1t-\frac{1}{2\sinh(t/2)},\qquad
b_*=\sup_{t>0}\frac{-A'(t)}{A(t)}.
\]
Then
\[
(x+b)\left(\psi\left(x+\frac12\right)-\log x\right)
\]
is completely monotone on \((0,\infty)\) if and only if \(b\ge b_*\).

## Current status

This is locally proved as a bridge result using the affine Laplace density threshold. It is not admitted as an APP.

The primary source explicitly leaves the best lower bound for \(b\) in Corollary 6 open, but the local variational formulation with \(A(t)\) and \(b_*\) is a restatement rather than the source wording. Later Yang-Chu-Zhang literature contains the same kernel mechanism \(Q(t)=1/t-1/(2\sinh(t/2))\) and the sharp \(Q'/Q\) constant mechanism, so the local result should be treated as a bridge primitive/literature extraction unless a stricter novelty audit reverses this.

The decimal anchor \(b_*\approx0.0717001453498977\) is useful for testing only; no interval certificate has been admitted.

## Source gate

- First-contact Oracle: `raw/oracle/RO-OFC-20260609T1543Z-buric-elezovic-source-gate-live.json`
- Recommendation: `needs_restatement`
- APP decision: not APP
