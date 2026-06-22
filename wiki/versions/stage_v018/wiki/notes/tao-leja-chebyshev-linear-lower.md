# Leja-Chebyshev Newton lower-bound obstruction

Status: `source_open_refuted_subtarget`.

The Tao blog comment-thread problem asks for effective upper bounds for the Newton condition number of Chebyshev roots in Leja ordering. A literal unnormalized polylogarithmic target is impossible.

For any ordering \(\mathbf x\) of the first-kind Chebyshev roots,
\[
\Lambda_{\mathcal N}(\mathbf x)
\ge
\csc\frac{\pi}{2n}
\ge
\frac{2n}{\pi}.
\]

The proof evaluates the final Newton summand at the final ordered node. With
\[
P(t)=\prod_{z\in X_n}(t-z)=2^{1-n}T_n(t),
\]
one has
\[
|P'(\cos\theta_j)|=2^{1-n}\frac n{\sin\theta_j}.
\]
Thus the terminal contribution is at least
\[
\sum_{j=1}^n\sin\frac{(2j-1)\pi}{2n}
=
\csc\frac{\pi}{2n}.
\]

Sharper form: if the final ordered node is \(y=\cos\theta_y\), then
\[
\Lambda_{\mathcal N}(\mathbf x)
\ge
\csc\theta_y\,\csc\frac{\pi}{2n}.
\]

This does not solve the broader effective upper-bound problem. It changes the viable target scale to something like
\[
\Lambda_{\mathcal N}=O(n(\log n)^C)
\]
or a normalized polylogarithmic bound.

Primary artifacts:

- Student proof: `.pudim/raw/student/20260604T-tao-leja-chebyshev-linear-lower.md`
- First-contact: `.pudim/oracle/responses/ORACLE-FC-20260604T-tao-leja-chebyshev-newton-condition-response.md`
- Student Oracle: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-leja-chebyshev-linear-lower-student-response.md`
