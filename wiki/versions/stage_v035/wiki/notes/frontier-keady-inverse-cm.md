# Frontier Note: Keady Inverse Complete-Monotonicity Questions

Keady--Wiwatanapataphee--Khajohnsaksumeth work with inverse branches associated to Robin eigenvalue formulae. Their paper records that \(\phi_1\) and \(\phi_2\) are completely monotone and that \(\phi_2\) is Stieltjes, while the complete monotonicity of corresponding inverse branches remains a delicate special question.

The general closure principle is false. The finite exponential mixture
\[
f(x)=99e^{-x}+e^{-10x}
\]
is strictly completely monotone, but its inverse branch on \((0,100)\) is not completely monotone. The obstruction is
\[
g'''(f(x))=\frac{3(f''(x))^2-f'''(x)f'(x)}{(f'(x))^5},
\]
and at \(x=0+\) the numerator is \(-988<0\), while the denominator is negative.

Status: true route-kill/bridge. The special Robin inverse branches remain open.


Status update 2026-05-31: the self-range version of Keady Question 3 is now solved by `T-Keady-self-bijection-inverse-CM-negative-example`. The function
\[
f(x)=x^{-1}+100e^{-x}
\]
maps \((0,\infty)\) onto \((0,\infty)\), and its inverse has \(g'''(f(1/8))>0\). The special Robin inverse branches remain open.
