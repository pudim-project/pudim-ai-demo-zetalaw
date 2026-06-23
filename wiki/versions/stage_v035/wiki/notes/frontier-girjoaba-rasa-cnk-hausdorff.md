# Girjoaba--Rasa \(c(n,k)\) Convexity and Hausdorff Frontier

Status: convexity source problem open; Hausdorff-moment strengthening refuted in the natural full range by `LA-20260528T163000-girjoaba-rasa-student`.

The source records Rasa's problem to prove convexity in \(k\) for
\[
c(n,k)=\binom{2n}{k}^{-2}
\sum_{j=0}^k\binom{n}{j}^2\binom{n}{k-j}^2.
\]
It also reports numerical evidence suggesting the stronger possibility that this sequence is Hausdorff moment/completely monotone.

The bounded Pudim target is to test the stronger Hausdorff-moment route first.  Any Hausdorff moment sequence \(h_k=\int_0^1t^k\,d\mu(t)\) is nonincreasing.  The case \(n=1\) gives \(c(1,0)=1\), \(c(1,1)=1/2\), \(c(1,2)=1\), so the full sequence cannot be Hausdorff moment in the natural order.

Oracle noticed and the local proof admitted a stronger endpoint obstruction: for every \(n\ge1\),
\[
c(n,2n-1)=\frac12<1=c(n,2n).
\]
Thus the full raw sequence \(0\le k\le2n\) is never Hausdorff moment in the natural order.  This still does not solve the convexity problem.
