---
id: "T-incomplete-beta-tail-BF-slice"
type: "theorem"
title: "incomplete beta tail is Bernstein for b positive and lambda between zero and one"
status: "proved"
tags: ["bernstein-function", "bridge-patch", "incomplete-beta", "proved", "source-slice", "theorem"]
parents: []
refs: ["librarian/audits/LA-20260529T-next-loop-incomplete-beta-tail-student.json", "raw/student/20260529T-next-loop-incomplete-beta-tail.md", "wiki/notes/frontier-incomplete-beta-tail-bernstein.md"]
---

# Theorem: incomplete beta tail is Bernstein for b positive and lambda between zero and one

## Statement

For \(b>0\) and \(0<\lambda\le1\), the incomplete-beta tail \(I_{b,\lambda}(x)=B(b,\lambda)-B(b,\lambda;e^{-x})=\int_0^x e^{-bt}(1-e^{-t})^{\lambda-1}\,dt\) is a Bernstein function on \((0,\infty)\).

## Proof and provenance references

- `librarian/audits/LA-20260529T-next-loop-incomplete-beta-tail-student.json`
- `raw/student/20260529T-next-loop-incomplete-beta-tail.md`
- `wiki/notes/frontier-incomplete-beta-tail-bernstein.md`

## Tags

`bernstein-function`, `bridge-patch`, `incomplete-beta`, `proved`, `source-slice`, `theorem`
