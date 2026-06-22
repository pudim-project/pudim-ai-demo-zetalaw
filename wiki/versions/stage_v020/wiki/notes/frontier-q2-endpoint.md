# Frontier: \(n=2\) Beta-Window Endpoint

The staged public node `mrw-e497f41bfc07` reduces Qi--Lim--Nantomah Open Problem 4 to the exceptional \(n=2\) beta window after solving all odd orders and all even orders \(n\ge4\).

Current certified status:
\[
\frac{4629}{2000}<L_2\le\frac{397}{170},
\qquad
\left[\frac{397}{170},3\right]\subseteq\mathcal I_2.
\]

The latest proof route has two viable branches:

- Tail-gate branch: sharpen the Euler--Maclaurin lower gate for \(Z_3(1/x)\) and certify a better rational threshold below \(397/170\).
- Critical-point branch: certify signs of
\[
G(x)=x\log x\,\Lambda(x)-\log R(x)
\]
on rational subintervals of
\[
\left[\frac{1409}{5000},\frac{293}{1000}\right],
\]
then combine this with outside-bracket upper bounds for \(Q_2\).

The first Advisor Attack Plan creates one normal-form critical-point route, one stronger interval-certificate route, and one mixed tail-gate route at \(7/3\).

## Student Update: 2026-05-25

The mixed tail-gate candidate at \(7/3\) is refuted. At
\[
x=\left(\frac{17}{24}\right)^3
\]
an exact rational upper bound for \(Z_3(1/x)\) gives
\[
Z_3(1/x)<\left(\frac{17}{24}\right)^7=x^{7/3}.
\]

Thus the next productive route should prioritize the derivative-sign/critical-point certificate or a more modest tail-gate threshold strictly above \(7/3\). Do not retry the raw \(7/3\) tail inequality as stated.

## Advisor Update: 2026-05-25

The next terminal-node Attack Plan uses `T-not-Q2-seven-thirds-tail-gate` as an overstrong-route obstruction. The \(7/3\) tail threshold is too aggressive, so the tail slot is demoted to a lower-priority diagnostic/progress route at
\[
\frac{404}{173},
\qquad
\frac73<\frac{404}{173}<\frac{397}{170}.
\]

The primary terminal routes are now:

- certify the global critical-point normal form for \(G(x)=x\log x\,\Lambda(x)-\log R(x)\);
- isolate the maximizer by outside-bracket upper bounds for \(Q_2\);
- only if practical, test the relaxed \(404/173\) tail gate using an exact Euler--Maclaurin/Sturm or subdivision certificate.

## Student Update: 2026-05-25, Terminal AP

The relaxed tail gate was proved:
\[
Z_3(1/x)>x^{404/173}\qquad(0<x<1).
\]
Consequently
\[
\left[\frac{404}{173},3\right]\subseteq\mathcal I_2,
\qquad
L_2\le\frac{404}{173}<\frac{397}{170}.
\]

This promotes `T-Q2-tail-404-173-gate` to true and propagates truth to `T-Q2-endpoint-certificate`, since the v2 frontier-progress node only required a strict improvement below \(397/170\). It does not solve `T-Q2-terminal-exact`: the exact value or exact description of \(L_2\) remains open. The critical-zero and outside-bracket candidates remain open after a numerical audit found the expected unique root near
\[
\xi\approx0.2873459296653486204,
\qquad
Q_2(\xi)\approx2.3145474011932263948,
\]
but no exact logarithmic/Hurwitz-zeta interval certificate was completed.

## Advisor Update: 2026-05-25, After \(404/173\)

The next terminal Attack Plan uses the true bound
\[
L_2\le\frac{404}{173}
\]
as strict upper-bound progress, but keeps the exact critical-zero route primary. The new three candidates are:

- a compact-bracket certificate for \(G(x)=x\log x\,\Lambda(x)-\log R(x)\);
- a finite outside-bracket cover for \(Q_2\), now only needing to isolate the true maximum below the proved \(404/173\) ceiling;
- an analytic logarithm-control reduction replacing raw logarithm interval arithmetic by exact integral or rational majorants/minorants.

