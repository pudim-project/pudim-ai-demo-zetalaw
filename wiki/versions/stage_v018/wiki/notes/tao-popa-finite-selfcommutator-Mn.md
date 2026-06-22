# Popa-Tao finite self-commutator \(M_n\) model

Status: finite-dimensional source-model progress.

For trace-zero Hermitian \(H\in M_n(\mathbb C)\), define
\[
\alpha(H)=\inf\{\|V\|^2:\ H=VV^*-V^*V\}.
\]
The earlier \(M_3\) theorem gave
\[
\alpha(H)=\max(\lambda_{\max}(H),-\lambda_{\min}(H)).
\]
This formula is false in general.

A sharp \(M_5\) counterexample is
\[
H_0=\operatorname{diag}\left(\frac45,-\frac35,\frac45,-\frac12,-\frac12\right).
\]
Here
\[
\max(\lambda_{\max}(H_0),-\lambda_{\min}(H_0))=\frac45,
\]
but
\[
\alpha(H_0)=1.
\]
The upper bound is given by the weighted shift with squared weights
\[
\frac45,\quad \frac15,\quad 1,\quad \frac12.
\]
The lower bound follows from the Horn inequality with
\[
I=J=\{1,2,4\},\qquad K=\{1,2,5\}.
\]

The correct replacement is the Horn-orbit invariant:
\[
\alpha(H)
=
\min_{\beta_1\ge\cdots\ge\beta_n\ge0}
\left\{
\beta_1:
\lambda(H)\in
\operatorname{Horn}\bigl(\beta,(-\beta_n,\ldots,-\beta_1)\bigr)
\right\}.
\]
Equivalently, \(\alpha(H)\) is the least \(t\) for which
\[
H=B-UBU^*,
\qquad
0\le B\le tI,
\]
for some unitary \(U\).

This is adjacent to Tao's Popa commutator model but does not solve the infinite operator problem.

Primary proof artifact: `.pudim/raw/student/20260604T-tao-popa-finite-selfcommutator-Mn.md`.

Oracle artifact: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-popa-finite-selfcommutator-Mn-student-response.md`.
