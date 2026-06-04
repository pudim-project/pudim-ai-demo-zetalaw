# Frontier Note: Qi--Guo Tau Threshold

Source: Feng Qi and Bai-Ni Guo, *Complete Monotonicities of Functions Involving Gamma and Digamma Functions*, RGMIA Research Report Collection 7(1), Article 8, 2004.

Open Problem 3 asks for the maximum of
\[
\tau(s,t)=\frac1s\left[t-(t+s+1)\left(\frac{t}{t+1}\right)^{s+1}\right],
\qquad (s,t)\in\mathbb N\times(0,\infty).
\]

The local solution shows that a finite maximum does not exist, but the sharp supremum is
\[
\sup_{s,t}\tau(s,t)=\frac{a_*}{1+a_*+a_*^2},
\qquad e^{a_*}=1+a_*+a_*^2,\quad a_*>0.
\]
Numerically this is \(0.298425607525639\ldots\).

The proof uses the substitution \(y=(t+1)^{-1}\), a one-crossing derivative form for fixed \(s\), and a monotone envelope argument showing that the fixed-\(s\) maxima increase to the limiting continuous envelope.
