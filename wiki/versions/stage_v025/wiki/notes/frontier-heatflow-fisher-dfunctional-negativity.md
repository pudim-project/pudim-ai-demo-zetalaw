# Frontier Note: Heat-Flow Fisher \(D[f]\) Negativity

Source: Jiayang Zou, Luyao Fan, Jiayang Gao, and Jia Wang, *A Hexagonal Counterexample to Log-Convexity of Fisher Information Along the Heat Flow*, arXiv:2605.18081.

First-contact records the source-open target with a dimension guard: the source asks whether \(D[f]\) can ever be negative, equivalently whether Fisher information is always convex along heat flow. It records \(D[f]\ge0\) as known in dimensions \(1,2,3,4\), so the live target is \(d\ge5\).

The first Student pass did not solve the source problem. It admitted four route lemmas:

- Log-concave densities satisfy \(D[f]\ge0\).
- \(D\) is additive under product densities, so product lifts from nonnegative factors do not create counterexamples.
- Radial densities reduce \(D\) to an exact one-dimensional integral in \(a=V''\) and \(b=V'/r\).
- A negative torus certificate \(D_T[u]<0\) transfers to a smooth positive Gaussian-decaying Euclidean density by Gaussian envelope.

Status: bridge and route-hygiene only. No APP is solved. The next non-numeric route is to prove a symbolic torus certificate, a uniform simplex expansion, or a radial integral certificate in dimension \(d\ge5\).
