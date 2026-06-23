# Bondesson--Simon \(HM_2\) Positive-Power Closure

Source: Lennart Bondesson and Thomas Simon, "Stieltjes functions of finite order and hyperbolic monotonicity", arXiv:1604.05267.

The source defines \(HM_k\) by asking that, for every \(u>0\),
\[
w\mapsto f(uv)f(uv^{-1}),\qquad w=v+v^{-1},
\]
is \(k\)-monotone. For \(k=2\), \(M_2\) is exactly the cone of nonnegative, nonincreasing, convex functions.

Source open question: Remark 4(a) asks whether \(f\in HM_k\) implies \(f^p\in HM_k\) for every \(p\ge1\).

Local admitted subcase:
\[
f\in HM_2,\ p\ge1\quad\Longrightarrow\quad f^p\in HM_2.
\]

Proof handle: if \(g\in M_2\), then \(g^p\in M_2\), because \(t^p\) is increasing and convex on \([0,\infty)\) for \(p\ge1\). Apply this to \(g_u(w)=f(uv)f(uv^{-1})\).

Scope guardrails:

- This does not solve the \(HM_k\) question for \(k\ge3\).
- This does not prove power-regularity \(\widehat{HM}_2\), which would require all \(p>0\).
- Future work should start with \(M_3\) / \(HM_3\), not repeat \(k=2\).
