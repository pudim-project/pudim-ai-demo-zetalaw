# Frontier: Karp--Sitnik Shifted Hypergeometric Ratios

Scout forage `FI-20260530T-karp-only-031` selected the Karp--Sitnik shifted-ratio frontier. The source proves monotonicity of shifted generalized hypergeometric quotients using generalized Stieltjes representations. In the special \(\sigma=1,\delta=1\) case, formula (21) gives a reciprocal-defect identity.

For \(q\ge1\) and \(b_i>a_i>0\), set
\[
F(x)={}_{q+1}F_q(1,a_1,\ldots,a_q;b_1,\ldots,b_q;-x).
\]
Karp--Sitnik's positive-density representation makes \(F\) a normalized Stieltjes function. Therefore \(G=1/F\) is complete Bernstein and
\[
\frac{G(x)-1}{x}
\]
is Stieltjes.

Using the contiguous defect identity,
\[
1-F(x)
=x\,{}_{q+1}F_q(1,a_1+1,\ldots,a_q+1;b_1+1,\ldots,b_q+1;-x)
\prod_i\frac{a_i}{b_i},
\]
the shifted ratio is
\[
R(x)=
\prod_i\frac{b_i}{a_i}\frac{G(x)-1}{x}.
\]
Thus \(R\) is Stieltjes and completely monotone, and \(xR(x)\) is complete Bernstein up to the same positive scalar.

The broader \(\sigma\ne1\), \(\delta\ne1\), and parameter-relaxed questions remain open. They require generalized Stieltjes quotient or fractional-shift machinery not supplied by the reciprocal-defect identity.

## Source-Wording Audit

The primary Karp--Sitnik source was rechecked after the Oracle retry. Formula (21), Lemma 1, and the monotone shifted-quotient theorem support the local proof above. However, the paper's explicit open problems ask for:

- multivariate hypergeometric expressions and analytic-continuation extensions for the \(g\)-density;
- relaxation of Theorem 1 parameter restrictions;
- two stated inequality conjectures;
- a direct derivation of a Thomae identity.

The source does not explicitly ask whether the \(\sigma=1,\delta=1\) shifted quotient is Stieltjes, completely monotone, or whether \(xR(x)\) is complete Bernstein. Therefore this node is a reusable bridge and theory-growth result, not a solved external application from Karp--Sitnik alone.