All three are intended as terminal-solving routes if proved; the tail gate itself is now background progress, not a terminal candidate.

## Advisor Update: 2026-05-25, After Atanh Log Helper

The Student roll did not solve the terminal node, but it promoted a reusable exact logarithm enclosure:
\[
\log r
=2\sum_{k=0}^{m}\frac{z^{2k+1}}{2k+1}+\epsilon_m,
\qquad
z=\frac{r-1}{r+1},
\qquad
|\epsilon_m|\le
\frac{2|z|^{2m+3}}{(2m+3)(1-z^2)}.
\]

The next terminal Attack Plan narrows the proof search around
\[
J=\left[\frac{287345}{1000000},\frac{287346}{1000000}\right],
\]
which contains the numerically observed root of \(G\). The three new candidates are:

- a microinterval Hurwitz-zeta and atanh-log certificate on \(J\);
- a full compact-bracket subdivision proof for \(G\) refined around \(J\);
- an outside-bracket cover for \(Q_2\) using the same exact log-bound helper.

Each candidate is still terminal-solving only if it supplies both the inner witness and the needed global comparison.

## Student Update: 2026-05-25, Atanh/Microinterval AP

The microinterval route remains open. Numerically,
\[
G\left(\frac{287345}{1000000}\right)>0,
\qquad
G\left(\frac{287346}{1000000}\right)<0,
\]
with the right endpoint having the smaller margin, about \(10^{-7}\). The observed root and peak remain
\[
\xi\approx0.2873459296653486204004979496,
\qquad
Q_2(\xi)\approx2.3145474011932263948.
\]

This roll promoted a second exact helper. For rational \(a>0\), integer \(s>1\), and \(N\ge1\),
\[
\sum_{k=0}^{N-1}(a+k)^{-s}+\frac{(a+N)^{1-s}}{s-1}
\le
Z_s(a)
\le
\sum_{k=0}^{N-1}(a+k)^{-s}+\frac{(a+N-1)^{1-s}}{s-1}.
\]

Thus the current local toolset has exact rational enclosures for both logarithms and Hurwitz-zeta tails. The remaining obstacle is an implementation-level rational interval certificate for the nonlinear expressions \(R\), \(\Lambda\), \(G\), and \(Q_2\), plus a finite outside-bracket cover.

## Advisor Update: 2026-05-25, Rational Interval Certificate

The next terminal Attack Plan uses both true local helpers:

- `T-log-atanh-rational-enclosure-lemma` for exact logarithm bounds;
- `T-hurwitz-zeta-integral-tail-enclosure-lemma` for exact Hurwitz-zeta tail bounds.

The three planned routes are:

- a deterministic rational interval-arithmetic certificate for \(R\), \(\Lambda\), \(G\), and \(Q_2\) on
\[
J=\left[\frac{287345}{1000000},\frac{287346}{1000000}\right];
\]
- a focused right-endpoint certificate for the tight inequality
\[
G\left(\frac{287346}{1000000}\right)<0;
\]
- a finite outside-cover proof split into near-zero, finite-middle, and near-one regimes.

Each route is required to preserve a candidate-to-terminal implication path, so a local point sign alone is treated as insufficient unless it is bundled with the compact one-crossing and global comparison data.

## Student Update: 2026-05-25, Rational Interval AP

The fixed-scale rational interval evaluator certified the endpoint signs on
\[
J=\left[\frac{287345}{1000000},\frac{287346}{1000000}\right].
\]
With scale \(10^{70}\), Hurwitz-zeta cutoff \(N=4000\), and atanh truncation \(m=220\), the replayable certificate gives
\[
G\left(\frac{287345}{1000000}\right)
\in
[1.3291193143713952\cdot10^{-6},\;1.3302145207712275\cdot10^{-6}]
\]
and
\[
G\left(\frac{287346}{1000000}\right)
\in
[-1.0114449998779718\cdot10^{-7},\;-1.0004930415540797\cdot10^{-7}].
\]

