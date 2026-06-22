# Frontier Note: Keady Self-Bijection Inverse-CM Counterexample

Status: solved source-fit negative example; not a Stieltjes or special-Robin result.

Keady Question 3 asks whether a completely monotone function mapping \((0,\infty)\) onto itself must have a completely monotone inverse, and asks for an example if not. The local example is
\[
f(x)=\frac1x+100e^{-x}.
\]
It is strictly completely monotone and decreasing, with range \((0,\infty)\). If \(g=f^{-1}\), then
\[
g'''(f(x))=\frac{3(f''(x))^2-f'''(x)f'(x)}{(f'(x))^5}.
\]
At \(x=1/8\), the numerator is negative while the denominator is negative, so \(g'''(f(1/8))>0\). This violates the complete-monotonicity sign requirement \(g'''\le0\).

The earlier finite-range route-kill \(99e^{-x}+e^{-10x}\) remains useful but maps onto \((0,100)\). The singular term \(1/x\) repairs the source's self-range condition while preserving a third-derivative inverse obstruction.

The special inverse branches attached to \(\varphi_1\) and \(\varphi_2\) remain open.
