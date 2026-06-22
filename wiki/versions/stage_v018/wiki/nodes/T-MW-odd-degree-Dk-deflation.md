---
id: "T-MW-odd-degree-Dk-deflation"
type: "theorem"
title: "Ma Weigert odd degree D_k regions deflate to previous even degree"
status: "proved"
tags: ["complete-monotonicity", "deflation", "log-functions", "ma-weigert", "proved", "theorem"]
parents: ["T-Finite-combinatorial-packing-shadow-principle", "D-Log-function-derivative-chain-language"]
refs: ["librarian/audits/LA-20260531T020200-ma-log-odd-deflation.json", "oracle/responses/ORACLE-OS-20260531T-ma-log-function-nle3-oracle-response.md", "raw/student/20260531T020200-ma-log-odd-deflation.md", "wiki/notes/frontier-ma-log-function-dk-odd-deflation.md"]
---

# Theorem: Ma Weigert odd degree D_k regions deflate to previous even degree

## Statement

Correcting Ma--Weigert's Conjecture 4.6 domain to \(x>0\), for every odd \(n\ge1\) and every \(k\ge0\), the region \(D_k^{(n)}=\{f_p\in\mathcal F_{1,n}: (-d/dx)^k f_p(x)\ge0\text{ for all }x>0\}\) equals \(D_k^{(n-1)}\) as an embedded subset of \(\mathcal F_{1,n}\).

## Dependencies

- [[wiki/nodes/T-Finite-combinatorial-packing-shadow-principle|Finite combinatorial packing and shadow principle]]
- [[wiki/nodes/D-Log-function-derivative-chain-language|Log-function derivative-sign regions]]

## Proof and provenance references

- `librarian/audits/LA-20260531T020200-ma-log-odd-deflation.json`
- `oracle/responses/ORACLE-OS-20260531T-ma-log-function-nle3-oracle-response.md`
- `raw/student/20260531T020200-ma-log-odd-deflation.md`
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

_Proof source: `raw/student/20260531T020200-ma-log-odd-deflation.md`._

## Tags

`complete-monotonicity`, `deflation`, `log-functions`, `ma-weigert`, `proved`, `theorem`
