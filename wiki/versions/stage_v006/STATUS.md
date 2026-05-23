# Status

## Goal Status

20260523T192152Z Advisor heartbeat update: Scout inbox was clear, so no new
Scout candidate changed opportunity cost, route ripeness, growth-forage
priority, or application yield.  The Advisor cycle stayed on the isolated
\(n=2\) exceptional case of Qi--Lim--Nantomah Open Problem 4.

The cycle promoted `mrw-ea265a369095`, proving
\[
\left[\frac{397}{170},3\right]\subseteq\mathcal I_2.
\]
It reuses the Euler--Maclaurin lower gate and certifies
\[
6+6y^{170}+3y^{340}-y^{680}-12y^{57}>0
\qquad(0<y<1)
\]
by exact Sturm count.  The certified \(n=2\) gap is now
\[
\frac{4629}{2000}<L_2\le\frac{397}{170}.
\]
Next work should either attempt one more rational tail-gate target below
\(397/170\) only if the exact certificate remains practical, or pivot to the
derivative-sign equation in `mrw-a3170d192f6c` for the true lower endpoint.

20260523T191151Z Advisor heartbeat update: Scout item
`20260523T190315Z-scout-forage` was audited.  Candidate 1 was
duplicate-reviewed: its Open Problem 3 endpoint obstruction
\(\beta<-1\) is already part of `mrw-0e9002ec3122`, with the sign partition
recorded in `mrw-ef08eba06fbe`.  Candidate 2 reinforced the active exceptional
\(n=2\) Open Problem 4 route; Candidates 3--5 were deferred.

The Advisor cycle promoted `mrw-c3e50abdd2fe`, proving the sharper admissible
subwindow
\[
\left[\frac{257}{110},3\right]\subseteq\mathcal I_2.
\]
It reuses the Euler--Maclaurin lower gate from `mrw-da05add5bca1` and certifies
\[
6+6y^{110}+3y^{220}-y^{440}-12y^{37}>0
\qquad(0<y<1)
\]
by exact Sturm count.  The certified \(n=2\) gap is now
\[
\frac{4629}{2000}<L_2\le\frac{257}{110}.
\]
Next work should either push the same tail-gate certificate lower with a
manageable rational denominator, or switch to the derivative-sign route from
`mrw-a3170d192f6c` to attack the true lower endpoint.

20260523T185221Z Advisor heartbeat update: Scout item
`20260523T184322Z-scout-forage` was audited.  Candidate 1 was reviewed as
duplicate/no-op because the \(C^1\) Gamma-numerator threshold is already
`mrw-6cd7f677ca40` and the self-entropy special cases are already
`mrw-82ac3282a187`.  Candidate 3 reinforced the active route: the exceptional
\(n=2\) beta window in Qi--Lim--Nantomah Open Problem 4.

The Advisor cycle promoted `mrw-da05add5bca1`, proving the sharper admissible
subwindow
\[
\left[\frac{187}{80},3\right]\subseteq\mathcal I_2.
\]
The proof replaces the three-term reciprocal-tail gate with a Bernoulli /
Euler--Maclaurin lower gate:
\[
Z_3(1/x)>
\frac12x^2+\frac12x^3+\frac14x^4-\frac1{12}x^6
\qquad(0<x<1),
\]
then certifies
\[
6+6y^{80}+3y^{160}-y^{320}-12y^{27}>0
\qquad(0<y<1)
\]
by exact Sturm count.  The certified \(n=2\) gap is now
\[
\frac{4629}{2000}<L_2\le\frac{187}{80}.
\]
Next work should either sharpen the tail gate toward the method threshold just
above \(7/3\), or return to the derivative-sign certificate from
`mrw-a3170d192f6c`.

20260523T183816Z Advisor heartbeat update: Scout inbox was clear, so no new
Scout candidate changed opportunity cost, route ripeness, growth-forage
priority, or application yield.  The Advisor cycle consolidated the
Qi--Lim--Nantomah Open Problem 4 route and promoted `mrw-e497f41bfc07`.

The promoted corollary records the solved/exceptional split:
\[
\mathcal I_n=\mathbb R\quad(n\ge1\text{ odd}),
\]
and
\[
\mathcal I_n=[n,n+1]\quad(n\ge4\text{ even}).
\]
Thus Open Problem 4 is solved for every \(n\ge1\) except possibly \(n=2\).
For the exceptional \(n=2\) case, the current certified status remains
\[
\frac{4629}{2000}<L_2\le\frac{19}{8},
\qquad
\left[\frac{19}{8},3\right]\subseteq\mathcal I_2.
\]
The next executable target is the exact \(n=2\) lower endpoint: either sharpen
the sufficient edge below \(19/8\) with a stronger reciprocal-tail certificate,
or certify derivative signs in the localized critical-point bracket.

20260523T182438Z Advisor heartbeat update: Scout item
`20260523T181642Z-scout-forage` was audited.  Candidate 1 was accepted after
local proof audit and promoted as `mrw-fd6576e56da0`; Candidates 2--5 remain
deferred.  Opportunity cost shifted because the item closes an infinite
source-grounded subfamily of Qi--Lim--Nantomah Open Problem 4.  Route ripeness
and application yield are high: odd orders were already solved by
`mrw-f3c6cef2ebb1`, and now even orders \(n\ge4\) are solved exactly.

The new theorem proves that for every even \(n\ge4\),
\[
\mathcal I_n=[n,n+1],
\]
where
\[
\mathcal I_n=\{\beta:x^\beta C_n(x)-P_n(x)<0\text{ for all }x>0\}.
\]
The proof uses the endpoint necessity from `mrw-0241ab931d33`, the reciprocal
tail bound
\[
Z_{n+1}(1/x)>\frac{x^n}{n}\qquad(0<x<1),
\]
and the factorial gap
\[
\frac{(n-1)!}{n}>1\qquad(n\ge4).
\]
The same shortcut fails structurally for \(n=2\), where \((n-1)!/n=1/2\).
Thus Qi--Lim--Nantomah Open Problem 4 is now solved for all \(n\ge1\) except
the even exceptional case \(n=2\).  The next executable target returns to the
\(n=2\) lower envelope, where the current certified gap remains
\[
\frac{4629}{2000}<L_2\le\frac{19}{8}.
\]

20260523T181253Z Advisor heartbeat update: Scout inbox was clear, so no new
Scout candidate changed opportunity cost, route ripeness, growth-forage
priority, or application yield.  The Advisor cycle continued the \(n=2\)
Qi--Lim--Nantomah beta-window route and promoted `mrw-19400778b4b5`, a sharper
explicit admissible subwindow.

The new theorem proves
\[
\left[\frac{19}{8},3\right]\subseteq\mathcal I_2.
\]
It sharpens the prior sufficient interval \([5/2,3]\) by proving the
reciprocal-Hurwitz lower gate
\[
Z_3(1/x)>x^{19/8}\qquad(0<x<1),
\]
using the first three terms of the \(Z_3(1/x)\) sum, a tail integral, and an
exact Sturm certificate for the resulting polynomial inequality.  This is a
global upper-bound improvement for the lower envelope, not the exact endpoint.
The certified gap is now
\[
\frac{4629}{2000}<L_2\le\frac{19}{8}.
\]
Next work should either sharpen the sufficient edge below \(19/8\) using a
tighter reciprocal-tail or denominator-ratio certificate, or return to the
critical-point equation in `mrw-a3170d192f6c` for derivative-sign
certification around the localized maximizer.

20260523T175811Z Advisor heartbeat update: Scout item
`20260523T174843Z-scout-forage` was audited.  Candidate 1 was accepted after
local proof audit and promoted as `mrw-5fabc550bd7d`; Candidates 2--5 remain
deferred.  Opportunity cost shifted materially because the item gives a clean
source-grounded admissible subwindow for Qi--Lim--Nantomah Open Problem 4.
Route ripeness and application yield both increased; growth-forage priority is
now to record this sufficient interval before resuming exact lower-envelope
work.

The promoted theorem proves
\[
\left[\frac52,3\right]\subseteq\mathcal I_2,
\]
where
\[
\mathcal I_2
=
\{\beta:x^\beta(\psi''(x)+x\psi^{(3)}(x))
-\psi''(x)\psi''(1/x)<0\text{ for all }x>0\}.
\]
The local proof uses
\[
3xZ_4(x)-Z_3(x)<2Z_3(x)
\]
and the reciprocal-tail gate
\[
Z_3(1/x)>x^\beta\qquad(5/2\le\beta\le3,\ x>0).
\]
This is not the largest-range solution.  Combined with the current lower
obstruction, the certified lower-envelope gap is
\[
\frac{4629}{2000}<L_2\le\frac52,
\qquad
L_2=\sup_{0<x<1}Q_2(x).
\]
The next executable target is the exact lower endpoint: use the critical-point
equation from `mrw-a3170d192f6c` to certify derivative signs on rational
subintervals, or prove a global outside-bracket upper bound for \(Q_2\).

20260523T174346Z Advisor heartbeat update: Scout inbox was clear, so no new
Scout candidate changed opportunity cost, route ripeness, growth-forage
priority, or application yield.  The Advisor cycle stayed on the \(n=2\)
polygamma lower-envelope route and promoted `mrw-a3170d192f6c`, a proved
critical-point equation for the localized compact maximum.

With
\[
R(x)=
\frac{2Z_3(x)Z_3(1/x)}
{3xZ_4(x)-Z_3(x)}
\]
and
\[
\Lambda(x)=
-\frac{3Z_4(x)}{Z_3(x)}
+\frac{3Z_4(1/x)}{x^2Z_3(1/x)}
-\frac{6Z_4(x)-12xZ_5(x)}
{3xZ_4(x)-Z_3(x)},
\]
there is
\[
\xi\in\left(\frac{1409}{5000},\frac{293}{1000}\right)
\]
such that
\[
Q_2(\xi)>\frac{4629}{2000},
\qquad
\xi\log \xi\,\Lambda(\xi)=\log R(\xi).
\]
This follows from the refined endpoint/interior comparison and Fermat's
theorem.  It is not a uniqueness theorem and not a global lower-endpoint
solution.  The next executable target is to certify signs of
\[
x\log x\,\Lambda(x)-\log R(x)
\]
on rational subintervals of \([1409/5000,293/1000]\), or to prove a global
outside-bracket upper bound for \(Q_2\).

20260523T173540Z Advisor heartbeat update: Scout item
`20260523T172341Z-scout-forage` was audited.  Its claimed Candidate 1,
the admissible-polynomial Gamma-product threshold, was reviewed as a duplicate
of the already-promoted `mrw-e0db175f66fc` and `mrw-6cd7f677ca40`; no Scout
claim was promoted.  Opportunity cost therefore stayed with the \(n=2\)
polygamma lower-envelope branch.  Scout Candidate 3 reinforced route ripeness
and application yield for Qi--Lim--Nantomah Open Problem 4; growth-forage
priority is now beta-window certification rather than more Gamma-only
examples.

The Advisor cycle promoted `mrw-3712cf1c88d8`, a refined compact localization
for the \(n=2\) lower-envelope maximum.  The certified rational comparisons
prove
\[
Q_2(1409/5000)<\frac{4629}{2000}<Q_2(23/80),
\]
and
\[
Q_2(293/1000)<\frac{4629}{2000}<Q_2(23/80).
\]
Thus \(Q_2\) has an interior maximizer on
\([1409/5000,293/1000]\), with value above \(4629/2000\).  This does not
increase the rational lower obstruction, but it narrows the localization from
\([7/25,3/10]\) to \([1409/5000,293/1000]\).  The next useful target is to
turn this bracket into derivative-sign certification on subintervals, or to
prove a global outside-bracket upper bound for \(Q_2\).

20260523T171753Z Advisor heartbeat update: Scout inbox was clear, so no new
Scout candidate changed opportunity cost, route ripeness, growth-forage
priority, or application yield.  The Advisor cycle continued the \(n=2\)
lower-envelope route and promoted `mrw-8c1324a498bf`, a sharper compact
maximum bracket for \(Q_2\).

The certified rational comparisons prove
\[
Q_2(7/25)<\frac{4629}{2000}<Q_2(23/80),
\qquad
Q_2(3/10)<\frac{4629}{2000}<Q_2(23/80).
\]
Therefore \(Q_2\) attains a maximum on \([7/25,3/10]\) at an interior point
\(\xi\in(7/25,3/10)\), with
\[
Q_2(\xi)>\frac{4629}{2000}.
\]
Consequently every admissible \(n=2\) beta parameter satisfies
\[
\beta>\frac{4629}{2000}.
\]
This refines the previous compact bracket \([1/4,1/3]\) to \([7/25,3/10]\)
and improves the certified lower obstruction from \(1157/500\) to
\(4629/2000\).  It is still not a global lower-envelope solution and does not
prove uniqueness of the maximizer.  The next executable target is derivative
sign or interval-monotonicity certification inside \([7/25,3/10]\), or a
global outside-bracket upper bound for \(Q_2\).

20260523T170813Z Advisor heartbeat update: Scout item
`20260523T165716Z-scout-forage` was audited.  Candidate 1 was accepted in
corrected form and promoted as `mrw-6cd7f677ca40`; Candidates 2--5 remain
deferred.  Opportunity cost was low because the proof is a one-dimensional
logarithmic-derivative audit, route-ripeness was high for Gamma threshold
consolidation, growth-forage priority increased for reusable Gamma-product
threshold vocabulary, and application yield is moderate but not a replacement
for the active \(n=2\) polygamma lower-envelope branch.

The promoted proposition says: if \(u:[1,\infty)\to(0,\infty)\) is \(C^1\),
\[
J_u(s)=\frac{u'(s)}{u(s)},\qquad
R_u(s)=\psi^{-1}\!\big(J_u(s)-\psi(s)\big)-s,\qquad
\rho_u=\sup_{s\ge1}R_u(s),
\]
then for \(\rho>-1\),
\[
\frac{u(s)}{\Gamma(s+\rho)\Gamma(s)}
\]
is nonincreasing on \([1,\infty)\) if and only if
\(\rho_u<\infty\) and \(\rho\ge\rho_u\).  If \(\rho>\rho_u\), strict
decrease is automatic.  At \(\rho=\rho_u\), strict decrease is equivalent to
the contact set \(\{s:R_u(s)=\rho_u\}\) containing no nontrivial interval.
This no-flat-contact condition is the necessary correction to the raw Scout
endpoint strictness claim; the earlier polynomial theorem supplies it
automatically by analyticity and asymptotic mismatch.

The terminal Goal remains unresolved.  After the Scout inbox is clear, the
next executable Advisor target returns to `mrw-2a62d2bc84ad`: narrow the
\(n=2\) compact bracket by derivative-sign or interval-monotonicity
certificates, or prove a global upper bound for \(Q_2\) outside
\([1/4,1/3]\).

20260523T164935Z Advisor heartbeat update: Scout inbox was clear, so no new
Scout candidate changed opportunity cost, route ripeness, growth-forage
priority, or application yield.  The Advisor cycle continued the \(n=2\)
lower-envelope route and promoted `mrw-2a62d2bc84ad`, a coarse compact
maximum bracket for \(Q_2\).

The certified rational comparisons prove
\[
Q_2(1/4)<\frac{1157}{500}<Q_2(2/7),
\qquad
Q_2(1/3)<\frac{1157}{500}<Q_2(2/7).
\]
Therefore \(Q_2\) attains a maximum on \([1/4,1/3]\) at an interior point
\(\xi\in(1/4,1/3)\), with
\[
Q_2(\xi)>\frac{1157}{500}.
\]
Consequently every admissible \(n=2\) beta parameter satisfies
\[
\beta>\frac{1157}{500},
\]
while `mrw-201bbda2c917` still gives the admissible right endpoint
\(\beta=3\).  This improves the certified necessary enclosure to
\[
\frac{1157}{500}<\beta\le3,
\]
but it is not a global lower-envelope solution and does not prove uniqueness
of the maximizer.

20260523T164412Z late Scout audit: a new Scout item
`20260523T163715Z-scout-forage` appeared during the final checks of the
Advisor heartbeat.  Candidate 1 was accepted after local proof audit and
promoted as `mrw-82ac3282a187`; Candidates 2--5 remain deferred.  The accepted
claim is application-adjacent Gamma threshold growth, not a replacement for
the active \(n=2\) lower-envelope branch.

For \(c\in\mathbb R\), \(\rho>-1\), and
\[
\Phi_{\rho,c}(s)=\frac{e^{-cs}s^s}{\Gamma(s+\rho)\Gamma(s)},
\qquad s\ge1,
\]
the exact threshold is
\[
\Phi_{\rho,c}\text{ strictly decreases on }[1,\infty)
\Longleftrightarrow
\psi(1+\rho)\ge\gamma+1-c.
\]
The proof is endpoint-controlled: the derivative of
\[
\psi(s+\rho)+\psi(s)-\log s-1+c
\]
is positive on \([1,\infty)\) because \(\psi'(s)>1/s\).  This closes the
source's \(s^s\) and \((s/e)^s\) numerator examples with necessity and
endpoint inclusion; it does not solve the separate extended Gamma-ratio
minimum problem.

20260523T163811Z Advisor heartbeat update: Scout inbox was clear, so no new
Scout candidate changed opportunity cost, route ripeness, growth-forage
priority, or application yield.  The Advisor cycle continued the \(n=2\)
lower-envelope target left by `mrw-201bbda2c917`.

The new promoted corollary `mrw-30f9a055fa9a` gives a certified rational
point obstruction at \(x=2/7\).  For
\[
Q_2(x)=\frac{\log(P_2(x)/C_2(x))}{\log x},
\]
exact rational tail bounds for the Hurwitz-zeta sums at \(x=2/7\) prove
\[
Q_2(2/7)>\frac{231}{100}.
\]
Hence every admissible \(n=2\) beta parameter must satisfy
\[
\beta>\frac{231}{100}.
\]
Combined with the right-endpoint theorem, the current certified enclosure is
\[
\frac{231}{100}<\beta\le3,
\]
and \(\beta=3\) is known to be admissible.  This still does not identify the
exact lower endpoint \(L_2=\sup_{0<x<1}Q_2(x)\); it is a validated pointwise
lower-envelope obstruction and a reusable interval-certificate template.

20260523T162751Z Advisor heartbeat update: Scout item
`20260523T161710Z-scout-forage` returned after the prior scaffold audit and
was re-audited.  Candidate 1 was accepted after local proof audit; Candidates
2--5 remain deferred as future forage/context.  The accepted Candidate 1
changed opportunity cost and route ripeness materially: the even-order
Qi--Lim--Nantomah beta-window branch no longer needs an \(x>1\) upper-envelope
attack.

The new promoted theorem `mrw-201bbda2c917` proves the right endpoint theorem
for every even order.  For even \(n\ge2\), with
\[
C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x),
\qquad
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x),
\]
one has
\[
x^{n+1}C_n(x)-P_n(x)<0\qquad(x>0).
\]
Thus \(\beta=n+1\) is admissible.  Combined with the earlier envelope
reduction, the even-order admissible set is now exactly
\[
\mathcal I_n
=
\left\{\beta\in\mathbb R:
\beta>Q_n(x)\text{ for every }0<x<1
\right\}
\cap(-\infty,n+1],
\qquad
Q_n(x)=\frac{\log(P_n(x)/C_n(x))}{\log x}.
\]
For \(n=2\), this proves the exact right endpoint \(\beta=3\), while the
lower scalar envelope on \(0<x<1\) remains unresolved.  Together with
`mrw-f27a36284da5`, every admissible \(n=2\) parameter must satisfy
\[
\beta>\lambda_{2,1/2}\approx2.2286936706,
\qquad
\beta\le3,
\]
and \(\beta=3\) is now known to work.  This is source-grounded
polygamma theory-growth, not public staging and not terminal Erdos #536
evidence.

20260523T161748Z Advisor heartbeat update: Scout item
`20260523T161710Z-scout-forage` was audited and marked blocked/no-op because
it was only a request-created scaffold with no candidates, nutrients, solution,
or patch.  No Scout claim was imported, so there was no opportunity-cost,
route-ripeness, growth-forage, or application-yield change from Scout.

The Advisor cycle then promoted `mrw-f27a36284da5`, a proved dyadic lower
obstruction for the \(n=2\) polygamma beta window.  For
\[
C_2(x)=\psi''(x)+x\psi^{(3)}(x),\qquad
P_2(x)=\psi''(x)\psi''(1/x),
\]
the exact \(x=1/2\) ratio is
\[
\frac{P_2(1/2)}{C_2(1/2)}
=
\frac{56\zeta(3)(\zeta(3)-1)}{\pi^4-28\zeta(3)}.
\]
Therefore any admissible \(\beta\) satisfies
\[
\beta>\lambda_{2,1/2}
:=
\frac{
\log\!\left(
\frac{56\zeta(3)(\zeta(3)-1)}{\pi^4-28\zeta(3)}
\right)}
{\log(1/2)}
\approx2.2286936706.
\]
The proof also gives \(\lambda_{2,1/2}>2\) by elementary bounds
\(\zeta(3)<121/100\) and \(\pi>31/10\).  Combining this with the prior
upper endpoint gives the necessary restriction
\[
\lambda_{2,1/2}<\beta\le3.
\]
This is still not a solution of the \(n=2\) even-order beta window; it is a
certified pointwise lower obstruction.  The next executable target is global
scalar-envelope certification for \(Q_2\), with no claim that all
\(\beta\in(\lambda_{2,1/2},3]\) work.

20260523T160802Z Advisor heartbeat update: Scout item
`20260523T155709Z-scout-forage` was audited after its response arrived.
Candidate 1 was accepted only as endpoint-barrier material.  The general
necessary even-order interval \(n\le\beta\le n+1\) had already been promoted
as `mrw-0241ab931d33`; the new promoted corollary `mrw-8a146667d25b` proves
the \(n=2\) left endpoint is excluded.  For
\[
C_2(x)=\psi''(x)+x\psi^{(3)}(x),\qquad
P_2(x)=\psi''(x)\psi''(1/x),
\]
the endpoint asymptotics give
\[
C_2(x)=4x^{-3}(1+o(1)),\qquad P_2(x)=2x^{-1}(1+o(1))
\]
as \(x\to0^+\).  Hence
\[
\frac{x^2C_2(x)}{P_2(x)}\to2>1,
\]
so \(x^2C_2(x)-P_2(x)>0\) for sufficiently small \(x\), and \(\beta=2\) is
not admissible.  Thus any admissible \(n=2\) parameter must satisfy
\[
2<\beta\le3.
\]
This is still not a solution of the \(n=2\) even-order beta window; it is an
endpoint obstruction.  The remaining target is scalar-envelope certification
inside \((2,3]\).  Scout Candidates 2--5 remain deferred.  This is
source-grounded polygamma theory-growth, not public staging and not terminal
Erdos #536 evidence.

20260523T155807Z Advisor heartbeat update: Scout inbox was clear at cycle
start, so the cycle continued the higher-polygamma beta-window branch opened by
`mrw-f3c6cef2ebb1`.  The new proved proposition `mrw-0241ab931d33` reduces
the even-order subfamily to a scalar-envelope problem.  For even \(n\ge2\),
with
\[
C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x),\qquad
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x),
\]
the prior sign-driver theorem gives \(C_n(x)>0\) and \(P_n(x)>0\).  Therefore
the admissible set for
\[
x^\beta C_n(x)-P_n(x)<0\qquad(x>0)
\]
is exactly the pointwise envelope condition
\[
\beta>Q_n(x)\quad(0<x<1),\qquad
\beta<Q_n(x)\quad(x>1),
\]
where
\[
Q_n(x)=\frac{\log(P_n(x)/C_n(x))}{\log x}.
\]
The point \(x=1\) imposes no restriction, and endpoint asymptotics prove
\[
\lim_{x\to0^+}Q_n(x)=n,\qquad
\lim_{x\to\infty}Q_n(x)=n+1,
\]
so every admissible \(\beta\) lies in \([n,n+1]\).  This is a reduction and
endpoint-pressure theorem, not a solution of the even-order range; the next
target is to certify the lower and upper scalar envelopes, especially for
\(n=2\).  During final checks, a new Scout item
`20260523T155709Z-scout-forage` appeared, but it was only a request-created
placeholder with no returned candidates, nutrients, solution, or patch; it was
marked blocked/no-op and no Scout claim was imported.  This remains
source-grounded polygamma theory-growth, not public staging and not terminal
Erdos #536 evidence.

20260523T154852Z Advisor heartbeat update: Scout item
`20260523T153713Z-scout-forage` was re-audited after its response arrived.
Candidate 1 was accepted with a local proof replacement and promoted as
`mrw-f3c6cef2ebb1`, a proved theorem on the odd-order subfamily of the
Qi--Lim--Nantomah higher-polygamma beta-window problem.  For \(n\ge1\), with
\[
C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x),
\qquad
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x),
\]
the local proof gives
\[
(-1)^nC_n(x)>0\qquad(x>0).
\]
It proves this directly from the Hurwitz-zeta inequality
\[
\sum_{k=0}^{\infty}(x+k)^{-s}
<
s x\sum_{k=0}^{\infty}(x+k)^{-s-1}
\qquad(s\ge2),
\]
using a tail-sum/integral-comparison argument, not Scout's external ratio
theorem.  Therefore, for every odd \(n\ge1\), \(C_n(x)<0\) and \(P_n(x)>0\),
so
\[
x^\beta C_n(x)-P_n(x)<0
\]
for every \(x>0\) and every \(\beta\in\mathbb R\).  Thus the admissible
parameter range in the odd-order subfamily is all of \(\mathbb R\).  Scout
Candidates 2--5 remain deferred; Candidate 2 overlaps the existing
reciprocal-digamma scalar-envelope branch.  This is source-grounded
polygamma theory-growth, not public staging and not terminal Erdos #536
evidence.

20260523T153832Z Advisor heartbeat update: Scout inbox item
`20260523T153713Z-scout-forage` was audited and marked blocked/no-op because
it was only a request-created scaffold with no returned candidates, nutrients,
solution, or patch.  No Scout claim was imported.  The Advisor cycle then
continued the prior reciprocal-digamma beta-window branch and promoted
`mrw-ef08eba06fbe`, a proved sign-partition proposition.  If
\[
A(x)=\psi(x)+x\psi'(x),\qquad B(x)=\psi(x)\psi(1/x),
\]
then \(A\) has a unique zero \(\eta_A\), \(\psi\) has a unique positive zero
\(z_\psi\), and with \(a_\psi=1/z_\psi\),
\[
0<\eta_A<\frac12<a_\psi<1<z_\psi<2.
\]
The only beta-dependent lower constraints for
\[
Q(x)=\frac{\log(B(x)/A(x))}{\log x}
\]
come from \(x\in(0,\eta_A)\cup(1,z_\psi)\), and the only upper constraints
come from \(x\in(a_\psi,1)\).  Thus the remaining exact-range problem is a
scalar-envelope certificate, not a sign-partition problem.  The full
\([-1,\beta_+)\) range remains unproved; the next useful target is to certify
the lower envelope, especially whether \(\sup Q=-1\) on the lower-constraint
intervals, and then the global minimum of \(Q\) on \((a_\psi,1)\).  This is
source-grounded polygamma theory-growth, not public staging and not terminal
Erdos #536 evidence.

20260523T153044Z Advisor heartbeat update: Scout inbox was clear, so the
Advisor audited deferred Scout Candidate 3 from `20260523T151043Z-scout-forage`.
The full Qi--Lim--Nantomah \(\beta_0\)-range is not solved, but the cycle
promoted `mrw-0e9002ec3122`, a proved reduction for the reciprocal-digamma
beta-window problem.  With
\[
A(x)=\psi(x)+x\psi'(x),\qquad
B(x)=\psi(x)\psi(1/x),\qquad
F_\beta(x)=x^\beta A(x)-B(x),
\]
the valid set
\[
\mathcal I=\{\beta:F_\beta(x)>0\text{ for all }x>0\}
\]
is exactly the intersection of pointwise half-line constraints obtained from
\[
Q(x)=\frac{\log(B(x)/A(x))}{\log x}
\]
on the same-sign regions of \(A\) and \(B\), with impossible points
\(A(x)\le0\le B(x)\).  The endpoint asymptotics also prove
\[
\mathcal I\subseteq[-1,\infty),
\]
so every \(\beta<-1\) is ruled out.  A raw numerical orientation found the
candidate upper-envelope value \(Q(x)\approx5.972836863845014\) near
\(x\approx0.7685997597477409\), but this remains raw-only until the sign
partition and global minimum of \(Q\) are certified.  This is partial
source-grounded polygamma theory-growth, not a new public staged application
and not terminal Erdos #536 evidence.

