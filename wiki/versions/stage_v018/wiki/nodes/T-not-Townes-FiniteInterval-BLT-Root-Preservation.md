---
id: "T-not-Townes-FiniteInterval-BLT-Root-Preservation"
type: "theorem"
title: "Townes finite-interval BLT root preservation is false"
status: "proved"
tags: ["bilateral-laplace-transform", "counterexample", "finite-interval-complete-monotonicity", "proved", "theorem", "townes", "true-negation"]
parents: ["O-Townes-FiniteInterval-BLT-Root-Counterexample"]
refs: ["oracle/responses/OS-20260609T1650Z-townes-root-preservation-student-oracle-response.md", "raw/student/20260609T1705-townes-root-preservation-counterexample.md"]
---

# Theorem: Townes finite-interval BLT root preservation is false

## Statement

The Townes finite-interval BLT root-preservation statement is false: there exists a real-valued infinitely divisible law with bilateral Laplace transform \(L\) completely monotone on \([0,1]\), but \(L^{1/100}\) is not completely monotone on \([0,1]\).

## Dependencies

- [[wiki/nodes/O-Townes-FiniteInterval-BLT-Root-Counterexample|Townes finite-interval BLT root-preservation counterexample]]

## Proof and provenance references

- `oracle/responses/OS-20260609T1650Z-townes-root-preservation-student-oracle-response.md`
- `raw/student/20260609T1705-townes-root-preservation-counterexample.md`

## Proof

Let
\[
\eta=10^{-4}
\]
and define
\[
L(s)=\exp\left(
-10\eta s+10^{-4}\left(e^{-10\eta s}-1\right)+\left(e^{\eta s}-1\right)
\right).
\]
Then \(L\) is the bilateral Laplace transform of
\[
X=\eta(10+10P-Q),
\]
where \(P\sim {\rm Pois}(10^{-4})\), \(Q\sim{\rm Pois}(1)\), and \(P,Q\) are independent. Thus \(X\) is a real-valued infinitely divisible law. Its support is unbounded below because of the negative jump \(-\eta Q\), so this does not use the already-depleted nonnegative-support theorem.

We prove:
\[
L\text{ is completely monotone on }[0,1],
\]
but
\[
L^{1/100}\text{ is not completely monotone on }[0,1].
\]

For \(s\in[0,1]\), the Esscher-normalized law has unscaled variable
\[
Z_{a,b}=10+10P_a-Q_b,
\]
where
\[
a=10^{-4}e^{-10\eta s},\qquad b=e^{\eta s}.
\]
Hence
\[
a\in[a_0,A],\qquad b\in[1,B],
\]
with
\[
a_0=10^{-4}e^{-10^{-3}}>9.99\cdot10^{-5},\qquad
A=10^{-4},\qquad B=e^{10^{-4}}<1.001.
\]

Since
\[
(-1)^kL^{(k)}(s)=L(s)\eta^k\mathbb E[Z_{a,b}^k],
\]
it is enough to prove \(\mathbb E[Z_{a,b}^k]\ge0\) for every \(k\ge0\) and every \((a,b)\) in the rectangle above.

Even moments are nonnegative. For odd moments, it suffices to prove the tail dominance
\[
\mathbb P(Z_{a,b}>r)\ge \mathbb P(Z_{a,b}<-r)
\qquad(r\ge0).
\]
Indeed, for \(j\ge0\),
\[
\mathbb E[Z_{a,b}^{2j+1}]
=(2j+1)\int_0^\infty r^{2j}
\left(\mathbb P(Z_{a,b}>r)-\mathbb P(Z_{a,b}<-r)\right)\,dr.
\]

The variable \(Z_{a,b}\) is stochastically increasing in \(a\) and decreasing in \(b\), so the tail-dominance difference is smallest at \(a=a_0\), \(b=B\).

