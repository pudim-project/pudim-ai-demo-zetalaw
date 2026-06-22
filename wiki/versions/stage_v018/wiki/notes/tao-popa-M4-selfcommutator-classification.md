# Popa-Tao \(M_4\) self-commutator classification

Status: finite-dimensional source-model progress.

For trace-zero Hermitian \(H\in M_4(\mathbb C)\),
\[
\alpha(H)
=
\inf\{\|V\|^2:\ H=VV^*-V^*V\}
=
\max(\lambda_{\max}(H),-\lambda_{\min}(H)).
\]

The proof uses the Horn-orbit invariant. After normalizing
\[
\max(\lambda_{\max},-\lambda_{\min})=1
\]
and replacing \(H\) by \(-H\) if needed, write
\[
\lambda(H)=(1,a,b,-1-a-b).
\]
If \(a\ge0\), choose
\[
\beta=(1,-b,-a-b,0).
\]
If \(a\le0\), choose
\[
\beta=(1,-a-b,-b,0).
\]
In both cases, the \(n=4\) Horn inequalities are satisfied for
\[
\lambda(H)\in
\operatorname{Horn}\bigl(\beta,(-\beta_4,-\beta_3,-\beta_2,-\beta_1)\bigr),
\]
which yields \(H=B-UBU^*\) with \(0\le B\le I\).

Thus the low-dimensional picture is:

- \(M_3\): spectral-radius formula holds.
- \(M_4\): spectral-radius formula holds.
- \(M_5\): spectral-radius formula fails.

Primary proof artifact: `.pudim/raw/student/20260604T-tao-popa-M4-selfcommutator-classification.md`.

Oracle artifact: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-popa-M4-selfcommutator-classification-student-response.md`.
