# Finite-dimensional \(\ell^1\) dual-certificate language

Let \(V\) be a real vector space and let \(\mathcal A\subset V\) be a finite family.

- The elements of \(\mathcal A\) are the coordinate atoms.
- A primal representation of \(v\in V\) is a finite expansion
  \[
  v=\sum_{a\in\mathcal A}c_a a.
  \]
- The \(\ell^1\)-norm of that representation is \(\sum_{a\in\mathcal A}|c_a|\).
- A dual certificate for the lower bound \(M\) is a linear functional \(\Lambda:V\to\mathbb R\) such that
  \[
  \Lambda(v)=M,
  \qquad
  |\Lambda(a)|\le 1\quad(a\in\mathcal A).
  \]

The standard duality estimate is then
\[
M=\Lambda(v)=\sum_{a\in\mathcal A}b_a\Lambda(a)
\le \sum_{a\in\mathcal A}|b_a|
\]
for every other representation \(v=\sum b_a a\). Hence any primal representation of norm \(M\), paired with such a dual certificate, proves exact minimality.
