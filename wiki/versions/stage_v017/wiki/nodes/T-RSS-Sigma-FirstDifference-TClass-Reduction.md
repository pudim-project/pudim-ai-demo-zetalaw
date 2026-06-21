---
id: "T-RSS-Sigma-FirstDifference-TClass-Reduction"
type: "lemma"
title: "RSS sigma first-difference T-class reduction"
status: "proved"
tags: ["bridge-result", "hausdorff-moment", "lemma", "proved", "residual-target", "rss", "universal-convexity"]
parents: ["D-RSS-UniversalConvexity-TClass-Language", "O-RSS-Sigma-UniversalConvexity-source-gate"]
refs: ["private librarian audit", "private Oracle response", "private proof note"]
---

# Lemma: RSS sigma first-difference T-class reduction

## Statement

Let \(Q_\sigma(z)=1+z\sigma''(z)/(2\sigma'(z))\). With \(b_n=\theta_n-1/3\), \(C_n=4/135-nb_n\), \(d_n=C_{n-1}-C_n\), and \(D(z)=\sum_{n\ge1}d_nz^{n-1}\), one has \(2Q_\sigma(z)-1/(1-z)=1+zD'(z)/D(z)\). Since the known RSS-adjacent theorem gives \(D\in\mathcal T\), proving \(1+zD'(z)/D(z)\in\mathcal T\) would prove the RSS universal-convexity conjecture for \(\sigma\).

## Dependencies

- [[wiki/nodes/D-RSS-UniversalConvexity-TClass-Language|RSS universal convexity and T-class language]]
- [[wiki/nodes/O-RSS-Sigma-UniversalConvexity-source-gate|RSS sigma universal convexity source gate]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`

## Proof

status: bridge-only; no APP-grade decision

Set
\[
b_n=\theta_n-\frac13,\qquad B_n=nb_n,\qquad C_n=\frac4{135}-B_n,
\]
and
\[
d_n=C_{n-1}-C_n,\qquad D(z)=\sum_{n\ge1}d_nz^{n-1}.
\]
The later Bakan--Ruscheweyh--Salinas theorem gives \(D\in\mathcal T\). Algebraically,
\[
(1-z)\sum_{n\ge1}nb_nz^{n-1}=D(z),
\]
and hence
\[
2Q_\sigma(z)-\frac{1}{1-z}=1+\frac{zD'(z)}{D(z)}.
\]
Therefore
\[
1+\frac{zD'(z)}{D(z)}\in\mathcal T
\quad\Longrightarrow\quad
Q_\sigma\in\mathcal T,
\]
because \(\mathcal T\) is convex and \(1/(1-z)\in\mathcal T\).

This is a sharper residual target for the RSS problem, but it is not itself a proof of universal convexity. The missing step is to prove
\[
1+\frac{zD'(z)}{D(z)}\in\mathcal T.
\]

_Proof source: `private proof note`._

## Tags

`bridge-result`, `hausdorff-moment`, `lemma`, `proved`, `residual-target`, `rss`, `universal-convexity`
