# Frontier Note: Erdos 536 LCM-Triangle Packing

## Status

Partial progress only.  The source problem remains open.

## Source Frontier

Erdos Problem 536 asks whether \(f(N)=o(N)\), where \(f(N)\) is the maximum size of an LCM-triangle-free subset of \([N]\).  The public source records this as open.

The public discussion thread records the three-layer packing bound
\[
f(N)\le\left(\frac{43}{48}+o(1)\right)N.
\]

## Local Patch

The fourth valuation layer
\[
\{11m,13m,143m\}
\]
under
\[
v_2(m)\equiv v_3(m)\equiv0\pmod4,\qquad
v_5(m),v_7(m),v_{11}(m),v_{13}(m)\equiv0\pmod2
\]
is disjoint from the three public layers and contributes density \(1/640\).

Thus the four-layer packing gives
\[
f(N)\le\left(\frac{1717}{1920}+o(1)\right)N.
\]

## Boundary

This is a valuation-residue packing improvement, not a solution of the \(o(N)\) question.  The next useful route would need overlap, entropy, or density-increment structure rather than adding small disjoint layers indefinitely.

## Rolling Loop Update: 20260531T203844

The predecessor-star top-code obstruction from
`T-Erdos536-linear-window-predecessor-star-code-avoids-pushforward` does not
survive full predecessor-window closure. The admitted node
`T-Erdos536-full-predecessor-window-closure-has-forks` proves that every full
rank window
\[
  \{A\subseteq P:m\le |A|\le n\}
\]
contains a union fork whenever \(m<n\le2m\). Thus a linear central window with
all predecessor ranks filled cannot be fork-free. This is only a diagnostic
closure failure: sparse or selectively centered predecessor closures remain
the active obstruction.

Advisor plan `AP-20260531T204249-erdos536-sparse-predecessor-closures` now
targets that sparse obstruction through three routes: dense partial
predecessor-window forks, sparse predecessor-layer mass collapse, and a
diagnostic sparse predecessor-center construction test.

Student execution at `20260531T205129-0300` kept all three routes open and
admitted `T-Erdos536-positive-density-partial-window-alone-does-not-force-fork`.
The sharp EKR star below one occupied top has positive lower-layer density but
no pair covers the top, so the next frontier is below-EKR stability: either
local traces amplify above the EKR threshold, or threshold stars synchronize
their centers enough to force cross-top forks or rank collapse.

Advisor plan `AP-20260531T205526-erdos536-below-ekr-stability` now attacks that
frontier with exactly three routes: super-EKR predecessor-trace amplification,
predecessor EKR-star center synchronization, and a diagnostic below-EKR sparse
top-code construction test.

Student execution at `20260531T210048-0300` kept all three below-EKR routes
open. The missing input is now explicit: a quantified EKR/Hilton-Milner-style
stability theorem for local predecessor traces, plus a cross-top center-entropy
capture theorem. No genuine positive-mass coherent below-EKR construction was
found.
