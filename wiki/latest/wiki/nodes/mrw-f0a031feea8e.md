---
id: mrw-f0a031feea8e
type: problem
title: Higher-order monotonicity of polygamma products Pn
aliases: ["mrw-f0a031feea8e", "Higher-order monotonicity of polygamma products Pn"]
status: partial
tags: ["scout-forage", "candidate", "partial", "polygamma", "counterexample"]
parents: []
refs: []
---

# Problem: Higher-order monotonicity of polygamma products Pn

## Statement

Problem statement: For \(n\ge 1\), determine convexity, monotonicity, or complete monotonicity properties of
\[
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x).
\]

Literature status: open candidate from the same 2025 polygamma source.  The stronger complete-monotonicity assertion is now locally refuted by [[wiki/nodes/mrw-dee642b8e9cb|Counterexample to complete monotonicity of higher-order polygamma product curvature]], which proves \(P_n'''(2)>0\) for all \(n\ge29\) and also \(P_7^{(6)}(3)<0\).  The \(n=1\) convexity subcase is solved by [[wiki/nodes/mrw-58db958e1bf1|Convexity of the reciprocal trigamma product]].  The full all-\(n\) convexity question remains open.

References:
- Feng Qi, Dongkyu Lim, and Kwara Nantomah, "Monotonicity and positivity of several functions involving ratios and products of polygamma functions", Journal of Inequalities and Applications 2025, article 5. DOI: https://doi.org/10.1186/s13660-024-03245-8

Connection to THEORY: This is a higher-polygamma analogue of partition-function curvature.

Expected difficulty: high.

## Literature Status

Imported from scout-forage response. Open-status evidence and references must be checked before use.

## Connection To Theory

See the candidate block above and the response artifact.

## Source References

- Feng Qi, Dongkyu Lim, and Kwara Nantomah, "Monotonicity and positivity of several functions involving ratios and products of polygamma functions", Journal of Inequalities and Applications 2025, article 5. DOI: https://doi.org/10.1186/s13660-024-03245-8


## Notes

- priority: 5
- status after ingestion: open candidate pending local attack
- sprint 20260518T091402Z update: the stronger claim that \(P_n''\) is completely monotone for all \(n\ge1\) is false.  There is an analytic high-order obstruction \(P_n'''(2)>0\) for all \(n\ge29\), and a lower-order rational interval certificate gives \(P_7^{(6)}(3)<0\).  The weaker convexity question for \(P_n\) is not settled by this counterexample.
- partial resolution: [[wiki/nodes/mrw-dee642b8e9cb|Counterexample to complete monotonicity of higher-order polygamma product curvature]]
- related beta-window resolution: [[wiki/nodes/mrw-f3c6cef2ebb1|Odd-order collapse for polygamma beta windows]] proves the odd-order subfamily of the Qi--Lim--Nantomah higher-polygamma beta-window problem for all real beta parameters.  This is a different source problem from the \(P_n\) convexity/complete-monotonicity question, but it uses the same polygamma product layer.
- sprint 20260518T101945Z update: the \(P_1\) subtarget remains open.  The cycle derived the exact \(T_{p,i,j}\) recurrence for \((P_1'')^{(r)}\), found no sampled sign failure through order \(35\) on a bounded grid, and promoted [[wiki/nodes/mrw-1c9d9f07a4ef|P1 trigamma product complete-monotonicity frontier]] as a partial note.  No theorem was promoted because Oracle was unavailable and the positive-kernel proof remains missing.
- sprint 20260518T110932Z update: the \(P_1\) subtarget remains open.  An order-80 floating-point recurrence screen reported apparent high-order failures, but they were rejected as counterexamples because they lack exact rational interval certification and occur in a cancellation-sensitive regime.  Live Oracle was again blocked in this host session.  The next useful step is an exact interval certificate for one candidate failure or a live Oracle-assisted positive-kernel proof.
- sprint 20260518T120047Z update: the direct \(A_m\)-product exact interval route was tested with outward-rounded dyadic rational intervals using `.math-wiki/calculations/certify_p1_interval.ps1`.  It did not certify the old floating failures; representative enclosures for \(x=20,r=37\), \(x=5,r=43\), \(x=2,r=49\), and \(x=1,r=46\) still straddled zero.  The next certificate attempt should split cancellation by double-series or pole families before bounding, or else use a live Oracle-assisted kernel grouping.
- sprint 20260518T125130Z update: the canonical double-series partial-fraction route was sharpened.  The promoted note [[wiki/nodes/mrw-5a84b7d9f2c1|Pole-family obstruction for the P1 kernel route]] proves that separate integer-pole and reciprocal-pole family positivity is impossible: the relevant families are negative near \(t=0\).  This does not settle \(P_1\), but it quarantines independent pole-family certification and forces cross-family cancellation, renormalization, or a distinct convexity-only proof plan.
- sprint 20260518T142240Z update: the next cross-family pass promoted [[wiki/nodes/mrw-a4339be8da59|Ratio-normal-form reduction for P1 convexity]] and [[wiki/nodes/mrw-58db958e1bf1|Convexity of the reciprocal trigamma product]].  This proves \(P_1''(x)>0\) for all \(x>0\), solving the \(n=1\) convexity subcase.  It does not prove complete monotonicity of \(P_1''\) and does not solve all-\(n\) convexity.
