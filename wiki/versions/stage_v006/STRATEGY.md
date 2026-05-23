# Strategy: Math Research Program

## Active Thesis

- Latest 20260523T191151Z: Scout item `20260523T190315Z-scout-forage` was
  audited.  Candidate 1 was duplicate-reviewed because the Open Problem 3
  endpoint obstruction \(\beta<-1\) is already proved in `mrw-0e9002ec3122`;
  Candidate 2 reinforced the active exceptional \(n=2\) Open Problem 4 route.
  Advisor then promoted `mrw-c3e50abdd2fe`, proving
  \[
  \left[\frac{257}{110},3\right]\subseteq\mathcal I_2.
  \]
  Portfolio effect: the only unsolved Open Problem 4 case has a narrower
  certified gap,
  \[
  \frac{4629}{2000}<L_2\le\frac{257}{110}.
  \]
  Next target: one more feasible rational tail-gate improvement below
  \(257/110\), or pivot to the derivative-sign equation on
  \([1409/5000,293/1000]\) if denominator growth makes the tail route stale.
- Latest 20260523T185221Z: Scout item `20260523T184322Z-scout-forage` was
  audited.  Candidate 1 was duplicate-reviewed against the already promoted
  \(C^1\) Gamma-numerator threshold and self-entropy threshold nodes; no Scout
  claim was promoted.  Candidate 3 reinforced the active exceptional \(n=2\)
  Open Problem 4 route.  Advisor then promoted `mrw-da05add5bca1`, proving
  \[
  \left[\frac{187}{80},3\right]\subseteq\mathcal I_2.
  \]
  Portfolio effect: the only unsolved Open Problem 4 case has a narrower
  certified gap,
  \[
  \frac{4629}{2000}<L_2\le\frac{187}{80}.
  \]
  The new proof introduces a reusable Bernoulli / Euler--Maclaurin lower gate
  for \(Z_3(1/x)\).  Next target: push the tail gate toward its numerical
  threshold just above \(7/3\), or switch to derivative-sign certification on
  \([1409/5000,293/1000]\) from `mrw-a3170d192f6c`.
- Latest 20260523T183816Z: Scout inbox was clear, so Advisor consolidated the
  Open Problem 4 route.  New corollary `mrw-e497f41bfc07` records that
  \[
  \mathcal I_n=\mathbb R\quad(n\ge1\text{ odd}),
  \qquad
  \mathcal I_n=[n,n+1]\quad(n\ge4\text{ even}).
  \]
  Portfolio effect: the source-grounded beta-window application is now fully
  classified outside \(n=2\), so future Advisor cycles should not re-open odd
  orders or even \(n\ge4\) unless a proof audit finds an error.  The remaining
  open case is exactly the exceptional \(n=2\) lower endpoint, with certified
  gap
  \[
  \frac{4629}{2000}<L_2\le\frac{19}{8}.
  \]
  Next target: sharpen the sufficient edge below \(19/8\), or certify
  derivative signs in the bracket from `mrw-a3170d192f6c`.
- Latest 20260523T182438Z: Scout item `20260523T181642Z-scout-forage` was
  audited.  Candidate 1 was accepted after local proof audit and promoted as
  `mrw-fd6576e56da0`; Candidates 2--5 remain deferred.  The new theorem gives
  the exact beta window for every even order outside the exceptional \(n=2\)
  case:
  \[
  \mathcal I_n=[n,n+1]\qquad(n\ge4,\ n\text{ even}).
  \]
  Portfolio effect: Qi--Lim--Nantomah Open Problem 4 is now solved for all
  odd orders and for all even \(n\ge4\).  The remaining open case in this
  branch is \(n=2\), where the certified gap is
  \[
  \frac{4629}{2000}<L_2\le\frac{19}{8}.
  \]
  Next target after Scout clearance: exact \(n=2\) lower-envelope work from
  `mrw-a3170d192f6c` and `mrw-19400778b4b5`, unless a new Scout item has
  higher application yield.
- Latest 20260523T181253Z: Scout inbox was clear, so Advisor continued the
  \(n=2\) Qi--Lim--Nantomah beta-window route.  New theorem
  `mrw-19400778b4b5` sharpens the explicit admissible interval to
  \[
  \left[\frac{19}{8},3\right]\subseteq\mathcal I_2.
  \]
  The proof improves the reciprocal-tail gate to
  \[
  Z_3(1/x)>x^{19/8}
  \qquad(0<x<1)
  \]
  by using three explicit terms, a tail integral, and an exact Sturm
  certificate.  Portfolio effect: this is a global upper-bound improvement
  for the \(n=2\) lower scalar envelope and narrows the certified gap to
  \[
  \frac{4629}{2000}<L_2\le\frac{19}{8}.
  \]
  Next target: either sharpen the sufficient edge below \(19/8\) with tighter
  ratio/tail bounds, or return to the critical-point equation
  `mrw-a3170d192f6c` for derivative-sign certification near the localized
  maximizer.
- Latest 20260523T175811Z: Scout item `20260523T174843Z-scout-forage` was
  audited.  Candidate 1 was accepted after local proof audit and promoted as
  `mrw-5fabc550bd7d`; Candidates 2--5 remain deferred.  The new theorem gives
  the first explicit nontrivial sufficient interval for the \(n=2\)
  Qi--Lim--Nantomah beta window:
  \[
  \left[\frac52,3\right]\subseteq\mathcal I_2.
  \]
  The proof reduces the inequality to
  \[
  Z_3(1/x)>x^\beta
  \]
  for \(5/2\le\beta\le3\), using the convex trapezoid lower bound for
  \(0<x<1\) and the first Hurwitz-zeta term for \(x\ge1\).  Portfolio effect:
  application yield is now high for the \(n=2\) source problem, but this is a
  partial admissible range, not the largest range.  The certified gap is
  \[
  \frac{4629}{2000}<L_2\le\frac52.
  \]
  Next target: exact lower endpoint work from `mrw-a3170d192f6c`, either by
  derivative-sign certification on \([1409/5000,293/1000]\) or by a global
  outside-bracket upper bound for \(Q_2\).
- Latest 20260523T174346Z: Scout inbox was clear, so the Advisor cycle
  continued the \(n=2\) lower-envelope route.  New corollary
  `mrw-a3170d192f6c` proves that the localized compact maximum supplies an
  interior critical point.  With
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
  there exists
  \[
  \xi\in(1409/5000,293/1000)
  \]
  such that \(Q_2(\xi)>4629/2000\) and
  \[
  \xi\log \xi\,\Lambda(\xi)=\log R(\xi).
  \]
  Portfolio effect: this converts the refined bracket into the exact
  derivative equation that the next interval-certificate pass must sign-test.
  It does not prove uniqueness or a global upper bound.  Next target:
  certify signs of \(x\log x\,\Lambda(x)-\log R(x)\) on rational subintervals
  of \([1409/5000,293/1000]\), or prove a global outside-bracket upper bound
  for \(Q_2\).
- Latest 20260523T173540Z: Scout item `20260523T172341Z-scout-forage` was
  audited.  Candidate 1 was a duplicate of the already-promoted admissible
  polynomial Gamma threshold (`mrw-e0db175f66fc`, with the \(C^1\) wrapper
  `mrw-6cd7f677ca40`), so no Scout claim was promoted.  Candidate 3 reinforced
  the \(n=2\) even-order beta-window route as the best current
  source-grounded application ladder.  New corollary `mrw-3712cf1c88d8`
  narrows the compact localization:
  \[
  Q_2(1409/5000)<\frac{4629}{2000}<Q_2(23/80),
  \qquad
  Q_2(293/1000)<\frac{4629}{2000}<Q_2(23/80).
  \]
  Portfolio effect: no new Gamma-only work; the \(Q_2\) maximum is now
  localized to \([1409/5000,293/1000]\) at the same rational level.  Next
  target: derivative-sign certification on subintervals of this bracket, or a
  global outside-bracket upper bound for \(Q_2\).
- Latest 20260523T171753Z: Scout inbox was clear, so Advisor continued the
  \(n=2\) lower-envelope route.  New corollary `mrw-8c1324a498bf` proves a
  sharper compact maximum bracket:
  \[
  Q_2(7/25)<\frac{4629}{2000}<Q_2(23/80),
  \qquad
  Q_2(3/10)<\frac{4629}{2000}<Q_2(23/80).
  \]
  Hence \(Q_2\) has an interior maximizer on \([7/25,3/10]\) with value above
  \(4629/2000\), and every admissible \(n=2\) beta satisfies
  \(\beta>4629/2000\).  Portfolio effect: this narrows the previous
  \([1/4,1/3]\) bracket and raises the rational lower obstruction without
  claiming the global endpoint.  Next target: prove derivative signs or
  interval monotonicity on subintervals of \([7/25,3/10]\), or prove
  \(Q_2(x)\le\) a certified rational ceiling outside this bracket.
- Latest 20260523T170813Z: Scout item `20260523T165716Z-scout-forage` was
  audited.  Candidate 1 was accepted in corrected form and promoted as
  `mrw-6cd7f677ca40`, the pointwise variational threshold for positive
  \(C^1\) Gamma numerators.  For
  \[
  R_u(s)=\psi^{-1}\!\big(u'(s)/u(s)-\psi(s)\big)-s,\qquad
  \rho_u=\sup_{s\ge1}R_u(s),
  \]
  the quotient \(u(s)/(\Gamma(s+\rho)\Gamma(s))\) is nonincreasing on
  \([1,\infty)\) exactly when \(\rho_u<\infty\) and \(\rho\ge\rho_u\).
  Strict endpoint monotonicity requires the contact set
  \(\{R_u=\rho_u\}\) to contain no nontrivial interval; this is the correction
  to the raw Scout strictness claim.  Portfolio effect: useful
  source-grounded Gamma consolidation with moderate application yield, but it
  should not displace the active \(n=2\) polygamma lower-envelope branch.
  Candidates 2--5 remain deferred.  Next target after Scout clearance:
  return to `mrw-2a62d2bc84ad` and narrow the \([1/4,1/3]\) bracket or prove
  a global outside-bracket upper bound for \(Q_2\).
- Latest 20260523T164935Z: Scout inbox was clear, so Advisor continued the
  \(n=2\) lower-envelope route.  New corollary `mrw-2a62d2bc84ad` proves a
  coarse compact maximum bracket:
  \[
  Q_2(1/4)<\frac{1157}{500}<Q_2(2/7),
  \qquad
  Q_2(1/3)<\frac{1157}{500}<Q_2(2/7).
  \]
  Hence \(Q_2\) has an interior maximizer on \([1/4,1/3]\) with value above
  \(1157/500\), and every admissible \(n=2\) beta satisfies
  \(\beta>1157/500\).  Portfolio effect: this converts the previous point
  certificate into a genuine compact maximizer bracket, but it still leaves
  uniqueness and global upper bounding open.  Next target: prove derivative
  signs or interval monotonicity on subintervals of \([1/4,1/3]\), or prove
  \(Q_2(x)\le\) a certified rational ceiling outside the bracket.
- Latest 20260523T164412Z: a late Scout item
  `20260523T163715Z-scout-forage` appeared during final checks and was audited
  before ending the heartbeat.  Candidate 1 was accepted and promoted as
  `mrw-82ac3282a187`, the self-entropy Gamma-product threshold:
  \[
  \frac{e^{-cs}s^s}{\Gamma(s+\rho)\Gamma(s)}
  \text{ strictly decreases on }[1,\infty)
  \Longleftrightarrow
  \psi(1+\rho)\ge\gamma+1-c.
  \]
  Portfolio effect: this is low-cost source-grounded Gamma theory-growth and
  closes the source's \(s^s\) and \((s/e)^s\) threshold examples, but it should
  not displace the active \(n=2\) polygamma lower-envelope route unless that
  route stalls.  Candidates 2--5 remain deferred.
- Latest 20260523T163811Z: Scout inbox was clear, so Advisor continued the
  \(n=2\) lower-envelope branch.  New corollary `mrw-30f9a055fa9a` proves a
  certified rational point obstruction at \(x=2/7\):
  \[
  Q_2(2/7)>\frac{231}{100}.
  \]
  Therefore every admissible \(n=2\) beta satisfies \(\beta>231/100\), while
  `mrw-201bbda2c917` still gives admissibility of \(\beta=3\).  Portfolio
  effect: this does not solve the global lower envelope, but it moves the
  lower-bound certificate from a special-value dyadic proof to a reusable
  rational interval-arithmetic template near the suspected maximum.  Next
  useful work is to turn this point certificate into a certified local
  maximum bracket or a global upper bound for \(Q_2\) on \(0<x<1\); avoid
  further isolated samples unless they sharpen the interval method.
- Latest 20260523T162751Z: Scout item `20260523T161710Z-scout-forage`
  returned after the earlier scaffold audit and was re-audited.  Candidate 1
  was accepted with a local proof replacement and promoted as
  `mrw-201bbda2c917`.  For every even \(n\ge2\),
  \[
  x^{n+1}C_n(x)-P_n(x)<0\qquad(x>0),
  \]
  so the right endpoint \(\beta=n+1\) is admissible.  The even-order
  beta-window now reduces exactly to
  \[
  \mathcal I_n
  =
  \left\{\beta:
  \beta>Q_n(x)\text{ for every }0<x<1
  \right\}
  \cap(-\infty,n+1].
  \]
  Portfolio effect: the \(x>1\) upper-envelope side of Qi--Lim--Nantomah Open
  Problem 4 is closed uniformly for even orders.  Candidate 1 therefore has
  high application-yield and route-ripeness impact.  Candidates 2--5 remain
  deferred.  Next useful work is the lower scalar envelope \(L_n=\sup_{0<x<1}Q_n(x)\),
  especially \(L_2\); do not spend more cycles on upper-endpoint sampling.
- Latest 20260523T161748Z: Advisor audited Scout item
  `20260523T161710Z-scout-forage` and marked it blocked/no-op because it was
  only a request-created scaffold with no returned candidates, nutrients,
  solution, or patch.  Scout did not change opportunity cost, route ripeness,
  growth-forage priority, or application yield.  The proof cycle then promoted
  `mrw-f27a36284da5`, a proved dyadic obstruction at \(x=1/2\) for the
  \(n=2\) polygamma beta window:
  \[
  \beta>
  \lambda_{2,1/2}
  =
  \frac{
  \log\!\left(
  \frac{56\zeta(3)(\zeta(3)-1)}{\pi^4-28\zeta(3)}
  \right)}
  {\log(1/2)}
  \approx2.2286936706.
  \]
  Together with the prior upper endpoint, any admissible \(n=2\) parameter
  must satisfy \(\lambda_{2,1/2}<\beta\le3\).  Portfolio effect: this is a
  certified lower-envelope obstruction, so it is useful theory-growth, but it
  still does not solve the scalar envelope.  Next useful work is to certify the
  global lower/upper envelope of \(Q_2\), not to collect unaudited point
  samples unless they come with an analytic certificate.
- Latest 20260523T160802Z: Advisor audited Scout item
  `20260523T155709Z-scout-forage` after its response arrived.  Candidate 1
  was accepted only as endpoint-barrier material.  The general even-order
  endpoint pressure was already covered by `mrw-0241ab931d33`; new corollary
  `mrw-8a146667d25b` proves the \(n=2\) left endpoint is excluded:
  \[
  \frac{x^2C_2(x)}{P_2(x)}\to2>1\qquad(x\to0^+),
  \]
  so \(\beta=2\) fails and any admissible \(n=2\) parameter satisfies
  \[
  2<\beta\le3.
  \]
  Portfolio effect: this sharpens the first even-order target without
  overclaiming the full scalar envelope.  Do not claim that all
  \(\beta\in(2,3]\) work; the next useful \(n=2\) target is still the global
  scalar-envelope certification.  Scout Candidates 2--5 remain deferred.
  This remains polygamma theory-growth, not public staging and not Erdos #536
  terminal evidence.
- Latest 20260523T155807Z: Scout inbox was clear at cycle start, so Advisor continued the
  higher-polygamma beta-window branch.  New proposition `mrw-0241ab931d33`
  proves the even-order scalar-envelope reduction.  For even \(n\ge2\),
  \[
  C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x)>0,\qquad
  P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x)>0,
  \]
  and the admissible \(\beta\)-set is exactly
  \[
  \beta>Q_n(x)\ (0<x<1),\qquad
  \beta<Q_n(x)\ (x>1),
  \quad
  Q_n(x)=\frac{\log(P_n(x)/C_n(x))}{\log x}.
  \]
  Endpoint pressure gives
  \[
  \lim_{x\to0^+}Q_n(x)=n,\qquad
  \lim_{x\to\infty}Q_n(x)=n+1,
  \]
  hence \(n\le\beta\le n+1\) is necessary.  Portfolio effect: this converts
  Scout's even-order candidate into a precise envelope target rather than a
  floating numerical problem.  Do not claim the even-order range; next useful
  work is scalar-envelope certification, with \(n=2\) as the first target, or
  return to the reciprocal-digamma \(n=0\) scalar envelope.  A late Scout item
  `20260523T155709Z-scout-forage` was only a request-created scaffold and has
  been marked blocked/no-op; it does not change opportunity cost, route
  ripeness, growth-forage priority, or application yield.  This remains
  polygamma theory-growth, not public staging and not Erdos #536 terminal
  evidence.
- Latest 20260523T154852Z: Advisor re-audited Scout item
  `20260523T153713Z-scout-forage` after its response arrived and accepted
  Candidate 1 with a local proof replacement.  New theorem
  `mrw-f3c6cef2ebb1` proves the odd-order collapse for the
  Qi--Lim--Nantomah higher-polygamma beta-window problem.  For
  \[
  C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x),
  \qquad
  P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x),
  \]
  the local Hurwitz-zeta tail-sum inequality proves
  \[
  (-1)^nC_n(x)>0.
  \]
  Hence for every odd \(n\ge1\),
  \[
  x^\beta C_n(x)-P_n(x)<0
  \qquad(x>0,\ \beta\in\mathbb R),
  \]
  so the admissible range is all of \(\mathbb R\).  Portfolio effect:
  this has higher immediate application yield than another beta-zero
  scalar-envelope pass, because it closes an infinite parity subfamily of a
  source-stated problem.  Do not conflate it with the \(n=0\)
  reciprocal-digamma window or the even-order beta-window envelopes; those
  remain open scalar problems.  This remains polygamma theory-growth, not
  public staging and not Erdos #536 terminal evidence.
- Latest 20260523T153832Z: Advisor audited Scout item
  `20260523T153713Z-scout-forage` and marked it blocked/no-op because it was
  only a request-created scaffold with no returned candidates.  The proof
  cycle therefore continued the already audited reciprocal-digamma branch and
  promoted `mrw-ef08eba06fbe`.  With
  \[
  A(x)=\psi(x)+x\psi'(x),\qquad B(x)=\psi(x)\psi(1/x),
  \]
  \(A\) has a unique zero \(\eta_A\), \(\psi\) has a unique positive zero
  \(z_\psi\), and \(a_\psi=1/z_\psi\) satisfies
  \[
  0<\eta_A<\frac12<a_\psi<1<z_\psi<2.
  \]
  Thus the prior pointwise beta reduction now has concrete intervals:
  lower constraints only on \((0,\eta_A)\cup(1,z_\psi)\), upper constraints
  only on \((a_\psi,1)\), and no constraints on
  \((\eta_A,a_\psi)\cup(z_\psi,\infty)\).  Portfolio effect: the exact
  \(\beta_0\)-range problem is now reduced to scalar-envelope certification.
  Do not claim \([-1,\beta_+)\) yet; next legitimate targets are proving the
  lower envelope equals \(-1\) if true, and certifying the global minimum of
  \(Q(x)=\log(B(x)/A(x))/\log x\) on \((a_\psi,1)\).  This remains
  polygamma theory-growth, not public staging and not Erdos #536 terminal
  evidence.
- Latest 20260523T153044Z: Scout inbox was empty, so Advisor audited deferred
  Scout Candidate 3 and promoted `mrw-0e9002ec3122`, a proved pointwise
  reduction for the Qi--Lim--Nantomah reciprocal-digamma \(\beta_0\)-window.
  For
  \[
  A(x)=\psi(x)+x\psi'(x),\qquad
  B(x)=\psi(x)\psi(1/x),
  \qquad
  F_\beta(x)=x^\beta A(x)-B(x),
  \]
  the admissible \(\beta\)-set is the intersection of lower and upper
  half-lines determined by
  \[
  Q(x)=\frac{\log(B(x)/A(x))}{\log x}
  \]
  on same-sign regions, and \(\beta<-1\) is impossible.  Portfolio effect:
  Candidate 3 has moved from unstructured numerical range-hunting to a clean
  scalar-envelope target.  Do not claim the full
  \([-1,\beta_+)\) range from the raw critical value
  \(5.972836863845014\); the next legitimate branch target is the analytic
  sign partition and the global minimum certificate for \(Q\).  This remains
  source-grounded polygamma theory-growth, not public staging and not Erdos
  #536 terminal evidence.
