---
id: "D-Qi-Convolution-LowerBound-Language"
type: "definition"
title: "Qi log-concave convolution lower-bound language"
status: "proved"
tags: ["convolution", "definition", "log-concavity", "lower-bound", "proved", "qi", "source-vocabulary"]
parents: ["O-Qi-LogConcaveConvolution-LowerBound-source-gate"]
refs: ["librarian/audits/LA-20260613T0348-qi-logconcave-convolution-first-contact.json", "oracle/responses/OFC-20260613Tqi-logconcave-convolution-lowerbound-oracle-first-contact-response.md"]
---

# Definition: Qi log-concave convolution lower-bound language

## Statement

For functions \(f_1,\ldots,f_n\) on \([0,a)\), the convolution is \((f_1*\cdots*f_n)(x)=\int_{t_i\ge0,\sum_{i=1}^{n-1}t_i\le x}\prod_{i=1}^{n-1}f_i(t_i)f_n(x-\sum_{i=1}^{n-1}t_i)\,dt\). Qi's source asks whether logarithmic concavity of all \(f_i\) permits a stronger lower bound than the displayed Beesack--Imoru--Mitrinovic convolution bound.

## Dependencies

- [[wiki/nodes/O-Qi-LogConcaveConvolution-LowerBound-source-gate|Qi log-concave convolution lower-bound sharpness source gate]]

## Proof and provenance references

- `librarian/audits/LA-20260613T0348-qi-logconcave-convolution-first-contact.json`
- `oracle/responses/OFC-20260613Tqi-logconcave-convolution-lowerbound-oracle-first-contact-response.md`

## Tags

`convolution`, `definition`, `log-concavity`, `lower-bound`, `proved`, `qi`, `source-vocabulary`
