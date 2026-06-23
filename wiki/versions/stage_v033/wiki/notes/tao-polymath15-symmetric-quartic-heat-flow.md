# Polymath15 symmetric quartic heat-flow certificate

Status: finite source-model progress.

For every \(0<a\le b\), the symmetric quartic
\[
F_0(x)=(x^2-a^2)(x^2-b^2)
\]
remains real-rooted under backward heat flow:
\[
F_t(x)=e^{-t\partial_x^2}F_0(x)
\]
has only real zeros for every \(t\ge0\).

Writing
\[
S=a^2+b^2,\qquad P=a^2b^2,
\]
one obtains
\[
F_t(x)=x^4-(S+12t)x^2+(P+2St+12t^2).
\]
With \(u=x^2\), the reduced quadratic has discriminant
\[
\Delta_t=(b^2-a^2)^2+16(a^2+b^2)t+96t^2\ge0,
\]
positive sum \(S+12t\), and positive product \(P+2St+12t^2\). Hence both \(u\)-roots are positive and all \(x\)-zeros are real.

This generalizes the earlier example \((x^2-1)(x^2-4)\). It is a finite Polymath15-style certificate theorem, not a de Bruijn-Newman \(\Lambda\)-bound improvement.

Primary proof artifact: `.pudim/raw/student/20260604T-tao-polymath15-symmetric-quartic-heat-flow.md`.

Oracle artifact: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-polymath15-symmetric-quartic-heat-flow-student-response.md`.
