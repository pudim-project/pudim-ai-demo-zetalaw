# Tao-Sawin Weyl algebra \(\ell^1\) model: exact value

Status: `source_open_solved_scoped`.

The Tao commutator thread contains a finite model problem, sharpened by Will Sawin: in the Weyl algebra \(DX-XD=1\), determine the least \(\ell^1\) coefficient norm of a balanced degree \((n,n)\) noncommutative polynomial equal to \(1\).

The exact value is
\[
L_n=\frac{2^n}{n!}.
\]

Upper bound:
\[
P_n=\frac1{n!}\operatorname{ad}_D^n(X^n)=1,
\]
and
\[
\|P_n\|_1=\frac{2^n}{n!}.
\]

Lower bound uses the dual functional \(\Phi_{-1/2}\), defined by normal ordering:
\[
\Phi_q(X^rD^s)=
\begin{cases}
q^r r!,&r=s,\\
0,&r\ne s.
\end{cases}
\]
The algebraic Wick formula gives, for a balanced word \(w\in W_n\),
\[
|\Phi_{-1/2}(w)|\le\frac{n!}{2^n}.
\]
Applying this to any representation \(P=1\) gives
\[
1=|\Phi_{-1/2}(P)|
\le
\frac{n!}{2^n}\|P\|_1.
\]

Therefore \(\|P\|_1\ge2^n/n!\), matching the commutator construction.

Primary artifacts:

- Student proof: `private proof note`
- First-contact: `private Oracle response`
- Student Oracle: `private Oracle response`

Scope: this is a finite Weyl-algebra model theorem. It does not solve the full operator-norm commutator problem.
