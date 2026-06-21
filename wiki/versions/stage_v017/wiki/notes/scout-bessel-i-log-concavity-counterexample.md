# Scout Result: Bessel \(I_\nu\) Square-Root Log-Concavity Counterexample

## Classification

This is a local Pudim v2 scout result, not a staged zeta-law application. The proposed extension
\[
u\mapsto \sqrt u\,I_\nu(u)
\]
strictly log-concave on \((0,\infty)\) for every \(\nu\ge0\) is false.

The exact counterexample is \(\nu=0,u=10\). The local certificate proves
\[
\frac{I_1(10)}{I_0(10)}<\frac{9487}{10000},
\]
and hence
\[
\left(\log(\sqrt u\,I_0(u))\right)''\bigg|_{u=10}
>
\frac{9831}{100000000}>0.
\]

## Literature Status

The 2011 Baricz--Ponnusamy--Vuorinen paper proves the result for \(\nu\ge1/2\) and asks whether it extends to all \(\nu\ge0\). The counterexample is in the missing range \(0\le\nu<1/2\).

A 2019 paper by Nanthanasub--Novaprateep--Wichailukkana appears to claim a broader log-concavity theorem for \(t^\mu I_\nu(t)\) that includes \(\nu=0,\mu=1/2\). The counterexample above contradicts that specialization. No erratum or prior matching counterexample was found in the web literature audit.

## Domain-Fit Decision

The proof is adjacent to the zeta-law project because it concerns special-function curvature and log-concavity, but it does not use a theorem, definition, or proof mechanism from the staged zeta-law theory. It should remain in the Wiki as a scout result unless a later Advisor/Librarian pass introduces a real bridge layer, such as a general special-function curvature certificate framework, and records how this result grows from that bridge.

## Local Proof Artifacts

- `private scout artifact`
- `private proof note`
- `private proof artifact`
- `private librarian audit`
