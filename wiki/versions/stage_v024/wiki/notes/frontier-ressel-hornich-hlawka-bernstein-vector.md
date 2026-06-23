# Ressel Hornich-Hlawka Bernstein Vector Frontier

Status: source-gate pending.

Forage 010 selected Ressel's vector Hornich-Hlawka question for Bernstein functions as the next plus-10 seed. The source problem asks whether the Euclidean/vector Hornich-Hlawka analogue holds for every Bernstein function \(f:[0,\infty)\to[0,\infty)\):

\[
f(|x+y|)+f(|y+z|)+f(|z+x|)
\le
f(|x|)+f(|y|)+f(|z|)+f(|x+y+z|)
\]

for all Hilbert-space triples \(x,y,z\).

The forage reduction is structural, not a proof. For

\[
\Delta_f(x,y,z)
=
f(|x|)+f(|y|)+f(|z|)+f(|x+y+z|)
-f(|x+y|)-f(|y+z|)-f(|z+x|),
\]

the Bernstein representation

\[
f(t)=a+bt+\int_0^\infty (1-e^{-st})\,\nu(ds)
\]

reduces the full question to the exponential kernel

\[
e^{-s|x|}+e^{-s|y|}+e^{-s|z|}+e^{-s|x+y+z|}
\le
1+e^{-s|x+y|}+e^{-s|y+z|}+e^{-s|z+x|}
\]

for every \(s>0\). If this kernel inequality is true, the source problem follows by integration. If it fails, \(f(t)=1-e^{-st}\) is a bounded Bernstein-function counterexample.

This is attractive for the plus-10 search because it uses consolidated primitive nodes directly: Bernstein transport, finite seven-term defect certificates, and kernel positivity/negativity. It is not a mere numeric counterexample task; a valid result should prove a symbolic exponential-kernel theorem or produce an exact geometric certificate.

Do not count this as APP. First-contact must verify exact source wording and later-literature novelty, then Student must prove or refute the exponential-kernel target.
