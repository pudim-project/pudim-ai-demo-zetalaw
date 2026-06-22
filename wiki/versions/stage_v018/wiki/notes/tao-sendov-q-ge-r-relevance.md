# Tao-Sendov \(q\ge r\) relevance correction

Status: proved local role-correction theorem.

The tangent-cluster reduction does not enforce
\[
q=\frac{m}{m+N}\ge r.
\]
For every fixed \(r\in(0,1)\), take \(m=1\) and \(N>1/r-1\); then \(q<r\). At \(r=1\), \(q<1=r\) for every \(m,N\ge1\).

The motivating cap-obstruction family also eventually violates \(q\ge r\). It has
\[
m=\left\lfloor\frac{\log n}{\log(1+r)}\right\rfloor+1,
\qquad
N=n-1-m,
\qquad
q=\frac{m}{n-1}\to0.
\]
Thus for fixed \(r\in(0,1)\), this family lies in \(q<r\) for all sufficiently large \(n\).

Consequently, `T-Tao-Sendov-discrete-root-gap-patch-q-ge-r` is a restricted-branch theorem. It controls large-root or all-interior-root geometry only where \(q\ge r\). It is not inherited from the tangent-cluster reduction and should not be applied to the full tangent-cluster family without checking the hypothesis.

The exact tangent-cluster Sendov conclusion remains independent of this restriction: the product identity
\[
y_1y_2=\frac{ab}{1+m+N}
\]
implies
\[
\min(|y_1|,|y_2|)
\le
\sqrt{\frac{1+r}{1+m+N}}
\le
\sqrt{\frac23}<1.
\]
So one free critical point lies in \(D(r,1)\) for every \(m,N\ge1\).

Primary proof artifact: `.pudim/raw/student/20260604T-tao-sendov-q-ge-r-relevance.md`.

Oracle artifact: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-sendov-q-ge-r-relevance-student-response.md`.