Because \(Z_{a,b}\) is integer-valued, it is enough to check integer \(r\ge0\). For \(0\le r\le9\),
\[
\mathbb P(Z_{a,b}>r)\ge \mathbb P(P_a=0,Q_b=0)=e^{-a-b}>e^{-A-B},
\]
whereas
\[
\mathbb P(Z_{a,b}<-r)\le\mathbb P(Q_B\ge11).
\]
The elementary Poisson tail bound
\[
\mathbb P(Q_B\ge N)
\le e^{-B}\frac{B^N}{N!}\frac{N}{N-B}
\qquad(N>B)
\]
gives
\[
\mathbb P(Q_B\ge11)<3\cdot10^{-8}<e^{-A-B}.
\]

For \(r\ge10\), put \(m=\lfloor r/10\rfloor\). Then \(m\ge1\), and the event \(P_a=m,\ Q_b=0\) gives
\[
\mathbb P(Z_{a,b}>r)
\ge e^{-a-b}\frac{a^m}{m!}
\ge e^{-A-B}\frac{a_0^m}{m!}.
\]
On the other hand,
\[
Z_{a,b}<-r\quad\Longrightarrow\quad Q_b\ge r+11,
\]
so
\[
\mathbb P(Z_{a,b}<-r)\le \mathbb P(Q_B\ge r+11).
\]
For \(10m\le r\le10m+9\), this is bounded by
\[
e^{-B}\frac{B^{10m+11}}{(10m+11)!}\frac{10m+11}{10m+11-B}.
\]
Therefore
\[
\frac{\mathbb P(Z_{a,b}<-r)}
{\mathbb P(Z_{a,b}>r)}
\le
6\,\frac{1.001^{10m+11}m!}{(9.99\cdot10^{-5})^m(10m+11)!}.
\]
At \(m=1\) the right-hand side is \(<10^{-14}\). The ratio of the bound at \(m+1\) to the bound at \(m\) is at most
\[
\frac{1.001^{10}(m+1)}
{(9.99\cdot10^{-5})(10m+12)(10m+13)\cdots(10m+21)}
<1
\]
for every \(m\ge1\). Thus the tail dominance holds for every \(r\ge10\).

This proves \(L\) is completely monotone on \([0,1]\).

Let
\[
R(s)=L(s)^{1/100}.
\]
For the unscaled infinitely divisible seed
\[
Z=10+10P-Q
\]
at \(s=0\), the first three cumulants are
\[
c_1=9.001,\qquad c_2=1.01,\qquad c_3=-0.9.
\]
At time \(t=1/100\), the third raw moment is the Bell-polynomial expression
\[
m_3(t)=tc_3+3t^2c_1c_2+t^3c_1^3.
\]
Thus
\[
m_3(1/100)
=-0.009+0.002727303+0.000729243027001
=-0.005543453972999<0.
\]
Consequently
\[
(-1)^3R'''(0)=\eta^3m_3(1/100)<0.
\]
This violates complete monotonicity. Therefore \(L^{1/100}\) is not completely monotone on \([0,1]\).

The source PGF is
\[
G(z)=L(1-z).
\]
If the corresponding Poisson mixture were \(100\)-divisible, then the PGF root \(H\) would satisfy \(H(z)^{100}=G(z)\) and \(H(1)=1\). Since \(G(z)>0\) on \([0,1]\), this root is the principal root
\[
H(z)=L(1-z)^{1/100}=R(1-z).
\]
But \(R\) is not completely monotone at \(s=0\), equivalently \(H\) is not absolutely monotone at \(z=1\). A PGF cannot have a negative factorial-moment derivative. Hence this mixed Poisson law is not DID.

_Proof source: `raw/student/20260609T1705-townes-root-preservation-counterexample.md`._

## Do not claim

- Do not confuse this with the already true nonnegative-support mixing theorem.

## Tags

`bilateral-laplace-transform`, `counterexample`, `finite-interval-complete-monotonicity`, `proved`, `theorem`, `townes`, `true-negation`
