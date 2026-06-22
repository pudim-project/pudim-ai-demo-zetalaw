---
id: "T-YHL-k-digamma-positive-alpha-endpoint-obstruction"
type: "theorem"
title: "positive alpha finite endpoint CM obstruction for weighted k-digamma bracket"
status: "proved"
tags: ["attack-plan", "complete-monotonicity", "endpoint", "k-digamma", "obstruction", "proved", "theorem"]
parents: ["T-Pointwise-obstruction-certificate-principle"]
refs: ["attack-plans/AP-20260528T134000-yhl-k-digamma-weighted-cm.json", "librarian/audits/LA-20260528T135000-yhl-k-digamma-student.json", "raw/student/20260528T134500-yhl-k-digamma-weighted-cm.md", "wiki/notes/frontier-yhl-k-digamma-weighted-cm.md"]
---

# Theorem: positive alpha finite endpoint CM obstruction for weighted k-digamma bracket

## Statement

If \(\alpha>0\) and \(B(x)=\psi_k(ax+b)-k\log(cx+d)\) has a finite right limit at \(0\), then \(x^\alpha B(x)\) can be completely monotonic on \((0,\infty)\) only when it vanishes identically.

## Dependencies

- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `attack-plans/AP-20260528T134000-yhl-k-digamma-weighted-cm.json`
- `librarian/audits/LA-20260528T135000-yhl-k-digamma-student.json`
- `raw/student/20260528T134500-yhl-k-digamma-weighted-cm.md`
- `wiki/notes/frontier-yhl-k-digamma-weighted-cm.md`

## Proof

This is a bounded pass. It records the source-backed \(\alpha=0\) case and proves a positive-\(\alpha\) endpoint obstruction. It does not attempt the full \(\alpha\le0\) parameter classification.

Let
\[
B(x)=\psi_k(ax+b)-k\log(cx+d),
\]
where \(k,a,b,c,d>0\).

Yin--Huang--Lin Theorem 2.2 states that \(B\) is completely monotonic on \((0,\infty)\) if and only if
\[
\mu=kc+ad-bc\le \frac{kc}{2}.
\]

This is admitted as a source-backed base node, not as a newly derived full proof. The same source gives the \(k\)-digamma derivative kernel
\[
\psi_k^{(m)}(x)=(-1)^{m+1}\int_0^\infty \frac{t^m e^{-xt}}{1-e^{-kt}}\,dt,
\]
which places the theorem in the current complete-monotonicity/Laplace-kernel layer.

Fix \(\alpha>0\), and define
\[
F_\alpha(x)=x^\alpha B(x).
\]

Since \(b,d>0\), the bracket has a finite right endpoint value
\[
B(0^+)=\psi_k(b)-k\log d.
\]
Therefore
\[
\lim_{x\to0^+}F_\alpha(x)
=\lim_{x\to0^+}x^\alpha B(x)
=0.
\]

Suppose \(F_\alpha\) is completely monotonic on \((0,\infty)\). Then \(F_\alpha\ge0\) and \(F_\alpha'\le0\), so \(F_\alpha\) is nonincreasing. For any fixed \(y>0\) and any \(0<x<y\),
\[
0\le F_\alpha(y)\le F_\alpha(x).
\]
Letting \(x\to0^+\) gives
\[
0\le F_\alpha(y)\le0.
\]
Thus \(F_\alpha(y)=0\) for every \(y>0\), so \(F_\alpha\equiv0\).

Consequently, for \(\alpha>0\), the weighted function can be completely monotonic only in the degenerate zero case. Under the positive-parameter source assumptions, every nonzero solution of Open Problem 4.1 must therefore lie in \(\alpha\le0\).

The positive-\(\alpha\) branch is exhausted by the endpoint obstruction, and the \(\alpha=0\) branch is covered by the source theorem. The remaining nontrivial frontier is the \(\alpha<0\) singular-weight classification, plus any exact zero-bracket degeneracy.

_Proof source: `raw/student/20260528T134500-yhl-k-digamma-weighted-cm.md`._

## Tags

`attack-plan`, `complete-monotonicity`, `endpoint`, `k-digamma`, `obstruction`, `proved`, `theorem`
