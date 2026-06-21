# Tao-Sendov cap geometry: centroid certificate

Status: partial source progress.

This note follows the annular structural alternatives for Tao's Sendov effectivization branch.

The main admitted certificate is:

If \(a=re^{i\theta}\) is a simple zero and
\[
\Re\left(e^{-i\theta}\sum_{i=2}^n z_i\right)
\ge
\left(\frac n2-1\right)r,
\]
then \(P'\) has a zero in \(\overline{D(a,1)}\). Strict inequality gives a zero in \(D(a,1)\).

This is proved by contraposition. Under Sendov failure, Gauss-Lucas places every critical point in \(\overline{\mathbb D}\), while being outside \(D(a,1)\) forces it into the half-plane
\[
\Re(e^{-i\theta}w)\le r/2.
\]
The critical-point centroid identity then forces the opposite strict inequality for the zero centroid.

The pass also records a route-kill: the previously forced opposite-cap mass alone is insufficient for the centroid or radial-segment methods. The obstruction pattern puts \(m\) zeros at \(-1\) and the rest at the tangent point
\[
\tau_+=r/2+i\sqrt{1-r^2/4}.
\]

Next frontier:

\[
T\text{-Tao-Sendov-tangent-cluster-normal-form-critical-point}.
\]

Artifacts:

- Attack plan: `private attack plan`
- Oracle Student: `private Oracle response`
- Proof note: `private proof note`
