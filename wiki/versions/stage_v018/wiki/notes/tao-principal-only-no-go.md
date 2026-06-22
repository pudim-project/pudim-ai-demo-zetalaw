# Principal-only single-primepower von Mangoldt no-go

Status: proved obstruction lemma; partial source progress.

This note explains a precise obstruction in Tao's nontrivial-class-group direction. The ideal-valued chain works on all nonzero integral ideals, but the naive principal-only chain fails unless the class number is one.

Let \(\mathcal P_K\) be the monoid of nonzero principal integral ideals. For a nonunit \(\mathfrak a\in\mathcal P_K\), define
\[
R(\mathfrak a)
=
\sum_{\substack{\mathfrak q\mid\mathfrak a\\
\mathfrak q=\mathfrak p^j\\
\mathfrak a/\mathfrak q\ \mathrm{principal}}}
\Lambda_K(\mathfrak q).
\]
Then
\[
R(\mathfrak a)=\log N\mathfrak a
\]
for every nonunit principal integral ideal if and only if \(K\) has class number one.

The obstruction is sharp. If \([\mathfrak p]\) has order \(h>1\), then \(\mathfrak p^h\) is principal, but among the divisors \(\mathfrak p,\ldots,\mathfrak p^h\), only \(\mathfrak p^h\) leaves a principal quotient. Thus
\[
R(\mathfrak p^h)=\log N\mathfrak p
\]
while
\[
\log N(\mathfrak p^h)=h\log N\mathfrak p.
\]
The missing mass is \((h-1)\log N\mathfrak p\).

This should not be read as saying non-UFD Tao analogues are impossible. It only rules out the unmodified principal-only, single-primepower, Tao-normalized rule.

Primary artifacts:

- Student proof: `.pudim/raw/student/20260604T-tao-principal-only-no-go.md`
- First-contact: `.pudim/oracle/responses/ORACLE-FC-20260604T-tao-principal-only-no-go-response.md`
- Student Oracle: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-principal-only-no-go-student-response.md`
