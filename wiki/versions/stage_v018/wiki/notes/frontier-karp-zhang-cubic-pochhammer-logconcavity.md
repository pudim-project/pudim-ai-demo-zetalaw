# Karp--Zhang Cubic Pochhammer Log-Concavity Frontier

## Source

Karp--Zhang, arXiv:2305.09029, state Conjecture 3.8 for the cubic Pochhammer transform
\[
f(\mu;x)=\sum_{n\ge1} f_n\frac{(\mu)_{3n}}{(3n-1)!}x^n.
\]
The forage candidate reports the source as asking whether, when the base sequence \((f_n)\) is log-concave and independent of \(\mu\), the map \(\mu\mapsto f(\mu;x)\) is coefficientwise log-concave.

## Primitive Bait

This is a coefficient-extraction and finite-certificate target.  The exact source statement should be attacked through the generalized Turanian
\[
f(\mu+\alpha;x)f(\mu+\beta;x)-f(\mu;x)f(\mu+\alpha+\beta;x)
\]
and coefficientwise nonnegativity of its \(x^m\)-coefficients.

The useful primitive nodes are determinant/triangular compression, finite-dimensional dual certificates, and coefficient extraction.  A successful proof would teach whether the \(r=3\) boundary admits a reusable triangular positive kernel or whether an exact finite coefficient obstruction exists.

## Gate Status

This is not an APP.  It is an open source-gate target selected from forage 004 because it is exact, primitive-aligned, and non-numeric.  APP status requires Oracle first-contact, Student proof, local audit, novelty confirmation, and bridge integration.