20260523T151830Z Advisor heartbeat update: Scout item
`20260523T151043Z-scout-forage` was audited.  Candidate 1 was accepted after
local proof audit and promoted as `mrw-e0db175f66fc`, a proved theorem on
admissible Gamma numerators.  If \(u\) is a real polynomial satisfying
\[
u(s)>0\qquad(s\ge1),
\]
and
\[
J_u(s)=\frac{u'(s)}{u(s)},\qquad
R_u(s)=\psi^{-1}\!\big(J_u(s)-\psi(s)\big)-s,
\]
then
\[
\rho_u=\max_{s\ge1}R_u(s)
\]
exists, and for every \(\rho>-1\),
\[
\frac{u(s)}{\Gamma(s+\rho)\Gamma(s)}
\]
is strictly decreasing on \([1,\infty)\) if and only if \(\rho\ge\rho_u\).
The proof locally checks compactness, the pointwise logarithmic-derivative
threshold, and strictness via analytic continuation plus the asymptotic
mismatch \(J_u(s)=O(1/s)\) versus
\(\psi(s+\rho)+\psi(s)\sim2\log s\).  The previous \(u_m=s^m+1\) theorem is
now a specialization; the scale and first-order asymptotic nodes remain
special-family estimation tools.  Scout Candidates 2--5 were deferred.  This
is internal theory-growth and Scout-audited source contact, not public staging
and not terminal Erdos #536 evidence.

20260523T150549Z Advisor heartbeat update: `mrw-2b0fbc6dc6db` sharpens the
polynomial Gamma-threshold scale theorem to a first-order logarithmic
asymptotic.  With
\[
J_m(s)=\frac{m s^{m-1}}{s^m+1},
\qquad
R_m(s)=\psi^{-1}\!\big(J_m(s)-\psi(s)\big)-s,
\qquad
\rho_m=\max_{s\ge1}R_m(s),
\]
the proved theorem gives
\[
\log\rho_m=m-\log m+\gamma-1+o(1),
\]
or equivalently
\[
\rho_m=\exp(\gamma-1+o(1))\frac{e^m}{m}.
\]
The proof does not assume uniqueness of the maximizing point.  It reduces
\(\log\rho_m\) to \(\max_s(J_m(s)-\psi(s))+o(1)\), uses the exact maximum
\[
\max_{s\ge1}J_m(s)=(m-1)^{(m-1)/m}
\]
at \(s=(m-1)^{1/m}\), and then uses \(\psi(s)\ge-\gamma\) plus continuity at
\(1\).  Scout inbox was again empty, so no Scout candidate changed
opportunity cost, route ripeness, growth-forage priority, or application
yield.  Oracle was not retried because the immediately prior live audit hit an
OpenAI API quota blocker.  This is internal Gamma theory-growth only, not a
new public staged application and not terminal Erdos #536 evidence.  Future
Gamma work should target maximizer uniqueness or higher-order asymptotics, not
raw numerical threshold tables.

20260523T145745Z Advisor heartbeat update: `mrw-c165b8d5e4e2` is now a
proved Gamma-threshold consolidation theorem.  For the polynomial numerator
branch
\[
\Phi_{\rho,m}(s)=\frac{s^m+1}{\Gamma(s+\rho)\Gamma(s)},
\]
with sharp threshold
\[
\rho_m=\max_{s\ge1}
\left(\psi^{-1}\!\left(\frac{m s^{m-1}}{s^m+1}-\psi(s)\right)-s\right),
\]
the theorem proves the structural scale
\[
\log\rho_m=m-\log m+O(1).
\]
Equivalently \(\rho_m=\exp(O(1))e^m/m\).  This uses the earlier
variational threshold theorem `mrw-37311e7a5a0f`, the support-localization
theorem `mrw-73218406186e`, and elementary digamma logarithmic estimates.
Scout inbox was empty, so no Scout candidate changed opportunity cost, route
ripeness, growth-forage priority, or application yield.  Oracle audit was
attempted but blocked by OpenAI API quota exhaustion; no Oracle claim was
imported.  This is internal theory-growth only: it is not a new staged
application, not public `stage_v004` material, and not terminal Erdos #536
evidence.  Next Advisor cycles should prefer Scout/source-import/growth-forage
unless a fresh ripe-enough certificate justifies Erdos #536 exploit; if the
Gamma polynomial branch is revisited, target uniqueness or sharper asymptotics
rather than raw numerical \(\rho_m\) values.

20260523T133726Z update: `APP-0009` is now logged as an internal application
of the Gamma/free-energy layer.  The source-grounded problem is the
Bulboaca--Zayed sharp reciprocal Gamma-product monotonicity threshold:
\[
\varphi_\rho(s)=\frac{1}{\Gamma(s+\rho)\Gamma(s)},\qquad s\ge1.
\]
Their paper proves sufficiency for \(\rho>\rho_*\), where
\[
\psi(1+\rho_*)=\gamma,
\]
and asks for the smallest positive values.  The local theorem
`mrw-0fd149ddc79d`, now titled as `APP-0009`, proves the exact iff statement:
\[
\varphi_\rho\text{ is strictly decreasing on }[1,\infty)
\quad\Longleftrightarrow\quad
\rho\ge\rho_*.
\]
The new application record is `mrw-0cb4eef49436`, and the internal theory has
been synthesized as `THEORY_v006`.  This is an internal, non-staged update:
public `stage_v004`, root public `APPLICATIONS.md`, GitHub, Gmail, and author
contact remain untouched.

20260523T130642Z update: `mrw-e33925f1a522` proves the fixed-child
obstruction split left by `mrw-7708298f0eb8`.  In the non-child-loss branch,
the fixed endpoint child \(g\) satisfies
\[
D_{\mathcal A,\mathcal C}(g)>\alpha^{-1},
\qquad
\mathfrak D_g=\lambda\mu D_{\mathcal A,\mathcal C}(g)
>\lambda\mu/\alpha.
\]
Writing \(U=B\setminus g\), and for \(h\subseteq U\)
\[
\pi_U(h)=\prod_{u\in h}q_u\prod_{u\notin h}(1-q_u),
\qquad
Q_U(h)=\prod_{u\in h}q_u,
\]
the fixed-child common-core weight factors as
\[
W_g=\sum_{h\subseteq U}\pi_U(h)Q_U(h)a_hc_h.
\]
Thus for \(0<\rho<\tau\le1\), either the active outside cores
\[
E_\rho(g)=\{h:a_hc_h>0,\ Q_U(h)\ge\rho\}
\]
have product mass
\[
\pi_U(E_\rho(g))\ge\tau-\rho,
\]
or there is an active covering pair \(x\cup y=g\) with
\[
\prod_{b\in x\triangle y}q_b<\tau/\mathfrak D_g
<\alpha\tau/(\lambda\mu).
\]
With the optional common-core cover cap \(C_g\le c\), this improves to
\[
\prod_{b\in x\triangle y}q_b<c\tau/\mathfrak D_g.
\]
In the prime-biased case \(q_u=1/u\), the heavy branch gives an active common
core with bounded denominator product
\[
\prod_{u\in h}u\le\rho^{-1}.
\]
Oracle returned `PASS_WITH_EDITS`; the promoted statement incorporates the
required conditional fixed-child phrasing.  This is not terminal Erdos 536
evidence.  The new primary target is the denominator-bounded common-core
branch: classify it as separator/product-tower residual structure, or prove
that many such bounded-core certificates force chargeable endpoint triples and
propagate the \(\eta^2\) third-fiber exclusions.

20260523T122641Z update: `mrw-7708298f0eb8` proves the cross-terminal dyadic
child-loss aggregation theorem.  For a pair-link-free endpoint-fiber union,
distinct terminal parents \(R_1\ne R_2\), endpoint parent fibers
\(\mathcal A=\mathcal E_{R_1}\), \(\mathcal C=\mathcal E_{R_2}\), and
\[
\mathcal T\subseteq I_T(R_1,R_2)\setminus\{R_1,R_2\},
\]
write
\[
M_{\mathcal T}=\sum_{R_3\in\mathcal T}\nu_T(R_3)\pi_B(\mathcal E_{R_3}),
\qquad
\sigma=\pi_B(\mathsf I_B(\mathcal A,\mathcal C)).
\]
For every \(0<\alpha\le1\), either
\[
M_{\mathcal T}\le(1-\alpha)\nu_T(\mathcal T),
\]
or some fixed endpoint child \(g\) has normalized interval-pileup
\[
D_{\mathcal A,\mathcal C}(g)>\alpha^{-1}.
\]
Writing
\[
\mathfrak D_g=\pi_B(\mathcal A)\pi_B(\mathcal C)
D_{\mathcal A,\mathcal C}(g),
\]
the fixed child then has a dyadic inverse-difference band
\[
S_j\ge\frac{\mathfrak D_g}{(J_g+1)2^{j+1}}
>
\frac{\lambda\mu}{\alpha(J_g+1)2^{j+1}},
\]
and, if \(W_g<\tau\), common-core band probability greater than
\[
\frac{\mathfrak D_g}{\tau(J_g+1)2^{j+1}},
\]
plus an active covering pair with
\[
\prod_{b\in x\triangle y}q_b<\tau/\mathfrak D_g.
\]
With the optional cover-probability cap \(C_g\le c\), this improves to
\[
\prod_{b\in x\triangle y}q_b<c\tau/\mathfrak D_g.
\]
In particular, endpoint parent masses \(\lambda,\mu\ge\eta\) give an
\(\eta^2\)-scale terminal child-loss alternative unless a fixed-child
\(W_g\)-heavy or dyadic tiny-difference obstruction remains.  Scout suggested
this packaging theorem and was ingested raw-only; Oracle returned `PASS` on
the local statement.  This is still not terminal Erdos 536 evidence.  The
primary remaining target is to classify the fixed-child obstruction branch:
prove that \(W_g\)-heavy common-core concentration or dyadic tiny-difference
cover concentration is separator/product-tower residual structure, or show
that many such fixed-child certificates propagate into chargeable endpoint
triples.

20260523T114641Z update: `mrw-4210f8220daf` promotes the fixed-child
inverse-difference spectrum split.  Combining `mrw-ce7f13a668ed` with
`mrw-52e62752b165`, the unnormalized fixed-child energy
\[
\mathfrak D_g=\pi_B(\mathcal A)\pi_B(\mathcal C)D_{\mathcal A,\mathcal C}(g)
\]
is exactly the common-core expectation
\[
\mathbb E\left[
\mathbf 1_{X\cup Y=g}\prod_{b\in X\triangle Y}q_b^{-1}
\right]
=
\frac{\mathfrak D_g}{W_g}
\]
when \(W_g>0\), and \(\mathfrak D_g=0\) when \(W_g=0\).  Hence for
\(\mathfrak D_g>0\) and \(\tau>0\), either \(W_g\ge\tau\), or an active
common-core section contains a covering pair with
\[
\prod_{b\in x\triangle y}q_b<\tau/\mathfrak D_g.
\]
The node also extracts a dyadic band \(\mathcal B_j\) with
\[
S_j\ge\frac{\mathfrak D_g}{(J_g+1)2^{j+1}},
\]
and, if \(W_g<\tau\), common-core band probability greater than
\[
\frac{\mathfrak D_g}{\tau(J_g+1)2^{j+1}}.
\]
With ordinary cover probability \(C_g\le c\), the tiny-difference certificate
improves to
\[
\prod_{b\in x\triangle y}q_b<c\tau/\mathfrak D_g.
\]
Oracle accepted the proof after active-denominator and ordered-distinct
boundary edits, which are included in the promoted node.  This is not terminal
evidence: the new target is to aggregate dyadic inverse-difference bands
across children/terminal intervals into chargeable endpoint triples and
\(\eta^2\)-scale third-fiber losses, or classify \(W_g\)-heavy and
tiny-difference concentration as separator/product-tower residual structure.

20260523T110631Z update: `mrw-52e62752b165` resolves the top-cover section
subbranch of the fixed-child pileup normal form into an exact
inverse-difference energy identity.  For a finite product law on \(2^g\),
define
\[
\Delta_g(x,y)
=
\mathbf 1_{x\cup y=g}\prod_{b\in x\triangle y}q_b^{-1}.
\]
Then the kernel from `mrw-ce7f13a668ed` satisfies
\[
\kappa_g(x,y)=\pi_g(x)\pi_g(y)\Delta_g(x,y).
\]
Consequently
\[
K_g(\mathcal P,\mathcal Q)
=
\mathbb E[\Delta_g(X,Y)\mid X\in\mathcal P,\ Y\in\mathcal Q]
\]
for positive-mass sections.  Thus high top-cover density extracts a covering
pair with large inverse symmetric-difference weight.  More sharply, if the
ordinary conditional cover probability is at most \(c\) and
\(K_g(\mathcal P,\mathcal Q)>L>0\), then some covering pair has
\[
\prod_{b\in x\triangle y}q_b<c/L.
\]
The ordered distinct repeated-parent version holds with the ordered distinct
conditional law.  Combining with `mrw-ce7f13a668ed`, fixed-child high pileup
now either has large ratio-weighted common-core mass or gives an
inverse-difference cover certificate.  Scout independently returned this
identity as its first candidate solution and was ingested raw-only; Oracle
accepted the proof after threshold and ordered-distinct boundary corrections.
This is not terminal evidence: the next obstruction is to aggregate many
inverse-difference certificates into chargeable endpoint triples and
\(\eta^2\)-scale third-fiber exclusions, or classify the remaining
common-core/tiny-difference branch as separator/product-tower residual
structure.

20260523T102630Z update: `mrw-ce7f13a668ed` gives a fixed-child normal form for
the high-pileup obstruction produced by `mrw-8d6210a920bc`.  Fix
\(g\subseteq B\) and put \(U=B\setminus g\).  Every ordered endpoint pair
\((a,c)\) with \(g\in I_B(a,c)\) has the unique form
\[
a=h\cup x,\qquad c=h\cup y,\qquad h\subseteq U,\quad x,y\subseteq g,\quad
x\cup y=g.
\]
For this representation,
\[
\frac{\pi_B(a)\pi_B(c)}{\pi_B(I_B(a,c))}
=
\omega_U(h)\kappa_g(x,y),
\]
where
\[
\omega_U(h)=\prod_{u\in h}q_u^2\prod_{u\in U\setminus h}(1-q_u)
\]
and
\[
\kappa_g(x,y)=\mathbf 1_{x\cup y=g}
\prod_{b\in x\cap y}q_b^2
\prod_{b\in g\setminus(x\cap y)}(1-q_b).
\]
Thus
\[
\lambda\mu D_{\mathcal A,\mathcal C}(g)
=
\sum_{h\subseteq U}\omega_U(h)\Phi_g(\mathcal A_h,\mathcal C_h).
\]
With
\[
W_g=\sum_h\omega_U(h)\pi_g(\mathcal A_h)\pi_g(\mathcal C_h),
\]
one has \(W_g=0\Rightarrow D_{\mathcal A,\mathcal C}(g)=0\), and otherwise
\[
D_{\mathcal A,\mathcal C}(g)=\frac{W_g}{\lambda\mu}\mathbb E[K_H].
\]
Hence if \(D_{\mathcal A,\mathcal C}(g)\ge L>0\), then for every
\(0<\rho\le1\) either \(W_g\ge\rho\lambda\mu\), or some outside-core section
has top-cover density \(K_h>L/\rho\).  The ordered distinct repeated-parent
version holds with \(D_{\mathcal A}^{\ne}\), \(Z_{\mathcal A}\), and
\(\Phi_g^{\ne}\).  Oracle accepted the proof after correcting the weighted
average and clarifying that \(W_g\) is ratio-weighted common-core mass, not an
ordinary pair probability.  Scout remained a scaffold and was ingested
raw-only.  This is not terminal evidence: the next obstruction is either
ratio-weighted common-core/separator mass or high top-cover section pileup.

20260523T094630Z update: `mrw-8d6210a920bc` turns the diffuse endpoint-shadow
branch into an exact normalized pileup alternative.  For finite full-support
endpoint product laws, endpoint families \(\mathcal A,\mathcal C\) of positive
masses \(\lambda,\mu\) define
\[
D_{\mathcal A,\mathcal C}(g)
=
\frac{1}{\lambda\mu}
\sum_{\substack{a\in\mathcal A,\ c\in\mathcal C\\ g\in I_B(a,c)}}
\frac{\pi_B(a)\pi_B(c)}{\pi_B(I_B(a,c))}.
\]
This is a \(\pi_B\)-probability density with exact support
\(\mathsf I_B(\mathcal A,\mathcal C)\).  Thus \(D_{\mathcal A,\mathcal C}\le K\)
with \(K\ge1\) implies
\[
\pi_B(\mathsf I_B(\mathcal A,\mathcal C))\ge K^{-1},
\]
and small endpoint interval shadow forces a point \(g\) with
\(D_{\mathcal A,\mathcal C}(g)>\sigma^{-1}\).  The repeated-parent branch has
the same statement for the ordered-distinct density \(D_{\mathcal A}^{\ne}\)
and \(\mathsf J_B(\mathcal A)\), provided
\[
Z_{\mathcal A}=\sum_{a\ne c\in\mathcal A}\pi_B(a)\pi_B(c)>0.
\]
Combining with `mrw-e64516fca3bd`, bounded pileup gives terminal child loss by
a factor \(1-K^{-1}\).  Oracle accepted the result after the \(K\ge1\),
\(\sigma>0\), exact-support, and zero-multiplicity boundary corrections.
Scout remained a scaffold and was ingested raw-only.  This is not terminal
evidence: unbounded normalized interval-pair pileup is now the next structural
obstruction to classify as interval-shielded product-tower/separator residual
structure, or to convert into chargeable endpoint triples and aggregate
\(\eta^2\)-scale third-fiber exclusions.

20260523T090621Z update: `mrw-6f8a9d8c0ea7` supplies the first endpoint-side
lower bound for the child-shadow loss theorem in the atom-concentrated branch.
For a finite endpoint product law with \(0<q_b<1\),
\[
\pi_B(I_B(a,b))\ge \pi_B(a)\pi_B(b)
\]
for all endpoint atoms \(a,b\subseteq B\).  Hence, if
\(0\le\alpha,\beta\le1\) and relevant endpoint multiplicity fibers contain
atoms of masses at least \(\alpha\) and \(\beta\), then the corresponding
endpoint interval shadow has mass at least \(\alpha\beta\).  Combining with
`mrw-e64516fca3bd`, cross-terminal interval children satisfy
\[
\sum_{R_3\in\mathcal C}\nu_T(R_3)\pi_B(\mathcal E_{R_3})
\le
(1-\alpha\beta)\nu_T(\mathcal C),
\]
where \(R_1\ne R_2\) and
\(\mathcal C\subseteq I_T(R_1,R_2)\setminus\{R_1,R_2\}\).  The two endpoint
atoms may be equal in this cross-terminal case.  In the repeated-parent
lower-shadow case, \(\mathcal E_R\) must contain two distinct endpoint atoms
of masses at least \(\alpha,\beta\), giving the analogous
\((1-\alpha\beta)\)-loss for \(\mathcal D\subseteq\{R_0:R_0\subsetneq R\}\).
Oracle accepted the proof after adding \(0\le\alpha,\beta\le1\), allowing
equal cross-terminal endpoint atoms, and retaining distinctness for
\(\mathsf J_B\).  Scout remained a scaffold and was ingested raw-only.  This
is not terminal evidence: if child-shadow charging is weak, the endpoint
multiplicity obstruction must be diffuse, all-atoms-small, interval-shielded,
product-tower-like, or separator residual.  The next target is to prove a
diffuse/non-shielded endpoint interval-shadow lower bound for large active
multiplicity fibers, or classify small endpoint-shadow families as known
residual structures.

20260523T082620Z update: `mrw-e64516fca3bd` converts the structural
cross-\(R\) exclusion into a conditional child-mass loss.  For endpoint
families define
\[
\mathsf I_B(\mathcal A,\mathcal B)
=
\bigcup_{a\in\mathcal A,\ b\in\mathcal B}I_B(a,b),
\qquad
\mathsf J_B(\mathcal A)
=
\bigcup_{\substack{a,b\in\mathcal A\\a\ne b}}I_B(a,b).
\]
If \(R_1\ne R_2\) and
\[
\mathcal C\subseteq I_T(R_1,R_2)\setminus\{R_1,R_2\},
\]
then any pair-link-free endpoint-fiber union satisfies
\[
\sum_{R_3\in\mathcal C}\nu_T(R_3)\pi_B(\mathcal E_{R_3})
\le
\left(1-\pi_B(\mathsf I_B(\mathcal E_{R_1},\mathcal E_{R_2}))\right)
\nu_T(\mathcal C).
\]
For repeated terminal parents, if
\[
\mathcal D\subseteq\{R_0:R_0\subsetneq R\},
\]
then
\[
\sum_{R_0\in\mathcal D}\nu_T(R_0)\pi_B(\mathcal E_{R_0})
\le
\left(1-\pi_B(\mathsf J_B(\mathcal E_R))\right)\nu_T(\mathcal D).
\]
Oracle accepted the corrected form after requiring \(R_1\ne R_2\), replacing
"equivalently" by "in particular" in the \(\sigma\)-forms, and weakening the
full-shadow boundary to zero endpoint-weighted child mass.  Scout remained a
scaffold and was ingested raw-only.  This is conditional charging, not
terminal evidence: it proves mass loss only after an endpoint interval-shadow
lower bound.  The next target is to prove such lower bounds under
diffuse/non-shielded hypotheses, or classify small endpoint-shadow families as
shielded product-tower/separator residual obstructions.

20260523T074620Z update: cross-\(R\) consistency for endpoint multiplicity
fibers is now explicit in `mrw-e3fec03bf987`.  Let
\[
\mathcal F=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal U_e\}
\subseteq2^{B\sqcup T}
\]
be pair-link-free, and set
\[
\mathcal E_R=\{e\in\mathcal E:R\in\mathcal U_e\}.
\]
If \(R_3\in I_T(R_1,R_2)\), then there are no
\[
e_i\in\mathcal E_{R_i}
\]
with \(e_3\in I_B(e_1,e_2)\) for which the pairs
\((e_i,R_i)\) are pairwise distinct.  Hence, if
\(R_1,R_2,R_3\) are pairwise distinct terminal points and
\(R_3\in I_T(R_1,R_2)\), then
\[
\mathcal E_{R_3}\cap I_B(\mathcal E_{R_1},\mathcal E_{R_2})
=\emptyset.
\]
If \(R_0\subsetneq R\), then
\[
\mathcal E_{R_0}
\cap
\bigcup_{\substack{e_1,e_2\in\mathcal E_R\\ e_1\ne e_2}}
I_B(e_1,e_2)
=\emptyset,
\]
and the corresponding one-sided repeated-terminal exclusions hold.  This
recovers the cross-\(R\) endpoint constraints lost by the pointwise
conditioning in `mrw-baa182012831` and sharpens the endpoint-weighted
separator-forest routing in `mrw-d83f21b84e5c`.  Oracle accepted the result;
Scout remained a scaffold and was ingested raw-only.  This is structural, not
terminal evidence.  The next target is a quantitative terminal-interval
shadow theorem: large active endpoint multiplicity over many high-window
terminal points should either force endpoint mass loss through these
cross-\(R\) exclusions, collapse to shielded product-tower/separator residuals,
or propagate the chargeable \(\eta^2\)-scale third-fiber losses.

20260523T070609Z update: endpoint-weighted separator forests now route active
leaf volume in `mrw-d83f21b84e5c`.  For each endpoint pattern \(e\), let
\[
C_e\subseteq T,\qquad
\mathcal V_e\subseteq2^{T\setminus C_e},
\]
and lift
\[
\mathcal U_e=
\{R\subseteq T:R\cap C_e=\emptyset,\ R\cap(T\setminus C_e)\in\mathcal V_e\}.
\]
For \(H=H_h(T)\),
\[
M_H=\sum_e\pi_B(e)\nu_T(\mathcal U_e\cap H)
=
\sum_e\pi_B(e)\Gamma_e
\nu_{T\setminus C_e}(\mathcal V_e\cap H_h(T\setminus C_e)).
\]
Equivalently,
\[
M_H=\sum_{R\in H}\nu_T(R)\pi_B(\mathcal E_R),
\qquad
\mathcal E_R=\{e:R\in\mathcal U_e\}.
\]
If the lifted family is pair-link-free, every \(\mathcal E_R\) is ordinary
endpoint pair-link-free.  Hence \(M_H\ge\eta\tau\), with
\(\tau=\nu_T(H)>0\), forces a pointwise endpoint residual certificate
\[
\pi_B(\mathcal E_R)\ge\eta
\]
for some \(R\in H\).  Under the overlap-accounting hypotheses of
`mrw-0845a9abe5b6` and the empty-atom exclusion \(P_0(B)<\delta\eta\), the
same active mass also gives the existing `mrw-0cbd2c0086d7` alternatives:
either a chargeable triple with common high-window overlap at least
\(\gamma\eta^2\) and third-fiber loss, or a distinct nonchargeable shielded
pair with overlap at least \((1-\gamma-\delta)\eta^2\).  Oracle accepted the
result after making \(\tau>0\) and the non-exclusive summary explicit; Scout
returned only a scaffold and was ingested raw-only.  This is not terminal
evidence.  The next target is to classify large ordinary endpoint
multiplicity fibers together with cross-\(R\) consistency, or propagate the
chargeable third-fiber losses across separator leaves.

20260523T062608Z update: separator trees now have a branch-volume obstruction
in `mrw-a20438d5edf8`.  For each leaf \(\ell\) in a finite separator forest,
write
\[
C_\ell=\bigcup_i Z_{\ell,i},
\qquad
\Gamma_\ell=\prod_{z\in C_\ell}(1-q_z),
\qquad
Q_\ell=\sum_{z\in C_\ell}q_z.
\]
If \(\mathcal V_\ell\subseteq2^{T\setminus C_\ell}\) is the final residual and
\[
\mathcal U_\ell
=
\{R\subseteq T:R\cap C_\ell=\emptyset,\ R\cap(T\setminus C_\ell)\in
\mathcal V_\ell\},
\]
then
\[
\nu_T(\mathcal U_\ell\cap H_h(T))
=
\Gamma_\ell\,
\nu_{T\setminus C_\ell}(\mathcal V_\ell\cap H_h(T\setminus C_\ell)).
\]
Therefore
\[
\nu_T\!\left(\bigcup_\ell\mathcal U_\ell\cap H_h(T)\right)
\le
\sum_\ell\Gamma_\ell\,
\nu_{T\setminus C_\ell}(\mathcal V_\ell\cap H_h(T\setminus C_\ell)).
\]
A lower bound \(Q_\ell\ge L\) on every path only gives an \(e^{-L}\) factor
times the residual leaf-volume budget
\[
B_h(\mathcal L)=
\sum_\ell\nu_{T\setminus C_\ell}(\mathcal V_\ell\cap H_h(T\setminus C_\ell)).
\]
The central-rank example with \(q_t=1/2\), leaves indexed by \(m\)-subsets of
\(T_{2m}\), and separators \(T_{2m}\setminus W\), has union mass at least
\((2m+1)^{-1}\) while every leaf has \(\Gamma_W=2^{-m}\le e^{-m/2}\).  Thus
path intensity alone cannot be the separator-tree contraction.  Oracle
accepted the result with coefficient and leaf-volume clarifications; Scout
returned only a scaffold and was ingested raw-only.  This is not terminal
evidence, and the example is not claimed pair-link-free.  The next target is a
leaf-volume/entropy control theorem for separator forests arising from
pair-link-free endpoint fibers, or an escape theorem forcing chargeable
endpoint interval triples when such control fails.

20260523T054605Z update: finite separator chains now telescope in
`mrw-ff32abc524eb`.  For separator blocks
\[
Z_i\subseteq T_{i-1},
\qquad
T_i=T_{i-1}\setminus Z_i,
\]
set
\[
c_i=\prod_{z\in Z_i}(1-q_z),
\qquad
Q_i=\sum_{z\in Z_i}q_z,
\qquad
\Gamma_i=\prod_{j=1}^i c_j.
\]
The first-hit layers \(E_i\) and avoid-all residual \(U_r\) partition the
terminal core, with
\[
\nu(E_i)=\Gamma_{i-1}(1-c_i)\le\Gamma_{i-1}Q_i,
\qquad
\nu(U_r)=\Gamma_r\le\exp\!\left(-\sum_i Q_i\right),
\]
and
\[
\sum_i\Gamma_{i-1}(1-c_i)=1-\Gamma_r.
\]
Lower branches whose members hit \(Z_i\) inherit the same
\(\Gamma_{i-1}(1-c_i)\) bound in every high-window cutoff, while final
avoid-all residuals factor as
\[
\Gamma_r\,\nu_{T_r}(\mathcal V_r\cap\{|W|>h\})
\]
with no support cutoff shift.  Oracle accepted the result after adding the
induced product-law convention, the \(r=0\) boundary, accumulated-intensity
wording, and the fixed-chain caveat; Scout returned only a scaffold and was
ingested raw-only.  This is not terminal evidence.  The next target is a
separator-tree or escape theorem: persistent low-intensity separator
filtrations must collapse into known product-tower residual structure, or the
family must escape separator form and create chargeable endpoint interval
triples with \(\eta^2\)-scale third-fiber exclusions.

20260523T050601Z update: terminal separator branches now have an explicit
cost dichotomy in `mrw-789506d08385`.  For a separator \(Z\subseteq T\), set
\[
c(Z)=\prod_{z\in Z}(1-q_z),
\qquad
Q(Z)=\sum_{z\in Z}q_z.
\]
If lower terminal parents hit \(Z\) and upper terminal sets avoid \(Z\), then
for every real \(h\),
\[
\nu_T(\mathcal A\cap\{|R|>h\})
\le
1-c(Z)
\le
Q(Z),
\]
while the upper fiber factors as
\[
\nu_T(\mathcal V\cap\{|R|>h\})
=
c(Z)\nu_{T\setminus Z}(\mathcal V^{\setminus Z}\cap\{|W|>h\})
\le e^{-Q(Z)}.
\]
Thus for every \(\lambda>0\), a separator branch is either lower-light
\((Q(Z)<\lambda)\), giving lower terminal mass \(<\lambda\), or upper-costly
\((Q(Z)\ge\lambda)\), giving upper residual coefficient at most
\(e^{-\lambda}\).  In mass-forced form, lower terminal mass at least \(m\)
forces \(Q(Z)\ge m\) and \(c(Z)\le e^{-m}\); with endpoint weight
\(\pi_B(f)>0\), lower endpoint contribution at least \(m\) forces
\[
c(Z)\le\exp(-m/\pi_B(f)).
\]
Oracle accepted the result with wording and boundary clarifications; Scout
returned only a scaffold and was ingested raw-only.  This is not terminal
evidence.  The next target is a separator iteration/contraction theorem:
repeated low-\(Q\) separator reductions must either lose lower/endpoint mass,
collapse into known product-tower residual structure, or escape into
chargeable endpoint interval triples and \(\eta^2\)-scale third-fiber
exclusions.

20260523T042600Z update: the comparable upper mixed-shadow branch now has a
concrete separator residual obstruction in `mrw-58fd4a90babe`.  If
\(P=B\sqcup T\), \(f\subsetneq u\subseteq B\), and terminal families
\(\mathcal A,\mathcal V\subseteq2^T\) admit a separator \(Z\subseteq T\) with
\[
A\cap Z\ne\emptyset\quad(A\in\mathcal A),
\qquad
V\cap Z=\emptyset\quad(V\in\mathcal V),
\]
then terminal pair-link-freeness of both fibers implies that
\[
\{f\cup A:A\in\mathcal A\}
\cup
\{u\cup V:V\in\mathcal V\}
\]
is pair-link-free.  The separator gives the stronger mixed-shadow exclusions
\[
\mathcal A\cap\mathsf J_T(\mathcal V)=\emptyset,
\qquad
\mathcal V\cap I_T(A,V)=\emptyset
\quad(A\in\mathcal A,\ V\in\mathcal V).
\]
Under a terminal product law, the upper fiber factors exactly as a smaller-core
residual:
\[
\nu_T(\mathcal V\cap\{|R|>h\})
=
\left(\prod_{z\in Z}(1-q_z)\right)
\nu_{T\setminus Z}(\mathcal V^{\setminus Z}\cap\{|W|>h\}).
\]
Thus top-union-free cover caps cannot aggregate in general without ruling out
low-cost terminal separators or charging them elsewhere.  Oracle accepted the
result after adding the \(\mathsf J_T\) convention, induced-core notation, and
boundary cases; Scout returned only a scaffold and was ingested raw-only.  This
is not terminal evidence.  The next target is a no-small-separator alternative:
active mass outside separator residuals should force chargeable endpoint
triples with \(\eta^2\)-scale third-fiber exclusions, or else decompose into
known product-tower/residual structures.

20260523T034558Z update: the high-support part of the small-cover branch is
now quarantined in `mrw-0c0cd605a52a`.  For terminal coordinates with
\(0<q_t\le1/2\), set
\[
c_t=q_t(2-q_t)
\]
and let \(c_{(1)}\ge\cdots\ge c_{(|T|)}\).  For
\[
\kappa_m(T)=\prod_{i=1}^m c_{(i)},
\]
every \(U\subseteq T\) with \(|U|\ge m\) satisfies
\[
C_U=\prod_{u\in U}q_u(2-q_u)
\le
\kappa_m(T)
\le
\left(\frac34\right)^m.
\]
Hence for \(h\ge0\), \(m(h)=\lfloor h\rfloor+1\), and
\[
H_h(T)=\{U:|U|>h\},
\]
every \(U\in H_h(T)\) has
\[
\operatorname{cov}^{\ne}_U
\le
C_U
\le
\kappa_{m(h)}(T)
\le
\left(\frac34\right)^{m(h)}
\]
unless \(H_h(T)\) is empty.  In the prime-biased case \(q_p=1/p\),
\[
\kappa_m(T)\le\frac{2^m}{(m+1)!}\to0
\]
uniformly over finite prime sets with at least \(m\) elements.  Thus in
growing high-support windows, tiny cover atom is automatic rather than
exceptional: a single lower parent can force at most
\[
1-\sqrt{1-\kappa_{m(h)}(T)}
\]
upper-fiber loss through the cover cap of `mrw-9077aa1c34bc`.  Oracle accepted
the result after adding the empty-window clause and the \((3/4)^m\) bound;
Scout returned only a scaffold and was ingested raw-only.  This is not terminal
evidence.  The next target is to aggregate cover caps across many lower
parents, use chargeable \(\eta^2\)-scale third-fiber exclusions, or classify the
remaining high-support tiny-cover branch as residual/product structure.

20260523T030557Z update: the small-cover branch left by
`mrw-9077aa1c34bc` is now classified locally in `mrw-7273d9801756`.  For a
nonempty terminal block \(U\) with \(0<q_u\le1/2\), write
\[
a_U=\prod_{u\in U}q_u,
\qquad
C_U=\prod_{u\in U}q_u(2-q_u).
\]
Then
\[
\operatorname{cov}^{\ne}_U
=
C_U-a_U^2
=
a_U\left(\prod_{u\in U}(2-q_u)-a_U\right),
\]
and
\[
a_U\le \operatorname{cov}^{\ne}_U\le C_U\le2^{|U|}a_U,
\qquad
\frac23C_U\le\operatorname{cov}^{\ne}_U\le C_U.
\]
Thus
\[
\operatorname{cov}^{\ne}_U<\varepsilon
\quad\Longrightarrow\quad
C_U<\frac32\varepsilon,\quad
a_U<\varepsilon,\quad
\sum_{u\in U}-\log q_u>\log\frac1\varepsilon.
\]
Small distinct-cover probability is therefore terminal cover-atom/all-present
atom rarity, except for the explicitly excluded empty-block boundary.  If
\(|U|\le K\), it also forces \(\min_{u\in U}q_u<\varepsilon^{1/K}\); without a
support-size bound this coordinate conclusion is false.  Combining with
`mrw-9077aa1c34bc`, lower parents with \(C_U\ge\varepsilon\) cap the upper
fiber by \(\sqrt{1-2\varepsilon/3}\), and lower parents with
\(a_U\ge\varepsilon\) cap it by \(\sqrt{1-\varepsilon}\).  Oracle suggested
the cover-atom tightening; Scout returned only a scaffold and was ingested
raw-only.  This is not terminal evidence.  The next target is to classify
tiny-cover-atom lower parents in the active prime-biased high-window regime,
or aggregate the cover caps across many non-tiny lower parents.

20260523T022551Z update: the sectionwise top-union-free branch now has a
product-measure cap in `mrw-9077aa1c34bc`.  For a fixed terminal block
\(U\) with product law \(\mu_U\), define the distinct-cover probability
\[
\operatorname{cov}^{\ne}_U
=
\mu_U^{\otimes2}\{(X,Y):X\cup Y=U,\ X\ne Y\}
=
\prod_{u\in U}(2q_u-q_u^2)
-
\left(\prod_{u\in U}q_u\right)^2.
\]
Every top-union-free section \(\mathcal S\subseteq2^U\) satisfies
\[
\mu_U(\mathcal S)\le\sqrt{1-\operatorname{cov}^{\ne}_U}.
\]
Consequently, if every \(U\)-section of \(\mathcal V\subseteq2^T\) is
top-union-free, then every subfamily \(\mathcal W\subseteq\mathcal V\),
including arbitrary high-window subfamilies, has
\[
\mu_T(\mathcal W)\le\sqrt{1-\operatorname{cov}^{\ne}_U}.
\]
In the comparable endpoint branch \(f\subsetneq u\), a fixed lower parent
\(U\in\mathcal R_f\) therefore charges the upper fiber \(\mathcal R_u\) by this
cover-probability loss.  Oracle accepted the proposition with only notational
clarification; Scout returned only a scaffold and was ingested raw-only.  This
is still not terminal evidence: when \(\operatorname{cov}^{\ne}_U\) is tiny,
the upper mixed-shadow branch remains active and should be classified as
residual/product structure rather than treated as decay.

20260523T014542Z update: the comparable upper mixed-shadow branch from
`mrw-740b9e5c6cff` is now reduced to a sectionwise top-union-free problem in
`mrw-dda277c43571`.  For \(A\subseteq T\), \(\mathcal V\subseteq2^T\), and
\[
\mathcal V_A(D)=\{X\subseteq A:D\cup X\in\mathcal V\},
\qquad D\subseteq T\setminus A,
\]
the exclusion
\[
\mathcal V\cap I_T(A,B)\subseteq\{B\}
\qquad(B\in\mathcal V)
\]
is equivalent to every section \(\mathcal V_A(D)\) having no distinct
\(X,Y\) with
\[
X\cup Y=A.
\]
The fixed-\(A\) calculation is
\[
C\in I_T(A,B)
\quad\Longleftrightarrow\quad
D'=D\text{ and }X\cup Y=A
\]
when \(B=D\cup X\), \(C=D'\cup Y\), \(D,D'\subseteq T\setminus A\), and
\(X,Y\subseteq A\).  Thus, for comparable endpoints \(f\subsetneq u\), every
lower-parent terminal set \(A\in\mathcal R_f\) forces every outside-trace
section of \(\mathcal R_u\) to be top-union-free on \(A\).  Oracle accepted the
result with the wording correction that \(B\) need not lie in \(I_T(A,B)\) in
general; Scout returned only a scaffold and was ingested raw-only.  This is not
terminal evidence.  The next target is to bound or classify top-union-free
sections under prime-biased terminal product measure and active high-window
hypotheses, or prove they force known residual/product structure.

20260523T010541Z update: the nonempty endpoint escape condition left by the
star residual envelope is now split into explicit terminal shadow exclusions in
`mrw-740b9e5c6cff`.  For nonempty endpoint support \(\mathcal U\), the ordered
endpoint-nonconstant condition from `mrw-a3c54ddf4ae3` is equivalent to:
pairwise distinct endpoint triples force
\[
\mathcal R_{u_3}\cap
\mathsf I_T(\mathcal R_{u_1},\mathcal R_{u_2})=\emptyset;
\]
repeated parents \((u,u,f)\) with \(f\subsetneq u\) force
\[
\mathcal R_f\cap\mathsf J_T(\mathcal R_u)=\emptyset;
\]
and repeated child/one parent cases \((f,u,u)\), \((u,f,u)\) with
\(f\subsetneq u\) force
\[
\mathcal R_u\cap I_T(A,B)\subseteq\{B\}
\qquad(A\in\mathcal R_f,\ B\in\mathcal R_u).
\]
Adding individual terminal pair-link-freeness covers the constant nonempty
endpoint triples \((u,u,u)\).  Oracle accepted the split after correcting the
final equivalence wording; Scout returned only a scaffold and was ingested
raw-only.  This is not terminal evidence.  The next target is to charge one of
these terminal shadow exclusions quantitatively, or prove that high-mass active
branches avoiding them decompose into known residual structures.

20260523T002549Z update: empty-bottom zero-gap branches sharing
\(\emptyset\) are now quarantined at the star level in `mrw-a3c54ddf4ae3`.
For
\[
\mathcal F=
\{R:R\in\mathcal R_{\emptyset}\}
\cup
\bigcup_{u\in\mathcal U}\{u\cup R:R\in\mathcal R_u\},
\]
pair-link-freeness is equivalent to the simultaneous two-fiber constraints for
each \(\emptyset,u\) plus one remaining nonempty endpoint escape condition:
every ordered nonconstant triple
\[
(u_1,u_2,u_3)\in\mathcal U^3,\qquad u_3\in I_B(u_1,u_2),
\]
must have no terminal witness \(R_3\in I_T(R_1,R_2)\) whose ambient sets are
pairwise distinct.  Consequently every pair-link-free star assembly satisfies
the upper envelope
\[
\nu_P(\mathcal F\cap\{|S|>L\})
\le
\pi_B(\emptyset)\mathfrak M_T(L)
+
\sum_{u\in\mathcal U}\pi_B(u)\mathfrak M_T(L-|u|).
\]
Oracle accepted the proposition with ordered-triple and ambient-distinctness
clarifications; Scout returned only a scaffold and was ingested raw-only.  This
is not terminal evidence: the envelope is not generally exact, and the remaining
nonempty endpoint escape constraints still need charging or structural
classification.  The next target is to prove a star escape alternative:
active nonchargeable mass is either contained in this residual envelope or
produces a nonempty endpoint interval triple with terminal cross-fiber
exclusions.

20260522T222538Z update: the empty-bottom comparable zero-gap branch is now
quarantined in `mrw-03f08f291f7c` for isolated two-fiber assemblies.  For
nonempty \(u\subseteq B\) and
\[
\mathcal F=\{R:R\in\mathcal R_0\}\cup\{u\cup R:R\in\mathcal R_u\},
\]
the endpoint intervals
\[
I_B(\emptyset,\emptyset)=\{\emptyset\},\qquad
I_B(\emptyset,u)=I_B(u,\emptyset)=\{u\},\qquad
I_B(u,u)=2^u
\]
give an exact pair-link-free criterion: \(\mathcal R_0\) and \(\mathcal R_u\)
are terminal pair-link-free,
\[
\mathcal R_0\cap\mathsf J_T(\mathcal R_u)=\emptyset,
\]
and for every \(A\in\mathcal R_0\), \(B\in\mathcal R_u\),
\[
\mathcal R_u\cap I_T(A,B)\subseteq\{B\}.
\]
Consequently any such two-fiber branch satisfies
\[
\nu_P(\mathcal F\cap\{|S|>L\})
\le
\pi_B(\emptyset)\mathfrak M_T(L)+\pi_B(u)\mathfrak M_T(L-|u|).
\]
The same bound applies to the contribution of the \(\emptyset\)- and \(u\)-fibers
inside a larger pair-link-free family after restriction.  Oracle accepted the
criterion with the pairwise-distinct convention made explicit; Scout returned
only a scaffold and was ingested raw-only.  This is not terminal evidence.  The
next target is to extend the quarantine to many empty-bottom comparable branches
sharing \(\emptyset\), or prove that any active nonchargeable branch outside
these residual windows has a positive-gap pair or a chargeable interval triple.

20260522T194532Z update: zero shield gaps are now classified in
`mrw-e75870a3c452`.  For distinct endpoint patterns \(e,f\subseteq B\),
endpoint membership in the symmetric-difference interval satisfies
\[
e\in I_B(e,f)\Longleftrightarrow f\subseteq e,
\qquad
f\in I_B(e,f)\Longleftrightarrow e\subseteq f.
\]
Thus incomparable pairs have \(S(e,f)=I_B(e,f)\) and positive gap.  If
\(f\subsetneq e\), then
\[
I_B(e,f)=\{(e\setminus f)\cup u:u\subseteq f\},
\]
only \(e\) lies in the interval, and
\[
\pi_B(S(e,f))
=
\pi_B(I_B(e,f))
\left(1-\prod_{b\in f}q_b\right).
\]
The case \(e\subsetneq f\) is symmetric.  Therefore zero gap occurs exactly for
empty-bottom comparable pairs \((\emptyset,u)\) or \((u,\emptyset)\) with
\(u\ne\emptyset\).  Under \(q_b\le1/2\), a nonempty smaller endpoint of size
\(m\) gives
\[
\pi_B(S(e,f))\ge(1-2^{-m})\pi_B(I_B(e,f)).
\]
Oracle accepted the result with endpoint-membership and empty-product wording
clarifications; Scout returned only a scaffold and was ingested raw-only.  This
is not terminal evidence.  The next target is to classify the empty-bottom
comparable branch as residual/tower structure, or prove useful lower bounds on
\(\pi_B(I_B(e,f))\) for the positive-gap nonchargeable high-overlap pairs.

20260522T190535Z update: the distinct nonchargeable shield branch now has an
endpoint interval-gap filter in `mrw-4a33f7d04fc3`.  For distinct endpoint
patterns \(e,f\subseteq B\), define
\[
I_B(e,f)=\{g\subseteq B:e\triangle f\subseteq g\subseteq e\cup f\},
\qquad
S(e,f)=I_B(e,f)\setminus\{e,f\}.
\]
Under endpoint product law,
\[
\pi_B(I_B(e,f))
=
\prod_{b\in e\triangle f}q_b
\prod_{b\notin e\cup f}(1-q_b),
\]
and
\[
\pi_B(S(e,f))
=
\pi_B(I_B(e,f))
-\mathbf 1_{f\subsetneq e}\pi_B(e)
-\mathbf 1_{e\subsetneq f}\pi_B(f).
\]
If a pair is locally shielded,
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\},
\]
then \(\Lambda=\pi_B(\mathcal E)\le1-\pi_B(S(e,f))\).  Therefore in the
active regime \(M\ge\eta\tau\), where \(\Lambda\ge\eta\), every locally
shielded selected pair satisfies
\[
\pi_B(S(e,f))\le1-\eta.
\]
Combining with `mrw-0cbd2c0086d7`, the active branch is either chargeable
overlap or a distinct nonchargeable high-overlap locally shielded pair with
this interval-gap bound.  Oracle accepted the result after replacing an
unrestricted equivalence with a restricted contrapositive; Scout returned only
a scaffold and was ingested raw-only.  This is not terminal evidence.  The
next target is to prove useful lower bounds on \(\pi_B(S(e,f))\) in active
prime-coordinate endpoint geometry, or classify small-gap cases as
residual/tower-like obstructions.

20260522T170530Z update: active high-window mass now forces quantified
overlap branches in `mrw-0cbd2c0086d7`.  In the trichotomy of
`mrw-0845a9abe5b6`, fix \(0<\gamma<1\), \(0<\delta<1-\gamma\), and
\(0<\eta\le1\).  If
\[
M\ge\eta\tau
\qquad\text{and}\qquad
P_0(B)<\delta\eta,
\]
then the empty-atom branch \(M\le P_0(B)\tau/\delta\) is impossible.  The
endpoint-intensity condition
\[
Q(B)>\log\frac1{\delta\eta}
\]
is sufficient because \(P_0(B)\le e^{-Q(B)}\).  Since active mass gives
\[
\rho=\frac{M}{\Lambda\tau}\ge\eta,
\]
the remaining trichotomy alternatives have concrete \(\eta^2\)-scale
overlap: either a chargeable interval witness has
\[
\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)/\tau\ge\gamma\eta^2,
\]
and under product/high-window pair-link-free hypotheses the third fiber
satisfies
\[
\nu_T(\mathcal R_g)\le1-\gamma\eta^2,
\]
or a distinct nonchargeable pair has
\[
\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)/\tau
\ge(1-\gamma-\delta)\eta^2
\]
and local shield \(\mathcal E\cap I_B(e,f)\subseteq\{e,f\}\).  Oracle
accepted the result with minor tightening; Scout returned only a scaffold and
was ingested raw-only.  This is still not terminal evidence.  The next target
is to classify the distinct nonchargeable shield branch or accumulate the
chargeable \(\eta^2\)-overlap exclusions.

20260522T145031Z update: the support-light and fiber-density-sparse branches
now have direct relative mass-loss envelopes in `mrw-45819fa8022f`.  In the
endpoint-fiber setting of `mrw-2b75fd587224`, with \(\tau>0\) and
\[
\rho=
\begin{cases}
M/(\Lambda\tau),&\Lambda>0,\\
0,&\Lambda=0,
\end{cases}
\]
one has, including the \(\Lambda=0\) boundary,
\[
0\le M/\tau\le \Lambda,
\qquad
0\le M/\tau\le \rho.
\]
Thus
\[
\Lambda<\lambda\Rightarrow M<\lambda\tau,
\qquad
\rho<r\Rightarrow M<r\tau,
\]
and either sparse branch gives
\[
M<\max\{\lambda,r\}\tau.
\]
Conversely, \(M\ge\eta\tau\) forces both \(\Lambda\ge\eta\) and
\(\rho\ge\eta\).  Combining with the empty-atom estimate from
`mrw-4a7cdb250fd4`, if the empty branch holds and
\[
Q(B)>\log\frac1{\varepsilon\lambda r},
\]
then \(\Lambda<\lambda\) or \(\rho<r\), hence
\[
M<\max\{\lambda,r\}\tau.
\]
Oracle accepted this after the citation patch that the endpoint-intensity
step must use the empty-atom estimate, not only the support-density identity.
Scout returned only a scaffold and was ingested raw-only.  This is not
terminal evidence; it shows sparse branches already lose relative mass.  The
next target is to prove non-sparse endpoint support and fiber density in the
active prime-coordinate model, or classify their failure as exact
residual/tower structure.

