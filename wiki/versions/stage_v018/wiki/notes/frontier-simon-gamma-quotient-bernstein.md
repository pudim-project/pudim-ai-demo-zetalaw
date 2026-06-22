# Simon Gamma-Quotient Bernstein Frontier

Thomas Simon's 2020 paper reduces the Bernstein character of the moment sequence \((n!)^t\), for \(0<t<1\), to the Bernstein character of
\[
\Phi_t(\lambda)=\frac{\Gamma(1-t+\lambda)}{\lambda^{1-t}\Gamma(\lambda)}.
\]
Equivalently, with \(\alpha=1-t\),
\[
F_\alpha(x)=\frac{\Gamma(x+\alpha)}{\Gamma(x)x^\alpha},
\qquad 0<\alpha<1.
\]

The source records this as unanswered and notes that \(1/\Phi_t\) is logarithmically completely monotone, but that this is not sufficient for \(\Phi_t\) to be Bernstein.

Local partial result:
\[
\frac{d}{dx}\log F_\alpha(x)
=
\int_0^\infty e^{-xt}
\left(
\frac{1-e^{-\alpha t}}{1-e^{-t}}-\alpha
\right)\,dt,
\]
and the kernel is positive by concavity of \(u\mapsto 1-e^{-ut}\). Thus \(1/F_\alpha\) is logarithmically completely monotone. The full Bernstein problem remains open in the local Theory.

## Status Update 2026-05-31

Student Oracle `ORACLE-OS-20260531T121700-simon-gamma-quotient-bf` was fired on the concrete Simon gamma-quotient target and returned a usable proof strategy. Local Student/Librarian audit `LA-20260531T123900-simon-gamma-quotient-bf` promotes the source Bernstein node true.

For \(0<\alpha<1\), the stronger admitted theorem is that
\[
1-F_\alpha(x)
\]
is completely monotone. With \(\beta=1-\alpha\), define
\[
J_\alpha(t)=\int_0^1(1-v)^{\alpha-1}
\left(\frac{t}{e^{tv}-1}\right)^\alpha\,dv.
\]
The factor \(t/(e^{tv}-1)\) is decreasing in \(t\), so \(J_\alpha\) is decreasing from \(\Gamma(\alpha)\Gamma(1-\alpha)\) to \(0\). Hence \(\mu_\alpha=-dJ_\alpha\) is a positive finite measure and
\[
1-F_\alpha(x)
=
\frac{1}{\Gamma(\alpha)\Gamma(1-\alpha)}
\int_0^\infty e^{-xt}\,\mu_\alpha(dt).
\]
Thus \(F_\alpha'\) is completely monotone and \(F_\alpha\) is Bernstein.

The complete-Bernstein strengthening is refuted. On the upper lip of the negative axis, for \(r\in(\alpha,1)\),
\[
F_\alpha(-r+i0)
=
\frac{\Gamma(\alpha-r)}{\Gamma(-r)}r^{-\alpha}e^{-i\pi\alpha},
\]
whose imaginary part is negative. This violates the Pick property required of complete Bernstein functions.

Staging status: private solved-source candidate only. It is not yet in the public v008 manuscript and should not be published without a source-wording/novelty check and the normal staging agent.
