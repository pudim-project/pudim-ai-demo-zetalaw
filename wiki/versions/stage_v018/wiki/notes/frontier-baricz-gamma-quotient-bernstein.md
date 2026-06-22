# Frontier Note: Baricz Gamma-Quotient Bernstein Problem

Source: Arpad Baricz, "Turan type inequalities for hypergeometric functions", Proceedings of the American Mathematical Society 136(9), 3223--3229, 2008.

Pudim source/proof note: `raw/student/20260530T212800-baricz-gamma-quotient-counterexample.md`

## Source Problem

The source asks whether, for every \(a,b>0\), the function
\[
x\mapsto
\frac{\Gamma(x)\Gamma(x-a+b)}{\Gamma(x-a)\Gamma(x+b)}
\]
is a Bernstein function on \((a,\infty)\).

## Pudim Resolution

The answer is no. For \(a=2\) and \(b=3\), writing \(y=x-2\) reduces the quotient to
\[
g(y)=\frac{y(y+1)}{(y+3)(y+4)},\qquad y>0.
\]

A Bernstein function must have completely monotone derivative, so \(g'''\ge0\) is necessary. But
\[
g'''(1)=-\frac{1017}{40000}<0.
\]

Therefore the source for-all-\(a,b\) Bernstein assertion is false.

Status:

- `T-Baricz-gamma-quotient-a2b3-not-BF`: true.
- `T-Baricz-gamma-quotient-BF-forall-negative-answer`: true.

This is unrelated to public `APP-0012`, which concerns Baricz's \(V_q\) strict \(q\)-log-convexity.