20260522T141021Z update: the missing positive relative mass lower bound is now
split into endpoint-support and fiber-density tasks in `mrw-2b75fd587224`.
With
\[
M=\sum_{e\in\mathcal E}\pi_B(e)\nu_T(\mathcal R_e\cap H),
\qquad
\Lambda=\sum_{e\in\mathcal E}\pi_B(e),
\qquad
\tau=\nu_T(H)>0,
\]
and
\[
\rho=
\begin{cases}
M/(\Lambda\tau),&\Lambda>0,\\
0,&\Lambda=0,
\end{cases}
\]
one has
\[
M/\tau=\Lambda\rho
\]
when \(\Lambda>0\), with \(0\le\rho\le1\).  Hence
\[
\Lambda\ge\lambda,\quad \rho\ge r
\quad\Longrightarrow\quad
M\ge\lambda r\,\tau.
\]
Combining this with `mrw-4a7cdb250fd4`, if the empty-atom branch holds and
\[
Q(B)>\log\frac1{\varepsilon\lambda r},
\]
then
\[
\Lambda<\lambda
\qquad\text{or}\qquad
\rho<r.
\]
Oracle accepted the result with the boundary convention \(\rho=0\) when
\(\Lambda=0\), confirmed the strict \(Q(B)\) inequality, and reiterated that
the branch reduction is inclusive.  Scout again returned only a scaffold and
was ingested raw-only.  This is not terminal evidence: it decomposes the
missing \(M/\tau\) lower bound into an endpoint-support lower bound and a
relative fiber-density lower bound.

20260522T133021Z update: the empty-atom branch has a clean endpoint-intensity
quarantine in `mrw-4a7cdb250fd4`.  In the setting of the trichotomy
`mrw-0845a9abe5b6`, if
\[
P_0(B)=\prod_{b\in B}(1-q_b),
\qquad
Q(B)=\sum_{b\in B}q_b,
\]
and the empty-atom branch holds,
\[
M\le P_0(B)\tau/\varepsilon,
\]
then
\[
\frac{M}{\tau}\le\frac{e^{-Q(B)}}{\varepsilon}.
\]
Therefore, for any \(m>0\), the branch is impossible under
\[
M\ge m\tau
\qquad\text{and}\qquad
Q(B)>\log\frac1{m\varepsilon}.
\]
Equivalently, along endpoint blocks with \(Q(B_n)\to\infty\) and fixed
\(\varepsilon>0\), any subsequence in the empty-atom branch has
\[
M_n/\tau_n\to0.
\]
Oracle accepted the corollary with minor clarifications: the estimate only
needs \(0<q_b<1\), the branch reduction is inclusive, and varying
\(\varepsilon_n\) requires \(e^{-Q(B_n)}/\varepsilon_n\to0\).  Scout again
returned only a scaffold and was ingested raw-only.  This is not terminal
evidence; it removes the empty-atom branch only after a positive relative
mass lower bound and growing endpoint intensity.  The next target is to prove
such an \(M/\tau\) lower bound in the active prime-coordinate regime, or show
that its failure is an exact terminal residual/tower branch.

20260522T125020Z update: the mass bookkeeping is now packaged as a
three-way branch in `mrw-0845a9abe5b6`.  In the prime-biased endpoint setting,
with
\[
M=\sum_e\pi_B(e)\nu_T(\mathcal R_e\cap H),
\qquad
\rho=\frac{M}{\Lambda\tau},
\]
total accounting
\[
\Omega_{\mathrm{tot}}\ge M^2/\tau,
\qquad
\Omega_{\mathrm{tot}}=\Omega_{\mathcal C}+\Delta+\Omega_{\mathcal N},
\]
and the empty-atom diagonal quarantine
\[
\Delta\le P_0(B)M,
\]
then for \(0\le\gamma<1\) and \(0<\varepsilon<1-\gamma\), at least one holds:

1. \(\Omega_{\mathcal C}\ge\gamma M^2/\tau\), and positive \(M,\gamma\)
   extract a chargeable endpoint interval witness with common high-window
   overlap density at least \(\gamma\rho^2\);
2. \(M\le P_0(B)\tau/\varepsilon\);
3. \(\Omega_{\mathcal N}\ge(1-\gamma-\varepsilon)M^2/\tau\), and positive
   \(M\) extracts a distinct nonchargeable pair with common high-window
   overlap density at least \((1-\gamma-\varepsilon)\rho^2\) and local shield
   \[
   \mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
   \]

Oracle accepted the bookkeeping with the correction that the strong
third-fiber bound
\[
\nu_T(\mathcal R_g)\le1-\alpha
\]
requires the product/high-window lower-shadow hypotheses from
`mrw-108414b9dce7`; it does not follow from pair-link-freeness alone for an
arbitrary terminal law and arbitrary \(H\).  Scout again produced only a
scaffold and was ingested raw-only.  This result is a routing theorem, not
terminal evidence: the next target is to quarantine the empty-atom-scale
\(M\)-branch as terminal residual/tower structure, or classify/charge the
locally shielded distinct nonchargeable-pair branch.

20260522T121013Z update: diagonal energy is now quarantined directly by
high-window mass, not just by endpoint support mass.  New corollary
`mrw-c79041553496` proves that in the prime-biased endpoint law
\[
\pi_B(e)=\prod_{b\in e}q_b\prod_{b\notin e}(1-q_b),
\qquad 0<q_b\le1/2,
\]
the diagonal energy and high-window endpoint-fiber mass
\[
M=\sum_e\pi_B(e)\nu_T(\mathcal R_e\cap H),
\qquad
\Delta=\sum_e\pi_B(e)^2\nu_T(\mathcal R_e\cap H)
\]
satisfy
\[
\Delta\le P_0(B)M\le e^{-Q(B)}M,
\]
where
\[
P_0(B)=\prod_b(1-q_b),
\qquad
Q(B)=\sum_bq_b.
\]
Hence, for \(M>0\),
\[
\frac{\Delta}{M^2/\tau}
\le
\frac{P_0(B)\tau}{M}
\le
\frac{e^{-Q(B)}}{M}.
\]
Combining with the total overlap lower bound from `mrw-ad1f6f41665a` and the
split from `mrw-90be6f9a7f88`, if
\[
\Omega_{\mathcal C}\le\gamma M^2/\tau
\quad\text{and}\quad
c=1-\gamma-P_0(B)\tau/M>0,
\]
then
\[
\Omega_{\mathcal N}\ge cM^2/\tau,
\]
and weighted averaging gives a positive-weight distinct nonchargeable pair
\((e,f)\) with overlap density at least \(c\rho^2\) and local shield
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]
Conversely, diagonal-heavy energy \(\Delta\ge\delta M^2/\tau\) forces
\[
M\le P_0(B)\tau/\delta\le e^{-Q(B)}/\delta.
\]
Oracle accepted the result with the \(M=0\) converse case and explicit
total-energy notation \(\Omega_{\mathrm{tot}}\); Scout again produced only a
scaffold and was ingested raw-only at
the next target is either to lower-bound/quarantine the high-window mass \(M\)
itself in the active model, or to classify/charge the distinct
nonchargeable-pair branch.

20260522T113013Z update: the diagonal branch is now quarantined in the actual
prime-biased endpoint model.  New corollary `mrw-a75270c4ad65` proves that for
the endpoint product law
\[
\pi_B(e)=\prod_{b\in e}q_b\prod_{b\notin e}(1-q_b),
\qquad 0<q_b\le1/2,
\]
with
\[
P_0(B)=\prod_b(1-q_b),
\qquad
Q(B)=\sum_b q_b,
\qquad
\Lambda=\pi_B(\mathcal E),
\]
the normalized endpoint weights \(w_e=\pi_B(e)/\Lambda\) satisfy
\[
\eta=\max_e w_e\le P_0(B)/\Lambda\le e^{-Q(B)}/\Lambda
\]
and
\[
H_2(w)\le P_0(B)/\Lambda\le e^{-Q(B)}/\Lambda.
\]
Therefore, in the endpoint-fiber setting of `mrw-724d68db9b8c`,
\[
\frac{\Delta}{M^2/\tau}
\le
\frac{P_0(B)}{\Lambda\rho}
\le
\frac{e^{-Q(B)}}{\Lambda\rho}.
\]
Combining with `mrw-ad1f6f41665a` and `mrw-90be6f9a7f88`, if
\[
\Omega_{\mathcal C}\le\gamma M^2/\tau
\quad\text{and}\quad
\gamma+P_0(B)/(\Lambda\rho)<1,
\]
then
\[
\Omega_{\mathcal N}
\ge
\left(1-\gamma-\frac{P_0(B)}{\Lambda\rho}\right)M^2/\tau,
\]
and a positive-weight distinct nonchargeable pair has common high-window
overlap at least
\[
\left(1-\gamma-\frac{P_0(B)}{\Lambda\rho}\right)\rho^2.
\]
Conversely, diagonal-heavy energy \(\Delta\ge\delta M^2/\tau\) forces
\[
\Lambda\le P_0(B)/(\delta\rho)\le e^{-Q(B)}/(\delta\rho).
\]
Oracle accepted the result with statement-level qualifications: this is a
quarantine corollary, \(P_0(B)/\Lambda\) may exceed \(1\), and no new
pair-link-free hypothesis is needed for the accounting/local-shield conclusion.
Scout again produced only a scaffold and was ingested raw-only at
the next target is either a lower bound/quarantine for endpoint support mass
\(\Lambda\) in the active high-support model, or a structural theorem for the
distinct nonchargeable-pair branch.

20260522T105008Z update: diagonal high-window energy is now controlled by
endpoint concentration.  New proposition `mrw-724d68db9b8c` proves that after
normalizing
\[
w_e=\lambda_e/\Lambda,
\qquad
a_e=\nu_T(\mathcal R_e\cap H)/\tau,
\qquad
\rho=\sum_e w_ea_e=M/(\Lambda\tau),
\]
the diagonal branch satisfies
\[
\frac{\Delta}{M^2/\tau}
=
\frac{\sum_e w_e^2a_e}{\rho^2}
\le
\frac{H_2(w)}{\rho^2},
\qquad
\frac{\Delta}{M^2/\tau}\le\frac{\eta}{\rho},
\]
where \(H_2(w)=\sum_e w_e^2\) and \(\eta=\max_e w_e\).  Thus with
\[
\kappa=\min\{H_2(w)/\rho^2,\eta/\rho\},
\]
one has \(\Delta\le\kappa M^2/\tau\).  Combining this with the total overlap
lower bound from `mrw-ad1f6f41665a` and the split from `mrw-90be6f9a7f88`,
if
\[
\Omega_{\mathcal C}\le\gamma M^2/\tau
\qquad\text{and}\qquad
\gamma+\kappa<1,
\]
then
\[
\Omega_{\mathcal N}\ge(1-\gamma-\kappa)M^2/\tau,
\]
so some positive-weight distinct nonchargeable pair \((e,f)\) has common
high-window overlap at least \((1-\gamma-\kappa)\rho^2\) and satisfies
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]
Conversely, diagonal-heavy energy \(\Delta\ge\delta M^2/\tau\) forces
\[
H_2(w)\ge\delta\rho^2,
\qquad
\eta\ge\delta\rho.
\]
Oracle accepted the algebra after requiring the combined branch to cite the
total overlap lower bound, not only the split identity.  Scout again produced
only a scaffold and was ingested raw-only at
the next target is either to prove endpoint weight diffuseness or concentration
quarantine in the prime-coordinate model, or to classify the distinct
nonchargeable-pair branch.

20260522T101007Z update: the overlap-energy avoidance branch has been split.
New corollary `mrw-90be6f9a7f88` proves that the unchargeable energy from
`mrw-ad1f6f41665a` decomposes as
\[
\Omega_{\mathcal U}=\Delta+\Omega_{\mathcal N},
\]
where
\[
\Delta=\sum_e\lambda_e^2\nu_T(\mathcal R_e\cap H)
\]
is diagonal high-window energy and
\[
\Omega_{\mathcal N}
=
\sum_{\substack{e\ne f\\(e,f)\notin\mathcal C}}
\lambda_e\lambda_f\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)
\]
is distinct nonchargeable-pair energy.  Hence
\[
\Omega_{\mathcal C}+\Delta+\Omega_{\mathcal N}\ge M^2/\tau.
\]
If \(\Omega_{\mathcal C}\le\gamma M^2/\tau\) and
\(\Delta\le\delta M^2/\tau\), then
\[
\Omega_{\mathcal N}\ge(1-\gamma-\delta)M^2/\tau.
\]
In the non-vacuous case \(M>0\), \(\gamma+\delta<1\), weighted averaging gives
a distinct nonchargeable ordered pair \((e,f)\) with
\[
\nu_T(\mathcal R_e\cap\mathcal R_f\cap H)/\tau
\ge(1-\gamma-\delta)\rho^2,
\]
and the selected pair is locally shielded:
\[
\mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
\]
Focused Oracle accepted the argument with the \(M>0\), \(\gamma+\delta<1\)
non-vacuity patch and warned not to promote the pair-level shield to a global
endpoint-family classification.  Scout again produced only the generated
scaffold and was ingested raw-only at
The next target is either a diagonal-control theorem, likely via effective
endpoint count or Herfindahl mass, or a structural theorem for the distinct
nonchargeable-pair relation.

20260522T093007Z update: common-overlap production has been reduced to a
clean overlap-energy alternative.  New corollary `mrw-ad1f6f41665a` proves
that for terminal high window \(H\) of measure \(\tau>0\), endpoint weights
\(\lambda_e\), and terminal fibers \(\mathcal R_e\), if
\[
M=\sum_e\lambda_e\nu_T(\mathcal R_e\cap H),
\qquad
\rho=\frac{M}{\Lambda\tau},
\qquad
\Lambda=\sum_e\lambda_e,
\]
then the high-window overlap energy satisfies
\[
\Omega_{\mathcal C}+\Omega_{\mathcal U}\ge\frac{M^2}{\tau}.
\]
Here \(\Omega_{\mathcal C}\) is the contribution from ordered endpoint pairs
\((e,f)\) for which there is a third endpoint pattern
\[
g\in\mathcal E\setminus\{e,f\},
\qquad
g\in I_B(e,f),
\]
and \(\Omega_{\mathcal U}\) is the complement, including diagonals.  Hence for
every \(0\le\gamma\le1\), either
\[
\Omega_{\mathcal C}\ge\gamma M^2/\tau
\]
or
\[
\Omega_{\mathcal U}\ge(1-\gamma)M^2/\tau.
\]
In the non-vacuous chargeable branch \(M>0\), \(0<\gamma\le1\), one finds a
chargeable pair and witness \(g\) with common high-window overlap at least
\(\gamma\rho^2\) as a fraction of \(H\).  If the endpoint-fiber union is
pair-link-free, `mrw-108414b9dce7` then gives
\[
\nu_T(\mathcal R_g)\le1-\gamma\rho^2.
\]
Focused Oracle accepted the Cauchy/Fubini proof and required the non-vacuity
patch; Scout again produced only an untouched scaffold and was ingested
terminal evidence.  The next target is to split the avoidance branch into
diagonal energy and distinct nonchargeable-pair energy, then classify the
distinct nonchargeable structure.

20260522T085001Z update: the common-fiber lower-shadow exclusion is now
quantitative under terminal product measure.  New corollary `mrw-108414b9dce7`
proves that for every terminal family \(\mathcal G\subseteq2^T\) and real
threshold \(h\),
\[
\nu_T(\mathcal G\cap H_h(T))
\le
\nu_T(\downarrow\mathcal G)\nu_T(H_h(T)),
\qquad
H_h(T)=\{R:|R|>h\}.
\]
Equivalently, when \(\tau_h=\nu_T(H_h(T))>0\),
\[
\nu_T(\downarrow\mathcal G)
\ge
\frac{\nu_T(\mathcal G\cap H_h(T))}{\tau_h}.
\]
The proof is a local Harris/FKG induction: decreasing events and increasing
events are negatively correlated under finite product measure.  Combining
this with `mrw-82f19bf75c98`, if \(\mathcal F\) is pair-link-free,
\(e_1,e_2,e_3\) are pairwise distinct, and \(e_3\in I_B(e_1,e_2)\), then
\[
\nu_T(\mathcal R_{e_3})
\le
1-
\frac{
\nu_T((\mathcal R_{e_1}\cap\mathcal R_{e_2})\cap H_h(T))
}
{\tau_h}.
\]
Thus a common fiber occupying an \(\alpha\)-fraction of the terminal
high-window charges at least \(\alpha\) total terminal measure against the
endpoint-interval third fiber.  Focused Oracle accepted the result with
minor edits around the \(\tau_h=0\) case and the endpoint hypotheses; Scout
again produced only an untouched scaffold and was ingested raw-only at
the next target is a production lemma forcing common high-window terminal
overlaps from escaped endpoint mass, or an avoidance decomposition into known
tower/shielded structures.

20260522T081000Z update: cross-\(R\) terminal exclusions have been sharpened.
New corollary `mrw-82f19bf75c98` proves that if
\[
\mathcal F
=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
\subseteq2^{B\sqcup T}
\]
is pair-link-free, \(e_1,e_2,e_3\in\mathcal E\) are pairwise distinct, and
\[
e_3\in I_B(e_1,e_2),
\]
then the third terminal fiber avoids the full lower closure of the common
terminal fiber of the first two:
\[
\mathcal R_{e_3}\cap
\downarrow(\mathcal R_{e_1}\cap\mathcal R_{e_2})
=\varnothing.
\]
Thus, for any probability law \(\nu_T\) on \(2^T\),
\[
\nu_T(\mathcal R_{e_3})
\le
1-\nu_T\!\left(\downarrow(\mathcal R_{e_1}\cap\mathcal R_{e_2})\right),
\]
with the analogous high-support-window bound.  In particular, if
\[
H_L(T)=\{R\subseteq T:|R|>L\}
\subseteq\mathcal R_{e_1}\cap\mathcal R_{e_2},
\qquad L<|T|,
\]
then \(\downarrow H_L(T)=2^T\) and \(\mathcal R_{e_3}=\varnothing\).
Focused Oracle accepted the proof and noted that no product structure is
needed for the measure inequalities; Scout again produced only an untouched
scaffold and was ingested raw-only at
the next target is a quantitative lower-shadow charging theorem for common
high-support terminal mass, or a decomposition showing escaped mass avoids
such common shadows only through known tower/shielded structures.

20260522T072953Z update: the empty/singleton/top endpoint boundary obstruction
is now promoted as `mrw-21208a768bed`.  For every finite endpoint set
\(|B|=n\ge3\), the family
\[
\mathcal S_B=\{\varnothing,B\}\cup\{\{b\}:b\in B\}
\]
is ordinary endpoint pair-link-free under the true interval
\[
I_B(A,C)=\{D:A\triangle C\subseteq D\subseteq A\cup C\}.
\]
The proof is by direct interval cases: empty endpoints have interval
\(\{X\}\), distinct singleton endpoints have interval \(\{\{b,c\}\}\), and a
singleton/top pair has interval \(\{B\setminus\{b\},B\}\).  For product
endpoint weights \(0<q_b<1\), with
\[
P_0(B)=\prod_{b\in B}(1-q_b),
\]
the mass is
\[
\nu_B(\mathcal S_B)
=
P_0(B)\left(1+\sum_{b\in B}\frac{q_b}{1-q_b}\right)
+\prod_{b\in B}q_b,
\]
specializing to \((1-q)^n+nq(1-q)^{n-1}+q^n\) in the homogeneous case.  Thus
the endpoint residual has explicit boundary lower bounds for \(a<0\) and
\(0\le a<1\).  Focused Oracle accepted the proposition and supplied the
\(n=1,2\) edge-case clarifications; Scout produced only an untouched scaffold
This is not terminal evidence for positive-\(\theta\) Erdos 536 decay.  The
next target is to peel this boundary and prove a correct positive-threshold
endpoint residual profile theorem, or return to cross-\(R\) terminal
shadow-growth via `mrw-88acf3940157`.

20260522T064952Z update: the naive endpoint Lubell/two-layer residual route is
now quarantined.  New counterexample `mrw-cdf34678a1e1` shows that ordinary
endpoint pair-link-free families need not be 2-Sperner under the squarefree
cosunflower interval
\[
I(A,B)=\{C:A\triangle B\subseteq C\subseteq A\cup B\}.
\]
For \(B=\{1,2,3\}\), \(q=1/10\), \(a=-1\), the family
\[
\mathcal A=\{\varnothing,\{1\},\{2\},\{3\},B\}
\]
is ordinary pair-link-free but contains
\[
\varnothing\subsetneq\{1\}\subsetneq B.
\]
Its homogeneous product mass is
\[
\nu_{3,1/10}(\mathcal A)=\frac{973}{1000},
\]
while the two largest eligible rank masses are
\[
w_0+w_1=\frac{729}{1000}+\frac{243}{1000}=\frac{972}{1000}.
\]
Thus the proposed bound of \(\mathfrak P_{n,q}(a)\) by the two largest
homogeneous rank probabilities is false in general.  Scout returned only a
malformed citation-fragment response and was ingested raw-only at
false chain implication and supplied the counterexample, then the proof was
locally audited against `mrw-3c39ca3d1973`.  The next target is a correct
endpoint residual profile theorem using the actual symmetric-difference
interval, with the \(\theta=0\)/empty-endpoint boundary separated, or a return
to cross-\(R\) terminal shadow-growth via `mrw-88acf3940157`.

20260522T060951Z update: terminal conditioning now reduces escaped
endpoint-fiber mass to a pointwise endpoint residual profile.  New corollary
`mrw-baa182012831` proves that if
\[
\mathcal F
=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
\subseteq2^{B\sqcup T}
\]
is pair-link-free and
\[
\mathcal E_R=\{e\in\mathcal E:R\in\mathcal R_e\},
\]
then every \(\mathcal E_R\) is ordinary endpoint pair-link-free.  Therefore,
with
\[
\mathfrak P_B(a)
=
\sup\{\nu_B(\mathcal A):\mathcal A\subseteq2^B,\ 
\mathcal A\text{ ordinary pair-link-free},\
\mathcal A\subseteq\{e:|e|>a\}\},
\]
one has
\[
\nu_P(\mathcal F\cap\{|S|>L\})
\le
\sum_{R\subseteq T}\nu_T(R)\mathfrak P_B(L-|R|)
=
\mathbb E_{R\sim\nu_T}\bigl[\mathfrak P_B(L-|R|)\bigr].
\]
The proof is the diagonal case of endpoint-terminal interval factorization:
an endpoint triple \(e_3\in I_B(e_1,e_2)\) over the same terminal set \(R\)
lifts to \(e_3\cup R\in I_P(e_1\cup R,e_2\cup R)\).  Focused Oracle
validated the statement, threshold direction, and lack of any terminal-fiber
pair-link-free hypothesis.  Scout stalled on the untouched scaffold and was
an upper-bound/decomposition result, not terminal decay.  The next target is
an endpoint residual profile theorem for \(\mathfrak P_B(a)\) in the
prime-biased endpoint regime, or a sharper cross-\(R\) terminal
shadow-growth theorem recovering the exclusions discarded by Fubini.

20260522T052951Z update: escaped endpoint mass is now localized to explicit
terminal cross-shadow exclusions.  New corollary `mrw-88acf3940157` proves
that if
\[
\mathcal F=\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
\subseteq2^{B\sqcup T}
\]
is pair-link-free, then every pairwise distinct endpoint interval triple
\[
e_3\in I_B(e_1,e_2)
\]
forces
\[
\mathcal R_{e_3}\cap
\mathsf I_T(\mathcal R_{e_1},\mathcal R_{e_2})
=\varnothing,
\]
where
\[
\mathsf I_T(\mathcal A,\mathcal B)
=
\bigcup_{A\in\mathcal A,\ B\in\mathcal B}I_T(A,B).
\]
In particular,
\[
\mathcal R_{e_1}\cap\mathcal R_{e_2}\cap\mathcal R_{e_3}
=\varnothing.
\]
The same corollary proves that comparable endpoint patterns \(f\subsetneq e\)
force
\[
\mathcal R_f\cap\mathsf J_T(\mathcal R_e)=\varnothing,
\qquad
\mathsf J_T(\mathcal A)
=
\bigcup_{A\ne B\in\mathcal A}I_T(A,B).
\]
Focused Oracle validated the distinctness hypotheses and confirmed that full
terminal interval shadows, not proper shadows, are the correct objects.  Scout
stalled on the untouched scaffold for more than eleven minutes; the run was
stopped and ingested raw-only as
quantitative: prove a terminal shadow-growth or overlap theorem making these
exclusions expensive for positive high-support fibers, or prove an
endpoint-support decomposition into complete product-tower pieces plus
negligible residue.

