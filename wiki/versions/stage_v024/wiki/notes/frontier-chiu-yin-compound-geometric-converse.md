# Frontier: Chiu--Yin Compound-Geometric Complete-Monotonicity Converse

Primary source: Sung Nok Chiu and Chuancun Yin, "On the complete monotonicity of the compound geometric convolution with applications in risk theory", Scandinavian Actuarial Journal 2014(2), 116--124. DOI: <https://doi.org/10.1080/03461238.2011.647061>.

The source proves forward preservation of complete monotonicity under mixed geometric compounding and derives risk-theory consequences for the Sparre Andersen model. Its Lemma 3.1 says that if the claim-size distribution \(H\) has a completely monotone density, then the ascending ladder-height distribution \(F^+\) has a completely monotone density.

Remark 3.5 explicitly conjectures the converse of Lemma 3.1 and, consequently, the converses of the ruin-probability, ruin-time, and deficit-at-ruin complete-monotonicity theorems.

## Classical Equilibrium Slice

In the classical Cramer--Lundberg/equilibrium-ladder subcase, the ascending ladder-height density is
\[
f_+(x)=\frac{\overline H(x)}{m},
\qquad
m=\int_0^\infty \overline H(u)\,du.
\]
Assume \(H\) has density \(h\). If \(f_+\) is completely monotone, then \(\overline H=m f_+\) is completely monotone, and
\[
h(x)=-\overline H'(x)=-m f_+'(x)
\]
is completely monotone because the negative derivative of a completely monotone function is completely monotone.

Thus the Chiu--Yin converse is true in this classical/equilibrium slice. The full Sparre Andersen converse remains open locally, because the general ladder-height transform includes the descending-ladder renewal factor and is not inverted by this one-line derivative argument.

This branch is theory growth in the Laplace-transform/complete-monotonicity closure layer, not a staged application candidate.
