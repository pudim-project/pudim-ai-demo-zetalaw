---
id: "T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-740872-to-one-Bernstein"
type: "theorem"
title: "BCG exponential-transition power is not Bernstein on the fixed a2 interval [0.740872,1)"
status: "proved"
tags: ["beghin-cristofaro-garrappa", "bernstein-function", "bernstein-polynomial-certificate", "fixed-line-exclusion", "not-app", "parameter-region-exclusion", "proved", "signed-moment-obstruction", "small-witness-cover", "theorem", "true-negation"]
parents: ["O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold", "T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-740872-750-Bernstein", "L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion"]
refs: ["private Oracle response", "private Oracle response", "private Oracle audit", "private Oracle audit", "private proof note", "private proof note", "theory/nodes/T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-740872-750-Bernstein.json"]
---

# Theorem: BCG exponential-transition power is not Bernstein on the fixed a2 interval [0.740872,1)

## Statement

For every a2 in [92609/125000,1), the function F(s)=s^((2*a2+(3/10)*s)/(s+2)) is not a Bernstein function on (0,infinity).

## Dependencies

- [[wiki/nodes/O-BeghinCristofaroGarrappa-ExpTransitionPowerBF-Threshold|Beghin-Cristofaro-Garrappa exponential-transition power Bernstein threshold]]
- [[wiki/nodes/T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-740872-750-Bernstein|BCG exponential-transition power is not Bernstein on the fixed a2 interval [0.740872,0.75]]]
- [[wiki/nodes/L-BCG-ExpTransitionPowerBF-InverseLaplace-Criterion|BCG exponential-transition power Bernstein inverse-Laplace criterion]]

## Proof and provenance references

- `private Oracle response`
- `private Oracle response`
- `private Oracle audit`
- `private Oracle audit`
- `private proof note`
- `private proof note`
- `theory/nodes/T-not-BCG-ExpTransitionPowerBF-fixed-line-a2-740872-750-Bernstein.json`

## Proof

Floating recurrence diagnostics for the \((2475,700)\) witness gave:

| \(a\) | \(W_{2475}(700;a)\) | \(\partial_a W_{2475}(700;a)\) |
| --- | ---: | ---: |
| 0.750 | \(-4.3888191258350133\cdot 10^{-7}\) | \(-4.917457451678494\cdot 10^{-5}\) |
| 0.760 | \(-9.351780703840947\cdot 10^{-7}\) | \(-5.008002322414627\cdot 10^{-5}\) |
| 0.780 | \(-1.9542314865864135\cdot 10^{-6}\) | \(-5.180629603446106\cdot 10^{-5}\) |
| 0.820 | \(-4.090089391652896\cdot 10^{-6}\) | \(-5.4906536890065784\cdot 10^{-5}\) |
| 0.900 | \(-8.683834966859775\cdot 10^{-6}\) | \(-5.9583831671222194\cdot 10^{-5}\) |
| 1.000 | \(-1.480582221473087\cdot 10^{-5}\) | \(-6.222174803232011\cdot 10^{-5}\) |

Floating diagnostics for the \((4206,1200)\) witness gave:

| \(a\) | \(W_{4206}(1200;a)\) | \(\partial_a W_{4206}(1200;a)\) |
| --- | ---: | ---: |
| 0.750 | \(2.2656244585473487\cdot 10^{-7}\) | \(2.5041151125175606\cdot 10^{-5}\) |
| 0.760 | \(4.793782283490987\cdot 10^{-7}\) | \(2.551976838858589\cdot 10^{-5}\) |
| 0.800 | \(1.5364482634988413\cdot 10^{-6}\) | \(2.7296272694972195\cdot 10^{-5}\) |
| 0.900 | \(4.4485681944421\cdot 10^{-6}\) | \(3.06814795376964\cdot 10^{-5}\) |
| 1.000 | \(7.615212041639484\cdot 10^{-6}\) | \(3.2339918682139764\cdot 10^{-5}\) |

These floating checks suggest both witnesses remain viable above \(3/4\), but this is not a proof.

The \((2475,700)\) recurrence was replayed with directed Decimal interval arithmetic at precision \(60\) on coarse chunks:

\[
[3/4,4/5],\quad [4/5,9/10],\quad [9/10,1].
\]

The resulting intervals were dependency-dominated:

\[
W_{2475}([3/4,4/5])
\subseteq
[-1.4905534401838552\cdot 10^{-4},\,1.4397438088889458\cdot 10^{-4}],
\]
\[
U_{2475}([3/4,4/5])
\subseteq
[-3.6660887258076431\cdot 10^{-4},\,2.6646211500103050\cdot 10^{-4}].
\]

The chunks \([4/5,9/10]\) and \([9/10,1]\) were similarly inconclusive.

A narrower \((2475,700)\) attempt at precision \(75\) on
\[
[3/4,19/25]
\]
also crossed zero:
\[
U_{2475}([3/4,19/25])
\subseteq
[-1.1080801902479763\cdot 10^{-4},\,1.1779087627033193\cdot 10^{-5}].
\]

The \((4206,1200)\) recurrence was then tested at precision \(70\) on
\[
[3/4,19/25],\quad [19/25,39/50],\quad [39/50,4/5].
\]
These were also dependency-dominated. For example:
\[
W_{4206}([3/4,19/25])
\subseteq
[-1.6460928595037090\cdot 10^{-5},\,1.7243276574780258\cdot 10^{-5}],
\]
\[
U_{4206}([3/4,19/25])
\subseteq
[-1.1643782850182242\cdot 10^{-5},\,6.2073542224222220\cdot 10^{-5}].
\]

_Proof source: `private proof note`._

## Do not claim

- Do not claim the full BCG Bernstein threshold is solved.
- Do not claim APP status.
- Do not claim relaxation nonnegativity or monotonicity failure from this Bernstein obstruction alone.
- Do not extend below 92609/125000 or away from the fixed line (a1,c)=(3/10,2) without a separate certificate.

## Tags

`beghin-cristofaro-garrappa`, `bernstein-function`, `bernstein-polynomial-certificate`, `fixed-line-exclusion`, `not-app`, `parameter-region-exclusion`, `proved`, `signed-moment-obstruction`, `small-witness-cover`, `theorem`, `true-negation`
