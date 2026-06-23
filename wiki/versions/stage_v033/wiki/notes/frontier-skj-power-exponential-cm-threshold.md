# Frontier: Power-Exponential Complete-Monotonicity Threshold

## Source

Shemyakova, Khashin, and Jeffrey, "A conjecture concerning a completely monotonic function", Computers & Mathematics with Applications 60(5), 1360--1363, 2010.

Source URL: https://www.sciencedirect.com/science/article/pii/S0898122110004311

Open-access mirror: https://arxiv.org/abs/1006.1374

The source recalls an Alzer--Berg open problem: determine the values of \(a\) for which
\[
H_a(x)=e^a-\left(1+\frac{a}{x}\right)^x
\]
is completely monotonic on \((0,\infty)\). It records that \(H_1\) is completely monotonic and \(H_3\) is not, and presents numerical evidence for a threshold near
\[
a_c\approx2.299656443.
\]

## Domain Fit

This is a complete-monotonicity problem in the Bernstein--Widder/Laplace-transform domain, with different authors and a different function family from the recent zeta-tail, Gamma-rational, Nielsen beta, Qi/Nantomah, and Kilbas--Saigo branches.

It can grow the current Theory in two useful ways:

- a parameter-threshold framework for complete monotonicity;
- deterministic derivative-recursion and finite-obstruction certificates for functions of the form \(e^a-\exp(x\log(1+a/x))\).

## Attack Policy

Do not attempt to numerically reproduce \(10^5\)-order derivative tables. The first Student pass should prove low-cost structural gates:

- endpoint behavior at \(x\to0^+\) and \(x\to\infty\);
- the first derivative sign for \(a>0\);
- a recurrence for \((-1)^n\partial_x^nH_a(x)\) suitable for later interval certificates.

If a clean Laplace-density representation or nontrivial certified interval \(1<a\le A\) does not appear quickly, rotate again.

## Student Structural Outcome

The bounded Student pass proved the basic structural gates for \(a>0\). Since
\[
x\log\left(1+\frac{a}{x}\right)<a,
\]
one has \(H_a(x)>0\) on \((0,\infty)\). Moreover,
\[
\lim_{x\to0^+}H_a(x)=e^a-1,
\qquad
H_a(x)=\frac{e^aa^2}{2x}+O(x^{-2})
\quad(x\to\infty).
\]
Writing \(r_a(x)=x\log(1+a/x)\), the identity
\[
r_a'(x)=\log\left(1+\frac{a}{x}\right)-\frac{a}{x+a}>0
\]
gives \(H_a'(x)<0\).

The replayable derivative recurrence is:
\[
p_0=1,\qquad p_{n+1}=p_n'+r_a'p_n,\qquad h_a^{(n)}=h_ap_n,
\]
where \(h_a=(1+a/x)^x\). For \(n\ge1\),
\[
(-1)^nH_a^{(n)}=h_aQ_n,\qquad
Q_1=r_a',\qquad Q_{n+1}=-Q_n'-r_a'Q_n.
\]
This promotes `T-SKJ-Ha-structural-gates-certificate` to true, but the threshold problem remains open.

Two further locally checked helper facts were admitted. First, the logarithmic defect
\[
\delta_a(x)=a-x\log\left(1+\frac{a}{x}\right)
\]
is strictly completely monotonic on \((0,\infty)\). Second, the second derivative gate yields the necessary condition
\[
a\le
T_2:=
\inf_{y>0}
\frac{y^3}{(1+y)^2\left(\log(1+y)-\frac{y}{1+y}\right)^2}.
\]
Only the symbolic obstruction formula is admitted; numerical values for \(T_2\) remain unaudited.

Using Alzer--Berg's theorem that \(H_1(x)=e-(1+1/x)^x\) is a Stieltjes transform, the same Student pass proved a certified interval:
\[
H_a(x)=e^a-(1+a/x)^x
\]
is completely monotonic for every \(0<a\le1\). This follows from
\[
H_a(x)=e^a\left[1-\left(1-\frac{H_1(x/a)}{e}\right)^a\right]
\]
and the positive coefficient expansion of \(1-(1-z)^a\) for \(0<a\le1\). The full SKJ threshold remains open.
