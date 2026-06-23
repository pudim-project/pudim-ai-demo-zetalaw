---
id: "T-Bouali-falpha-phi-asymptotic"
type: "theorem"
title: "Bouali f alpha phi alpha endpoint asymptotic"
status: "proved"
tags: ["bouali", "complete-monotonicity", "digamma", "endpoint-asymptotic", "proved", "source-correction", "theorem"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["attack-plans/AP-20260531T050824-bouali-falpha-endpoint.json", "oracle/responses/ORACLE-FI-20260531T-rolling-066-oracle-forage-response.md", "oracle/responses/ORACLE-OS-20260531T-bouali-falpha-endpoint-oracle-response.md", "raw/scout/sources/bouali-falpha-endpoint-source-status.md", "raw/source-cache/bouali-falpha-endpoint/bouali-falpha-endpoint.txt", "raw/student/20260531T050824-bouali-falpha-endpoint.md", "wiki/notes/frontier-bouali-falpha-endpoint.md"]
---

# Theorem: Bouali f alpha phi alpha endpoint asymptotic

## Statement

For \(f_\alpha(x)=x^{x(\psi(x)-\log x)-\alpha}\), \(\theta(x)=x(\log x-\psi(x))\), and \(\phi_\alpha(x)=-(\log f_\alpha)'(x)\), one has \(\phi_\alpha(x)=(\alpha+1/2)/x+(1-\log x)/(12x^2)+O(\log x/x^4)\) as \(x\to\infty\).

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `attack-plans/AP-20260531T050824-bouali-falpha-endpoint.json`
- `oracle/responses/ORACLE-FI-20260531T-rolling-066-oracle-forage-response.md`
- `oracle/responses/ORACLE-OS-20260531T-bouali-falpha-endpoint-oracle-response.md`
- `raw/scout/sources/bouali-falpha-endpoint-source-status.md`
- `raw/source-cache/bouali-falpha-endpoint/bouali-falpha-endpoint.txt`
- `raw/student/20260531T050824-bouali-falpha-endpoint.md`
- `wiki/notes/frontier-bouali-falpha-endpoint.md`

## Proof

Status: endpoint/lower-region obstruction solved; interior gap remains open.

Bouali studies
\[
f_\alpha(x)=x^{x(\psi(x)-\log x)-\alpha}.
\]
The source proves logarithmic complete monotonicity, hence complete monotonicity, for \(\alpha\ge -1/4\). Remark 1.12 prints the open range as \((-1/4,-1/2]\), which is reversed as a literal interval. The local correction treats the intended unresolved lower side as a frontier and proves that the endpoint \(\alpha=-1/2\) cannot be included.

Let \(\theta(x)=x(\log x-\psi(x))\) and
\[
\phi_\alpha(x)=-(\log f_\alpha)'(x)=\frac{\theta(x)+\alpha}{x}+\theta'(x)\log x.
\]
The digamma expansion gives
\[
\phi_\alpha(x)=\frac{\alpha+1/2}{x}+\frac{1-\log x}{12x^2}+O\!\left(\frac{\log x}{x^4}\right).
\]
Thus \(\phi_\alpha(x)<0\) eventually whenever \(\alpha\le -1/2\). Since positive complete monotone functions must be nonincreasing, this proves
\[
\alpha\le -\frac12 \quad\Longrightarrow\quad f_\alpha\notin CM(0,\infty).
\]

This is useful theory growth because it packages a reusable Gamma/psi endpoint-obstruction template, but it is not application-eligible as a full solution. The interior interval
\[
-\frac12<\alpha<-\frac14
\]
remains open.

confirmed the corrected interior interval as source-open and found no later
gap. It isolated the reduction
\[
f_\alpha(x)=x^\beta f_{-1/4}(x),
\qquad
\beta=-(\alpha+1/4)\in(0,1/4),
\]
so the remaining problem is whether the non-CM factor \(x^\beta\) preserves
complete monotonicity for this specific endpoint function. This is useful
theory growth, but not a solved source open problem and not APP-countable.

_Proof source: `wiki/notes/frontier-bouali-falpha-endpoint.md`._

## Tags

`bouali`, `complete-monotonicity`, `digamma`, `endpoint-asymptotic`, `proved`, `source-correction`, `theorem`
