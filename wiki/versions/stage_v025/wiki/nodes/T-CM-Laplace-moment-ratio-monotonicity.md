---
id: "T-CM-Laplace-moment-ratio-monotonicity"
type: "theorem"
title: "positive Laplace tilted moments imply strict monotonicity of a_{n+1}/(a_n a_{n+2})"
status: "proved"
tags: ["bridge-layer", "complete-monotonicity", "laplace-moments", "moment-log-convexity", "proved", "student", "theorem"]
parents: ["T-Nielsen-k-beta-derivative-ratio-monotonicity"]
refs: ["attack-plans/AP-20260526T140000-Nielsen-k-beta.json", "raw/student/20260526T140500-nielsen-k-beta-moment-ratio.md", "wiki/notes/frontier-nielsen-k-beta-moment-ratio.md"]
---

# Theorem: positive Laplace tilted moments imply strict monotonicity of a_{n+1}/(a_n a_{n+2})

## Statement

Let \(a_j(x)=\int_0^\infty t^j e^{-xt}\,d\mu(t)>0\) be tilted moments of a positive Laplace measure for the needed indices. Then, for every \(n\ge0\), \(B_n(x)=a_{n+1}(x)/(a_n(x)a_{n+2}(x))\) is strictly increasing on its domain.

## Dependencies

- [[wiki/nodes/T-Nielsen-k-beta-derivative-ratio-monotonicity|Nielsen k-beta derivative ratio has parity monotonicity: odd n increasing, even n decreasing]]

## Proof and provenance references

- `attack-plans/AP-20260526T140000-Nielsen-k-beta.json`
- `raw/student/20260526T140500-nielsen-k-beta-moment-ratio.md`
- `wiki/notes/frontier-nielsen-k-beta-moment-ratio.md`

## Tags

`bridge-layer`, `complete-monotonicity`, `laplace-moments`, `moment-log-convexity`, `proved`, `student`, `theorem`