20260522T044950Z update: complete prime-biased product towers are now
quarantined at positive threshold parameter.  New proposition
`mrw-8e3a53602d1d` proves the finite grow-or-absorb dichotomy.  If
\(X\) is a finite endpoint part with \(0<q_x\le1/2\), then its one-hit
probability
\[
a(X)=\sum_{x\in X}q_x\prod_{u\in X\setminus\{x\}}(1-q_u)
\]
satisfies
\[
a(X)\le\frac12.
\]
Therefore a complete multipartite transversal endpoint tower with \(K\)
nonempty endpoint parts has endpoint coefficient
\[
\Gamma=\prod_{i=1}^K a(X_i)\le2^{-K},
\]
and exact residual
\[
\mathcal R(L)=\Gamma\,\mathfrak M_T(L-K)
\]
bounded by
\[
\mathcal R(L)\le2^{-K}.
\]
Combining this with `mrw-7f4dbc4882f4`, for every
\(0\le\theta'<\theta<1\), either
\[
K-\theta\mu_B\le(\theta-\theta')\mu_T
\]
and
\[
\mathcal R(\theta\mu_P)
\le
\Gamma\,\mathfrak M_T(\theta'\mu_T),
\]
or
\[
K>\theta\mu_B+(\theta-\theta')\mu_T
\]
and
\[
\mathcal R(\theta\mu_P)
<
2^{-(\theta-\theta')\mu_T}.
\]
Focused Oracle validated the one-hit bound and finite dichotomy after adding
closure/concavity details and explicit \(m=0,1,\ge2\) cases.  Scout returned a
severely truncated response and was ingested raw-only as
therefore no longer a separate positive-mass obstruction at positive
\(\theta\); the next target is escaped mass outside exact complete product
towers: force nonconstant endpoint interval triples and terminal cross-fiber
exclusions using `mrw-20ca89f696f2`, or decompose high-mass
interval-shielded endpoint supports into complete-product pieces plus
negligible residue.  Keep \(\theta=0\) separate.

20260522T040948Z update: fixed and sublinear endpoint product towers are now
absorbed by degraded terminal thresholds.  New proposition `mrw-7f4dbc4882f4`
proves that if \(P=B\sqcup T\), \(\mu_X=\sum_{x\in X}q_x\), \(\mu_T>0\),
\[
L=\theta\mu_P=\theta(\mu_B+\mu_T),
\]
and an endpoint product-tower residual has exact polynomial form
\[
\mathcal R_\otimes(L)=\sum_{s=0}^K\Gamma_s\mathfrak M_T(L-s),
\qquad \Gamma_s\ge0,
\]
then, with
\[
\theta_K\mu_T=\theta\mu_T+\theta\mu_B-K,
\]
one has
\[
\mathcal R_\otimes(\theta\mu_P)
\le
G(1)\mathfrak M_T(\theta_K\mu_T),
\qquad
G(1)=\sum_{s=0}^K\Gamma_s.
\]
In particular, if
\[
K-\theta\mu_B\le(\theta-\theta')\mu_T,
\]
then
\[
\mathcal R_\otimes(\theta\mu_P)
\le
G(1)\mathfrak M_T(\theta'\mu_T).
\]
Thus bounded \(K,\mu_B\), or more generally
\(K-\theta\mu_B=o(\mu_T)\), reduces product towers at positive
\(\theta\) to the same terminal residual theorem at any lower
\(\theta'<\theta\).  Focused Oracle validated the result with wording patches
(\(\mu_T>0\), \(\theta_K\) algebraic, no decay claim); Scout returned a
malformed/truncated response and was ingested raw-only as
complete-product-tower dichotomy: combine this threshold-degraded absorption
with endpoint coefficient decay for genuinely growing endpoint shifts, or
prove that mass outside exact product towers creates nonconstant endpoint
interval triples and terminal cross-fiber exclusions.  Keep the
\(\theta=0\) boundary explicit.

20260522T032947Z update: the naive shifted-window comparison route is now
obstructed.  New counterexample `mrw-474262d39b1d` proves that for every
integer \(h\ge1\) and every \(R>0\), there is a finite terminal product core
\(T\), threshold \(L\), and product law such that
\[
\mathfrak M_T(L)>0
\qquad\text{but}\qquad
\mathfrak M_T(L-h)/\mathfrak M_T(L)>R.
\]
Explicitly, take \(T=\{1,\ldots,h\}\) with equal coordinate weight \(q\) and
\(L=h-\tfrac12\).  Then
\[
\mathfrak M_T(L)=q^h,
\]
while after shifting by \(h\), the pair-link-free family
\[
\{\varnothing\}\cup\{\{i\}:1\le i\le h\}
\]
has mass \((1-q)^h+hq(1-q)^{h-1}\).  Hence the ratio is at least
\[
((1-q)/q)^h\to\infty.
\]
Focused Oracle validated the counterexample and the caveat: this does not
refute shifted-window estimates in the actual prime-weight/high-support Erdos
536 regime, but it rules out any universal finite-shift comparison over
arbitrary finite product cores, arbitrary product weights, and arbitrary
thresholds.  Scout returned only `Thinking` and was ingested raw-only as
threshold-aware: either prove shifted-window control using the actual
prime-weight/high-support scaling, or prove a product-tower alternative
forcing nonconstant endpoint interval triples outside exact product models.

20260522T024942Z update: exact product towers now have both a quantitative
endpoint-factor envelope and a finite shifted-window polynomial formalism.
New corollary `mrw-1c7a59e679e0` proves that for fixed finite complete
multipartite product towers, if the endpoint part intensities satisfy
\[
\max_{x\in P}q_x\to0,\qquad \sum_{x\in P}q_x\to\beta_P<\infty,
\]
then the endpoint coefficient tends to
\[
\Gamma_\infty=e^{-A}\prod_{P\in\mathcal P}\beta_P,
\qquad A=\sum_P\beta_P,
\]
and hence
\[
\Gamma_\infty\le e^{-A}(A/K)^K\le e^{-K},
\qquad K=|\mathcal P|.
\]
The residual statement is only asymptotic in the endpoint coefficient:
\[
\mathcal R_n(L)
\le
\left(e^{-A}(A/K)^K+o(1)\right)\mathfrak M_T(L-K).
\]
Focused Oracle validated this after patches for \(K\ge1\), zero intensities,
and the \(o(1)\) interpretation.  Scout also returned a useful theorem,
locally promoted as `mrw-1e5d6b8e8ab1`: for any finite product of
interval-shielded endpoint families with endpoint size polynomials
\[
G_j(z)=\sum_{e\in\mathcal E_j}\pi_{B_j}(e)z^{|e|},
\qquad
\prod_jG_j(z)=\sum_s\Gamma_s z^s,
\]
the exact residual is
\[
\mathcal R_\otimes(L)=\sum_s\Gamma_s\mathfrak M_T(L-s).
\]
Any terminal shift profile
\(\mathfrak M_T(L-s)\le\lambda_s(L)\mathfrak M_T(L)\) therefore gives the
corresponding endpoint-polynomial bound.  The next target is the actual
shifted-window theorem: control the finite ratios
\(\mathfrak M_T(L-s)/\mathfrak M_T(L)\), especially as tower size grows, or
prove a product-tower alternative forcing nonconstant endpoint intervals
outside exact product models.  Do not treat endpoint-factor envelopes or
fixed product-polynomial identities alone as terminal evidence.

20260522T020942Z update: the iterated multipartite endpoint-tower obstruction
is now formalized.  New proposition `mrw-cd7b1fe1d9af` proves that finite
products of interval-shielded endpoint families are interval-shielded.  If
\[
B=B_1\sqcup\cdots\sqcup B_r,\qquad
\mathcal E_\otimes
=
\{e_1\sqcup\cdots\sqcup e_r:\ e_j\in\mathcal E_j\},
\]
and every \(\mathcal E_j\subseteq2^{B_j}\) is interval-shielded, then
\(\mathcal E_\otimes\) is interval-shielded and has exact supported residual
\[
\mathcal R_\otimes(L)
=
\sum_{(e_1,\ldots,e_r)}
\left(\prod_{j=1}^r\pi_{B_j}(e_j)\right)
\mathfrak M_T\!\left(L-\sum_{j=1}^r|e_j|\right).
\]
If each level is \(k_j\)-uniform, with
\(\Gamma_j=\sum_{e\in\mathcal E_j}\pi_{B_j}(e)\) and
\(K=\sum_j k_j\), this becomes
\[
\mathcal R_\otimes(L)
=
\left(\prod_j\Gamma_j\right)\mathfrak M_T(L-K).
\]
For fixed finite products of complete multipartite transversal levels, the
balanced diffuse endpoint factor is
\[
e^{-\sum_j\alpha_j}\prod_j\frac{\alpha_j^{k_j}}{k_j^{k_j}}.
\]
Scout again returned a malformed non-auditable source fragment and was
Oracle succeeded and validated the proposition, with wording patches applied
to keep the claim finite/fixed and non-terminal.  The next target is a
product-tower alternative or shifted-window contraction theorem: either
positive mass outside exact finite product towers creates nonconstant endpoint
interval triples and cross-fiber exclusions, or the shifted terminal factor
\(\mathfrak M_T(L-K)\) must be controlled.  Do not use exact finite product
towers alone as terminal evidence.

20260522T012941Z update: the higher-uniform endpoint-shield obstruction is
now consolidated for all fixed uniformities.  New proposition
`mrw-fd7565b99af5` proves that if
\[
B=X_1\sqcup\cdots\sqcup X_k
\]
and \(H\subseteq X_1\times\cdots\times X_k\), then the transversal endpoint
family
\[
\mathcal E(H)
=
\{\{x_1,\ldots,x_k\}:(x_1,\ldots,x_k)\in E(H)\}
\]
is interval-shielded.  Thus its exact supported residual is
\[
\mathcal R_H(L)
=
\sum_{e\in\mathcal E(H)}\pi_B(e)\mathfrak M_T(L-k).
\]
In the complete \(k\)-partite case this factors as
\[
\mathcal R_{X_1,\ldots,X_k}(L)
=
\left(\prod_{i=1}^k a_i\right)\mathfrak M_T(L-k),
\qquad
a_i=\sum_{x\in X_i}q_x\prod_{u\in X_i\setminus\{x\}}(1-q_u).
\]
For balanced diffuse weights \(|X_i|=m\), \(q_b=\alpha/(km)\), the endpoint
factor tends to
\[
e^{-\alpha}\frac{\alpha^k}{k^k}.
\]
Scout returned a malformed non-auditable fragment and was ingested raw-only as
with inline files, but the live browser run lost the Chrome window before
completion and is recorded at
The next target is no longer to find more fixed-uniformity endpoint shields:
prove a shifted-window comparison/contraction theorem controlling
\(e^{-\alpha}\alpha^k k^{-k}\mathfrak M_T(L-k)\), or formalize the iterated
multipartite endpoint-tower obstruction and identify where terminal-core decay
or cross-fiber exclusions must enter.  Do not use any fixed \(k\)-partite
transversal endpoint lift alone as terminal evidence.

20260522T004939Z update: the endpoint-shield branch now has a positive
higher-uniform obstruction.  New proposition `mrw-1e4b87d9862b` proves that if
\(B=X\sqcup Y\sqcup Z\) and \(H\subseteq X\times Y\times Z\) is any
3-partite 3-uniform endpoint hypergraph, then
\[
\mathcal E(H)=\{\{x,y,z\}:(x,y,z)\in E(H)\}
\]
is interval-shielded.  Therefore, by `mrw-3d6bb8271a4c`, its supported
terminal lift has exact residual
\[
\mathcal R_H(L)
=
\left(\sum_{e\in\mathcal E(H)}\pi_B(e)\right)\mathfrak M_T(L-3).
\]
In the complete tripartite case this becomes
\[
\mathcal R_{X,Y,Z}(L)=a_Xa_Ya_Z\,\mathfrak M_T(L-3),
\]
where \(a_X\) is the product-law probability of selecting exactly one point
from \(X\), and analogously for \(Y,Z\).  With balanced diffuse weights
\(|X|=|Y|=|Z|=m\), \(q_b=\alpha/(3m)\), the endpoint factor tends to
\[
e^{-\alpha}\frac{\alpha^3}{27}.
\]
Scout produced only the untouched scaffold and was ingested raw-only as
passed, but the live browser consult failed before send with an attachment
button timeout, recorded at
The next target is now a higher-uniform endpoint-profile envelope, starting
with \(k\)-partite \(k\)-uniform shields and the candidate diffuse factor
\(e^{-\alpha}\alpha^k/k^k\), or a terminal-core residual/cross-fiber exclusion
that beats these shifted residuals.  Do not use 3-uniform tripartite endpoint
lifts alone as terminal evidence.

20260522T000926Z update: the two-uniform triangle-free endpoint-profile branch
is now bounded by a fractional bipartite envelope.  New corollary
`mrw-d602b51accb8` proves that for every triangle-free endpoint graph \(G\) on
\(B\),
\[
\mathcal R_G(L)
=
P_0(B)\left(\sum_{uv\in E(G)}r_ur_v\right)\mathfrak M_T(L-2)
\le
\frac{P_0(B)R_B^2}{4}\mathfrak M_T(L-2),
\qquad
R_B=\sum_{b\in B}\frac{q_b}{1-q_b}.
\]
Under diffuse endpoint weights with
\(\max_b q_b\to0\) and \(\sum_bq_b\to\alpha\), every triangle-free
endpoint-pair shield has endpoint mass at most
\[
e^{-\alpha}\frac{\alpha^2}{4}+o(1).
\]
Balanced complete bipartite shields attain this diffuse envelope and are the
old one-from-each tower branch from `mrw-50bca8113dbf`; balanced
\(C_{2h+1}\)-blow-ups have mass \(e^{-\alpha}\alpha^2/(2h+1)\), with \(C_5\)
deficit \(e^{-\alpha}\alpha^2/20\).  Scout stalled before ChatGPT thinking
focused Oracle validated the corollary after notation/equality patches, all
applied.  The next target should leave two-uniform endpoint mass: either prove
a terminal-core residual decay or cross-fiber exclusion theorem below this
fractional envelope, or construct/audit a higher-uniformity interval-shielded
endpoint support, starting with dense cancellative 3-uniform families.

20260521T232925Z update: the first non-bipartite triangle-free endpoint-pair
shield has been audited.  New proposition `mrw-3161f39fd270` proves that if
\(B=V_0\sqcup\cdots\sqcup V_{2h}\) and \(G\) is the complete blow-up of the
odd cycle \(C_{2h+1}\), then \(G\) is triangle-free and its endpoint-pair
support has exact shifted terminal residual
\[
\mathcal R_G(L)
=
P_0(B)\left(\sum_{i=0}^{2h}R_iR_{i+1}\right)\mathfrak M_T(L-2),
\qquad
R_i=\sum_{v\in V_i}\frac{q_v}{1-q_v}.
\]
In the balanced diffuse specialization \(|V_i|=m\) and
\(q_v=\alpha/((2h+1)m)\),
\[
\Pi_G(B)\to e^{-\alpha}\frac{\alpha^2}{2h+1},
\]
so a balanced \(C_5\)-blow-up has endpoint mass
\(e^{-\alpha}\alpha^2/5\).  Since every part is nonempty, the blow-up contains
an odd cycle and is not representable as a single two-class one-from-each
subtower on the same endpoint coordinates.  It only decomposes as adjacent
complete-bipartite edge blocks, with a common endpoint-absence factor; this is
not a global tower reduction.  Scout hit the ChatGPT usage limit and was
Oracle validated the proposition after minor wording patches, all applied.
The next target is a weighted triangle-free endpoint-profile residual theorem:
decide whether high-mass triangle-free endpoint graphs decompose into
bipartite subtower pieces plus controlled odd-cycle components, or whether
odd-cycle blow-ups force a new finite odd-cycle shifted-residual branch.

20260521T222219Z update: the complete bipartite endpoint-pair obstruction is
now quarantined as the previously audited one-from-each endpoint tower.  New
corollary `mrw-50bca8113dbf` proves that if \(P=T\sqcup X\sqcup Y\) and
\(G\subseteq X\times Y\) is a bipartite endpoint graph, then the supported
endpoint-pair residual is exactly
\[
\mathcal R_G(L)
=
\left(\sum_{xy\in E(G)}\alpha_x\beta_y\right)\mathfrak M_T(L-2),
\]
where
\[
\alpha_x=q_x\prod_{u\in X\setminus\{x\}}(1-q_u),
\qquad
\beta_y=q_y\prod_{v\in Y\setminus\{y\}}(1-q_v).
\]
Thus every bipartite shield is a subtower dominated by
\[
\alpha_X\beta_Y\mathfrak M_T(L-2),
\qquad
\alpha_X=\sum_x\alpha_x,\quad \beta_Y=\sum_y\beta_y,
\]
and equality in the endpoint factor is the complete bipartite case
\(G=K_{X,Y}\).  This complete case is exactly the \(r=1\) endpoint tower from
`mrw-b52df00c958c` with \(\Gamma_1=\alpha_X\beta_Y\); the balanced diffuse
mass \(e^{-\alpha}\alpha^2/4\) from `mrw-1b04240e9886` is precisely this
one-from-each factor.  Live Scout stalled before ChatGPT thinking and was
Oracle validated the corollary after minor patches, all applied.  The next
two-uniform shielded branch is non-bipartite triangle-free structure, starting
with balanced blow-ups of \(C_5\): compute its diffuse mass and shifted
terminal residual, then decide whether it decomposes into bipartite subtowers
or creates a genuinely new odd-cycle shielded residual branch.

20260521T214218Z update: the first genuinely overlapping endpoint-shielded
branch is now isolated.  New proposition `mrw-1b04240e9886` proves that a
two-point endpoint-pattern family \(\mathcal E(G)=\{\{u,v\}:uv\in E(G)\}\)
is interval-shielded if and only if the graph \(G\) is triangle-free.  Its
exact endpoint mass is
\[
\Pi_G(B)
=
\left(\prod_{b\in B}(1-q_b)\right)
\sum_{uv\in E(G)}
\frac{q_u}{1-q_u}\frac{q_v}{1-q_v},
\]
and every triangle-free endpoint-pair shield has exact shifted terminal
residual
\[
\mathcal R_G(L)=\Pi_G(B)\mathfrak M_T(L-2).
\]
Balanced complete bipartite shields give a positive diffuse obstruction:
if \(B_n=X_n\sqcup Y_n\), \(|X_n|=|Y_n|=m_n\to\infty\), and
\(q_b=\alpha/(2m_n)\), then for \(G_n=K_{m_n,m_n}\),
\[
\Pi_{G_n}(B_n)\to e^{-\alpha}\frac{\alpha^2}{4}.
\]
Thus overlapping shielded endpoint-pair mass can remain positive even with
internal singleton intensity \(Q_{1,n}=0\), and it is not explained by the
disjoint-block/matching theorem.  Scout returned a malformed non-auditable stub
and was ingested raw-only as an operational blocker; focused Oracle validated
the proof after statement-hygiene patches, all applied.  The next target is a
weighted triangle-free endpoint-pair residual theorem with shifted terminal
windows, or a tower-level reduction showing that dense bipartite endpoint-pair
shields are exactly the known one-from-each residual branch and cannot yield a
new terminal \(R_P(\theta)\) lift.

20260521T210217Z update: the matching/disjoint-block endpoint shield branch is
now controlled.  New proposition `mrw-7f81977a8847` proves that every finite
pairwise disjoint family \(\mathcal A\) of nonempty endpoint blocks is
interval-shielded and has exact endpoint mass
\[
\Pi_{\mathcal A}(B)
=
\left(\prod_{b\in B}(1-q_b)\right)
\sum_{A\in\mathcal A}\prod_{a\in A}\frac{q_a}{1-q_a}.
\]
For a terminal core \(T\), its exact shifted residual is
\[
\mathcal R_{\mathcal A}(L)
=
\sum_{A\in\mathcal A}\pi(A)\mathfrak M_T(L-|A|).
\]
If \(\delta=\max_b q_b<1/2\) and \(Q=\sum_b q_b\), then the non-singleton
block contribution satisfies
\[
\sum_{A\in\mathcal A,\ |A|\ge2}\pi(A)\mathfrak M_T(L-|A|)
\le 4\delta Qe^{-Q}\le 4\delta/e.
\]
Consequently, under diffuse weights \(\delta_n\to0\),
\(Q_n\to\alpha\), and singleton-block intensity \(Q_{1,n}\to\alpha_1\),
\[
\mathcal R_{\mathcal A_n}(L)
=
e^{-\alpha}\alpha_1\mathfrak M_T(L-1)+o(1),
\]
while if \(\delta_n\to0\) and \(Q_n\to\infty\) the entire disjoint-block
endpoint mass vanishes.  Thus disjoint pairs, matchings, and larger disjoint
blocks do not create a new positive diffuse shielded obstruction beyond the
singleton branch.  Scout failed at the attachment-send step and was ingested
raw-only; focused Oracle validated the proposition after a wording patch to
make the \(Q_n\to\infty\) clause explicitly diffuse.  The next target is the
remaining overlapping shielded-antichain problem: either decompose every
high-mass interval-shielded endpoint family into a singleton/disjoint-block
core plus negligible remainder, or construct an overlapping high-mass
shielded family and audit its full pair-link intervals and any possible
\(R_P(\theta)\) lift.

20260521T202217Z update: a broad endpoint-only decay theorem for
interval-shielded endpoint families is obstructed.  New counterexample
`mrw-89ac956348a7` proves that the singleton endpoint family
\[
\mathcal E_1(B)=\{\{b\}:b\in B\}
\]
is interval-shielded and has exact product mass
\[
\Pi_1(B)
=
\sum_{b\in B}q_b\prod_{c\ne b}(1-q_c)
=
\left(\prod_{c\in B}(1-q_c)\right)
\sum_{b\in B}\frac{q_b}{1-q_b}.
\]
If \(Q_n=\sum_{b\in B_n}q_b\to\alpha\in(0,\infty)\) and
\(\max_b q_b\to0\), then
\[
\Pi_1(B_n)\to\alpha e^{-\alpha}.
\]
Thus diffuse endpoint weights with nonzero limiting total intensity can carry
constant interval-shielded mass, e.g. \(e^{-1}\) when \(\alpha=1\).  For every
terminal pair-link-free \(\mathcal R\subseteq2^T\), the lift
\[
\{\{b\}\cup R:b\in B,\ R\in\mathcal R\}
\]
is pair-link-free and has exact high-support value
\[
\Pi_1(B)\nu_T(\mathcal R\cap\{|R|>L-1\}),
\]
so the singleton-shielded branch is exactly
\[
\Pi_1(B)\mathfrak M_T(L-1).
\]
Scout again failed at the attachment-send step and was ingested raw-only;
focused Oracle validated the counterexample and requested only the
"nonvanishing limit" wording patch, now applied.  The next target is no longer
plain endpoint-only shield decay.  It must be a refined interval-shield
variational theorem using endpoint-size/profile and shifted terminal residual
windows, or a proof that mass beyond singleton/matching-type residual envelopes
forces nonconstant endpoint interval triples and terminal cross-fiber
exclusions.

20260521T194216Z update: the interval-shielded endpoint branch is now
quarantined as an exact self-similar residual.  New corollary
`mrw-3d6bb8271a4c` proves that if \(P=B\sqcup T\), product measure factors as
\(\nu_P=\nu_B\otimes\nu_T\), and \(\mathcal E\subseteq2^B\) has no
nonconstant endpoint interval triple, then endpoint-pattern fiber unions
supported on \(\mathcal E\) have exact high-support supremum
\[
\sum_{e\in\mathcal E}\pi_B(e)\mathfrak M_T(L-|e|).
\]
In endpoint-tower notation, if the endpoint-set image
\(\{E(\omega):\omega\in\mathcal E\}\) is interval-shielded, the shielded
defect residual is exactly
\[
\mathcal S_{\mathrm{sh}}(L;\mathcal E)
=
\sum_{\omega\in\mathcal E}
\pi(\omega)\mathfrak M_{P_r}(L-|E(\omega)|).
\]
Thus shielded defect-pattern mass alone does not force pointwise mixed
incidence, a full pair-link interval hit, or a new saving beyond terminal
residual self-similarity.  Scout again failed at the attachment-send step and
was ingested raw-only; focused Oracle passed the corollary and requested only
scope/endpoint-set wording patches, now applied.  The next target is to prove
an endpoint interval-shield variational theorem bounding the weighted shielded
residual, or to prove that positive high-support mass outside that residual
must generate many nonconstant endpoint interval triples and the terminal
cross-fiber exclusions from `mrw-20ca89f696f2`.

20260521T182914Z update: the first missing cross-pattern constraint has been
isolated.  New proposition `mrw-20ca89f696f2` proves that for a disjoint split
\(P=B\sqcup T\), endpoint patterns \(e_i\subseteq B\), terminal sets
\(R_i\subseteq T\), and \(S_i=e_i\cup R_i\), one has
\[
S_3\in I_P(S_1,S_2)
\quad\Longleftrightarrow\quad
e_3\in I_B(e_1,e_2)\ \text{and}\ R_3\in I_T(R_1,R_2).
\]
Therefore a union of endpoint-pattern terminal fibers
\[
\mathcal F=\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
\]
is pair-link-free exactly when no endpoint interval triple
\(e_3\in I_B(e_1,e_2)\) supports a terminal interval witness
\(R_3\in I_T(R_1,R_2)\) with the three full sets pairwise distinct.  A clean
sufficient shield is stronger than ordinary endpoint pair-link-freeness:
\(\mathcal E\) must have no nonconstant endpoint interval triple, equivalently
ordinary endpoint pair-link-freeness plus an antichain condition.  Scout again
failed at the attachment-send step and was ingested raw-only; focused Oracle
confirmed the factorization and independently flagged the same repeated-endpoint
distinctness issue.  The next target is to use this factorization to sharpen
the endpoint-pattern residual budget: either many defect patterns force many
endpoint interval triples and cross-fiber exclusions, or interval-shielded
defect patterns form an antichain-like residual family whose mass is small or
self-similar.

20260521T174914Z update: the realized-overfull-to-\(\Xi\) route also needs a
stronger hypothesis.  New proposition `mrw-1f23857438d4` proves that every
fixed exact endpoint occupancy pattern
\[
\omega=((A_1,B_1),\ldots,(A_r,B_r))
\]
is just a shifted terminal-core residual.  For
\[
\mathcal A_\omega(\mathcal R)=\{R\cup E(\omega):R\in\mathcal R\},
\]
one has pair-link-freeness in \(2^P\) if and only if
\(\mathcal R\subseteq2^{P_r}\) is pair-link-free, and
\[
\nu_P(\mathcal A_\omega(\mathcal R)\cap H_L)
=
\pi(\omega)\nu_{P_r}(\mathcal R\cap\{|R|>L-|E(\omega)|\}).
\]
Thus the fixed-pattern optimum is exactly
\[
\pi(\omega)\mathfrak M_{P_r}(L-|E(\omega)|).
\]
If \(\omega\) is overfull, all this mass lies in the realized overfull event
\(O_{\mathrm{ov}}\), but it still need not produce the pointwise mixed
incidence hypothesis of `mrw-7f0eb8d1648c`.  Scout failed at the attachment-send
step and was ingested raw-only; focused Oracle passed the proposition after an
exact-pattern wording patch.  The next target is now cross-pattern: prove that
mass spread across incompatible endpoint patterns forces a full pair-link
interval or a same-component point-support overlap \(\Xi(K)>0\), or else
reduce the occupancy-defect branch to an explicit mixture of fixed-pattern
terminal residuals.

20260521T170913Z update: the proposed endpoint-moment-to-\(\Xi\) route has a
local obstruction.  New counterexample `mrw-d65c4d544e56` proves that the
endpoint-pair budget \(R_2\) and the absorbed third-order endpoint tail in
`mrw-2a765ca2676f` are ambient slack unless tied to realized family mass.  For
a disjoint decomposition \(P=Z\sqcup X\sqcup Y\), exact one-from-each
assemblies
\[
\mathcal A=\{R\cup\{x,y\}:x\in X,\ y\in Y,\ R\in\mathcal R_{xy}\}
\]
are pair-link-free whenever the endpoint fibers are pair-link-free
(`mrw-d7b3299d3813`) and have zero pointwise mixed incidence because
\(C_0=X\), \(C_1=Y\), and \(X\cap Y=\varnothing\)
(`mrw-23227179a350`).  Yet
\[
R_2=\sum_{\{p,q\}\subseteq X}q_pq_q+\sum_{\{p,q\}\subseteq Y}q_pq_q
\]
can be positive, and if \(X=\{x_1,x_2\}\), \(|Y|\ge3\), then the collapsed
absorbed tail \(q_{x_1}q_{x_2}\nu_Y(|B|\ge3)\) is also positive.  Taking
\(Z=\varnothing\) gives a positive-mass high-support witness for \(L<2\); for
larger thresholds the same obstruction requires terminal fibers with positive
mass above \(L-2\).  Scout produced only a scaffold and was ingested raw-only;
focused Oracle agreed with the obstruction and the threshold qualifier.  This
does not refute `mrw-2a765ca2676f`, but it kills the ambient-moment implication.
The next target is a realized-overfull charging theorem: prove that excess
high-support mass outside exact endpoint-tower residuals creates actual
overfull endpoint-slice mass or escaped occupancy that forces \(\Xi>0\) via
`mrw-7f0eb8d1648c`, or else reduces to a strict smaller terminal-core residual.

20260521T160712Z update: the strict-deletion tail budget is now inserted into
one terminal-window inequality.  New corollary `mrw-2a765ca2676f` combines
`mrw-5df7f8135e2c` with the \(b=2\) absorbed-window estimate
`mrw-791fae526f01`.  With
\[
R_2=\sum_{e\in\mathcal E_{\mathrm{ov}}}q_e
\]
and collapsed opposite classes \(D_j\), every pair-link-free
\(\mathcal F\subseteq2^P\) satisfies
\[
\nu_P(\mathcal F\cap H_L)
\le
\mathfrak M_{P_r}(L-2r)
+2R_2\mathfrak M_{P_r}(L-2r-2)
+R_2^2
+
\frac13\sum_{e=C_j\in\mathcal E_{\mathrm{col}}}q_eQ(D_j)^3.
\]
The proof first records the sharper form with coefficient
\(\sum_e q_e(\Gamma_e+\beta_e)\), second-overfull charge
\(\sum_e q_e\pi_{\mathrm{ov}}^e\), and absorbed tail
\[
\sum_{e=C_j}q_e(\Gamma_e+\beta_e)\nu_{D_j}(|B|\ge3).
\]
Then it uses \(0\le\Gamma_e\le1\), \(\beta_e\le1\), retained induced
endpoint classes being original classes or subsets, and the product triple
union bound.  This is nonterminal: it does not prove terminal residual decay,
\(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or an \(R_P(\theta)\) lift.
Scout live upload failed before send and was ingested raw-only; focused Oracle
hit the ChatGPT usage limit, so no Oracle proof content was imported.  The
next target is a higher-occupancy-to-mixed-incidence theorem: show that
non-negligible \(R_2^2\) or absorbed cubic mass forces pointwise mixed
incidence and coherent-component defect, or construct an endpoint-moment-heavy
candidate and audit all full pair-link intervals.

20260521T152927Z update: the strict-deletion residual branch now has a
one-step iteration and the collapsed enlarged cores are no longer opaque.
New corollary `mrw-5df7f8135e2c` proves that for every same-class endpoint
pair \(e\), with induced tower data from `mrw-3dde1053699f`, one has
\[
\mathfrak M_{P\setminus e}(U)
\le
(\Gamma_e+\beta_e)\mathfrak M_{T_e}(U-2\ell_e)
+
\pi_{\mathrm{ov}}^e,
\]
where \(\beta_e=0\) only for the length-zero induced tower and
\(\pi_{\mathrm{ov}}^e\) is the second-generation overfull probability in the
retained endpoint classes of the induced tower.  Therefore every
pair-link-free \(\mathcal F\subseteq2^P\) satisfies
\[
\nu_P(\mathcal F\cap H_L)
\le
\mathfrak M_{P_r}(L-2r)
+
\sum_{e\in\mathcal E_{\mathrm{ov}}}q_e
\left[
(\Gamma_e+\beta_e)\mathfrak M_{T_e}(L-2-2\ell_e)
+
\pi_{\mathrm{ov}}^e
\right].
\]
Surviving deletions have \(T_e=P_r\) and \(\ell_e=r\); collapsed deletions
with \(r>1\) have \(T_e=P_r\cup D_j\) and \(\ell_e=r-1\); the \(r=j=1\)
collapsed case is already terminal.  Focused Oracle passed this corollary
after a length-zero wording patch.

Scout then supplied a useful slicing lemma, locally audited and promoted as
`mrw-791fae526f01`: for disjoint product coordinate sets \(C,D\),
\[
\mathfrak M_{C\sqcup D}(T)
\le
\mathbb E_{B\sim\nu_D}\mathfrak M_C(T-|B|).
\]
Applied to a collapsed terminal core \(P_r\cup D_j\), this gives
\[
\mathfrak M_{P_r\cup D_j}(L-2r)
\le
\mathbb E_{B\sim\nu_{D_j}}\mathfrak M_{P_r}(L-2r-|B|)
\le
\mathfrak M_{P_r}(L-2r-2)+\nu_{D_j}(|B|\ge3),
\]
and
\[
\nu_{D_j}(|B|\ge3)\le
\sum_{\{a,b,c\}\subseteq D_j}q_aq_bq_c
\le Q(D_j)^3/6.
\]
Focused Oracle passed this proposition after dependency cleanup and the
\(b=2\) specialization patch.  This remains nonterminal: no residual decay or
\(R_P(\theta)\) lift follows.  The next target is to insert this absorbed
window into the full strict-deletion iteration and prove that the weighted
third-order absorbed tails and second-overfull probabilities are summable or
force pointwise mixed incidence/coherent-component defect.

20260521T145110Z update: the strict-deletion structural caveat is now
resolved locally.  New proposition `mrw-3dde1053699f` proves that every
same-class endpoint-pair deletion \(P\setminus e\), with
\(e=\{p,q\}\subseteq C_j\in\{X_j,Y_j\}\), admits a compatible induced
endpoint tower.  If the deleted endpoint class survives, then the tower has
the same length \(r\), terminal core \(P_r\), and only \(C_j\) is replaced by
\(C_j\setminus e\).  If the deleted class is exhausted, then level \(j\) is
skipped, the opposite endpoint class \(D_j\) is absorbed into every deeper
core, the induced tower has length \(r-1\), and the terminal core becomes
\(P_r\cup D_j\).  Applying `mrw-05f82d03b190` to the induced tower gives, for
each real \(U\),
\[
\mathfrak M_{P\setminus e}(U)
\le
\Gamma_e\,\mathfrak M_{T_e}(U-2\ell_e)
+
\mathcal R_{\mathrm{def}}^e(U).
\]
Therefore the overfull branch from `mrw-c82229c73d8d` satisfies
\[
\sum_{e\in\mathcal E_{\mathrm{ov}}}q_e
\mathfrak M_{P\setminus e}(L-2)
\le
\sum_{e\in\mathcal E_{\mathrm{ov}}}q_e
\left(
\Gamma_e\,\mathfrak M_{T_e}(L-2-2\ell_e)
+
\mathcal R_{\mathrm{def}}^e(L-2)
\right).
\]
This is structural, not terminal: it does not prove residual decay, a
terminal-core theorem, or an \(R_P(\theta)\) lift.  Scout returned no usable
solution section and was ingested raw-only.  Focused Oracle passed the proof
with one hygiene caveat, now patched: when \(r=j=1\) and the endpoint class is
exhausted, the induced tower has length zero, with
\(\ell_e=0\), \(T_e=P\setminus e\), \(\Gamma_e=1\), and
\(\mathcal R_{\mathrm{def}}^e=0\).  The next target is a contraction or
iteration theorem for these induced strict-deletion residuals, especially the
collapsed-class cores \(T_e=P_r\cup D_j\), or a proof that near-extremal
induced residuals force pointwise mixed incidence and coherent-component
defect.

20260521T140929Z update: the overfull endpoint branch is now reduced to
strict two-point deletion residuals.  New proposition `mrw-c82229c73d8d`
proves that if
\[
\mathcal E_{\mathrm{ov}}
=
\bigcup_{j=1}^r\left(\binom{X_j}{2}\cup\binom{Y_j}{2}\right)
\]
is the set of same-class endpoint pairs, then every pair-link-free
\(\mathcal F\subseteq2^P\) satisfies
\[
\nu_P(\mathcal F\cap H_L\cap O_{\mathrm{ov}})
\le
\sum_{e=\{p,q\}\in\mathcal E_{\mathrm{ov}}}
q_pq_q\,\mathfrak M_{P\setminus e}(L-2).
\]
Combining this with the non-overfull endpoint-pattern bound gives the global
estimate
\[
\nu_P(\mathcal F\cap H_L)
\le
\mathfrak M_{P_r}(L-2r)
+
\sum_{e=\{p,q\}\in\mathcal E_{\mathrm{ov}}}
q_pq_q\,\mathfrak M_{P\setminus e}(L-2).
\]
The proof uses only product conditioning on \(e\subseteq S\), common-coordinate
stability of pair-link intervals, and the endpoint-pattern residual theorem.
Focused Oracle passed the proposition as proved and flagged the main caveat:
the deleted ground set \(P\setminus e\) need not inherit the same endpoint
tower, especially when deleting two points empties or damages an endpoint
class.  Scout returned a weaker compatible pair-light accounting view and was
ingested raw-only.  This is still nonterminal: the next target is a
strict-deletion residual induction or re-towering theorem controlling the
weighted sum of \(\mathfrak M_{P\setminus e}(L-2)\), or a proof that
near-extremal strict-deletion residuals force pointwise mixed incidence and
coherent-component defect.

20260521T133141Z update: the defect-pattern budget now has two local
terminal-residual gates.  New proposition `mrw-9cb7a5d73a8f` proves the
basic active-layer localization: if
\[
\mathcal R_{\mathrm{def}}(L)
=
\sum_m \Pi_m^{\mathrm{def}}\mathfrak M_{P_r}(L-m),
\qquad
\Pi_{\mathrm{def}}=\sum_m\Pi_m^{\mathrm{def}}\le1,
\]
then
\[
\mathcal R_{\mathrm{def}}(L)
\le
\Pi_{\mathrm{def}}
\max_{\Pi_m^{\mathrm{def}}>0}\mathfrak M_{P_r}(L-m),
\]
so a large \(\mathcal R_{\mathrm{def}}(L)\) exposes a large active shifted
terminal residual.  Focused Oracle passed this proof and emphasized its
accounting-only strength: the active shift \(m\) is uncontrolled.

Scout then suggested, and local audit promoted, the stronger proposition
`mrw-59f327fd233e`: balanced missing or underfilled endpoint-defect patterns
are absorbed by the exact-shift terminal residual, and the remaining
uncontrolled branch is overfull endpoint incidence.  In the notation of
`mrw-05f82d03b190`,
\[
\mathcal R_{\mathrm{def}}(L)
\le
\mathfrak M_{P_r}(L-2r)+\pi_{\mathrm{ov}},
\]
where \(\pi_{\mathrm{ov}}\) is the product-measure probability that some
endpoint class \(X_j\) or \(Y_j\) contains at least two selected coordinates.
Moreover
\[
\pi_{\mathrm{ov}}
\le
\sum_{j=1}^r
\left(
\sum_{\{p,q\}\subseteq X_j}q_pq_q
+
\sum_{\{p,q\}\subseteq Y_j}q_pq_q
\right)
\le
\frac12\sum_{j=1}^r(Q(X_j)^2+Q(Y_j)^2).
\]
Thus \(\mathcal R_{\mathrm{def}}(L)\ge\eta\) forces either
\(\mathfrak M_{P_r}(L-2r)\ge\eta/2\) or
\(\pi_{\mathrm{ov}}\ge\eta/2\).  Focused Oracle passed this second proof as a
proved, nonterminal residual alternative.  The next target is the missing
overfull-incidence bridge: prove that non-negligible overfull endpoint
incidence in a high-support pair-link-free family creates pointwise mixed
incidence/coherent-component defect, loses enough high-support mass, or
reduces to a smaller terminal core residual with a meaningful cutoff.

20260521T124943Z update: the occupancy-defect slice now has an explicit
terminal-core residual budget.  New proposition `mrw-05f82d03b190` proves
that for a finite endpoint tower and an arbitrary endpoint occupancy pattern
\[
\omega=((A_1,B_1),\ldots,(A_r,B_r))
\in\prod_j(2^{X_j}\times2^{Y_j}),
\]
with endpoint set \(E(\omega)\) and endpoint probability \(\pi(\omega)\), the
terminal fiber
\[
\mathcal F_\omega=\{R\subseteq P_r:R\cup E(\omega)\in\mathcal F\}
\]
is pair-link-free whenever \(\mathcal F\subseteq2^P\) is pair-link-free.
Thus
\[
\nu_P(\mathcal F\cap\{|S|>L\})
=
\sum_{\omega}\pi(\omega)\,
\nu_{P_r}(\mathcal F_\omega\cap\{|R|>L-|E(\omega)|\})
\le
\sum_{\omega}\pi(\omega)\mathfrak M_{P_r}(L-|E(\omega)|).
\]
Restricting to non-exact patterns gives
\[
\nu_P(\mathcal F\cap D_{\mathrm{tw}}\cap\{|S|>L\})
\le
\mathcal R_{\mathrm{def}}(L)
:=
\sum_{\omega\in\Omega_{\mathrm{def}}}
\pi(\omega)\mathfrak M_{P_r}(L-|E(\omega)|).
\]
The exact patterns recover
\[
\Gamma_r\mathfrak M_{P_r}(L-2r),
\]
and the defect budget also regroups as
\[
\mathcal R_{\mathrm{def}}(L)
=
\sum_m \Pi_m^{\mathrm{def}}\mathfrak M_{P_r}(L-m),
\qquad
\mathcal R_{\mathrm{def}}(L)
\le
\nu_P(D_{\mathrm{tw}}\cap\{|S|>L\}).
\]
Scout hit the ChatGPT usage limit and was ingested raw-only.  Focused Oracle
passed the proof and requested only common-coordinate stability and the
cardinality regrouping, now patched.  This remains nonterminal: the result
does not prove that \(\mathcal R_{\mathrm{def}}\) is small, and it still
ignores cross-pattern pair-link constraints.  The next target is a
defect-pattern alternative: large \(\mathcal R_{\mathrm{def}}(\theta S_P)\)
must either force a large terminal-core residual on \(P_r\) or produce
positive pointwise mixed incidence that can be charged by `mrw-7f0eb8d1648c`.

20260521T121039Z update: the exact endpoint-tower branch is now separated
from the remaining occupancy-defect branch.  New proposition
`mrw-640f82d14b4e` proves that for a fixed finite endpoint tower
\[
P=P_0\supseteq\cdots\supseteq P_r,\qquad
P_{j-1}=P_j\sqcup X_j\sqcup Y_j,
\]
and any pair-link-free \(\mathcal F\subseteq2^P\), if
\[
E_{\mathrm{tw}}=\{S:|S\cap X_j|=|S\cap Y_j|=1\text{ for all }j\},
\qquad
D_{\mathrm{tw}}=2^P\setminus E_{\mathrm{tw}},
\]
then for \(H_L=\{S:|S|>L\}\),
\[
\nu_P(\mathcal F\cap H_L)
\le
\Gamma_r\,\mathfrak M_{P_r}(L-2r)
+
\nu_P(\mathcal F\cap D_{\mathrm{tw}}\cap H_L).
\]
Thus any high-support mass exceeding the exact tower residual must lie in the
non-exact occupancy slice, where a set selects zero, two, or more points from
at least one endpoint class.  Scout returned a truncated advisory reduction
note and was ingested raw-only.  Focused Oracle passed the proof as a valid
accounting reduction and requested only dependency hygiene; the node now lists
`mrw-b52df00c958c` as the direct proof dependency and records
`mrw-23227179a350`, `mrw-d7b3299d3813`, and `mrw-fe13472e08c8` as contextual
ancestry.  This is not terminal: no bound on the defect slice, no
\(\Xi>0\) theorem, and no \(M_{P_k}(\theta)\), \(U_k(\theta)\), or
\(R_P(\theta)\) lift follows.  The next target is an occupancy-defect
charging theorem: positive high-support mass in \(D_{\mathrm{tw}}\) must
either produce pointwise mixed incidence and coherent-component defect, lose
enough high-support mass, or reduce to a smaller terminal core residual.

20260521T112857Z update: the clean zero-\(\Xi\) escape branch is now
classified under exact occupancy.  New corollary `mrw-23227179a350` proves
that if
\[
P=Z\sqcup X\sqcup Y,\qquad |A\cap X|=|A\cap Y|=1
\quad(A\in\mathcal A),
\]
then \(C_0=X\), \(C_1=Y\) have zero pointwise mixed incidence and
\(\mathcal A\) has the unique endpoint-fiber representation
\[
\mathcal A=\{R\cup\{x,y\}:x\in X,\ y\in Y,\ R\in\mathcal R_{xy}\}.
\]
Thus the full pair-link interval test and product-mass decomposition reduce
to endpoint fibers by `mrw-d7b3299d3813`.  The same unique transcript
classification holds for iterated exact towers
\[
P_{j-1}=P_j\sqcup X_j\sqcup Y_j,\qquad |A\cap X_j|=|A\cap Y_j|=1,
\]
and `mrw-b52df00c958c` gives the terminal residual value
\[
\Gamma_r\,\mathfrak M_{P_r}(L-2r).
\]
Scout returned only a short process note and was ingested raw-only.  Focused
Oracle passed the proof after requiring nonempty endpoint classes and explicit
notation for \(E(\mathbf e)\), \(\Gamma_r\), and \(\mathfrak M_{P_r}\); those
patches are applied.  This is not terminal: it does not prove \(\Xi>0\), and
it does not show that \(\Xi=0\) alone forces exact occupancy.  The next target
is an occupancy-defect theorem for the remaining zero-\(\Xi\) branch: sets
selecting zero, two, or more points from a normalized support class must
either pay defect/mixed incidence, lose high-support mass, or reduce to a
terminal core residual.

20260521T104936Z update: pointwise mixed incidence is now the local source
object for the coherent-component defect route.  New corollary
`mrw-7f0eb8d1648c` defines
\[
C_a(K)=\bigcup_{i\in K}\widehat S_i^a,\qquad
\Xi(K)=w(C_0(K)\cap C_1(K)),
\]
and proves, in the setting of `mrw-b2b9ece4dd87` with ordinary corridor side
disjointness,
\[
\Xi(K)\le \mathcal E_{\mathrm{mix}}(K)
\le (|K|-1)\mathcal D(K).
\]
Thus any positive pointwise mixed-incidence lower bound
\(\Xi(K)\ge\eta>0\) forces
\[
\mathcal D(K)\ge \eta/(|K|-1)
\qquad(|K|\ge2).
\]
In the zero-defect case the normalized point supports
\[
C_0(K),\quad C_1(K)
\]
are disjoint modulo \(w\)-null sets, giving the exact local two-class
point-support escape alternative.  Scout was attempted twice: the first run
failed before send because attachments never reached a clickable send button,
and the inline retry returned only the ChatGPT usage-limit message, so Scout
was ingested raw-only with no promoted content.  Focused Oracle first failed
because Chrome closed, then passed on retry and requested only the explicit
\(i<j\) notation patch, now applied.  This remains nonterminal: the next
target is a global high-support incidence lemma forcing \(\Xi(K)>0\) inside a
completed robust component, preferably with bounded component size or a summed
form controlling the \((|K|-1)\) loss; failing that, classify the zero-\(\Xi\)
two-class point-support alternative as an endpoint-fiber/tower assembly and
test full pair-link intervals plus any possible \(R_P(\theta)\) lift.

20260521T100912Z update: the mixed-overlap defect budget is now an explicit
certificate.  New corollary `mrw-b2b9ece4dd87` packages
`mrw-bc27191b14d4` by defining
\[
\mathcal E_{\mathrm{mix}}(K)=
\sum_{\{i,j\}\subseteq K}\sum_{a\ne b}
w(\widehat S_i^a\cap\widehat S_j^b),
\qquad
\mathcal D(K)=\sum_{i\in K}(D_i^0+D_i^1),
\]
and proving
\[
\mathcal E_{\mathrm{mix}}(K)\le (|K|-1)\mathcal D(K).
\]
Thus any positive same-component lower bound
\(\mathcal E_{\mathrm{mix}}(K)\ge\eta\) forces
\[
\mathcal D(K)\ge \eta/(|K|-1)
\]
for \(|K|\ge2\).  In the complete zero-defect case, mixed normalized sharing
has zero weight.  Scout again returned the known attachment-mismatch blocker
because `THEORY_LATEST.tex` is the zeta/Gamma manuscript, but its advisory
derivation matched the local proof and was ingested raw-only at
Oracle passed after requiring the endpoint-tower interpretation to be stated
conditionally: `mrw-b52df00c958c` is contextual ancestry, not a direct bridge
from endpoint towers to zero-defect coherent robust components.  This is not a
terminal \(M_{P_k}(\theta)\), \(U_k(\theta)\), or \(R_P(\theta)\) theorem.
The next target is a same-component mixed-overlap production lemma from
positive high-support mass outside exact endpoint-tower residuals, preferably
with control of the \((|K|-1)\) loss.

20260521T093015Z update: the exact endpoint-fiber obstruction now has a
finite iterated-tower form.  New proposition `mrw-b52df00c958c` proves that
for any tower
\[
P=P_0\supseteq P_1\supseteq\cdots\supseteq P_r,\qquad
P_{j-1}=P_j\sqcup X_j\sqcup Y_j,
\]
the class of exact towers selecting one point from each \(X_j\) and \(Y_j\)
has optimal high-support mass
\[
\sup_{\mathcal A}
\nu_P(\mathcal A\cap\{S:|S|>L\})
=
\Gamma_r\,\mathfrak M_{P_r}(L-2r),
\qquad
\Gamma_r=\prod_{j=1}^r\alpha_j\beta_j.
\]
Pair-link triples cannot mix endpoint transcripts, so pair-link-freeness is
equivalent to pair-link-freeness of every terminal fiber.  The equal terminal
fiber construction is sharp.  Scout again returned the known
attachment-mismatch blocker because `THEORY_LATEST.tex` is still the
zeta/Gamma manuscript; its advisory recommendation was raw-only at
Oracle passed the proof and requested only notation/dependency hygiene, now
patched.  This is not a terminal \(M_{P_k}(\theta)\), \(U_k(\theta)\), or
\(R_P(\theta)\) theorem.  The next target is a mass-to-defect theorem:
positive high-support pair-link-free mass must be forced out of the exact
endpoint-tower model and charged to the mixed-overlap budget from
`mrw-bc27191b14d4`, or else a genuinely new terminal-core residual estimate is
needed.

20260521T084930Z update: the endpoint-fiber mixture branch has been reduced
to an exact self-similar variational identity.  New proposition
`mrw-fe13472e08c8` proves that for finite \(P=Z\sqcup X\sqcup Y\), product
law \(\nu_P\), threshold \(L\), and exact one-from-each assemblies with
pair-link-free endpoint fibers,
\[
\sup_{\mathcal A}
\nu_P(\mathcal A\cap\{S:|S|>L\})
=
\alpha_X\beta_Y\,\mathfrak M_Z(L-2),
\]
where \(\alpha_X\beta_Y\) is the probability of selecting exactly one endpoint
from each endpoint class and \(\mathfrak M_Z(L-2)\) is the shifted optimal
pair-link-free core residual on \(Z\).  Thus heterogeneous endpoint fibers
give no advantage over one equal extremal core fiber in every endpoint pair.
Scout again returned the known attachment-mismatch blocker because
`THEORY_LATEST.tex` is still the zeta/Gamma manuscript; it was ingested
raw-only at
Oracle passed the local proof and requested only dependency hygiene, now
patched on `mrw-fe13472e08c8`.  This is not a terminal
\(M_{P_k}(\theta)\), \(U_k(\theta)\), or \(R_P(\theta)\) theorem.  The next
target is to prove that positive high-support mass must leave the exact
one-from-each normal form and pay the mixed-overlap defects from
`mrw-bc27191b14d4`, or else prove a stronger shifted core residual theorem
that breaks the self-similar reduction.

20260521T081052Z update: the exact coherent two-class assembly has now been
tested against full pair-link intervals.  New proposition `mrw-d7b3299d3813`
proves that for a finite disjoint decomposition \(P=Z\sqcup X\sqcup Y\) and
endpoint fibers \(\mathcal R_{xy}\subseteq2^Z\), the assembly
\[
\mathcal A=\{R\cup\{x,y\}:x\in X,\ y\in Y,\ R\in\mathcal R_{xy}\}
\]
is pair-link-free in \(2^P\) if and only if every fixed endpoint-pair fiber
\(\mathcal R_{xy}\) is pair-link-free in \(2^Z\).  Pair-link triples cannot
mix endpoint pairs: if \(A,B\) use different \(X\)-endpoints or different
\(Y\)-endpoints, then every \(C\in I(A,B)\) would contain two points of that
endpoint class, contradicting the exact one-from-each form.  The product-law
mass decomposes as
\[
\nu_P(\mathcal A)=
\sum_{x\in X}\sum_{y\in Y}\alpha_x\beta_y\,\nu_Z(\mathcal R_{xy}),
\]
with the high-support cutoff shifted by \(+2\) in each core fiber.  Scout again
returned the known attachment-mismatch blocker because `THEORY_LATEST.tex` is
the zeta/Gamma manuscript; it was ingested raw-only at
Focused Oracle passed the proof and requested only dependency hygiene, which
is patched.  This is not a terminal \(M_{P_k}(\theta)\), \(U_k(\theta)\), or
\(R_P(\theta)\) theorem.  The next target is the endpoint-fiber mixture
obstruction: prove that positive high-support mass cannot be carried by the
weighted sum of pair-link-free core fibers, or prove that any positive-mass
candidate must leave the exact one-from-each normal form and pay the mixed
overlap defects from `mrw-bc27191b14d4`.

20260521T073215Z update: the pairwise relative-parity filter has been
aggregated into a component-level normalized mixed-overlap bound.  New
proposition `mrw-bc27191b14d4` proves that if \(H\) is the complete robust
side-overlap multigraph on a finite corridor set and \(K\) is a
parity-consistent connected component with potential \(\epsilon_i\), then the
normalized sides
\[
\widehat S_i^a=S_i^{a+\epsilon_i\pmod2}
\]
have all mixed normalized overlaps charged to side defects:
\[
i\ne j,\quad a\ne b
\quad\Longrightarrow\quad
w(\widehat S_i^a\cap\widehat S_j^b)
\le
\widehat D_i^a+\widehat D_j^b.
\]
Consequently,
\[
\sum_{\{i,j\}\subseteq K}\sum_{a\ne b}
w(\widehat S_i^a\cap\widehat S_j^b)
\le
(|K|-1)\sum_{i\in K}(D_i^0+D_i^1).
\]
In the complete case, mixed normalized overlaps between distinct corridors
have zero weight.  Scout returned an attachment-mismatch blocker because the
current `THEORY_LATEST.tex` is still the zeta/Gamma manuscript rather than an
Erdos 536 corridor theory; the response was ingested raw-only at
Focused Oracle passed the proof and requested only wording/dependency hygiene,
which is patched.  This remains nonterminal local progress, not
\(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or an \(R_P(\theta)\) lift.  The
next target is to prove that positive high-support mass creates enough
same-component mixed-overlap mass to contradict this defect budget, or else
construct the coherent two-class signature-potential assembly and test every
full pair-link interval plus any possible \(R_P(\theta)\) lift.

20260521T065018Z update: the coherent signature-potential assembly now has a
pairwise relative-parity overlap filter.  New proposition `mrw-10ea41c73237`
proves that for two near-complete lower corridors \(i,j\), if one side pair
\((b,c)\) has robust overlap
\[
O_{bc}=w(S_i^b\cap S_j^c)>D_i^b+D_j^c
\]
and \(p=b+c\pmod2\), then the corridor signatures have relative parity
\[
\tau_j=\operatorname{comp}^p(\tau_i),
\]
and every opposite-parity side pair is defect-small:
\[
b'+c'\not\equiv p\pmod2
\quad\Longrightarrow\quad
w(S_i^{b'}\cap S_j^{c'})
\le D_i^{b'}+D_j^{c'}.
\]
Equivalently,
\[
O^{(1-p)}_{ij}\le D_i^0+D_i^1+D_j^0+D_j^1.
\]
In the complete case \(\lambda_i=\lambda_j=1\), positive shared side support
between two corridors can occur in at most one relative parity.  Scout returned
the same filter as an advisory patch but was ingested raw-only at
Oracle passed the proof and requested only dependency hygiene, so
`mrw-a082a34f6797` is recorded as contextual rather than a formal parent.  This
is still not a terminal \(M_{P_k}(\theta)\), \(U_k(\theta)\), or
\(R_P(\theta)\) lift.  The next target is to aggregate these pairwise
forbidden-parity bounds over a coherent robust component to force accumulated
near-purity defect, or construct a two-class assembly satisfying the filter
and test every full pair-link interval plus any possible \(R_P(\theta)\) lift.

20260521T060947Z update: the parity-consistent branch now has an explicit
signed-potential normal form.  New proposition `mrw-a082a34f6797` proves that
in the setting of `mrw-750fb7a7e30c`, any finite loopless multigraph of robust
side-overlap edges has componentwise parity potentials.  If an edge \(e\) with
endpoints \(i,j\) tests \(S_i^{s_e(i)}\cap S_j^{s_e(j)}\), with
\[
p_e=s_e(i)+s_e(j)\pmod 2,
\]
then each connected component \(K\) has \(\epsilon_i\in\{0,1\}\) satisfying
\[
\epsilon_i+\epsilon_j=p_e\pmod 2.
\]
For a root signature \(\rho\), all selected corridor signatures are forced by
\[
\tau_i=\operatorname{comp}^{\epsilon_i}(\rho),
\]
and each oriented side \(S_i^b\) has selected pure signature
\[
\operatorname{comp}^{\epsilon_i+b}(\rho).
\]
In the complete case \(\lambda_i=1\), every positive-weight point of
\(S_i^b\) lies in that pure class.  Oracle passed the proof after requiring
incidence-based edge labels for multigraphs; the patch is applied.  Scout
created only the request/response scaffold for this branch, so no Scout claim
was promoted.  This is still not a terminal \(M_{P_k}(\theta)\),
\(U_k(\theta)\), or \(R_P(\theta)\) lift.  The next target is to prove that
positive high-support pair-link-free mass forces a robust odd-parity
side-overlap component, or to test the resulting two-class coherent
signature-potential assembly against every full pair-link interval and any
possible \(R_P(\theta)\) lift.

20260521T052939Z update: corridor-family overlap now has a signed parity
consistency test.  New proposition `mrw-750fb7a7e30c` proves that for a finite
family of near-complete lower corridors in one inherited ancestor-signature
system, a robust overlap edge between oriented sides imposes a parity relation
on the chosen near-pure signatures.  Robust same-side overlaps force equality
of selected signatures, while robust cross-side overlaps force complementary
selected signatures.  Consequently, every fully robust side-overlap cycle has
even total side parity; an odd-parity cycle must contain an edge whose overlap
is bounded by the corresponding near-purity defects.  In the complete case,
an odd-parity cycle must have a zero-weight tested overlap.  Scout returned a
useful family-overlap sketch but was ingested raw-only at
Focused Oracle failed because the Chrome window closed before completion and
returned no mathematical content.  This is still not a terminal
\(M_{P_k}(\theta)\), \(U_k(\theta)\), or \(R_P(\theta)\) lift.  The next
target is to prove that positive high-support mass forces a robust odd-parity
corridor-overlap cycle, or else construct the parity-consistent signature-tree
assembly and test every full pair-link interval.

20260521T045012Z update: global near-purity assembly now has a local overlap
packing tool.  New proposition `mrw-206678825c7a` proves that if two
near-complete inherited-signature corridors \(U_j|W_j\) share the same
ancestor-signature system and have edge masses
\[
M_Q(U_j,W_j)\ge\lambda_jA_jB_j,\qquad 1/2\le\lambda_j\le1,
\]
then any chosen near-pure signatures \(\tau_j\) supplied by
`mrw-36595780824f` control side overlap.  For example,
\[
\tau_1\ne\tau_2
\quad\Longrightarrow\quad
w(U_1\cap U_2)
\le
(1-\lambda_1)A_1+(1-\lambda_2)A_2,
\]
with analogous \(W_1\cap W_2\), \(U_1\cap W_2\), and \(W_1\cap U_2\) bounds.
Thus incompatible signature choices cannot reuse substantial weighted side
mass except through the near-purity defects.  Scout returned only malformed
source fragments and was ingested raw-only at
the ChatGPT usage limit and supplied no mathematical content.  This is still
not a terminal \(M_{P_k}(\theta)\), \(U_k(\theta)\), or \(R_P(\theta)\) lift.
The next target is to produce a global source of many near-complete corridors
with overlapping side mass, then use `mrw-206678825c7a` to force accumulated
defect or a coherent signature-tree normal form.

20260521T040944Z update: exact ancestor-signature inheritance now has a
near-complete weighted form.  New proposition `mrw-36595780824f` proves that
under the ancestor complete-bipartite slice hypotheses of `mrw-fced7420b905`,
if \(U,W\subseteq V\) are disjoint weighted sides with positive side masses
\[
A=\sum_{u\in U}a_u,\qquad B=\sum_{w\in W}b_w,
\]
and signature weights
\[
A_\tau=\sum_{u\in U\cap V_\tau}a_u,\qquad
B_\tau=\sum_{w\in W\cap V_\tau}b_w,
\]
then the lower edge mass obeys
\[
M_Q(U,W)\le\sum_{\tau}A_\tau B_{\bar\tau}.
\]
Consequently, if \(1/2\le\lambda\le1\) and
\[
M_Q(U,W)\ge\lambda AB,
\]
then some inherited complementary ancestor-signature pair carries at least a
\(\lambda\)-fraction of the weight on both sides:
\[
A_{\tau^*}\ge\lambda A,\qquad
B_{\bar\tau^*}\ge\lambda B.
\]
In equality, all positive side weight is supported on one complementary
ancestor-signature pair and all positive-product pairs across those supports
are lower edges.  Focused Oracle passed the proposition and caught an endpoint
tie issue at \(\lambda=1/2\); the proof was patched here and in the older
near-full node `mrw-8a0c228a0166`.  Scout returned only the fragment `CAND` and
Scout claim was promoted.  This is still local progress only, not
\(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or an \(R_P(\theta)\) lift.  The
next target is global: prove that positive high-support mass forces
incompatible near-purity requirements across many corridors, or construct a
coherent signature-tree assembly and test every full pair-link interval plus
any possible \(R_P(\theta)\) lift.

20260521T033055Z update: coherent-corridor assembly now has an ancestor
signature-purity test.  New proposition `mrw-49eaa53e7ffe` proves that if
\(Q\subseteq R_i\) for \(1\le i\le m\), the upper slice graphs
\(G_{R_i}^{\mathcal F}\) contain complete bipartite graphs \(K_{X_i,Y_i}\) on
one common vertex set \(V=X_i\sqcup Y_i\), and the lower slice contains a
complete bipartite corridor \(K_{U,W}\subseteq G_Q^{\mathcal F}[V]\), then the
whole lower corridor inherits a single ancestor signature:
\[
U\subseteq V_\tau,\qquad
W\subseteq V_{\mathbf 1-\tau}
\]
for some \(\tau\in\{0,1\}^m\).  The weighted equality form says that if
nonnegative side weights have positive masses and lower edge mass across
\(U|W\) equals the full product side mass, then the positive-weight supports
are contained in one complementary ancestor-signature pair.  Focused Oracle
confirmed the proof, requested the explicit \(m\ge1\) wording, and warned that
missing incompatible positive-weight pairs give strict but not uniform loss.
Scout returned only a one-character response and was ingested raw-only at
This is not a terminal \(M_{P_k}(\theta)\), \(U_k(\theta)\), or
\(R_P(\theta)\) theorem.  The next target is to show that positive high-support
mass forces incompatible inherited ancestor signatures across many complete
or near-complete corridors, or to construct a coherent signature-tree assembly
and test all full pair-link intervals plus any possible \(R_P(\theta)\) lift.

20260521T025048Z update: repeated dominant-pair persistence now has a local
coherent normal form.  New proposition `mrw-827094b15843` proves that, for one
fixed coarse complementary corridor \(A=V_\tau\), \(B=V_{\bar\tau}\) refined
by \(\ell\) nested upper cuts, any near-full lower corridor
\[
M_Q(A,B)\ge\lambda W_AW_B,\qquad 1/2\le\lambda\le1,
\]
has a full refined signature \(\omega^*\) such that
\[
\alpha_{\omega^*}\ge\lambda W_A,\qquad
\beta_{\bar\omega^*}\ge\lambda W_B.
\]
Moreover the same \(\omega^*\) gives a coherent prefix chain through every
intermediate refinement depth:
\[
\alpha^{(t)}_{\omega^*_{\le t}}\ge\lambda W_A,\qquad
\beta^{(t)}_{\overline{\omega^*_{\le t}}}\ge\lambda W_B
\qquad(0\le t\le\ell).
\]
In the equality case \(M_Q(A,B)=W_AW_B\), all positive side weight lies in one
complementary refined-signature pair and the lower graph is complete on those
positive-weight supports, up to zero-weight pairs.  This packages
`mrw-8a0c228a0166` into the exact local normal form for a persistent heavy
corridor.  It is not a global anti-alignment exhaustion theorem and proves no
\(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or \(R_P(\theta)\) lift.  Scout
returned malformed source-fragment text and was ingested raw-only at
local corollary and the equality-case completeness caveat.  The next target is
global: prove that positive-mass high-support pair-link-free families cannot
assemble many coherent normal-form corridors without creating a full pair-link
interval hit, or construct such an assembly and test every full pair-link
interval plus any possible \(R_P(\theta)\) lift.

20260521T021237Z update: the near-equality case of corridor refinement is now
classified.  New proposition `mrw-8a0c228a0166` proves that, in the setting of
`mrw-a9efecc818c7`, if a coarse complementary corridor \(A|B\) has positive
side weights and normalized refined-signature distributions
\[
p_\omega=\frac{\alpha_\omega}{W_A},\qquad
q_\omega=\frac{\beta_\omega}{W_B},
\]
then
\[
M_Q(A,B)
\le
W_AW_B\sum_\omega p_\omega q_{\bar\omega}.
\]
Consequently, if \(1/2\le\lambda\le1\) and
\[
M_Q(A,B)\ge\lambda W_AW_B,
\]
then one complementary refined-signature pair carries at least a
\(\lambda\)-fraction of the weight on both sides:
\[
\alpha_{\omega_0}\ge\lambda W_A,\qquad
\beta_{\bar\omega_0}\ge\lambda W_B.
\]
In the equality case \(M_Q(A,B)=W_AW_B\), the positive-weight support is
refined-signature pure: all \(A\)-weight lies in one \(A_{\omega_0}\) and all
\(B\)-weight lies in \(B_{\bar\omega_0}\).  Scout returned off-route
polygamma/zeta-tail candidates and was ingested raw-only at
local proposition and recommended the "concentration" wording for the
near-full case.  This is still not a global mass theorem and proves no
\(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or \(R_P(\theta)\) lift.  The
next target is global: prove repeated dominant complementary refined-signature
pairs cannot persist at positive high-support mass without collapsing into a
rigid fixed/coherent corridor normal form, or construct that normal form and
test every full pair-link interval plus any possible \(R_P(\theta)\) lift.

20260521T012914Z update: the heavy-corridor side of the
signature-fragmentation dichotomy now has a quantitative refinement test.
New proposition `mrw-a9efecc818c7` proves that if \(m\ge1\) coarse nested
upper cuts select a complementary signature corridor
\[
A=V_\tau,\qquad B=V_{\bar\tau},
\]
and \(\ell\ge1\) further nested upper cuts refine \(A\) and \(B\) into classes
\(A_\omega,B_\omega\), then every lower edge across \(A|B\) must lie in a
refined anti-corridor.  With nonnegative weights and
\[
\alpha_\omega=\sum_{a\in A_\omega}w_a,\qquad
\beta_\omega=\sum_{b\in B_\omega}w_b,
\]
the lower edge mass satisfies
\[
M_Q(A,B)
\le
\sum_{\omega\in\{0,1\}^{\ell}}\alpha_\omega\beta_{\bar\omega}.
\]
For one added cut this becomes the exact capacity identity
\[
M_Q(A,B)\le
\alpha_0\beta_1+\alpha_1\beta_0
=
W_AW_B-(\alpha_0\beta_0+\alpha_1\beta_1).
\]
Thus a \((1-\varepsilon)\)-heavy corridor can survive the added cut only if
the same-side weighted product obeys
\[
\alpha_0\beta_0+\alpha_1\beta_1\le\varepsilon W_AW_B.
\]
This is a local anti-alignment theorem, not a global mass theorem and not a
proof of \(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or an
\(R_P(\theta)\) lift.  Scout returned malformed source-fragment text and was
Oracle confirmed the proposition after a retry and the unordered-edge/weight
notation cleanup; the response is advisory only.

20260521T005033Z update: the nested-bipartition frontier now has a quantitative
signature-fragmentation bound.  New proposition `mrw-816fd32c3294` proves that
under the hypotheses of `mrw-fced7420b905`, with \(m\ge1\) nested upper
complete bipartite blocks on a common vertex set \(V\), arbitrary nonnegative
weights \(a_v\), signature class weights \(W_\tau\), and lower slice edge mass
\[
M_Q(V)
=
\sum_{\{u,v\}\in E_Q^\mathcal F\cap\binom V2}a_u a_v,
\]
one has
\[
M_Q(V)
\le
\sum_{\{\tau,\bar\tau\}}W_\tau W_{\bar\tau}.
\]
Consequently, if \(W=\sum_\tau W_\tau>0\) and
\(\rho=\max_\tau W_\tau/W\), then
\[
M_Q(V)\le\frac{\rho}{2}W^2.
\]
Thus fragmented signatures force small lower edge mass, while
\(M_Q(V)\ge\delta W^2\) forces both a class of weight at least \(2\delta W\)
and a complementary signature pair with
\[
W_\tau W_{\bar\tau}\ge \frac{\delta}{2^{m-1}}W^2.
\]
This is still not a global mass theorem and gives no \(M_{P_k}(\theta)\),
\(U_k(\theta)\), or \(R_P(\theta)\) vanishing result.  Its value is a precise
dichotomy: either many independent upper cuts fragment the lower slice, or a
heavy complementary corridor remains and must be tested as a stable
non-product assembly.  Scout again returned the explicitly quarantined routine
\(s=9\) inverse-tail route and was ingested raw-only at
new proposition as a local weighted corollary, with only the \(W>0\) caveat
already reflected in the node; the advisory response is stored at
and is not used as proof.

20260521T001014Z update: fixed complete-bipartite global assemblies are now
classified, and Scout supplied one locally audited nested-core coherence patch.
Proposition `mrw-c7c76faed872` proves that if \(X,Y\subseteq P\) are disjoint
nonempty sets, \(Z=P\setminus(X\cup Y)\), and
\[
\mathcal B(\mathcal R;X,Y)
=\{R\cup\{x,y\}:R\in\mathcal R,\ x\in X,\ y\in Y\},
\]
then \(\mathcal B(\mathcal R;X,Y)\) is pair-link-free in \(2^P\) if and only
if \(\mathcal R\) is pair-link-free in \(2^Z\).  Under any product law,
\[
\nu_P(\mathcal B(\mathcal R;X,Y))
=\alpha_X\alpha_Y\nu_Z(\mathcal R),
\]
and high-support thresholds transfer exactly by the support shift
\(|R|\mapsto |R|+2\).  Thus the direct fixed-\(X,Y\) complete bipartite
blow-up is not a new positive-mass counterexample route; it is a
lower-dimensional copy of the original pair-link problem.

The locally audited Scout patch `mrw-fced7420b905` proves a nested-core version
of the path-shadow obstruction.  If \(Q\subseteq R\) and \(G_R^\mathcal F\) is
the two-extension slice graph of a pair-link-free family, then
\[
E_Q^\mathcal F\cap P_2(G_R^\mathcal F)=\varnothing.
\]
Consequently, an upper complete bipartite block \(K_{X,Y}\subseteq G_R\)
forces the lower graph \(G_Q[X\cup Y]\) to be bipartite for the same cut
\(X|Y\).  Multiple upper bipartitions over \(R_i\supseteq Q\) force every lower
edge on a common vertex set to join complementary signature classes.  This is
still not a mass theorem, not \(M_{P_k}(\theta)\to0\), not
\(U_k(\theta)\to0\), and not an \(R_P(\theta)\) lift.  The next executable
target is quantitative: prove that positive-mass high-support pair-link-free
families must create enough incompatible upper bipartitions to make the
complementary-signature lower graphs negligible or contradictory, or construct
a genuine non-product dense-slice assembly and test every full pair-link
interval.
only the locally re-proved nested-core patch was promoted.  Focused Oracle
confirmed both new propositions after the nondegenerate \(K_{X,Y}\) wording
patch in `mrw-fced7420b905`; the response remains advisory and is cited only
as an audit artifact.

20260520T233725Z update: path-shadow overlap collapse now has a local sharpness
stress test.  Proposition `mrw-f83b56a1aa89` proves that a fixed-core complete
bipartite slice
\[
\mathcal F_{R,X,Y}=\{R\cup\{u,v\}:u\in X,\ v\in Y\}
\]
is pair-link-free, has empty endpoint-pair core for same-side endpoints
\(x,z\in X\), and makes the \(Q\)-overlap bottleneck from
`mrw-c6d0c6fa4d30` asymptotically sharp under product measure.  The important
correction, caught by Oracle before promotion, is that middle vertices in
\(R\) also create path shadows:
\[
\mathcal P^r_{xz}=\{(R\setminus\{r\})\cup\{y\}:y\in Y\}.
\]
After including these \(R\)-middle shadows, the ordered diagonal-including
\(Q\) formula is correct and shows that complete bipartite core slices can
force genuine quadratic off-diagonal overlap collapse.  This is a local
obstruction, not a positive-mass high-support counterexample, not a proof of
\(U_k(\theta)\to0\), and not an \(R_P(\theta)\) lift.  Scout again returned
routine \(s=9\) tail-floor material and was ingested raw-only.  The next
executable target is global: prove that positive-mass high-support
pair-link-free families cannot coherently assemble many such collapsed
bipartite core blocks, or construct such a coherent family and test every full
pair-link interval.

20260520T114136Z update: path-shadow lower-shadow quantification now has a
proved overlap-bottleneck proposition.  Proposition `mrw-c6d0c6fa4d30` proves
that for a pair-link-free \(\mathcal F\subseteq2^P\), fixed distinct endpoints
\(x,z\), endpoint-pair core
\[
\mathcal E_{xz}=\{D\subseteq P\setminus\{x,z\}:D\cup\{x,z\}\in\mathcal F\},
\]
and \(y\)-augmented path shadows \(\mathcal S^y_{xz}\) generated by two-edge
paths \(R\cup\{x,y\},R\cup\{y,z\}\), one has
\[
\mathcal E_{xz}\cap\bigcup_y\mathcal S^y_{xz}=\varnothing.
\]
Moreover, for any probability measure \(\mu\) on \(2^{P\setminus\{x,z\}}\),
if
\[
T=\sum_y\mu(\mathcal S^y_{xz}),\qquad
Q=\sum_{y,y'}\mu(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz}),
\]
where \(Q\) is the ordered double sum including diagonal terms, then for
\(T>0\)
\[
\mu\left(\bigcup_y\mathcal S^y_{xz}\right)\ge \frac{T^2}{Q},
\qquad
\mu(\mathcal E_{xz})+\frac{T^2}{Q}\le1.
\]
Under the prime-biased product law, each individual shadow has mass at least
the corresponding path-core mass after deleting \(x,y,z\).  This still does
not prove \(U_k(\theta)\to0\), \(M_{P_k}(\theta)\to0\), or any lift to
\(R_P(\theta)\); it isolates the next obstruction: positive endpoint-pair core
mass plus abundant paths can survive only through heavy overlap collapse among
the shadows \(\mathcal S^y_{xz}\).  Scout again returned malformed material
and pointed to the explicitly rejected routine \(s=9\) tail-floor route, so it
was ingested raw-only.  Focused Oracle confirmed the proof, required the
ordered-diagonal wording for \(Q\), and recommended quantifying
\(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz}\) under prime-biased measure next.

20260520T110040Z update: cross-core pair-link coherence now has a proved
path-shadow proposition.  Proposition `mrw-2bcc2955fe38` proves that if
\(\mathcal F\subseteq2^P\) is pair-link-free and a two-extension slice contains
the path
\[
R\cup\{x,y\},\qquad R\cup\{y,z\},
\]
then every endpoint-pair completion
\[
D\cup\{x,z\},\qquad D\subseteq R\cup\{y\},
\]
is excluded from \(\mathcal F\).  Equivalently, for fixed endpoints \(x,z\),
the endpoint-pair core family is disjoint from the \(y\)-augmented lower shadow
of the corresponding path-core family.  Thus a complete bipartite local Mantel
extremizer cannot be repeated across cores without casting lower-core
forbidden shadows on same-side endpoint pairs.  This is not a mass theorem and
does not prove \(U_k(\theta)\to0\), \(M_{P_k}(\theta)\to0\), or any lift to
\(R_P(\theta)\), but it replaces the exhausted direct weighted-Mantel route by
a precise product-measure shadow target.  Scout again returned malformed source
fragments and was ingested raw-only.  Focused Oracle first failed with
`Chrome window closed before oracle finished`; a compact `--browser-inline-files`
retry confirmed the proof and warned that the next step must quantify the path
shadows under the prime-biased product law.

20260520T102016Z update: weighted cross-core aggregation now has a proved
second-support-moment bound.  Proposition `mrw-a32a6d3a5f20` proves that if
\(\mathcal F\subseteq2^P\) is pair-link-free under a product law
\(\nu(p\in A)=q_p\), with odds weights \(a_p=q_p/(1-q_p)\) and
\[
W(R)=\sum_{p\notin R}a_p,
\]
then
\[
\sum_{A\in\mathcal F}\binom{|A|}{2}\nu(A)
\le
\frac14\sum_{R\subseteq P}\nu(R)W(R)^2.
\]
For the prime-biased law \(q_p=1/p\), this gives
\[
\sum_{A\in\mathcal F}\binom{|A|}{2}\nu_P(A)
\le
\frac14\left(S_P^2+\sum_{p\in P}\frac1{p^2(p-1)}\right).
\]
Thus pair-link-free families inside \(H_{P,\theta}\) have only the constant
limsup bound \(\nu_{P_k}(\mathcal F_k)\le 1/(2\theta^2)+o(1)\) from this
method.  The theorem is a real global aggregation of the triangle-free
two-extension slices, but it is nonterminal: it does not apply to arbitrary
union-free families and does not prove \(U_k(\theta)\to0\),
\(M_{P_k}(\theta)\to0\), or any lift to \(R_P(\theta)\).  Scout again returned
malformed source fragments and was ingested raw-only.  Focused Oracle confirmed
the proof and recommended the next target: a cross-core Mantel-defect or
stability/coherence theorem forcing \(o(S_P^2)\) aggregate slice mass, or an
explicit near-extremal coherent dense-slice construction tested against the
full pair-link interval criterion.

20260520T030334Z update: the sparse pair-link hypergraph route now has a
common-core link-graph constraint.  Proposition `mrw-354b105d4977` proves that
if \(\mathcal F\subseteq2^P\) is pair-link-free, then for every \(R\subseteq P\)
the two-extension slice graph
\[
G_R^\mathcal F=(P\setminus R,E_R^\mathcal F),
\qquad
\{x,y\}\in E_R^\mathcal F
\Longleftrightarrow
R\cup\{x,y\}\in\mathcal F
\]
is triangle-free.  Hence each fixed core has the sharp local bound
\[
|E_R^\mathcal F|
\le
\left\lfloor |P\setminus R|^2/4\right\rfloor.
\]
This packages and strengthens the one-swap insertion-fiber obstruction as a
link-graph theorem, but it is still nonterminal: complete bipartite slices show
the Mantel bound is locally sharp and has no standalone prime-biased mass
consequence.  Scout completed but returned unrelated zeta/Nantomah, \(s=9\),
and polygamma material, so it was ingested raw-only.  Focused Oracle confirmed
the proof and warned against summing per-core Mantel bounds, claiming
\(U_k(\theta)\to0\), or treating dense bipartite slices as global
counterexamples.  The next frontier is weighted cross-core aggregation of these
triangle-free slices, or an explicit coherent dense-slice construction tested
against full pair-link intervals and any lift to \(R_P(\theta)\).

20260520T022056Z update: the sparse pair-link hypergraph route now has its
first local independent-set constraint.  Proposition `mrw-25cdd8da0601` proves
that if \(\mathcal F\subseteq2^P\) is pair-link-free and \(A\in\mathcal F\),
then every one-swap insertion fiber
\[
D_y^{\mathcal F}(A)
=
\{x\in A:(A\setminus\{x\})\cup\{y\}\in\mathcal F\}
\]
has size at most one for each \(y\in P\setminus A\).  Consequently the
Johnson one-swap neighborhood of \(A\) inside \(\mathcal F\) has size at most
\(|P\setminus A|\), rather than the ambient \(|A||P\setminus A|\).
This is a genuine structural statement about independent sets in the
three-uniform pair-link hypergraph, not projection-only, endpoint-degree, or
rectangle evidence.  It is still nonterminal: it controls only same-rank
one-swap neighbors, not unequal-rank neighborhoods or larger same-rank
Hamming-distance slices, and it has no standalone prime-biased mass
consequence.  Scout was ingested raw-only after a malformed source-fragment
response.  Focused Oracle first failed with `Chrome window closed before oracle
finished`, then a compact `--browser-inline-files` retry confirmed the proof
and caveats.  The next frontier is a weighted one-swap expansion theorem
forcing same-insertion collisions in every positive-mass high-support
pair-link-free/union-free candidate, or an explicit positive-mass low-expansion
counterexample tested against full pair-link intervals and any lift to
\(R_P(\theta)\).

20260520T014549Z update: projection-level rare-pair arguments are now
quarantined.  Proposition `mrw-b1f87c9d6a42` proves that every exact rank layer
\(\binom Pr\), \(2\le r\le |P|-1\), has full genuine pair-link projection:
for every \(A\in\binom Pr\) there are distinct \(B,C\in\binom Pr\) with
\[
C\in I^\circ(A,B).
\]
Consequently, for the full capped band
\[
\mathcal B_{k,\theta,\alpha}
=\{A\subseteq P_k:\theta S_k<|A|\le\alpha S_k\},
\]
every vertex lies in the first-coordinate projection of the genuine pair-link
relation for all sufficiently large \(k\), while `mrw-4f1e9a2d6b73` and
`mrw-6d4a8b0f2c91` still give \(O(S_k^{-1})\) random-pair visibility and no
positive endpoint cores/rectangles under their cap hypotheses.  This is not a
counterexample and not a proof of \(U_k(\theta)\to0\); it kills the inference
"rare relation means most vertices have no local pair-link witness."  The next
frontier is the sparse three-uniform pair-link hypergraph on positive-mass
subfamilies, a union-specific container/deletion-trace theorem, or an explicit
positive-mass family whose rare relation has full or near-full projection but
still avoids all pair-link/union triples.

20260520T010053Z update: capped pair-link sparsity now has endpoint and
rectangle forms.  Corollary `mrw-6d4a8b0f2c91` proves that in every fixed cap
\[
\theta S_k<|A|\le\alpha S_k<2\theta S_k,
\]
if \(\mathcal F_k\) has \(\nu_{P_k}(\mathcal F_k)\ge\eta\) and
\(\lambda_k=\nu_{P_k}(\cdot\mid\mathcal F_k)\), then the capped union relation
\(R^\cup(A,B)\iff A\cup B\in\mathcal F_k\) and the full pair-link relation
\(R^I(A,B)\iff I(A,B)\cap\mathcal F_k\ne\varnothing\) satisfy
\[
\int d_R(A)\,d\lambda_k(A)
=
(\lambda_k\times\lambda_k)(R)
=O_{\eta,\theta,\alpha}(S_k^{-1}).
\]
Consequently no positive-mass endpoint set can have fixed-positive capped
union or pair-link neighborhood degree, and no positive-mass product rectangle
can lie inside these relations.  This is a route-kill, not a proof of
\(U_k(\theta)\to0\): the next frontier is the rare exceptional relation set
\[
E_k=\{(A,B):I(A,B)\cap\mathcal F_k\ne\varnothing\},
\qquad
\lambda_k^{\otimes2}(E_k)=O(S_k^{-1}),
\]
a union-specific hypergraph/container mechanism, fair-thinning upward
boundary, or a non-capped argument.

20260520T001456Z update: capped random-pair union and pair-link averaging is
now quarantined as a terminal route.  Corollary `mrw-4f1e9a2d6b73` proves that
if \(0<\theta<1\), \(\theta<\alpha<2\theta\), and
\(\mathcal F_k\subseteq\{\theta S_k<|A|\le\alpha S_k\}\) has
\(\nu_{P_k}(\mathcal F_k)\ge\eta\), then for conditioned independent
\(X,Y\in\mathcal F_k\),
\[
\Pr(X\cup Y\in\mathcal F_k)=O(S_k^{-1})
\]
and, for the full pair-link interval \(I(X,Y)\),
\[
\Pr(I(X,Y)\cap\mathcal F_k\ne\varnothing)=O(S_k^{-1}).
\]
The proof is a direct cap-to-overlap implication plus the entropy-overlap bound
`mrw-c7f4e0c9a821`.  Thus a random-pair supersaturation proof inside a fixed
cap cannot force the weighted union-free theorem; the next frontier must use
the rare high-overlap pair geometry, a union-specific rooted
hypergraph/container mechanism, fair-thinning upward boundary, or a non-capped
argument.

20260519T233444Z update: the mixed overlap-graph frontier is now sharpened by
an entropy overlap-energy invariant.  Proposition `mrw-c7f4e0c9a821` proves
that for any positive-mass family \(\mathcal F\subseteq2^P\),
\[
\mathbb E_{\nu_P(\cdot\mid\mathcal F)^{\otimes2}}|X\cap Y|
\le
4\sum_{p\in P}\frac1{p^2}+2\log\frac1{\nu_P(\mathcal F)}.
\]
Thus if \(\nu_{P_k}(\mathcal F_k)\ge\eta\), then the conditional edge density
of the \(\gamma S_k\)-overlap graph is \(O_{\eta,\gamma}(S_k^{-1})\), and any
cover by internally \(\gamma S_k\)-intersecting clusters requires
\(\Omega_{\eta,\gamma}(S_k)\) clusters.  Together with `mrw-7c6a0e9f2d31` and
`mrw-18e9c7b0a5af`, a surviving positive-mass #536 obstruction must be a
linear-many-cluster sparse overlap graph: no positive-mass low-overlap
independent part, vanishing high-overlap edge density, and no sublinear
high-overlap clique cover.  The next frontier is a measured sparse-overlap
graph theorem using union-free/pair-link structure, or an explicit
linear-many-cluster counterexample tested against full pair-link intervals.

20260519T225444Z update: high-intersection clique templates are now killed
under the prime-biased product measure.  Proposition `mrw-18e9c7b0a5af` proves
that if \(\mathcal F\subseteq2^P\) has \(|A|\ge t\) for every member and
\(|A\cap B|\ge t\) for every distinct pair, then
\[
\nu_P(\mathcal F)
\le
\left(\frac{\sum_{p\in P}p^{-2}}{t}\right)^{1/2}.
\]
Since \(\sum_p p^{-2}<\infty\), any internally
\(\gamma S_k\)-intersecting subfamily of \(H_{k,\theta}\) has mass
\(O_\gamma(S_k^{-1/2})\), and any cover by \(o(\sqrt{S_k})\) such
high-intersection cliques has vanishing mass.  Together with the private-shadow
bound `mrw-7c6a0e9f2d31`, this says a positive-mass #536 obstruction cannot be
a sparse-intersection code and cannot be one or few high-overlap clusters.  The
next frontier is a mixed overlap-graph theorem, or an explicit many-cluster
counterexample tested against full pair-link intervals and the \(R_P(\theta)\)
lift.

20260519T173438Z update: sparse-intersection high-support code templates are
now killed directly under the prime-biased product measure.  Proposition
`mrw-7c6a0e9f2d31` proves a weighted private-shadow bound: if every member has
size at least \(r\) and all distinct intersections have size \(<t\), then
\[
\nu_P(\mathcal F)\le
\frac{\nu_P(|X|=t)}{\binom r t}
\le
\binom r t^{-1}.
\]
Consequently any family inside \(H_{k,\theta}\) with pairwise intersections
\(<\gamma S_k\), for fixed \(0<\gamma<\theta\), has vanishing
\(\nu_{P_k}\)-mass.  In an upper capped band
\(\theta S_k<|A|\le\alpha S_k\) with \(\alpha<2\theta\), this eliminates the
natural broad low-overlap union-free and pair-link-free code template.  For
\(\theta>1/2\), any positive-mass capped pair-link obstruction must therefore
contain linearly large intersections somewhere.  The next #536 frontier is a
high-intersection clustering theorem, or a genuine positive-mass clustered
counterexample tested against full pair-link intervals and the \(R_P(\theta)\)
lift.

20260519T165434Z update: near-total-root visibility is now closed as a
separate #536 target.  Proposition `mrw-4b9f5c2e6a1d` proves that for every
\(B\ge0\), the supremum of high-support union-free families satisfying a
bounded-outside-variance comparable-pair visibility condition is exactly the
original \(U_k(\theta)\), because \(J=P_k\) has outside variance zero and makes
visibility automatic.  It also proves that even a proper-root variant is too
weak: one-spare padding transfers any positive-mass counterexample for
\(U_k(\theta)\) into \(P_{k+1}\) with outside variance
\[
\frac1{p_{k+1}}\left(1-\frac1{p_{k+1}}\right)\to0.
\]
Thus the next #536 frontier is not "prove the near-total-root case" as an
intermediate theorem.  The next useful loop must attack the full prime-biased
weighted union-free theorem, the full pair-link hypergraph, or a genuinely
non-vacuous root-essentiality/anti-padding condition.

20260519T161429Z update: moving/growing roots are now controlled whenever
outside reciprocal-prime variance diverges.  Proposition `mrw-a92d7b6e4031`
shows that if \(\mathcal F_k\subseteq2^{P_k}\) satisfies global comparable-pair
visibility through arbitrary root sets \(J_k\), then
\[
\nu_{P_k}(\mathcal F_k)
\le
C_0\left(1+\sum_{p_i\notin J_k}\frac1{p_i}\left(1-\frac1{p_i}\right)\right)^{-1/2}.
\]
Thus a positive-mass high-support obstruction of this visibility type must have
root sets carrying all but \(O(1)\) of the reciprocal-prime Bernoulli variance,
or it must evade global comparable-pair visibility altogether.  The next #536
frontier is the near-total-root-variance case, or an explicit positive-mass
union-free counterexample with near-total roots tested against pair-link
intervals and the lift to \(R_P(\theta)\).

20260519T153428Z update: fixed finite-junta comparable-pair visibility is now
proved harmless for positive prime-biased mass.  Proposition
`mrw-9e0b4f1a5c33` shows that if every proper comparable pair
`A subsetneq C` in a family has `(C\A) cap J` nonempty for one fixed finite
junta/root set `J`, then the family is a union of finitely many antichains and
has \(\nu_{P_k}\)-mass \(O_J(V_k^{-1/2})\to0\), conditional on the same
product-measure antichain estimate used in `mrw-54968b07a069`.  The live #536
frontier is therefore no longer fixed finite-junta trace-local mass; any
positive-mass high-support union-free obstruction must use moving/growing roots
with insufficient outside antichain variance, or comparable-pair deletions that
escape every fixed finite junta.

20260519T121424Z update: ordinary unrestricted \(ij\)-shifting is now proved
invalid for the prime-biased union-free route.  Counterexample
`mrw-8fcc1c2c5cda` shows that a measure-increasing shift can take a union-free
family out of the admissible class, so the next #536 route must use a
union-aware compression, max-fiber/container/junta decomposition, or explicit
broad-fiber counterexample, as formalized in open problem `mrw-3474bf5c904f`.

unresolved / local theory v005 remains latest / Erdos #25 finite-shadow, union-tail, essential-index, block-uniform first-hit, unshifted CRT prefix-dispersion, threshold-aware CRT, activation-scale \(Q_I\), and first-cycle entropy \(Q_I\) criteria proved / unshifted \(R_I\) route obstructed / CRT projection-amplification identity proved in `mrw-8d210c890d07` / Erdos #25 residue-tail route parked until a new projection-balance or projection-energy invariant appears / Erdos #536 imported in `mrw-277fbbb4ccb9` / valuation and cosunflower translations proved / naive positive-density finite-prime fiber lifting obstructed in `mrw-efc6dd81fc95` / rectangular packing `mrw-c44269169b5b` improves disjoint-packing constants / row-column fiber theorem `mrw-41a967169307` proves \(f(N)\le N-\lfloor N/6\rfloor\) / finite-prime weighted-grid reduction `mrw-f835f9671070` proves the \(g_P\) integral bridge / pair-slice obstruction `mrw-34f73025a206` proves direct \(P=\{2,3,5\}\) two-prime slicing cannot beat \(5/6\) / finite-prefix certificate `mrw-a261a0a4df25` proves \(\limsup f(N)/N\le149/180<5/6\) and corrects the raw \(743/300\) weighted-independent-set transfer / extended prefix-rank certificate `mrw-3367b245c458` proves \(\limsup f(N)/N\le197623/243000=0.8132633744\ldots\) / fixed-prime axis-floor obstruction `mrw-2060f97aad60` proves every fixed finite-prime route has positive floor \(\delta_P(1+\sum_{p\in P}1/(p-1))\), equal to \(11/15\) for \(P=\{2,3,5\}\) / low-support growing-prime criterion `mrw-4daa694d9526` proves that \(R_P(\theta)\to0\) along prime sets with \(S_P=\sum_{p\in P}1/p\to\infty\) implies \(f(N)=o(N)\) / squarefree binary-choice obstruction `mrw-9afb17b1b84a` proves high support alone does not force grid-bad triples and pointwise support-only envelopes fail, while block-transversal harmonic mass still decays / biased squarefree residual problem `mrw-37dbc6aeedf9` defines \(M_P(\theta)\) precisely / ambient cosunflower sparsity `mrw-053bc325c601` proves the full high-support layer has vanishing ambient random cosunflower density, so uniform ambient-density supersaturation is not the right invariant / pair-link shadow criterion `mrw-3c39ca3d1973` proves the exact self-link formulation / lower-shadow problem node `mrw-d0402aea6f58` names the sufficient union-cover route / deletion-trace proposition `mrw-cc4f876149b7` proves lower-shadow-freeness is equivalent to pairwise-intersecting deletion traces below every top set / rank-only families have vanishing biased high-support mass in `mrw-02dadc6b1bba` / fixed finite-core high-support cylinders force triples in `mrw-30aae977a4b6` / tilted-thinning criterion `mrw-2a2c5551301e` forces positive near-identity upward-boundary leakage under the standard biased intersecting trace hypothesis / union-tilted boundary proposition `mrw-67f99fecf9e2` proves positive external boundary and refutes global boundary-smallness via rank layers / product-measure antichain implication `mrw-54968b07a069` proves max-fiber antichain skeletons have vanishing high-support mass, conditional on the cited product-measure LYM/anti-concentration theorem / next executable frontier is the structural gap from killed max-fiber skeletons to arbitrary prime-biased high-support union-free families, or an explicit positive-mass counterexample outside all quarantined templates / no staging

## Latest Completed Cycle

- Full non-staging loop
  `20260520T102016Z-erdos-536-weighted-cross-core-aggregation-of-triangle-free-t`
  promoted proposition `mrw-a32a6d3a5f20`.  It proves a weighted cross-core
  Mantel double count for pair-link-free families:
  \[
  \sum_{A\in\mathcal F}\binom{|A|}{2}\nu(A)
  \le
  \frac14\sum_R\nu(R)W(R)^2.
  \]
  In the prime-biased case this is \((S_P^2+T_P)/4\), with
  \(T_P=\sum_{p\in P}1/(p^2(p-1))\).  This is nonterminal because the induced
  high-support mass bound is only constant-size and the result does not apply
  to arbitrary union-free families.  Scout completed but returned malformed
  source fragments and was ingested raw-only.  Focused Oracle completed with
  `--browser-inline-files`, confirmed the proof and edge cases, and identified
  cross-core Mantel-defect/stability as the next target.  No public staging,
  GitHub push, Gmail draft, or email occurred.
- Full non-staging loop
  `20260520T030334Z-erdos-536-pair-link-hypergraph-prove-two-extension-slice-tri`
  promoted proposition `mrw-354b105d4977`.  It proves that every common-core
  two-extension slice graph of a pair-link-free family is triangle-free and
  satisfies the sharp Mantel edge bound
  \(\lfloor |P\setminus R|^2/4\rfloor\).  This is a structural constraint on
  the actual pair-link hypergraph, not a mass theorem.  Complete bipartite
  slices are locally sharp, so the next target is weighted cross-core
  aggregation or a coherent dense-slice construction tested against all
  pair-link intervals.  Scout was ingested raw-only after returning unrelated
  zeta/Nantomah, \(s=9\), and polygamma material.  Focused Oracle first failed
  from a mistyped local file path, then the corrected `--browser-inline-files`
  retry completed and confirmed the proof/caveats.  No public staging, GitHub
  push, Gmail draft, or email occurred.
- Full non-staging loop
  `20260520T022056Z-erdos-536-sparse-pair-link-hypergraph-prove-one-swap-inserti`
  promoted proposition `mrw-25cdd8da0601`.  It proves that pair-link-free
  families have injective one-swap insertion fibers: for fixed
  \(A\in\mathcal F\) and \(y\notin A\), at most one deletion
  \(x\in A\) can keep \((A\setminus\{x\})\cup\{y\}\) inside \(\mathcal F\).
  The result gives a local Johnson one-swap degree bound
  \(|\Gamma_1^\mathcal F(A)|\le |P\setminus A|\), but no standalone
  prime-biased mass bound.  Scout completed with `--browser-inline-files` but
  returned a malformed source-fragment response; it was ingested raw-only at
  Oracle first failed with `Chrome window closed before oracle finished`; the
  compact inline retry completed and confirmed the proof while warning against
  unequal-rank, full same-rank-slice, dual fixed-deletion, \(I\)-instead-of-
  \(I^\circ\), and mass-decay overclaims.  No public staging, GitHub push,
  Gmail draft, or email occurred.
- Full non-staging loop
  `20260520T014549Z-erdos-536-rare-pair-link-geometry-prove-or-refute-a-rare-hig`
  promoted proposition `mrw-b1f87c9d6a42`.  It proves that exact rank layers
  and eventual full capped support bands have full genuine pair-link
  projection, even though the capped random-pair relation remains
  \(O(S_k^{-1})\) by prior nodes.  Scout completed with
  `--browser-inline-files` but returned routine \(s=9\) inverse-tail material;
  it was ingested raw-only at
  current strategy explicitly rejects routine \(s=9\) as terminal evidence.
  Focused Oracle completed with `--browser-inline-files` and confirmed the
  finite construction while rejecting degree, rectangle, counterexample, and
  \(U_k(\theta)\) overclaims.  No public staging, GitHub push, Gmail draft, or
  email occurred.
- Full non-staging loop
  `20260520T010053Z-erdos-536-rare-pair-link-endpoint-degree-invisibility-after`
  promoted corollary `mrw-6d4a8b0f2c91`.  It converts the capped random-pair
  sparsity of `mrw-4f1e9a2d6b73` into endpoint-degree and rectangle statements:
  capped union and full pair-link relations have no positive-mass endpoint
  core and no positive-mass product rectangle inside a fixed cap.  Scout
  completed but returned only the malformed one-word response `The`; it was
  Oracle completed with `--browser-inline-files` and confirmed the proof as a
  corollary after endpoint-inclusive wording was added.  No public staging,
  GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260520T001456Z-erdos536-sparse-overlap-graph`
  promoted corollary `mrw-4f1e9a2d6b73`.  It proves that inside a fixed capped
  band \(\theta S_k<|A|\le\alpha S_k<2\theta S_k\), positive-mass families
  have only \(O(S_k^{-1})\) conditioned random-pair union completions and only
  \(O(S_k^{-1})\) full pair-link interval hits back into the cap.  Scout
  completed and again returned routine \(s=9\) tail material, so it was ingested
  completed with `--browser-inline-files` and recommended promotion as a
  corollary with non-overclaim wording.  No public staging, GitHub push, Gmail
  draft, or email occurred.
- Full non-staging loop `20260519T233444Z-erdos536-mixed-overlap-graph`
  promoted proposition `mrw-c7f4e0c9a821`.  It proves the conditional
  overlap-energy bound by finite-product relative entropy decomposition and a
  self-contained Bernoulli divergence curvature inequality.  The result
  upgrades the previous high-intersection cluster-cover quarantine from
  \(o(\sqrt{S_k})\) clusters to \(o(S_k)\) clusters for every positive-mass
  family.  Scout completed but again followed the zeta-tail manuscript and
  returned routine \(s=9\) material, so it was ingested raw-only at
  `--browser-inline-files` and confirmed the proof with endpoint and
  non-overclaim wording incorporated.  No public staging, GitHub push, Gmail
  draft, or email occurred.
- Full non-staging loop `20260519T225444Z-erdos536-high-intersection-clustering`
  promoted proposition `mrw-18e9c7b0a5af`.  It proves the product-square moment
  bound for high-intersection cliques under \(\nu_P(p\in S)=1/p\), using
  \(\mathbb E|X\cap Y|=\sum_{p\in P}p^{-2}\).  The result kills positive-mass
  high-support families that are internally \(\gamma S_k\)-intersecting, and
  kills covers by \(o(\sqrt{S_k})\) such cliques.  Scout completed but again
  drifted to parked zeta/polygamma and \(s=9\) material, so it was ingested
  first hit `Chrome window closed before oracle finished`; the inline retry
  completed and confirmed the proof with wording caveats incorporated.  No
  public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T173438Z-erdos536-private-shadow-code-quarantine`
  promoted proposition `mrw-7c6a0e9f2d31`.  It proves a weighted private-shadow
  packing bound under \(\nu_P(p\in S)=1/p\), then applies it to show that
  sparse-intersection high-support code templates have vanishing mass.  Inside
  capped bands \(\theta S_k<|A|\le\alpha S_k\), \(\alpha<2\theta\), this kills
  the broad low-overlap union-free and squarefree pair-link-free obstruction
  template.  Scout completed but drifted to parked polygamma and \(s=9\)
  material, so it was ingested raw-only at
  `--browser-inline-files`; its advisory output is recorded in
  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T165434Z-erdos536-near-total-root-equivalence`
  promoted proposition `mrw-4b9f5c2e6a1d`.  It proves that near-total-root
  visibility is terminal-equivalent to the original weighted union-free problem:
  \(U_k^{\mathrm{vis},B}(\theta)=U_k(\theta)\) for \(B\ge0\), and one-spare
  padding defeats the proper-root variant while preserving positive limsup mass
  and every lower high-support threshold \(\theta'<\theta\).  Scout completed
  but returned parked polygamma and routine \(s=9\) material, so it was ingested
  completed through `--browser-inline-files` and confirmed the claim with
  endpoint caveats incorporated in the node.  No public staging, GitHub push,
  Gmail draft, or email occurred.
- Full non-staging loop `20260519T161429Z-erdos536-outside-variance-roots`
  promoted proposition `mrw-a92d7b6e4031`.  It removes the trace-count loss from
  the fixed-junta argument by conditioning on \(S\cap J_k\), proving that every
  outside fiber is an antichain and hence any visibility family has mass
  \(O((1+W_k(J_k))^{-1/2})\).  Scout completed and was ingested raw-only; the
  focused Oracle attachment run failed with
  `Attachments never reached a clickable send button before timeout`, then the
  inline-file fallback completed and confirmed the proof after a minor
  empty-outside wording correction.  No public staging, GitHub push, Gmail
  draft, or email occurred.
- Full non-staging loop `20260519T153428Z-erdos536-fixed-junta-root-consistency`
  promoted proposition `mrw-9e0b4f1a5c33`.  It proves, conditional on the
  product-measure antichain estimate already isolated in `mrw-54968b07a069`,
  that a family whose every proper comparable-pair deletion hits one fixed
  finite set \(J\) has vanishing prime-biased mass, because each fixed
  \(J\)-trace class is an antichain.  Scout completed but was ingested raw-only;
  the focused Oracle attachment run failed with
  `Attachments never reached a clickable send button before timeout`, and the
  compact inline fallback completed as advisory.  No public staging, GitHub
  push, Gmail draft, or email occurred.
- Bootstrap import from the preserved PDF extract completed earlier.
- THEORY_v002 was built and staged publicly; the public repository remains at staged `stage_v003`.
- Local `.math-wiki` theory is ahead at THEORY_v005 with APP-0007 and APP-0008; no new staging has occurred.
- Research-only cycle `20260518T091402Z-heartbeat-sprint-attack-qi-lim-nantomah-open-problem-2-for-h` refuted the all-\(n\) complete-monotonicity strengthening for higher \(P_n''\): \(P_n'''(2)>0\) for all \(n\ge29\), and \(P_7^{(6)}(3)<0\).
- Research-only cycle `20260518T101945Z-research-only-p1-trigamma-product-frontier` derived the \(P_1\) exact \(T_{p,i,j}\) recurrence and found no order-35 sampled sign obstruction.
- Research-only cycle `20260518T110932Z-research-only-p1-kernel-or-counterexample-sprint` extended the floating screen to order \(80\), rejected apparent high-order failures as uncertified, and kept \(P_1\) open.
- Research-only cycle `20260518T120047Z-p1-exact-interval-sprint` added `.math-wiki/calculations/certify_p1_interval.ps1`, but direct \(A_m\)-product interval enclosures still straddled zero and were quarantined as too ill-conditioned.
- Research-only cycle `20260518T125130Z-p1-pole-family-sprint` proved a route obstruction: in the canonical partial-fraction inverse-Laplace decomposition for \(P_1''\), independent integer-pole and reciprocal-pole family positivity fails near \(t=0\).  Note `mrw-5a84b7d9f2c1` records the proof.
- Research-only cycle `20260518T142240Z-build-a-cross-family-cancellation-or-renormalized-laplace-ke` promoted proposition `mrw-a4339be8da59`, the ratio-normal-form reduction for \(P_1\) convexity, and theorem `mrw-58db958e1bf1`, proving \(P_1''(x)>0\) for all \(x>0\).  No public staging, GitHub push, Gmail draft, or email occurred.
- Research-only outside-route cycle `20260518T153717Z-outside-route-restart-find-a-new-source-grounded-open-proble` followed the user's instruction to steer away from the \(P_1/P_n\) \(-P''\) monotonicity branch.  Scout/Oracle forage returned quarantined targets (\(s=9\) tail repetition and \(P_n\) variants), so the response was ingested raw-only and rejected for promotion.  A local Librarian/Student pass selected Bulboaca--Zayed's Gamma-product sharp-constant problem and promoted theorem `mrw-0fd149ddc79d`, proving the sharp threshold for \(u(s)/(\Gamma(s+\rho)\Gamma(s))\) when \(u'/u\) is nonincreasing.  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T165311Z-gamma-product-polynomial-threshold-reduction-for-u-m-s-s-m-1` promoted theorem `mrw-37311e7a5a0f`, proving the exact variational threshold formula for polynomial numerators \(u_m(s)=s^m+1\).  It also proves the left-endpoint formula fails for every \(m\ge4\), so the remaining problem is the uniqueness/localization/asymptotics of the maximizer.  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T173138Z-gamma-maximizer-full-attempt-with-erdos-fallback-selection` made a full attempt on the Gamma maximizer frontier.  It promoted theorem `mrw-73218406186e`, proving every \(m\ge4\) maximizer of \(R_m\) lies in \(1<s<(m-1)^{1/m}\), hence \(s=1+O(\log m/m)\).  This is durable progress but not a complete solution of the Gamma open problem, so the user-requested gate triggered the fallback into the Erdos problem list.  The selected next target is Erdos Problem #25, promoted as open problem node `mrw-3d524c92103b`.  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T181156Z-erdos-25-finite-avoidance-densities-and-tail-obstruction` promoted proposition `mrw-ba29cdf1fd30`, proving the finite avoidance densities \(\delta_N=|C_N|/L_N\), the zero-shadow case \(\delta_N\to0\), and a sufficient tail-defect criterion for the full logarithmic density.  It also promoted obstruction note `mrw-17f44100cb83`.  This does not solve full Erdos #25 in the positive-shadow case.  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T182422Z-erdos-25-positive-tail-control-sprint` promoted proposition `mrw-f92c897044c4`, proving a union-tail criterion for Erdos #25:
\[
U_N=
\limsup_{x\to\infty}
\frac1{\log x}
\sum_{\substack{i>N\\n_i<x}}
\frac{1+\log(x/n_i)}{n_i}
\to0
\]
implies that \(B\) has logarithmic density \(\delta=\lim_N\delta_N\).  In particular, the problem is locally solved under \(\sum_i1/n_i<\infty\).  The same proposition proves the criterion is not necessary using nested even-modulus exclusions, so the full positive-shadow case remains open and now requires overlap-sensitive tail control.  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T185221Z-erdos-25-essential-index-overlap-tail-criterion` promoted proposition `mrw-171478aeed08`, proving an essential-index tail criterion.  With \(\delta_0=1\), \(h_i=\delta_{i-1}-\delta_i\), and \(\mathcal I=\{i:h_i>0\}\), the condition
\[
U_N^{\mathrm{ess}}=
\limsup_{x\to\infty}
\frac1{\log x}
\sum_{\substack{i>N\\i\in\mathcal I\\n_i<x}}
\frac{1+\log(x/n_i)}{n_i}
\to0
\]
implies that \(B\) has logarithmic density \(\delta\).  This strictly weakens the raw union-tail test by discarding fully redundant zero-decrement exclusions; nested even-modulus exclusions satisfy the essential test while raw \(U_N\) diverges.  Full Erdos #25 remains open.  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T193105Z-erdos-25-partial-redundancy-positive-shadow-tail-criterion` promoted proposition `mrw-e0778085804e`, proving a block-uniform first-hit criterion: if finite first-hit blocks \(G_r\) satisfy \(\sup_{x\ge2}\mu_x(G_r)\le C\eta_r+\varepsilon_r\) with \(\sum_r\varepsilon_r<\infty\), then \(B\) has logarithmic density \(\delta\).  It also promoted obstruction note `mrw-536639208ce1`, proving by a logarithmic interval-spike model that fixed individual density data alone cannot control escaping tail mass.  This is not a counterexample to Erdos #25; it quarantines h-only decrement chasing and makes residue-overlap uniformity the next target.  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T201314Z-erdos-25-crt-prefix-dispersion-certificate-for-block-uniform` promoted proposition `mrw-2945dff32e3e`, proving a finite CRT prefix-dispersion certificate for first-hit block uniformity.  For a block \(G_I\), it proves \(\sup_x\mu_x(G_I)\le P_I+R_I+c_0\eta_I\), where \(P_I\) is threshold-prefix concentration and \(R_I\) is harmonic prefix concentration of the eventual CRT support.  This keeps the Erdos #25 route live but shifts the next obstruction to summability or failure of \(P_I+R_I\).  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T205009Z-erdos-25-small-residue-obstruction-to-crt-prefix-defects` promoted note `mrw-e0971c9b820a`, proving that the unshifted \(R_I\) defect is not automatically summable even for sparse singleton blocks with \(\sum_i1/n_i<\infty\), because small formal representatives can lie below the activation threshold.  It also promoted proposition `mrw-f1348014e087`, proving the threshold-aware replacement certificate \(\sup_x\mu_x(G_I)\le P_I+Q_I+c_0\eta_I\), where \(Q_I\) charges first active representatives.  Full Erdos #25 remains open.  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T213009Z-erdos-25-activation-scale-bound-for-threshold-aware-defects` promoted proposition `mrw-eaf102b5cac0`, proving \(Q_I\le L_B\eta_I/(n_B\log n_B)\) and the resulting activation-scale sufficient condition for logarithmic density.  This is not a complete solution of Erdos #25; the unresolved issue is whether the ratio \(\Lambda_I=L_B/(n_B\log n_B)\) can be improved by overlap or first-cycle entropy, or whether a true actual-mass obstruction exists.  No public staging, GitHub push, Gmail draft, or email occurred.
- Heartbeat research-only cycle `20260518T221010Z-erdos-25-first-cycle-entropy-bound-for-q-defects` promoted proposition `mrw-7586943cc138`, proving \(Q_I\le\Phi(n_B,L_B\eta_I)\), where \(\Phi\) is the packed harmonic profile of first active representatives.  This improves the linear activation-scale bound and proves support-size-only sharpness, but it still does not solve Erdos #25.  The next obstruction is residue-structured dispersion beyond \(\Phi\), a true actual-mass obstruction, or an Erdos-list restart outside residue-tail continuity.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260518T225329Z-erdos-25-residue-structured-dispersion-or-erdos-list-restart` completed the #25 route audit and restart gate.  It recovered and audited the Oracle response, proved lemma `mrw-8d210c890d07` (CRT projection amplification for finite residue shadows), rejected the live Scout response as raw-only because it returned to parked routine \(s=9\) inverse-tail work, and promoted Erdos #536 as source-grounded open problem node `mrw-277fbbb4ccb9`.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T001240Z-erdos-536-finite-prime-lcm-fiber-lifting` completed the #536 first attack.  Scout was run and ingested raw-only, then rejected for promotion because it returned to parked \(s=9\) inverse-tail material.  Erudition and Oracle were run; the seven-file Oracle upload failed at browser-send, the inline request fallback completed, and the response was audited as advisory only.  The cycle promoted valuation lemma `mrw-2e217726536f`, squarefree cosunflower lemma `mrw-e80e409bf536`, packing proposition `mrw-e844b4203305` proving \(f(N)\le 11N/12+O((\log N)^2)\), obstruction note `mrw-efc6dd81fc95`, and next-frontier problem `mrw-c5a954e7138b`.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T005126Z-erdos-536-p-2-3-weighted-finite-prime-exponent-grid-packing` improved the #536 packing route.  It proved proposition `mrw-c44269169b5b`: a finite rectangular \(2,3\)-grid packing certificate gives
\[
f(N)\le \frac{42287}{46656}N+O(1)=0.9063571673\ldots N+O(1).
\]
The same proposition also gives a structured dyadic multiscale packing bound
\[
f(N)\le\left(1-\frac{\sigma_{2,3}}3\right)N+O((\log N)^2),
\qquad
\sigma_{2,3}=0.2807753443\ldots,
\]
and proves the old unit-corner model is saturated at exponent weight \(1/4\), so the \(11/12\) bound cannot be improved by unit-corner parity changes alone.  The Scout response was ingested raw-only and then locally audited; its row-column fiber argument was promoted as theorem `mrw-41a967169307`, proving the stronger bound \(f(N)\le N-\lfloor N/6\rfloor\).  Unverified Scout literature comments and higher-prime extrapolations remain raw-only.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T013317Z-erdos-536-p-2-3-5-weighted-grid-obstruction-and-finite-prime` proved proposition `mrw-f835f9671070`, the finite-prime weighted-grid reduction
\[
f(N)\le
\sum_{\substack{r\le N\\(r,Q_P)=1}}g_P(N/r),
\qquad
\limsup_{N\to\infty}\frac{f(N)}N
\le
\delta_P\int_1^\infty g_P(t)t^{-2}\,dt.
\]
It also promoted obstruction note `mrw-34f73025a206`, proving that the direct \(P=\{2,3,5\}\) pair-slice transfer gives exactly the existing \(5/6\) constant and cannot improve it.  Oracle was run successfully through an inline fallback after attachment/browser issues; Scout's corrected live run stalled and was recorded as a blocker, with no Scout promotion.  A raw exact branch-and-bound audit on \([0,2]^3\) found the advisory bound \(743/300\), which with trivial tail would yield \(2783/3375<5/6\), but this remains raw-only pending a compact certificate.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T021730Z-erdos-536-finite-0-2-3-weighted-grid-rational-certificate-fo` promoted proposition `mrw-a261a0a4df25`.  It proves the corrected finite-prefix plus pair-tail bound
\[
\int_1^\infty g_{235}(t)t^{-2}\,dt\le\frac{149}{48},
\qquad
\limsup_{N\to\infty}\frac{f(N)}N\le\frac{149}{180}<\frac56.
\]
The cycle also certifies the old finite \([0,2]^3\) weighted independent-set upper bound \(743/300\), but records that this object is not the prefix-rank integral appearing in the finite-prime reduction.  The raw \(743/300+277/450\) transfer is therefore not promoted.  Scout completed and was ingested raw-only with no promotion because it returned to unrelated polygamma/tail candidates.  Oracle was run as an advisory audit of the corrected prefix certificate.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T025623Z-erdos-536-extend-three-prime-prefix-rank-savings-beyond-149` promoted proposition `mrw-3367b245c458`.  It proves the extended finite-prefix rank bound
\[
\int_1^\infty g_{235}(t)t^{-2}\,dt
\le
\frac{197623}{64800},
\qquad
\limsup_{N\to\infty}\frac{f(N)}N
\le
\frac{197623}{243000}
=0.8132633744\ldots.
\]
The proof uses exact finite prefix ranks through threshold \(162\), integrates the resulting deficits through \([162,180)\), and returns to the pair-slice envelope for \(t\ge180\).  Scout completed but returned to parked polygamma/tail candidates and was ingested raw-only.  The first Oracle upload attempt failed because attachments never reached a clickable send button; the inline retry completed and audited the prefix-rank certificate as promotable with the exact verifier retained as part of the proof object.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T033518Z-erdos-536-reusable-rank-cover-from-three-prime-prefix-rank-d` promoted proposition `mrw-2060f97aad60`.  It proves the fixed finite-prime axis-floor obstruction
\[
\delta_P\int_1^\infty g_P(t)t^{-2}\,dt
\ge
\delta_P\left(1+\sum_{p\in P}\frac1{p-1}\right).
\]
For \(P=\{2,3,5\}\), this floor is \(11/15\).  Therefore fixed \(P=\{2,3,5\}\) prefix-rank improvements can still sharpen constants between \(197623/243000\) and \(11/15\), but they cannot be a terminal route to \(f(N)=o(N)\).  Scout completed but returned an unusable shell response and was ingested raw-only.  Oracle completed through inline files and audited the axis-floor claim as promotable, while warning not to overclaim against growing-\(P\) finite-prime strategies.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T041518Z-erdos-536-growing-prime-finite-prime-criterion` promoted proposition `mrw-4daa694d9526`.  It defines
\[
R_P(\theta)=
\delta_P\int_1^\infty
\bigl(g_P(t)-L_{P,\theta}(t)\bigr)_+t^{-2}\,dt,
\]
where \(L_{P,\theta}(t)\) counts vectors in \(\Gamma_P(t)\) with support size at most \(\theta S_P\), \(S_P=\sum_{p\in P}1/p\), and \(0\le\theta<1\).  It proves that if \(S_{P_j}\to\infty\) and \(R_{P_j}(\theta)\to0\), then \(f(N)=o(N)\).  The proof uses the harmonic exponent measure \(\mu_P(\alpha)=\delta_P\prod p^{-\alpha_p}\), under which support size is a Bernoulli sum with mean \(S_P\), plus a Chernoff lower-tail bound.  Oracle audited the criterion as promotable and warned that \(R_P(\theta)\) is a prefix-rank residual, not the mass of one global independent set.  Scout completed and was ingested raw-only; no Scout claim was promoted.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T045417Z-erdos-536-squarefree-high-support-residual-test` promoted note `mrw-9afb17b1b84a`.  It proves that for the first \(2m\) primes grouped into pairs, the squarefree family choosing exactly one prime from each pair has \(2^m\) members, every member has support \(m\), and no three members form a grid-bad triple.  This gives exponentially large high-support pointwise spikes above \(L_{P,\theta}\), but the family's harmonic mass is at most \(1/m!\).  The same note proves every block-transversal spike of support \(r\) has harmonic mass at most \(e^{-r}\).  Thus support-only pointwise envelopes are quarantined, while \(R_P(\theta)\to0\) remains neither proved nor refuted.  Scout completed and was ingested raw-only with no promotion; the first focused Oracle live run failed because the Chrome window closed, then the retry completed and was audited as advisory.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T053417Z-erdos-536-biased-squarefree-residual` promoted open problem node `mrw-37dbc6aeedf9` and proved proposition `mrw-053bc325c601`.  The problem node defines the biased squarefree residual \(M_P(\theta)\) precisely and records the pair-link formulation \(I(A,B)=\{C:A\triangle B\subseteq C\subseteq A\cup B\}\).  The proposition proves
\[
\Xi_P=\prod_{p\in P}\left(1-\frac3p\left(1-\frac1p\right)^2\right),
\qquad
\log \Xi_P=-3S_P+O(1),
\]
so ambient cosunflower triples are exponentially sparse under \(\nu_P^3\), even though the high-support event \(|S|>\theta S_P\) has \(\nu_P\)-mass tending to \(1\).  This is not a counterexample to \(M_P(\theta)\to0\); it quarantines only uniform ambient-density supersaturation and makes pair-link/family-specific sparse supersaturation the next target.  Scout completed after one attachment failure and one inline retry, was ingested raw-only, and was rejected for promotion because it returned to parked \(s=9\), polygamma, and Gamma-style branches.  Oracle audited the formulas and caveats as advisory.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T061418Z-erdos-536-pair-link-supersaturation` promoted proposition `mrw-3c39ca3d1973`.  It proves the exact pair-link shadow criterion: with
\[
I(A,B)=\{C:A\triangle B\subseteq C\subseteq A\cup B\},
\qquad
\mathcal L_P(\mathcal F)=\bigcup_{A\ne B\in\mathcal F}I^\circ(A,B),
\]
a family \(\mathcal F\subseteq2^P\) is squarefree-cosunflower-free iff \(\mathcal F\cap\mathcal L_P(\mathcal F)=\emptyset\).  It also proves
\[
\nu_P(I(A,B))=
\prod_{p\in A\triangle B}\frac1p
\prod_{p\notin A\cup B}\left(1-\frac1p\right),
\]
and the local lower-trace obstruction: if \(C\in\mathcal F\), no two distinct lower members \(A,B\in\mathcal F\cap2^C\) can satisfy \(A\cup B=C\).  In particular, at most one one-deletion \(C\setminus\{p\}\) may lie in \(\mathcal F\).  Scout failed before browser attachment submission and was ingested raw-only with no promotion.  Oracle audited the proposition and required only wording corrections distinguishing coordinate cosunflowers from distinct triples and replacing "positive mass" by mass at least \(\eta\).  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T065418Z-erdos-536-biased-lower-shadow-union-cover` promoted open problem node `mrw-d0402aea6f58` and proved proposition `mrw-cc4f876149b7`.  The problem node states the biased lower-shadow union-cover theorem: for fixed \(0\le\theta<1\) and \(\eta>0\), every \(\mathcal F\subseteq H_{P_k,\theta}\) with \(\nu_{P_k}(\mathcal F)\ge\eta\) should contain \(A,B,C\in\mathcal F\) with \(A,B\subsetneq C\), \(A\ne B\), and \(A\cup B=C\), for all large \(k\).  The proposition proves the local trace equivalence: a family \(\mathcal F\subseteq2^P\) is lower-shadow union-cover-free iff, for every \(C\in\mathcal F\), the deletion trace
\[
\mathcal D_{\mathcal F}(C)=\{D\subseteq C:\ D\ne\varnothing,\ C\setminus D\in\mathcal F\}
\]
is pairwise intersecting.  This strengthens the previous one-deletion obstruction to all deletion sizes.  Scout stalled in the browser after a valid inline dry run and was ingested raw-only with no promotion.  Oracle audited the trace equivalence as safe to promote, found no obvious positive-mass counterexample, and recommended weighted lower-shadow double-counting plus a biased intersecting-trace bound as the next mechanism.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T073419Z-erdos-536-biased-weighted-deletion-trace` promoted proved propositions `mrw-02dadc6b1bba` and `mrw-30aae977a4b6`.  Proposition `mrw-02dadc6b1bba` proves that rank-only lower-shadow-free families have vanishing biased high-support mass along any finite prime sets with \(S_P=\sum_{p\in P}1/p\to\infty\).  The proof gives an exact rank criterion: ranks \(a,b,c\in T\) with \(a,b<c\) and \(a+b\ge c\) force a lower-shadow triple, so positive allowed ranks must more than double; Fourier anti-concentration for the Bernoulli support size then makes the biased mass of such lacunary rank sets tend to \(0\).  Proposition `mrw-30aae977a4b6` proves that fixed finite-core high-support cylinders cannot be counterexamples: once enough tail primes are present, two unused tail coordinates produce \(A=U\cup T\cup\{x\}\), \(B=U\cup T\cup\{y\}\), and \(C=U\cup T\cup\{x,y\}\).  Scout and the focused Oracle audit both had valid dry runs but the browser live path stalled with no thinking status; both are recorded as raw-only blockers, not mathematical evidence.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T081420Z-erdos-536-tail-sensitive-biased-trace` promoted proved propositions `mrw-c228258e6ab4` and `mrw-bf64e9def00c`.  Proposition `mrw-c228258e6ab4` proves the fair-thinning bound: if \(\mathcal F\) is lower-shadow union-cover-free and \(C\in\mathcal F\), then for uniformly random \(A\subseteq C\),
\[
\Pr(A\in\mathcal F\mid C)\le \frac12+2^{-|C|}.
\]
Under the coupled law where \(C\) has inclusion probabilities \(\min(2/p,1)\) and is then thinned by \(1/2\), this gives
\[
\Pr(A\in\mathcal F,\ C\in\mathcal F)
\le
\frac12\widetilde\nu_P(\mathcal F)
+
\mathbb E_{\widetilde\nu_P}[1_{\mathcal F}(C)2^{-|C|}].
\]
Proposition `mrw-bf64e9def00c` proves that upward-closed positive-mass high-support families force lower-shadow triples for \(P_k=\{p_1,\ldots,p_k\}\) and fixed \(0\le\theta<1\).  Thus a genuine counterexample must now be non-rank-only, non-finite-core, nonmonotone, and tail-sensitive.  Scout completed but returned to parked QLN/zeta-tail problems and was ingested raw-only with no promotion.  Focused Oracle had a valid dry run but the live ChatGPT project response was the rate-limit blocker "You've hit your limit. Please try again later."  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T085420Z-erdos-536-fair-thinning-boundary-gap` promoted proved proposition `mrw-4a98da3d7f40`.  It proves the exact fair-thinning upward-boundary identity
\[
\nu_P(\mathcal F)
=
\Pr(A\in\mathcal F,\ C\in\mathcal F)
+
\Pr(A\in\mathcal F,\ C\in(\uparrow\mathcal F)\setminus\mathcal F),
\]
where \(C\sim\widetilde\nu_P\), \(A\) is obtained by fair thinning, and \(A\sim\nu_P\).  Combined with `mrw-c228258e6ab4`, every lower-shadow-free \(\mathcal F\) satisfies
\[
\Pr(A\in\mathcal F,\ C\in(\uparrow\mathcal F)\setminus\mathcal F)
\ge
\nu_P(\mathcal F)
-
\frac12\widetilde\nu_P(\mathcal F)
-
\mathbb E_{\widetilde\nu_P}[1_{\mathcal F}(C)2^{-|C|}].
\]
Thus the fair-thinning self-overlap gap is now an upward-boundary leakage problem: a counterexample must be nonmonotone and boundary-heavy under the \((\nu_P,\widetilde\nu_P)\) coupling.  Scout and focused Oracle were run with literal prompts and treated as raw-only/blocker material; no external claim was promoted.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T093421Z-erdos-536-boundary-leakage-junta-test` promoted conditional proposition `mrw-2a2c5551301e` and proved proposition `mrw-67f99fecf9e2`.  The tilted-thinning proposition defines \(\nu_{P,\tau}(p\in C)=1/(\tau p)\), thins \(C\) to \(A\sim\nu_P\), and, assuming the standard \(r\)-biased intersecting trace bound, proves
\[
\Pr(A\in\mathcal F,\ C\in(\uparrow\mathcal F)\setminus\mathcal F)
\ge
\nu_P(\mathcal F)
-
\left(1-\tau+\tau^{\theta S_P}\right)\nu_{P,\tau}(\mathcal F)
\]
for lower-shadow-free \(\mathcal F\subseteq H_{P,\theta}\), \(0<\theta<1\).  Thus positive \(\nu_P\)-mass forces positive near-identity upward-boundary leakage along \(S_P\to\infty\).  The union-tilted proposition proves
\[
\nu_P(\mathcal G)^2
\le
2e^{-S_P/2}
+
\mu_P^\vee(\partial^\vee\mathcal G),
\qquad
\mu_P^\vee(p\in C)=\frac2p-\frac1{p^2},
\]
for lower-shadow-free \(\mathcal G\), and proves exact-rank layers can have \(\mu_P^\vee(\partial^\vee\mathcal G)\to1\).  Therefore global boundary-smallness is false; the next target is boundary absorption or structural decomposition, not another raw boundary lower bound.  Scout returned to parked polygamma/zeta-tail candidates and was ingested raw-only.  Oracle was run and audited as advisory only.  No public staging, GitHub push, Gmail draft, or email occurred.
- Full non-staging loop `20260519T101422Z-erdos-536-boundary-absorption-structure` promoted proved proposition `mrw-b4075311abd3` and open problem `mrw-55a8d9eddd2e`.  Proposition `mrw-b4075311abd3` fixes the semantics: lower-shadow union-cover-freeness is exactly the standard union-free set-family condition, i.e. no three distinct \(A,B,C\in\mathcal F\) satisfy \(A\cup B=C\).  The next target is therefore the prime-biased weighted union-free theorem
\[
U_k(\theta)=
\sup\{\nu_{P_k}(\mathcal F):\mathcal F\subseteq H_{k,\theta},\ \mathcal F\text{ union-free}\}\to0
\]
for every fixed \(0\le\theta<1\), where \(\nu_{P_k}(p_i\in S)=1/p_i\) and \(H_{k,\theta}=\{S:|S|>\theta\sum_{i\le k}1/p_i\}\).  The cycle inspected union-free and partition-free source families, recorded them as context only, and did not promote any external weighted theorem.  The full-attachment Oracle upload failed before send; inline-file Oracle/Scout outputs are advisory only.  No public staging, GitHub push, Gmail draft, or email occurred.
- The same loop promoted proved example `mrw-2ff2fe94bc57`: if each maximum-coordinate fiber is an antichain, then the resulting max-fiber skeleton is union-free.  This is not a counterexample to `mrw-55a8d9eddd2e`; it is the first concrete non-rank-only skeleton that the next weighted-mass proof must control.
- Full non-staging loop `20260519T105423Z-erdos536-max-fiber-antichain-mass` promoted proved conditional proposition `mrw-54968b07a069`.  Using the cited product-measure LYM plus support-size anti-concentration theorem of Yehuda--Yehudayoff as source context, it proves that every max-fiber antichain skeleton
\[
\mathcal F_k=\{X\cup\{m\}:X\in\mathcal A_m,\ \mathcal A_m\subseteq2^{[m-1]}\text{ antichain}\}
\]
has \(\nu_{P_k}\)-mass \(o(1)\) on \(H_{k,\theta}\) for every fixed \(0\le\theta<1\).  Thus `mrw-2ff2fe94bc57` cannot provide a positive-mass obstruction to `mrw-55a8d9eddd2e`.  Scout and Oracle dry-runs succeeded, but live browser runs failed with localhost `ECONNREFUSED`; both responses remain blocker/raw-only.  No public staging, GitHub push, Gmail draft, or email occurred.

## Current Central Target

Erdos-list fallback branch, now focused on Erdos Problem #536.  For #25, the finite-shadow, zero-shadow, union-tail/summable-reciprocal, essential-index, block-uniform first-hit, unshifted CRT prefix-dispersion, threshold-aware CRT, activation-scale \(Q_I\), first-cycle entropy \(Q_I\), and CRT projection-amplification diagnostic stages are done.  The remaining positive-shadow tail-continuity problem is parked because the current certificates do not control projection concentration of surviving shadows modulo future gcds.  For #536, the prime-valuation and squarefree cosunflower translations are proved, naive positive-density finite-prime fiber lifting is false, disjoint-packing constants have been improved, the two-prime row-column theorem gives \(5/6\), and the finite-prime \(g_P\) integral bridge is proved.  Fixed finite-prime optimization is nonterminal by the axis-floor obstruction, while the low-support growing-prime criterion makes \(R_P(\theta)\) the terminal finite-prime residual.  The support-level squarefree route has now been normalized: by `mrw-b4075311abd3`, the lower-shadow union-cover theorem is exactly the prime-biased high-support union-free problem.  Thus the current named target is open problem `mrw-55a8d9eddd2e`, asking whether \(U_k(\theta)\to0\) for every fixed \(0\le\theta<1\).  Rank-only, fixed finite-core, upward-closed, exact-rank boundary-smallness, and max-fiber antichain skeleton templates are now identified by `mrw-02dadc6b1bba`, `mrw-30aae977a4b6`, `mrw-bf64e9def00c`, `mrw-67f99fecf9e2`, and `mrw-2ff2fe94bc57`.  The next target is a weighted Kleitman/compression/container/junta theorem for this prime product measure, or an explicit positive-mass high-support union-free counterexample outside those templates.

## Active Strategy Thesis

Continue research without staging.  The #25 harmonic finite-shadow branch remains parked after `mrw-8d210c890d07`: the next #25 theorem would need a new projection-balance or projection-energy invariant, not another support-size, activation-scale, first-cycle entropy, or ambient-mass estimate.  The live branch is Erdos Problem #536 through finite prime-coordinate shadows for lcm triples.  The finite-prime integral bridge and low-support growing-prime criterion reduce the terminal route to \(R_P(\theta)\), while the squarefree support subroute is now the prime-biased weighted union-free theorem `mrw-55a8d9eddd2e`.  Proving \(U_k(\theta)\to0\) gives the lower-shadow theorem and \(M_{P_k}(\theta)\to0\); only after that should a loop try to lift from squarefree supports to the exponent-grid prefix-rank residual.  The next serious route should use weighted Kleitman, compression under unequal prime weights, product-measure containers, junta/decomposition, or boundary absorption as lemmas toward the weighted union-free theorem.  Do not cite uniform Boolean-lattice cardinality bounds as sufficient; they are source context only because \(\nu_{P_k}\) is an inhomogeneous product measure.  Do not try to prove global boundary-smallness; `mrw-67f99fecf9e2` refutes it.  Further fixed \(P=\{2,3,5\}\) computation is secondary unless it exposes a scalable mechanism for \(R_P(\theta)\).  The \(P_1/P_n\), \(-P''\), routine \(s=9\), Gamma-threshold, and Erdos #25 residue-tail branches remain parked unless the user explicitly asks to return or a new projection invariant appears.

## Bridge To Goal

THEORY_v005 modular-residue and zeta-law layer -> harmonic/logarithmic density model -> Erdos #25 finite-shadow route -> CRT projection-amplification obstruction to ambient-mass dispersion -> Erdos-list restart -> Erdos #536 equal pairwise lcm problem -> prime-valuation/cosunflower translation -> \(2,3\)-grid disjoint lcm-triangle packing -> two-prime row-column fiber theorem -> finite-prime \(g_P\) integral bridge -> three-prime finite-prefix certificate \(149/180\) -> extended prefix-rank certificate \(197623/243000\) -> fixed finite-prime axis floor \(11/15\) for \(P=\{2,3,5\}\) -> low-support growing-prime criterion \(R_P(\theta)\to0\Rightarrow f(N)=o(N)\) -> squarefree pointwise support-only obstruction -> biased squarefree residual target -> pair-link self-shadow criterion -> lower-shadow union-cover problem -> union-free reformulation -> prime-biased weighted union-free theorem \(U_k(\theta)\to0\) -> squarefree residual \(M_{P_k}(\theta)\to0\) if proved -> exponent-grid prefix-rank lift, still without public staging.

## Progress Invariant

- \(s=7\) inverse-tail theorem is solved locally in `mrw-28bcccec471e`.
- \(s=8\) inverse-tail theorem is solved locally in `mrw-544506a822b8`.
- Reciprocal-Gamma complete monotonicity is solved locally in `mrw-48a67678d0c1`.
- Reciprocal-digamma product curvature is solved locally in `mrw-0db1ed17aa9a`.
- Higher-order polygamma product complete monotonicity is refuted locally in `mrw-dee642b8e9cb`.
- The \(P_1''\) frontier has an exact recurrence, order-35 no-failure floating screen, order-80 uncertified apparent failures, an inconclusive dyadic interval helper, a proved pole-family obstruction in `mrw-5a84b7d9f2c1`, a ratio reduction in `mrw-a4339be8da59`, and a proved convexity theorem in `mrw-58db958e1bf1`.
- The weaker all-\(n\) higher-polygamma convexity question remains open in `mrw-f0a031feea8e`.
- The outside-route Gamma-product threshold problem is represented by `mrw-1396775c6089` and solved in the monotone-logarithmic-derivative case by theorem `mrw-0fd149ddc79d`.
- The polynomial numerator threshold problem for \(u_m=s^m+1\) is reduced by theorem `mrw-37311e7a5a0f` to the exact maximization of \(R_m\); for \(m\ge4\), the endpoint \(s=1\) is provably not the maximizer.
- Gamma maximizer support is localized by theorem `mrw-73218406186e`: every \(m\ge4\) maximizer lies in \(1<s<(m-1)^{1/m}\), hence \(s=1+O(\log m/m)\).  This is partial progress, not a complete Gamma solution.
- Erdos Problem #25 has been imported as open problem node `mrw-3d524c92103b`, with source note `references/sources/20260518T173138Z-erdos-residue-log-density.md`.
- Finite-shadow reduction `mrw-ba29cdf1fd30` proves every finite approximant \(B_N\) has logarithmic density \(\delta_N=|C_N|/L_N\), proves the \(\delta_N\to0\) case, and reduces the positive-shadow case to \(\Theta_N\to0\).
- Obstruction note `mrw-17f44100cb83` records that finite \(B_N\) computations are not enough; the hard point is continuity from above for the active tail \(B_N\setminus B\).
- Union-tail criterion `mrw-f92c897044c4` proves that \(U_N\to0\) implies logarithmic density \(\delta\), and therefore solves the summable-reciprocal subcase \(\sum_i1/n_i<\infty\).  Its nested even-modulus example proves this criterion is sufficient but not necessary.
- Essential-index criterion `mrw-171478aeed08` proves that zero-decrement exclusions \(h_i=\delta_{i-1}-\delta_i=0\) remove no residual first-hit points and may be discarded before applying a tail majorant.  This strictly weakens the raw union-tail condition but is still partial because positive-decrement indices can remain highly redundant.
- Block-uniform criterion `mrw-e0778085804e` proves that finite first-hit blocks controlled uniformly by their finite-shadow decrement plus summable error imply the full logarithmic-density conclusion.
- Obstruction note `mrw-536639208ce1` proves that fixed individual logarithmic density data alone cannot imply continuity from above; h-only decrement chasing is quarantined unless paired with uniformity or residue-overlap structure.
- CRT prefix-dispersion certificate `mrw-2945dff32e3e` proves the finite block estimate \(\sup_x\mu_x(G_I)\le P_I+R_I+c_0\eta_I\), but the unshifted \(R_I\) summability target is now obstructed.
- Small-residue obstruction `mrw-e0971c9b820a` proves the unshifted \(R_I\) defect can be non-summable for singleton blocks even when \(\sum_i1/n_i<\infty\); this quarantines \(P_I+R_I\) as an automatic target.
- Threshold-aware CRT certificate `mrw-f1348014e087` proves the repaired finite estimate \(\sup_x\mu_x(G_I)\le P_I+Q_I+c_0\eta_I\), where \(Q_I\) charges first active representatives.
- Activation-scale bound `mrw-eaf102b5cac0` proves \(Q_I\le L_B\eta_I/(n_B\log n_B)\) and the corresponding activation-scale sufficient condition for logarithmic density.
- First-cycle entropy bound `mrw-7586943cc138` proves \(Q_I\le\Phi(n_B,L_B\eta_I)\), recovers the activation-scale bound, and shows support-size-only sharpness.
- Scout/Oracle response `theory/forage/responses/20260518T153717Z-outside-route-open-problem-scout-no-staging-response.md` is raw-only and was not promoted because it violated the user's route constraints.
- THEORY_v005 remains the latest local theory; no public staging or email has occurred.

## Staleness Signals

- Public `wiki/latest` and repo-root `theory/latest` remain at staged v003, while `.math-wiki` is ahead at local v005 plus the new unstaged \(P_1\) convexity theorem.
- Repeating \(P_1\) floating-point sign checks is stale.
- Repeating direct \(A_m\)-product dyadic intervals is stale unless a new cancellation split is added.
- Repeating independent pole-family positivity is proved impossible.
- Re-proving \(P_1\) convexity is now stale; the open target is complete monotonicity or a higher-derivative counterexample.
- Avoid inverse-tail consecutive cases unless a general theorem emerges.
- The \(P_1/P_n\) complete-monotonicity branch is user-parked for now.
- Oracle's \(s=9\) inverse-tail suggestion is quarantined as a routine consecutive-tail repetition.
- Fixed \(P=\{2,3,5\}\) finite-prefix table extension is now nonterminal unless it produces a reusable integer rank-cover pattern or feeds a growing-\(P\) theorem.
- The growing-\(P\) route now has a named invariant \(R_P(\theta)\); a cycle that only rephrases the low-support criterion without attacking or obstructing this residual is stale.
- Pointwise or cardinality-only high-support arguments for \(R_P(\theta)\) are now stale: `mrw-9afb17b1b84a` gives exponentially large squarefree high-support grid-bad-free spikes while also proving the obvious block-transversal spikes have vanishing harmonic mass.

## Strongest Durable Results So Far

- Pudim wiki initialized and graph refreshed.
- Original PDF preserved under `.math-wiki/bootstrap/main.pdf`.
- Three original zeta-inequality applications remain proved.
- Exact inverse-tail floor formulas at \(s=7\) and \(s=8\) are proved.
- Reciprocal-Gamma curvature complete monotonicity is proved.
- Reciprocal-digamma product curvature complete monotonicity is proved.
- Higher-order polygamma product complete monotonicity is refuted.
- \(P_1\) convexity is proved: \(P_1''(x)>0\) for \(x>0\).
- Sharp Gamma-product monotonicity threshold theorem is proved for all positive differentiable \(u\) with nonincreasing \(J=u'/u\): \(u(s)/(\Gamma(s+\rho)\Gamma(s))\) is strictly decreasing on \([1,\infty)\) iff \(\psi(1+\rho)\ge\gamma+J(1)\).
- Variational polynomial Gamma threshold theorem is proved for \(u_m=s^m+1\): \(\rho_m=\max_{s\ge1}R_m(s)\), and \(R_m'(1)>0\) for \(m\ge4\).
- Polynomial Gamma maximizers are localized: theorem `mrw-73218406186e` proves every \(m\ge4\) maximizer lies in \(1<s<(m-1)^{1/m}\).
- Erdos Problem #25 is selected as the next fallback frontier in `mrw-3d524c92103b`.
- Finite-shadow Erdos #25 reduction is proved in `mrw-ba29cdf1fd30`.
- Tail-continuity obstruction is recorded in `mrw-17f44100cb83`.
- Union-tail positive subcase and summable-reciprocal corollary are proved in `mrw-f92c897044c4`.
- Essential-index positive subcase is proved in `mrw-171478aeed08`.
- Block-uniform first-hit positive subcase is proved in `mrw-e0778085804e`.
- h-only decrement control is quarantined by obstruction note `mrw-536639208ce1`.
- CRT prefix-dispersion certificate is proved in `mrw-2945dff32e3e`, with unshifted summability obstruction in `mrw-e0971c9b820a` and threshold-aware replacement in `mrw-f1348014e087`.
- Activation-scale \(Q_I\) bound is proved in `mrw-eaf102b5cac0`; it isolates the remaining ratio \(\Lambda_I=L_B/(n_B\log n_B)\).
- First-cycle entropy \(Q_I\) bound is proved in `mrw-7586943cc138`; it replaces \(\Lambda_I\) by \(\Phi(n_B,L_B\eta_I)\) and proves support-size-only sharpness.
- CRT projection-amplification lemma `mrw-8d210c890d07` proves that future congruence mass inside a finite shadow is the ambient factor \(g/n\) times projected shadow concentration modulo \(g=(M,n)\).
- Erdos #536 open problem node `mrw-277fbbb4ccb9` is now the selected restart frontier.
- Prime-valuation criterion `mrw-2e217726536f` and squarefree cosunflower criterion `mrw-e80e409bf536` translate equal pairwise lcm triples into coordinatewise maximum constraints.
- Disjoint lcm-triangle packing proposition `mrw-e844b4203305` proves \(f(N)\le 11N/12+O((\log N)^2)\) for Erdos #536.
- Fiber obstruction note `mrw-efc6dd81fc95` proves positive density alone does not force a rich common outside-kernel finite-prime fiber.
- Weighted finite-prime fiber problem `mrw-c5a954e7138b` is the active #536 continuation frontier.
- Rectangular packing proposition `mrw-c44269169b5b` improves the #536 local upper bound to \(f(N)\le42287N/46656+O(1)\), records the dyadic multiscale bound, and closes the unit-corner packing subroute at exponent weight \(1/4\).
- Two-prime row-column theorem `mrw-41a967169307` proves \(f(N)\le N-\lfloor N/6\rfloor\), the strongest local #536 bound so far.
- Finite-prime weighted-grid reduction `mrw-f835f9671070` proves the exact \(g_P\) integral bridge for #536.
- Pair-slice obstruction `mrw-34f73025a206` proves direct \(P=\{2,3,5\}\) two-prime slicing gives exactly \(5/6\), not an improvement.
- Finite-prefix certificate `mrw-a261a0a4df25` proves
\[
\int_1^\infty g_{235}(t)t^{-2}\,dt\le\frac{149}{48},
\qquad
\limsup_{N\to\infty}\frac{f(N)}N\le\frac{149}{180}<\frac56.
\]
It also certifies the old raw weighted independent-set upper bound \(743/300\) on \([0,2]^3\), while proving that the raw \(743/300+277/450\) transfer used the wrong finite object.
- Extended prefix-rank certificate `mrw-3367b245c458` proves
\[
\int_1^\infty g_{235}(t)t^{-2}\,dt\le\frac{197623}{64800},
\qquad
\limsup_{N\to\infty}\frac{f(N)}N\le\frac{197623}{243000}.
\]
It uses exact finite prefix ranks through threshold \(162\), saves \(4877/64800\) from the pair-slice integral, and keeps all extrapolation toward \(f(N)=o(N)\) raw-only.
- Fixed finite-prime axis-floor obstruction `mrw-2060f97aad60` proves
\[
\delta_P\int_1^\infty g_P(t)t^{-2}\,dt
\ge
\delta_P\left(1+\sum_{p\in P}\frac1{p-1}\right),
\]
so fixed \(P=\{2,3,5\}\) has an unavoidable floor \(11/15\).  This makes fixed-\(P\) constant optimization a nonterminal subroute.
- Low-support growing-prime criterion `mrw-4daa694d9526` proves that for \(0\le\theta<1\), if
\[
R_P(\theta)=
\delta_P\int_1^\infty
\bigl(g_P(t)-L_{P,\theta}(t)\bigr)_+t^{-2}\,dt
\]
tends to \(0\) along finite prime sets with \(S_P=\sum_{p\in P}1/p\to\infty\), then \(f(N)=o(N)\).  Under the harmonic exponent measure, support size is a Bernoulli sum with mean \(S_P\), so the low-support contribution itself decays by Chernoff.
- Squarefree binary-choice obstruction note `mrw-9afb17b1b84a` proves that high support alone does not force grid-bad triples.  For the first \(2m\) primes grouped in pairs, the one-from-each-pair family has \(2^m\) high-support squarefree vectors and no grid-bad triple, while its harmonic mass is at most \(1/m!\).  More generally, every block-transversal spike of support \(r\) has harmonic mass at most \(e^{-r}\).
- Upward-boundary identity `mrw-4a98da3d7f40` proves that under fair thinning,
\[
\nu_P(\mathcal F)
=
\Pr(A\in\mathcal F,\ C\in\mathcal F)
+
\Pr(A\in\mathcal F,\ C\in(\uparrow\mathcal F)\setminus\mathcal F),
\]
so the surviving fair-thinning obstruction is boundary leakage, not merely low self-overlap.
- Partial frontier note `mrw-1c9d9f07a4ef` records the \(P_1\) exact recurrence, floating-order warnings, failed direct interval route, pole-family obstruction, ratio reduction, and convexity theorem.

## Exact Unresolved Obstruction

The Erdos #25 finite-shadow stage is solved, including the \(\delta_N\to0\) case, the union-tail/summable-reciprocal positive subcase, the essential-index positive subcase, an abstract block-uniform first-hit criterion, a finite unshifted CRT prefix-dispersion certificate, the small-residue obstruction to unshifted \(R_I\)-summability, a threshold-aware CRT certificate, an activation-scale \(Q_I\) bound, a first-cycle entropy \(Q_I\) bound, and the CRT projection-amplification diagnostic.  The exact unresolved #25 obstruction remains the positive-shadow tail-continuity condition
\[
\Theta_N=\limsup_{x\to\infty}\mu_x(B_N\setminus B)\to0.
\]
However, `mrw-8d210c890d07` shows that future-hit estimates require control of projected survivor concentration modulo \(g=(M,n)\).  The existing certificates do not control this projection concentration, and the support-size-only profile \(Q_I\le\Phi(n_B,L_B\eta_I)\) is sharp without residue information.  Therefore #25 is parked until a new projection-balance or projection-energy invariant appears.  The current unresolved #536 obstruction is no longer the naive finite-prime lifting lemma, the fixed-prime \(P=\{2,3,5\}\) route, or pointwise high-support counting.  The low-support growing-prime criterion `mrw-4daa694d9526` reduces the terminal finite-prime route to the high-support prefix-rank residual \(R_P(\theta)\).  The squarefree support route is now named precisely: by `mrw-b4075311abd3`, the lower-shadow route is the prime-biased union-free problem, and `mrw-55a8d9eddd2e` asks whether \(U_k(\theta)\to0\).  Rank-only, fixed finite-core, upward-closed, exact-rank boundary-smallness, and max-fiber antichain skeleton templates are quarantined; `mrw-54968b07a069` kills the max-fiber template under cited product-measure LYM/anti-concentration.  The live obstruction is a weighted Kleitman/compression/container/junta decomposition theorem for \(\nu_{P_k}\), or an explicit positive-mass high-support union-free counterexample outside those quarantined templates.  A successful squarefree theorem still needs a separate lift to exponent-grid prefix ranks.

## Next Executable Cycle Target

Run one full non-staging Pudim loop.  Primary target: bridge from the killed max-fiber antichain skeletons in `mrw-54968b07a069` to the full prime-biased weighted union-free theorem `mrw-55a8d9eddd2e`, or construct a genuine counterexample outside that skeleton model.  For \(P_k=\{p_1,\ldots,p_k\}\), let \(\nu_{P_k}(p_i\in S)=1/p_i\), \(S_k=\sum_{i\le k}1/p_i\), and \(H_{k,\theta}=\{S:|S|>\theta S_k\}\).  Prove or refute
\[
U_k(\theta)=
\sup\{\nu_{P_k}(\mathcal F):\mathcal F\subseteq H_{k,\theta},\ \mathcal F\text{ union-free}\}\to0
\]
for every fixed \(0\le\theta<1\).  A proof gives the biased lower-shadow theorem and hence \(M_{P_k}(\theta)\to0\); then isolate the lift to the exponent-grid residual \(R_P(\theta)\).  The next subtarget is no longer to test max-fiber antichain skeletons; they are killed conditionally by `mrw-54968b07a069`.  Instead, prove a compression/decomposition theorem reducing positive-mass union-free families to antichain-like max-fiber pieces plus negligible rank-layer/fixed-core residues, or build an explicit positive-mass family that is not rank-only, not a fixed finite-core cylinder, not upward-closed, not exact-rank-layer-like, and not a max-fiber antichain skeleton.  Use weighted Kleitman, compression under unequal prime weights, product-measure containers, junta/decomposition, or boundary absorption only as lemmas toward this weighted theorem.  Do not cite uniform cardinality bounds as sufficient, do not pursue global boundary-smallness, fixed-\(P\) table extension, pointwise support-only counts, or plain ambient triple-density estimates.  Include Scout and Oracle where applicable, use literal prompt text or inline-file mode with Oracle CLI 0.12.1, treat all output as advisory, and enforce the patch gate.

## Next Advisor Review Trigger

Run a full Advisor Gate at the start of the next loop.  The Advisor must keep #25 parked unless a new projection-balance or projection-energy invariant is proposed, and must reject plans that reprove raw union-tail, essential-index, abstract block-uniform, unshifted CRT, threshold-aware CRT, activation-scale \(Q_I\), or first-cycle entropy criteria.  It must also reject \(P_1/P_n\), routine \(s=9\) tail inversion, Gamma-only obstruction chasing, public staging, GitHub, or Gmail without explicit user approval.

## Heartbeat

- active thread heartbeat: `pudim-p1-cm-continuation`
- purpose: legacy heartbeat name; current continuation target is a full non-staging Pudim loop on the Erdos #536 prime-biased weighted union-free frontier.

## Continuation Prompt

Use $pudim. Run one full non-staging Pudim loop in `C:\Users\domin\OneDrive\Projects_Codex\pudim\zetalaw-demo`. Read `.math-wiki/GOAL.md`, `.math-wiki/STATUS.md`, `.math-wiki/STRATEGY.md`, raw log `20260519T105423Z-erdos536-max-fiber-antichain-mass.md`, proposition node `mrw-54968b07a069`, proposition node `mrw-b4075311abd3`, open problem node `mrw-55a8d9eddd2e`, example node `mrw-2ff2fe94bc57`, lower-shadow problem `mrw-d0402aea6f58`, pair-link node `mrw-3c39ca3d1973`, biased squarefree residual problem `mrw-37dbc6aeedf9`, tilted-boundary proposition `mrw-2a2c5551301e`, union-tilted/rank-layer obstruction `mrw-67f99fecf9e2`, rank-only proposition `mrw-02dadc6b1bba`, finite-core-cylinder proposition `mrw-30aae977a4b6`, source note `references/sources/20260519T105423Z-product-measure-antichain-context.md`, and source note `references/sources/20260519T101422Z-erdos-536-union-free-context.md`. Current durable frontier: Erdos #536 squarefree support residual after max-fiber antichain skeletons were killed conditionally under product-measure LYM/anti-concentration. Primary target: bridge from this killed skeleton template to arbitrary prime-biased high-support union-free families, or refute the theorem with a genuine counterexample.  Prove or refute
\[
U_k(\theta)=
\sup\{\nu_{P_k}(\mathcal F):\mathcal F\subseteq H_{k,\theta},\ \mathcal F\text{ union-free}\}\to0
\]
for every fixed \(0\le\theta<1\), where \(\nu_{P_k}(p_i\in S)=1/p_i\). If proved, conclude the biased lower-shadow theorem and \(M_{P_k}(\theta)\to0\), then isolate the lift to \(R_P(\theta)\). If refuted, construct an explicit positive-mass high-support union-free family that is not rank-only, not fixed-core, not upward-closed, not exact-rank-layer-like, and not a max-fiber antichain skeleton, then test full non-union pair-link intervals. Use weighted Kleitman/compression/container/junta or a max-fiber decomposition theorem rather than uniform cardinality bounds alone. Include Scout and Oracle where applicable using literal prompt text or inline-file mode; if Oracle browser automation again fails with localhost `ECONNREFUSED`, record the blocker and continue locally. Treat raw output as advisory until Student/Librarian audit, explicit wiki patch, refresh, and Editor preflight. Do not stage, push, create Gmail drafts, send email, contact authors, run publisher-stage, return to routine \(s=9\), \(P_1/P_n\), Gamma-only, fixed-\(P\) table extension, pointwise support-only counts, global boundary-smallness, or Erdos #25 residue-tail work unless STATUS/STRATEGY explicitly revives them.

## Latest Cycle Update: 20260519T113424Z

- Full non-staging Pudim loop `20260519T113424Z-erdos536-union-free-decomposition-gap` completed locally.
- Scout was run and ingested raw-only.  The live Scout browser leg stalled with repeated no-thinking-status messages and saved no mathematical response.
- A focused Oracle dry-run succeeded with about 71.4k tokens and 9 attached files.  The live Oracle browser leg failed before sending: `Attachments never reached a clickable send button before timeout.`
- New proved proposition `mrw-265ec9f57561` records a structural criterion: for fixed \(0<\theta<1\), if the moving maximum fibers of \(\mathcal F_k\) have weighted antichain-cover width
\[
B_k(\theta)=
\sum_{\substack{m\le k\\T_m>\theta S_k/2}}w_{m,k}a_{m,k}
=o(\sqrt{S_k}),
\]
then \(\nu_k(\mathcal F_k\cap H_{k,\theta})\to0\).
- This does not prove \(U_k(\theta)\to0\).  It sharpens the obstruction: any positive-mass high-support union-free counterexample for \(0<\theta<1\) must have \(B_k(\theta)\not=o(\sqrt{S_k})\) along a subsequence.
- No `THEORY_LATEST` successor was saved; the promotion is structural wiki progress, not manuscript-level proved material.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove that prime-biased high-support union-free families have subcritical weighted max-fiber antichain-cover width, or construct a genuine positive-mass counterexample with \(B_k(\theta)\gtrsim\sqrt{S_k}\) on the moving maxima.

Start from raw log `20260519T113424Z-erdos536-union-free-decomposition-gap.md`, proposition `mrw-265ec9f57561`, prior max-fiber proposition `mrw-54968b07a069`, union-free reformulation `mrw-b4075311abd3`, open problem `mrw-55a8d9eddd2e`, and the lower-shadow/pair-link nodes already listed above.  The next proof mechanism should be a weighted compression, product-measure container, junta/decomposition, or fiber-width theorem under \(\nu_{P_k}(p_i\in S)=1/p_i\).  If the theorem fails, the counterexample must be explicit, high-support, positive \(\nu_{P_k}\)-mass, union-free, and not rank-only, fixed-core, upward-closed, exact-rank-layer-like, max-fiber antichain, or subcritical fiber-width.

If a squarefree theorem is proved, use `mrw-b4075311abd3` and `mrw-3c39ca3d1973` to conclude the biased lower-shadow theorem and \(M_{P_k}(\theta)\to0\), then isolate the lift to the exponent-grid residual \(R_P(\theta)\).  Do not return to fixed-\(P\) table extension, pointwise support-only counts, global boundary-smallness, routine \(s=9\), \(P_1/P_n\), Gamma-only, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact unless explicitly revived.

## Continuation Prompt: supersedes above

Use $pudim. Run one full non-staging Pudim loop in `C:\Users\domin\OneDrive\Projects_Codex\pudim\zetalaw-demo`. Read `.math-wiki/GOAL.md`, `.math-wiki/STATUS.md`, `.math-wiki/STRATEGY.md`, raw log `20260519T113424Z-erdos536-union-free-decomposition-gap.md`, proposition `mrw-265ec9f57561`, prior proposition `mrw-54968b07a069`, union-free reformulation `mrw-b4075311abd3`, weighted union-free open problem `mrw-55a8d9eddd2e`, max-fiber skeleton example `mrw-2ff2fe94bc57`, lower-shadow problem `mrw-d0402aea6f58`, pair-link node `mrw-3c39ca3d1973`, biased residual problem `mrw-37dbc6aeedf9`, low-support criterion `mrw-4daa694d9526`, tilted-boundary proposition `mrw-2a2c5551301e`, rank-layer obstruction `mrw-67f99fecf9e2`, rank-only proposition `mrw-02dadc6b1bba`, and finite-core proposition `mrw-30aae977a4b6`.  Current durable frontier: Erdos #536 squarefree support residual after subcritical max-fiber antichain-cover width was proved negligible for \(0<\theta<1\).  Primary target: prove union-free families satisfy that subcritical width condition, or construct a true positive-mass high-support union-free counterexample with \(B_k(\theta)\gtrsim\sqrt{S_k}\).  Include Scout and Oracle where applicable using literal prompt text and forward-slash file paths with Oracle CLI 0.12.1; if browser automation fails, record the exact blocker and continue locally.  Treat all raw output as advisory until local audit, explicit wiki patch, refresh, and Editor preflight.

## Latest Cycle Update: 20260519T121424Z

- Full non-staging Pudim loop `20260519T121424Z-erdos536-compression-obstruction` completed locally.
- Scout was run and ingested raw-only.  The live response returned to parked routine \(s=9\) inverse-tail material and was not promoted.
- A focused Oracle dry-run succeeded after switching to literal one-line prompt text and forward-slash file paths.  The live Oracle run completed with `--browser-attachments never`; the response was audited locally before any wiki patch.
- New proved counterexample `mrw-8fcc1c2c5cda` shows that ordinary unrestricted \(ij\)-shifting does not preserve union-free families.  On \(\{1,2,3\}\),
\[
\mathcal F=\{\{1\},\{1,2\},\{3\}\}
\]
is union-free, but \(S_{2,3}\mathcal F=\{\{1\},\{2\},\{1,2\}\}\) is not, since \(\{1\}\cup\{2\}=\{1,2\}\).
- The counterexample is in the relevant prime-weighted direction:
\[
\nu(\mathcal F)=\frac7{15},
\qquad
\nu(S_{2,3}\mathcal F)=\frac8{15}
\]
for weights \(q_1=1/2,q_2=1/3,q_3=1/5\).
- New open problem `mrw-3474bf5c904f` records the replacement target: find a union-aware weighted compression/decomposition mechanism, or use failed shifts as shift-resistance certificates feeding the max-fiber width, union-triple, or pair-link route.
- No `THEORY_LATEST` successor was saved; this was wiki-level route clarification and a proved obstruction to a proof template, not manuscript-level progress toward a final #536 theorem.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: replace ordinary weighted shifting, which is now blocked by `mrw-8fcc1c2c5cda`, with a valid max-fiber/container/junta/decomposition mechanism for prime-biased high-support union-free families.  Equivalently, solve or sharpen open problem `mrw-3474bf5c904f`.

Start from raw log `20260519T121424Z-erdos536-compression-obstruction.md`, counterexample `mrw-8fcc1c2c5cda`, open problem `mrw-3474bf5c904f`, structural width proposition `mrw-265ec9f57561`, union-free theorem target `mrw-55a8d9eddd2e`, union-free reformulation `mrw-b4075311abd3`, pair-link node `mrw-3c39ca3d1973`, and the prior max-fiber/background nodes listed above.  The next proof mechanism should avoid unrestricted shifts.  If using ad-extremis or property-preserving shifts, every failed shift should produce a quantitative shift-resistance certificate that feeds \(B_k(\theta)\gtrsim\sqrt{S_k}\), a union triple, or a pair-link triple.

If a squarefree theorem is proved, use `mrw-b4075311abd3` and `mrw-3c39ca3d1973` to conclude the biased lower-shadow theorem and \(M_{P_k}(\theta)\to0\), then isolate the lift to the exponent-grid residual \(R_P(\theta)\).  Do not return to fixed-\(P\) table extension, pointwise support-only counts, global boundary-smallness, routine \(s=9\), \(P_1/P_n\), Gamma-only, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact unless explicitly revived.

## Continuation Prompt: supersedes above


## Latest Cycle Update: 20260519T125425Z

- Full non-staging Pudim loop `20260519T125425Z-erdos536-union-aware-decomposition` completed locally.
- Oracle caught a real defect in the first cylinder corollary: a core cylinder need not contain a union triple when the tail has fewer than two coordinates.  The promoted node was patched to the corrected condition
\[
|P\setminus Q|\ge2
\qquad\text{and}\qquad
|U|+|P\setminus Q|-1>\theta S_P.
\]
- New proved proposition `mrw-bf35ac1a9ad3` records the core-fiber decomposition for union-free families.  For \(P=Q\sqcup R\) and fibers
\[
\mathcal F_U=\{T\subseteq R:\ U\cup T\in\mathcal F\},
\]
global union triples are exactly cross-fiber relations \(U\cup V=W\), \(A\cup B=C\) with full members \(U\cup A,V\cup B,W\cup C\).  Hence each single fiber is union-free, but fiberwise union-freeness is not enough; the cross-fiber constraint is the active structure.
- The result does not prove \(U_k(\theta)\to0\).  It blocks naive full-core-cylinder containers and sets up the next quantitative rooted-container/deletion-trace route.
- No `THEORY_LATEST` successor was saved; this is structural wiki progress, not manuscript-level #536 completion.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: turn the core-fiber constraint in `mrw-bf35ac1a9ad3` into a quantitative cross-fiber/junta/container theorem for prime-biased high-support union-free families, or construct a genuine broad-fiber positive-mass obstruction.

Start from raw log `20260519T125425Z-erdos536-union-aware-decomposition.md`, proposition `mrw-bf35ac1a9ad3`, ordinary-shift counterexample `mrw-8fcc1c2c5cda`, union-aware compression problem `mrw-3474bf5c904f`, width proposition `mrw-265ec9f57561`, union-free reformulation `mrw-b4075311abd3`, weighted union-free open problem `mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, pair-link node `mrw-3c39ca3d1973`, and biased residual problem `mrw-37dbc6aeedf9`.

The next proof should show that any positive \(\nu_{P_k}\)-mass family \(\mathcal F\subset H_{k,\theta}\) that is union-free either forces a cross-fiber union triple, collapses into a rank-layer-like or other already quarantined negligible skeleton, or yields an explicit broad-fiber obstruction.  A useful first sublemma is the two-spare-tail face constraint: in many core fibers, the triple
\[
T\cup\{x\},\qquad T\cup\{y\},\qquad T\cup\{x,y\}
\]
forces at least one deletion; the hard part is converting these local deletion constraints into a vanishing prime-biased high-support mass bound.

Include Scout and Oracle where applicable using literal prompt text and forward-slash file paths with Oracle CLI 0.12.1.  Treat all raw output as advisory until local audit, explicit wiki patch, refresh, and Editor preflight.  Do not stage, push, create Gmail drafts, send email, contact authors, run publisher-stage, return to routine \(s=9\), \(P_1/P_n\), Gamma-only, fixed-\(P\) table extension, pointwise support-only counts, global boundary-smallness, ordinary shifted-family normal form, or Erdos #25 residue-tail work unless STATUS/STRATEGY explicitly revives them.

## Continuation Prompt: supersedes above


## Latest Cycle Update: 20260519T133426Z

- Full non-staging Pudim loop `20260519T133426Z-erdos536-cross-fiber-container` completed locally.
- Erudition inspected union-free/container context again, including union-free containers and general hypergraph container sources.  No external theorem was promoted as locally proved.
- New proved obstruction note `mrw-0d6b8cbd7ced` shows that fixed-depth bounded-deletion union hypergraphs cannot supply the needed prime-biased high-support supersaturation.  For fixed \(d\ge1\), the rank-congruence family
\[
\mathcal R_{k,a}^{(d+1)}
=\{S\subseteq P_k:\ |S|\equiv a\pmod {d+1}\}
\]
has
\[
\nu_k(\mathcal R_{k,a}^{(d+1)}\cap H_{k,\theta})\to\frac1{d+1}
\]
for every fixed \(0\le\theta<1\), while avoiding every union triple with
\[
1\le |C\setminus A|,\ |C\setminus B|\le d.
\]
- In particular, the two-spare-tail face mechanism from the previous prompt is obstructed at \(d=1\): parity-rank families have asymptotic high-support mass \(1/2\) and avoid all such faces.
- This is not a counterexample to the full weighted union-free theorem.  Rank-congruence families contain full union triples with deletion size \(d+1\) once supports are large.  The route consequence is narrower: any successful container/deletion-trace proof must use unbounded deletion traces, the full union hypergraph, the full pair-link hypergraph, or a mechanism converting bounded-depth resistance into a genuine full union triple.
- Focused Oracle audited `mrw-0d6b8cbd7ced` as proved after wording patches clarifying fixed \(d\), the use of \(\sum_p1/p=\infty\), and the nonterminal nature of the obstruction.
- No `THEORY_LATEST` successor was saved; this is route-structural wiki progress, not a manuscript-level #536 solution.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: replace the killed fixed-\(d\) bounded-deletion/two-spare route with an unbounded deletion-trace or full union-hypergraph container theorem for the prime-biased weighted union-free problem.

Start from raw log `20260519T133426Z-erdos536-cross-fiber-container.md`, obstruction note `mrw-0d6b8cbd7ced`, core-fiber proposition `mrw-bf35ac1a9ad3`, weighted union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, deletion-trace proposition `mrw-cc4f876149b7`, pair-link criterion `mrw-3c39ca3d1973`, union-free reformulation `mrw-b4075311abd3`, and bounded-deletion source note `references/sources/20260519T133426Z-bounded-deletion-container-context.md`.

The next concrete subtarget is a growing-deletion trace theorem: for lower-shadow-free \(\mathcal F\subset H_{k,\theta}\), the traces
\[
\mathcal D_{\mathcal F}(C)=\{D\subseteq C:\ D\ne\varnothing,\ C\setminus D\in\mathcal F\}
\]
are pairwise intersecting for every \(C\in\mathcal F\).  Prove that positive \(\nu_k\)-mass forces, at deletion sizes growing with \(S_k\), two disjoint deletions in some trace; or construct a positive-mass high-support family whose deletion traces remain pairwise intersecting at all growing scales.  If such a family exists, test it against the full pair-link intervals and audit any reverse lift to \(R_P(\theta)\).

Include Scout and Oracle where applicable using literal prompt text and forward-slash file paths with Oracle CLI 0.12.1.  Treat all raw output as advisory until local audit, explicit wiki patch, refresh, and Editor preflight.  Do not stage, push, create Gmail drafts, send email, contact authors, run publisher-stage, return to routine \(s=9\), \(P_1/P_n\), Gamma-only, fixed-\(P\) table extension, pointwise support-only counts, global boundary-smallness, ordinary shifted-family normal form, full-core-cylinder approximation, or fixed-\(d\) bounded-deletion supersaturation as terminal evidence.

## Continuation Prompt: supersedes above


## Latest Cycle Update: 20260519T141427Z

- Full non-staging Pudim loop `20260519T141427Z-erdos536-growing-deletion-trace` completed locally.
- Erudition inspected intersecting-family, star, junta, and product-measure context.  No external theorem was imported as locally proved.
- New proved note `mrw-6a9d1e4f2c8b` shows that single-trace intersectingness cannot supply the growing-deletion theorem.  For a finite top set \(C_n\), root \(x_n\in C_n\), and \(0<\lambda<1\), the star trace
\[
\mathcal S_{x_n}(C_n)=\{D\subseteq C_n:\ x_n\in D\}
\]
is pairwise intersecting and has deletion mass \(\lambda\) under the product deletion law.  If
\[
\limsup_{n\to\infty}\frac{L_n}{|C_n|}<\lambda,
\]
then
\[
\pi_{C_n,\lambda}\{D\in\mathcal S_{x_n}(C_n): |D|\ge L_n\}\to\lambda.
\]
- Oracle audited the note as promotable after wording patches clarifying that thresholds are measured relative to \(|C|\), that thresholds comparable to \(S_k\) need \(|C|\asymp S_k\), and that the note is not a positive-mass union-free counterexample.
- Route consequence: the next #536 loop must target a global root-consistency theorem, a rooted-container theorem, or the full pair-link hypergraph.  A theorem about one trace being intersecting is insufficient.
- No `THEORY_LATEST` successor was saved; this is route-structural wiki progress, not manuscript-level #536 completion.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove or refute the global root-consistency step for prime-biased high-support union-free families.  Start from raw log `20260519T141427Z-erdos536-growing-deletion-trace.md`, new note `mrw-6a9d1e4f2c8b`, bounded-deletion obstruction `mrw-0d6b8cbd7ced`, core-fiber proposition `mrw-bf35ac1a9ad3`, deletion-trace proposition `mrw-cc4f876149b7`, weighted union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, pair-link criterion `mrw-3c39ca3d1973`, and union-free reformulation `mrw-b4075311abd3`.

Prove that positive \(\nu_{P_k}\)-mass inside \(H_{k,\theta}\) cannot coherently realize star-like or finite-junta-like deletion traces across many top sets without creating a union triple, or construct an explicit positive-mass high-support union-free family realizing coherent rooted traces.  If refuted, test the family against full pair-link intervals and any reverse lift to \(R_P(\theta)\).  Do not use trace-local intersectingness, fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact unless explicitly revived.

## Continuation Prompt: supersedes above


## Latest Cycle Update: 20260519T145428Z

- Full non-staging Pudim loop `20260519T145428Z-erdos536-root-consistency` completed locally.
- Erudition inspected rooted-container and finite-junta context, especially Balogh--Wagner rooted containers for union-free families, general hypergraph containers, and Dinur--Friedgut/Friedgut intersecting-junta vocabulary.  No external theorem was imported as proved local material.
- Focused Oracle dry-run with attachments succeeded, but the live browser run failed with the exact blocker `Attachments never reached a clickable send button before timeout`.  The inline retry returned `You've hit your limit. Please try again later.`  The saved Oracle response is therefore a blocker record only.
- New proved note `mrw-1f7c23e5a9d4` shows that finite-junta deletion traces also obstruct trace-local rooted estimates.  If \(J\) is fixed finite, \(\mathcal I\subseteq2^J\) is pairwise intersecting and \(\varnothing\notin\mathcal I\), then
\[
\mathcal T_{\mathcal I,J}(C)=
\{D\subseteq C:\ D\cap J\in\mathcal I\}
\]
is pairwise intersecting and has product deletion mass \(\pi_{J,\lambda}(\mathcal I)\).  For \(|C_n|=n\) and \(\limsup L_n/n<\lambda\),
\[
\pi_{C_n,\lambda}\{D\in\mathcal T_{\mathcal I,J}(C_n):|D|\ge L_n\}
\to \pi_{J,\lambda}(\mathcal I).
\]
- This is not a counterexample to `mrw-55a8d9eddd2e`.  It says that even a finite-junta classification of individual deletion traces cannot prove vanishing below the ambient deletion mean.  The next theorem must be global: root/junta consistency across many top supports, a rooted-container theorem, or the full pair-link hypergraph.
- No `THEORY_LATEST` successor was saved; this is route-structural wiki progress, not manuscript-level #536 completion.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove a global root-consistency/rooted-container theorem under \(\nu_{P_k}(p_i\in S)=1/p_i\), showing positive-mass high-support union-free families cannot realize positive-mass finite-junta deletion traces coherently, or construct an explicit coherent positive-mass high-support union-free counterexample.

Start from new note `mrw-1f7c23e5a9d4`, star note `mrw-6a9d1e4f2c8b`, bounded-deletion obstruction `mrw-0d6b8cbd7ced`, core-fiber proposition `mrw-bf35ac1a9ad3`, deletion-trace proposition `mrw-cc4f876149b7`, weighted union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, pair-link criterion `mrw-3c39ca3d1973`, and union-free reformulation `mrw-b4075311abd3`.  If a coherent counterexample is found, test it against full pair-link intervals and any reverse lift to \(R_P(\theta)\).

Do not use trace-local intersectingness, finite-junta trace-local mass, fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact unless explicitly revived.

## Latest Cycle Update: 20260520T014549Z

- Full non-staging Pudim loop
  `20260520T014549Z-erdos-536-rare-pair-link-geometry-prove-or-refute-a-rare-hig`
  completed locally.
- Scout ran with Oracle CLI 0.12.1 and `--browser-inline-files`.  It returned
  routine \(s=9\) inverse-tail material from the zeta-tail branch, so it was
  Scout claim was promoted.
- Erudition inspected the active Erdos #536 page, the related weak-sunflower
  page, and modern sunflower context only as vocabulary/source grounding.  No
  external theorem was imported as a local proof.
- New proved proposition `mrw-b1f87c9d6a42` shows that every exact rank layer
  \(\binom Pr\), \(2\le r\le |P|-1\), has full genuine pair-link projection.
  The proof is the explicit same-rank construction
  \[
  B=(A\setminus\{x\})\cup\{y\},\qquad
  C=(A\setminus\{z\})\cup\{y\},
  \]
  with \(x,z\in A\) distinct and \(y\notin A\).
- Consequently the full capped band
  \[
  \{A\subseteq P_k:\theta S_k<|A|\le\alpha S_k\}
  \]
  has full genuine pair-link first-coordinate projection for all sufficiently
  large \(k\), although prior nodes still give \(O(S_k^{-1})\) conditional
  random-pair visibility under their cap hypotheses.
- This is a route-kill, not a counterexample and not a proof of
  \(U_k(\theta)\to0\).  Sparse random-pair measure can coexist with full vertex
  projection, so the next route must use the pair-link-free/union-free
  hypergraph structure itself.
- Focused Oracle completed with `--browser-inline-files` and confirmed the
  construction, while explicitly rejecting endpoint-degree, rectangle,
  counterexample, arbitrary-subfamily, and \(R_P(\theta)\)-lift overclaims.
- No `THEORY_LATEST` successor was saved; this is route-structural wiki
  progress, not manuscript-level #536 completion.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove a sparse
pair-link hypergraph/container theorem for positive-mass capped high-support
union-free or squarefree pair-link-free families, or construct a genuine
positive-mass family whose rare pair-link relation has full or near-full
projection but still avoids all union/pair-link triples.

Start from raw log
proposition `mrw-b1f87c9d6a42`, endpoint/rectangle corollary
`mrw-6d4a8b0f2c91`, capped random-pair corollary `mrw-4f1e9a2d6b73`,
entropy-overlap proposition `mrw-c7f4e0c9a821`, pair-link criterion
`mrw-3c39ca3d1973`, weighted union-free problem `mrw-55a8d9eddd2e`,
lower-shadow problem `mrw-d0402aea6f58`, union-free reformulation
`mrw-b4075311abd3`, deletion-trace proposition `mrw-cc4f876149b7`, source note
`references/sources/20260520T014549Z-rare-pair-link-full-band-projection-context.md`,
response

The next theorem should control
\[
E_k^\circ(F)=\{(A,B)\in F^2:\ I^\circ(A,B)\cap F\ne\emptyset\},
\qquad
\lambda_k^{\otimes2}(E_k^\circ(F))=O(S_k^{-1}),
\]
using more than projection or endpoint degree: either the full three-uniform
pair-link hypergraph, a union-specific container/deletion-trace mechanism, or
a structural counterexample tested against `mrw-3c39ca3d1973` and any possible
reverse lift to \(R_P(\theta)\).

Do not use projection-only sparsity, random-pair capped supersaturation,
positive endpoint-degree/rectangle supersaturation, sparse-intersection code
templates, one/few or sublinear high-intersection clique covers,
near-total-root visibility, fixed-junta visibility, max-fiber antichain
skeletons, fixed-core cylinders, rank-only families, exact-rank-layer-like
families, trace-local intersectingness, finite-junta trace-local mass,
fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-\(P\) table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging,
GitHub, Gmail, or author contact as terminal evidence unless explicitly
revived.

## Continuation Prompt: supersedes above

Use $pudim in `C:\Users\domin\OneDrive\Projects_Codex\pudim\zetalaw-demo`.
Run one full non-staging Pudim loop.  Read `.math-wiki/GOAL.md`,
`.math-wiki/STATUS.md`, `.math-wiki/STRATEGY.md`, raw log
`20260520T014549Z-erdos-536-rare-pair-link-geometry-prove-or-refute-a-rare-hig.md`,
proposition `mrw-b1f87c9d6a42`, corollary `mrw-6d4a8b0f2c91`, corollary
`mrw-4f1e9a2d6b73`, proposition `mrw-c7f4e0c9a821`, proposition
`mrw-3c39ca3d1973`, problem `mrw-55a8d9eddd2e`, problem `mrw-d0402aea6f58`,
proposition `mrw-b4075311abd3`, proposition `mrw-cc4f876149b7`, source note
`references/sources/20260520T014549Z-rare-pair-link-full-band-projection-context.md`,
response
before choosing the target.  Current durable frontier: rare pair-link relations
inside fixed caps have \(O(S_k^{-1})\) conditional pair measure and no positive
endpoint cores or rectangles, but full capped rank bands can still have full
genuine pair-link projection.  Primary target: prove a structural sparse
pair-link hypergraph/container theorem for positive-mass capped union-free or
pair-link-free families, or construct an explicit positive-mass high-support
counterexample with full or near-full rare projection and test it against full
pair-link intervals plus any reverse lift to \(R_P(\theta)\).  Do not use
projection-only sparsity, endpoint-degree, rectangles, routine \(s=9\), or any
previously quarantined mechanism as terminal evidence unless STATUS/STRATEGY
explicitly revives it.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove a weighted
one-swap expansion theorem for positive-mass high-support pair-link-free or
union-free families under \(\nu_{P_k}(p_i\in S)=1/p_i\), or construct an
explicit positive-mass low-expansion counterexample and test it against the
full pair-link interval criterion plus any reverse lift to \(R_P(\theta)\).

Start from raw log
new proposition `mrw-25cdd8da0601`, full-band projection proposition
`mrw-b1f87c9d6a42`, endpoint/rectangle corollary `mrw-6d4a8b0f2c91`, capped
random-pair corollary `mrw-4f1e9a2d6b73`, entropy-overlap proposition
`mrw-c7f4e0c9a821`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`,
deletion-trace proposition `mrw-cc4f876149b7`, source note
`references/sources/20260520T022056Z-one-swap-insertion-fiber-context.md`,
and Oracle response

The next theorem should convert the local fiber obstruction
\[
|D_y^\mathcal F(A)|\le1
\]
into a measured contradiction for positive-mass high-support candidates, or
exhibit a genuine family with globally low same-insertion one-swap expansion.
Do not use projection-only sparsity, endpoint-degree/rectangle
supersaturation, exact-rank-layer templates, trace-local or finite-junta trace
mass, fixed-depth bounded deletion, ordinary shifting, routine \(s=9\),
\(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub,
Gmail, or author contact as terminal evidence unless explicitly revived.

## Continuation Prompt: supersedes above

Use $pudim in `C:\Users\domin\OneDrive\Projects_Codex\pudim\zetalaw-demo`.
Run one full non-staging Pudim loop.  Read `.math-wiki/GOAL.md`,
`.math-wiki/STATUS.md`, `.math-wiki/STRATEGY.md`, raw log
new proposition `mrw-25cdd8da0601`, prior full-band projection proposition
`mrw-b1f87c9d6a42`, endpoint/rectangle corollary `mrw-6d4a8b0f2c91`, capped
random-pair corollary `mrw-4f1e9a2d6b73`, entropy-overlap proposition
`mrw-c7f4e0c9a821`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`,
deletion-trace proposition `mrw-cc4f876149b7`, source note
`references/sources/20260520T022056Z-one-swap-insertion-fiber-context.md`,
and Oracle response
before choosing the target.  Current durable frontier: pair-link-free
families have injective one-swap insertion fibers, so around each
\(A\in\mathcal F\) at most one deletion can use a fixed inserted coordinate.
Primary target: prove a weighted one-swap expansion theorem showing
positive-mass high-support pair-link-free or union-free families must have
same-insertion collisions, or construct an explicit positive-mass
low-expansion counterexample and test it against full pair-link intervals plus
any reverse lift to \(R_P(\theta)\).  Do not use projection-only sparsity,
endpoint-degree/rectangle supersaturation, rank-layer templates, trace-local
or finite-junta trace mass, fixed-depth bounded deletion, routine \(s=9\), or
any previously quarantined mechanism as terminal evidence unless
STATUS/STRATEGY explicitly revives it.

## Continuation Prompt: supersedes above

Use $pudim in `C:\Users\domin\OneDrive\Projects_Codex\pudim\zetalaw-demo`.
Run one full non-staging Pudim loop.  Read `.math-wiki/GOAL.md`,
`.math-wiki/STATUS.md`, `.math-wiki/STRATEGY.md`, raw log
new proposition `mrw-2bcc2955fe38`, weighted Mantel proposition
`mrw-a32a6d3a5f20`, two-extension slice proposition `mrw-354b105d4977`,
pair-link criterion `mrw-3c39ca3d1973`, one-swap proposition
`mrw-25cdd8da0601`, full-band projection proposition `mrw-b1f87c9d6a42`,
entropy-overlap proposition `mrw-c7f4e0c9a821`, weighted union-free problem
`mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`,
union-free reformulation `mrw-b4075311abd3`, deletion-trace proposition
`mrw-cc4f876149b7`, source note
`references/sources/20260520T110040Z-cross-core-path-shadow-context.md`,
Scout ingestion
Oracle response
before choosing the target.  Current durable frontier: two-edge paths in
pair-link-free two-extension slices cast full endpoint-pair completion shadows
over every \(D\subseteq R\cup\{y\}\), so complete bipartite local Mantel
extremizers cannot be repeated across cores without deleting many lower-core
same-side endpoint pairs.  Primary target: prove a prime-biased product-measure
lower-shadow theorem quantifying these path-shadow deletions enough to force
quadratic aggregate Mantel defect or vanishing high-support pair-link-free
mass; or construct an explicit positive-mass dense-slice family evading the
path-shadow lower shadows and test every full pair-link interval plus any
reverse lift to \(R_P(\theta)\).  Do not use direct weighted-Mantel aggregation,
projection-only sparsity, random-pair capped supersaturation, positive
endpoint-degree/rectangle supersaturation, rank-layer templates, trace-local or
finite-junta trace mass, fixed-depth bounded deletion, ordinary shifting,
full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table
extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail
work, staging, GitHub, Gmail, or author contact as terminal evidence unless
STATUS/STRATEGY explicitly revives them.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove a global
coherent-corridor assembly theorem for Erdos #536, or construct the coherent
assembly and test it directly.

Start from raw log
new proposition `mrw-827094b15843`, previous proposition
`mrw-8a0c228a0166`, corridor-refinement proposition `mrw-a9efecc818c7`,
signature fragmentation proposition `mrw-816fd32c3294`, nested coherence
proposition `mrw-fced7420b905`, fixed blow-up proposition
`mrw-c7c76faed872`, complete-bipartite stress test `mrw-f83b56a1aa89`,
path-shadow bottleneck `mrw-c6d0c6fa4d30`, path-shadow proposition
`mrw-2bcc2955fe38`, weighted Mantel proposition `mrw-a32a6d3a5f20`,
two-extension slice proposition `mrw-354b105d4977`, pair-link criterion
`mrw-3c39ca3d1973`, weighted union-free problem `mrw-55a8d9eddd2e`,
lower-shadow problem `mrw-d0402aea6f58`, union-free reformulation
`mrw-b4075311abd3`, source note
`references/sources/20260521T025048Z-coherent-normal-form-context.md`, Scout

Current durable frontier: a heavy corridor that persists through many nested
refinements is locally forced into one coherent refined-signature normal form;
equality is a complete positive-weight corridor on that single complementary
signature pair.  Primary target: prove that positive-mass high-support
pair-link-free families cannot assemble many such coherent normal-form
corridors without creating a full pair-link interval hit, or construct the
assembly and test every full pair-link interval plus any possible
\(R_P(\theta)\) lift.

Do not stage, push, create Gmail drafts, send email, contact authors, run
publisher-stage, or use direct weighted-Mantel aggregation, path-shadow
disjointness alone, projection-only sparsity, endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-P table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, or Erdos #25 residue-tail work as
terminal evidence unless STATUS.md/STRATEGY.md explicitly revives them.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: leave two-uniform
endpoint mass and prove either a terminal-core residual decay/cross-fiber
exclusion theorem below the fractional bipartite envelope, or construct and
audit a higher-uniformity interval-shielded endpoint support, starting with
dense cancellative 3-uniform families.

Start from new corollary `mrw-d602b51accb8`, odd-cycle proposition
`mrw-3161f39fd270`, bipartite subtower corollary `mrw-50bca8113dbf`,
triangle-free endpoint-pair proposition `mrw-1b04240e9886`, shielded-residual
corollary `mrw-3d6bb8271a4c`, cross-pattern factorization
`mrw-20ca89f696f2`, fixed-pattern residual proposition `mrw-1f23857438d4`,
endpoint-pattern residual proposition `mrw-05f82d03b190`, pointwise-incidence
corollary `mrw-7f0eb8d1648c`, and core weighted union-free nodes
`mrw-55a8d9eddd2e`, `mrw-d0402aea6f58`, and `mrw-b4075311abd3`.

Do not stage, push, create Gmail drafts, send email, contact authors, run
publisher-stage, or use bipartite endpoint-pair lifts, triangle-free
endpoint-pair lifts, odd-cycle endpoint-pair lifts, interval-shielded endpoint
mass alone, direct weighted-Mantel aggregation, endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-P table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, ambient endpoint-moment budgets alone,
singleton endpoint lifts alone, disjoint block/matching endpoint lifts alone,
or Erdos #25 residue-tail work as terminal evidence unless STATUS.md/STRATEGY.md
explicitly revives them.

## Continuation Prompt: supersedes above

Use $pudim in `C:/Users/domin/OneDrive/Projects_Codex/pudim/zetalaw-demo`.
Run one full non-staging Pudim loop.  Read `.math-wiki/GOAL.md`,
`.math-wiki/STATUS.md`, `.math-wiki/STRATEGY.md`, raw log
Scout raw log
response
new corollary `mrw-d602b51accb8`, odd-cycle proposition `mrw-3161f39fd270`,
bipartite subtower corollary `mrw-50bca8113dbf`, triangle-free endpoint-pair
proposition `mrw-1b04240e9886`, shielded-residual corollary
`mrw-3d6bb8271a4c`, cross-pattern factorization `mrw-20ca89f696f2`,
fixed-pattern residual proposition `mrw-1f23857438d4`, endpoint-pattern
residual proposition `mrw-05f82d03b190`, pointwise-incidence corollary
`mrw-7f0eb8d1648c`, overfull strict residual proposition `mrw-c82229c73d8d`,
ambient-moment counterexample `mrw-d65c4d544e56`, endpoint decoupling
proposition `mrw-d7b3299d3813`, endpoint-moment budget corollary
`mrw-2a765ca2676f`, strict-deletion iteration `mrw-5df7f8135e2c`, and
absorbed-window proposition `mrw-791fae526f01`.

Current durable frontier: every two-uniform triangle-free endpoint-pair shield
is bounded by the fractional bipartite envelope
\[
\mathcal R_G(L)\le \frac{P_0(B)R_B^2}{4}\mathfrak M_T(L-2),
\]
and under diffuse endpoint weights has endpoint mass at most
\(e^{-\alpha}\alpha^2/4+o(1)\).  Complete bipartite shields attain this
envelope and are old one-from-each towers; odd-cycle blow-ups are genuine
non-bipartite shields but sit strictly below it.  Primary target: leave
two-uniform endpoint mass and prove either a terminal-core residual
decay/cross-fiber exclusion theorem below the envelope, or construct and audit
a higher-uniformity interval-shielded endpoint support, starting with dense
cancellative 3-uniform families.  For any candidate, audit every full
pair-link interval plus any possible \(R_P(\theta)\) lift.  Include Scout and
Oracle where applicable; treat raw output as advisory until local audit,
explicit wiki patch, refresh, and Editor preflight.  Do not stage, push,
create Gmail drafts, send email, contact authors, run publisher-stage, or use
bipartite endpoint-pair lifts, triangle-free endpoint-pair lifts, odd-cycle
endpoint-pair lifts, interval-shielded endpoint mass alone, direct
weighted-Mantel aggregation, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-P table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, ambient endpoint-moment budgets alone, singleton endpoint
lifts alone, disjoint block/matching endpoint lifts alone, or Erdos #25
residue-tail work as terminal evidence unless STATUS.md/STRATEGY.md explicitly
revives them.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove a weighted
triangle-free endpoint-profile residual theorem for two-uniform shielded
families.  Start from new proposition `mrw-3161f39fd270`, bipartite subtower
corollary `mrw-50bca8113dbf`, triangle-free endpoint-pair proposition
`mrw-1b04240e9886`, shielded-residual corollary `mrw-3d6bb8271a4c`,
cross-pattern factorization `mrw-20ca89f696f2`, fixed-pattern residual
proposition `mrw-1f23857438d4`, endpoint-pattern residual proposition
`mrw-05f82d03b190`, pointwise-incidence corollary `mrw-7f0eb8d1648c`, and
the core weighted union-free nodes `mrw-55a8d9eddd2e`, `mrw-d0402aea6f58`,
and `mrw-b4075311abd3`.

Decide whether every high-mass triangle-free endpoint graph decomposes into
bipartite subtower pieces plus controlled odd-cycle components, or whether
balanced odd-cycle blow-ups force a genuinely new finite odd-cycle
shifted-residual envelope.  If that fails, move to higher-uniformity shielded
families such as dense cancellative 3-uniform endpoint supports and audit every
full pair-link interval plus any possible \(R_P(\theta)\) lift.

Do not stage, push, create Gmail drafts, send email, contact authors, run
publisher-stage, or use bipartite endpoint-pair lifts, triangle-free
endpoint-pair lifts, odd-cycle endpoint-pair lifts, interval-shielded endpoint
mass alone, direct weighted-Mantel aggregation, endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-P table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, ambient endpoint-moment budgets alone,
singleton endpoint lifts alone, disjoint block/matching endpoint lifts alone,
or Erdos #25 residue-tail work as terminal evidence unless STATUS.md/STRATEGY.md
explicitly revives them.

## Continuation Prompt: supersedes above

Use $pudim in `C:/Users/domin/OneDrive/Projects_Codex/pudim/zetalaw-demo`.
Run one full non-staging Pudim loop.  Read `.math-wiki/GOAL.md`,
`.math-wiki/STATUS.md`, `.math-wiki/STRATEGY.md`, raw log
response
new proposition `mrw-3161f39fd270`, bipartite subtower corollary
`mrw-50bca8113dbf`, triangle-free endpoint-pair proposition
`mrw-1b04240e9886`, shielded-residual corollary `mrw-3d6bb8271a4c`,
cross-pattern factorization `mrw-20ca89f696f2`, fixed-pattern residual
proposition `mrw-1f23857438d4`, endpoint-pattern residual proposition
`mrw-05f82d03b190`, pointwise-incidence corollary `mrw-7f0eb8d1648c`,
overfull strict residual proposition `mrw-c82229c73d8d`,
ambient-moment counterexample `mrw-d65c4d544e56`, endpoint decoupling
proposition `mrw-d7b3299d3813`, endpoint-moment budget corollary
`mrw-2a765ca2676f`, strict-deletion iteration `mrw-5df7f8135e2c`, and
absorbed-window proposition `mrw-791fae526f01`.

Current durable frontier: odd-cycle blow-ups of \(C_{2h+1}\), especially
\(C_5\), are non-bipartite triangle-free endpoint-pair shields with exact
shifted residual
\[
P_0(B)\left(\sum_iR_iR_{i+1}\right)\mathfrak M_T(L-2)
\]
and balanced diffuse mass \(e^{-\alpha}\alpha^2/(2h+1)\).  They are not
single two-class one-from-each subtowers on the same endpoint coordinates,
though their edge sets split into adjacent complete-bipartite blocks.
Primary target: prove a weighted triangle-free endpoint-profile residual
theorem, either decomposing high-mass triangle-free endpoint graphs into
bipartite subtower pieces plus controlled odd-cycle components or isolating a
clean finite odd-cycle residual envelope.  If that fails, move to
higher-uniformity shielded families such as dense cancellative 3-uniform
endpoint supports and audit every full pair-link interval plus any possible
\(R_P(\theta)\) lift.  Include Scout and Oracle where applicable; treat raw
output as advisory until local audit, explicit wiki patch, refresh, and Editor
preflight.  Do not stage, push, create Gmail drafts, send email, contact
authors, run publisher-stage, or use bipartite endpoint-pair lifts,
triangle-free endpoint-pair lifts, odd-cycle endpoint-pair lifts,
interval-shielded endpoint mass alone, direct weighted-Mantel aggregation,
endpoint-degree/rectangle supersaturation, rank-layer templates, trace-local
or finite-junta trace mass, fixed-depth bounded deletion, ordinary shifting,
full-core-cylinder approximation, global boundary-smallness, fixed-P table
extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, ambient
endpoint-moment budgets alone, singleton endpoint lifts alone, disjoint
block/matching endpoint lifts alone, or Erdos #25 residue-tail work as terminal
evidence unless STATUS.md/STRATEGY.md explicitly revives them.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: aggregate the pairwise
relative-parity filter from `mrw-10ea41c73237` over coherent robust components
to force accumulated near-purity defect, or construct/test a two-class
signature-potential assembly satisfying the filter directly.

Start from raw log
new proposition `mrw-10ea41c73237`, previous signed-potential proposition
`mrw-a082a34f6797`, previous parity proposition `mrw-750fb7a7e30c`,
overlap-packing proposition `mrw-206678825c7a`, near-complete
ancestor-signature proposition `mrw-36595780824f`, endpoint-patched near-full
proposition `mrw-8a0c228a0166`, exact ancestor-signature proposition
`mrw-49eaa53e7ffe`, coherent-normal-form proposition `mrw-827094b15843`,
corridor-refinement proposition `mrw-a9efecc818c7`, signature-fragmentation
proposition `mrw-816fd32c3294`, nested coherence proposition
`mrw-fced7420b905`, fixed blow-up proposition `mrw-c7c76faed872`,
complete-bipartite stress test `mrw-f83b56a1aa89`, path-shadow bottleneck
`mrw-c6d0c6fa4d30`, path-shadow proposition `mrw-2bcc2955fe38`, weighted
Mantel proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, Scout
Scout response
`theory/forage/responses/20260521T064701Z-erdos536-relative-parity-overlap-filter-response.md`,
and Oracle response

Current durable frontier: once two near-complete corridors have one robust
relative side-overlap parity, all side overlaps of the opposite relative
parity are bounded by the near-purity defects; in the complete case, positive
shared support can occur in at most one relative parity.  Primary target:
aggregate this pairwise relative-parity filter over coherent robust
components to force defect accumulation, or construct and audit a two-class
assembly satisfying the filter against every full pair-link interval plus any
possible \(R_P(\theta)\) lift.

Do not stage, push, create Gmail drafts, send email, contact authors, run
publisher-stage, or use direct weighted-Mantel aggregation, path-shadow
disjointness alone, projection-only sparsity, endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-P table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, or Erdos #25 residue-tail work as
terminal evidence unless STATUS.md/STRATEGY.md explicitly revives them.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove that positive
high-support pair-link-free mass forces a robust odd-parity side-overlap
component, or use `mrw-a082a34f6797` to test the two-class coherent
signature-potential assembly directly.

Start from raw log
new proposition `mrw-a082a34f6797`, previous parity proposition
`mrw-750fb7a7e30c`, overlap-packing proposition `mrw-206678825c7a`,
near-complete ancestor-signature proposition `mrw-36595780824f`,
endpoint-patched near-full proposition `mrw-8a0c228a0166`, exact
ancestor-signature proposition `mrw-49eaa53e7ffe`, coherent-normal-form
proposition `mrw-827094b15843`, corridor-refinement proposition
`mrw-a9efecc818c7`, signature-fragmentation proposition
`mrw-816fd32c3294`, nested coherence proposition `mrw-fced7420b905`, fixed
blow-up proposition `mrw-c7c76faed872`, complete-bipartite stress test
`mrw-f83b56a1aa89`, path-shadow bottleneck `mrw-c6d0c6fa4d30`, path-shadow
proposition `mrw-2bcc2955fe38`, weighted Mantel proposition
`mrw-a32a6d3a5f20`, two-extension slice proposition `mrw-354b105d4977`,
pair-link criterion `mrw-3c39ca3d1973`, weighted union-free problem
`mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, union-free
reformulation `mrw-b4075311abd3`, Scout request
`theory/forage/requests/20260521T060700Z-erdos536-parity-consistent-signature-tree-request.md`,
Scout response scaffold
`theory/forage/responses/20260521T060700Z-erdos536-parity-consistent-signature-tree-response.md`,
and Oracle response

Current durable frontier: parity-consistent robust side-overlap components
have coherent signature potentials; in the complete case they are genuine
two-class pure-support signature-potential assemblies.  Primary target:
derive a global robust odd-parity side-overlap component from positive
high-support mass, or construct and audit the two-class coherent assembly
against every full pair-link interval plus any possible \(R_P(\theta)\) lift.

Do not stage, push, create Gmail drafts, send email, contact authors, run
publisher-stage, or use direct weighted-Mantel aggregation, path-shadow
disjointness alone, projection-only sparsity, endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-P table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, or Erdos #25 residue-tail work as
terminal evidence unless STATUS.md/STRATEGY.md explicitly revives them.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: leave two-uniform
endpoint mass and prove either a terminal-core residual decay/cross-fiber
exclusion theorem below the fractional bipartite envelope, or construct and
audit a higher-uniformity interval-shielded endpoint support, starting with
dense cancellative 3-uniform families.

Start from new corollary `mrw-d602b51accb8`, odd-cycle proposition
`mrw-3161f39fd270`, bipartite subtower corollary `mrw-50bca8113dbf`,
triangle-free endpoint-pair proposition `mrw-1b04240e9886`, shielded-residual
corollary `mrw-3d6bb8271a4c`, cross-pattern factorization
`mrw-20ca89f696f2`, fixed-pattern residual proposition `mrw-1f23857438d4`,
endpoint-pattern residual proposition `mrw-05f82d03b190`, pointwise-incidence
corollary `mrw-7f0eb8d1648c`, and core weighted union-free nodes
`mrw-55a8d9eddd2e`, `mrw-d0402aea6f58`, and `mrw-b4075311abd3`.

Do not stage, push, create Gmail drafts, send email, contact authors, run
publisher-stage, or use bipartite endpoint-pair lifts, triangle-free
endpoint-pair lifts, odd-cycle endpoint-pair lifts, interval-shielded endpoint
mass alone, direct weighted-Mantel aggregation, endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-P table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, ambient endpoint-moment budgets alone,
singleton endpoint lifts alone, disjoint block/matching endpoint lifts alone,
or Erdos #25 residue-tail work as terminal evidence unless STATUS.md/STRATEGY.md
explicitly revives them.

## Continuation Prompt: supersedes above

Use $pudim in `C:/Users/domin/OneDrive/Projects_Codex/pudim/zetalaw-demo`.
Run one full non-staging Pudim loop.  Read `.math-wiki/GOAL.md`,
`.math-wiki/STATUS.md`, `.math-wiki/STRATEGY.md`, raw log
Scout raw log
response
new corollary `mrw-d602b51accb8`, odd-cycle proposition `mrw-3161f39fd270`,
bipartite subtower corollary `mrw-50bca8113dbf`, triangle-free endpoint-pair
proposition `mrw-1b04240e9886`, shielded-residual corollary
`mrw-3d6bb8271a4c`, cross-pattern factorization `mrw-20ca89f696f2`,
fixed-pattern residual proposition `mrw-1f23857438d4`, endpoint-pattern
residual proposition `mrw-05f82d03b190`, pointwise-incidence corollary
`mrw-7f0eb8d1648c`, overfull strict residual proposition `mrw-c82229c73d8d`,
ambient-moment counterexample `mrw-d65c4d544e56`, endpoint decoupling
proposition `mrw-d7b3299d3813`, endpoint-moment budget corollary
`mrw-2a765ca2676f`, strict-deletion iteration `mrw-5df7f8135e2c`, and
absorbed-window proposition `mrw-791fae526f01`.

Current durable frontier: every two-uniform triangle-free endpoint-pair shield
is bounded by the fractional bipartite envelope
\[
\mathcal R_G(L)\le \frac{P_0(B)R_B^2}{4}\mathfrak M_T(L-2),
\]
and under diffuse endpoint weights has endpoint mass at most
\(e^{-\alpha}\alpha^2/4+o(1)\).  Complete bipartite shields attain this
envelope and are old one-from-each towers; odd-cycle blow-ups are genuine
non-bipartite shields but sit strictly below it.  Primary target: leave
two-uniform endpoint mass and prove either a terminal-core residual
decay/cross-fiber exclusion theorem below the envelope, or construct and audit
a higher-uniformity interval-shielded endpoint support, starting with dense
cancellative 3-uniform families.  For any candidate, audit every full
pair-link interval plus any possible \(R_P(\theta)\) lift.  Include Scout and
Oracle where applicable; treat raw output as advisory until local audit,
explicit wiki patch, refresh, and Editor preflight.  Do not stage, push,
create Gmail drafts, send email, contact authors, run publisher-stage, or use
bipartite endpoint-pair lifts, triangle-free endpoint-pair lifts, odd-cycle
endpoint-pair lifts, interval-shielded endpoint mass alone, direct
weighted-Mantel aggregation, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-P table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, ambient endpoint-moment budgets alone, singleton endpoint
lifts alone, disjoint block/matching endpoint lifts alone, or Erdos #25
residue-tail work as terminal evidence unless STATUS.md/STRATEGY.md explicitly
revives them.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove that positive
high-support pair-link-free mass forces a robust odd-parity side-overlap
component, or use `mrw-a082a34f6797` to test the two-class coherent
signature-potential assembly directly.

Start from raw log
new proposition `mrw-a082a34f6797`, previous parity proposition
`mrw-750fb7a7e30c`, overlap-packing proposition `mrw-206678825c7a`,
near-complete ancestor-signature proposition `mrw-36595780824f`,
endpoint-patched near-full proposition `mrw-8a0c228a0166`, exact
ancestor-signature proposition `mrw-49eaa53e7ffe`, coherent-normal-form
proposition `mrw-827094b15843`, corridor-refinement proposition
`mrw-a9efecc818c7`, signature-fragmentation proposition
`mrw-816fd32c3294`, nested coherence proposition `mrw-fced7420b905`, fixed
blow-up proposition `mrw-c7c76faed872`, complete-bipartite stress test
`mrw-f83b56a1aa89`, path-shadow bottleneck `mrw-c6d0c6fa4d30`, path-shadow
proposition `mrw-2bcc2955fe38`, weighted Mantel proposition
`mrw-a32a6d3a5f20`, two-extension slice proposition `mrw-354b105d4977`,
pair-link criterion `mrw-3c39ca3d1973`, weighted union-free problem
`mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, union-free
reformulation `mrw-b4075311abd3`, Scout request
`theory/forage/requests/20260521T060700Z-erdos536-parity-consistent-signature-tree-request.md`,
Scout response scaffold
`theory/forage/responses/20260521T060700Z-erdos536-parity-consistent-signature-tree-response.md`,
and Oracle response

Current durable frontier: parity-consistent robust side-overlap components
have coherent signature potentials; in the complete case they are genuine
two-class pure-support signature-potential assemblies.  Primary target:
derive a global robust odd-parity side-overlap component from positive
high-support mass, or construct and audit the two-class coherent assembly
against every full pair-link interval plus any possible \(R_P(\theta)\) lift.

Do not stage, push, create Gmail drafts, send email, contact authors, run
publisher-stage, or use direct weighted-Mantel aggregation, path-shadow
disjointness alone, projection-only sparsity, endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-P table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, or Erdos #25 residue-tail work as
terminal evidence unless STATUS.md/STRATEGY.md explicitly revives them.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove that positive
high-support pair-link-free mass forces a robust odd-parity
corridor-overlap cycle, or construct the parity-consistent signature-tree
assembly and test it directly.

Start from raw log
new proposition `mrw-750fb7a7e30c`, overlap-packing proposition
`mrw-206678825c7a`, near-complete ancestor-signature proposition
`mrw-36595780824f`, endpoint-patched near-full proposition
`mrw-8a0c228a0166`, exact ancestor-signature proposition
`mrw-49eaa53e7ffe`, coherent-normal-form proposition `mrw-827094b15843`,
corridor-refinement proposition `mrw-a9efecc818c7`, signature-fragmentation
proposition `mrw-816fd32c3294`, nested coherence proposition
`mrw-fced7420b905`, fixed blow-up proposition `mrw-c7c76faed872`,
complete-bipartite stress test `mrw-f83b56a1aa89`, path-shadow bottleneck
`mrw-c6d0c6fa4d30`, path-shadow proposition `mrw-2bcc2955fe38`, weighted
Mantel proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, Scout
`theory/forage/responses/20260521T052700Z-erdos536-corridor-family-overlap-defect-response.md`,
and Oracle blocker response

Current durable frontier: robust side-overlap graphs of near-complete
corridors must be parity consistent.  Robust same-side overlaps force equal
selected signatures, robust cross-side overlaps force complementary selected
signatures, and every odd-parity cycle must pay a near-purity defect edge.
Primary target: prove that positive high-support mass generates such an
odd-parity robust cycle, or construct a parity-consistent coherent
signature-tree assembly and test every full pair-link interval plus any
possible \(R_P(\theta)\) lift.

Do not stage, push, create Gmail drafts, send email, contact authors, run
publisher-stage, or use direct weighted-Mantel aggregation, path-shadow
disjointness alone, projection-only sparsity, endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-P table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, or Erdos #25 residue-tail work as
terminal evidence unless STATUS.md/STRATEGY.md explicitly revives them.

## Next Executable Cycle Target: supersedes above

Run one full non-staging Pudim loop.  Primary target: prove that positive
high-support pair-link-free mass forces a robust odd-parity side-overlap
component, or use `mrw-a082a34f6797` to test the two-class coherent
signature-potential assembly directly.

Start from raw log
new proposition `mrw-a082a34f6797`, previous parity proposition
`mrw-750fb7a7e30c`, overlap-packing proposition `mrw-206678825c7a`,
near-complete ancestor-signature proposition `mrw-36595780824f`,
endpoint-patched near-full proposition `mrw-8a0c228a0166`, exact
ancestor-signature proposition `mrw-49eaa53e7ffe`, coherent-normal-form
proposition `mrw-827094b15843`, corridor-refinement proposition
`mrw-a9efecc818c7`, signature-fragmentation proposition
`mrw-816fd32c3294`, nested coherence proposition `mrw-fced7420b905`, fixed
blow-up proposition `mrw-c7c76faed872`, complete-bipartite stress test
`mrw-f83b56a1aa89`, path-shadow bottleneck `mrw-c6d0c6fa4d30`, path-shadow
proposition `mrw-2bcc2955fe38`, weighted Mantel proposition
`mrw-a32a6d3a5f20`, two-extension slice proposition `mrw-354b105d4977`,
pair-link criterion `mrw-3c39ca3d1973`, weighted union-free problem
`mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, union-free
reformulation `mrw-b4075311abd3`, Scout request
`theory/forage/requests/20260521T060700Z-erdos536-parity-consistent-signature-tree-request.md`,
Scout response scaffold
`theory/forage/responses/20260521T060700Z-erdos536-parity-consistent-signature-tree-response.md`,
and Oracle response

Current durable frontier: parity-consistent robust side-overlap components
have coherent signature potentials; in the complete case they are genuine
two-class pure-support signature-potential assemblies.  Primary target:
derive a global robust odd-parity side-overlap component from positive
high-support mass, or construct and audit the two-class coherent assembly
against every full pair-link interval plus any possible \(R_P(\theta)\) lift.

Do not stage, push, create Gmail drafts, send email, contact authors, run
publisher-stage, or use direct weighted-Mantel aggregation, path-shadow
disjointness alone, projection-only sparsity, endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-P table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, or Erdos #25 residue-tail work as
terminal evidence unless STATUS.md/STRATEGY.md explicitly revives them.