Thus the endpoint sign change is now a true auxiliary certificate, recorded as `T-Q2-J-endpoint-G-signs-certificate`. The terminal node remains open: a compact one-crossing certificate and a finite outside-cover comparison are still missing. Representative point checks below an inner endpoint witness worked in the finite-middle and near-one regions, but the near-zero regime remains too wide under the current unscaled evaluator.

## Advisor Update: 2026-05-25, Cover Split After Endpoint Signs

The next terminal Attack Plan uses the true endpoint-sign certificate on
\[
J=\left[\frac{287345}{1000000},\frac{287346}{1000000}\right],
\]
plus the true atanh and Hurwitz-zeta enclosure helpers. It splits the remaining work into three routes:

- a compact one-crossing and compact-dominance certificate on
\[
\left[\frac{1409}{5000},\frac{287345}{1000000}\right]
\cup
\left[\frac{287346}{1000000},\frac{293}{1000}\right];
\]
- a near-zero asymptotic or scaled enclosure proving \(Q_2(x)<q_J\), since the unscaled fixed-point evaluator was too wide there;
- a finite-middle and near-one cover proving \(Q_2(x)<q_J\), using the successful representative checks as seeds.

Each candidate remains terminal-solving only if it bundles or supplies the complementary compact and outside-cover data needed to determine \(L_2=Q_2(\xi)\).

## Student Update: 2026-05-25, Cover Split AP

The near-zero part now has a true scaled subcover. For \(0<x\le1/100\),
\[
R(x)>\frac{100}{303}x^2>x^{23/10},
\]
so, because \(\log x<0\),
\[
Q_2(x)<\frac{23}{10}<q_J.
\]
This proves `T-Q2-near-zero-1-100-qJ-cover`.

The compact interval route remains open. A direct variable-interval extension of the fixed-scale evaluator was too wide on compact intervals outside \(J\), even on short diagnostic intervals. The next compact attempt should use smaller adaptive intervals with derivative information or Taylor-model style enclosure rather than raw interval propagation.

The outside-cover problem is reduced: the near-zero interval \((0,1/100]\) is handled, while \([1/100,1)\setminus J\) still needs finite-middle and near-one coverage below \(q_J\).

## Advisor Update: 2026-05-25, Final Cover Mechanisms

The next terminal Attack Plan uses the true near-zero cover
\[
Q_2(x)<q_J\qquad(0<x\le 1/100),
\]
the true endpoint-sign certificate on \(J\), and the true atanh/Hurwitz-zeta enclosure lemmas. It splits the remaining proof mechanisms into:

- a Taylor-model or derivative-bounded compact one-crossing certificate for \(G\) outside \(J\);
- an adaptive finite-middle cover of
\[
\left[\frac{1}{100},\frac{1409}{5000}\right]
\cup
\left[\frac{293}{1000},\frac{9}{10}\right]
\]
below \(q_J\);
- a near-one variable-change cover on \([9/10,1)\), where raw quotient intervals are unstable because \(\log x\) is small.

Each candidate is formulated as terminal-solving only when bundled with the complementary cover pieces needed to determine \(L_2=Q_2(\xi)\).

## Student Update: 2026-05-25, Near-One Cover

The near-one outside region is now covered. A rational subdivision verifier proves
\[
R(x)>1\qquad(9/10\le x<1).
\]
Since \(\log R(x)>0\) and \(\log x<0\), this gives
\[
Q_2(x)<0<q_J
\qquad(9/10\le x<1).
\]

This promotes `T-Q2-near-one-9-10-qJ-cover` to true. Together with the true near-zero cover, the outside-cover work is reduced to
\[
\left[\frac1{100},\frac{1409}{5000}\right]
\cup
\left[\frac{293}{1000},\frac9{10}\right],
\]
plus the compact one-crossing certificate for \(G\) outside \(J\).

## Advisor Update: 2026-05-25, Reduced Middle/Compact Plan

The outside endpoint regimes are now true:
\[
Q_2(x)<q_J\qquad(0<x\le1/100),
\]
and
\[
Q_2(x)<q_J\qquad(9/10\le x<1).
\]

