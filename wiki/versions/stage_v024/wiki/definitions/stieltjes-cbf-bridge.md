# Stieltjes And Complete Bernstein Bridge

A Stieltjes function has the form
\[
f(x)=c+\int_0^\infty \frac{d\mu(t)}{x+t},
\qquad c\ge0,\quad \mu\ge0,
\]
with the usual local integrability condition. Compact-support variants such as
\[
f(x)=\int_0^1\frac{d\nu(s)}{1+sx}
\]
are equivalent after a change of variables and scaling.

The standard bridge used in `FI-20260530T-karp-only-031` is:

- if \(F\) is a nonzero Stieltjes function, then \(1/F\) is a complete Bernstein function;
- if \(G\) is complete Bernstein and \(G(0+)<\infty\), then
\[
\frac{G(x)-G(0+)}{x}
\]
is Stieltjes.

Together these convert normalized Stieltjes transforms \(F(0)=1\) into Stieltjes defect quotients
\[
\frac{1/F(x)-1}{x}.
\]
