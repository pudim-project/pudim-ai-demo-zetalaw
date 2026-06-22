# Ma--Weigert Log-Function \(D_k\) Regions

Source: Rourou Ma and Julian Weigert, "Complete monotonicity of log-functions", Analysis and Mathematical Physics 15, article 141 (2025), DOI `10.1007/s13324-025-01136-9`.

The source studies
\[
\mathcal F_{s,n}=
\left\{ \frac{p(\log x_1,\ldots,\log x_s)}{x_1\cdots x_s}:\deg p\le n\right\}
\]
on the positive orthant and proves a finite semialgebraic test for complete monotonicity by identifying \(\mathrm{CM}_{s,n}\) with a nonnegative-polynomial cone.

Conjecture 4.6 asks whether the one-derivative regions \(D_k\) form a descending chain and converge to \(\mathrm{CM}_{1,n}\). Its displayed \(x\in\mathbb R\) is a domain typo for this log-function family; all local statements use \(x>0\).

Admitted local result:
\[
D_k^{(n)}=D_k^{(n-1)}\qquad(n\ge1\text{ odd},\ k\ge0).
\]
The proof uses the recurrence
\[
Q_{k+1}(y)=(k+1)Q_k(y)-Q'_k(y),
\qquad
\left(-\frac{d}{dx}\right)^k\frac{p(\log x)}x=x^{-k-1}Q_k(\log x),
\]
so the top coefficient of \(Q_k\) is \(k!\) times the top coefficient of \(p\). A nonnegative real polynomial cannot have odd degree.

Consequence: Conjecture 4.6 is verified for \(n\le3\), because \(n=1,3\) reduce to \(n=0,2\) and the source handles \(n=2\).

Open frontier:
\[
D_k^{(4)}\supseteq D_{k+1}^{(4)}
\]
is the first nondeflated case. Future attacks should start with the normalized quartic slice in the source's Example 4.5.
