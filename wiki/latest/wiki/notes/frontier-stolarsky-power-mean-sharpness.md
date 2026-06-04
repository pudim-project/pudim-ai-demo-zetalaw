# Frontier Note: Stolarsky Power-Mean Bernstein Sharpness

## Source

Adam Bessenyei, "On complete monotonicity of some functions related to means", Mathematical Inequalities and Applications 16 (2013), 233--239.

Source PDF: https://abesenyei.web.elte.hu/publications/compmon.pdf

## Public Source Problem

The source records the Chen--Qi question asking what can be said about complete monotonicity of derivatives of shifted Stolarsky means:
\[
x\mapsto S_{p,q}(x+s,x+t).
\]
Equivalently, in the terminology used by the local Theory, the question asks for Bernstein-function behavior of shifted means.

## Local Bounded Target

Bessenyei proves a positive range that includes shifted power means
\[
H_p(a,b)=\left(\frac{a^p+b^p}{2}\right)^{1/p}
\]
for \(-1\le p\le1\). The local target is the complementary obstruction for the all-shifts extension beyond \(p=1\):
\[
p>1,\ a\ne b
\quad\Longrightarrow\quad
x\mapsto H_p(x+a,x+b)
\text{ is not Bernstein.}
\]

This is a sharpness result around the power-mean subfamily only. It does not classify all Stolarsky parameters.

## Theory-Growth Role

The proof uses the same endpoint-obstruction principle that has been useful for complete-monotonicity problems: a Bernstein function has a nonincreasing derivative, while the shifted power-mean derivative is eventually increasing when \(p>1\) and the shifts differ.

## Student Outcome

For \(p>1\) and unequal shifts, write \(y=x+(a+b)/2\) and \(d=(a-b)/2\ne0\). The local proof gives the exact curvature certificate
\[
\frac{d^2}{dy^2}H_p(y+d,y-d)>0
\qquad (y>|d|),
\]
with tail expansion
\[
H_p(y+d,y-d)
=y+\frac{(p-1)d^2}{2y}+O(y^{-3}),
\]
and therefore
\[
\frac{d^2}{dy^2}H_p(y+d,y-d)
=\frac{(p-1)d^2}{y^3}+O(y^{-5})>0
\]
as \(y\to\infty\). Since a Bernstein function must have nonpositive second derivative, the \(p>1\) all-shifts power-mean extension is refuted.

## Status

- Source frontier: open.
- Bounded \(p>1\) power-mean obstruction: locally proved.
- Public application label: none.
