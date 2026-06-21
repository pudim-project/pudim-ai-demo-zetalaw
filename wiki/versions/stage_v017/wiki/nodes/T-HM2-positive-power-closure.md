---
id: "T-HM2-positive-power-closure"
type: "theorem"
title: "HM2 is closed under powers p at least 1"
status: "proved"
tags: ["HM2", "bondesson-simon", "hyperbolic-monotonicity", "power-closure", "proved", "source-subcase-solved", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "T-M2-power-closure-pge1"]
refs: ["private librarian audit", "private Oracle response", "raw/source-cache/bondesson-simon-1604.05267/STHM5.tex", "private proof note", "wiki/notes/frontier-hm2-power-closure.md"]
---

# Theorem: HM2 is closed under powers p at least 1

## Statement

For Bondesson--Simon finite hyperbolic monotonicity, if \(f\in HM_2\), then \(f^p\in HM_2\) for every \(p\ge1\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/T-M2-power-closure-pge1|M2 cone is closed under positive powers p at least 1]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `raw/source-cache/bondesson-simon-1604.05267/STHM5.tex`
- `private proof note`
- `wiki/notes/frontier-hm2-power-closure.md`

## Proof

For \(k=2\), the source definition of \(M_k\) reduces exactly to:
\[
g\in M_2
\quad\Longleftrightarrow\quad
g\ge0,\quad g\text{ is nonincreasing},\quad g\text{ is convex}.
\]

Let \(g\in M_2\) and \(p\ge1\). The function \(\phi_p(t)=t^p\) is nonnegative, nondecreasing, and convex on \([0,\infty)\). Since \(g\ge0\), the composition \(g^p=\phi_p\circ g\) is nonnegative. Since \(\phi_p\) is nondecreasing and \(g\) is nonincreasing, \(g^p\) is nonincreasing. Since \(\phi_p\) is convex and nondecreasing, and \(g\) is convex, \(\phi_p\circ g\) is convex. Hence
\[
g\in M_2,\ p\ge1 \quad\Longrightarrow\quad g^p\in M_2.
\]

Now suppose \(f\in HM_2\). For every \(u>0\),
\[
g_u(w)=f(uv)f(uv^{-1}),\qquad w=v+v^{-1},
\]
belongs to \(M_2\). Therefore \(g_u^p\in M_2\). But
\[
g_u(w)^p
=f(uv)^p f(uv^{-1})^p
=(f^p)(uv)(f^p)(uv^{-1}).
\]
Thus the defining \(HM_2\) condition holds for \(f^p\).

the M2 power closure pge1: true elementary cone-closure lemma.
the HM2 positive power closure: true solved source subcase.
the BS HMk positive power closure kge3 open: open remaining frontier.

Do not claim \(\widehat{HM}_2\) or the full \(HM_k\) result. This is not public staging.

_Proof source: `private proof note`._

## Tags

`HM2`, `bondesson-simon`, `hyperbolic-monotonicity`, `power-closure`, `proved`, `source-subcase-solved`, `theorem`