The next Attack Plan reduces the terminal proof to exactly three routes:

- adaptive finite-middle coverage of
\[
\left[\frac1{100},\frac{1409}{5000}\right]
\cup
\left[\frac{293}{1000},\frac9{10}\right];
\]
- derivative/Taylor compact one-crossing and dominance on \([1409/5000,293/1000]\setminus J\);
- a reduced terminal assembly node that combines the two true outside endpoint covers, the endpoint signs on \(J\), and the two remaining certificates.

## Student Update: 2026-05-25, Left-Middle Zeta Subcover

The left finite-middle interval has a new true subcover. For \(0<x<1/2\),
\[
3xZ_4(x)-Z_3(x)
=2x^{-3}+\sum_{k=1}^{\infty}\frac{2x-k}{(x+k)^4}
<2x^{-3}.
\]
Since \(Z_3(x)>x^{-3}\), this gives
\[
R(x)>Z_3(1/x).
\]

A deterministic finite rational subdivision with \(N=4000\) proves
\[
Z_3(1/x)>x^{23/10}
\qquad
\left(1/100\le x\le9/50\right).
\]
Therefore
\[
Q_2(x)<23/10<q_J
\qquad
\left(1/100\le x\le9/50\right),
\]
promoting `T-Q2-left-middle-1-100-9-50-qJ-cover` to true.

The outside-cover frontier is now reduced to
\[
\left[\frac9{50},\frac{1409}{5000}\right]
\cup
\left[\frac{293}{1000},\frac9{10}\right],
\]
plus the compact one-crossing and dominance certificate on
\[
\left[\frac{1409}{5000},\frac{293}{1000}\right]\setminus J.
\]

## Advisor Update: 2026-05-25, Remainder Log/Taylor/Assembly Plan

The next Attack Plan uses the true covers
\[
Q_2(x)<q_J\qquad(0<x\le9/50)
\]
and
\[
Q_2(x)<q_J\qquad(9/10\le x<1),
\]
plus the true endpoint signs on \(J\) and the true atanh/Hurwitz-zeta enclosure lemmas.

It creates three terminal-solving routes:

- a direct-log finite cover of
\[
\left[\frac9{50},\frac{1409}{5000}\right]
\cup
\left[\frac{293}{1000},\frac9{10}\right],
\]
bundled with the compact certificate;
- a Taylor-model or derivative-bounded compact monotonicity certificate on
\[
\left[\frac{1409}{5000},\frac{293}{1000}\right]\setminus J;
\]
- a reduced analytic-denominator assembly that tries to extend the \(D<2x^{-3}\) mechanism before falling back to interval arithmetic.

Scout first-contact is not required for these nodes because they are internal local continuations from the current formula store and true local certificates.

## Student Update: 2026-05-25, Terminal Assembly Solved

The remaining finite-middle outside cover is now certified. A replayable script proves
\[
Q_2(x)<q_J
\]
on
\[
\left[\frac9{50},\frac{1409}{5000}\right]
\cup
\left[\frac{293}{1000},\frac9{10}\right].
\]
It uses an analytic \(R(x)>Z_3(1/x)\) bridge up to \(221050/1000000\), then range-reduced direct-log comparisons
\[
\log R(x)>\frac{115727}{50000}\log x
\]
on the remaining finite-middle intervals.

The compact bracket is also certified. A rational interval cover proves
\[
H(x)=\Lambda(x)+x\Lambda'(x)>0
\qquad
\left(\frac{1409}{5000}\le x\le\frac{293}{1000}\right).
\]
Since \(G'(x)=\log x\,H(x)\), this gives \(G'(x)<0\). Together with the true endpoint signs on \(J\), \(G\) has a unique zero
\[
\xi\in
\left[\frac{287345}{1000000},\frac{287346}{1000000}\right],
\]
and \(Q_2\) attains its global maximum there.

Thus the exact endpoint is determined:
\[
L_2=Q_2(\xi),
\qquad
\mathcal I_2=(Q_2(\xi),3].
\]

The terminal Theory node `T-Q2-terminal-exact` is now true.
