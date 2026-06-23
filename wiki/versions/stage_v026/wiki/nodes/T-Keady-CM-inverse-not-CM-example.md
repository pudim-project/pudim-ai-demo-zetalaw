---
id: "T-Keady-CM-inverse-not-CM-example"
type: "theorem"
title: "finite exponential mixture has inverse branch not completely monotone"
status: "proved"
tags: ["bridge-only", "complete-monotonicity", "counterexample", "inverse-branch", "keady", "proved", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260530T222500-keady-inverse-cm-counterexample.json", "oracle/responses/ORACLE-FI-20260530T-elegance-042-oracle-forage-response.md", "raw/scout/FI-20260530T-elegance-042.md", "raw/student/20260530T222500-keady-inverse-cm-counterexample.md", "wiki/notes/frontier-keady-inverse-cm.md"]
---

# Theorem: finite exponential mixture has inverse branch not completely monotone

## Statement

The strictly completely monotone function \(f(x)=99e^{-x}+e^{-10x}\) maps \((0,\infty)\) decreasingly onto \((0,100)\), but its inverse branch is not completely monotone on \((0,100)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260530T222500-keady-inverse-cm-counterexample.json`
- `oracle/responses/ORACLE-FI-20260530T-elegance-042-oracle-forage-response.md`
- `raw/scout/FI-20260530T-elegance-042.md`
- `raw/student/20260530T222500-keady-inverse-cm-counterexample.md`
- `wiki/notes/frontier-keady-inverse-cm.md`

## Proof

For every \(n\ge0\),
\[
(-1)^n f^{(n)}(x)=99e^{-x}+10^n e^{-10x}>0.
\]
Hence \(f\) is strictly completely monotone, and \(f'<0\), so the inverse branch \(g=f^{-1}\) exists.

For \(y=f(x)\), inverse differentiation gives
\[
g'(y)=\frac1{f'(x)},\qquad
g''(y)=-\frac{f''(x)}{(f'(x))^3},
\]
and
\[
g'''(y)=\frac{3(f''(x))^2-f'''(x)f'(x)}{(f'(x))^5}.
\]
At \(x=0+\),
\[
f'(0+)=-109,\qquad f''(0+)=199,\qquad f'''(0+)=-1099.
\]
Therefore
\[
3(f''(0+))^2-f'''(0+)f'(0+)
=3\cdot199^2-(-1099)(-109)
=-988<0.
\]
Since \((f'(0+))^5<0\), this gives
\[
g'''(100-)>0.
\]
By continuity, \(g'''>0\) on a left-neighborhood of \(100\). Complete monotonicity of \(g\) would require \((-1)^3g'''\ge0\), i.e. \(g'''\le0\). This contradiction proves that \(g\) is not completely monotone.

_Proof source: `raw/student/20260530T222500-keady-inverse-cm-counterexample.md`._

## Tags

`bridge-only`, `complete-monotonicity`, `counterexample`, `inverse-branch`, `keady`, `proved`, `theorem`
