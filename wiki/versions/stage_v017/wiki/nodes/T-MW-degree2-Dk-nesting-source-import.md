---
id: "T-MW-degree2-Dk-nesting-source-import"
type: "theorem"
title: "Ma Weigert source degree two D_k nesting and convergence for F_1_2"
status: "proved"
tags: ["complete-monotonicity", "log-functions", "ma-weigert", "proved", "source-import", "theorem"]
parents: ["T-Finite-combinatorial-packing-shadow-principle", "D-Log-function-derivative-chain-language"]
refs: ["https://link.springer.com/article/10.1007/s13324-025-01136-9", "private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-ma-log-function-dk-odd-deflation.md"]
---

# Theorem: Ma Weigert source degree two D_k nesting and convergence for F_1_2

## Statement

In Ma--Weigert's one-variable quadratic log-function family \(\mathcal F_{1,2}\), the signed-derivative regions \(D_k^{(2)}\) form the descending nesting/convergence picture toward \(\mathrm{CM}_{1,2}\) described by the source's degree-two discriminant computation.

## Dependencies

- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]
- [[wiki/nodes/D-Log-function-derivative-chain-language|Log-function derivative-sign regions]]

## Proof and provenance references

- `https://link.springer.com/article/10.1007/s13324-025-01136-9`
- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-ma-log-function-dk-odd-deflation.md`

## Proof

Put \(y=\log x\). Define \(Q_{0,p}=p\) and
\[
\left(-\frac{d}{dx}\right)^k f_p(x)=x^{-k-1}Q_{k,p}(\log x).
\]
If this holds for \(k\), then
\[
\left(-\frac{d}{dx}\right)^{k+1}f_p(x)
=-\frac{d}{dx}\left(x^{-k-1}Q_{k,p}(\log x)\right)
=x^{-k-2}\left((k+1)Q_{k,p}(\log x)-Q'_{k,p}(\log x)\right).
\]
Thus
\[
Q_{k+1,p}(y)=(k+1)Q_{k,p}(y)-Q'_{k,p}(y).
\]
If \(p(y)=c_ny^n+\cdots\), induction gives
\[
[y^n]Q_{k,p}=k!c_n.
\]

Now suppose \(n\) is odd and \(f_p\in D_k^{(n)}\). Since \(x>0\) implies \(y=\log x\) ranges over all of \(\mathbb R\), the polynomial \(Q_{k,p}(y)\) is nonnegative for all real \(y\). A real nonzero polynomial of odd degree cannot be nonnegative on all of \(\mathbb R\). Therefore its degree must be less than \(n\), hence \(k!c_n=0\) and \(c_n=0\). So \(p\in\mathbb R[y]_{n-1}\), meaning \(f_p\in D_k^{(n-1)}\). The reverse inclusion follows from \(\mathcal F_{1,n-1}\subset\mathcal F_{1,n}\).

For \(n=0\), the regions are the nonnegative ray \(c_0/x\). The deflation gives \(n=1\). The source's quadratic analysis gives \(n=2\), and the deflation gives \(n=3\). The first nondeflated case is \(n=4\).

the MW odd degree Dk deflation: true local proof.
the MW Conjecture 4 6 nle3 subcase: true solved subcase.
the MW Conjecture 4 6 even nge4 open: open frontier.

This is solved subcase/theory growth only. It is not a full solved source problem and not a public staging application.

_Proof source: `private proof note`._

## Tags

`complete-monotonicity`, `log-functions`, `ma-weigert`, `proved`, `source-import`, `theorem`
