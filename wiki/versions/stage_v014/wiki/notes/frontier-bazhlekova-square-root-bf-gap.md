# Frontier: Bazhlekova Square-Root Bernstein Gap

Primary source: Emilia Bazhlekova and Ivan Bazhlekov, "Subordination approach to multi-term time-fractional diffusion-wave equations", arXiv:1707.09828.

The source proves the propagation-function positivity package under
\[
1<\alpha\le2,\qquad \alpha-\alpha_m\le1,
\]
by showing that
\[
\sqrt{g(s)}\in CBF,\qquad g(s)=c s^\alpha+\sum_j c_j s^{\alpha_j}.
\]
It leaves open whether, and to what extent, this gap condition can be relaxed for the actual properties
\[
w\ge0,\qquad w_t\ge0,\qquad -w_x\ge0.
\]

## Local Result

For the two-term wave endpoint
\[
g(s)=c s^2+d s^b,\qquad c,d>0,\quad 0<b<1,
\]
the condition cannot be relaxed. Put \(h(s)=\sqrt{g(s)}\). Then
\[
h''(s)=\frac{d}{2\sqrt c}(b-1)(b-2)s^{b-3}+O(s^{2b-5})>0
\]
for all sufficiently large \(s\).

The source gives
\[
\mathcal L\{w_t(x,\cdot)\}(s)=e^{-xh(s)}.
\]
If \(w_t(x,\cdot)\ge0\), this Laplace transform must be completely monotone. But
\[
\frac{d^2}{ds^2}e^{-xh(s)}
=e^{-xh(s)}\left(x^2h'(s)^2-xh''(s)\right),
\]
which is negative at a large \(s_0\) after choosing \(x>0\) sufficiently small. Hence \(w_t\) fails positivity for some \(x\).

## Status

This is a sharp no-relaxation slice at \(\alpha=2\), not a full solution of the global relaxation problem. The broader two-term case \(g(s)=c s^a+d s^b\), \(1<a<2\), \(a-b>1\), remains open locally.

Do not stage this as an application without a later explicit staging request and an application-policy audit. It is theory growth in the complete-monotonicity/Bernstein-function layer.

## Two-Term Concavity-Loss Criterion

A later bounded Student pass classified the exact region where the second-derivative obstruction fires for two-term symbols. Let
\[
g(s)=c s^a+d s^b,\qquad c,d>0,\quad 1<a<2,\quad 0<b<a-1,
\]
and set \(h(s)=\sqrt{g(s)}\), \(y=(c/d)s^{a-b}\). Then the sign of \(h''\) is the sign of
\[
N_{a,b}(y)
=a(a-2)y^2
+2(a^2-ab-a+b^2-b)y
+b(b-2).
\]
The discriminant is
\[
4(a-b)^2\left((a-1)^2+(b-1)^2-1\right).
\]
Since \(a>1\) and \(b<1\), \(h''\) is positive somewhere exactly when
\[
(a-1)^2+(b-1)^2>1.
\]
In that region, \(e^{-x\sqrt g}\) fails complete monotonicity for a suitable small \(x>0\), so \(w_t\) cannot be nonnegative for all \(x,t>0\). The source examples \((a,b)=(1.9,0.5)\) and \((1.8,0.3)\) lie in this outside-disk region.

The remaining two-term inner gap
\[
1<a<2,\qquad 0<b<a-1,\qquad (a-1)^2+(b-1)^2\le1
\]
is still open locally. There the square-root symbol is concave by this test, but no Bernstein-function representation or positivity theorem has been admitted.

Scope guard from the live Oracle audit: the outside-disk condition is not a global criterion for arbitrary \(a,b\); it is the exact criterion only in the source-relevant straddling/gap regime \(1<a\le2\), \(0<b<a-1\). If both exponents are above \(1\), use the full quadratic criterion instead of the disk shortcut.

The full two-term concavity criterion is now recorded as `T-sqrt-two-term-symbol-exact-concavity-criterion` and the Wiki note `wiki/notes/two-term-square-root-concavity-criterion.md`. In particular, the inner gap has been demoted as a second-derivative route: the remaining problem there is no longer concavity but Bernstein status or an inverse-Laplace sign mechanism beyond concavity.

## Inner-Gap Fifth-Derivative Counterexample

A later bounded Student pass found an exact higher-derivative obstruction inside the inner disk. Let
\[
g(s)=s^{28/25}+s^{1/50},\qquad h(s)=\sqrt{g(s)}.
\]
Then
\[
1<a<2,\qquad 0<b<a-1,\qquad a-b=\frac{11}{10}>1,
\]
and
\[
(a-1)^2+(b-1)^2
=\left(\frac3{25}\right)^2+\left(-\frac{49}{50}\right)^2
=\frac{2437}{2500}<1.
\]
Thus this is not covered by the positive-\(h''\) outside-disk obstruction.

Direct differentiation gives
\[
h^{(5)}(1)
=-\frac{5570045943\sqrt2}{320000000000}<0.
\]
Since a Bernstein function has completely monotone derivative, it must satisfy \(h^{(5)}\ge0\). Therefore \(\sqrt{s^{28/25}+s^{1/50}}\) is not a Bernstein function.

The same example gives propagation failure, not only failure of the sufficient CBF route. With
\[
F_x(s)=e^{-xh(s)}=\mathcal L\{w_t(x,\cdot)\}(s),
\]
we have
\[
F_x^{(5)}(1)=-x h^{(5)}(1)+O(x^2)>0
\]
for all sufficiently small \(x>0\). This contradicts complete monotonicity of \(F_x\), which would be necessary if \(w_t(x,\cdot)\ge0\). Hence \(w_t\)-positivity fails for this inner-gap two-term symbol.

This is still a partial source answer, not a complete classification of the inner disk. The remaining open problem is now a residual parameter-region classification for Bernstein status and propagation positivity.

## Advisor Rotation: Universal Two-Term Gap Program

After the Baskakov \(\alpha=1,r=8\) refutation, Advisor returned to this source-backed frontier as a low-hanging theory-growth target rather than forcing the unripe Erdős route. Scout forage for open-ended growth was attempted, but the Oracle forage helper correctly suppressed the live browser launch under the hard sticky blocklist; this branch was selected by local source-first fallback.

Attack Plan `AP-20260601T013500-bazhlekova-two-term-gap-universal` targets the two-term gap frontier
\[
g(s)=c s^a+d s^b,\qquad c,d>0,\quad 1<a\le2,\quad 0<b<a,\quad a-b>1.
\]

The plan asks whether the existing outside-disk obstruction and the exact inner-gap fifth-derivative example can be unified into a no-relaxation theorem:
\[
e^{-x\sqrt{g(s)}}\notin CM(0,\infty)
\]
for some \(x>0\) throughout the two-term gap. The preferred route is an odd-derivative obstruction for
\[
h(s)=\sqrt{c s^a+d s^b}
\]
in the residual inner disk
\[
1<a<2,\qquad 0<b<a-1,\qquad (a-1)^2+(b-1)^2\le1.
\]
The diagnostic route is a finite resultant audit of \(h^{(5)}\), \(h^{(7)}\), and \(h^{(9)}\) after the scaling \(y=(c/d)s^{a-b}\). This is designed to either cover the residual cells with certified derivative signs or return exact semialgebraic cells for the next Advisor pass.

## Student Outcome: Odd-Derivative Normal Form

Student execution of `AP-20260601T013500-bazhlekova-two-term-gap-universal` used a compliant Oracle gate, `ORACLE-OS-20260601T014500-bazhlekova-two-term-gap-universal`, and locally replayed the exact rational diagnostics.

For
\[
h(s)=\sqrt{c s^a+d s^b},\qquad
\Delta=a-b,\qquad B=\frac b2,\qquad y=\frac cd s^\Delta,
\]
one has
\[
h^{(n)}(s)=\sqrt d\,s^{B-n}(1+y)^{1/2-n}Q_n(y),
\]
where
\[
Q_0=1,
\]
and
\[
Q_{n+1}
=(B-n)(1+y)Q_n
+
\Delta y\left((1+y)Q_n'+\left(\frac12-n\right)Q_n\right).
\]
Thus each fixed exponent pair \((a,b)\) has a weight-uniform derivative sign test on \(y>0\).

The pass promoted the odd-derivative criterion: if \(Q_{2q+1}(y_0)<0\), then \(e^{-x\sqrt g}\) fails complete monotonicity for all sufficiently small \(x>0\), hence \(w_t\)-positivity fails using the source Laplace-transform identity.

Exact residual seeds:
\[
Q_5^{28/25,\,1/50}(1)<0,\qquad
Q_7^{107/100,\,1/100}\left(\frac32\right)<0,\qquad
Q_9^{53/50,\,1/100}\left(\frac74\right)<0.
\]
The seventh and ninth derivative seeds show that higher odd derivatives add genuine coverage beyond the original fifth-derivative example.

However, the universal two-term failure theorem remains open. At
\[
(a,b)=\left(\frac32,\frac25\right)
\]
and also at
\[
(a,b)=\left(\frac{11}{10},\frac1{20}\right),
\]
exact Sturm counts show that \(Q_5,Q_7,Q_9\) have no positive roots and are positive on \(y>0\). Therefore the finite fifth/seventh/ninth diagnostic cannot close the residual inner gap. The next Advisor pass should target either higher-order asymptotics for \(Q_{2q+1}\) or a possible Bernstein-function island near these no-cover seeds.

## Advisor Rotation: High-Order Versus Island Split

Attack Plan `AP-20260601T020500-bazhlekova-inner-gap-next-split` turns the finite \(5,7,9\) no-cover result into exactly three next candidates:
\[
T\text{-Bazhlekova-inner-gap-Wright-negativity-asymptotic},
\quad
T\text{-Bazhlekova-seed-3half-2fifths-all-order-odd-test},
\quad
T\text{-Bazhlekova-no-cover-neighborhood-BF-island-diagnostic}.
\]

The first route is global: prove a high-order scaling for the odd derivative polynomials \(Q_{2q+1}\) and show a Wright-type limiting function is negative somewhere for every residual inner-gap pair. If true, this implies the universal odd-derivative obstruction.

The second route is a controlled rational test case: decide the all-order sign behavior of \(Q_{2q+1}^{3/2,2/5}\) on \(y>0\). This seed is already known to evade \(Q_5,Q_7,Q_9\), so it is a useful stress test for any claimed high-order mechanism.

The third route is the alternative: if odd derivatives fail near the no-cover seeds, test whether the neighborhood contains a genuine Bernstein-function or complete-monotonicity island, or whether an inverse-Laplace sign obstruction rules out such an island.

## Student Outcome: High-Order Split

Student execution of `AP-20260601T020500-bazhlekova-inner-gap-next-split` used the mandatory Oracle gate `ORACLE-OS-20260601T021500-bazhlekova-inner-gap-next-split` and replayed the finite claims locally.

The Wright route remains open. The formal scaling
\[
h(s)=s^\alpha(1+s^{-p})^{1/2},\qquad \alpha=\frac a2,\quad p=a-b,
\]
leads to a Wright-type series
\[
W_{\alpha,p}(\lambda)
=
\Gamma(-\alpha)
\sum_{k\ge0}\binom{1/2}{k}\frac{\lambda^k}{\Gamma(kp-\alpha)},
\]
but the pass did not prove the uniform error bound or the global negativity statement needed to promote the route.

The no-cover seeds are more stable than the previous \(5,7,9\) audit showed. Exact coefficient/discriminant checks prove
\[
(-1)^{n-1}Q_n(y)>0
\]
for all \(y>0\) and \(1\le n\le201\) at both
\[
(a,b)=\left(\frac32,\frac25\right),
\qquad
(a,b)=\left(\frac{11}{10},\frac1{20}\right).
\]
This is finite evidence for a Bernstein-function island, not an all-order proof.

Nearby, however, higher odd orders do fire:
\[
Q_{15}^{6/5,\,3/50}(7)<0,
\qquad
Q_{17}^{3/2,\,6/25}(18)<0.
\]
By the existing odd-derivative small-\(x\) criterion, these give uniform \(w_t\)-positivity failure for the corresponding exponent pairs and all \(c,d>0\).

Finally, the complete-Bernstein version of the island is impossible in the residual region \(p=a-b>1\). For
\[
f(z)=z^{b/2}(1+z^p)^{1/2},
\]
points \(z=re^{i\theta}\) with \(p\theta>\pi\) and \(r\) large have limiting argument
\[
\frac a2\theta-\pi<0
\]
for \(\theta\) close to \(\pi\). Thus \(f\) fails the Pick upper-half-plane mapping property. Plain Bernstein status remains open.

## Advisor Rotation: Island Split

Attack Plan `AP-20260601T024500-bazhlekova-island-split` turns the high-order split into three next candidates.

First, it asks for an all-order proof of the coefficient/discriminant pattern behind the finite order-\(201\) certificate at
\[
(a,b)=\left(\frac32,\frac25\right),
\qquad
(a,b)=\left(\frac{11}{10},\frac1{20}\right).
\]
If successful, this would prove the Bernstein derivative signs at the two exact no-cover seeds.

Second, it asks for a certified finite high-order split map on the two line slices \((3/2,b)\) and \((11/10,b)\). The intended output is not a plot: each rational interval cell must carry either an explicit odd-polynomial obstruction \(Q_{2q+1}(y)<0\) or a finite signed-polynomial positivity certificate.

Third, it asks for the remaining local dichotomy near the apparent island. Since complete Bernstein status has been ruled out, the next test is plain Bernstein positivity of \(h(s)=\sqrt{c s^a+d s^b}\) versus an inverse-Laplace or finite-\(x\) complete-monotonicity sign obstruction for \(e^{-x h(s)}\).

## Student Outcome: Island Split

Student execution of `AP-20260601T024500-bazhlekova-island-split` used the mandatory Oracle gate `ORACLE-OS-20260601T025500-bazhlekova-island-split` and replayed the usable claims locally.

The coefficient/discriminant route is refuted as stated. At the no-cover seed
\[
(a,b)=\left(\frac32,\frac25\right),
\]
exact top-band recurrence gives a negative \(y^{4479}\) coefficient in
\[
R_{4482}(y)=(-1)^{4481}Q_{4482}(y).
\]
Thus the finite pattern seen through order \(201\), where only the \(y^{n-1}\) coefficient could be negative, is not an all-order structure. This does not refute plain Bernstein status at the seed; it only kills that specific induction target.

The finite line-split branch produced certified rational cells. Positivity through order \(201\) holds on
\[
a=\frac32,\quad b\in\left[\frac{3999}{10000},\frac{4001}{10000}\right],
\qquad
a=\frac{11}{10},\quad b\in\left[\frac{49}{1000},\frac{51}{1000}\right].
\]
Obstruction cells were certified at
\[
\left(\frac32,\left[\frac{199}{1000},\frac{201}{1000}\right]\right),\quad Q_5(3)<0,
\]
\[
\left(\frac32,\left[\frac{2399}{10000},\frac{2401}{10000}\right]\right),\quad Q_{17}(18)<0,
\]
\[
\left(\frac32,\left[\frac{249999}{1000000},\frac{250001}{1000000}\right]\right),\quad Q_{85}(134)<0,
\]
\[
\left(\frac{11}{10},\left[\frac{199}{10000},\frac{201}{10000}\right]\right),\quad Q_9(2)<0,
\]
and
\[
\left(\frac{11}{10},\left[\frac{2499}{100000},\frac{2501}{100000}\right]\right),\quad Q_{47}(16)<0.
\]

The full line map and the plain Bernstein/inverse-Laplace dichotomy remain open. The next useful target is no longer the simple coefficient pattern, but either a top-cap/Wright positivity problem for the no-cover seeds or a direct inverse-Laplace density analysis.

## Advisor Rotation: Top-Cap, Line Map, and Density

Attack Plan `AP-20260601T032000-bazhlekova-topcap-island-map` converts the route-kill into three bounded next candidates.

First, it replaces the failed single-coefficient induction with a top-cap/Wright dichotomy for the no-cover seeds. The scaling is
\[
y\sim n^{a-b}\lambda,
\]
and the task is to prove a rigorous limiting sign theorem for \(R_n(y)\) in that cap. A negative limit would give high-order odd obstructions; a positive limit would push the seed problem into a bulk or density analysis.

Second, it extends the certified rational line map beyond the current cells. This is deliberately finite and auditable: every new cell must carry either an exact odd-polynomial witness \(Q_{2q+1}(y_0)<0\), or a finite positivity certificate with an explicit order cutoff.

Third, it attacks the remaining plain Bernstein island directly through an inverse-Laplace or Levy-density representation for
\[
h(s)=s^{b/2}(1+s^{a-b})^{1/2},
\]
or through a finite-\(x\) complete-monotonicity obstruction for \(e^{-x h(s)}\). This is the only candidate in the new plan with a direct implication to the current island dichotomy.

## Student Outcome: Top-Cap and Line-Map Extension

Student execution of `AP-20260601T032000-bazhlekova-topcap-island-map` used the mandatory Oracle gate `ORACLE-OS-20260601T033000-bazhlekova-topcap-island-map` and replayed the promoted finite claims locally.

The fixed-depth top cap of the coefficient vector is now understood. For
\[
R_n(y)=(-1)^{n-1}Q_n(y),
\]
and \(p=a-b>1\), every fixed coefficient depth satisfies
\[
\operatorname{sgn}[y^{n-\ell}]R_n(y)=(-1)^\ell
\]
for all sufficiently large \(n\). Thus fixed odd top depths are eventually negative. This explains the \(R_{4482}\) break and shows that the failed coefficient-pattern route cannot be repaired by adding more finite discriminant checks.

The formal Wright top-cap limit
\[
W_{\alpha,p}(\lambda)
=
1-\frac{\Gamma(1-\alpha)}{\alpha}
\sum_{j\ge1}\binom{1/2}{j}
\frac{\lambda^{-j}}{\Gamma(pj-\alpha)}
\]
was numerically positive on the audited grid at both no-cover seeds, but no rigorous sign theorem or transfer theorem was proved. The top-cap/Wright dichotomy remains open.

The certified line map gained four more obstruction cells. On \(a=3/2\):
\[
Q_7(6)<0\quad
b\in\left[\frac{2199}{10000},\frac{2201}{10000}\right],
\]
\[
Q_9(8)<0\quad
b\in\left[\frac{28}{125},\frac{113}{500}\right],
\]
and
\[
Q_{13}(13)<0\quad
b\in\left[\frac{2349}{10000},\frac{2351}{10000}\right].
\]
On \(a=11/10\):
\[
Q_5(1)<0\quad
b\in\left[\frac7{500},\frac2{125}\right].
\]
Each cell gives uniform small-\(x\) complete-monotonicity failure for all \(c,d>0\).

Finally, the plain Bernstein island branch was reduced to complete monotonicity of
\[
h'(s)
=
s^{b/2-1}(1+s^{a-b})^{-1/2}
\left(\frac b2+\frac a2s^{a-b}\right).
\]
No density sign theorem and no finite-\(x\) obstruction was proved.

## Advisor Rotation: Wright Positivity, Threshold Witnesses, and Density

Attack Plan `AP-20260601T034800-bazhlekova-wright-density-thresholds` keeps the program focused on the three remaining proof mechanisms.

First, it asks for a rigorous positivity theorem for the Wright top-cap limit at the no-cover seeds:
\[
W_{\alpha,p}(\lambda)>0\qquad(\lambda>0).
\]
This would not solve the island problem, but it would certify that the top-cap route supports the apparent island rather than producing a high-order obstruction at the seeds.

Second, it turns the raw high-order line witnesses near the predicted top-cap thresholds into exact audit targets. The raw witnesses
\[
Q_{1001}^{3/2,\,63/250}(2876)<0,
\qquad
Q_{1001}^{11/10,\,13/500}(447)<0
\]
remain unpromoted until exact arithmetic verifies them; if they are too expensive or false, the Student route should replace them with lower-order exact witnesses in the same threshold region.

Third, it asks for the actual island decision through the normalized derivative density. The object is
\[
h'(s)
=
s^{b/2-1}(1+s^{a-b})^{-1/2}
\left(\frac b2+\frac a2s^{a-b}\right).
\]
A complete-monotonicity density certificate, or a negative density/finite-derivative witness with rational-neighborhood stability, directly resolves the selected no-cover seed density dichotomy.

## Student Outcome: \(Q_{1001}\) Point Witnesses

Student execution of `AP-20260601T034800-bazhlekova-wright-density-thresholds` launched the mandatory live Student Oracle gate `ORACLE-OS-20260601T005309-bazhlekova-wright-density-thresholds` before local proof work. The local point-witness audit uses no Oracle mathematical claim while that response remains pending.

The raw order-\(1001\) threshold witnesses are now exact point certificates:
\[
Q_{1001}^{3/2,\,63/250}(2876)<0,
\qquad
Q_{1001}^{11/10,\,13/500}(447)<0.
\]
The replay script evaluates the signed-polynomial recurrence over \(\mathbb Q\). Since \(1001\) is odd, \(R_{1001}=Q_{1001}\), so both signs are direct odd-derivative obstructions at the two rational exponent pairs.

The same audit found lower-order exact rational interval replacements:
\[
Q_{151}^{3/2,\,b}(269)<0
\quad
b\in\left[
\frac{2509999}{10000000},
\frac{2510001}{10000000}
\right],
\]
and
\[
Q_{131}^{11/10,\,b}(50)<0
\quad
b\in\left[
\frac{25699}{1000000},
\frac{25701}{1000000}
\right].
\]
Thus `T-Bazhlekova-threshold-line-witnesses-Q1001-audit-or-replacement` is solved in its diagnostic line-map sense. The no-cover seed Wright positivity theorem and the normalized derivative density decision remain open.

## Student Outcome: Wright-Density Bridge

The live Oracle response for `ORACLE-OS-20260601T005309-bazhlekova-wright-density-thresholds` suggested that the top-cap and density branches share the same Wright function. The local audit confirms the bridge.

With
\[
h(s)=s^\alpha(1+s^{-p})^{1/2},
\qquad
\beta=\alpha-\frac p2,
\]
define
\[
\mathcal W_{\alpha,p}(x)
=
-\sum_{m=0}^{\infty}
\binom{1/2}{m}\frac{x^m}{\Gamma(pm-\alpha)}.
\]
Then
\[
\mathcal L^{-1}\{h'\}(t)
=t^{-\alpha}\mathcal W_{\alpha,p}(t^p).
\]
The previous top-cap normalization satisfies
\[
W^{\mathrm{top}}_{\alpha,p}(\lambda)
=
\frac{\Gamma(1-\alpha)}{\alpha}
\mathcal W_{\alpha,p}(\lambda^{-1}),
\]
so the sign of the top-cap limit is the sign of the same density function. Thus the no-cover seed density problem and the all-\(\lambda\) top-cap positivity problem are not separate mechanisms; both reduce to proving positivity, or finding a negative value, for
\[
\mathcal W_{3/4,11/10}(x)
\quad\text{and}\quad
\mathcal W_{11/20,21/20}(x)
\qquad(x>0).
\]
No positivity theorem is promoted yet.

## Advisor Rotation: Unified Wright Sign Problem

Attack Plan `AP-20260601T042500-bazhlekova-unified-wright-sign` uses the bridge theorem to collapse the next work into one sign problem:
\[
\mathcal W_{3/4,11/10}(x)>0,
\qquad
\mathcal W_{11/20,21/20}(x)>0
\qquad(x>0).
\]
It creates exactly three candidates. The first is a direct endpoint-plus-compact interval certificate for both functions. The second is a structural positivity route through a positive kernel, fractional differential equation, Mellin-Barnes contour deformation, or total-positivity mechanism. The third is diagnostic: a certified negative search either refutes positivity with a rational negative interval, giving a finite-\(x\) obstruction by the density bridge, or returns the exact compact gaps that remain.

No Scout first-contact is required because these are internal continuations of the admitted Bazhlekova frontier and Wright-density bridge.

## Student Outcome: Small-\(x\) Wright Endpoint

Student execution of `AP-20260601T042500-bazhlekova-unified-wright-sign` began with the mandatory live Oracle gate `ORACLE-OS-20260601T012716-bazhlekova-unified-wright-sign`. While the Oracle response was pending, the local audit proved the small-\(x\) endpoint piece of the positivity envelope.

For both no-cover seed functions,
\[
\mathcal W_{\alpha,p}(x)>0
\qquad
0\le x\le1.
\]
The proof uses the alternating coefficient sign pattern
\[
\mathcal W_{\alpha,p}(x)=\sum_{m=0}^\infty(-1)^m A_mx^m,
\qquad A_m>0,
\]
and shows that, at \(r=17/20\), the positive \(m=0\) term dominates all negative odd terms. A sign-separated interval bound then covers \([17/20,1]\). The lower margins are approximately \(0.01134\) on the first piece and at least \(0.0587\) on the bridge piece.

The same sign-separated interval method adaptively covers \([1,10]\). Thus the current certified compact result is
\[
\mathcal W_{3/4,11/10}(x)>0,
\qquad
\mathcal W_{11/20,21/20}(x)>0
\qquad
0\le x\le10.
\]
The second seed requires far more subdivision because the sign-separated lower bound is conservative for larger \(x\), but the replay closes the interval.

The high-precision point search found numerical minima near \(x=1.19114\) and \(x=3.37531\), both positive. The remaining gap is the interval \(x>10\), especially a certified large-\(x\) endpoint argument.

## Advisor Rotation: Post-\(10\) Wright Tail

Student triage after the \([0,10]\) proof showed that brute sign-separated
subdivision becomes inefficient just past \(10\), especially for
\(\mathcal W_{11/20,21/20}\). Advisor therefore created
`AP-20260601T021500-bazhlekova-post-ten-wright-tail` rather than jumping to an
Erdős-class problem.

The three new candidates are:
\[
T\text{-Bazhlekova-Wright-Watson-tail-closes-post-ten-gap},
\quad
T\text{-Bazhlekova-Wright-finite-window-tail-bridge},
\quad
T\text{-Bazhlekova-Wright-branch-audited-kernel-positive}.
\]
They ask for, respectively, an explicit Watson/Wright remainder starting at or
near \(10\), a faster certified finite-window bridge to an asymptotic threshold,
and a correctly branch-audited positive-kernel representation. All three remain
internal continuations of the admitted Wright-density bridge and the true
\([0,10]\) compact block.

## Student Outcome: Post-\(10\) Derivative Bridge

Student execution of `AP-20260601T021500-bazhlekova-post-ten-wright-tail` ran
the mandatory live Oracle gate
`ORACLE-OS-20260601T021600-bazhlekova-post-ten-wright-tail`. Oracle recommended
the route
\[
[0,10]\ \text{compact positivity}
\quad+\quad
[10,20]\ \text{finite bridge}
\quad+\quad
[20,\infty)\ \text{Watson remainder}.
\]
The finite bridge is now locally certified. For both seed functions,
\[
\mathcal W_{\alpha,p}'(x)>0
\qquad
10\le x\le20.
\]
The replay script covers \([10,20]\) by centered Taylor models for
\(\mathcal W_{\alpha,p}'\) on the five intervals centered at
\[
11,\ 13,\ 15,\ 17,\ 19
\]
with radius \(1\). It subtracts explicit bounds for the centered Taylor tail
and for omitted defining-series coefficients. The limiting seed is
\((11/20,21/20)\), where the minimum certified derivative lower bound is
\[
0.00299977163172\ldots.
\]
Combining this derivative bridge with the previous \([0,10]\) theorem gives
\[
\mathcal W_{3/4,11/10}(x)>0,
\qquad
\mathcal W_{11/20,21/20}(x)>0
\qquad
0\le x\le20.
\]
The remaining gap is \(x>20\), for which the next certificate should be a
Watson/Wright explicit remainder.

## Student Outcome: Watson Tail and Source Closure

The \(x\ge20\) tail is now certified. With
\[
\beta=\alpha-\frac p2,
\]
Student uses the three-term Watson polynomial
\[
P_3(x)
=
A_0x^{1/2}+A_1x^{-1/2}+A_2x^{-3/2},
\qquad
A_k=
\binom{1/2}{k}\frac{\beta+kp}{\Gamma(1-\beta-kp)}.
\]
The replay splits the branch-audited contour remainder into an algebraic
negative-axis remainder and the two root-cut contributions from
\[
x^{1/p}e^{\pm i\pi/p}.
\]
At \(x=20\), after subtracting all certified remainders, the margins are
\[
0.732374180856\ldots
\]
for \((\alpha,p)=(3/4,11/10)\), and
\[
0.100568095684\ldots
\]
for \((\alpha,p)=(11/20,21/20)\). The hard seed is still safely positive.

Combining the previous \([0,20]\) certificate with the new Watson tail gives
\[
\mathcal W_{3/4,11/10}(x)>0,
\qquad
\mathcal W_{11/20,21/20}(x)>0
\qquad
x>0.
\]
Therefore the finite-window-to-tail candidate is true with \(X=20\), and the
no-cover Wright top-cap positivity source is true by the admitted bridge edge.

The method-specific direct Watson-from-\(10\) node remains open as stated, and
the positive-kernel node remains open. The naive one-cut Hankel kernel is not a
valid positive-kernel proof because it misses the root cuts and its
negative-axis jump changes sign.
