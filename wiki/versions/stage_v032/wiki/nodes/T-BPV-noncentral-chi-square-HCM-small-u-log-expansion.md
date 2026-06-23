---
id: "T-BPV-noncentral-chi-square-HCM-small-u-log-expansion"
type: "theorem"
title: "BPV noncentral chi-square HCM small u hyperbolic product log expansion"
status: "proved"
tags: ["HCM", "modified-bessel", "noncentral-chi-square", "partial-source-progress", "proved", "small-u-expansion", "theorem"]
parents: ["T-endpoint-log-derivative-monotonicity-principle", "D-Hyperbolically-completely-monotone-language"]
refs: ["attack-plans/AP-20260531T062200-noncentral-chi-square-hcm.json", "librarian/audits/LA-20260531T062900-noncentral-chi-square-hcm.json", "oracle/responses/ORACLE-OS-20260531T-noncentral-chi-square-hcm-oracle-response.md", "raw/scout/sources/bpv-noncentral-chi-square-hcm-source-status.md", "raw/student/20260531T062900-noncentral-chi-square-hcm.md", "wiki/notes/frontier-noncentral-chi-square-hcm.md"]
---

# Theorem: BPV noncentral chi-square HCM small u hyperbolic product log expansion

## Statement

For \(\mu>0\), \(\lambda>0\), and \(H_u(w)=\chi_{\mu,\lambda}(uv)\chi_{\mu,\lambda}(u/v)\) with \(w=v+v^{-1}\), uniformly for \(w\) in compact subintervals of \([2,\infty)\), \(\log H_u(w)=C_u+\frac{u}{2}(\lambda/\mu-1)w-\frac{\lambda^2u^2}{4\mu^2(\mu+2)}(w^2-2)+O(u^3)\) as \(u\downarrow0\).

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]
- [[wiki/nodes/D-Hyperbolically-completely-monotone-language|Hyperbolically completely monotone density]]

## Proof and provenance references

- `attack-plans/AP-20260531T062200-noncentral-chi-square-hcm.json`
- `librarian/audits/LA-20260531T062900-noncentral-chi-square-hcm.json`
- `oracle/responses/ORACLE-OS-20260531T-noncentral-chi-square-hcm-oracle-response.md`
- `raw/scout/sources/bpv-noncentral-chi-square-hcm-source-status.md`
- `raw/student/20260531T062900-noncentral-chi-square-hcm.md`
- `wiki/notes/frontier-noncentral-chi-square-hcm.md`

## Proof

The source asks for the optimal parameter range in which
\[
\chi_{\mu,\lambda}(x)
=\frac12 e^{-(x+\lambda)/2}
\left(\frac{x}{\lambda}\right)^{\mu/4-1/2}
I_{\mu/2-1}(\sqrt{\lambda x})
\]
is hyperbolically completely monotone.

The local small-\(u\) hyperbolic-product expansion is
\[
\log\{\chi_{\mu,\lambda}(uv)\chi_{\mu,\lambda}(u/v)\}
=C_u+\frac{u}{2}\left(\frac{\lambda}{\mu}-1\right)w
-\frac{\lambda^2u^2}{4\mu^2(\mu+2)}(w^2-2)
+O(u^3),
\qquad w=v+v^{-1}.
\]

Consequences:
\[
\lambda>\mu\quad\Longrightarrow\quad \chi_{\mu,\lambda}\notin HCM,
\]
and
\[
(\lambda-\mu)^2<\frac{2\lambda^2}{\mu+2}
\quad\Longrightarrow\quad
\chi_{\mu,\lambda}\notin HCM.
\]

Equivalently, inside \(0<\lambda\le\mu\), the second obstruction excludes
\[
\frac{\lambda}{\mu}>
\frac{1}{1+\sqrt{2/(\mu+2)}}.
\]

Remaining frontier:
\[
0<\lambda\le\mu,\qquad
(\lambda-\mu)^2\ge\frac{2\lambda^2}{\mu+2}.
\]

This note is partial theory growth only. Do not stage as a solved application unless the full optimal HCM range is proved or the source problem is explicitly narrowed.

_Proof source: `wiki/notes/frontier-noncentral-chi-square-hcm.md`._

## Tags

`HCM`, `modified-bessel`, `noncentral-chi-square`, `partial-source-progress`, `proved`, `small-u-expansion`, `theorem`
