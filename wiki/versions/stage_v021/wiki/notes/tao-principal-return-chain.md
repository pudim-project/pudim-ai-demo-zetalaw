# Principal-return trace theorem for the ideal von Mangoldt chain

Status: partial source progress.

This note records a positive repair of the failed naive principal-only chain in the nontrivial-class-group setting suggested by Tao. The correct principal-ideal process is not a one-primepower principal-only chain; it is the first-return trace of the full ideal von Mangoldt chain on the principal class.

Let \(\mathcal P_K\) be the nonzero principal integral ideals. Start the full downward ideal chain at \(\mathfrak a\in\mathcal P_K\), and stop at the first later time it returns to \(\mathcal P_K\). This defines a stochastic downward trace
\[
\widehat P^\downarrow(\mathfrak a\to\mathfrak b)
=
\mathbb P_{\mathfrak a}(Y_{\tau_{\mathcal P}}=\mathfrak b).
\]

The upward trace is obtained by strict block reversal:
\[
\widehat P^\uparrow(\mathfrak b\to\mathfrak a)
=
\frac{\nu_K(\mathfrak a)}{\nu_K(\mathfrak b)}
\widehat P^\downarrow(\mathfrak a\to\mathfrak b),
\qquad \mathfrak a\ne\mathfrak b.
\]
The absorbing downward self-loop at \((1)\) is not reversed.

The analytic input is a class-return lemma. For each ideal class \(C\),
\[
S_C(s)=\sum_{c(\mathfrak q)=C}\Lambda_K(\mathfrak q)N\mathfrak q^{-s}
\sim\frac1{h_K}\frac1{s-1}.
\]
This implies that the full upward ideal chain returns to the principal class almost surely, so the upward principal-return trace is stochastic.

For every principal ideal \(\mathfrak a\),
\[
\mathbb P_{(1)}^{\widehat\uparrow}(\text{hit }\mathfrak a)=\nu_K(\mathfrak a).
\]
Therefore principal-ideal antichains satisfy
\[
\sum_{\mathfrak a\in A}\nu_K(\mathfrak a)\le1.
\]
With \(\kappa_K=\operatorname{Res}_{s=1}\zeta_K(s)\),
\[
\limsup_{X\to\infty}\sup_A
\sum_{\substack{\mathfrak a\in A\\N\mathfrak a\ge X}}
\frac1{N\mathfrak a\log N\mathfrak a}
\le\kappa_K,
\]
where \(A\) ranges over principal-ideal antichains.

This is a process-level repair, not a full element-level solution.

Primary artifacts:

- Student proof: `.pudim/raw/student/20260604T-tao-principal-return-chain.md`
- First-contact: `.pudim/oracle/responses/ORACLE-FC-20260604T-tao-principal-return-chain-response.md`
- Student Oracle: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-principal-return-chain-student-response.md`
