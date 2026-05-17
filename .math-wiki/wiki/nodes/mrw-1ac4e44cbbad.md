---
id: mrw-1ac4e44cbbad
type: theorem
title: Zeta-law successor entropy and modular resolution
aliases: ["mrw-1ac4e44cbbad", "Zeta-law successor entropy and modular resolution"]
status: partial
tags: [zeta-law, theorem, partial, entropy, modular]
parents: [mrw-43596105b428, mrw-538319137c76]
refs: ["raw/20260517T155448Z-build-a-raw-pudim-wiki-for-the-zeta-law-entropy-modular-reso-bootstrap-import.md"]
---

# Theorem: Zeta-law successor entropy and modular resolution

## Statement

For every \(\beta>1\), define
\[
\Sigma(\beta)=\sum_{n=1}^{\infty}\rho_\beta(n)
\log\frac{\rho_\beta(n)}{\rho_\beta(n+1)}.
\]
The imported PDF states
\[
\Sigma(\beta)=
\frac{\beta}{\zeta(\beta)}
\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}\zeta(\beta+k),
\]
and
\[
\Sigma(\beta)=\sup_{q\ge2}B_q(\beta)=\lim_{q\to\infty}B_q(\beta).
\]

## Evidence

The PDF proof expands \(\log(1+1/n)\) and uses a log-sum inequality to compare microscopic successor entropy with finite modular successor entropy. It then lets \(q\to\infty\) so early residue classes isolate the first \(M\) integers up to small tails.

## Depends on

- [[wiki/nodes/mrw-43596105b428|Riemann zeta probability law]]
- [[wiki/nodes/mrw-538319137c76|Modular residue distribution and successor entropy]]

## Used by

- [[wiki/nodes/mrw-b3e8267d43b5|Prime-modulus Dirichlet L-resolution]]
- [[wiki/nodes/mrw-593af0548f67|Four-layer zeta-law framework]]

## Notes

- Status is `partial` because the theorem is imported from PDF extraction and should be audited against the PDF or matching TeX before being marked `proved`.
