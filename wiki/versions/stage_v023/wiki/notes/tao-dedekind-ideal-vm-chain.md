# Tao non-UFD class-group direction: Dedekind ideal von Mangoldt chain

Status: partial source progress.

Tao commented that extensions to number fields or function fields with unique factorization should be easy, while the nontrivial class-group case is less clear and might require analogues on ideals rather than individual elements. This note proves that ideal-valued analogue for a fixed number field.

Scope: \(K\) is fixed, and the state space is the monoid \(\mathcal I_K\) of nonzero integral ideals ordered by divisibility. This does not solve the element-level or principal-ideal-only non-UFD problem.

For \(N\mathfrak a>1\), define
\[
\nu_K(\mathfrak a)
=
\int_1^\infty
\frac{\log N\mathfrak a}{\zeta_K(s)N\mathfrak a^s}\,ds,
\]
and set \(\nu_K((1))=1\). The ideal von Mangoldt function is
\[
\Lambda_K(\mathfrak p^j)=\log N\mathfrak p.
\]

The downward ideal chain divides by prime-power ideals:
\[
P^\downarrow(\mathfrak a\searrow\mathfrak a/\mathfrak q)
=
\frac{\Lambda_K(\mathfrak q)}{\log N\mathfrak a}.
\]
Unique factorization of ideals gives stochasticity:
\[
\sum_{\mathfrak q\mid\mathfrak a}\Lambda_K(\mathfrak q)=\log N\mathfrak a.
\]

The invariant identity is
\[
\nu_K(\mathfrak a)
=
\sum_{\mathfrak q\ne(1)}
\nu_K(\mathfrak a\mathfrak q)
\frac{\Lambda_K(\mathfrak q)}{\log N(\mathfrak a\mathfrak q)}.
\]
It follows from
\[
-\frac{\zeta_K'}{\zeta_K}(s)
=
\sum_{\mathfrak q\ne(1)}\Lambda_K(\mathfrak q)N\mathfrak q^{-s}
\]
and the derivative identity for \(F_\mathfrak a(s)=N\mathfrak a^{-s}/\zeta_K(s)\).

The adjoint upward chain has hitting mass
\[
\mathbb P_{(1)}^\uparrow(\text{hit }\mathfrak a)=\nu_K(\mathfrak a).
\]
Therefore every ideal antichain \(A\) satisfies
\[
\sum_{\mathfrak a\in A}\nu_K(\mathfrak a)\le1.
\]

With \(\kappa_K=\operatorname{Res}_{s=1}\zeta_K(s)\),
\[
\nu_K(\mathfrak a)
\sim
\frac1{\kappa_KN\mathfrak a\log N\mathfrak a}.
\]
Consequently,
\[
\limsup_{X\to\infty}
\sup_A
\sum_{\substack{\mathfrak a\in A\\N\mathfrak a\ge X}}
\frac1{N\mathfrak a\log N\mathfrak a}
\le
\kappa_K,
\]
where the supremum is over ideal antichains.

Remaining open obstruction: the element/principal-ideal non-UFD problem is not solved because removing nonprincipal prime-ideal factors from a principal ideal usually exits the principal state space.

Primary artifacts:

- Student proof: `.pudim/raw/student/20260604T-tao-dedekind-ideal-vm-chain.md`
- First-contact: `.pudim/oracle/responses/ORACLE-FC-20260604T-tao-dedekind-ideal-chain-response.md`
- Student Oracle: `.pudim/oracle/responses/ORACLE-OS-20260604T-tao-dedekind-ideal-chain-student-response.md`
