---
id: "T-AlzerBerg-palphabeta-endpoint-strip"
type: "lemma"
title: "Alzer-Berg p alpha beta endpoint strip"
status: "proved"
tags: ["alzer-berg", "bridge-result", "complete-monotonicity", "endpoint-obstruction", "lemma", "parameter-region", "proved", "true"]
parents: ["D-AlzerBerg-EulerLimit-palphabeta-Language", "D-Endpoint-obstruction-certificate-language", "O-AlzerBerg-EulerLimit-palphabeta-CM-source-gate"]
refs: ["librarian/audits/LA-20260613T0358-alzerberg-palphabeta-bridge-audit.json", "oracle/responses/OS-20260613Talzerberg-palphabeta-cm-region-oracle-response.md", "raw/student/20260613T0355-alzerberg-palphabeta-strip-stieltjes-wedge.md"]
---

# Lemma: Alzer-Berg p alpha beta endpoint strip

## Statement

If \(p_{\alpha,\beta}(x)=e^\alpha-(1+\alpha/x)^{x+\beta}\) is completely monotone on \((0,\infty)\), then \(-1<\beta\le0\).

## Dependencies

- [[wiki/nodes/D-AlzerBerg-EulerLimit-palphabeta-Language|Alzer-Berg Euler-limit p alpha beta language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/O-AlzerBerg-EulerLimit-palphabeta-CM-source-gate|Alzer-Berg Euler-limit p alpha beta complete monotonicity source gate]]

## Proof and provenance references

- `librarian/audits/LA-20260613T0358-alzerberg-palphabeta-bridge-audit.json`
- `oracle/responses/OS-20260613Talzerberg-palphabeta-cm-region-oracle-response.md`
- `raw/student/20260613T0355-alzerberg-palphabeta-strip-stieltjes-wedge.md`

## Proof

\emph{Alzer-Berg \(p\_{\alpha,\beta}\) Endpoint Strip and Stieltjes Wedge.}

status: bridge-only; no APP-grade full two-parameter classification

Set
\[
F_{\alpha,\beta}(x)=\left(1+\frac{\alpha}{x}\right)^{x+\beta}.
\]
If \(\beta>0\), then as \(x\downarrow0\),
\[
F_{\alpha,\beta}(x)\sim \alpha^\beta x^{-\beta}\to\infty,
\]
so \(p_{\alpha,\beta}(x)<0\) near \(0\), which is incompatible with complete monotonicity.

If \(\beta=-c<0\), then
\[
F_{\alpha,-c}(x)=\alpha^{-c}x^c\{1+O(x\log(1/x))\}.
\]
For \(c>1\), \(F_{\alpha,-c}''(x)>0\) near \(0\), hence \(p_{\alpha,-c}''(x)<0\), violating complete monotonicity. For \(c=1\),
\[
F_{\alpha,-1}(x)=\frac{x}{\alpha}\left(1+x\log\frac{\alpha}{x}+O(x)\right),
\]
again giving \(F_{\alpha,-1}''(x)>0\) near \(0\). Therefore
\[
p_{\alpha,\beta}\in\mathcal{CM}\quad\Longrightarrow\quad -1<\beta\le0.
\]

On the principal branch cut \(\mathbb C\setminus[-\alpha,0]\), for \(0<s<\alpha\),
\[
F_{\alpha,\beta}(-s+i0)
=\left(\frac{\alpha-s}{s}\right)^{\beta-s}e^{-i\pi(\beta-s)}.
\]
Thus
\[
\operatorname{Im}p_{\alpha,\beta}(-s+i0)
=\left(\frac{\alpha-s}{s}\right)^{\beta-s}\sin\pi(\beta-s).
\]
If
\[
-1<\beta\le0,\qquad 0<\alpha\le\beta+1,
\]
then \(\beta-s\in[-1,0]\) on \(0<s<\alpha\), so the boundary density
\[
d\mu_{\alpha,\beta}(s)
=-\frac1\pi
\left(\frac{\alpha-s}{s}\right)^{\beta-s}
\sin\pi(\beta-s)\,ds
\]
is nonnegative. The endpoint case \(\alpha=\beta+1\) also has a positive atom at \(s=\alpha\). Hence
\[
p_{\alpha,\beta}(x)=\int_{(0,\alpha]}\frac{d\mu_{\alpha,\beta}(s)}{x+s},
\]
so \(p_{\alpha,\beta}\) is Stieltjes and therefore completely monotone throughout the wedge
\[
-1<\beta\le0,\qquad 0<\alpha\le\beta+1.
\]

Let
\[
\Phi(x)=(x+\beta)\log\left(1+\frac{\alpha}{x}\right),\qquad F=e^\Phi.
\]
Because \(p_{\alpha,\beta}(\infty)=0\),
\[
p_{\alpha,\beta}\in\mathcal{CM}
\quad\Longleftrightarrow\quad
F_{\alpha,\beta}'\in\mathcal{CM}.
\]
Equivalently, all Bell-polynomial signs
\[
(-1)^{n+1}B_n\bigl(\Phi'(x),\Phi''(x),\ldots,\Phi^{(n)}(x)\bigr)\ge0
\]
must hold for \(n\ge1\), \(x>0\). This is an exact residual criterion, not a closed parameter classification.

_Proof source: `raw/student/20260613T0355-alzerberg-palphabeta-strip-stieltjes-wedge.md`._

## Tags

`alzer-berg`, `bridge-result`, `complete-monotonicity`, `endpoint-obstruction`, `lemma`, `parameter-region`, `proved`, `true`