- Latest 20260523T151830Z: Advisor audited Scout item
  `20260523T151043Z-scout-forage` and accepted Candidate 1.  New theorem
  `mrw-e0db175f66fc` proves the exact variational threshold for every
  admissible polynomial Gamma numerator \(u\), meaning \(u(s)>0\) on
  \([1,\infty)\):
  \[
  \rho_u=\max_{s\ge1}
  \left(\psi^{-1}\!\left(\frac{u'(s)}{u(s)}-\psi(s)\right)-s\right),
  \]
  and
  \[
  \frac{u(s)}{\Gamma(s+\rho)\Gamma(s)}
  \text{ decreases strictly on }[1,\infty)
  \Longleftrightarrow
  \rho\ge\rho_u.
  \]
  Portfolio effect: Scout materially changed opportunity cost and growth
  priority.  Instead of further special-family Gamma asymptotics, the program
  now has a class-level theorem; `mrw-37311e7a5a0f` is a specialization, and
  `mrw-c165b8d5e4e2`/`mrw-2b0fbc6dc6db` are estimation tools for one family.
  Deferred Scout candidates are the Gamma-log ratio interval, exponent-tilted
  reciprocal-digamma positivity, weaker higher-polygamma convexity, and a hard
  Erdos #536 biased union-free target.  Do not use this Gamma consolidation as
  Erdos #536 terminal evidence.
- Latest 20260523T150549Z: Advisor heartbeat promoted
  `mrw-2b0fbc6dc6db`, sharpening the polynomial Gamma threshold result to
  \[
  \log\rho_m=m-\log m+\gamma-1+o(1).
  \]
  This closes the first-order asymptotic target named after
  `mrw-c165b8d5e4e2`.  The proof is structural and does not require uniqueness
  of the maximizer.  Portfolio effect: the Gamma polynomial branch has now
  moved from exact variational formula to localization, scale, and first-order
  asymptotic.  It should be parked unless the next Gamma cycle has a genuine
  mechanism for maximizer uniqueness or higher-order asymptotics.  Scout inbox
  was empty; no Scout-driven opportunity-cost change occurred.  This remains
  internal theory-growth, not a new staged application and not Erdos #536
  terminal evidence.  Default next move remains Scout/source-import/
  growth-forage unless a fresh ripe-enough certificate justifies Erdos #536.
- Latest 20260523T145745Z: Advisor heartbeat promoted `mrw-c165b8d5e4e2`,
  an internal Gamma-threshold scale theorem.  In the polynomial branch
  attached to Bulboaca--Zayed's \(\rho_m\)-question,
  \[
  \rho_m=\max_{s\ge1}
  \left(\psi^{-1}\!\left(\frac{m s^{m-1}}{s^m+1}-\psi(s)\right)-s\right)
  \]
  now satisfies
  \[
  \log\rho_m=m-\log m+O(1).
  \]
  Portfolio effect: this is useful theory-growth consolidation because it
  converts the branch from raw threshold numerics to the structural scale
  \(e^m/m\).  It is not a new public staged application and not Erdos #536
  terminal evidence.  Scout inbox was empty during the heartbeat; Oracle
  audit was blocked by API quota exhaustion, so no Oracle material was
  imported.  Next strategy remains growth-forage/source-import by default
  unless a fresh ripe-enough certificate is stated for Erdos #536.  If the
  Gamma polynomial branch is reopened, the next worthy targets are uniqueness
  of the maximizer or a sharper asymptotic such as
  \[
  \log\rho_m=m-\log m+\gamma-1+o(1),
  \]
  not a floating numerical table.
- Latest 20260523T133726Z: the program has an internal application-yield
  consolidation, `APP-0009`, independent of the Erdos #536 abstraction tower.
  Bulboaca--Zayed's reciprocal Gamma-product threshold problem is now logged
  through problem node `mrw-1396775c6089`, theorem node `mrw-0fd149ddc79d`,
  and application record `mrw-0cb4eef49436`.  The exact endpoint certificate is
  \[
  \frac{1}{\Gamma(s+\rho)\Gamma(s)}
  \text{ decreases on }[1,\infty)
  \Longleftrightarrow
  \psi(1+\rho)\ge\gamma.
  \]
  Portfolio effect: this is external reality contact and should count as a
  solved application for the internal theory (`THEORY_v006`), but it is not
  public-staged until Publisher is explicitly invoked.  Next strategy after
  this consolidation should prefer growth-forage/source-import unless the
  Advisor issues a fresh ripe-enough certificate for a hard deep route.
- Latest 20260523T130642Z: `mrw-e33925f1a522` resolves the fixed-child split
  left by the cross-terminal dyadic child-loss theorem.  In the fixed-child
  branch, with \(U=B\setminus g\),
  \[
  W_g=\sum_{h\subseteq U}\pi_U(h)Q_U(h)a_hc_h,
  \qquad
  Q_U(h)=\prod_{u\in h}q_u.
  \]
  Therefore, for every \(0<\rho<\tau\le1\), either active outside cores with
  \(Q_U(h)\ge\rho\) have mass
  \[
  \pi_U(E_\rho(g))\ge\tau-\rho,
  \]
  or the fixed child yields a tiny top-difference covering pair
  \[
  \prod_{b\in x\triangle y}q_b<\tau/\mathfrak D_g
  <\alpha\tau/(\lambda\mu).
  \]
  In the prime-biased model, the heavy branch means active common cores with
  bounded squarefree denominator product
  \[
  \prod_{u\in h}u\le\rho^{-1}.
  \]
  Route invariant: the fixed-child obstruction is now reduced to either tiny
  top differences or a denominator-bounded common-core branch.  Next: classify
  bounded common-core mass as separator/product-tower residual structure, or
  show that many bounded-core certificates create chargeable endpoint triples
  and propagate the \(\eta^2\)-scale third-fiber exclusions.  Do not use this
  split alone as terminal evidence.
- Latest 20260523T122641Z: `mrw-7708298f0eb8` aggregates the dyadic
  fixed-child obstruction into the terminal child-loss framework.  For
  distinct terminal parents \(R_1\ne R_2\) and
  \[
  \mathcal T\subseteq I_T(R_1,R_2)\setminus\{R_1,R_2\},
  \]
  either endpoint-weighted terminal child mass loses an \(\alpha\)-factor,
  \[
  M_{\mathcal T}\le(1-\alpha)\nu_T(\mathcal T),
  \]
  or a fixed endpoint child \(g\) has normalized endpoint interval-pileup
  \(D_{\mathcal A,\mathcal C}(g)>\alpha^{-1}\).  The latter triggers
  `mrw-4210f8220daf`: a dyadic inverse-difference band satisfies
  \[
  S_j\ge\frac{\mathfrak D_g}{(J_g+1)2^{j+1}}
  >
  \frac{\lambda\mu}{\alpha(J_g+1)2^{j+1}},
  \]
  and if \(W_g<\tau\), the same fixed child yields a common-core
  tiny-difference covering pair.  Route invariant: the cross-terminal
  \(\eta^2\)-loss aggregation is now proved.  The remaining obstruction is no
  longer missing aggregation; it is fixed-child structure.  Next: classify
  \(W_g\)-heavy common-core concentration or dyadic tiny-difference cover
  concentration as separator/product-tower residual structure, or prove that
  many such certificates force chargeable endpoint triples.  Do not use this
  aggregation theorem alone as terminal evidence.
- Latest 20260523T114641Z: `mrw-4210f8220daf` upgrades the single-section
  inverse-difference identity into a fixed-child spectrum split.  For
  \[
  \mathfrak D_g=\pi_B(\mathcal A)\pi_B(\mathcal C)
  D_{\mathcal A,\mathcal C}(g),
  \]
  either the ratio-weighted common-core mass \(W_g\) is large, or an active
  common-core section contains a covering pair with tiny symmetric-difference
  product.  More quantitatively, some dyadic inverse-difference band satisfies
  \[
  S_j\ge\frac{\mathfrak D_g}{(J_g+1)2^{j+1}},
  \]
  and if \(W_g<\tau\), the common-core law gives that band probability greater
  than
  \[
  \frac{\mathfrak D_g}{\tau(J_g+1)2^{j+1}}.
  \]
  If the ordinary common-core cover probability is at most \(c\), the
  extracted cover pair obeys
  \[
  \prod_{b\in x\triangle y}q_b<c\tau/\mathfrak D_g.
  \]
  The ordered-distinct repeated-parent analogue is explicit and only asserts
  extraction on active denominators.  Route invariant: fixed-child pileup now
  has a scale-local dyadic certificate, but this alone is not terminal
  evidence.  Next: aggregate dyadic bands over endpoint children and terminal
  intervals into chargeable endpoint triples with \(\eta^2\) third-fiber
  exclusions, or prove that \(W_g\)-heavy/tiny-difference concentration is
  separator/product-tower residual structure.
- Latest 20260523T110631Z: `mrw-52e62752b165` converts the top-cover section
  branch from `mrw-ce7f13a668ed` into inverse-difference cover energy.  With
  \[
  \Delta_g(x,y)=
  \mathbf 1_{x\cup y=g}\prod_{b\in x\triangle y}q_b^{-1},
  \]
  one has
  \[
  \kappa_g(x,y)=\pi_g(x)\pi_g(y)\Delta_g(x,y)
  \]
  and hence
  \[
  K_g(\mathcal P,\mathcal Q)
  =
  \mathbb E[\Delta_g(X,Y)\mid X\in\mathcal P,\ Y\in\mathcal Q].
  \]
  High top-cover density therefore extracts a concrete covering pair with
  large inverse symmetric-difference weight; if ordinary cover probability is
  at most \(c\), high density \(>L\) forces
  \(\prod_{b\in x\triangle y}q_b<c/L\).  Route invariant: fixed-child high
  pileup is now split into large ratio-weighted common-core mass or
  inverse-difference cover certificates.  Next: aggregate many such
  certificates into chargeable endpoint triples and \(\eta^2\)-scale
  third-fiber losses, or classify common-core/tiny-difference concentration as
  separator/product-tower residual structure.  Do not use the
  inverse-difference witness alone as terminal evidence.
- Latest 20260523T102630Z: `mrw-ce7f13a668ed` refines high normalized
  endpoint interval-pileup into a fixed-child normal form.  For a pileup child
  \(g\), every contributing parent pair shares a common outside core
  \(h\subseteq B\setminus g\) and has inside traces \(x,y\subseteq g\) with
  \(x\cup y=g\).  The density summand factors as
  \[
  \frac{\pi_B(a)\pi_B(c)}{\pi_B(I_B(a,c))}
  =
  \omega_U(h)\kappa_g(x,y),
  \]
  giving
  \[
  \lambda\mu D_{\mathcal A,\mathcal C}(g)
  =
  \sum_h\omega_U(h)\Phi_g(\mathcal A_h,\mathcal C_h).
  \]
  With the ratio-weighted common-core section weight \(W_g\), positive pileup
  satisfies
  \[
  D_{\mathcal A,\mathcal C}(g)
  =
  \frac{W_g}{\lambda\mu}\mathbb E[K_H].
  \]
  Therefore high pileup either has large ratio-weighted common-core weight, or
  localizes to a section with still larger top-cover pileup.  The repeated
  parent branch has the same statement using ordered distinct pairs.  Route
  invariant: the unbounded-pileup obstruction is now split into a
  common-core/separator branch and a top-cover section branch.  Next: classify
  the top-cover section branch using the existing top-union-free,
  cover-probability, and separator nodes, or show that large common-core
  weight is exactly product-tower/separator residual structure.  Do not use
  this fixed-child normal form alone as terminal evidence.
- Latest 20260523T094630Z: `mrw-8d6210a920bc` gives the correct diffuse
  endpoint-shadow alternative.  For endpoint families
  \(\mathcal A,\mathcal C\) of positive product masses, the normalized density
  \[
  D_{\mathcal A,\mathcal C}(g)
  =
  \frac{1}{\pi_B(\mathcal A)\pi_B(\mathcal C)}
  \sum_{\substack{a\in\mathcal A,\ c\in\mathcal C\\ g\in I_B(a,c)}}
  \frac{\pi_B(a)\pi_B(c)}{\pi_B(I_B(a,c))}
  \]
  integrates to one and has exact support
  \(\mathsf I_B(\mathcal A,\mathcal C)\).  Hence bounded pileup
  \(D_{\mathcal A,\mathcal C}\le K\), \(K\ge1\), forces endpoint-shadow mass
  at least \(K^{-1}\), and `mrw-e64516fca3bd` then gives terminal child loss
  by the factor \(1-K^{-1}\).  The repeated-parent branch uses the ordered
  distinct-pair density \(D_{\mathcal A}^{\ne}\) and
  \(\mathsf J_B(\mathcal A)\), with no assertion when
  \(Z_{\mathcal A}=0\).  Route invariant: small endpoint shadows can no
  longer be treated as a diffuse mystery; they are exactly high normalized
  interval-pair pileup.  Next: classify high-pileup endpoint multiplicity as
  interval-shielded product-tower/separator residual structure, or extract
  chargeable endpoint triples and aggregate the \(\eta^2\) third-fiber losses
  from `mrw-0cbd2c0086d7`.  Do not use bounded-pileup charging or pileup
  certification alone as terminal evidence.
- Latest 20260523T090621Z: `mrw-6f8a9d8c0ea7` gives an endpoint-side lower
  bound for the child-shadow mechanism when endpoint multiplicity fibers have
  heavy atoms.  For a finite endpoint product law with \(0<q_b<1\),
  \[
  \pi_B(I_B(a,b))\ge\pi_B(a)\pi_B(b).
  \]
  Therefore two endpoint atoms of masses at least \(\alpha,\beta\) force
  endpoint-shadow mass at least \(\alpha\beta\).  Combined with
  `mrw-e64516fca3bd`, terminal interval children over
  \(\mathcal C\subseteq I_T(R_1,R_2)\setminus\{R_1,R_2\}\), \(R_1\ne R_2\),
  lose an \(\alpha\beta\)-factor:
  \[
  \sum_{R_3\in\mathcal C}\nu_T(R_3)\pi_B(\mathcal E_{R_3})
  \le
  (1-\alpha\beta)\nu_T(\mathcal C).
  \]
  The cross-terminal endpoint atoms may coincide; the repeated-parent
  \(\mathsf J_B\) branch still requires two distinct endpoint atoms.  Route
  invariant: atom-concentrated multiplicity fibers are chargeable, so weak
  child-shadow loss must come from a diffuse/all-atoms-small or shielded
  residual endpoint structure.  Next: prove a diffuse or non-shielded
  endpoint interval-shadow lower bound for large active multiplicity fibers,
  or classify small endpoint-shadow families as interval-shielded
  product-tower/separator residuals.  Do not use this heavy-atom charge alone
  as terminal evidence.
- Latest 20260523T082620Z: `mrw-e64516fca3bd` gives the first quantitative
  child-mass version of the cross-\(R\) exclusion.  If \(R_1\ne R_2\) and
  \[
  \mathcal C\subseteq I_T(R_1,R_2)\setminus\{R_1,R_2\},
  \]
  then
  \[
  \sum_{R_3\in\mathcal C}\nu_T(R_3)\pi_B(\mathcal E_{R_3})
  \le
  \left(1-\pi_B(\mathsf I_B(\mathcal E_{R_1},\mathcal E_{R_2}))\right)
  \nu_T(\mathcal C).
  \]
  If \(\mathcal D\subseteq\{R_0:R_0\subsetneq R\}\), then
  \[
  \sum_{R_0\in\mathcal D}\nu_T(R_0)\pi_B(\mathcal E_{R_0})
  \le
  \left(1-\pi_B(\mathsf J_B(\mathcal E_R))\right)\nu_T(\mathcal D),
  \]
  where \(\mathsf J_B\) uses distinct endpoint parents only.  Route invariant:
  terminal interval child mass is costly exactly to the extent that the
  relevant endpoint interval shadow has endpoint product mass.  Next: prove
  endpoint-shadow lower bounds for large active multiplicity fibers under
  diffuse/non-shielded hypotheses, or classify small endpoint-shadow families
  as interval-shielded product-tower/separator residual structures.  Do not
  use this conditional charge alone as terminal evidence.
- Latest 20260523T074620Z: `mrw-e3fec03bf987` restores the cross-\(R\)
  consistency that pointwise endpoint conditioning loses.  For a pair-link-free
  endpoint-fiber union
  \[
  \mathcal F=
  \bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal U_e\},
  \qquad
  \mathcal E_R=\{e:R\in\mathcal U_e\},
  \]
  any terminal interval relation \(R_3\in I_T(R_1,R_2)\) forbids endpoint
  witnesses \(e_i\in\mathcal E_{R_i}\) with \(e_3\in I_B(e_1,e_2)\) unless
  two endpoint-terminal pairs \((e_i,R_i)\) are equal.  In particular,
  pairwise distinct terminal triples satisfy
  \[
  \mathcal E_{R_3}\cap I_B(\mathcal E_{R_1},\mathcal E_{R_2})=\emptyset,
  \]
  and repeated-parent terminal triples \(R_0\subsetneq R\) exclude
  \[
  \mathcal E_{R_0}
  \cap
  \bigcup_{e_1\ne e_2\in\mathcal E_R}I_B(e_1,e_2).
  \]
  Route invariant: large endpoint multiplicity fibers from
  `mrw-d83f21b84e5c` cannot be arranged independently across terminal
  high-window points.  Next: prove a quantitative terminal-interval
  shadow/mass-loss theorem, classify cross-\(R\) shielded multiplicity as
  product-tower or separator residual structure, or propagate the chargeable
  \(\eta^2\)-scale third-fiber losses from `mrw-0cbd2c0086d7`.  Do not use
  this structural cross-\(R\) exclusion alone as terminal evidence.
- Latest 20260523T070609Z: `mrw-d83f21b84e5c` restores endpoint weights to the
  separator-forest branch-volume budget.  For lifted terminal leaf fibers
  \[
  \mathcal U_e=
  \{R:R\cap C_e=\emptyset,\ R\cap(T\setminus C_e)\in\mathcal V_e\},
  \]
  the active terminal-window mass is
  \[
  M_H=
  \sum_e\pi_B(e)\Gamma_e
  \nu_{T\setminus C_e}(\mathcal V_e\cap H_h(T\setminus C_e))
  =
  \sum_{R\in H_h(T)}\nu_T(R)\pi_B(\mathcal E_R),
  \]
  where \(\mathcal E_R=\{e:R\in\mathcal U_e\}\).  If the lifted family is
  pair-link-free, each \(\mathcal E_R\) is ordinary endpoint pair-link-free.
  Thus \(M_H\ge\eta\tau\), \(\tau>0\), always yields a pointwise endpoint
  residual certificate \(\pi_B(\mathcal E_R)\ge\eta\).  With the existing
  active-overlap hypotheses and \(P_0(B)<\delta\eta\), the same mass also
  forces either a chargeable endpoint triple with \(\gamma\eta^2\)-scale
  common high-window overlap and third-fiber loss, or a distinct nonchargeable
  shielded pair with \((1-\gamma-\delta)\eta^2\)-scale overlap.  Route
  invariant: leaf-volume failure is now localized to large ordinary endpoint
  multiplicity fibers plus cross-\(R\) consistency, or to the known
  chargeable/nonchargeable overlap branches.  Next: classify large endpoint
  multiplicity fibers using cross-\(R\) constraints, or propagate chargeable
  third-fiber losses across separator leaves.  Do not use endpoint-weighted
  branch accounting or the active-overlap routing alone as terminal evidence.
- Latest 20260523T062608Z: `mrw-a20438d5edf8` blocks the naive
  separator-tree contraction.  A finite separator forest satisfies the exact
  branch-volume budget
  \[
  \nu_T\!\left(\bigcup_\ell\mathcal U_\ell\cap H_h(T)\right)
  \le
  \sum_\ell\Gamma_\ell\,
  \nu_{T\setminus C_\ell}(\mathcal V_\ell\cap H_h(T\setminus C_\ell)),
  \]
  where
  \[
  \Gamma_\ell=\prod_{z\in C_\ell}(1-q_z),
  \qquad
  Q_\ell=\sum_{z\in C_\ell}q_z,
  \qquad
  \Gamma_\ell\le e^{-Q_\ell}.
  \]
  A uniform path-intensity lower bound \(Q_\ell\ge L\) therefore yields only
  \[
  e^{-L}
  \sum_\ell
  \nu_{T\setminus C_\ell}(\mathcal V_\ell\cap H_h(T\setminus C_\ell)),
  \]
  so the residual leaf-volume or branch entropy must be controlled.  The
  central-rank separator forest shows this is not cosmetic: union mass can be
  polynomially large while every path has exponentially small coefficient.
  Route invariant: path intensity alone is not a separator-tree theorem.
  Next: prove a leaf-volume/entropy control theorem for separator forests
  arising from pair-link-free endpoint fibers, or force escape into chargeable
  endpoint triples and \(\eta^2\)-scale third-fiber exclusions.  Do not use the
  branch-volume budget or central-rank obstruction as terminal evidence.
- Latest 20260523T054605Z: `mrw-ff32abc524eb` upgrades separator-cost
  bookkeeping to a fixed finite separator-chain filtration.  With
  \[
  Z_i\subseteq T_{i-1},\qquad
  c_i=\prod_{z\in Z_i}(1-q_z),\qquad
  Q_i=\sum_{z\in Z_i}q_z,\qquad
  \Gamma_i=\prod_{j\le i}c_j,
  \]
  the first-hit layers and avoid-all residual satisfy
  \[
  \nu(E_i)=\Gamma_{i-1}(1-c_i)\le\Gamma_{i-1}Q_i,
  \qquad
  \nu(U_r)=\Gamma_r\le\exp\!\left(-\sum_i Q_i\right),
  \]
  and telescope by
  \[
  \sum_i\Gamma_{i-1}(1-c_i)=1-\Gamma_r.
  \]
  Thus accumulated low separator intensity gives small first-hit leakage,
  while large accumulated intensity gives exponential loss in the avoid-all
  product residual.  The final residual factors on \(T_r\) with no support
  cutoff shift because all separator coordinates are absent.  Route invariant:
  this is a fixed-chain product filtration, not a classification of adaptive
  separator trees and not terminal evidence.  Next: prove a separator-tree or
  escape theorem showing that persistent low-intensity separator reductions
  collapse into known product-tower residuals, or else force chargeable
  endpoint triples and \(\eta^2\)-scale third-fiber exclusions.  Do not use
  finite separator telescoping alone as terminal evidence.
- Latest 20260523T050601Z: `mrw-789506d08385` turns terminal separators into a
  lower-light/upper-costly dichotomy.  For separator \(Z\),
  \[
  c(Z)=\prod_{z\in Z}(1-q_z),\qquad Q(Z)=\sum_{z\in Z}q_z.
  \]
  Lower parents hitting \(Z\) have absolute terminal high-window mass at most
  \[
  1-c(Z)\le Q(Z),
  \]
  while upper sets avoiding \(Z\) factor through the smaller core
  \(T\setminus Z\) with coefficient
  \[
  c(Z)\le e^{-Q(Z)}.
  \]
  Hence a separator branch is either lower-light when \(Q(Z)\) is small, or
  upper-costly when \(Q(Z)\) is bounded below.  Mass in the lower endpoint
  branch forces an exponential coefficient loss in the upper residual, scaled
  by the endpoint atom \(\pi_B(f)\).  Route invariant: low-cost separators can
  still pass mass to a smaller-core residual, so the next proof must iterate
  this dichotomy, classify the resulting product-tower residual, or force
  escape into chargeable endpoint triples.  Do not use separator cost
  bookkeeping alone as terminal evidence.
- Latest 20260523T042600Z: `mrw-58fd4a90babe` identifies a residual/product
  obstruction to aggregate cover-cap charging.  In a comparable two-fiber
  branch \(f\subsetneq u\), if a terminal separator \(Z\) satisfies
  \[
  A\cap Z\ne\emptyset\quad(A\in\mathcal A),
  \qquad
  V\cap Z=\emptyset\quad(V\in\mathcal V),
  \]
  then terminal pair-link-freeness of \(\mathcal A\) and \(\mathcal V\) makes
  \[
  \{f\cup A:A\in\mathcal A\}\cup\{u\cup V:V\in\mathcal V\}
  \]
  pair-link-free.  The mixed shadows are strictly separated:
  \[
  \mathcal A\cap\mathsf J_T(\mathcal V)=\emptyset,\qquad
  \mathcal V\cap I_T(A,V)=\emptyset.
  \]
  The upper fiber is exactly a smaller-core residual on \(T\setminus Z\) with
  coefficient
  \[
  \prod_{z\in Z}(1-q_z)
  \]
  and no support cutoff shift.  Route invariant: high-support cover caps do not
  aggregate merely because there are many lower parents; a common separator can
  satisfy all sectionwise top-union-free constraints at once.  Next: prove a
  no-small-separator alternative, charge separator branches through endpoint
  triples and \(\eta^2\)-scale third-fiber exclusions, or classify separator
  residuals as known product-tower structure.  Do not use terminal separators
  or the separator factorization alone as terminal evidence.
- Latest 20260523T034558Z: `mrw-0c0cd605a52a` shows that the tiny-cover branch
  is automatic for high-support lower parents.  With
  \[
  c_t=q_t(2-q_t),\qquad \kappa_m(T)=\prod_{i=1}^m c_{(i)}
  \]
  for the \(m\) largest \(c_t\)'s, every \(U\subseteq T\) with \(|U|\ge m\)
  has
  \[
  \operatorname{cov}^{\ne}_U\le C_U\le\kappa_m(T)\le(3/4)^m.
  \]
  For prime-biased terminal cores this improves to
  \[
  \kappa_m(T)\le 2^m/(m+1)!.
  \]
  Thus, in growing positive high-support windows, a fixed lower parent cannot
  produce a uniform upper-fiber loss from the cover-probability cap alone; the
  possible one-parent loss tends to zero.  The route invariant is now sharper:
  top-union-free cover caps only help if they can be aggregated across many
  lower parents or combined with endpoint interval triples/terminal cross-fiber
  exclusions.  Next: prove an aggregate cover-cap theorem, connect active
  high-window overlap to chargeable \(\eta^2\) third-fiber exclusions, or
  classify the high-support tiny-cover branch as exact residual/product
  structure.  Do not use high-support cover-atom collapse alone as terminal
  evidence.
- Latest 20260523T030557Z: `mrw-7273d9801756` classifies the small-cover
  branch from `mrw-9077aa1c34bc`.  For nonempty \(U\) with \(0<q_u\le1/2\),
  \[
  a_U=\prod_{u\in U}q_u,\qquad
  C_U=\prod_{u\in U}q_u(2-q_u)
  \]
  satisfy
  \[
  a_U\le\operatorname{cov}^{\ne}_U\le C_U\le2^{|U|}a_U,
  \qquad
  \frac23C_U\le\operatorname{cov}^{\ne}_U\le C_U.
  \]
  Therefore small distinct-cover probability is exactly a tiny terminal
  cover-atom/all-present-atom branch, apart from the empty-block boundary.
  Lower parents with non-negligible \(C_U\) or \(a_U\) force a uniform
  upper-fiber cap through the top-union-free theorem; avoiding that cap means
  the active lower parents have large multiplicative surprise
  \(\sum_{u\in U}-\log q_u\) or growing support.  Next: classify
  tiny-cover-atom lower parents in the active prime-biased high-window regime,
  aggregate cover caps over many non-tiny lower parents, or connect the branch
  to the chargeable \(\eta^2\) third-fiber exclusions.  Do not use this atom
  classification or the cover cap alone as terminal evidence.
- Latest 20260523T022551Z: `mrw-9077aa1c34bc` gives the first quantitative
  cap for the sectionwise top-union-free branch.  For a fixed terminal block
  \(U\),
  \[
  \operatorname{cov}^{\ne}_U
  =
  \prod_{u\in U}(2q_u-q_u^2)
  -
  \left(\prod_{u\in U}q_u\right)^2
  \]
  is exactly the product probability that two independent \(U\)-traces cover
  \(U\) by distinct sets.  Every top-union-free section has measure at most
  \[
  \sqrt{1-\operatorname{cov}^{\ne}_U}.
  \]
  Therefore, in the comparable branch \(f\subsetneq u\), any fixed lower
  terminal parent \(U\in\mathcal R_f\) with non-negligible
  \(\operatorname{cov}^{\ne}_U\) forces the same cap on every high-window
  subfamily of the upper fiber \(\mathcal R_u\).  The route invariant is now:
  upper mixed-shadow either pays distinct-cover probability, or the relevant
  lower parents have tiny distinct-cover probability and must be classified as
  residual/product obstructions.  Next: prove a small-cover-probability
  classification for lower terminal parents in the active high-window regime,
  or combine several cover caps across many lower parents.  Do not use this
  cover cap alone as terminal evidence.
- Latest 20260523T014542Z: `mrw-dda277c43571` turns the comparable upper
  mixed-shadow exclusion from `mrw-740b9e5c6cff` into an exact section theorem.
  If \(A\subseteq T\), \(\mathcal V\subseteq2^T\), and
  \[
  \mathcal V_A(D)=\{X\subseteq A:D\cup X\in\mathcal V\},
  \]
  then
  \[
  \mathcal V\cap I_T(A,B)\subseteq\{B\}
  \quad(B\in\mathcal V)
  \]
  is equivalent to every section \(\mathcal V_A(D)\) being top-union-free:
  no distinct \(X,Y\) in the section satisfy \(X\cup Y=A\).  Therefore, for
  comparable endpoints \(f\subsetneq u\), every lower-parent terminal set
  \(A\in\mathcal R_f\) makes each outside-trace section of \(\mathcal R_u\)
  top-union-free on \(A\).  The route invariant is now sharper: the preferred
  upper mixed-shadow scheme is a product-section extremal problem, not just a
  vague terminal shadow exclusion.  Next: prove a prime-biased/high-window
  bound for top-union-free sections, classify high-mass sections as
  dictator-like residual/product obstructions, or combine this with chargeable
  \(\eta^2\) third-fiber exclusions.  Do not use top-union-freeness alone as
  terminal evidence.
- Latest 20260523T010541Z: `mrw-740b9e5c6cff` splits the nonempty endpoint
  escape branch from the star criterion into three explicit terminal shadow
  schemes.  Pairwise distinct endpoint triples force full cross-shadow
  exclusion, repeated parents \((u,u,f)\) with \(f\subsetneq u\) force
  \[
  \mathcal R_f\cap\mathsf J_T(\mathcal R_u)=\emptyset,
  \]
  and repeated child/one parent triples \((f,u,u)\) or \((u,f,u)\) force
  \[
  \mathcal R_u\cap I_T(A,B)\subseteq\{B\}
  \quad(A\in\mathcal R_f,\ B\in\mathcal R_u).
  \]
  The route invariant is now concrete: after empty-bottom star residual
  quarantine, all escape must pay one of these terminal shadow exclusions.
  Next: prove a quantitative charging theorem for the full cross-shadow,
  lower-child shadow, or upper mixed-shadow schemes, or classify high-mass
  avoidance as known residual/product structure.  Do not use the split alone
  as terminal evidence.
- Latest 20260523T002549Z: `mrw-a3c54ddf4ae3` extends the empty-bottom
  quarantine from one \(\emptyset,u\) pair to a star
  \[
  \{\emptyset\}\cup\mathcal U.
  \]
  A star assembly is pair-link-free exactly when each \(\emptyset,u\)
  two-fiber branch satisfies the conditions of `mrw-03f08f291f7c`, and every
  ordered nonconstant endpoint triple
  \[
  (u_1,u_2,u_3)\in\mathcal U^3,\qquad u_3\in I_B(u_1,u_2),
  \]
  has no terminal interval witness with pairwise distinct ambient sets.  Its
  high-support mass is bounded by the residual envelope
  \[
  \pi_B(\emptyset)\mathfrak M_T(L)
  +
  \sum_{u\in\mathcal U}\pi_B(u)\mathfrak M_T(L-|u|).
  \]
  The route invariant is now: empty-bottom zero-gap mass is star-residual
  unless it escapes through ordered nonempty endpoint interval triples.  Next:
  prove an active escape alternative from the star criterion, or charge the
  nonempty endpoint triples via terminal cross-fiber exclusions.  Do not use
  the star residual envelope alone as terminal evidence.
- Latest 20260522T222538Z: `mrw-03f08f291f7c` quarantines the zero-gap
  empty-bottom comparable branch when restricted to endpoint patterns
  \(\emptyset\) and \(u\ne\emptyset\).  The two-fiber assembly
  \[
  \mathcal F=\{R:R\in\mathcal R_0\}\cup\{u\cup R:R\in\mathcal R_u\}
  \]
  is pair-link-free exactly when both terminal fibers are pair-link-free, the
  lower fiber avoids the top-fiber two-point interval shadow
  \[
  \mathcal R_0\cap\mathsf J_T(\mathcal R_u)=\emptyset,
  \]
  and every mixed parent pair has no new top-fiber child:
  \[
  \mathcal R_u\cap I_T(A,B)\subseteq\{B\}
  \quad(A\in\mathcal R_0,\ B\in\mathcal R_u).
  \]
  Hence its high-support mass is bounded by the shifted terminal residual
  window
  \[
  \pi_B(\emptyset)\mathfrak M_T(L)+\pi_B(u)\mathfrak M_T(L-|u|).
  \]
  The route invariant is now: an empty-bottom zero-gap pair is residual once
  isolated to two fibers, while any non-isolated active branch must be charged
  through multi-endpoint interactions, positive-gap pairs, or chargeable
  interval triples.  Next: extend the residual quarantine to many
  empty-bottom comparables sharing \(\emptyset\), or force escape into the
  positive-gap/chargeable branches.  Do not use the two-fiber residual bound
  alone as terminal evidence.
- Latest 20260522T194532Z: `mrw-e75870a3c452` classifies the small-gap cases
  left by `mrw-4a33f7d04fc3`.  For distinct \(e,f\), endpoint membership in
  \[
  I_B(e,f)=\{g:e\triangle f\subseteq g\subseteq e\cup f\}
  \]
  is
  \[
  e\in I_B(e,f)\Longleftrightarrow f\subseteq e,\qquad
  f\in I_B(e,f)\Longleftrightarrow e\subseteq f.
  \]
  Therefore incomparable pairs have \(S(e,f)=I_B(e,f)\) and positive gap.  In
  the comparable case \(f\subsetneq e\),
  \[
  \pi_B(S(e,f))
  =
  \pi_B(I_B(e,f))
  \left(1-\prod_{b\in f}q_b\right),
  \]
  with the symmetric formula for \(e\subsetneq f\).  Hence zero shield gap is
  exactly the empty-bottom comparable obstruction \((\emptyset,u)\) or
  \((u,\emptyset)\), \(u\ne\emptyset\).  Under \(q_b\le1/2\), a nonempty smaller
  endpoint of size \(m\) loses at least a \((1-2^{-m})\)-fraction of interval
  mass.  The route invariant is now: locally shielded nonchargeable overlap is
  either empty-bottom comparable, or has positive interval gap.  Next: classify
  empty-bottom comparable pairs as residual/tower structure, prove lower bounds
  on \(\pi_B(I_B(e,f))\) for positive-gap pairs, or propagate the chargeable
  \(\eta^2\) third-fiber exclusions.  Do not use this classification alone as
  terminal evidence.
- Latest 20260522T190535Z: `mrw-4a33f7d04fc3` filters the locally shielded
  nonchargeable branch by endpoint interval-gap mass.  For
  \[
  S(e,f)=I_B(e,f)\setminus\{e,f\},
  \]
  local shielding
  \[
  \mathcal E\cap I_B(e,f)\subseteq\{e,f\}
  \]
  forces
  \[
  \Lambda\le1-\pi_B(S(e,f)).
  \]
  In the active regime \(M\ge\eta\tau\), hence \(\Lambda\ge\eta\), every
  locally shielded pair must satisfy
  \[
  \pi_B(S(e,f))\le1-\eta.
  \]
  The exact product formula is
  \[
  \pi_B(I_B(e,f))
  =
  \prod_{b\in e\triangle f}q_b
  \prod_{b\notin e\cup f}(1-q_b),
  \]
  with endpoint atoms subtracted from \(I_B(e,f)\) only in the comparable
  cases.  The route invariant is now chargeable overlap or a nonchargeable
  shield whose interval gap is small enough.  Next: prove lower bounds on
  \(\pi_B(S(e,f))\) from active endpoint geometry, or classify the small-gap
  cases as residual/tower-like obstructions.  Do not use this filter alone as
  terminal evidence.
- Latest 20260522T170530Z: `mrw-0cbd2c0086d7` makes the active branch
  quantitative.  Under the trichotomy of `mrw-0845a9abe5b6`, if
  \(M\ge\eta\tau\) and
  \[
  P_0(B)<\delta\eta
  \]
  for \(0<\gamma<1\), \(0<\delta<1-\gamma\), then the empty-atom branch is
  excluded.  The sufficient endpoint-intensity test is
  \[
  Q(B)>\log\frac1{\delta\eta}.
  \]
  The remaining branches now have fixed positive scale: either a chargeable
  endpoint interval triple has common high-window overlap at least
  \(\gamma\eta^2\) and, under product/high-window pair-link-free hypotheses,
  third-fiber loss \(\nu_T(\mathcal R_g)\le1-\gamma\eta^2\); or a distinct
  nonchargeable pair has common high-window overlap at least
  \((1-\gamma-\delta)\eta^2\) with local shield
  \(\mathcal E\cap I_B(e,f)\subseteq\{e,f\}\).  The route invariant is now
  quantified overlap-or-local-shield in the active regime.  Next: classify
  the locally shielded distinct nonchargeable pair relation, or sum/propagate
  chargeable \(\eta^2\)-scale third-fiber exclusions.  Do not use this
  conditional branch lemma as terminal evidence.
- Latest 20260522T145031Z: `mrw-45819fa8022f` converts the two sparse
  branches from the support-density split into direct mass loss.  With
  \[
  \rho=
  \begin{cases}
  M/(\Lambda\tau),&\Lambda>0,\\
  0,&\Lambda=0,
  \end{cases}
  \]
  one has
  \[
  M/\tau\le\Lambda,\qquad M/\tau\le\rho.
  \]
  Hence support-lightness \(\Lambda<\lambda\) or fiber-density sparseness
  \(\rho<r\) gives
  \[
  M<\max\{\lambda,r\}\tau.
  \]
  With the empty-atom estimate from `mrw-4a7cdb250fd4`, an empty branch in
  growing endpoint intensity and
  \[
  Q(B)>\log\frac1{\varepsilon\lambda r}
  \]
  is forced into one of these sparse branches and therefore has the same mass
  loss.  The route invariant is now non-sparse-or-small: any active argument
  needing \(M\ge\eta\tau\) must prove both \(\Lambda,\rho\ge\eta\), or
  quarantine the failure as residual/tower structure.  Do not use this
  envelope alone as terminal evidence.
- Latest 20260522T141021Z: `mrw-2b75fd587224` decomposes the missing
  relative high-window mass lower bound.  With endpoint support
  \(\Lambda=\pi_B(\mathcal E)\) and relative fiber density
  \[
  \rho=M/(\Lambda\tau)
  \]
  when \(\Lambda>0\), one has
  \[
  M/\tau=\Lambda\rho.
  \]
  Thus \(\Lambda\ge\lambda\) and \(\rho\ge r\) imply
  \(M\ge\lambda r\,\tau\).  In growing endpoint-intensity blocks, if the
  empty branch holds and
  \[
  Q(B)>\log\frac1{\varepsilon\lambda r},
  \]
  then necessarily
  \[
  \Lambda<\lambda\quad\text{or}\quad\rho<r.
  \]
  The route invariant is now support-or-density: to remove the empty branch,
  prove endpoint support and relative fiber-density lower bounds, or show that
  failure of either is an exact residual/tower branch.  Do not use the split,
  endpoint support, or fiber density alone as terminal evidence.
- Latest 20260522T133021Z: `mrw-4a7cdb250fd4` quarantines the empty-atom
  branch by endpoint intensity.  In the trichotomy of `mrw-0845a9abe5b6`,
  \[
  M\le P_0(B)\tau/\varepsilon
  \]
  implies
  \[
  M/\tau\le e^{-Q(B)}/\varepsilon.
  \]
  Hence if \(M\ge m\tau\) and
  \[
  Q(B)>\log\frac1{m\varepsilon},
  \]
  the empty-atom branch is impossible and at least one overlap branch
  remains: chargeable energy or distinct nonchargeable shielded overlap.  The
  route invariant is now sharper: prove a positive relative high-window mass
  lower bound in growing endpoint-intensity blocks, or show that failure of
  such a lower bound is exactly a terminal residual/tower branch.  Do not use
  this quarantine alone as terminal evidence; it is only branch elimination
  under \(M/\tau\) and \(Q(B)\) hypotheses.
- Latest 20260522T125020Z: `mrw-0845a9abe5b6` packages the current route as a
  mass-or-chargeable-or-shield trichotomy.  Under total overlap accounting and
  the empty-atom diagonal quarantine \(\Delta\le P_0(B)M\), for any
  \(0\le\gamma<1\) and \(0<\varepsilon<1-\gamma\), either chargeable energy
  has size at least \(\gamma M^2/\tau\), or
  \[
  M\le P_0(B)\tau/\varepsilon,
  \]
  or the distinct nonchargeable branch has energy at least
  \[
  (1-\gamma-\varepsilon)M^2/\tau
  \]
  and yields a pair-level shield
  \[
  \mathcal E\cap I_B(e,f)\subseteq\{e,f\}
  \]
  with common high-window overlap density at least
  \((1-\gamma-\varepsilon)\rho^2\).  The strong third-fiber loss
  \(\nu_T(\mathcal R_g)\le1-\alpha\) is available only after invoking the
  product/high-window lower-shadow hypotheses from `mrw-108414b9dce7`.  The
  route invariant is now explicit: either quarantine empty-atom-scale
  high-window mass as terminal residual/tower structure, or classify/charge
  locally shielded distinct nonchargeable pairs.  Do not use the trichotomy,
  empty-atom branch, or local shield alone as terminal evidence.
- Latest 20260522T121013Z: `mrw-c79041553496` removes the remaining
  \(\Lambda,\rho\) bookkeeping from diagonal quarantine.  In the prime-biased
  endpoint product law with \(0<q_b\le1/2\),
  \[
  \Delta\le P_0(B)M\le e^{-Q(B)}M,
  \]
  where
  \[
  M=\sum_e\pi_B(e)\nu_T(\mathcal R_e\cap H)
  \]
  is the high-window endpoint-fiber mass.  Therefore
  \[
  \Delta/(M^2/\tau)\le P_0(B)\tau/M.
  \]
  Diagonal-heavy energy \(\Delta\ge\delta M^2/\tau\) now forces
  \[
  M\le P_0(B)\tau/\delta\le e^{-Q(B)}/\delta.
  \]
  The route invariant is now mass-or-shield: either the active high-window
  mass \(M\) is empty-atom scale and must be quarantined as a tiny residual, or
  the diagonal branch is negligible and, if chargeable energy is also small,
  the distinct nonchargeable-pair branch is forced.  Do not use this mass
  quarantine alone as terminal evidence.
- Latest 20260522T113013Z: `mrw-a75270c4ad65` specializes diagonal control to
  the prime-biased endpoint product law.  When \(0<q_b\le1/2\),
  \[
  P_0(B)=\prod_b(1-q_b),\qquad Q(B)=\sum_b q_b,
  \]
  every endpoint atom satisfies \(\pi_B(e)\le P_0(B)\le e^{-Q(B)}\).
  Therefore, for endpoint support mass \(\Lambda=\pi_B(\mathcal E)\),
  \[
  \eta\le P_0(B)/\Lambda,\qquad H_2(w)\le P_0(B)/\Lambda,
  \]
  and
  \[
  \Delta/(M^2/\tau)\le P_0(B)/(\Lambda\rho)
  \le e^{-Q(B)}/(\Lambda\rho).
  \]
  Thus diagonal-heavy energy at positive \(\rho\) forces tiny endpoint support
  mass:
  \[
  \Delta\ge\delta M^2/\tau
  \Longrightarrow
  \Lambda\le P_0(B)/(\delta\rho)\le e^{-Q(B)}/(\delta\rho).
  \]
  The route invariant is now support-mass-or-shield: either prove the active
  endpoint support has \(\Lambda\rho\gg P_0(B)\), or quarantine tiny
  \(\Lambda\) as an exact terminal residual/tower branch; otherwise the
  distinct nonchargeable-pair branch is forced.  Do not use the atom bound or
  support-mass estimate alone as terminal evidence.
- Latest 20260522T105008Z: `mrw-724d68db9b8c` controls the diagonal branch by
  endpoint concentration.  With
  \[
  w_e=\lambda_e/\Lambda,\qquad
  a_e=\nu_T(\mathcal R_e\cap H)/\tau,\qquad
  \rho=\sum_e w_ea_e,
  \]
  the exact normalization is
  \[
  \frac{\Delta}{M^2/\tau}
  =
  \frac{\sum_e w_e^2a_e}{\rho^2}.
  \]
  Hence
  \[
  \Delta/(M^2/\tau)\le H_2(w)/\rho^2,
  \qquad
  \Delta/(M^2/\tau)\le\eta/\rho,
  \]
  where \(H_2(w)=\sum_e w_e^2\) and \(\eta=\max_e w_e\).  Thus diagonal-heavy
  energy at positive high-window density forces Herfindahl/max-atom
  concentration:
  \[
  \Delta\ge\delta M^2/\tau
  \Longrightarrow
  H_2(w)\ge\delta\rho^2,\quad \eta\ge\delta\rho.
  \]
  Combining with `mrw-ad1f6f41665a` and `mrw-90be6f9a7f88`, if chargeable
  energy is small and endpoint weights are diffuse at scale \(\rho\), the
  distinct nonchargeable-pair branch must carry positive high-window overlap.
  The route invariant is now concentration-or-shield: either prove endpoint
  diffuseness/concentration quarantine in the prime-coordinate model, or
  classify the locally shielded nonchargeable-pair branch.  Do not use this
  Herfindahl control alone as terminal evidence.
- Latest 20260522T101007Z: `mrw-90be6f9a7f88` splits the avoidance branch
  from `mrw-ad1f6f41665a` into diagonal and distinct nonchargeable overlap:
  \[
  \Omega_{\mathcal U}=\Delta+\Omega_{\mathcal N},
  \qquad
  \Omega_{\mathcal C}+\Delta+\Omega_{\mathcal N}\ge M^2/\tau.
  \]
  If the chargeable energy and diagonal energy are small,
  \[
  \Omega_{\mathcal C}\le\gamma M^2/\tau,
  \qquad
  \Delta\le\delta M^2/\tau,
  \]
  then
  \[
  \Omega_{\mathcal N}\ge(1-\gamma-\delta)M^2/\tau.
  \]
  In the non-vacuous case \(M>0\), \(\gamma+\delta<1\), some distinct
  nonchargeable endpoint pair \((e,f)\) has common terminal high-window overlap
  at least \((1-\gamma-\delta)\rho^2\) and satisfies the local pair shield
  \[
  \mathcal E\cap I_B(e,f)\subseteq\{e,f\}.
  \]
  The route invariant is now a sharper avoidance dichotomy: either control
  diagonal concentration by effective endpoint count/Herfindahl mass, or turn
  many locally shielded nonchargeable pairs into a structural endpoint-support
  theorem or a new chargeable interval triple.  Do not use this accounting
  split alone as terminal evidence.
- Latest 20260522T093007Z: `mrw-ad1f6f41665a` converts common-overlap
  production into a precise energy alternative.  For high-window endpoint
  mass \(M\), endpoint weight \(\Lambda\), and \(\rho=M/(\Lambda\tau)\),
  Cauchy gives
  \[
  \Omega_{\mathcal C}+\Omega_{\mathcal U}\ge M^2/\tau.
  \]
  If the chargeable endpoint-pair energy \(\Omega_{\mathcal C}\) carries a
  \(\gamma\)-share, then some endpoint interval triple gives an
  \(\alpha\ge\gamma\rho^2\) common high-window overlap and
  `mrw-108414b9dce7` charges the third fiber by
  \[
  \nu_T(\mathcal R_g)\le1-\gamma\rho^2.
  \]
  Otherwise the high-window overlap energy concentrates on
  \(\Omega_{\mathcal U}\), which includes diagonal and distinct
  nonchargeable pairs.  The route invariant is now avoidance-branch
  structure: split diagonal energy from distinct nonchargeable energy, then
  classify endpoint supports whose overlap energy is mostly nonchargeable.
  Do not use the energy alternative alone as terminal evidence.
- Latest 20260522T085001Z: `mrw-108414b9dce7` gives the first quantitative
  lower-shadow charging lemma for the escaped-mass branch.  For terminal
  product measure and
  \[
  H_h(T)=\{R:|R|>h\},\qquad \tau_h=\nu_T(H_h(T)),
  \]
  every terminal family \(\mathcal G\) satisfies
  \[
  \nu_T(\mathcal G\cap H_h(T))
  \le
  \nu_T(\downarrow\mathcal G)\tau_h.
  \]
  Hence, if endpoint fibers over \(e_1,e_2\) share an \(\alpha\)-fraction of
  the terminal high window and \(e_3\in I_B(e_1,e_2)\), the whole \(e_3\)-fiber
  has terminal measure at most \(1-\alpha\).  The route invariant is now
  common-overlap production: either prove escaped endpoint mass produces such
  common high-window overlaps, or classify the avoidance mechanism as
  near-disjoint terminal fibers, exact product towers, or another shielded
  endpoint residual branch.  Do not use the charging lemma alone as terminal
  evidence.
- Latest 20260522T081000Z: `mrw-82f19bf75c98` recovers a concrete piece of
  the cross-\(R\) information lost by pointwise endpoint conditioning.  If
  \(e_1,e_2,e_3\) are pairwise distinct and
  \[
  e_3\in I_B(e_1,e_2),
  \]
  then
  \[
  \mathcal R_{e_3}\cap
  \downarrow(\mathcal R_{e_1}\cap\mathcal R_{e_2})
  =
  \varnothing.
  \]
  In particular, two complete high-window terminal fibers over \(e_1,e_2\)
  leave no third fiber over \(e_3\).  The route invariant is now quantitative
  lower-shadow cost: prove that positive escaped endpoint mass creates common
  terminal fibers whose lower closures have large measure, or classify the
  avoidance mechanism as a tower/shielded decomposition.  Do not treat this
  local exclusion alone as terminal evidence.
- Latest 20260522T072953Z: `mrw-21208a768bed` shows the
  empty/singleton/top obstruction is persistent, not a one-off numerical
  accident.  For every \(|B|\ge3\),
  \[
  \mathcal S_B=\{\varnothing,B\}\cup\{\{b\}:b\in B\}
  \]
  is ordinary endpoint pair-link-free for the symmetric-difference interval,
  and has product mass
  \[
  P_0(B)\left(1+\sum_{b\in B}\frac{q_b}{1-q_b}\right)
  +\prod_{b\in B}q_b.
  \]
  This gives explicit boundary lower bounds for \(\mathfrak P_B(a)\) when
  \(a<0\) and \(0\le a<1\).  The route invariant is now boundary peeling:
  endpoint residual work must separate empty/singleton/top pieces before
  claiming a positive-threshold profile, or must use cross-\(R\) terminal
  shadows from `mrw-88acf3940157`.  Do not use this boundary family,
  false Lubell/two-layer envelopes, or pointwise endpoint residual bounds
  alone as terminal evidence.
- Latest 20260522T064952Z: `mrw-cdf34678a1e1` kills the naive
  Lubell/two-layer endpoint residual route.  Ordinary endpoint
  pair-link-freeness does not imply 2-Sperner because the relevant interval is
  the squarefree cosunflower interval
  \[
  I(A,B)=\{C:A\triangle B\subseteq C\subseteq A\cup B\},
  \]
  not the ordinary interval between \(A\cap B\) and \(A\cup B\).  The boundary
  example
  \[
  \{\varnothing,\{1\},\{2\},\{3\},\{1,2,3\}\}
  \]
  at \(q=1/10\), \(a=-1\), is pair-link-free, contains a strict
  three-member inclusion chain, and has mass \(973/1000\), exceeding the
  two largest eligible rank masses \(972/1000\).  The route invariant is now
  more precise: any endpoint residual profile theorem must use the true
  symmetric-difference interval or must first prove an additional
  antichain/2-Sperner decomposition.  Keep the \(\theta=0\) and empty-endpoint
  boundary explicit; do not use false Lubell/two-layer envelopes as endpoint
  residual bounds.
- Latest 20260522T060951Z: `mrw-baa182012831` turns escaped endpoint-fiber
  mass into a terminal-conditioned endpoint residual problem.  For a
  pair-link-free union
  \[
  \mathcal F
  =
  \bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal R_e\}
  \subseteq2^{B\sqcup T},
  \]
  each pointwise endpoint support
  \[
  \mathcal E_R=\{e:R\in\mathcal R_e\}
  \]
  is ordinary endpoint pair-link-free, since any endpoint interval triple over
  the same \(R\) lifts through \(R\in I_T(R,R)\).  Hence
  \[
  \nu_P(\mathcal F\cap\{|S|>L\})
  \le
  \mathbb E_{R\sim\nu_T}\bigl[\mathfrak P_B(L-|R|)\bigr],
  \]
  where \(\mathfrak P_B(a)\) is the endpoint pair-link-free residual above
  support threshold \(a\).  The route invariant is now split: either bound the
  prime-biased endpoint residual profile \(\mathfrak P_B(a)\), or recover the
  cross-\(R\) terminal shadow exclusions discarded by this Fubini
  conditioning.  Do not use the pointwise endpoint residual bound by itself as
  terminal evidence.
- Latest 20260522T052951Z: `mrw-88acf3940157` converts escaped endpoint
  interval structure into explicit terminal exclusions.  If endpoint patterns
  \(e_1,e_2,e_3\) are pairwise distinct and
  \[
  e_3\in I_B(e_1,e_2),
  \]
  then pair-link-freeness forces
  \[
  \mathcal R_{e_3}\cap
  \mathsf I_T(\mathcal R_{e_1},\mathcal R_{e_2})
  =
  \varnothing.
  \]
  If \(f\subsetneq e\), it forces
  \[
  \mathcal R_f\cap\mathsf J_T(\mathcal R_e)=\varnothing.
  \]
  Full terminal shadows are essential; terminal endpoints cannot be removed.
  The route invariant is now quantitative cross-shadow cost: escaped endpoint
  mass can survive only if terminal fibers avoid full interval shadows.  The
  next useful theorem must prove terminal shadow growth/overlap for
  positive high-support fibers, or decompose endpoint supports into complete
  product-tower pieces plus negligible residue after removing costly interval
  triples.
- Latest 20260522T044950Z: `mrw-8e3a53602d1d` closes the complete
  prime-biased product-tower obstruction at positive threshold parameter.  For
  every endpoint part \(X\) with \(0<q_x\le1/2\), the one-hit probability
  \[
  a(X)=\sum_{x\in X}q_x\prod_{u\in X\setminus\{x\}}(1-q_u)
  \]
  satisfies \(a(X)\le1/2\).  Hence a complete multipartite transversal tower
  with \(K\) nonempty endpoint parts has coefficient
  \[
  \Gamma\le2^{-K}.
  \]
  Combining this with degraded-threshold absorption gives the finite
  grow-or-absorb alternative: for \(0\le\theta'<\theta<1\), either
  \[
  K-\theta\mu_B\le(\theta-\theta')\mu_T
  \]
  and the tower is absorbed into
  \[
  \Gamma\mathfrak M_T(\theta'\mu_T),
  \]
  or else
  \[
  \mathcal R(\theta\mu_P)<2^{-(\theta-\theta')\mu_T}.
  \]
  The route invariant is now escaped mass outside exact complete product
  towers.  Future progress should use cross-pattern factorization to force
  nonconstant endpoint interval triples and terminal cross-fiber exclusions, or
  prove that general high-mass interval-shielded endpoint supports decompose
  into complete product-tower pieces plus negligible residue.  Do not use
  complete product towers as terminal evidence, and keep \(\theta=0\)
  separate.
- Latest 20260522T040948Z: `mrw-7f4dbc4882f4` repairs the shifted-window
  branch in the only safe direction: endpoint shifts are absorbed by lowering
  the terminal threshold parameter.  For \(P=B\sqcup T\),
  \(\mu_X=\sum_{x\in X}q_x\), and
  \[
  L=\theta\mu_P,
  \]
  every finite product-tower residual
  \[
  \mathcal R_\otimes(L)=\sum_{s=0}^K\Gamma_s\mathfrak M_T(L-s)
  \]
  satisfies
  \[
  \mathcal R_\otimes(\theta\mu_P)
  \le
  G(1)\mathfrak M_T(\theta_K\mu_T),
  \qquad
  \theta_K\mu_T=\theta\mu_T+\theta\mu_B-K.
  \]
  Hence whenever
  \[
  K-\theta\mu_B\le(\theta-\theta')\mu_T,
  \]
  one has
  \[
  \mathcal R_\otimes(\theta\mu_P)
  \le
  G(1)\mathfrak M_T(\theta'\mu_T).
  \]
  Fixed finite product towers and sublinear endpoint shifts are therefore
  self-similar at any positive \(\theta\): they reduce to the same terminal
  residual theorem at a slightly lower parameter \(\theta'<\theta\).  This is
  not terminal decay and not a same-threshold comparison.  The route invariant
  is now a dichotomy: absorb bounded/sublinear endpoint shifts by degraded
  threshold, and handle growing endpoint shifts either by endpoint coefficient
  decay or by forcing escaped mass into nonconstant endpoint interval triples
  and terminal cross-fiber exclusions.  Keep the \(\theta=0\) boundary
  separate.
- Latest 20260522T032947Z: `mrw-474262d39b1d` kills the universal
  shifted-window comparison route.  For every \(h\ge1\), arbitrary finite
  terminal product cores can have
  \[
  \mathfrak M_T(L-h)/\mathfrak M_T(L)
  \]
  arbitrarily large even when \(\mathfrak M_T(L)>0\).  The explicit example is
  \(T=\{1,\ldots,h\}\), equal coordinate weight \(q\), and
  \(L=h-\tfrac12\): the upper window contains only the full set of mass
  \(q^h\), while the shifted window contains the pair-link-free empty/singleton
  family of mass \((1-q)^h+hq(1-q)^{h-1}\).  Thus endpoint factors and
  pair-link-freeness alone cannot provide shifted-window contraction.  The
  route invariant is now threshold-aware terminal structure: any useful
  shifted-window theorem must use the actual prime-weight/high-support scaling
  or additional core-profile hypotheses, or else progress must come from a
  product-tower alternative that forces nonconstant endpoint interval triples
  outside exact product models.  Do not invoke a universal finite-shift
  comparison without such hypotheses.
- Latest 20260522T024942Z: `mrw-1e5d6b8e8ab1` and `mrw-1c7a59e679e0`
  convert exact product towers into an explicit finite shifted-window problem.
  For endpoint size polynomials
  \[
  G_j(z)=\sum_{e\in\mathcal E_j}\pi_{B_j}(e)z^{|e|},
  \qquad
  \prod_jG_j(z)=\sum_s\Gamma_s z^s,
  \]
  every finite product of interval-shielded endpoint families has exact
  residual
  \[
  \mathcal R_\otimes(L)=\sum_s\Gamma_s\mathfrak M_T(L-s).
  \]
  Hence any terminal shift profile immediately gives a product-tower bound.
  For fixed finite complete multipartite product towers, the diffuse endpoint
  coefficient additionally obeys the Poisson envelope
  \[
  \Gamma_\infty=e^{-A}\prod_P\beta_P
  \le e^{-A}(A/K)^K\le e^{-K}.
  \]
  The route invariant is now precise: endpoint geometry contributes only the
  polynomial coefficients \(\Gamma_s\); the unsolved part is the finite or
  growing shifted-window profile of \(\mathfrak M_T(L-s)\), or else proving
  that mass outside exact product towers creates nonconstant endpoint interval
  triples and cross-fiber exclusions.  Do not treat endpoint-factor envelopes,
  product-polynomial identities, or fixed exact product towers as terminal
  evidence.
- Latest 20260522T020942Z: `mrw-cd7b1fe1d9af` formalizes the exact iterated
  endpoint-tower obstruction.  Finite products of interval-shielded endpoint
  supports remain interval-shielded.  For
  \(B=B_1\sqcup\cdots\sqcup B_r\) and
  \[
  \mathcal E_\otimes
  =
  \{e_1\sqcup\cdots\sqcup e_r:\ e_j\in\mathcal E_j\},
  \]
  the supported residual is
  \[
  \mathcal R_\otimes(L)
  =
  \sum_{(e_1,\ldots,e_r)}
  \left(\prod_j\pi_{B_j}(e_j)\right)
  \mathfrak M_T\!\left(L-\sum_j|e_j|\right).
  \]
  If the levels are \(k_j\)-uniform, this collapses to
  \[
  \left(\prod_j\Gamma_j\right)\mathfrak M_T(L-K),
  \qquad K=\sum_jk_j.
  \]
  Complete multipartite transversal levels give the predicted product of
  diffuse factors
  \[
  e^{-\sum_j\alpha_j}\prod_j\alpha_j^{k_j}/k_j^{k_j}
  \]
  for fixed finite products.  The route invariant is now exact product towers
  versus escaped mass: inside a finite shielded product tower there is no
  cross-fiber exclusion to exploit.  Progress must either prove a
  shifted-window contraction controlling \(\mathfrak M_T(L-K)\), or prove a
  product-tower alternative showing that positive mass outside these exact
  towers forces nonconstant endpoint interval triples and terminal
  cross-fiber exclusions.  Do not use exact finite product towers alone as
  terminal evidence.
- Latest 20260522T012941Z: `mrw-fd7565b99af5` consolidates the
  higher-uniform endpoint-shield branch.  For
  \(B=X_1\sqcup\cdots\sqcup X_k\) and
  \(H\subseteq X_1\times\cdots\times X_k\), the transversal endpoint family
  \[
  \mathcal E(H)
  =
  \{\{x_1,\ldots,x_k\}:(x_1,\ldots,x_k)\in E(H)\}
  \]
  is interval-shielded.  Therefore
  \[
  \mathcal R_H(L)
  =
  \sum_{e\in\mathcal E(H)}\pi_B(e)\mathfrak M_T(L-k).
  \]
  In the complete balanced \(k\)-partite diffuse case the endpoint factor is
  \[
  e^{-\alpha}\alpha^k/k^k.
  \]
  This recovers singleton, complete bipartite, and tripartite shields, and
  shows that fixed-uniformity transversal endpoint mass is always
  self-similar rather than terminal.  The route invariant is now shifted-window
  contraction versus iterated multipartite endpoint towers: either prove a
  comparison controlling
  \(e^{-\alpha}\alpha^k k^{-k}\mathfrak M_T(L-k)\) across \(k\), or formalize
  the exact iterated multipartite tower obstruction and find where terminal
  core decay/cross-fiber exclusions enter.  Do not use any fixed
  \(k\)-partite transversal endpoint lift alone as terminal evidence.
- Latest 20260522T004939Z: `mrw-1e4b87d9862b` shows that the endpoint-shield
  obstruction persists in higher uniformity.  If
  \(B=X\sqcup Y\sqcup Z\) and \(H\subseteq X\times Y\times Z\), then the
  3-uniform endpoint support
  \[
  \mathcal E(H)=\{\{x,y,z\}:(x,y,z)\in E(H)\}
  \]
  is interval-shielded.  Hence its supported terminal lift has exact value
  \[
  \mathcal R_H(L)
  =
  \left(\sum_{e\in\mathcal E(H)}\pi_B(e)\right)\mathfrak M_T(L-3).
  \]
  For the complete tripartite support this is
  \(a_Xa_Ya_Z\mathfrak M_T(L-3)\), and balanced diffuse weights give endpoint
  factor
  \[
  e^{-\alpha}\alpha^3/27.
  \]
  This branch is outside the two-uniform fractional envelope but is still
  self-similar: it shifts the terminal residual window by three and gives no
  terminal \(R_P(\theta)\) evidence.  The route invariant is now
  higher-uniform endpoint-profile structure versus terminal residual decay.
  The next useful theorem should either bound \(k\)-partite \(k\)-uniform or
  cancellative shielded profiles, compare the factors
  \(e^{-\alpha}\alpha^k/k^k\) against shifted terminal windows, or prove
  cross-fiber exclusions/terminal-core decay below the shielded residual.
  Do not use 3-uniform tripartite endpoint lifts alone as terminal evidence.
- Latest 20260522T000926Z: `mrw-d602b51accb8` controls the whole two-uniform
  triangle-free endpoint-profile branch by a fractional complete-bipartite
  envelope.  For any triangle-free endpoint graph \(G\),
  \[
  \mathcal R_G(L)
  \le
  \frac{P_0(B)R_B^2}{4}\mathfrak M_T(L-2).
  \]
  In diffuse endpoint profiles with total intensity \(\alpha\), this gives
  the uniform endpoint-mass bound
  \[
  \Pi_G(B)\le e^{-\alpha}\alpha^2/4+o(1).
  \]
  The complete bipartite branch attains this envelope and is already the
  one-from-each tower; odd-cycle blow-ups are genuine non-bipartite shields
  but sit strictly below the envelope, with \(C_5\) deficit
  \(e^{-\alpha}\alpha^2/20\).  The route invariant is no longer two-uniform
  endpoint mass.  Future progress must either attack the terminal-core factor
  \(\mathfrak M_T(L-2)\), use cross-fiber exclusions not captured by
  interval-shielded endpoint mass, or jump to higher-uniformity shielded
  supports such as cancellative 3-uniform endpoint families.  Do not use
  triangle-free or odd-cycle endpoint-pair mass alone as terminal evidence.
- Latest 20260521T232925Z: `mrw-3161f39fd270` proves that the next
  two-uniform shield branch is genuinely non-bipartite.  For the complete
  blow-up of \(C_{2h+1}\) on
  \(B=V_0\sqcup\cdots\sqcup V_{2h}\),
  \[
  \mathcal R_G(L)
  =
  P_0(B)\left(\sum_{i=0}^{2h}R_iR_{i+1}\right)\mathfrak M_T(L-2),
  \qquad
  R_i=\sum_{v\in V_i}\frac{q_v}{1-q_v}.
  \]
  In the balanced diffuse case the endpoint mass tends to
  \[
  e^{-\alpha}\frac{\alpha^2}{2h+1},
  \]
  with \(C_5\) giving \(e^{-\alpha}\alpha^2/5\).  This odd-cycle shield is not
  a single one-from-each subtower on the same endpoint coordinate set, although
  its edge set is the disjoint union of adjacent complete-bipartite blocks.
  The route invariant is now triangle-free endpoint-profile structure:
  bipartite shields are old towers, odd-cycle blow-ups are finite
  non-bipartite shifted residuals, and the next theorem must either decompose
  high-mass triangle-free endpoint graphs into bipartite pieces plus controlled
  odd-cycle components or promote a clean odd-cycle residual envelope.  Do not
  use odd-cycle endpoint-pair lifts alone as terminal evidence.
- Latest 20260521T222219Z: `mrw-50bca8113dbf` closes the bipartite
  endpoint-pair shield branch by reducing it to the exact one-from-each tower.
  For \(P=T\sqcup X\sqcup Y\) and \(G\subseteq X\times Y\),
  \[
  \mathcal R_G(L)
  =
  \left(\sum_{xy\in E(G)}\alpha_x\beta_y\right)\mathfrak M_T(L-2)
  \le
  \alpha_X\beta_Y\mathfrak M_T(L-2).
  \]
  The complete bipartite case \(G=K_{X,Y}\) is exactly the \(r=1\) endpoint
  tower with \(\Gamma_1=\alpha_X\beta_Y\); non-complete bipartite graphs are
  subtowers with empty fibers on nonedges.  The balanced positive mass
  \(e^{-\alpha}\alpha^2/4\) is therefore not new structure.  The route
  invariant is now odd-cycle/non-bipartite triangle-free endpoint-pair
  shielding: construct and audit \(C_5\)-blow-up shields, compute their
  diffuse shifted residual, and decide whether they reduce to a finite mixture
  of bipartite subtowers or form a genuinely new residual branch.  Do not use
  bipartite or triangle-free endpoint-pair lifts alone as terminal evidence.
- Latest 20260521T214218Z: `mrw-1b04240e9886` identifies the first positive
  overlapping endpoint-shielded obstruction.  Two-uniform endpoint supports are
  graph edge families, and they are interval-shielded exactly when the graph is
  triangle-free.  For a triangle-free graph \(G\),
  \[
  \mathcal R_G(L)=\Pi_G(B)\mathfrak M_T(L-2),
  \qquad
  \Pi_G(B)=
  \left(\prod_{b\in B}(1-q_b)\right)
  \sum_{uv\in E(G)}
  \frac{q_u}{1-q_u}\frac{q_v}{1-q_v}.
  \]
  Balanced complete bipartite graphs with diffuse endpoint weights satisfy
  \[
  \Pi_G(B)\to e^{-\alpha}\alpha^2/4,
  \]
  so positive overlapping shielded mass survives beyond singleton and
  disjoint-block branches.  The route invariant is now
  triangle-free/bipartite endpoint-pair residual versus tower self-similarity:
  either prove a weighted triangle-free endpoint-pair residual theorem with
  shifted terminal windows, or show that dense bipartite shields are exactly
  the known one-from-each tower residual and must pass the problem to terminal
  core decay.  Do not use bipartite or triangle-free endpoint-pair lifts alone
  as terminal evidence.
- Latest 20260521T210217Z: `mrw-7f81977a8847` controls the
  disjoint-block/matching endpoint shield class.  If
  \(\mathcal A\subseteq2^B\) is a pairwise disjoint family of nonempty endpoint
  blocks, then \(\mathcal A\) is interval-shielded and its terminal lift has
  exact residual
  \[
  \sum_{A\in\mathcal A}\pi(A)\mathfrak M_T(L-|A|).
  \]
  For diffuse endpoint weights, every block of size at least two contributes
  only \(O(\delta Qe^{-Q})\), where \(\delta=\max_b q_b\) and
  \(Q=\sum_b q_b\).  Hence matchings and larger disjoint blocks vanish in the
  diffuse limit; the only positive disjoint-block obstruction is the singleton
  residual \(e^{-\alpha}\alpha_1\mathfrak M_T(L-1)\).  The route invariant is
  now the overlapping shielded-antichain problem: prove that high-mass
  interval-shielded endpoint families decompose into a singleton/disjoint-block
  core plus negligible remainder, or construct an overlapping high-mass
  shielded family and test the full pair-link intervals and any
  \(R_P(\theta)\) lift.  Do not treat interval-shielded endpoint mass,
  singleton lifts, or disjoint block/matching lifts as terminal evidence.
- Latest 20260521T202217Z: `mrw-89ac956348a7` obstructs any endpoint-only
  decay theorem based solely on interval-shieldedness.  The singleton endpoint
  family \(\mathcal E_1(B)=\{\{b\}:b\in B\}\) is interval-shielded, has exact
  mass
  \[
  \Pi_1(B)=
  \left(\prod_{c\in B}(1-q_c)\right)
  \sum_{b\in B}\frac{q_b}{1-q_b},
  \]
  and under diffuse weights with \(\sum q_b\to\alpha\in(0,\infty)\) satisfies
  \[
  \Pi_1(B)\to \alpha e^{-\alpha}.
  \]
  Its terminal lift is fully pair-link-free by `mrw-20ca89f696f2` and has
  exact value
  \[
  \Pi_1(B)\mathfrak M_T(L-1).
  \]
  The route invariant is now a refined variational problem rather than a
  plain shield-mass problem.  Useful progress must exploit the endpoint-size
  profile and the shifted terminal residual windows, prove terminal residual
  decay, or show that shielded families exceeding singleton/matching-type
  envelopes must generate nonconstant endpoint interval triples.  Do not treat
  interval-shielded endpoint mass, ambient endpoint moments, or singleton
  endpoint lifts as terminal evidence.
- Latest 20260521T194216Z: `mrw-3d6bb8271a4c` closes the clean
  interval-shielded endpoint branch.  If \(\mathcal E\subseteq2^B\) has no
  nonconstant endpoint interval triple, then the best pair-link-free
  endpoint-fiber union supported on \(\mathcal E\) has value
  \[
  \sum_{e\in\mathcal E}\pi_B(e)\mathfrak M_T(L-|e|).
  \]
  In the endpoint-tower setting this becomes the exact shielded defect
  residual
  \[
  \mathcal S_{\mathrm{sh}}(L;\mathcal E)
  =
  \sum_{\omega\in\mathcal E}
  \pi(\omega)\mathfrak M_{P_r}(L-|E(\omega)|),
  \]
  where shieldedness is imposed on the endpoint-set image
  \(\{E(\omega):\omega\in\mathcal E\}\).  The route invariant is now sharper:
  shielded endpoint mass is not a defect certificate; it is a self-similar
  variational residual.  Future progress must either bound the weighted
  interval-shielded endpoint variational problem itself, prove terminal
  residual decay, or force unshielded nonconstant endpoint interval triples so
  that `mrw-20ca89f696f2` creates terminal cross-fiber exclusions.  Do not use
  ordinary endpoint-pattern pair-link-freeness without antichain control,
  ambient endpoint moments, or single fixed endpoint-pattern mass as terminal
  evidence.
- Latest 20260521T182914Z: `mrw-20ca89f696f2` identifies the exact
  cross-pattern object missing from the endpoint-pattern residual budget.
  For \(P=B\sqcup T\), \(S_i=e_i\cup R_i\), pair-link intervals factor as
  \[
  S_3\in I_P(S_1,S_2)
  \quad\Longleftrightarrow\quad
  e_3\in I_B(e_1,e_2)\ \text{and}\ R_3\in I_T(R_1,R_2).
  \]
  Hence cross-pattern improvement over `mrw-05f82d03b190` must come from
  endpoint triples \(e_3\in I_B(e_1,e_2)\) whose terminal fibers have forbidden
  interval intersections.  The clean endpoint-only shield is no nonconstant
  endpoint interval triple, equivalently ordinary endpoint pair-link-freeness
  plus an antichain condition.  The next route invariant is therefore
  antichain/interval-shield versus cross-fiber exclusion: either high-support
  defect mass creates many endpoint interval triples to charge, or it lives in
  an interval-shielded endpoint-pattern family that must be bounded by a new
  endpoint-pattern mass theorem or reduced to fixed-pattern terminal residuals.
- Latest 20260521T174914Z: `mrw-1f23857438d4` shows that replacing ambient
  endpoint moments by realized overfull mass is still not enough.  A fixed
  exact endpoint pattern \(\omega\) has an interval-isomorphism with the
  terminal core:
  \[
  \mathcal A_\omega(\mathcal R)=\{R\cup E(\omega):R\in\mathcal R\}
  \]
  is pair-link-free iff \(\mathcal R\) is pair-link-free, and its high-support
  value is exactly
  \[
  \pi(\omega)\mathfrak M_{P_r}(L-|E(\omega)|).
  \]
  If \(\omega\) is overfull, this is fully realized overfull mass, but it is
  still a shifted terminal residual rather than a pointwise-incidence
  certificate.  The route invariant is now cross-pattern: a future
  \(\Xi>0\) theorem must use interaction between distinct endpoint patterns,
  prove terminal residual decay in every fixed pattern, or identify a separate
  same-component point-support overlap.  Single-pattern overfull mass is
  quarantined as residual self-similarity.
- Latest 20260521T170913Z: `mrw-d65c4d544e56` kills the direct
  endpoint-moment-to-pointwise-incidence route.  The endpoint-moment terms in
  `mrw-2a765ca2676f` are ambient product-law budgets unless connected to
  realized family mass.  Exact one-from-each endpoint assemblies
  \[
  \mathcal A=\{R\cup\{x,y\}:x\in X,\ y\in Y,\ R\in\mathcal R_{xy}\}
  \]
  remain pair-link-free by endpoint-fiber decoupling, have
  \(\Xi=w(X\cap Y)=0\), but can have positive same-class moment
  \[
  R_2=\sum_{\{p,q\}\subseteq X}q_pq_q+
  \sum_{\{p,q\}\subseteq Y}q_pq_q
  \]
  and positive collapsed absorbed cubic slack.  The route invariant is now
  stricter: \(R_2\), \(R_2^2\), and absorbed endpoint tails cannot be used as
  terminal evidence for mixed incidence.  The next theorem must produce a
  realized witness, such as actual high-support mass in overfull endpoint
  slices, mass outside exact one-from-each occupancy, or an escaped
  strict-deletion slice.  Only then can `mrw-7f0eb8d1648c` charge the mass to
  coherent-component defect.  If no such witness can be forced, the surviving
  object is another exact endpoint-tower or shifted terminal-core residual
  problem, not a pointwise-incidence contradiction.
- Latest 20260521T160712Z: `mrw-2a765ca2676f` turns the previous
  strict-deletion continuation target into an explicit endpoint-moment budget.
  Let
  \[
  R_2=\sum_{e\in\mathcal E_{\mathrm{ov}}}q_e.
  \]
  After inserting the \(b=2\) absorbed-window bound from `mrw-791fae526f01`
  into `mrw-5df7f8135e2c`, every pair-link-free
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
  The route invariant has sharpened from "control recursive strict-deletion
  residuals" to "control one terminal window plus two endpoint-moment error
  budgets."  The second-generation overfull charge is quadratically summable
  because every retained induced endpoint class is an original endpoint class
  or a subset of one; the collapsed enlarged-core cost is a third-order
  absorbed-class moment.  This is still not residual decay and not an
  \(R_P(\theta)\) lift.  The next theorem should force pointwise mixed
  incidence from any non-negligible endpoint-pair or absorbed-third-order
  mass, using `mrw-7f0eb8d1648c`; failing that, build the endpoint-moment-heavy
  candidate and run the full pair-link interval audit.
- Latest 20260521T152927Z: `mrw-5df7f8135e2c` and `mrw-791fae526f01`
  convert the strict-deletion branch into a terminal-window plus
  higher-occupancy-tail problem.  The first corollary applies the
  terminal-or-overfull alternative to every induced strict-deletion tower:
  \[
  \mathfrak M_{P\setminus e}(U)
  \le
  (\Gamma_e+\beta_e)\mathfrak M_{T_e}(U-2\ell_e)
  +
  \pi_{\mathrm{ov}}^e.
  \]
  Thus the global high-support bound becomes
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
  Surviving deletions return to \(T_e=P_r\).  Collapsed deletions produce
  \(T_e=P_r\cup D_j\), but `mrw-791fae526f01` shows these enlarged terminal
  cores are only window averages over the original terminal core:
  \[
  \mathfrak M_{P_r\cup D_j}(L-2r)
  \le
  \mathfrak M_{P_r}(L-2r-2)+\nu_{D_j}(|B|\ge3)
  \le
  \mathfrak M_{P_r}(L-2r-2)+Q(D_j)^3/6.
  \]
  The route invariant has sharpened again: the remaining obstruction is no
  longer "unknown residual on \(P\setminus e\)" or "opaque enlarged core";
  it is the weighted second-overfull charge plus absorbed-class third-order
  tails.  The next theorem should insert the \(b=2\) absorbed-window bound
  into the full iteration and prove those higher-occupancy terms are summable
  under the endpoint mass budgets, or else show that a near-extremal
  higher-occupancy assembly forces pointwise mixed incidence and pays
  `mrw-7f0eb8d1648c`.  Do not treat this as residual decay or an
  \(R_P(\theta)\) lift.
- Latest 20260521T145110Z: `mrw-3dde1053699f` removes the structural blocker
  left by the strict two-point residual reduction.  For every same-class
  endpoint pair \(e=\{p,q\}\subseteq C_j\), the deleted space \(P\setminus e\)
  admits an induced endpoint tower.  If \(C_j\setminus e\ne\varnothing\), the
  induced tower has the same length and terminal core \(P_r\).  If \(C_j=e\),
  level \(j\) is skipped, the opposite class \(D_j\) is absorbed into the
  deeper cores, and the terminal core is \(P_r\cup D_j\).  Hence every strict
  residual in `mrw-c82229c73d8d` is bounded by an induced endpoint-pattern
  residual:
  \[
  \mathfrak M_{P\setminus e}(U)
  \le
  \Gamma_e\mathfrak M_{T_e}(U-2\ell_e)
  +
  \mathcal R_{\mathrm{def}}^e(U).
  \]
  The route invariant is now recursive on induced towers rather than blocked
  by loss of tower structure.  The next theorem must prove a contraction or
  summable induction for
  \[
  \sum_{e\in\mathcal E_{\mathrm{ov}}}q_e
  \left(
  \Gamma_e\mathfrak M_{T_e}(L-2-2\ell_e)
  +
  \mathcal R_{\mathrm{def}}^e(L-2)
  \right),
  \]
  with special attention to collapsed-class cores \(T_e=P_r\cup D_j\).  If
  this induction does not close, the fallback is to prove that near-extremal
  induced strict-deletion residuals force pointwise mixed incidence and pay
  the coherent-component defect budget from `mrw-7f0eb8d1648c`.  Do not treat
  this as residual decay or an \(R_P(\theta)\) lift.
- Latest 20260521T140929Z: `mrw-c82229c73d8d` converts the overfull endpoint
  branch into a strict smaller-ground-set residual inequality.  For same-class
  endpoint pairs
  \[
  \mathcal E_{\mathrm{ov}}
  =
  \bigcup_{j=1}^r\left(\binom{X_j}{2}\cup\binom{Y_j}{2}\right),
  \]
  any pair-link-free \(\mathcal F\subseteq2^P\) satisfies
  \[
  \nu_P(\mathcal F\cap H_L)
  \le
  \mathfrak M_{P_r}(L-2r)
  +
  \sum_{e=\{p,q\}\in\mathcal E_{\mathrm{ov}}}
  q_pq_q\,\mathfrak M_{P\setminus e}(L-2).
  \]
  The route invariant is now recursive rather than purely ambient:
  overfull incidence is controlled by conditioning on a selected same-class
  endpoint pair and passing to \(P\setminus e\).  The key caveat is structural:
  \(P\setminus e\) may not inherit the same endpoint-tower hypotheses, so the
  next theorem must either control strict-deletion residuals uniformly, prove
  a compatible re-towering lemma for \(P\setminus e\), or show that
  near-extremal strict-deletion residuals produce pointwise mixed incidence
  and trigger `mrw-7f0eb8d1648c`.  Do not treat this as terminal residual
  decay or an \(R_P(\theta)\) lift.
- Latest 20260521T133141Z: `mrw-59f327fd233e` sharpens the endpoint-defect
  branch from a raw pattern residual into a terminal-or-overfull alternative.
  Together with the active-layer averaging gate `mrw-9cb7a5d73a8f`, it proves
  that
  \[
  \mathcal R_{\mathrm{def}}(L)
  =
  \sum_m\Pi_m^{\mathrm{def}}\mathfrak M_{P_r}(L-m)
  \]
  cannot hide as a diffuse balanced endpoint-pattern average.  The strongest
  current bound is
  \[
  \mathcal R_{\mathrm{def}}(L)
  \le
  \mathfrak M_{P_r}(L-2r)+\pi_{\mathrm{ov}},
  \]
  where \(\pi_{\mathrm{ov}}\) is the probability that some endpoint class
  \(X_j\) or \(Y_j\) contributes at least two selected coordinates, and
  \[
  \pi_{\mathrm{ov}}
  \le
  \frac12\sum_{j=1}^r(Q(X_j)^2+Q(Y_j)^2).
  \]
  The route invariant is now cleaner: large defect budget forces either a
  large exact-shift terminal residual or large overfull endpoint incidence.
  The next theorem should prove an overfull-incidence charging theorem:
  non-negligible overfull incidence in a high-support pair-link-free family
  must create pointwise mixed incidence chargeable by `mrw-7f0eb8d1648c`,
  lose enough high-support mass, or reduce to a strict smaller terminal-core
  residual with a still-meaningful cutoff.  Do not treat the new propositions
  as terminal residual decay or an \(R_P(\theta)\) lift.
- Latest 20260521T124943Z: `mrw-05f82d03b190` refines the occupancy-defect
  branch into a terminal-core endpoint-pattern residual.  For every endpoint
  pattern \(\omega\), the fiber
  \[
  \mathcal F_\omega=\{R\subseteq P_r:R\cup E(\omega)\in\mathcal F\}
  \]
  is pair-link-free, and the high-support mass decomposes as
  \[
  \nu_P(\mathcal F\cap\{|S|>L\})
  =
  \sum_\omega \pi(\omega)
  \nu_{P_r}(\mathcal F_\omega\cap\{|R|>L-|E(\omega)|\}).
  \]
  Hence the non-exact endpoint branch is bounded by
  \[
  \mathcal R_{\mathrm{def}}(L)
  =
  \sum_{\omega\in\Omega_{\mathrm{def}}}
  \pi(\omega)\mathfrak M_{P_r}(L-|E(\omega)|)
  =
  \sum_m\Pi_m^{\mathrm{def}}\mathfrak M_{P_r}(L-m).
  \]
  The route invariant is now a two-way accounting fork: either
  \(\mathcal R_{\mathrm{def}}(\theta S_P)\) is small under a terminal-core
  residual estimate, or a large defect-pattern budget must be converted into
  pointwise mixed incidence and charged through `mrw-7f0eb8d1648c`.  The next
  theorem should prove such a defect-pattern alternative, preferably
  separating the endpoint-cardinality tail from the terminal residual and
  identifying the first place where cross-pattern pair-link constraints enter.
- Latest 20260521T121039Z: `mrw-640f82d14b4e` gives the current route a clean
  residual-plus-error form.  For a fixed endpoint tower and any pair-link-free
  \(\mathcal F\subseteq2^P\),
  \[
  \nu_P(\mathcal F\cap H_L)
  \le
  \Gamma_r\,\mathfrak M_{P_r}(L-2r)
  +
  \nu_P(\mathcal F\cap D_{\mathrm{tw}}\cap H_L),
  \]
  where \(D_{\mathrm{tw}}\) is the event that at least one endpoint class is
  not occupied exactly once.  The exact zero-\(\Xi\) endpoint-tower branch is
  therefore fully self-similar and quarantined in the residual term; any
  additional high-support mass must be carried by the occupancy-defect slice.
  The route invariant is now sharper: prove that positive mass in
  \(D_{\mathrm{tw}}\) either creates pointwise mixed incidence and pays the
  defect budget from `mrw-7f0eb8d1648c`, loses enough high-support mass by
  occupancy alone, or admits a strict smaller-core residual reduction.  If no
  such charging theorem holds, construct a concrete non-exact zero-\(\Xi\)
  candidate and run the full pair-link interval and \(R_P(\theta)\) audit.
- Latest 20260521T112857Z: `mrw-23227179a350` classifies the clean
  zero-\(\Xi\) exact-occupancy escape model.  If a two-class decomposition
  \(P=Z\sqcup X\sqcup Y\) has exact occupancy
  \[
  |A\cap X|=|A\cap Y|=1
  \qquad(A\in\mathcal A),
  \]
  then \(C_0=X\) and \(C_1=Y\) are disjoint, so pointwise mixed incidence is
  zero, and the family is uniquely an endpoint-fiber assembly.  The full
  pair-link interval then decouples by endpoint pair using
  `mrw-d7b3299d3813`.  Iterated exact occupancy is likewise exactly the
  endpoint-tower model of `mrw-b52df00c958c`, with residual value
  \[
  \Gamma_r\,\mathfrak M_{P_r}(L-2r).
  \]
  The route invariant is now a trichotomy: positive \(\Xi\) pays defect via
  `mrw-7f0eb8d1648c`; zero \(\Xi\) plus exact occupancy reduces to terminal
  endpoint fibers/towers; the only unclassified branch is zero \(\Xi\) with
  occupancy defects, meaning missing or multiple selections from a normalized
  support class.  The next theorem should charge those occupancy defects, or
  produce a concrete non-exact zero-\(\Xi\) candidate and test full
  pair-link/\(R_P(\theta)\) behavior.
- Latest 20260521T104936Z: `mrw-7f0eb8d1648c` identifies the pointwise
  mixed-incidence mass as the concrete local quantity the global route must
  force.  For a coherent robust component \(K\), set
  \[
  C_a(K)=\bigcup_{i\in K}\widehat S_i^a
  \qquad(a=0,1)
  \]
  and
  \[
  \Xi(K)=w(C_0(K)\cap C_1(K)).
  \]
  Under ordinary corridor side disjointness,
  \[
  \Xi(K)\le \mathcal E_{\mathrm{mix}}(K)
  \le (|K|-1)\mathcal D(K).
  \]
  The strategy invariant has sharpened: positive high-support mass must now
  be made to produce pointwise sharing between the two normalized classes
  inside one completed robust component, or else the surviving object has
  disjoint two-class point supports modulo null sets.  That zero-\(\Xi\)
  alternative is the exact local shape expected of coherent endpoint-fiber or
  endpoint-tower candidates.  The next theorem should either force
  \(\Xi(K)\ge\eta\) with bounded-size components or a summed estimate that
  controls the \((|K|-1)\) loss, or classify the zero-\(\Xi\) alternative and
  run the full pair-link/\(R_P(\theta)\) audit.
- Latest 20260521T100912Z: `mrw-b2b9ece4dd87` turns the coherent-component
  mixed-overlap estimate into the explicit accounting certificate needed for
  the next global step.  For a parity-consistent component \(K\), set
  \[
  \mathcal E_{\mathrm{mix}}(K)=
  \sum_{\{i,j\}\subseteq K}\sum_{a\ne b}
  w(\widehat S_i^a\cap\widehat S_j^b),
  \qquad
  \mathcal D(K)=\sum_{i\in K}(D_i^0+D_i^1).
  \]
  Then
  \[
  \mathcal E_{\mathrm{mix}}(K)\le (|K|-1)\mathcal D(K).
  \]
  Consequently, any positive same-component lower bound
  \(\mathcal E_{\mathrm{mix}}(K)\ge\eta\) forces
  \(\mathcal D(K)\ge\eta/(|K|-1)\).  The route invariant is now precise:
  positive mass must either produce same-component mixed normalized overlap,
  which pays defect, or avoid such overlap by remaining in a coherent
  two-class/tower candidate that still needs a full interval and \(R_P\)-lift
  audit.  The next theorem should produce the lower bound on
  \(\mathcal E_{\mathrm{mix}}\), ideally in bounded-size components or in a
  summed form that controls the component-size loss.
- Latest 20260521T093015Z: `mrw-b52df00c958c` extends the exact
  endpoint-fiber reduction to finite iterated towers.  If
  \[
  P=P_0\supseteq P_1\supseteq\cdots\supseteq P_r,\qquad
  P_{j-1}=P_j\sqcup X_j\sqcup Y_j,
  \]
  and the family chooses exactly one endpoint from every \(X_j\) and \(Y_j\),
  then pair-link triples cannot mix endpoint transcripts.  Therefore the
  optimal high-support mass inside the exact tower class is exactly
  \[
  \Gamma_r\,\mathfrak M_{P_r}(L-2r),
  \qquad
  \Gamma_r=\prod_{j=1}^r\alpha_j\beta_j.
  \]
  The route invariant is now fully recursive: staying in the exact coherent
  endpoint-tower model never produces extra savings beyond endpoint factors
  and the terminal core residual.  The next useful theorem must force escape
  from this exact tower and charge the escaped mass to
  `mrw-bc27191b14d4`, or else prove a new terminal-core residual estimate that
  is not just another application of the endpoint-fiber identity.
- Latest 20260521T084930Z: `mrw-fe13472e08c8` shows that the exact
  endpoint-fiber mixture model has no hidden variational gain.  For
  \(P=Z\sqcup X\sqcup Y\), threshold \(L\), and exact one-from-each assemblies
  whose endpoint fibers are pair-link-free,
  \[
  \sup_{\mathcal A}
  \nu_P(\mathcal A\cap\{S:|S|>L\})
  =
  \alpha_X\beta_Y\,\mathfrak M_Z(L-2).
  \]
  The proof is purely finite: `mrw-d7b3299d3813` decomposes mass by endpoint
  pair, each truncated fiber is bounded by the same shifted core residual, and
  the equal-fiber construction attains the bound.  The route invariant is now
  self-similar rather than obstructive: optimizing heterogeneous endpoint
  fibers cannot beat the shifted core problem.  The next target is therefore
  outside the exact model: force positive high-support mass to leave the
  one-from-each normal form and pay the mixed-overlap defect budget from
  `mrw-bc27191b14d4`, or prove a stronger shifted core residual theorem that
  can be iterated through this identity.
- Latest 20260521T081052Z: `mrw-d7b3299d3813` audits the exact
  one-from-each coherent two-class assembly against the full pair-link
  interval.  For \(P=Z\sqcup X\sqcup Y\) and endpoint fibers
  \(\mathcal R_{xy}\subseteq2^Z\), the assembly
  \[
  \mathcal A=\{R\cup\{x,y\}:x\in X,\ y\in Y,\ R\in\mathcal R_{xy}\}
  \]
  is pair-link-free iff every \(\mathcal R_{xy}\) is pair-link-free.  The
  full interval test decouples by endpoint pair: cross-endpoint triples are
  impossible because an interval completion would need two points from one
  endpoint class.  Product mass decomposes as
  \[
  \nu_P(\mathcal A)=
  \sum_{x,y}\alpha_x\beta_y\nu_Z(\mathcal R_{xy}),
  \]
  and high-support mass is the same endpoint-weighted mixture with the core
  cutoff shifted by \(+2\).  The route invariant has changed: the exact
  two-class coherent assembly is not killed by full pair-link intervals; it
  reduces to an endpoint-fiber mixture problem.  The next target is a weighted
  endpoint-fiber high-support theorem, or a proof that positive mass must exit
  the exact one-from-each form and pay the mixed-overlap defect budget from
  `mrw-bc27191b14d4`.
- Latest 20260521T073215Z: `mrw-bc27191b14d4` converts the coherent
  signed-potential normal form into a component-level defect budget.  In the
  complete robust side-overlap graph, a parity-consistent connected component
  with potential \(\epsilon_i\) can be normalized by
  \[
  \widehat S_i^a=S_i^{a+\epsilon_i\pmod2}.
  \]
  After normalization, every mixed side overlap between distinct corridors is
  defect-small:
  \[
  a\ne b
  \quad\Longrightarrow\quad
  w(\widehat S_i^a\cap\widehat S_j^b)
  \le \widehat D_i^a+\widehat D_j^b.
  \]
  Summing over a component \(K\) gives
  \[
  \sum_{\{i,j\}\subseteq K}\sum_{a\ne b}
  w(\widehat S_i^a\cap\widehat S_j^b)
  \le
  (|K|-1)\sum_{i\in K}(D_i^0+D_i^1).
  \]
  The route invariant is now quantitative at component scale: a coherent
  two-class assembly may have large equal-normalized-side sharing, but all
  cross-class sharing must be paid for by near-purity defect.  The next target
  is to find a global source of cross-class overlap mass inside robust
  components, or to explicitly build the two-class assembly and audit every
  full pair-link interval plus any possible \(R_P(\theta)\) lift.
- Latest 20260521T065018Z: `mrw-10ea41c73237` turns the coherent
  signature-potential alternative into a pairwise quantitative filter.  If
  two near-complete corridors \(i,j\) have one robust side overlap
  \(O_{bc}>D_i^b+D_j^c\), then the side parity \(p=b+c\pmod2\) determines the
  relative corridor signatures:
  \[
  \tau_j=\operatorname{comp}^p(\tau_i).
  \]
  Every side overlap of the opposite relative parity is defect-small:
  \[
  b'+c'\not\equiv p\pmod2
  \quad\Longrightarrow\quad
  w(S_i^{b'}\cap S_j^{c'})
  \le D_i^{b'}+D_j^{c'}.
  \]
  Thus
  \[
  O^{(1-p)}_{ij}\le D_i^0+D_i^1+D_j^0+D_j^1.
  \]
  The next route invariant is no longer just component parity consistency:
  a coherent assembly must place each robust corridor-pair overlap into one
  relative parity class, with all forbidden-parity overlap charged to
  near-purity defect.  The next target is to aggregate this charge over a
  component or construct a two-class assembly satisfying it and test full
  pair-link intervals.
- Latest 20260521T060947Z: `mrw-a082a34f6797` resolves the
  parity-consistent alternative left by `mrw-750fb7a7e30c` into a signed
  potential normal form.  For a robust side-overlap edge \(e\) with endpoint
  labels \(s_e(i),s_e(j)\), put
  \[
  p_e=s_e(i)+s_e(j)\pmod 2.
  \]
  Every robust connected component has a parity potential
  \(\epsilon_i\in\{0,1\}\) with
  \[
  \epsilon_i+\epsilon_j=p_e\pmod 2,
  \]
  so one root signature \(\rho\) forces all selected corridor signatures by
  \[
  \tau_i=\operatorname{comp}^{\epsilon_i}(\rho),
  \]
  and every oriented side \(S_i^b\) has selected pure signature
  \(\operatorname{comp}^{\epsilon_i+b}(\rho)\).  In the complete case this is
  actual positive-weight support containment.  The route invariant is now
  binary: either positive high-support mass forces a robust odd-parity
  component, or the surviving object is a two-class coherent
  signature-potential assembly that must fail a full pair-link interval test.
- Latest 20260521T052939Z: `mrw-750fb7a7e30c` turns overlap-packing into a
  signed graph obstruction for corridor-family assembly.  For near-complete
  corridors with oriented sides \(S_i^0=U_i\), \(S_i^1=W_i\), a robust
  same-side overlap forces equal selected inherited signatures, while a
  robust cross-side overlap forces complementary signatures.  Hence every
  fully robust side-overlap cycle has even total side parity.  Any odd-parity
  cycle must contain an edge whose overlap is bounded by the corresponding
  near-purity defects.  The next route invariant is now concrete: either
  positive high-support mass creates a robust odd-parity cycle, or the
  surviving assembly is a parity-consistent signature tree that must be
  constructed and tested directly.
- Latest 20260521T045012Z: `mrw-206678825c7a` gives the first overlap-packing
  tool for global near-purity assembly.  If two near-complete inherited
  signature corridors \(U_j|W_j\) have chosen signatures \(\tau_j\), then
  incompatible choices can share only defect-sized side mass:
  \[
  \tau_1\ne\tau_2
  \quad\Longrightarrow\quad
  w(U_1\cap U_2)
  \le
  (1-\lambda_1)A_1+(1-\lambda_2)A_2,
  \]
  with the analogous \(W_1\cap W_2\), \(U_1\cap W_2\), and \(W_1\cap U_2\)
  estimates.  Scout was malformed and raw-only; focused Oracle hit the usage
  limit, so the promotion is local-audit only.  The next route invariant is
  no longer just local near-purity, but a global corridor-family mechanism
  forcing overlapping near-complete corridors whose signature requirements
  cannot all be packed without defect.
- Latest 20260521T040944Z: `mrw-36595780824f` upgrades exact
  ancestor-signature inheritance to a quantitative near-complete corridor
  theorem.  Under the ancestor complete-bipartite slice hypotheses, any
  weighted lower corridor \(U|W\) satisfies
  \[
  M_Q(U,W)\le\sum_\tau A_\tau B_{\bar\tau}.
  \]
  Therefore, if \(M_Q(U,W)\ge\lambda AB\) for \(1/2\le\lambda\le1\), then one
  inherited complementary signature pair carries at least a \(\lambda\)-fraction
  of both side weights:
  \[
  A_{\tau^*}\ge\lambda A,\qquad
  B_{\bar\tau^*}\ge\lambda B.
  \]
  Focused Oracle caught and the cycle patched the \(\lambda=1/2\) tie case in
  both this node and `mrw-8a0c228a0166`.  The next route invariant is now
  global incompatibility among near-pure inherited signatures across many
  corridors; local exact completeness is no longer the bottleneck.
- Latest 20260521T033055Z: `mrw-49eaa53e7ffe` gives an
  ancestor-signature purity test for global coherent-corridor assembly.  Under
  the nested upper complete-bipartite hypotheses of `mrw-fced7420b905`, if the
  lower slice contains a complete corridor \(K_{U,W}\), then the whole corridor
  is contained in one complementary ancestor-signature pair:
  \[
  U\subseteq V_\tau,\qquad
  W\subseteq V_{\mathbf 1-\tau}.
  \]
  In weighted equality form, full product lower edge mass across \(U|W\)
  forces the positive-weight supports to lie in one such complementary pair.
  This converts the equality case of the coherent normal form
  `mrw-827094b15843` into a global assembly filter: any complete corridor must
  align with every ancestor upper bipartition already present on the same
  vertex set.  The next route invariant is incompatibility of inherited
  ancestor signatures across many corridors, not another local heavy-corridor
  normal form.
- Latest 20260521T025048Z: `mrw-827094b15843` converts repeated
  dominant-pair persistence into a local coherent normal form.  For one fixed
  coarse complementary corridor \(A=V_\tau\), \(B=V_{\bar\tau}\) refined by
  \(\ell\) nested upper cuts, a near-full lower corridor
  \[
  M_Q(A,B)\ge\lambda W_AW_B,\qquad 1/2\le\lambda\le1,
  \]
  has a full refined signature \(\omega^*\) with
  \[
  \alpha_{\omega^*}\ge\lambda W_A,\qquad
  \beta_{\bar\omega^*}\ge\lambda W_B.
  \]
  The same \(\omega^*\) gives a coherent prefix chain at every intermediate
  refinement depth:
  \[
  \alpha^{(t)}_{\omega^*_{\le t}}\ge\lambda W_A,\qquad
  \beta^{(t)}_{\overline{\omega^*_{\le t}}}\ge\lambda W_B.
  \]
  Equality forces a complete positive-weight corridor on one complementary
  refined-signature pair, modulo zero-weight vertices.  The surviving
  obstruction is no longer local diffuse anti-alignment; it is global assembly
  of many already coherent normal-form corridors.
- Latest 20260521T021237Z: `mrw-8a0c228a0166` gives the near-equality
  rigidity for the corridor-refinement invariant.  In the setting of
  `mrw-a9efecc818c7`, after normalizing refined side weights by
  \[
  p_\omega=\alpha_\omega/W_A,\qquad q_\omega=\beta_\omega/W_B,
  \]
  the lower edge mass across a coarse complementary corridor satisfies
  \[
  M_Q(A,B)\le
  W_AW_B\sum_\omega p_\omega q_{\bar\omega}.
  \]
  If \(M_Q(A,B)\ge\lambda W_AW_B\) for \(1/2\le\lambda\le1\), then some
  complementary refined-signature pair \((\omega_0,\bar\omega_0)\) carries at
  least a \(\lambda\)-fraction of both side weights:
  \[
  \alpha_{\omega_0}\ge\lambda W_A,\qquad
  \beta_{\bar\omega_0}\ge\lambda W_B.
  \]
  Equality gives true refined-signature purity on the positive-weight support.
  The route invariant is now sharper: persistent heavy corridors cannot remain
  diffusely anti-aligned over many refined pairs.  They must keep selecting
  dominant complementary refined-signature pairs, or lose capacity.  The next
  global target is to prove that such dominant pairs cannot persist at
  positive high-support mass without collapsing into a rigid coherent normal
  form, or to construct that normal form and test the full pair-link interval.
- Latest 20260521T012914Z: `mrw-a9efecc818c7` sharpens the heavy-corridor
  side of signature fragmentation.  If a coarse complementary corridor
  \(A|B\) survives the first \(m\) nested cuts, then any additional nested
  cuts refine it into classes \(A_\omega,B_\omega\), and the lower edge mass
  across the corridor is bounded by
  \[
  M_Q(A,B)\le
  \sum_{\omega\in\{0,1\}^{\ell}}\alpha_\omega\beta_{\bar\omega}.
  \]
  For one added cut,
  \[
  M_Q(A,B)\le
  W_AW_B-(\alpha_0\beta_0+\alpha_1\beta_1).
  \]
  The new route invariant is anti-alignment: a corridor remains heavy only if
  subsequent cuts place the two coarse sides on opposite refined sides in
  weighted product.  The next global target is to prove this anti-alignment
  cannot persist across enough high-support mass, or to construct a coherent
  non-product assembly where it does.
- Latest 20260521T005033Z: `mrw-816fd32c3294` converts complementary-signature
  coherence into a weighted fragmentation dichotomy.  If \(m\ge1\) nested
  upper complete bipartite blocks define signature classes \(V_\tau\) on a
  common lower vertex set \(V\), and \(W_\tau\) are arbitrary nonnegative
  class weights, then the lower slice edge mass satisfies
  \[
  M_Q(V)\le\sum_{\{\tau,\bar\tau\}}W_\tau W_{\bar\tau}.
  \]
  In particular, if \(\rho=\max_\tau W_\tau/W\), then
  \[
  M_Q(V)\le\frac{\rho}{2}W^2.
  \]
  The route invariant is now quantitative: independent upper cuts are useful
  only if they fragment signature mass; otherwise a heavy complementary
  corridor survives and becomes the next object to classify or refute.  This
  remains nonterminal squarefree support-level progress, not a proof of
  \(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or an \(R_P(\theta)\) lift.
- Latest 20260521T001014Z: fixed complete-bipartite blow-ups no longer count
  as independent coherent counterexample candidates.  Proposition
  `mrw-c7c76faed872` proves the exact equivalence
  \[
  \mathcal B(\mathcal R;X,Y)\text{ pair-link-free in }2^P
  \quad\Longleftrightarrow\quad
  \mathcal R\text{ pair-link-free in }2^{P\setminus(X\cup Y)}
  \]
  for disjoint nonempty fixed parts \(X,Y\), where
  \[
  \mathcal B(\mathcal R;X,Y)=
  \{R\cup\{x,y\}:R\in\mathcal R,\ x\in X,\ y\in Y\}.
  \]
  Product measure and high-support mass factor through the same construction,
  with multiplier \(\alpha_X\alpha_Y\) and support shift \(+2\).  The direct
  fixed-part blow-up route is therefore self-similar rather than terminal.
- Latest 20260521T001014Z Scout-audited patch: `mrw-fced7420b905` promotes the
  locally checked nested-core path-shadow coherence theorem.  For \(Q\subseteq
  R\),
  \[
  E_Q^\mathcal F\cap P_2(G_R^\mathcal F)=\varnothing.
  \]
  Thus upper complete bipartite blocks force lower slice graphs to respect the
  same cut, and many upper cuts force lower edges to join complementary
  signature classes only.  This is the new progress invariant: quantify
  incompatible bipartition signatures under the prime-biased high-support law,
  or construct a non-product dense-slice assembly that evades the signature
  collapse and survives every full pair-link interval plus any possible
  \(R_P(\theta)\) lift.
- Latest 20260520T233725Z: `mrw-f83b56a1aa89` proves the local complete
  bipartite stress test for path-shadow overlap collapse.  A fixed-core slice
  \[
  \mathcal F_{R,X,Y}=\{R\cup\{u,v\}:u\in X,\ v\in Y\}
  \]
  is pair-link-free and, for same-side endpoints \(x,z\in X\), has empty
  endpoint-pair core while its path shadows collapse onto the common union
  \(\bigcup_{y\in Y}2^{R\cup\{y\}}\).  Oracle caught the key first-draft
  omission: vertices \(r\in R\) are also middle vertices, with
  \[
  \mathcal P^r_{xz}=\{(R\setminus\{r\})\cup\{y\}:y\in Y\}.
  \]
  The corrected \(T,Q\) formulas show the Cauchy \(T^2/Q\) bottleneck can be
  asymptotically sharp locally as the \(q_y\to0\).  Therefore the next useful
  theorem cannot be another local \(Q\)-count: it must prove global cross-core
  incoherence of these collapsed bipartite blocks at positive high-support
  mass, or construct a coherent positive-mass dense-slice family and test the
  full pair-link interval plus any possible \(R_P(\theta)\) lift.
- Latest 20260520T114136Z: `mrw-c6d0c6fa4d30` quantifies the path-shadow
  frontier.  For fixed endpoints \(x,z\), the endpoint-pair core
  \(\mathcal E_{xz}\) is disjoint from the union of all \(y\)-augmented
  endpoint-pair path shadows \(\mathcal S^y_{xz}\).  If
  \(T=\sum_y\mu(\mathcal S^y_{xz})\) and
  \(Q=\sum_{y,y'}\mu(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz})\), with \(Q\)
  the ordered diagonal-including double sum, then
  \[
  \mu\left(\bigcup_y\mathcal S^y_{xz}\right)\ge \frac{T^2}{Q},
  \qquad
  \mu(\mathcal E_{xz})+\frac{T^2}{Q}\le1.
  \]
  Under product measure, each \(\mathcal S^y_{xz}\) has mass at least the
  corresponding two-edge path-core mass.  The next executable target is no
  longer direct weighted-Mantel aggregation or path-shadow disjointness; it is
  to quantify the overlap term \(Q\), especially the off-diagonal intersections
  \(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz}\), or construct a coherent
  positive-mass dense-slice family where those shadows collapse without
  creating a full pair-link interval hit.
- Latest 20260520T110040Z: `mrw-2bcc2955fe38` proves the cross-core
  pair-link path-shadow exclusion.  A two-edge path
  \(R\cup\{x,y\},R\cup\{y,z\}\) in a pair-link-free two-extension slice forbids
  every endpoint-pair completion \(D\cup\{x,z\}\) with
  \(D\subseteq R\cup\{y\}\).  Thus complete bipartite local Mantel extremizers
  cast lower-core forbidden shadows on same-side endpoint pairs.  This does not
  prove a mass theorem, but it gives the next precise bridge: quantify the
  prime-biased product-measure lower shadows of the path-core families, or
  build a positive-mass dense-slice construction that evades those shadows and
  survives the full pair-link interval test.
- Current phase: research-only Codex automation sprint series after local THEORY_v005.
- The \(s=7\) and \(s=8\) inverse-tail floor formulas are proved locally.
- The reciprocal-Gamma complete-monotonicity problem is proved locally.
- The reciprocal-digamma product problem \(P_0(x)=\psi(x)\psi(1/x)\) is proved locally in the stronger complete-monotonicity form for \(-P_0''\).
- The stronger all-\(n\) complete-monotonicity assertion for higher-order \(P_n\) polygamma products is refuted locally.
- The \(P_1\) low-order trigamma frontier now has a proved convexity theorem: \(P_1''(x)>0\) for \(x>0\).
- Complete monotonicity of \(P_1''\) remains unresolved.  It has an exact recurrence, old floating failures that are advisory only, a failed direct dyadic interval route, a proved obstruction to independent pole-family positivity, and a successful convexity proof by ratio normal form.
- The weaker all-\(n\) convexity problem \(P_n''\ge0\) remains open.
- User-steered outside-route restart remains active: the \(P_1/P_n\) \(-P''\) branch is parked, routine \(s=9\) tail inversion is rejected, and the Gamma-product sharp-threshold branch is now parked after producing a localization theorem but not a complete solution.
- New proved theorem `mrw-0fd149ddc79d` solves the sharp endpoint for \(u(s)/(\Gamma(s+\rho)\Gamma(s))\) whenever \(J=u'/u\) is nonincreasing on \([1,\infty)\).
- New proved theorem `mrw-37311e7a5a0f` gives the exact variational threshold for \(u_m(s)=s^m+1\) and proves endpoint failure for all \(m\ge4\).
- New proved theorem `mrw-73218406186e` localizes every \(m\ge4\) polynomial Gamma-threshold maximizer to \(1<s<(m-1)^{1/m}\), but this is partial progress rather than a complete solution of the source open problem.
- Previous live target: Erdos Problem #25, the residue-class logarithmic-density problem, imported as `mrw-3d524c92103b`; it is now parked until a new projection-balance or projection-energy invariant appears.
- Current live target: Erdos Problem #536, the equal pairwise least-common-multiple problem, imported as `mrw-277fbbb4ccb9`.
- New proved counterexample `mrw-8fcc1c2c5cda` blocks ordinary unrestricted weighted shifting for the prime-biased union-free route: a measure-increasing \(S_{2,3}\) shift can take a union-free family to one containing a union triple.  New open problem `mrw-3474bf5c904f` is the replacement strategy target: union-aware compression, max-fiber/container/junta decomposition, or a broad-fiber counterexample.
- New proved proposition `mrw-ba29cdf1fd30` gives the finite-shadow reduction for Erdos #25: \(\delta_N=|C_N|/L_N\), the zero-shadow case is solved, and the positive-shadow case reduces to the tail defect \(\Theta_N\).
- New proved proposition `mrw-f92c897044c4` gives a first positive-tail subcase: \(U_N\to0\) implies logarithmic density \(\delta\), and \(\sum_i1/n_i<\infty\) is enough.  The same proposition proves this union-tail criterion is not necessary, so the next target is overlap-sensitive residual tail control.
- New proved proposition `mrw-171478aeed08` gives an essential-index refinement: indices with zero finite-shadow decrement \(h_i=\delta_{i-1}-\delta_i\) remove no residual first-hit points and may be discarded before applying the tail majorant.  This strictly weakens the raw union-tail condition, but partial redundancy among \(h_i>0\) indices remains open.
- New proved proposition `mrw-e0778085804e` gives a block-uniform first-hit criterion: if finite blocks of actual first-hit sets are uniformly controlled by their total finite-shadow decrement plus a summable error, then Erdos #25 has logarithmic density \(\delta\).
- New proved obstruction note `mrw-536639208ce1` quarantines h-only decrement chasing: fixed individual logarithmic density data alone cannot control escaping mass without a uniformity, scale-localization, or residue-overlap mechanism.
- New proved proposition `mrw-2945dff32e3e` gives a CRT prefix-dispersion certificate: for a finite first-hit block \(G_I\), \(\sup_x\mu_x(G_I)\le P_I+R_I+c_0\eta_I\).
- New proved note `mrw-e0971c9b820a` obstructs the unshifted \(R_I\) summability route: \(R_I\) can be non-summable for singleton blocks because it counts small formal representatives below activation threshold.
- New proved proposition `mrw-f1348014e087` gives the threshold-aware replacement certificate \(\sup_x\mu_x(G_I)\le P_I+Q_I+c_0\eta_I\).
- New proved proposition `mrw-eaf102b5cac0` gives the activation-scale bound \(Q_I\le L_B\eta_I/(n_B\log n_B)\), now superseded as the live invariant by the first-cycle entropy profile below.
- New proved proposition `mrw-7586943cc138` gives the first-cycle entropy bound \(Q_I\le\Phi(n_B,L_B\eta_I)\), recovers the activation-scale bound, and proves support-size-only sharpness.
- New proved lemma `mrw-8d210c890d07` gives the CRT projection-amplification identity, showing that future congruence mass inside a finite shadow is controlled by projected survivor concentration modulo \(g=(M,n)\), not by ambient reciprocal mass alone.
- New open problem node `mrw-277fbbb4ccb9` selects Erdos #536 as the restart frontier; the active obstruction is finite-prime fiber lifting for lcm triples.
- New proved lemmas `mrw-2e217726536f` and `mrw-e80e409bf536` translate Erdos #536 into prime-valuation and squarefree cosunflower language: an equal-pairwise-lcm triple is exactly a triple whose coordinatewise maximum is never unique.
- New proved proposition `mrw-e844b4203305` gives the first local #536 upper bound from disjoint lcm-triangle packings:
\[
f(N)\le \frac{11}{12}N+O((\log N)^2).
\]
- New proved obstruction note `mrw-efc6dd81fc95` rejects the naive positive-density finite-prime fiber lifting heuristic.
- New open problem node `mrw-c5a954e7138b` replaces that false heuristic with the \(P=\{2,3\}\) weighted finite-prime exponent-grid extremal problem.
- New proved proposition `mrw-c44269169b5b` improves the #536 local packing bound to the finite rectangular certificate
\[
f(N)\le \frac{42287}{46656}N+O(1)
=0.9063571673\ldots N+O(1),
\]
and also proves the structured dyadic multiscale bound
\[
f(N)\le
\left(1-\frac{\sigma_{2,3}}3\right)N+O((\log N)^2),
\qquad
\sigma_{2,3}=0.2807753443\ldots,
\]
and proves the unit-corner packing model is saturated at exponent weight \(1/4\).
- New proved theorem `mrw-41a967169307` gives the stronger two-prime row-column fiber bound
\[
f(N)\le N-\left\lfloor\frac N6\right\rfloor.
\]
- New proved proposition `mrw-f835f9671070` gives the finite-prime weighted-grid reduction for #536:
\[
f(N)\le
\sum_{\substack{r\le N\\(r,Q_P)=1}}g_P(N/r),
\qquad
\limsup_{N\to\infty}\frac{f(N)}N
\le
\delta_P\int_1^\infty g_P(t)t^{-2}\,dt.
\]
- New proved obstruction note `mrw-34f73025a206` closes the direct \(P=\{2,3,5\}\) pair-slice transfer: applying the two-prime theorem in fixed third-coordinate slices gives exactly \(5/6\), not an improvement.
- New proved proposition `mrw-a261a0a4df25` gives the corrected finite-prefix plus pair-tail bound
\[
\int_1^\infty g_{235}(t)t^{-2}\,dt\le\frac{149}{48},
\qquad
\limsup_{N\to\infty}\frac{f(N)}N\le\frac{149}{180}<\frac56.
\]
It also certifies the old \([0,2]^3\) weighted independent-set value \(743/300\), but records that the raw \(743/300+277/450\) transfer is invalid because the finite-prime reduction uses a prefix-rank integral.
- New proved proposition `mrw-3367b245c458` extends the exact prefix-rank method through threshold \(162\):
\[
\int_1^\infty g_{235}(t)t^{-2}\,dt\le\frac{197623}{64800},
\qquad
\limsup_{N\to\infty}\frac{f(N)}N\le\frac{197623}{243000}.
\]
This strengthens the local #536 constant but remains constant-density progress.  The next route must extract reusable rank-cover or weighted-cover structure, not merely extend a finite table.
- New proved proposition `mrw-2060f97aad60` gives the fixed finite-prime axis-floor obstruction:
\[
\delta_P\int_1^\infty g_P(t)t^{-2}\,dt
\ge
\delta_P\left(1+\sum_{p\in P}\frac1{p-1}\right).
\]
For \(P=\{2,3,5\}\), the floor is \(11/15\).  This proves fixed finite-prime optimization cannot be terminal; the next bridge must use growing \(P\) or a non-fixed-fiber mechanism.
- New proved proposition `mrw-4daa694d9526` gives the low-support growing-prime criterion.  For \(0\le\theta<1\), if
\[
R_P(\theta)=
\delta_P\int_1^\infty
\bigl(g_P(t)-L_{P,\theta}(t)\bigr)_+t^{-2}\,dt
\]
tends to \(0\) along finite prime sets with \(S_P=\sum_{p\in P}1/p\to\infty\), then \(f(N)=o(N)\).  The next bridge is now the high-support residual \(R_P(\theta)\), not generic growing-\(P\) formulation.
- New proved note `mrw-9afb17b1b84a` gives the squarefree binary-choice obstruction to pointwise support envelopes.  For the first \(2m\) primes grouped into pairs, the one-from-each-pair squarefree family has \(2^m\) members, support \(m\), and no grid-bad triple, while its harmonic mass is at most \(1/m!\).  More generally, every block-transversal spike of support \(r\) has harmonic mass at most \(e^{-r}\).  Thus high support alone does not force grid-bad triples, but the obvious block-transversal obstructions do not refute \(R_P(\theta)\to0\).
- New open problem node `mrw-37dbc6aeedf9` names the biased squarefree residual \(M_P(\theta)\), and proved proposition `mrw-053bc325c601` shows the full high-support layer has vanishing ambient random cosunflower density, so plain ambient supersaturation is unavailable.
- New proved proposition `mrw-3c39ca3d1973` gives the exact pair-link shadow criterion for squarefree cosunflowers.  New open problem node `mrw-d0402aea6f58` names the biased lower-shadow union-cover sufficient route, and new proved proposition `mrw-cc4f876149b7` proves that lower-shadow union-cover-freeness is equivalent to pairwise-intersecting deletion traces below every top set.  The next bridge is therefore a biased weighted trace theorem or explicit positive-mass counterexample.
- New proved proposition `mrw-4a98da3d7f40` gives the fair-thinning upward-boundary identity
\[
\nu_P(\mathcal F)
=
\Pr(A\in\mathcal F,\ C\in\mathcal F)
+
\Pr(A\in\mathcal F,\ C\in(\uparrow\mathcal F)\setminus\mathcal F).
\]
Combined with the fair-thinning ceiling `mrw-c228258e6ab4`, the live bridge is now an upward-boundary leakage problem for nonmonotone tail-sensitive families.
- New conditional proposition `mrw-2a2c5551301e` tilts the thinning law: for \(1/2\le\tau<1\), \(C\sim\nu_{P,\tau}\) with \(\nu_{P,\tau}(p\in C)=1/(\tau p)\), then \(\tau\)-thinning gives \(A\sim\nu_P\).  Assuming the standard \(r\)-biased intersecting trace bound, every lower-shadow-free \(\mathcal F\subseteq H_{P,\theta}\) satisfies
\[
\Pr(A\in\mathcal F,\ C\in(\uparrow\mathcal F)\setminus\mathcal F)
\ge
\nu_P(\mathcal F)
-
\left(1-\tau+\tau^{\theta S_P}\right)\nu_{P,\tau}(\mathcal F),
\]
so positive \(\nu_P\)-mass forces positive near-identity upward-boundary leakage along \(S_P\to\infty\).  New proved proposition `mrw-67f99fecf9e2` proves a separate union-tilted external boundary expansion and refutes global boundary-smallness by exact-rank layers.  New proved proposition `mrw-b4075311abd3` identifies the lower-shadow route exactly with the usual union-free family condition, and open problem `mrw-55a8d9eddd2e` names the prime-biased weighted union-free theorem \(U_k(\theta)\to0\).  The next bridge is a weighted Kleitman/compression/container/junta theorem for \(\nu_{P_k}\), or a genuine positive-mass high-support union-free counterexample, not another raw boundary lower bound.
- New proved proposition `mrw-9e0b4f1a5c33` gives the fixed-junta root-consistency bound: if every proper comparable pair \(A\subsetneq C\) in \(\mathcal F_k\) has \((C\setminus A)\cap J\ne\emptyset\) for one fixed finite \(J\), then \(\mathcal F_k\) is a union of finitely many antichains and has vanishing \(\nu_{P_k}\)-mass, conditional on the same product-measure antichain estimate used by `mrw-54968b07a069`.  Therefore fixed finite roots and fixed finite-junta comparable-pair visibility are no longer viable positive-mass obstruction templates; the remaining obstruction must use moving/growing roots, enough loss of outside variance, or non-junta comparable-pair visibility.
- New proved proposition `mrw-a92d7b6e4031` removes the moving-root trace-count loss: if arbitrary root sets \(J_k\subseteq P_k\) see every proper comparable-pair deletion in \(\mathcal F_k\), then
\[
\nu_{P_k}(\mathcal F_k)
\le
C_0\left(1+\sum_{p_i\notin J_k}\frac1{p_i}\left(1-\frac1{p_i}\right)\right)^{-1/2}.
\]
Thus moving roots only survive at positive mass if they absorb all but bounded reciprocal-prime variance, or if the family evades global comparable-pair visibility altogether.
- New proved proposition `mrw-4b9f5c2e6a1d` closes the near-total-root visibility framing as a separate target.  For every \(B\ge0\),
\[
U_k^{\mathrm{vis},B}(\theta)=U_k(\theta),
\]
because the full root set \(J=P_k\) has outside variance zero and makes comparable-pair visibility automatic.  Even if a proper outside coordinate is required, one-spare padding transfers every positive-mass counterexample to a near-total-root visibility counterexample with outside variance tending to zero.  Future #536 work should not treat bounded or near-zero outside variance as a proper intermediate unless an additional non-vacuous anti-padding or root-essentiality hypothesis is introduced.
- New proved proposition `mrw-7c6a0e9f2d31` kills the broad sparse-intersection high-support code template by a direct weighted private-shadow count.  If all members have size at least \(r\) and all distinct intersections have size \(<t\), then \(\nu_P(\mathcal F)\le\nu_P(|X|=t)/\binom r t\).  Therefore any positive-mass capped pair-link obstruction for \(\theta>1/2\) must contain linearly large intersections somewhere; the next #536 route should quantify high-intersection clustering or construct a genuine clustered counterexample.
- New proved proposition `mrw-18e9c7b0a5af` kills the opposite extreme: one high-intersection clique, or a cover by \(o(\sqrt{S_k})\) such cliques.  The proof uses two independent \(\nu_P\)-samples and the finite second-prime sum
\[
\mathbb E|X\cap Y|=\sum_{p\in P}\frac1{p^2}\le\sum_p\frac1{p^2}<\infty.
\]
Thus any internally \(\gamma S_k\)-intersecting high-support family has mass \(O_\gamma(S_k^{-1/2})\).  The surviving #536 obstruction must have mixed overlap-graph structure, not a sparse code and not a few-clique high-overlap cluster cover.
- New proved proposition `mrw-c7f4e0c9a821` adds the entropy side of the mixed-overlap graph.  Conditioning on any family \(\mathcal F\) of mass \(m>0\) costs only \(\log(1/m)\) relative entropy, and this bounds the squared conditional marginals:
\[
\mathbb E_{\nu_P(\cdot\mid\mathcal F)^{\otimes2}}|X\cap Y|
\le
4\sum_{p\in P}p^{-2}+2\log(1/m).
\]
Consequently, positive-mass high-support families have \(O(1/S_k)\) conditional edge density in the \(\gamma S_k\)-overlap graph, and any cover by internally high-overlap clusters must have \(\Omega(S_k)\) clusters.  The surviving #536 obstruction is therefore a sparse linear-many-cluster overlap graph, not merely a many-cluster graph.
- New proved corollary `mrw-4f1e9a2d6b73` shows that, in a fixed capped band \(\theta S_k<|A|\le\alpha S_k<2\theta S_k\), random-pair union completions and full pair-link interval hits back into the cap have conditional probability \(O(S_k^{-1})\) for every positive-mass family.  Therefore a proof of the weighted union-free theorem cannot rely on positive-density random-pair capped union or pair-link supersaturation.  The next usable mechanism must exploit the rare high-overlap pair geometry, a union-specific rooted hypergraph/container structure, fair-thinning upward boundary, or a non-capped argument.
- New proved corollary `mrw-6d4a8b0f2c91` strengthens this route-kill to endpoint-degree and rectangle forms: the capped union and full pair-link relations in such a fixed cap have no positive-mass endpoint core and no positive-mass product rectangle.  Thus positive endpoint-neighborhood or positive rectangle supersaturation is also quarantined as terminal evidence.  The next target must analyze the rare \(O(S_k^{-1})\) relation set itself, use union-specific hypergraph/container structure, use fair-thinning upward boundary, or leave the capped random-pair framework.
- New proved proposition `mrw-b1f87c9d6a42` kills the projection-only version of that rare-relation route.  Every exact rank layer \(\binom Pr\), \(2\le r\le |P|-1\), has full genuine pair-link projection, and full capped support bands inherit this for all sufficiently large \(k\).  Hence \(O(S_k^{-1})\) random-pair visibility and endpoint/rectangle invisibility are compatible with every vertex having a genuine pair-link witness in the full band.  The next target must use the pair-link-free or union-free hypergraph structure itself, not merely local projection or nonzero endpoint degree.

## Sufficient Conditions

- The \(s=7\) proof cycle is complete because theorem node `mrw-28bcccec471e` contains a proof and finite-case certificate reference.
- The \(s=8\) proof cycle is complete because theorem node `mrw-544506a822b8` contains a proof and exact certificate reference.
- The reciprocal-Gamma proof cycle is complete because theorem node `mrw-48a67678d0c1` contains a proof, Oracle response reference, and local sanity-check reference.
- The reciprocal-digamma proof cycle is complete because theorem node `mrw-0db1ed17aa9a` contains a proof, Oracle response reference, and local symbolic/numeric audit reference.
- The higher-polygamma complete-monotonicity refutation is complete because theorem node `mrw-dee642b8e9cb` contains the \(n\ge29\) analytic counterfamily, the \(n=7\) rational interval certificate, Oracle response reference, and local audit script references.
- The \(P_1\) convexity subcase is complete because theorem node `mrw-58db958e1bf1` proves \(P_1''(x)>0\) through the ratio reduction `mrw-a4339be8da59` and a positive scalar Laplace kernel.
- A future \(P_1\) complete-monotonicity theorem needs either a nonnegative cross-family kernel for all derivatives, a higher-order ratio/recurrence mechanism, or an exact cancellation-aware counterexample certificate.
- The Gamma-product threshold sprint is complete in the monotone-logarithmic-derivative case because theorem node `mrw-0fd149ddc79d` proves both necessity and sufficiency from the monotonicity of \(\psi\).
- The polynomial Gamma-threshold reduction is complete because theorem node `mrw-37311e7a5a0f` proves \(\rho_m=\max R_m\), compactness of the maximum, and \(R_m'(1)>0\) for \(m\ge4\).
- The Gamma maximizer localization subproblem is complete because theorem node `mrw-73218406186e` proves \(1<s_m<(m-1)^{1/m}\) and \(s_m=1+O(\log m/m)\) for every \(m\ge4\) maximizer.
- The Erdos #25 finite-shadow stage is complete because proposition node `mrw-ba29cdf1fd30` proves the finite-density theorem for \(B_N\), the monotone limit \(\delta\), the \(\delta=0\) case, and a sufficient tail-defect criterion.
- The union-tail positive subcase is complete because proposition node `mrw-f92c897044c4` proves \(U_N\to0\) implies logarithmic density \(\delta\), and proves the summable-reciprocal corollary.
- The essential-index positive subcase is complete because proposition node `mrw-171478aeed08` proves \(U_N^{\mathrm{ess}}\to0\) implies logarithmic density \(\delta\), and proves this criterion strictly improves the raw union-tail criterion.
- The block-uniform first-hit positive subcase is complete because proposition node `mrw-e0778085804e` proves that uniform block control by finite-shadow decrement plus summable error implies logarithmic density \(\delta\).
- The CRT prefix-dispersion certificate is complete because proposition node `mrw-2945dff32e3e` proves that threshold-prefix concentration \(P_I\) and CRT residue-prefix dispersion \(R_I\) imply the block-uniform hypothesis.
- The unshifted \(R_I\) summability route is closed as an automatic target because note `mrw-e0971c9b820a` constructs sparse singleton blocks with \(\sum\eta_i<\infty\) but \(\sum R_i=\infty\).
- The threshold-aware CRT certificate is complete because proposition node `mrw-f1348014e087` proves that \(P_I+Q_I\) controls first-hit block mass.
- The activation-scale \(Q_I\) subcase is complete because proposition node `mrw-eaf102b5cac0` proves \(Q_I\le L_B\eta_I/(n_B\log n_B)\) and feeds it through the threshold-aware certificate and block-uniform criterion.
- The first-cycle entropy \(Q_I\) subcase is complete because proposition node `mrw-7586943cc138` proves \(Q_I\le\Phi(n_B,L_B\eta_I)\) and support-size-only sharpness.
- A future Erdos #25 solution in the remaining positive-shadow case needs a new projection-balance or projection-energy invariant; absent that, the route is parked.
- The first Erdos #536 packing stage is complete because proposition node `mrw-e844b4203305` proves \(f(N)\le 11N/12+O((\log N)^2)\) by disjoint \(2,3\)-grid lcm triangles.
- The naive Erdos #536 positive-density finite-prime fiber route is closed because note `mrw-efc6dd81fc95` gives a positive-density set with only the trivial \(P\)-smooth multiplier in every fixed outside-kernel fiber.
- The unit-corner Erdos #536 packing subroute is complete because `mrw-c44269169b5b` proves a matching vertex-charge upper bound \(1/4\) for unit cells.
- The rectangular Erdos #536 packing subroute has a strict improvement because `mrw-c44269169b5b` gives deletion density \(4369/46656\), with the dyadic series as a structured secondary certificate.
- The two-prime row-column fiber subroute is complete because `mrw-41a967169307` proves \(f(N)\le N-\lfloor N/6\rfloor\).
- The general finite-prime integral criterion for Erdos #536 is complete because `mrw-f835f9671070` proves the \(g_P\) bridge.
- The direct \(P=\{2,3,5\}\) pair-slice route is closed because `mrw-34f73025a206` proves it gives exactly the current \(5/6\) constant.
- The first \(P=\{2,3,5\}\) finite-prefix improvement is complete because `mrw-a261a0a4df25` proves the corrected prefix-rank bound \(149/48\), hence \(\limsup f(N)/N\le149/180<5/6\).
- The extended finite-prefix improvement is complete because `mrw-3367b245c458` proves the exact prefix-rank bound \(197623/64800\), hence \(\limsup f(N)/N\le197623/243000\).
- The fixed finite-prime axis-floor obstruction is complete because `mrw-2060f97aad60` proves a positive lower floor for every fixed \(P\).  A future Erdos #536 terminal improvement now needs a growing-prime finite-prime theorem whose constants tend to zero, or a non-fixed-fiber mechanism.  Bare fixed-\(P\) table extension is no longer a preferred target unless it yields explicit reusable dual certificates for a growing-\(P\) criterion.
- The low-support growing-prime criterion is complete because `mrw-4daa694d9526` proves that \(R_P(\theta)\to0\) along \(S_P\to\infty\) implies \(f(N)=o(N)\).  The squarefree pointwise diagnostic is complete because `mrw-9afb17b1b84a` proves high-support block-transversal spikes exist but have vanishing harmonic mass.  The biased squarefree residual problem is named in `mrw-37dbc6aeedf9`, the pair-link shadow criterion `mrw-3c39ca3d1973` proves the exact self-link formulation, and `mrw-b4075311abd3` proves the sufficient lower-shadow route is exactly the prime-biased high-support union-free problem.  The active sufficient condition is now open problem `mrw-55a8d9eddd2e`: prove \(U_k(\theta)\to0\), followed by a lift to a structural prefix-rank inequality \(g_P(t)\le L_{P,\theta}(t)+E_P(t)\), or else construct a genuine nonvanishing biased-mass union-free obstruction with reverse-lift audit.  Global boundary-smallness is quarantined by exact-rank layers, product-measure antichain proposition `mrw-54968b07a069` quarantines the max-fiber antichain skeleton template, `mrw-9e0b4f1a5c33` quarantines fixed finite-junta comparable-pair visibility, `mrw-4f1e9a2d6b73` quarantines random-pair capped union/pair-link supersaturation, and `mrw-6d4a8b0f2c91` quarantines positive endpoint-degree or positive rectangle supersaturation inside a fixed cap as terminal proof styles.
- Public staging remains blocked until the user explicitly requests it.

## Bridge Chains

- Tail zeta partition definition -> exact \(s=7\) and \(s=8\) inverse-tail floor theorems -> application section in local theory.
- Gamma/polygamma route -> Qi-Lim-Nantomah Open Problem 5 -> reciprocal-Weierstrass Laplace kernel -> complete monotonicity theorem.
- Gamma/polygamma route -> Qi-Lim-Nantomah Open Problem 1 -> shifted digamma expansion -> grouped Laplace kernel -> complete monotonicity theorem.
- Gamma/polygamma route -> Qi-Lim-Nantomah Open Problem 2 -> dominant-summand obstruction -> complete-monotonicity refutation -> \(P_1\) low-order survivor -> \(P_1\) convexity theorem -> remaining \(P_1''\) complete-monotonicity proof or counterexample.
- Gamma/Mellin route -> Bulboaca--Zayed Gamma monotonicity problem -> logarithmic derivative threshold -> exact endpoint theorem for decreasing \(u'/u\) -> variational polynomial threshold theorem -> maximizer localization/asymptotics.
- Modular residue route -> Erdos Problem #25 -> harmonic finite-measure model for residue-class avoidance -> proved finite shadow densities \(\delta_N\) -> proved union-tail subcase -> proved essential-index subcase -> proved block-uniform first-hit criterion -> proved CRT prefix-dispersion certificate -> small-residue obstruction to unshifted \(R_I\) -> proved threshold-aware CRT certificate -> proved activation-scale \(Q_I\) bound -> proved first-cycle entropy \(Q_I\) bound -> CRT projection-amplification diagnostic -> Erdos Problem #536 restart -> prime-valuation/cosunflower translation -> unit \(2,3\)-grid lcm-triangle packing -> two-prime row-column fiber theorem -> finite-prime \(g_P\) integral bridge -> pair-slice obstruction -> finite \(P=\{2,3,5\}\) prefix certificate \(149/180\) -> extended prefix-rank certificate \(197623/243000\) -> fixed-prime axis floor \(11/15\) -> low-support growing-prime criterion -> squarefree pointwise support-only obstruction -> biased squarefree residual \(M_P(\theta)\) -> pair-link/lower-shadow deletion trace -> union-free reformulation -> prime-biased weighted union-free theorem -> max-fiber antichain skeletons killed conditionally by product-measure LYM -> fixed finite-junta comparable-pair visibility killed conditionally by the same antichain package -> moving-root/outside-variance theorem -> near-total-root visibility shown terminal-equivalent -> sparse-intersection code templates killed by private shadows -> high-intersection cliques/few-clique covers killed by product-square moment -> conditional entropy overlap energy forces linear many high-overlap clusters -> capped random-pair union and pair-link averaging killed -> rare high-overlap-pair structure or union-specific container/fair-thinning invariant -> exponent-grid prefix-rank residual \(R_P(\theta)\).

## Route Portfolio

- Live routes: Erdos #536 weighted finite-prime lcm hypergraphs, modular entropy refinements, zeta-ratio moment inequalities, and other source-grounded non-tail problems with clear mathematical interest.
- Primary next route: bridge from `mrw-c7f4e0c9a821`, `mrw-4f1e9a2d6b73`, `mrw-6d4a8b0f2c91`, `mrw-18e9c7b0a5af`, `mrw-7c6a0e9f2d31`, `mrw-a92d7b6e4031`, `mrw-9e0b4f1a5c33`, and `mrw-54968b07a069` to the full prime-biased weighted union-free theorem `mrw-55a8d9eddd2e`, or refute the theorem with a genuine positive-mass family outside the killed sparse-code, sublinear-cluster high-overlap, random-pair capped pair-link, endpoint-core/rectangle, rooted-visibility, skeleton, and finite-junta models.  With \(P_k=\{p_1,\ldots,p_k\}\), \(\nu_{P_k}(p_i\in S)=1/p_i\), \(S_k=\sum_{i\le k}1/p_i\), and \(H_{k,\theta}=\{S:|S|>\theta S_k\}\), prove
\[
U_k(\theta)=
\sup\{\nu_{P_k}(\mathcal F):\mathcal F\subseteq H_{k,\theta},\ \mathcal F\text{ union-free}\}\to0
\]
for every fixed \(0\le\theta<1\), or construct a true positive-mass high-support union-free counterexample.  The previous diagnostic subtargets are closed conditionally or directly: max-fiber antichain skeletons from `mrw-2ff2fe94bc57` have vanishing high-support \(\nu_{P_k}\)-mass by `mrw-54968b07a069`, fixed finite-junta comparable-pair visibility has vanishing mass by `mrw-9e0b4f1a5c33`, moving-root visibility with divergent outside variance has vanishing mass by `mrw-a92d7b6e4031`, near-total-root visibility is terminal-equivalent by `mrw-4b9f5c2e6a1d`, broad sparse-intersection code templates are killed by `mrw-7c6a0e9f2d31`, one/few high-intersection clique covers are killed by `mrw-18e9c7b0a5af`, every positive-mass family has \(O(1/S_k)\) high-overlap edge density and needs \(\Omega(S_k)\) high-overlap clusters by `mrw-c7f4e0c9a821`, random-pair union or full pair-link hits back into any fixed cap are \(O(1/S_k)\) by `mrw-4f1e9a2d6b73`, and positive endpoint cores or product rectangles for those capped relations are killed by `mrw-6d4a8b0f2c91`.  The next counterexample must not be rank-only, a fixed finite-core cylinder, upward-closed, exact-rank-layer-like, a max-fiber antichain skeleton, rooted-visible in the killed senses, uniformly low-overlap after any useful cap, random-pair pair-link dense inside a fixed cap, positive-endpoint-degree/rectangle dense inside a fixed cap, or coverable by \(o(S_k)\) high-overlap cliques.  It must be tested against rare high-overlap full pair-link intervals and any reverse lift to \(R_P(\theta)\).  Boundary absorption, deletion traces, tilted thinning, union-tilted expansion, product-measure antichain theory, moving-root decompositions, outside-variance estimates, private-shadow packing, product-square overlap bounds, entropy overlap-energy bounds, capped pair-link sparsity, and endpoint-degree/rectangle sparsity remain useful only as mechanisms toward this weighted theorem.  Uniform Boolean-lattice cardinality bounds are source context, not sufficient proof under the inhomogeneous prime product measure.  Only after the squarefree biased target is settled should the loop lift back to the exponent-grid prefix-rank residual \(R_P(\theta)\).  The fixed \(P=\{2,3,5\}\) branch is secondary unless it reveals a scalable mechanism for \(R_P(\theta)\).
- Parked route: Gamma-product sharp thresholds for polynomial numerators; return only if it directly supports the Erdos modular-density target or the user asks.
- Parked route: \(P_1''\) complete monotonicity by cross-family kernel or exact high-order certificate, pending explicit user request.
- Deferred routes: publisher-stage, Gmail, GitHub pushes, and public application staging until the user explicitly requests them.

## Route Graveyard

- The earlier conjectural status of the \(s=7\) formula is superseded by proved theorem node `mrw-28bcccec471e`.
- The \(s=8\) special case is proved by adjacent-truncation enclosure, but the general \(s>6\) family remains open.
- The reciprocal-Gamma complete-monotonicity problem is superseded by theorem node `mrw-48a67678d0c1`.
- The reciprocal-digamma product \(P_0\) problem is superseded by theorem node `mrw-0db1ed17aa9a`.
- The complete-monotonicity strengthening "\(P_n''\) completely monotone for all \(n\ge1\)" is refuted by theorem node `mrw-dee642b8e9cb`.
- The \(P_1\) convexity subcase is superseded by theorem node `mrw-58db958e1bf1`.
- The Gamma maximizer localization subproblem is superseded by theorem node `mrw-73218406186e`; uniqueness and exact \(\rho_m\) remain open, so the branch is parked rather than declared solved.
- Floating-point-only \(P_1\) high-order failures are quarantined from theorem promotion.
- Direct \(A_m\)-product dyadic intervals for the named \(P_1\) failures are quarantined as too ill-conditioned unless preceded by cancellation splitting.
- Independent pole-family positivity for the canonical \(P_1''\) partial-fraction kernel is quarantined by proved note `mrw-5a84b7d9f2c1`.
- Automatic summability of the unshifted Erdos \(R_I\) certificate defect is quarantined by proved note `mrw-e0971c9b820a`; use threshold-aware \(Q_I\) instead.
- No route has yet closed \(P_1''\) complete monotonicity or the weaker all-\(n\) convexity target.
- Oracle Scout suggestion of \(s=9\) exact inverse-tail floor formula is quarantined as a route-violating consecutive tail repetition.

## Restart Portfolio

- Tail-zeta reciprocal partition formulas are quarantined from automatic next-target selection because the user identified them as repetitive.
- Erdos Problem #25 is no longer the active fallback target; it is parked after the CRT projection-amplification audit unless a new projection-balance or projection-energy invariant appears.
- Erdos Problem #536 remains the active fallback target because it is a source-grounded open problem connected to lcm finite shadows and prime-coordinate maxima.
- The naive finite-prime fiber lifting route for #536 is closed by `mrw-efc6dd81fc95`; do not try to force one rich outside-kernel fiber from positive density alone.
- The unit-corner packing route for #536 is closed by `mrw-c44269169b5b`; do not spend another cycle changing unit-cell parity patterns.
- The two-prime row-column route for #536 is closed by `mrw-41a967169307`; do not spend another cycle on \(P=\{2,3\}\) unless it is proving a reusable general finite-prime criterion.
- The general finite-prime integral bridge is closed by `mrw-f835f9671070`; use it as infrastructure, not as the next target.
- The direct \(P=\{2,3,5\}\) pair-slice transfer is closed by `mrw-34f73025a206`; do not spend another cycle merely slicing the grid by one prime.
- The first active #536 replacement route succeeded partially: `mrw-a261a0a4df25` proves a genuine three-prime finite-prefix improvement to \(149/180\), and `mrw-3367b245c458` extends it to \(197623/243000\).  The fixed finite-prime terminal route is obstructed by `mrw-2060f97aad60`, which gives floor \(11/15\) for \(P=\{2,3,5\}\).  The generic growing-\(P\) route is now sharpened by `mrw-4daa694d9526` to the residual \(R_P(\theta)\), and `mrw-9afb17b1b84a` quarantines pointwise support-only envelopes.  Do not spend another cycle on the invalid \(743/300+277/450\) transfer, fixed-\(P\) table extension, or high-support cardinality-only arguments unless it feeds a biased-measure proof or obstruction for \(R_P(\theta)\).
- The max-fiber antichain skeleton obstruction template is quarantined by `mrw-54968b07a069` under product-measure LYM/anti-concentration.  Do not spend another cycle trying to make that exact template positive-mass; either prove a decomposition from general union-free families to antichain-like max-fibers plus negligible residue, or construct a counterexample outside the template.
- Erdos finite-shadow reduction is done; do not spend another cycle recomputing \(|C_N|/L_N\) unless it feeds a tail-defect estimate.
- Erdos union-tail criterion is done; do not spend another cycle reproving \(U_N\to0\) or \(\sum_i1/n_i<\infty\) unless it is part of a strictly stronger overlap theorem.
- Erdos essential-index criterion is done; do not spend another cycle merely discarding zero-decrement indices unless it feeds a partial-redundancy theorem.
- Erdos block-uniform first-hit criterion is done; do not spend another cycle proving the abstract criterion unless it is made checkable from residue-overlap data.
- H-only finite-shadow decrement control is quarantined by `mrw-536639208ce1`; future uses must add uniformity, scale localization, or residue-overlap hypotheses.
- Erdos unshifted CRT prefix-dispersion certificate is done and its automatic summability route is obstructed; do not spend another cycle trying to sum \(R_I\).
- Erdos threshold-aware CRT certificate, activation-scale \(Q_I\) bound, and first-cycle entropy \(Q_I\) bound are done; the next cycle must use residue structure beyond \(\Phi\), construct a true actual-mass obstruction, or restart inside the Erdos list.
- Gamma-product sharp-threshold base problem is now solved as `APP-0009`;
  polynomial numerator threshold refinements remain parked unless the user
  explicitly returns to that branch.
- Gamma/polygamma curvature and reciprocal-product problems are parked unless the user explicitly asks to return.
- Modular residue entropy and Dirichlet-\(L\) shadow identities remain available.
- Zeta-ratio moment inequalities remain available.
- If the \(P=\{2,3,5\}\) route stalls without an improvement or obstruction, run Scout/Advisor normally inside the full non-staging loop rather than forcing another Erdos-tail continuation.

## Stale Or Quarantined Branches

- Quarantine \(s=9\) and similar consecutive inverse-tail formula work unless a general theorem emerges.
- Quarantine public staging, GitHub pushes, Gmail drafts, and outreach until the user explicitly asks.
- Quarantine repeated \(P_1\) grid sampling unless it is attached to a symbolic proof or exact certificate.
- Quarantine order-80 floating failures as proof claims until exact interval arithmetic certifies one.
- Quarantine the direct \(A_m\)-product interval route in its current form because it bounds after cancellation and produced only zero-straddling intervals.
- Quarantine independent pole-family positivity because the integer and reciprocal pole families are locally negative near \(t=0\).
- Quarantine further \(P_1\) convexity-only work unless it strengthens toward all-\(n\) convexity or complete monotonicity.
- Quarantine the \(P_1/P_n\) branch for now by direct user instruction.
- Quarantine Oracle's old \(s=9\) inverse-tail suggestion as a route violation
  unless the user explicitly asks for tail continuation.  Do not reuse
  `APP-0009` for that parked suggestion; `APP-0009` now names the
  Bulboaca--Zayed Gamma-product threshold application.
- Quarantine Gamma-only maximizer obstruction chasing until it has a direct bridge to a full open-problem solution.
- Quarantine finite-\(N\) Erdos density computations as a completion claim; the only live Erdos obstruction is positive-shadow tail continuity.
- Quarantine pointwise high-support/cardinality-only attacks on \(R_P(\theta)\): `mrw-9afb17b1b84a` proves exponentially large high-support squarefree grid-bad-free spikes.  Future progress must be biased-measure or prefix-integral sensitive.
- Quarantine max-fiber antichain skeletons as positive-mass counterexamples: `mrw-54968b07a069` proves they are negligible under the cited product-measure antichain package.
- Quarantine random-pair capped union or pair-link supersaturation as a terminal
  #536 route: `mrw-4f1e9a2d6b73` proves those hit probabilities are
  \(O(S_k^{-1})\) for every positive-mass capped family when
  \(\alpha<2\theta\).

## Analogy Map

- Moment layer: zeta ratios become expectations under the zeta law.
- Tail layer: \(\zeta_n(s)^{-1}\) is a reciprocal partition function for a tail zeta law.
- Telescoping layer: rational enclosure of a tail sum yields exact floor formulas.
- Curvature layer: derivatives of log partition functions become variances.
- Mellin-Planck layer: Holder inequalities become log-convexity or norm inequalities.
- Reciprocal-Gamma layer: reciprocal substitution creates sign-indefinite terms that can sometimes be regrouped into positive Laplace kernels.
- Polygamma layer: high-order products admit dominant-summand counterexamples; \(P_1\) convexity can be recovered by a ratio surplus, but complete monotonicity still requires higher-order cancellation control.
- Pole-principal audit: high-order derivative screens must distinguish true counterexamples from cancellation artifacts in the double-series pole expansion.
- Pole-family obstruction: positivity cannot be checked one pole family at a time; cross-family cancellation is structurally necessary.
- Ratio-surplus analogy: the successful \(P_1\) convexity proof groups the reciprocal problem into a one-scale \(U,V\) inequality before applying a positive Laplace kernel.
- Analogy between analogies: successful routes group before bounding; stale routes bound after cancellation is exposed.
- Gamma-threshold analogy: if the logarithmic derivative of the numerator is monotone, the entire sharp-constant problem collapses to the left endpoint \(s=1\).
- New analogy between analogies: endpoint certificates are the Gamma-threshold analogue of grouping-before-bounding; both turn a global sign problem into a structural monotonicity fact before estimation.
- Erdos residue analogy: the finite residue-exclusion sets \(B_N\) are modular shadows of an infinite avoidance set, mirroring the theory's finite modular approximations to zeta-law successor entropy.
- New analogy between analogies: both Gamma thresholds and Erdos logarithmic density ask for a global scalar limit produced by local constraints; the Gamma branch produced only localization, so the next test is whether modular finite shadows give a true limit theorem.
- Tail-continuity analogy: Davenport--Erdos for multiples is the benchmark where finite lcm shadows do pass to the infinite object; arbitrary residue classes need a replacement for divisibility monotonicity.
- Union-bound analogy: first-moment tail control works when late residue progressions have small total harmonic mass, but nested multiples show overlap can dominate first moments.
- New analogy between analogies: successful positive-tail routes must group late exclusions before bounding, matching the earlier "group before estimate" lesson from the \(P_1\) and Gamma branches.
- Essential-index analogy: zero finite-shadow decrement is the residue-sieve analogue of a redundant divisor condition; it can be pruned before bounding.
- Partial-redundancy analogy: the next missing analogue of Davenport--Erdos is not full redundancy, but a quantitative version of the \(B_h-B_k\) tail bound for residual first-hit mass.
- Block-uniformity analogy: Davenport--Erdos supplies a uniform tail estimate from grouped density increments; the residue-class branch now needs an explicit CRT/overlap certificate for the same kind of uniformity.
- Escaping-mass analogy: fixed limiting densities are pointwise convergence data, while the Erdos tail asks for uniform integrability over moving indices.
- CRT-prefix analogy: the finite residue support \(D_I\) is now the analogue of the multiplicative support in Davenport--Erdos; the obstruction is prefix concentration of \(D_I\), not merely its density.

## Erudition Map

- Source families represented: exact zeta-tail inverse formulas, asymptotic inverse-tail formulas, Qi-Lim-Nantomah polygamma product open problems, DLMF polygamma formulas, same-point polygamma complete-monotonicity/Turan inequalities, Bernstein-Widder Laplace characterization.
- Latest Erudition Gate inspected:
  - Qi-Lim-Nantomah 2025 for Open Problem 2 provenance.
  - DLMF 5.15 for standard polygamma formulas and trigamma series inputs.
  - Bernstein-Widder/Widder-Schilling-Song-Vondracek context for the nonnegative-Laplace-kernel strategy.
- Erudition mismatch: same-point Turan inequalities, generic Bernstein-Widder context, and independent pole-family positivity do not handle the reciprocal \(x\leftrightarrow1/x\) cancellation.
- New local import: ratio variables \(U=xA_2/A_1\) and \(V=xA_3/A_2\) convert \(P_1\) convexity to a scalar surplus inequality.
- Latest outside-route Erudition inspected Bulboaca--Zayed 2026, "Monotonic nature of the Gamma function", as source context for sharp Gamma-product constants.
- New local import: if \(J=u'/u\) is nonincreasing, the optimal threshold for \(u(s)/(\Gamma(s+\rho)\Gamma(s))\) is \(\psi(1+\rho)\ge \gamma+J(1)\).
- New local import: for \(u_m=s^m+1\), the optimal threshold is the maximum of the inverse-digamma functional \(R_m\); for \(m\ge4\), \(R_m'(1)>0\), so the endpoint formula is not sharp.
- New local import: every \(m\ge4\) polynomial Gamma-threshold maximizer lies in \(1<s<(m-1)^{1/m}\), hence \(s=1+O(\log m/m)\).
- Latest Erdos fallback Erudition inspected the Erdős Problems Database entries #25 and #486, plus the primitive-sets open tag page, and imported #25 as the next source-grounded open target.
- Latest Erdos proof cycle inspected Erdos #25/#486 and the Davenport--Erdos 1936 multiples paper, then promoted the local finite-shadow reduction `mrw-ba29cdf1fd30` and tail obstruction note `mrw-17f44100cb83`.
- Latest Erdos tail sprint rechecked Erdos #25/#486 and the Davenport--Erdos 1936 benchmark, promoted union-tail criterion `mrw-f92c897044c4`, and proved by nested even-modulus exclusions that the criterion is not necessary.
- Latest Erdos overlap sprint inspected Davenport--Erdos 1951, promoted source note `references/sources/20260518T185221Z-davenport-erdos-elementary-proof.md`, and proved essential-index criterion `mrw-171478aeed08`.
- Latest Erdos partial-redundancy sprint reused the Davenport--Erdos 1951 mechanism note and promoted block-uniform criterion `mrw-e0778085804e` plus h-only obstruction note `mrw-536639208ce1`.
- Latest Erdos CRT sprint promoted certificate proposition `mrw-2945dff32e3e`, reducing block uniformity to threshold-prefix concentration \(P_I\) and CRT prefix-dispersion \(R_I\).
- Latest Erdos prefix-defect sprint promoted obstruction note `mrw-e0971c9b820a` and replacement certificate `mrw-f1348014e087`, changing the live defect from unshifted \(R_I\) to threshold-aware \(Q_I\).
- Latest Erdos activation-scale sprint promoted proposition `mrw-eaf102b5cac0`, proving \(Q_I\le L_B\eta_I/(n_B\log n_B)\) and isolating the ratio \(\Lambda_I=L_B/(n_B\log n_B)\).
- Latest Erdos first-cycle entropy sprint promoted proposition `mrw-7586943cc138`, proving \(Q_I\le\Phi(n_B,L_B\eta_I)\) and support-size-only sharpness.
- Latest full-loop Erudition/Oracle audit promoted the CRT projection-amplification identity `mrw-8d210c890d07` and open problem node `mrw-277fbbb4ccb9` for Erdos #536.
- Latest #536 Erudition/Oracle audit inspected Erdos #536, adjacent Erdos list entries, and Tang--Zhang harmonic lcm/sunflower context.  It promoted the local valuation/cosunflower translations, the \(11/12\) disjoint packing bound, the false single-fiber obstruction, and the \(P=\{2,3\}\) weighted finite-prime fiber problem.
- Latest #536 weighted-grid Erudition inspected #536, Tang--Zhang harmonic LCM context, weak-sunflower context, and Naslund--Sawin sunflower-free context.  It promoted no external theorem but clarified that the next route is weighted hypergraph matching/covering rather than harmonic-weight import.
- Latest #536 three-prime Erudition inspected #536/#857 and harmonic lcm/sunflower context, promoted no external theorem, and locally proved the finite-prime \(g_P\) bridge plus pair-slice obstruction.
- Latest #536 extended finite-prefix cycle promoted no external theorem.  It locally proved `mrw-3367b245c458`, extending the corrected prefix-rank integral to
\[
\limsup_{N\to\infty}\frac{f(N)}N\le\frac{197623}{243000},
\]
and confirmed by Oracle audit that this remains finite-computational constant-density progress, not a solution of #536.
- Latest #536 rank-cover Erudition inspected Erdos #536, Tang--Zhang harmonic LCM/sunflower context, and hypergraph cover/matching sources.  It promoted no external theorem, but locally proved fixed finite-prime axis-floor obstruction `mrw-2060f97aad60` and recorded that ordinary matching/fractional LP duals are too weak in the tested \(P=\{2,3,5\}\) prefixes.
- Latest #536 growing-prime Erudition inspected Erdos #536, Tang--Zhang harmonic LCM/sunflower capacity, Naslund--Sawin sunflower-free bounds, and Saxton--Thomason hypergraph containers.  It promoted no external theorem, but locally proved low-support criterion `mrw-4daa694d9526` and identified \(R_P(\theta)\) as the next invariant.
- Latest #536 squarefree-support Erudition inspected union-free, sunflower-free, and pseudo-sunflower contexts.  It promoted no external theorem, but locally proved `mrw-9afb17b1b84a`: block-transversal high-support squarefree spikes are grid-bad-free yet harmonic-measure harmless.
- Latest #536 biased-squarefree Erudition inspected density Hales-Jewett, biased Boolean hypercube, hypergraph container, and removal contexts.  It promoted no external theorem, but locally proved ambient cosunflower sparsity `mrw-053bc325c601` and named the pair-link residual problem `mrw-37dbc6aeedf9`.
- Latest #536 pair-link Erudition inspected union-free families and density Hales-Jewett context.  It promoted no external theorem, but locally proved pair-link shadow criterion `mrw-3c39ca3d1973` and reduced the next support-level attack to a biased lower-shadow union-cover theorem or counterexample.
- Latest #536 lower-shadow Erudition inspected union-free families, EKR/intersecting-family context, and biased intersecting systems.  It promoted no external theorem, but locally proved `mrw-cc4f876149b7`: lower-shadow union-cover-freeness is equivalent to pairwise-intersecting deletion traces below every top set.  Scout stalled in browser and was ingested raw-only; Oracle audited the trace equivalence and recommended weighted lower-shadow double-counting plus a biased intersecting-trace bound.
- Latest #536 boundary-leakage cycle reused biased product-measure intersecting-family and junta/stability context.  It promoted no external theorem as locally proved, but `mrw-2a2c5551301e` records the standard \(r\)-biased intersecting trace bound as an explicit hypothesis and derives the tilted-thinning consequence.  The same cycle locally proved union-tilted expansion and the exact-rank obstruction in `mrw-67f99fecf9e2`; Scout was raw-only and Oracle was advisory only.
- Latest #536 union-free nomenclature Erudition inspected union-free and partition-free family sources, including Balogh--Wagner on counting union-free families, Fox--Lee--Sudakov on maximum union-free subfamilies, and Frankl--Kupavskii on partition-free families.  It promoted no external weighted theorem, but locally proved `mrw-b4075311abd3`, named open problem `mrw-55a8d9eddd2e`, and promoted max-fiber antichain skeleton example `mrw-2ff2fe94bc57`.
- Latest #536 max-fiber skeleton Erudition inspected Yehuda--Yehudayoff product-measure LYM/anti-concentration, promoted no external theorem as locally proved, and promoted conditional implication `mrw-54968b07a069`: the cited product-measure antichain package kills every max-fiber antichain skeleton in high-support prime bias.
- Latest #536 path-shadow overlap cycle promoted no external theorem.  It locally proved `mrw-c6d0c6fa4d30`, turning the path-shadow exclusion into a Cauchy/second-moment bottleneck for the ordered diagonal-including overlap term \(Q=\sum_{y,y'}\mu(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz})\).  Scout was raw-only after malformed \(s=9\) material; Oracle confirmed the proof and terminology caveats.
- Next Erudition trigger: for #536, inspect weighted/biased union-free, Kleitman-type, compression, product-measure container, junta, rank-layer stability, partition-free/deletion-trace methods, or hypergraph link-overlap/container tools only if they can plausibly control the off-diagonal path-shadow intersections \(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz}\) or produce a true positive high-support biased-mass pair-link-free/union-free obstruction outside all quarantined templates.  Do not return to #25 residue-tail continuity unless a new projection-balance invariant is available.

## External-Theory Gaps

- No external theorem is needed for the existing \(s=7\), \(s=8\), reciprocal-Gamma, reciprocal-digamma, high-order counterexample, or \(P_1\) convexity proofs beyond classical formulas already audited.
- The \(P_1''\) complete-monotonicity proof may need a stronger theorem family: Bernstein/Stieltjes kernel closure, total positivity, variation-diminishing transforms, or a new reciprocal two-pole grouping lemma.
- Current literature status for a post-2025 resolution of Qi-Lim-Nantomah Open Problem 2 remains a citation risk; bounded search has not found a direct solved source.
- The polynomial Gamma-threshold case with nonmonotone \(J\) may require proving a unique maximizer of \(J(s)-\psi(s)\) rather than an endpoint argument; this is parked after localization.
- Erdos Problem #25 now requires a theorem-family for projection-balance or projection-energy control of finite residue shadows; absent that, it is parked.
- Erdos Problem #536 now requires proof or obstruction for the prime-biased weighted union-free theorem `mrw-55a8d9eddd2e`, then the high-support prefix-rank residual \(R_P(\theta)\), or a non-fixed-fiber mechanism.  Fixed \(P\) certificates are bounded below by the axis floor in `mrw-2060f97aad60`; low-support mass is negligible along \(S_P\to\infty\); pointwise high-support cardinality is insufficient by `mrw-9afb17b1b84a`; uniform ambient triple-density supersaturation is insufficient by `mrw-053bc325c601`; the exact self-link shadow criterion is recorded in `mrw-3c39ca3d1973`; and the lower-shadow route is exactly union-free by `mrw-b4075311abd3`.  The max-fiber antichain skeleton `mrw-2ff2fe94bc57` is now bounded by `mrw-54968b07a069`, conditional on Yehuda--Yehudayoff product-measure LYM/anti-concentration.  The remaining finite-prime route needs either a local proof/import of the antichain package plus a weighted Kleitman/compression/container/junta decomposition under the prime product measure, or a genuine high-support biased-mass union-free obstruction outside the killed skeleton template.

## Imported Ideas Pending Audit

- General exact inverse-tail floor formulas for integer \(s>6\): open, with solved \(s=7\) and \(s=8\) special cases.
- Higher-order polygamma products \(P_n\): complete-monotonicity strengthening refuted by `mrw-dee642b8e9cb`; \(P_1\) convexity solved by `mrw-58db958e1bf1`; all-\(n\) convexity remains open.
- \(P_1''\): exact recurrence and sign audits in `mrw-1c9d9f07a4ef`; pole-family obstruction in `mrw-5a84b7d9f2c1`; ratio reduction in `mrw-a4339be8da59`; convexity theorem in `mrw-58db958e1bf1`; complete monotonicity pending.
- Order-80 \(P_1\) floating failures: advisory only; require rational interval certification before use.
- Direct \(A_m\)-product dyadic interval method: useful as infrastructure but not currently sufficient for certification.
- Independent pole-family positivity: proved impossible for the canonical partial-fraction decomposition.
- Bulboaca--Zayed Gamma-product polynomial numerator thresholds: monotone \(J\) cases solved by `mrw-0fd149ddc79d`; \(u_m=s^m+1\) reduced by `mrw-37311e7a5a0f`; maximizer localization solved by `mrw-73218406186e`; uniqueness and exact threshold remain pending.
- Erdos residue-class logarithmic density: problem #25 imported as `mrw-3d524c92103b`; finite-density and zero-shadow mechanisms proved in `mrw-ba29cdf1fd30`; union-tail and summable-reciprocal subcases proved in `mrw-f92c897044c4`; essential-index subcase proved in `mrw-171478aeed08`; block-uniform first-hit subcase proved in `mrw-e0778085804e`; h-only decrement route obstructed in `mrw-536639208ce1`; CRT prefix-dispersion certificate proved in `mrw-2945dff32e3e`; unshifted \(R_I\) summability route obstructed in `mrw-e0971c9b820a`; threshold-aware certificate proved in `mrw-f1348014e087`; activation-scale \(Q_I\) bound proved in `mrw-eaf102b5cac0`; first-cycle entropy \(Q_I\) bound proved in `mrw-7586943cc138`; CRT projection amplification proved in `mrw-8d210c890d07`; route parked pending a new projection invariant.
- Erdos equal pairwise lcm problem: problem #536 imported as `mrw-277fbbb4ccb9`; valuation criterion `mrw-2e217726536f`, squarefree cosunflower criterion `mrw-e80e409bf536`, unit packing bound `mrw-e844b4203305`, fiber obstruction `mrw-efc6dd81fc95`, rectangular packing bound `mrw-c44269169b5b`, two-prime row-column theorem `mrw-41a967169307`, finite-prime reduction `mrw-f835f9671070`, pair-slice obstruction `mrw-34f73025a206`, first prefix certificate `mrw-a261a0a4df25`, extended prefix-rank certificate `mrw-3367b245c458`, fixed-prime axis-floor obstruction `mrw-2060f97aad60`, low-support growing-prime criterion `mrw-4daa694d9526`, squarefree binary-choice obstruction `mrw-9afb17b1b84a`, biased squarefree residual problem `mrw-37dbc6aeedf9`, ambient cosunflower sparsity proposition `mrw-053bc325c601`, pair-link shadow criterion `mrw-3c39ca3d1973`, lower-shadow problem `mrw-d0402aea6f58`, deletion-trace equivalence `mrw-cc4f876149b7`, rank-only biased-mass proposition `mrw-02dadc6b1bba`, finite-core-cylinder proposition `mrw-30aae977a4b6`, union-free reformulation `mrw-b4075311abd3`, prime-biased weighted union-free problem `mrw-55a8d9eddd2e`, max-fiber antichain skeleton example `mrw-2ff2fe94bc57`, and conditional max-fiber mass proposition `mrw-54968b07a069` are promoted.  The next target for weighted finite-prime fiber problem `mrw-c5a954e7138b` is proving a structural decomposition for \(U_k(\theta)\to0\) beyond max-fiber antichain skeletons, or constructing a genuine obstruction, then lifting from \(M_P(\theta)\) to \(R_P(\theta)\).

## Next Advisor Review Trigger

- Run a full Advisor Gate at the start of each research-only sprint.
- Reject attempts to sum the unshifted \(R_I\), reprove the activation-scale \(Q_I\) bound, reprove the first-cycle entropy \(Q_I\) bound, or return to #25 without a projection invariant; reject \(P_1/P_n\), routine \(s=9\), Gamma-only obstruction chasing, staging, GitHub, and Gmail routes unless explicitly requested by the user.
- Oracle/ChatGPT should be used for heavy proof exploration only when tooling is executable in the active host.
- If live Oracle fails again, require a concrete local plan before further computation.

## Next Continuation Target

\[
U_k(\theta)=
\sup\{\nu_{P_k}(\mathcal F):\mathcal F\subseteq H_{k,\theta},\ \mathcal F\text{ union-free}\}\to0
\]
for every fixed \(0\le\theta<1\).  If proved, use `mrw-b4075311abd3` and `mrw-3c39ca3d1973` to conclude \(M_{P_k}(\theta)\to0\), then isolate the lift to the exponent-grid prefix-rank residual
\[
R_P(\theta)=
\delta_P\int_1^\infty
\bigl(g_P(t)-L_{P,\theta}(t)\bigr)_+t^{-2}\,dt.
\]
The max-fiber antichain skeleton diagnostic is closed conditionally by `mrw-54968b07a069`.  The next subtarget is a structural decomposition/compression theorem reducing any positive-mass union-free family to antichain-like max-fiber pieces plus negligible rank-layer/fixed-core residues, or a positive-mass high-support union-free counterexample outside all quarantined templates.  If the theorem fails, construct the counterexample explicitly and test whether full non-union pair-link intervals still force a triple; the counterexample must not be rank-only, a fixed finite-core cylinder, upward-closed, exact-rank-layer-like, or a max-fiber antichain skeleton.  Do not repeat the binary-choice proof except as a dependency.  Do not use plain ambient random-triple density, uniform cardinality bounds alone, global boundary-smallness, or fixed \(P=\{2,3,5\}\) table extension as terminal evidence.

Do not return to Erdos #25 residue-tail continuity unless a new projection-balance or projection-energy invariant is introduced.  Do not run routine \(s=9\), \(P_1/P_n\), Gamma-only, staging, GitHub, Gmail, or author-contact workflows.  The next loop should still run Scout and Oracle where applicable, but use literal `--prompt` text with Oracle CLI 0.12.1 because `-p "@file"` is not expanded in this host.  Every raw response remains advisory until Student/Librarian audit and explicit wiki patching.

## Latest Strategy Update: 20260519T113424Z

- New local structural result: `mrw-265ec9f57561` proves that for fixed \(0<\theta<1\), subcritical moving-fiber antichain-cover width forces \(\nu_k(\mathcal F_k\cap H_{k,\theta})\to0\).
- The max-fiber antichain skeleton quarantine is now stronger: positive-mass high-support union-free counterexamples must have weighted antichain-cover width at least on the order of \(\sqrt{S_k}\) across moving maximum fibers.
- The next strategy is not to extend fixed \(P=\{2,3,5\}\) tables and not to repeat skeleton tests.  It is to prove a weighted fiber-width/compression/container/junta theorem for union-free families under \(\nu_{P_k}\), or to construct a broad-fiber positive-mass union-free counterexample.
- The \(0<\theta<1\) case has the clean criterion.  The \(\theta=0\) endpoint remains more delicate because low-maximum fibers can matter when antichain-cover widths grow.
- Latest Oracle status: dry-run/files-report works with literal prompt text and forward-slash paths; live browser mode failed with `Attachments never reached a clickable send button before timeout.`  Future loops should keep Oracle bounded and record exact blockers before continuing locally.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through the weighted union-free problem by either proving subcritical max-fiber antichain-cover width for all prime-biased high-support union-free families, or constructing a genuine broad-fiber counterexample.  Start with `mrw-265ec9f57561`, `mrw-54968b07a069`, `mrw-b4075311abd3`, and `mrw-55a8d9eddd2e`.  A successful proof should then pass through the lower-shadow and pair-link bridge to \(M_{P_k}(\theta)\to0\), followed by a separate lift to the exponent-grid residual \(R_P(\theta)\).  A refutation must be explicit and must survive the existing quarantines: not rank-only, not fixed-core, not upward-closed, not exact-rank-layer-like, not a max-fiber antichain skeleton, and not subcritical fiber-width.

## Latest Strategy Update: 20260519T121424Z

- New local route-kill: `mrw-8fcc1c2c5cda` proves ordinary unrestricted \(ij\)-shifts do not preserve union-free families.  The witness is \(\{\{1\},\{1,2\},\{3\}\}\), whose \(S_{2,3}\)-shift contains the union triple \(\{1\}\cup\{2\}=\{1,2\}\).
- The witness is in the useful prime-weighted direction: for \(q_1=1/2,q_2=1/3,q_3=1/5\), the shift changes mass from \(7/15\) to \(8/15\).  Therefore the standard "shift to a left-compressed extremizer" proof template is invalid for `mrw-55a8d9eddd2e`.
- New strategy node `mrw-3474bf5c904f` replaces ordinary compression with union-aware weighted compression, max-fiber/container/junta decomposition, or shift-resistance certificates.  Ad-extremis shifting is a diagnostic only unless it yields a quantitative certificate forcing broad fiber width, a union triple, or a pair-link triple.
- Scout remains raw-only for this cycle because it returned to parked \(s=9\) material.  Oracle was useful as an audit and route recommendation, but only the locally checked counterexample and open-problem refinement were promoted.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 by replacing invalid ordinary weighted shifting with a direct admissible mechanism.  Start with raw log `20260519T121424Z-erdos536-compression-obstruction.md`, counterexample `mrw-8fcc1c2c5cda`, open problem `mrw-3474bf5c904f`, structural width proposition `mrw-265ec9f57561`, union-free target `mrw-55a8d9eddd2e`, and union-free reformulation `mrw-b4075311abd3`.  The preferred route is a max-fiber/container/junta/decomposition theorem under \(\nu_{P_k}(p_i\in S)=1/p_i\) that avoids unrestricted shifts.  If an ad-extremis or union-aware compression is tried, failed shifts must be turned into explicit shift-resistance certificates feeding \(B_k(\theta)\gtrsim\sqrt{S_k}\), a union triple, or the pair-link route `mrw-3c39ca3d1973`.

Do not use ordinary shifted-family normal form as an assumption.  Do not return to fixed-\(P\) table extension, pointwise support-only counts, global boundary-smallness, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact unless explicitly revived.

## Latest Strategy Update: 20260519T125425Z

- New local structural node `mrw-bf35ac1a9ad3` proves the exact core-fiber decomposition for union-free families.  For \(P=Q\sqcup R\), a global union triple decomposes into cross-fiber data
\[
U\cup V=W,
\qquad
A\cup B=C,
\]
with \(A\in\mathcal F_U\), \(B\in\mathcal F_V\), and \(C\in\mathcal F_W\).
- The same node proves each single fiber \(\mathcal F_U\) is union-free, but Oracle correctly flagged that this is not enough globally.  Cross-fiber constraints, not independent fiberwise union-freeness, are the essential structure.
- Oracle also caught and corrected the first local cylinder threshold.  The valid full-core-cylinder obstruction requires two tail coordinates and the size condition
\[
|P\setminus Q|\ge2,
\qquad
|U|+|P\setminus Q|-1>\theta S_P.
\]
- Strategy consequence: exact full high-support core cylinders are not viable terminal containers.  A successful product-measure container or junta theorem must either preserve the cross-fiber union relation or quantify the high-support mass lost by deleting enough two-spare-tail faces.
- Scout remained raw-only because it returned parked polygamma/tail content.  No source theorem was promoted from the Erudition Gate; the literature check only supports the next route choice: rooted hypergraph containers, deletion-trace containers, weighted Kleitman, or product-measure decomposition.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through a quantitative cross-fiber rooted-container/deletion-trace theorem.  Start from `mrw-bf35ac1a9ad3`, `mrw-3474bf5c904f`, `mrw-8fcc1c2c5cda`, `mrw-265ec9f57561`, `mrw-b4075311abd3`, and `mrw-55a8d9eddd2e`.  The next useful lemma should convert many local two-spare-tail constraints
\[
T\cup\{x\},\qquad T\cup\{y\},\qquad T\cup\{x,y\}
\]
into a vanishing bound for \(\nu_{P_k}(\mathcal F\cap H_{k,\theta})\), unless \(\mathcal F\) is concentrated on a rank-layer-like, fixed-core, upward-closed, max-fiber, or other already quarantined negligible skeleton.

If this theorem fails, construct a genuine broad-fiber positive-mass high-support union-free family and test it against the full pair-link route `mrw-3c39ca3d1973`.  Do not use ordinary shifted-family normal form, full-core-cylinder approximation, pointwise support-only counts, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact unless explicitly revived.

## Latest Strategy Update: 20260519T133426Z

- New proved obstruction note `mrw-0d6b8cbd7ced` kills the fixed-depth bounded-deletion version of the two-spare-tail face route.  For every fixed \(d\ge1\), ranks modulo \(d+1\) avoid all union triples whose two deletion sets have sizes at most \(d\), yet each residue class has asymptotic high-support \(\nu_{P_k}\)-mass \(1/(d+1)\).
- The \(d=1\) parity case directly refutes the previous two-spare-tail face supersaturation lemma as a terminal mechanism: parity-rank families avoid every face
\[
T\cup\{x\},\qquad T\cup\{y\},\qquad T\cup\{x,y\}
\]
while carrying asymptotic high-support mass \(1/2\).
- This is not a counterexample to `mrw-55a8d9eddd2e`; rank-congruence families contain full union triples with deletion size \(d+1\) once supports are large.  The obstruction is methodological: fixed-\(d\) local deletion hypergraphs do not have the necessary product-measure supersaturation.
- Strategy consequence: future container work must use unbounded deletion traces, the full union hypergraph, the full pair-link hypergraph, or a mechanism that upgrades bounded-depth resistance to a full union triple.  Do not spend another loop trying to sum only two-spare or bounded-depth local faces.
- Erudition added only route guidance from union-free/container sources.  Scout returned no usable sections and was raw-only.  Oracle audited the obstruction as proved after wording patches.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through an unbounded deletion-trace theorem.  Start from `mrw-0d6b8cbd7ced`, `mrw-bf35ac1a9ad3`, `mrw-55a8d9eddd2e`, `mrw-d0402aea6f58`, `mrw-cc4f876149b7`, `mrw-3c39ca3d1973`, and `mrw-b4075311abd3`.  The next central question is whether positive \(\nu_{P_k}\)-mass inside \(H_{k,\theta}\) forces some deletion trace
\[
\mathcal D_{\mathcal F}(C)=\{D\subseteq C:\ D\ne\varnothing,\ C\setminus D\in\mathcal F\}
\]
to contain two disjoint deletion sets at scales growing with \(S_k\).  If yes, the lower-shadow/union-free route advances toward \(M_{P_k}(\theta)\to0\).  If no, construct the positive-mass family explicitly and test whether full pair-link intervals still force a squarefree cosunflower or whether the obstruction can reverse-lift to \(R_P(\theta)\).

Quarantine fixed-\(d\) bounded-deletion supersaturation as terminal evidence.  Also keep ordinary shifting, full-core-cylinder approximation, pointwise support-only counts, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, and author contact parked unless explicitly revived.

## Latest Strategy Update: 20260519T141427Z

- New proved note `mrw-6a9d1e4f2c8b` kills the trace-local version of the growing-deletion route.  A star deletion trace
\[
\mathcal S_x(C)=\{D\subseteq C:\ x\in D\}
\]
is pairwise intersecting but has fixed deletion mass \(\lambda\) under the auxiliary product deletion law \(\pi_{C,\lambda}\), and keeps asymptotic mass \(\lambda\) on all thresholds \(L_n\le(\lambda-\varepsilon)|C_n|\).
- This is not a counterexample to `mrw-55a8d9eddd2e`; it is a methodological obstruction.  Single-trace intersectingness cannot force vanishing large-deletion mass.  The next theorem must prove that such rooted traces cannot be realized coherently across a positive-mass high-support union-free family, or else produce such a coherent family explicitly.
- Source context from intersecting-family/junta literature is now only vocabulary: stars and finite juntas are the natural local objects, but no external theorem is promoted as a weighted union-free proof.
- Scout is again raw-only because it returned parked \(P_n\)/digamma and \(s=9\) material.  Do not promote the \(s=9\) formula without explicit user revival and separate audit; current strategy rejects routine tail extension.
- Strategy consequence: replace "prove a growing-deletion trace theorem from pairwise-intersecting traces" with "prove a global root-consistency/rooted-container theorem, or use the full pair-link hypergraph."

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through global root consistency for deletion traces.  Start from `mrw-6a9d1e4f2c8b`, `mrw-0d6b8cbd7ced`, `mrw-bf35ac1a9ad3`, `mrw-cc4f876149b7`, `mrw-55a8d9eddd2e`, `mrw-d0402aea6f58`, `mrw-3c39ca3d1973`, and `mrw-b4075311abd3`.  Prove that positive \(\nu_{P_k}\)-mass in \(H_{k,\theta}\) cannot maintain star-like or finite-junta-like deletion traces across many top sets without creating a union triple, or construct the coherent rooted counterexample explicitly and test it against the full pair-link shadow and the \(R_P(\theta)\) lift.

Keep trace-local intersectingness, fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, and author contact parked unless explicitly revived.

## Latest Strategy Update: 20260519T145428Z

- New proved note `mrw-1f7c23e5a9d4` extends the star-trace obstruction from `mrw-6a9d1e4f2c8b` to every fixed finite intersecting junta trace.  For fixed finite \(J\) and pairwise-intersecting \(\mathcal I\subseteq2^J\) with \(\varnothing\notin\mathcal I\), the trace
\[
\mathcal T_{\mathcal I,J}(C)=
\{D\subseteq C:\ D\cap J\in\mathcal I\}
\]
is intersecting and keeps asymptotic deletion mass \(\pi_{J,\lambda}(\mathcal I)\) on all thresholds \(L_n\le(\lambda-\varepsilon)|C_n|\).
- Strategy consequence: a theorem that only classifies individual deletion traces as stars or finite juntas cannot close `mrw-55a8d9eddd2e`.  The missing step is global coherence: roots or finite juntas must be shown impossible to realize across a positive-mass high-support union-free family, or else such a coherent family must be constructed and tested against the full pair-link shadow.
- Rooted-container vocabulary remains source-supported by Balogh--Wagner and general container sources, but no external theorem has been imported as a local prime-biased weighted-union-free result.
- Scout was raw-only and malformed in this cycle.  Focused Oracle was blocked: attachment mode failed with `Attachments never reached a clickable send button before timeout`, and the inline retry returned `You've hit your limit. Please try again later.`

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through global root consistency.  Start from `mrw-1f7c23e5a9d4`, `mrw-6a9d1e4f2c8b`, `mrw-0d6b8cbd7ced`, `mrw-bf35ac1a9ad3`, `mrw-cc4f876149b7`, `mrw-55a8d9eddd2e`, `mrw-d0402aea6f58`, `mrw-3c39ca3d1973`, and `mrw-b4075311abd3`.  Prove that positive \(\nu_{P_k}\)-mass in \(H_{k,\theta}\) cannot maintain positive-mass finite-junta deletion traces coherently across many top sets without creating a union triple, or construct the coherent rooted/finite-junta counterexample explicitly and test it against the full pair-link shadow and the \(R_P(\theta)\) lift.

## Latest Strategy Update: 20260519T161429Z

- Moving finite or growing roots are no longer an automatic escape from the fixed-junta theorem.  Proposition `mrw-a92d7b6e4031` proves the outside-variance version: root visibility gives vanishing mass whenever
\[
W_k(J_k)=\sum_{p_i\notin J_k}\frac1{p_i}\left(1-\frac1{p_i}\right)\to\infty.
\]
- Therefore the surviving positive-mass obstruction must be sharper than "roots escape every fixed finite \(J\)".  It must either have \(W_k(J_k)=O(1)\), so the root sets carry \(V_k-O(1)\) variance, or avoid any global comparable-pair visibility description.
- Scout was ingested raw-only.  The focused Oracle attachment path failed with `Attachments never reached a clickable send button before timeout`; `--browser-inline-files` worked and should be preferred for compact Oracle request files on this host.

## Next Continuation Target: supersedes above


Keep trace-local intersectingness, finite-junta trace-local mass, fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, and author contact parked unless explicitly revived.

## Latest Strategy Update: 20260519T165434Z

- New proved proposition `mrw-4b9f5c2e6a1d` shows that the near-total-root-variance case left by `mrw-a92d7b6e4031` is terminal-equivalent to the original weighted union-free problem.
- The exact visibility supremum with bounded outside variance satisfies \(U_k^{\mathrm{vis},B}(\theta)=U_k(\theta)\) for every \(B\ge0\), since choosing \(J=P_k\) makes visibility automatic.
- Proper-root variants do not repair this by themselves: adding one unused prime coordinate preserves union-freeness and positive mass, gives outside variance \(p_{k+1}^{-1}(1-p_{k+1}^{-1})\to0\), and preserves every lower threshold \(\theta'<\theta\).
- Scout was ingested raw-only because it returned parked polygamma and routine \(s=9\) material.  Focused Oracle completed with `--browser-inline-files` and confirmed the proof with the caveats now included in the node.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 without using near-total-root visibility as a terminal intermediate.  Start from raw log `20260519T165434Z-erdos536-near-total-root-equivalence.md`, proposition `mrw-4b9f5c2e6a1d`, outside-variance proposition `mrw-a92d7b6e4031`, weighted union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, deletion-trace proposition `mrw-cc4f876149b7`, and pair-link criterion `mrw-3c39ca3d1973`.

Primary target: prove the full prime-biased weighted union-free theorem \(U_k(\theta)\to0\) by a non-root-visibility structural invariant, prove a genuinely non-vacuous root-essentiality or anti-padding theorem that cannot be defeated by \(J=P_k\) or one-spare padding, or construct an explicit positive-mass high-support union-free counterexample and test it against full pair-link intervals plus any reverse lift to \(R_P(\theta)\).

Do not use near-total-root visibility, fixed-junta visibility, max-fiber antichain skeletons, fixed-core cylinders, rank-only families, exact-rank-layer-like families, trace-local intersectingness, finite-junta trace-local mass, fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260519T173438Z

- New proved proposition `mrw-7c6a0e9f2d31` kills a natural non-root counterexample template: broad high-support families whose members form a sparse-intersection code.
- The weighted private-shadow inequality is elementary and internal:
\[
\nu_P(\mathcal F)
\le
\frac{\nu_P(|X|=t)}{\binom r t}
\]
whenever every member has size at least \(r\) and all distinct intersections are \(<t\).  Thus for fixed \(0<\gamma<\theta\), any \(\mathcal F_k\subseteq H_{k,\theta}\) with \(|A\cap B|<\gamma S_k\) has vanishing prime-biased mass.
- In a capped band \(\theta S_k<|A|\le\alpha S_k\), \(\alpha<2\theta\), low overlaps force unions and pair-link intervals above the cap, but the private-shadow bound still gives vanishing mass.  Hence low-overlap capped union-free or pair-link-free codes cannot be positive-mass obstructions.
- Scout was ingested raw-only because it drifted to parked polygamma and \(s=9\) material.  The focused Oracle run used `--browser-inline-files`; its response is advisory and should be checked against the node before any future strengthening.

## Next Continuation Target: supersedes above


Primary target: prove that any positive-mass capped high-support union-free or squarefree pair-link-free family with necessarily large intersections yields a non-vacuous clustered-root/container structure, a union triple, or a pair-link hit; or construct an explicit positive-mass high-intersection clustered counterexample and test it against full pair-link intervals plus any reverse lift to \(R_P(\theta)\).

Do not use sparse-intersection code templates, near-total-root visibility, fixed-junta visibility, max-fiber antichain skeletons, fixed-core cylinders, rank-only families, exact-rank-layer-like families, trace-local intersectingness, finite-junta trace-local mass, fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260519T225444Z

- New proved proposition `mrw-18e9c7b0a5af` kills high-intersection clique templates under \(\nu_P(p\in S)=1/p\).
- The proof uses independent samples \(X,Y\sim\nu_P\): if both lie in a \(t\)-intersecting clique with member sizes at least \(t\), then \(|X\cap Y|\ge t\), but \(\mathbb E|X\cap Y|=\sum_{p\in P}p^{-2}=O(1)\). Hence clique mass is at most \((\Sigma_2/t)^{1/2}\).
- Therefore any internally \(\gamma S_k\)-intersecting high-support subfamily has mass \(O_\gamma(S_k^{-1/2})\), and covers by \(o(\sqrt{S_k})\) such cliques vanish.
- Together with `mrw-7c6a0e9f2d31`, the remaining positive-mass obstruction must have mixed overlap-graph structure: no positive-mass low-overlap independent part and no small high-overlap clique cover.
- Scout was raw-only because it drifted to zeta/polygamma and \(s=9\) material. Focused Oracle first failed with Chrome window closed, then the inline retry confirmed the proof with wording caveats now incorporated.

## Next Continuation Target: supersedes above


Primary target: prove that a positive-mass capped high-support union-free or squarefree pair-link-free family whose \(\gamma S_k\)-overlap graph has vanishing measured independent sets and no \(o(\sqrt{S_k})\)-clique cover must contain a union triple or pair-link hit; or construct an explicit positive-mass many-cluster mixed-overlap counterexample and test it against full pair-link intervals plus any reverse lift to \(R_P(\theta)\).

Do not use sparse-intersection code templates, one/few high-intersection clique covers, near-total-root visibility, fixed-junta visibility, max-fiber antichain skeletons, fixed-core cylinders, rank-only families, exact-rank-layer-like families, trace-local intersectingness, finite-junta trace-local mass, fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260519T233444Z

- New proved proposition `mrw-c7f4e0c9a821` adds an entropy invariant to the mixed-overlap route.  If \(\mathcal F\) has \(\nu_P\)-mass \(m>0\), then conditioning on \(\mathcal F\) gives
\[
\mathbb E_{\nu_P(\cdot\mid\mathcal F)^{\otimes2}}|X\cap Y|
\le
4\sum_{p\in P}p^{-2}+2\log(1/m).
\]
- Hence positive-mass high-support families have only \(O(1/S_k)\) conditional edge density in the \(\gamma S_k\)-overlap graph.
- Any cover by internally \(\gamma S_k\)-intersecting clusters now needs \(\Omega(S_k)\) clusters, improving the previous \(o(\sqrt{S_k})\) quarantine from `mrw-18e9c7b0a5af`.
- Scout was raw-only again because it returned routine \(s=9\) inverse-tail material from the zeta manuscript, not an Erdos #536 mixed-overlap candidate.  Focused Oracle confirmed the entropy proof with endpoint and non-overclaim wording now incorporated.

## Next Continuation Target: supersedes above


Primary target: prove that a positive-mass capped high-support union-free or squarefree pair-link-free family whose \(\gamma S_k\)-overlap graph has \(O(1/S_k)\) conditional edge density, no positive-mass independent set, and no \(o(S_k)\)-clique cover must contain a union triple or pair-link hit; or construct an explicit positive-mass linear-many-cluster sparse-overlap counterexample and test full pair-link intervals plus any reverse lift to \(R_P(\theta)\).

Do not use sparse-intersection code templates, one/few or sublinear high-intersection clique covers, near-total-root visibility, fixed-junta visibility, max-fiber antichain skeletons, fixed-core cylinders, rank-only families, exact-rank-layer-like families, trace-local intersectingness, finite-junta trace-local mass, fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260520T010053Z

- New proved corollary `mrw-6d4a8b0f2c91` converts capped random-pair sparsity into endpoint-degree and rectangle sparsity.  In a fixed cap \(\theta S_k<|A|\le\alpha S_k<2\theta S_k\), the capped union relation and the full pair-link relation have total conditional pair measure \(O(S_k^{-1})\), hence no fixed-positive endpoint core and no fixed-positive product rectangle.
- This is a route-kill rather than terminal progress.  It applies to every positive-mass capped family, not specifically to union-free families, so it cannot prove \(U_k(\theta)\to0\).
- Scout completed but returned only the malformed response `The`; it was ingested raw-only.  Focused Oracle completed with `--browser-inline-files` and approved promotion as a corollary after endpoint-inclusive wording was added.

## Next Continuation Target: supersedes above


Primary target: prove a rare-high-overlap pair theorem for
\[
E_k=\{(A,B)\in\mathcal F_k^2:I(A,B)\cap\mathcal F_k\ne\varnothing\},
\qquad
\lambda_k^{\otimes2}(E_k)=O(S_k^{-1}),
\]
showing that positive-mass capped union-free or pair-link-free families cannot hide all relevant structure inside this rare relation; or construct an explicit positive-mass counterexample and test it against full pair-link intervals plus any reverse lift to \(R_P(\theta)\).

Do not use random-pair capped supersaturation, positive endpoint-degree/rectangle supersaturation, sparse-intersection code templates, one/few or sublinear high-intersection clique covers, near-total-root visibility, fixed-junta visibility, max-fiber antichain skeletons, fixed-core cylinders, rank-only families, exact-rank-layer-like families, trace-local intersectingness, finite-junta trace-local mass, fixed-\(d\) bounded deletion, ordinary shifting, full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260520T014549Z

- New proved proposition `mrw-b1f87c9d6a42` shows that rare pair-link sparsity does not imply local absence.  Every exact rank layer \(\binom Pr\), \(2\le r\le |P|-1\), has full genuine pair-link projection via the same-rank swap construction
\[
B=(A\setminus\{x\})\cup\{y\},\qquad
C=(A\setminus\{z\})\cup\{y\}.
\]
- Therefore the full capped band \(\theta S_k<|A|\le\alpha S_k\) has full genuine pair-link projection for all sufficiently large \(k\), even while prior nodes give \(O(S_k^{-1})\) random-pair visibility and no positive endpoint cores or rectangles under their hypotheses.
- This is a route-kill only.  It does not prove \(U_k(\theta)\to0\), does not construct a positive-mass pair-link-free family, and does not lift to \(R_P(\theta)\).
- Scout was raw-only because it returned routine \(s=9\) inverse-tail material, a route the current strategy explicitly rejects as terminal evidence.  Focused Oracle confirmed the finite construction and the non-overclaim boundary using `--browser-inline-files`.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through the sparse pair-link hypergraph, not through
projection-only sparsity.  Start from raw log
proposition `mrw-b1f87c9d6a42`, endpoint/rectangle corollary
`mrw-6d4a8b0f2c91`, capped random-pair corollary `mrw-4f1e9a2d6b73`,
entropy-overlap proposition `mrw-c7f4e0c9a821`, pair-link criterion
`mrw-3c39ca3d1973`, weighted union-free problem `mrw-55a8d9eddd2e`,
lower-shadow problem `mrw-d0402aea6f58`, union-free reformulation
`mrw-b4075311abd3`, and deletion-trace proposition `mrw-cc4f876149b7`.

Primary target: prove a structural theorem showing that positive-mass capped
union-free or squarefree pair-link-free families cannot sit inside a rare
pair-link relation with full or near-full projection, or construct such a
family explicitly and test it against the full pair-link interval criterion and
any reverse lift to \(R_P(\theta)\).

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

## Latest Strategy Update: 20260520T022056Z

- New proved proposition `mrw-25cdd8da0601` gives the first local
  independent-set constraint inside the sparse pair-link hypergraph.  If
  \(\mathcal F\subseteq2^P\) is pair-link-free, \(A\in\mathcal F\), and
  \(y\in P\setminus A\), then
  \[
  D_y^\mathcal F(A)
  =
  \{x\in A:(A\setminus\{x\})\cup\{y\}\in\mathcal F\}
  \]
  has size at most one.
- Consequently the Johnson one-swap neighborhood of \(A\) inside
  \(\mathcal F\) has size at most \(|P\setminus A|\).  This is a structural
  hypergraph-independent-set statement, not projection-only or endpoint-degree
  evidence.
- Oracle confirmed the proof after a compact `--browser-inline-files` retry,
  and flagged the correct caveats: the result controls only same-rank one-swap
  neighbors, not unequal-rank neighborhoods, larger same-rank Hamming-distance
  slices, or dual fixed-deletion fibers; it has no standalone mass consequence.
- Scout was ingested raw-only because the response was malformed and contained
  only source-name fragments.
- The active bridge is now a weighted one-swap expansion theorem: prove that
  any positive-mass high-support pair-link-free/union-free family must create a
  same-insertion collision, or construct a genuine positive-mass low-expansion
  family and test it against the full pair-link interval criterion and the
  \(R_P(\theta)\) lift.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through weighted one-swap expansion.  Start from raw
log
proposition `mrw-25cdd8da0601`, full-band projection proposition
`mrw-b1f87c9d6a42`, endpoint/rectangle corollary `mrw-6d4a8b0f2c91`, capped
random-pair corollary `mrw-4f1e9a2d6b73`, entropy-overlap proposition
`mrw-c7f4e0c9a821`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, and
deletion-trace proposition `mrw-cc4f876149b7`.

Primary target: prove that positive \(\nu_{P_k}\)-mass inside a high-support
cap forces a same-insertion collision
\[
|D_y^\mathcal F(A)|\ge2
\]
for some \(A\in\mathcal F\), \(y\notin A\), unless there is an explicit
positive-mass family with globally low same-insertion one-swap expansion.  If
such a family is constructed, test it against full pair-link intervals and any
reverse lift to \(R_P(\theta)\).

Do not use projection-only sparsity, random-pair capped supersaturation,
positive endpoint-degree/rectangle supersaturation, rank-layer templates,
trace-local or finite-junta trace mass, fixed-depth bounded deletion, ordinary
shifting, full-core-cylinder approximation, global boundary-smallness,
fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work,
Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact as
terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260520T030334Z

- New proved proposition `mrw-354b105d4977` upgrades the one-swap obstruction
  into a common-core link-graph theorem.  For every pair-link-free
  \(\mathcal F\subseteq2^P\) and every \(R\subseteq P\), the graph
  \(G_R^\mathcal F\) on \(P\setminus R\), with edge \(\{x,y\}\) when
  \(R\cup\{x,y\}\in\mathcal F\), is triangle-free.
- Therefore each fixed two-extension slice has at most
  \[
  \left\lfloor |P\setminus R|^2/4\right\rfloor
  \]
  members.  The proof is finite and self-contained: a triangle
  \(xy,xz,yz\) over core \(R\) gives a forbidden triple
  \(R\cup\{x,y\},R\cup\{x,z\},R\cup\{y,z\}\).
- The result is nonterminal.  Complete bipartite slices attain the Mantel
  bound locally, so no prime-biased mass conclusion follows without a
  cross-core theorem.  Dense bipartite slices are now the stress test for any
  proposed expansion/container argument.
- Scout was raw-only because it returned unrelated zeta/Nantomah, \(s=9\), and
  polygamma material.  Focused Oracle confirmed the proof after a corrected
  `--browser-inline-files` retry and warned against summing per-core Mantel
  bounds or treating dense slices as global counterexamples without full
  interval tests.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through weighted cross-core aggregation of
triangle-free two-extension slices.  Start from raw log
proposition `mrw-354b105d4977`, one-swap proposition `mrw-25cdd8da0601`,
full-band projection proposition `mrw-b1f87c9d6a42`, endpoint/rectangle
corollary `mrw-6d4a8b0f2c91`, capped random-pair corollary
`mrw-4f1e9a2d6b73`, entropy-overlap proposition `mrw-c7f4e0c9a821`,
pair-link criterion `mrw-3c39ca3d1973`, weighted union-free problem
`mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, union-free
reformulation `mrw-b4075311abd3`, and deletion-trace proposition
`mrw-cc4f876149b7`.

Primary target: prove that positive \(\nu_{P_k}\)-mass inside a high-support
band forces incoherent dense triangle-free two-extension slices, hence a full
pair-link interval hit, or construct an explicit coherent positive-mass
dense-slice counterexample and test it against all full pair-link intervals
plus any reverse lift to \(R_P(\theta)\).

Do not use projection-only sparsity, random-pair capped supersaturation,
positive endpoint-degree/rectangle supersaturation, rank-layer templates,
trace-local or finite-junta trace mass, fixed-depth bounded deletion, ordinary
shifting, full-core-cylinder approximation, global boundary-smallness,
fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work,
Erdos #25 residue-tail work, staging, GitHub, Gmail, or author contact as
terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260520T102016Z

- New proved proposition `mrw-a32a6d3a5f20` gives the first weighted
  cross-core aggregation of the triangle-free two-extension slice theorem.  For
  any product law with odds \(a_p=q_p/(1-q_p)\),
  \[
  \sum_{A\in\mathcal F}\binom{|A|}{2}\nu(A)
  \le
  \frac14\sum_{R\subseteq P}\nu(R)
  \left(\sum_{p\notin R}a_p\right)^2
  \]
  for every pair-link-free \(\mathcal F\).
- In the prime-biased law this becomes
  \[
  \sum_{A\in\mathcal F}\binom{|A|}{2}\nu_P(A)
  \le
  \frac14\left(S_P^2+\sum_{p\in P}\frac1{p^2(p-1)}\right).
  \]
  Hence the pure weighted-Mantel aggregation route gives only a constant
  high-support mass ceiling, asymptotically \(1/(2\theta^2)\), and cannot be
  terminal.
- This theorem is route-positive but also a route boundary: local Mantel and
  its direct weighted cross-core sum are now exhausted.  The next useful
  theorem must find a Mantel-defect or stability/coherence gain across nearby
  cores, reducing the aggregate from \(S_P^2/4\) to \(o(S_P^2)\), or else build
  a near-extremal coherent dense-slice construction and test every full
  pair-link interval.
- The result is pair-link-specific.  It should not be used as a theorem for
  arbitrary union-free families, because union-free families need not have
  triangle-free two-extension slice graphs.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through cross-core Mantel-defect/stability after the
weighted aggregation theorem.  Start from raw log
proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, one-swap proposition `mrw-25cdd8da0601`, full-band
projection proposition `mrw-b1f87c9d6a42`, endpoint/rectangle corollary
`mrw-6d4a8b0f2c91`, capped random-pair corollary `mrw-4f1e9a2d6b73`,
entropy-overlap proposition `mrw-c7f4e0c9a821`, pair-link criterion
`mrw-3c39ca3d1973`, weighted union-free problem `mrw-55a8d9eddd2e`,
lower-shadow problem `mrw-d0402aea6f58`, union-free reformulation
`mrw-b4075311abd3`, and deletion-trace proposition `mrw-cc4f876149b7`.

Primary target: prove a cross-core Mantel-defect or stability/coherence theorem
showing that positive-mass high-support pair-link-free families cannot have
\[
\sum_R\nu(R)M_R(\mathcal F)\asymp S_P^2
\]
without incompatible near-bipartitions and hence a full pair-link interval hit;
or construct an explicit coherent near-extremal dense-slice family and test it
against every full pair-link interval plus any reverse lift to \(R_P(\theta)\).

Do not use direct weighted-Mantel aggregation, projection-only sparsity,
random-pair capped supersaturation, positive endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-\(P\) table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging,
GitHub, Gmail, or author contact as terminal evidence unless explicitly
revived.

## Latest Strategy Update: 20260521T001014Z

- New proved proposition `mrw-c7c76faed872` classifies fixed complete
  bipartite blow-ups.  For fixed disjoint nonempty \(X,Y\), the blow-up
  \[
  \{R\cup\{x,y\}:R\in\mathcal R,\ x\in X,\ y\in Y\}
  \]
  is pair-link-free if and only if the core family \(\mathcal R\) is
  pair-link-free.  Product-measure mass and high-support mass factor exactly
  through the core with multiplier \(\alpha_X\alpha_Y\) and support shift
  \(+2\).
- New proved proposition `mrw-fced7420b905`, promoted from a locally audited
  Scout patch, gives nested path-shadow coherence:
  \[
  Q\subseteq R\quad\Longrightarrow\quad
  E_Q^\mathcal F\cap P_2(G_R^\mathcal F)=\varnothing.
  \]
  Hence upper complete bipartite blocks force lower graphs to respect the same
  bipartition, and multiple upper bipartitions restrict lower edges to
  complementary signature classes.
- The direct fixed-product construction is therefore quarantined as a terminal
  counterexample route, but changing or incompatible bipartitions remain the
  live frontier.  This is still squarefree support-level progress only; no
  \(M_{P_k}(\theta)\), \(U_k(\theta)\), or \(R_P(\theta)\) vanishing theorem is
  claimed.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through changing-bipartition/core compatibility for
dense complete-bipartite slice assemblies.  Start from raw log
new propositions `mrw-c7c76faed872` and `mrw-fced7420b905`, previous
complete-bipartite stress test `mrw-f83b56a1aa89`, path-shadow bottleneck
`mrw-c6d0c6fa4d30`, path-shadow proposition `mrw-2bcc2955fe38`, weighted
Mantel proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, source note
`references/sources/20260521T001014Z-complete-bipartite-blowup-coherence-context.md`,
Oracle response
if present.

Primary target: prove a quantitative compatibility theorem showing that
positive-mass high-support pair-link-free families must generate enough
incompatible upper bipartitions that the complementary-signature lower slices
become negligible or force a full pair-link interval hit; or construct a
genuine non-product coherent dense-slice family and test every full pair-link
interval plus any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260521T052939Z

- New proved proposition `mrw-750fb7a7e30c` gives a signed graph consistency
  test for robust side-overlap graphs of near-complete corridors.  Robust
  same-side overlap edges impose equality of selected inherited signatures;
  robust cross-side overlap edges impose complementarity.
- Every fully robust cycle has even total side parity.  Equivalently, an
  odd-parity cycle contains an edge whose overlap is at most the sum of the
  relevant near-purity defects.  In the complete case, such a cycle must have
  a zero-weight tested overlap.
- Scout returned a useful family-overlap sketch but was ingested raw-only at
- Focused Oracle failed because the Chrome window closed before completion;
  the blocker is recorded at
- The route is still nonterminal.  The missing global ingredient is a theorem
  producing robust odd-parity corridor-overlap cycles from positive
  high-support mass, or a full construction and pair-link audit of the
  parity-consistent signature-tree normal form.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through signed corridor-overlap parity.  Start from
raw log
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

Primary target: prove that positive high-support pair-link-free mass creates
a robust odd-parity corridor-overlap cycle, or construct a parity-consistent
coherent signature-tree assembly and test every full pair-link interval plus
any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\),
\(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub,
Gmail, or author contact as terminal evidence unless explicitly revived.


## Latest Strategy Update: 20260521T045012Z

- New proved proposition `mrw-206678825c7a` turns near-purity into an
  overlap-packing constraint.  If two near-complete inherited-signature
  corridors share a common weight system, then incompatible selected
  signatures can overlap only by the sum of their side defects.  For example,
  \[
  \tau_1\ne\tau_2
  \quad\Longrightarrow\quad
  w(U_1\cap U_2)\le
  (1-\lambda_1)A_1+(1-\lambda_2)A_2.
  \]
  The same proof gives the \(W_1\cap W_2\), \(U_1\cap W_2\), and
  \(W_1\cap U_2\) compatibility tests.
- Scout returned only malformed source fragments and was ingested raw-only at
- Focused Oracle could not run because ChatGPT reported a usage-limit blocker.
  The promoted proof is a local audit depending only on `mrw-36595780824f`.
- The route is still nonterminal.  The missing global ingredient is a theorem
  that positive high-support pair-link-free mass creates many near-complete
  corridors with enough overlapping side mass for the packing bound to bite.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through global corridor-family incompatibility.
Start from raw log
new proposition `mrw-206678825c7a`, near-complete ancestor-signature
proposition `mrw-36595780824f`, endpoint-patched near-full proposition
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
`theory/forage/responses/20260521T044659Z-erdos536-global-near-purity-incompatibility-response.md`,
and Oracle response

Primary target: prove that positive-mass high-support pair-link-free families
generate many near-complete inherited-signature corridors with enough
overlapping side mass that `mrw-206678825c7a` forces accumulated defect, or
construct a coherent signature-tree assembly and test every full pair-link
interval plus any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\),
\(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging, GitHub,
Gmail, or author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260521T040944Z

- New proved proposition `mrw-36595780824f` gives the near-complete
  ancestor-signature purity theorem:
  \[
  M_Q(U,W)\le\sum_\tau A_\tau B_{\bar\tau},
  \]
  and if \(M_Q(U,W)\ge\lambda AB\) for \(1/2\le\lambda\le1\), then some
  complementary inherited signature pair satisfies
  \[
  A_{\tau^*}\ge\lambda A,\qquad
  B_{\bar\tau^*}\ge\lambda B.
  \]
- The equality case recovers positive-support completeness and exact
  ancestor-signature purity.
- Focused Oracle passed the theorem and identified the \(\lambda=1/2\)
  arbitrary-maximizer tie issue; the proof was patched here and in
  `mrw-8a0c228a0166`.
- Scout returned only `CAND` and was ingested raw-only at
- The route remains nonterminal: it proves no \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or \(R_P(\theta)\) lift.  It gives the quantitative
  local filter needed before a global positive-mass incompatibility theorem.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through global incompatibility of near-complete
coherent-corridor assemblies.  Start from raw log
new proposition `mrw-36595780824f`, endpoint-patched near-full proposition
`mrw-8a0c228a0166`, exact ancestor-signature proposition `mrw-49eaa53e7ffe`,
coherent-normal-form proposition `mrw-827094b15843`, corridor-refinement
proposition `mrw-a9efecc818c7`, signature-fragmentation proposition
`mrw-816fd32c3294`, nested coherence proposition `mrw-fced7420b905`, fixed
blow-up proposition `mrw-c7c76faed872`, complete-bipartite stress test
`mrw-f83b56a1aa89`, path-shadow bottleneck `mrw-c6d0c6fa4d30`, path-shadow
proposition `mrw-2bcc2955fe38`, weighted Mantel proposition
`mrw-a32a6d3a5f20`, two-extension slice proposition `mrw-354b105d4977`,
pair-link criterion `mrw-3c39ca3d1973`, weighted union-free problem
`mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, union-free
reformulation `mrw-b4075311abd3`, Scout ingestion
`theory/forage/responses/20260521T040659Z-erdos536-near-complete-ancestor-signature-purity-response.md`,
and Oracle response

Primary target: prove that positive-mass high-support pair-link-free families
must generate incompatible near-purity requirements across many coherent
corridors, or construct a coherent signature-tree assembly and test every full
pair-link interval plus any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260521T033055Z

- New proved proposition `mrw-49eaa53e7ffe` gives the ancestor-signature purity
  test for complete lower corridors.  If nested upper complete bipartite blocks
  define signatures on a common \(V\), then every complete lower corridor
  \(K_{U,W}\subseteq G_Q^\mathcal F[V]\) lies in one complementary signature
  pair:
  \[
  U\subseteq V_\tau,\qquad
  W\subseteq V_{\mathbf 1-\tau}.
  \]
- The weighted equality version applies to the positive-weight support when
  the lower edge mass across \(U|W\) equals the full product side mass.
- Scout returned only `I` and was ingested raw-only at
- Focused Oracle confirmed the proof after the \(m\ge1\) wording and dependency
  cleanup.  The response remains advisory.
- The route is nonterminal: it still proves no \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or \(R_P(\theta)\) lift.  Its value is a sharper
  assembly filter for coherent normal-form corridors.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through inherited ancestor-signature incompatibility
for coherent-corridor assemblies.  Start from raw log
new proposition `mrw-49eaa53e7ffe`, coherent-normal-form proposition
`mrw-827094b15843`, near-full corridor proposition `mrw-8a0c228a0166`,
corridor-refinement proposition `mrw-a9efecc818c7`, signature-fragmentation
proposition `mrw-816fd32c3294`, nested coherence proposition
`mrw-fced7420b905`, fixed blow-up proposition `mrw-c7c76faed872`,
complete-bipartite stress test `mrw-f83b56a1aa89`, path-shadow bottleneck
`mrw-c6d0c6fa4d30`, path-shadow proposition `mrw-2bcc2955fe38`, weighted
Mantel proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, Scout
`theory/forage/responses/20260521T032658Z-erdos536-coherent-corridor-assembly-response.md`,
and Oracle response

Primary target: prove that positive-mass high-support pair-link-free families
must generate incompatible inherited ancestor signatures across many coherent
normal-form corridors, or construct a coherent signature-tree assembly and
test every full pair-link interval plus any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260521T033055Z

- New proved proposition `mrw-49eaa53e7ffe` gives the ancestor-signature purity
  test for complete lower corridors.  If nested upper complete bipartite blocks
  define signatures on a common \(V\), then every complete lower corridor
  \(K_{U,W}\subseteq G_Q^\mathcal F[V]\) lies in one complementary signature
  pair:
  \[
  U\subseteq V_\tau,\qquad
  W\subseteq V_{\mathbf 1-\tau}.
  \]
- The weighted equality version applies to the positive-weight support when
  the lower edge mass across \(U|W\) equals the full product side mass.
- Scout returned only `I` and was ingested raw-only at
- Focused Oracle confirmed the proof after the \(m\ge1\) wording and dependency
  cleanup.  The response remains advisory.
- The route is nonterminal: it still proves no \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or \(R_P(\theta)\) lift.  Its value is a sharper
  assembly filter for coherent normal-form corridors.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through inherited ancestor-signature incompatibility
for coherent-corridor assemblies.  Start from raw log
new proposition `mrw-49eaa53e7ffe`, coherent-normal-form proposition
`mrw-827094b15843`, near-full corridor proposition `mrw-8a0c228a0166`,
corridor-refinement proposition `mrw-a9efecc818c7`, signature-fragmentation
proposition `mrw-816fd32c3294`, nested coherence proposition
`mrw-fced7420b905`, fixed blow-up proposition `mrw-c7c76faed872`,
complete-bipartite stress test `mrw-f83b56a1aa89`, path-shadow bottleneck
`mrw-c6d0c6fa4d30`, path-shadow proposition `mrw-2bcc2955fe38`, weighted
Mantel proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, Scout
`theory/forage/responses/20260521T032658Z-erdos536-coherent-corridor-assembly-response.md`,
and Oracle response

Primary target: prove that positive-mass high-support pair-link-free families
must generate incompatible inherited ancestor signatures across many coherent
normal-form corridors, or construct a coherent signature-tree assembly and
test every full pair-link interval plus any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260521T033055Z

- New proved proposition `mrw-49eaa53e7ffe` gives the ancestor-signature purity
  test for complete lower corridors.  If nested upper complete bipartite blocks
  define signatures on a common \(V\), then every complete lower corridor
  \(K_{U,W}\subseteq G_Q^\mathcal F[V]\) lies in one complementary signature
  pair:
  \[
  U\subseteq V_\tau,\qquad
  W\subseteq V_{\mathbf 1-\tau}.
  \]
- The weighted equality version applies to the positive-weight support when
  the lower edge mass across \(U|W\) equals the full product side mass.
- Scout returned only `I` and was ingested raw-only at
- Focused Oracle confirmed the proof after the \(m\ge1\) wording and dependency
  cleanup.  The response remains advisory.
- The route is nonterminal: it still proves no \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or \(R_P(\theta)\) lift.  Its value is a sharper
  assembly filter for coherent normal-form corridors.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through inherited ancestor-signature incompatibility
for coherent-corridor assemblies.  Start from raw log
new proposition `mrw-49eaa53e7ffe`, coherent-normal-form proposition
`mrw-827094b15843`, near-full corridor proposition `mrw-8a0c228a0166`,
corridor-refinement proposition `mrw-a9efecc818c7`, signature-fragmentation
proposition `mrw-816fd32c3294`, nested coherence proposition
`mrw-fced7420b905`, fixed blow-up proposition `mrw-c7c76faed872`,
complete-bipartite stress test `mrw-f83b56a1aa89`, path-shadow bottleneck
`mrw-c6d0c6fa4d30`, path-shadow proposition `mrw-2bcc2955fe38`, weighted
Mantel proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, Scout
`theory/forage/responses/20260521T032658Z-erdos536-coherent-corridor-assembly-response.md`,
and Oracle response

Primary target: prove that positive-mass high-support pair-link-free families
must generate incompatible inherited ancestor signatures across many coherent
normal-form corridors, or construct a coherent signature-tree assembly and
test every full pair-link interval plus any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260521T005033Z

- New proved proposition `mrw-816fd32c3294` gives the quantitative
  signature-fragmentation bound for nested bipartite slice blocks:
  \[
  M_Q(V)\le\sum_{\{\tau,\bar\tau\}}W_\tau W_{\bar\tau}
  \le\frac{\rho}{2}W^2.
  \]
- This turns `mrw-fced7420b905` from a qualitative compatibility statement
  into a dichotomy.  Either many upper bipartitions fragment the lower
  signature weights and force small lower edge mass, or a heavy complementary
  signature corridor survives.
- Scout returned the explicitly rejected routine \(s=9\) inverse-tail route
  No Scout claim was promoted.
- Focused Oracle confirmed the local proof after the explicit \(W>0\) caveat;
  the response remains an advisory audit artifact.
- The theorem is nonterminal: it does not prove \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or an \(R_P(\theta)\) lift.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through the heavy-corridor side of the
signature-fragmentation dichotomy.  Start from raw log
new proposition `mrw-816fd32c3294`, nested coherence proposition
`mrw-fced7420b905`, fixed blow-up proposition `mrw-c7c76faed872`,
complete-bipartite stress test `mrw-f83b56a1aa89`, path-shadow bottleneck
`mrw-c6d0c6fa4d30`, path-shadow proposition `mrw-2bcc2955fe38`, weighted
Mantel proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, source note
`references/sources/20260521T005033Z-signature-fragmentation-context.md`,
`theory/forage/responses/20260521T004656Z-erdos536-signature-rank-dichotomy-response.md`,
and focused Oracle response
if present.

Primary target: prove that positive-mass high-support pair-link-free families
must generate enough genuinely independent upper bipartitions to fragment
every lower signature partition, or show that any surviving heavy
complementary signature corridor reduces to a fixed/coherent blow-up already
quarantined by `mrw-c7c76faed872`.  If neither holds, construct an explicit
non-product dense-slice family and test every full pair-link interval plus any
possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260521T021237Z

- New proved proposition `mrw-8a0c228a0166` gives the near-equality
  concentration case of the corridor-refinement bound:
  \[
  M_Q(A,B)\le
  W_AW_B\sum_\omega p_\omega q_{\bar\omega}.
  \]
- If \(M_Q(A,B)\ge\lambda W_AW_B\) for \(1/2\le\lambda\le1\), then one
  complementary refined-signature pair carries at least a \(\lambda\)-fraction
  of both side weights:
  \[
  \alpha_{\omega_0}\ge\lambda W_A,\qquad
  \beta_{\bar\omega_0}\ge\lambda W_B.
  \]
  Equality gives true refined-signature purity on the positive-weight support.
- Scout returned off-route polygamma/zeta-tail candidates and was ingested
  promoted.
- Focused Oracle confirmed the proof and warned against describing the
  near-full case as full purity.
- The result is nonterminal: it does not prove \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or an \(R_P(\theta)\) lift.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through global dominant-pair exhaustion for heavy
signature corridors.  Start from raw log
new proposition `mrw-8a0c228a0166`, previous corridor-refinement proposition
`mrw-a9efecc818c7`, signature fragmentation proposition `mrw-816fd32c3294`,
nested coherence proposition `mrw-fced7420b905`, fixed blow-up proposition
`mrw-c7c76faed872`, complete-bipartite stress test `mrw-f83b56a1aa89`,
path-shadow bottleneck `mrw-c6d0c6fa4d30`, path-shadow proposition
`mrw-2bcc2955fe38`, weighted Mantel proposition `mrw-a32a6d3a5f20`,
two-extension slice proposition `mrw-354b105d4977`, pair-link criterion
`mrw-3c39ca3d1973`, weighted union-free problem `mrw-55a8d9eddd2e`,
lower-shadow problem `mrw-d0402aea6f58`, union-free reformulation
`mrw-b4075311abd3`, source note
`references/sources/20260521T021237Z-near-full-corridor-purity-context.md`,
`theory/forage/responses/20260521T020657Z-erdos536-anti-alignment-exhaustion-response.md`,
and Oracle response

Primary target: prove that repeated dominant complementary refined-signature
pairs cannot persist at positive high-support mass without either losing
corridor capacity or collapsing into a rigid fixed/coherent corridor normal
form; or construct that normal form and test every full pair-link interval plus
any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260521T012914Z

- New proved proposition `mrw-a9efecc818c7` gives the corridor-refinement
  bound:
  \[
  M_Q(A,B)\le
  \sum_{\omega\in\{0,1\}^{\ell}}\alpha_\omega\beta_{\bar\omega}.
  \]
- In the one-cut case, the permitted capacity is exactly
  \[
  \alpha_0\beta_1+\alpha_1\beta_0
  =
  W_AW_B-(\alpha_0\beta_0+\alpha_1\beta_1).
  \]
  Thus same-side refined product is the capacity lost by the new cut.
- Scout returned malformed source-fragment text and was ingested raw-only at
- Focused Oracle confirmed the proof after a retry and notation cleanup.  The
  response remains advisory.
- The result is nonterminal: it does not prove \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or an \(R_P(\theta)\) lift.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through global anti-alignment exhaustion for heavy
signature corridors.  Start from raw log
new proposition `mrw-a9efecc818c7`, previous proposition `mrw-816fd32c3294`,
nested coherence proposition `mrw-fced7420b905`, fixed blow-up proposition
`mrw-c7c76faed872`, complete-bipartite stress test `mrw-f83b56a1aa89`,
path-shadow bottleneck `mrw-c6d0c6fa4d30`, path-shadow proposition
`mrw-2bcc2955fe38`, weighted Mantel proposition `mrw-a32a6d3a5f20`,
two-extension slice proposition `mrw-354b105d4977`, pair-link criterion
`mrw-3c39ca3d1973`, weighted union-free problem `mrw-55a8d9eddd2e`,
lower-shadow problem `mrw-d0402aea6f58`, union-free reformulation
`mrw-b4075311abd3`, source note
`references/sources/20260521T012914Z-corridor-refinement-context.md`, Scout
`theory/forage/responses/20260521T012656Z-erdos536-heavy-signature-corridor-classification-response.md`,
and Oracle response

Primary target: prove that positive-mass high-support pair-link-free families
cannot maintain weighted anti-alignment across enough nested upper cuts, so
every heavy corridor eventually fragments; or construct a persistent
anti-aligned non-product dense-slice family and test every full pair-link
interval plus any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260521T001014Z

- New proved proposition `mrw-c7c76faed872` classifies fixed complete
  bipartite blow-ups.  For fixed disjoint nonempty \(X,Y\), the blow-up
  \[
  \{R\cup\{x,y\}:R\in\mathcal R,\ x\in X,\ y\in Y\}
  \]
  is pair-link-free if and only if the core family \(\mathcal R\) is
  pair-link-free.  Product-measure mass and high-support mass factor exactly
  through the core with multiplier \(\alpha_X\alpha_Y\) and support shift
  \(+2\).
- New proved proposition `mrw-fced7420b905`, promoted from a locally audited
  Scout patch, gives nested path-shadow coherence:
  \[
  Q\subseteq R\quad\Longrightarrow\quad
  E_Q^\mathcal F\cap P_2(G_R^\mathcal F)=\varnothing.
  \]
  Hence upper complete bipartite blocks force lower graphs to respect the same
  bipartition, and multiple upper bipartitions restrict lower edges to
  complementary signature classes.
- The direct fixed-product construction is therefore quarantined as a terminal
  counterexample route, but changing or incompatible bipartitions remain the
  live frontier.  This is still squarefree support-level progress only; no
  \(M_{P_k}(\theta)\), \(U_k(\theta)\), or \(R_P(\theta)\) vanishing theorem is
  claimed.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through changing-bipartition/core compatibility for
dense complete-bipartite slice assemblies.  Start from raw log
new propositions `mrw-c7c76faed872` and `mrw-fced7420b905`, previous
complete-bipartite stress test `mrw-f83b56a1aa89`, path-shadow bottleneck
`mrw-c6d0c6fa4d30`, path-shadow proposition `mrw-2bcc2955fe38`, weighted
Mantel proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, source note
`references/sources/20260521T001014Z-complete-bipartite-blowup-coherence-context.md`,
Oracle response
if present.

Primary target: prove a quantitative compatibility theorem showing that
positive-mass high-support pair-link-free families must generate enough
incompatible upper bipartitions that the complementary-signature lower slices
become negligible or force a full pair-link interval hit; or construct a
genuine non-product coherent dense-slice family and test every full pair-link
interval plus any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.

## Latest Strategy Update: 20260520T114136Z

- New proved proposition `mrw-c6d0c6fa4d30` turns the path-shadow exclusion into
  a product-measure bottleneck.  For fixed endpoints \(x,z\), endpoint-pair core
  \(\mathcal E_{xz}\), and \(y\)-augmented path shadows
  \(\mathcal S^y_{xz}\), pair-link-freeness gives
  \[
  \mathcal E_{xz}\cap\bigcup_y\mathcal S^y_{xz}=\varnothing.
  \]
- For any probability measure \(\mu\), if
  \[
  T=\sum_y\mu(\mathcal S^y_{xz}),\qquad
  Q=\sum_{y,y'}\mu(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz}),
  \]
  where \(Q\) is the ordered double sum including diagonal terms, then
  \[
  \mu\left(\bigcup_y\mathcal S^y_{xz}\right)\ge\frac{T^2}{Q},
  \qquad
  \mu(\mathcal E_{xz})+\frac{T^2}{Q}\le1.
  \]
- Under a product law on \(P\setminus\{x,z\}\), each individual path shadow has
  measure at least the corresponding path-core measure on
  \(P\setminus\{x,y,z\}\), using the two disjoint embedded copies
  \(R\) and \(R\cup\{y\}\).
- This is nonterminal.  Since \(Q\) includes the diagonal, the next useful
  theorem must quantify the off-diagonal intersections
  \(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz}\), or show that large overlap
  collapse itself forces a full pair-link interval hit.
- Scout returned malformed material and pointed back to the explicitly
  rejected routine \(s=9\) tail-floor route; it was ingested raw-only.  Focused
  Oracle confirmed the proof after requiring the diagonal-including wording for
  \(Q\) and safer "path shadow" / "\(y\)-augmented lower shadow" terminology.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 by quantifying path-shadow overlap collapse.  Start
from raw log
new proposition `mrw-c6d0c6fa4d30`, path-shadow proposition
`mrw-2bcc2955fe38`, weighted Mantel proposition `mrw-a32a6d3a5f20`,
two-extension slice proposition `mrw-354b105d4977`, pair-link criterion
`mrw-3c39ca3d1973`, weighted union-free problem `mrw-55a8d9eddd2e`,
lower-shadow problem `mrw-d0402aea6f58`, union-free reformulation
`mrw-b4075311abd3`, deletion-trace proposition `mrw-cc4f876149b7`, source note
`references/sources/20260520T114136Z-path-shadow-overlap-context.md`, Scout
Oracle response

Primary target: prove a prime-biased overlap-collapse theorem for
\[
Q_{xz}=\sum_{y,y'}\mu(\mathcal S^y_{xz}\cap\mathcal S^{y'}_{xz})
\]
showing that large off-diagonal path-shadow overlap forces additional
endpoint-pair deletions, a full pair-link interval hit, or a vanishing
high-support pair-link-free mass contribution; or construct an explicit
positive-mass dense-slice family whose path shadows have massive overlap and
test every full pair-link interval plus any reverse lift to \(R_P(\theta)\).

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, random-pair capped supersaturation, positive
endpoint-degree/rectangle supersaturation, rank-layer templates, trace-local or
finite-junta trace mass, fixed-depth bounded deletion, ordinary shifting,
full-core-cylinder approximation, global boundary-smallness, fixed-\(P\) table
extension, routine \(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25
residue-tail work, staging, GitHub, Gmail, or author contact as terminal
evidence unless explicitly revived.

## Latest Strategy Update: 20260520T110040Z

- New proved proposition `mrw-2bcc2955fe38` gives a cross-core coherence theorem
  for pair-link-free two-extension slices.  If
  \(R\cup\{x,y\}\) and \(R\cup\{y,z\}\) lie in \(\mathcal F\), then every set
  \[
  D\cup\{x,z\},\qquad D\subseteq R\cup\{y\},
  \]
  is excluded from \(\mathcal F\).
- In fixed-endpoint language, the endpoint-pair core family
  \[
  \mathcal E_{xz}=\{D:D\cup\{x,z\}\in\mathcal F\}
  \]
  is disjoint from the \(y\)-augmented lower shadow of the path-core family
  \[
  \mathcal P^y_{xz}=
  \{R:R\cup\{x,y\},R\cup\{y,z\}\in\mathcal F\}.
  \]
- This is the missing cross-core object behind local complete-bipartite
  Mantel extremizers: same-side endpoint pairs in a dense bipartite slice are
  not merely nonedges in that slice; their lower-core edge columns are forbidden
  below every two-edge path.
- The result is nonterminal.  It does not prove \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or a lift to \(R_P(\theta)\), and it does not import any
  external container or stability theorem.
- Scout was again raw-only after malformed source fragments.  Focused Oracle
  first failed because Chrome closed; the compact `--browser-inline-files`
  retry confirmed the proof and recommended path-shadow product-measure
  quantification before any Mantel-defect bookkeeping.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through the path-shadow lower-core obstruction.
Start from raw log
new proposition `mrw-2bcc2955fe38`, weighted Mantel proposition
`mrw-a32a6d3a5f20`, two-extension slice proposition `mrw-354b105d4977`,
pair-link criterion `mrw-3c39ca3d1973`, one-swap proposition
`mrw-25cdd8da0601`, full-band projection proposition `mrw-b1f87c9d6a42`,
entropy-overlap proposition `mrw-c7f4e0c9a821`, weighted union-free problem
`mrw-55a8d9eddd2e`, lower-shadow problem `mrw-d0402aea6f58`, union-free
reformulation `mrw-b4075311abd3`, deletion-trace proposition
`mrw-cc4f876149b7`, source note
`references/sources/20260520T110040Z-cross-core-path-shadow-context.md`,
Scout ingestion
Oracle response

Primary target: prove a prime-biased product-measure lower-shadow theorem for
the path-shadow families
\[
\downarrow_y\mathcal P^y_{xz}
\]
that forces enough endpoint-pair core deletion to create quadratic aggregate
Mantel defect or vanishing high-support pair-link-free mass; or construct an
explicit positive-mass dense-slice family whose path shadows collapse into a
small already-forbidden region, then test every full pair-link interval plus
any reverse lift to \(R_P(\theta)\).

Do not use direct weighted-Mantel aggregation, projection-only sparsity,
random-pair capped supersaturation, positive endpoint-degree/rectangle
supersaturation, rank-layer templates, trace-local or finite-junta trace mass,
fixed-depth bounded deletion, ordinary shifting, full-core-cylinder
approximation, global boundary-smallness, fixed-\(P\) table extension, routine
\(s=9\), \(P_1/P_n\), Gamma-only work, Erdos #25 residue-tail work, staging,
GitHub, Gmail, or author contact as terminal evidence unless explicitly
revived.

## Latest Strategy Update: 20260521T001014Z

- New proved proposition `mrw-c7c76faed872` classifies fixed complete
  bipartite blow-ups.  For fixed disjoint nonempty \(X,Y\), the blow-up
  \[
  \{R\cup\{x,y\}:R\in\mathcal R,\ x\in X,\ y\in Y\}
  \]
  is pair-link-free if and only if the core family \(\mathcal R\) is
  pair-link-free.  Product-measure mass and high-support mass factor exactly
  through the core with multiplier \(\alpha_X\alpha_Y\) and support shift
  \(+2\).
- New proved proposition `mrw-fced7420b905`, promoted from a locally audited
  Scout patch, gives nested path-shadow coherence:
  \[
  Q\subseteq R\quad\Longrightarrow\quad
  E_Q^\mathcal F\cap P_2(G_R^\mathcal F)=\varnothing.
  \]
  Hence upper complete bipartite blocks force lower graphs to respect the same
  bipartition, and multiple upper bipartitions restrict lower edges to
  complementary signature classes.
- The direct fixed-product construction is therefore quarantined as a terminal
  counterexample route, but changing or incompatible bipartitions remain the
  live frontier.  This is still squarefree support-level progress only; no
  \(M_{P_k}(\theta)\), \(U_k(\theta)\), or \(R_P(\theta)\) vanishing theorem is
  claimed.

## Next Continuation Target: supersedes above

Attack Erdos Problem #536 through changing-bipartition/core compatibility for
dense complete-bipartite slice assemblies.  Start from raw log
new propositions `mrw-c7c76faed872` and `mrw-fced7420b905`, previous
complete-bipartite stress test `mrw-f83b56a1aa89`, path-shadow bottleneck
`mrw-c6d0c6fa4d30`, path-shadow proposition `mrw-2bcc2955fe38`, weighted
Mantel proposition `mrw-a32a6d3a5f20`, two-extension slice proposition
`mrw-354b105d4977`, pair-link criterion `mrw-3c39ca3d1973`, weighted
union-free problem `mrw-55a8d9eddd2e`, lower-shadow problem
`mrw-d0402aea6f58`, union-free reformulation `mrw-b4075311abd3`, source note
`references/sources/20260521T001014Z-complete-bipartite-blowup-coherence-context.md`,
Oracle response
if present.

Primary target: prove a quantitative compatibility theorem showing that
positive-mass high-support pair-link-free families must generate enough
incompatible upper bipartitions that the complementary-signature lower slices
become negligible or force a full pair-link interval hit; or construct a
genuine non-product coherent dense-slice family and test every full pair-link
interval plus any possible \(R_P(\theta)\) lift.

Do not use direct weighted-Mantel aggregation, path-shadow disjointness alone,
projection-only sparsity, endpoint-degree/rectangle supersaturation,
rank-layer templates, trace-local or finite-junta trace mass, fixed-depth
bounded deletion, ordinary shifting, full-core-cylinder approximation, global
boundary-smallness, fixed-\(P\) table extension, routine \(s=9\), \(P_1/P_n\),
Gamma-only work, Erdos #25 residue-tail work, staging, GitHub, Gmail, or
author contact as terminal evidence unless explicitly revived.
