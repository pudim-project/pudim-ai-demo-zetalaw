# Zeta-Law Theory PDF Extract

## Metadata
- source_pdf: `C:\Users\domin\Downloads\main.pdf`
- preserved_copy: `.math-wiki/bootstrap/main.pdf`
- sha256: `d71a0dd6093aa29d2f8a7a57db11a3e93bfe3e55d2809dae0c21b67743cdde6b`
- extracted_utc: `20260517T155423Z`
- page_count: 15
- pdf_metadata_Producer: pdfTeX-1.40.28
- pdf_metadata_Author: 
- pdf_metadata_Title: 
- pdf_metadata_Subject: 
- pdf_metadata_Creator: LaTeX with hyperref
- pdf_metadata_Keywords: 
- pdf_metadata_CreationDate: D:20260517105947Z
- pdf_metadata_ModDate: D:20260517105947Z
- pdf_metadata_Trapped: /False
- pdf_metadata_PTEX.Fullbanner: This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025) kpathsea version 6.4.1

## Extraction Notes
- This is a raw text extraction from the PDF because no matching LaTeX source was found in `C:\Users\domin\Downloads`.
- Formula layout, summation bounds, and special glyphs should be audited against the preserved PDF before any node is upgraded to a proved theorem.
- Inline mathematical expressions below are not guaranteed to be valid TeX; they are provenance text for the initial Pudim wiki.

## PDF Outline
- pages 1-1: The zeta law as a Gibbs law
- pages 2-4: Successor entropy and modular resolution
- pages 5-5: Euler-score observations
- pages 6-8: A curvature lemma for the cold zeta law
- pages 6-8: Application I: Nantomah's zeta positivity problem
- pages 9-10: Application II: Alzer–Kwong convexity and concavity problem
- pages 11-13: Application III: A generalized Hölder problem of Sroysang
- pages 14-15: Summary of the framework

## Section: The zeta law as a Gibbs law

Pages: 1-1

### Page 1

Zeta-Law Entropy, Modular Resolution, and Three Applications to
Zeta Inequalities
1 The zeta law as a Gibbs law
All logarithms are natural. Forβ >1, define the Riemann zeta probability law
ρβ(n) := n−β
ζ(β) , n∈N.
Equivalently,
ρβ(n) = e−βE(n)
Z(β) , E(n) = logn, Z(β) =ζ(β).
Thus the Riemann zeta function is the partition function of the energy landscapeE(n) = lognon
N.
We use the notation
A(β) := logζ(β).
ThenAis the free energy of the zeta law. Its first two derivatives are
A′(β) =−E β[logN],
and
A′′(β) = Varβ(logN).
More generally, the derivatives ofAare cumulants of logNunderρ β.
Proposition 1(Zeta-law calculus).Letβ >1and letNbe distributed according toρ β. Then:
Eβ[N −r] = ζ(β+r)
ζ(β) (r≥0).
Moreover, forα, β >1,
D(ρα∥ρβ) = (β−α)E α[logN] + logζ(β)−logζ(α).
Finally,
(logζ) ′′(β) = Varβ(logN)≥0.
Thuslogζis convex on(1,∞).
Proof.The moment identity is immediate:
Eβ[N −r] =
∞X
n=1
n−β
ζ(β) n−r = ζ(β+r)
ζ(β) .
1

## Section: Successor entropy and modular resolution

Pages: 2-4

### Page 2

For the relative entropy,
D(ρα∥ρβ) =
∞X
n=1
ρα(n) log ρα(n)
ρβ(n)
=
∞X
n=1
ρα(n) [(β−α) logn+ logζ(β)−logζ(α)]
= (β−α)E α[logN] + logζ(β)−logζ(α).
DifferentiatingA(β) = logζ(β) gives
A′(β) = ζ ′(β)
ζ(β) =−E β[logN],
and
A′′(β) = ζ ′′(β)
ζ(β) −
 ζ ′(β)
ζ(β)
2
=E β[(logN) 2]−E β[logN] 2.
2 Successor entropy and modular resolution
Forq≥2, define the residue distribution of the zeta law moduloqby
µq,β(a) :=
X
n≥1
n≡a(modq)
ρβ(n), a∈Z/qZ.
We writea+ 1 cyclically inZ/qZand define the modular successor entropy
Bq(β) :=
X
a∈Z/qZ
µq,β(a) log µq,β(a)
µq,β(a+ 1) .
Theorem 2(Zeta-law successor entropy).For everyβ >1,
Σ(β) :=
∞X
n=1
ρβ(n) log ρβ(n)
ρβ(n+ 1) = β
ζ(β)
∞X
k=1
(−1)k+1
k ζ(β+k). (1)
Furthermore,
Σ(β) = sup
q≥2
Bq(β) = lim
q→∞
Bq(β).(2)
Equivalently,
β
ζ(β)
∞X
k=1
(−1)k+1
k ζ(β+k) = sup
q≥2
X
a∈Z/qZ
µq,β(a) log µq,β(a)
µq,β(a+ 1) . (3)
Proof.Since
ρβ(n)
ρβ(n+ 1) =

1 + 1
n
β
,
we have
Σ(β) = β
ζ(β)
∞X
n=1
n−β log

1 + 1
n

.
2

### Page 3

Using
log(1 +x) =
∞X
k=1
(−1)k+1
k xk (0< x≤1)
and monotone Abel limiting atx= 1 gives
Σ(β) = β
ζ(β)
∞X
k=1
(−1)k+1
k ζ(β+k).
It remains to prove the modular variational identity. Fixq≥2. For each residue classa, the
log-sum inequality gives
X
n≥1
n≡a(modq)
ρβ(n) log ρβ(n)
ρβ(n+ 1) ≥µ q,β(a) log µq,β(a)P
n≡a(modq) ρβ(n+ 1) .
Fora̸= 0, the denominator isµ q,β(a+ 1). Fora= 0, the denominator isµ q,β(1)−ρ β(1), which is
at mostµ q,β(1). Therefore
Σ(β)≥B q(β) (q≥2),
and so
Σ(β)≥sup
q≥2
Bq(β).
Conversely, fixM∈N. Forq > M+ 1, the residue classes 1,2, . . . , M+ 1 isolate the firstM+ 1
integers up to tails of sizeO β(q−β):
µq,β(a) =ρ β(a) +O β,M (q−β) (1≤a≤M+ 1).
Also,
µq,β(0) =q −β.
For 1≤a≤q−2, the sequenceµ q,β(a) is decreasing ina, and
µq,β(q−1)> µ q,β(0).
Hence all cyclic terms inB q(β) are nonnegative except possibly the boundary term
µq,β(0) log µq,β(0)
µq,β(1) =O β(q−β logq),
which tends to 0. Therefore
lim inf
q→∞
Bq(β)≥
MX
n=1
ρβ(n) log ρβ(n)
ρβ(n+ 1) .
LettingM→ ∞yields
lim inf
q→∞
Bq(β)≥Σ(β).
Together withB q(β)≤Σ(β), this proves
lim
q→∞
Bq(β) = Σ(β),
and hence the supremum identity.
3

### Page 4

Corollary 3(Prime-modulus DirichletL-resolution).Letpbe prime and letχrange over Dirichlet
characters modulop. Fora∈ {1, . . . , p−1}, define
Sa(p, β) :=
X
χmodp
χ(a)L(β, χ).
Then
µp,β(a) = Sa(p, β)
(p−1)ζ(β) (1≤a≤p−1),
whereas
µp,β(0) =p −β.
Consequently,
Σ(β)≥F p(ζ(β),{L(β, χ)} χmodp ) (pprime, β >1).(4)
where
Fp =p −β log p−β(p−1)ζ(β)
S1(p, β)
+ 1
(p−1)ζ(β)
p−2X
a=1
Sa(p, β) log Sa(p, β)
Sa+1(p, β)
+ Sp−1(p, β)
(p−1)ζ(β) log Sp−1(p, β)
p−β(p−1)ζ(β) .
Moreover,
Σ(β) = limp→∞
pprime
Fp(ζ(β),{L(β, χ)} χmodp ) = sup
pprime
Fp(ζ(β),{L(β, χ)} χmodp ). (5)
Proof.Fora̸= 0 (modp), character orthogonality gives
1
p−1
X
χmodp
χ(a)χ(n) =
(
1, n≡a(modp),
0, n̸≡a(modp),
forncoprime top. Hence
X
n≥1
n≡a(modp)
n−β = 1
p−1
X
χmodp
χ(a)L(β, χ).
Dividing byζ(β) gives the formula forµ p,β(a). The zero class satisfies
µp,β(0) = 1
ζ(β)
∞X
m=1
(mp)−β =p −β.
Substituting these expressions intoB p(β) givesF p. The inequality and limiting identity follow from
Theorem 2 along the prime sequencep→ ∞.
Remark 4(Interpretation).Theorem 2 says that the microscopic additive successor entropy of the
zeta law,
n7→n+ 1,
is recovered exactly from its finite modular shadows,
n7→nmodq.
For prime moduli, the modular shadows are finite nonlinear functionals of DirichletL-values. Thus
an additive entropy production observable ofζis resolved through Dirichlet spectral data.
4

## Section: Euler-score observations

Pages: 5-5

### Page 5

3 Euler-score observations
The modular entropy theorem uses the residue shadows
µq,β(a) =P β(N≡a(modq))
of the zeta law. A second, Euler-product shadow is obtained by looking only at the zero residue
class:
µd,β(0) =P β(d|N) =d −β.
These zero-class shadows decompose the zeta energy.
Proposition 5(Euler-score decomposition).For everyβ >1,
−(logζ) ′(β) =E β[logN] =
∞X
d=1
Λ(d)µd,β(0) =
∞X
d=1
Λ(d)
dβ .
Equivalently,
− ζ ′(β)
ζ(β) =
∞X
d=1
Λ(d)
dβ .
Proof.The identity
logn=
X
d|n
Λ(d)
gives
Eβ[logN] =
∞X
n=1
ρβ(n)
X
d|n
Λ(d)
=
∞X
d=1
Λ(d)Pβ(d|N).
But
Pβ(d|N) = 1
ζ(β)
∞X
m=1
(dm)−β =d −β.
Thus
Eβ[logN] =
∞X
d=1
Λ(d)
dβ .
Since
Eβ[logN] =−(logζ) ′(β),
the claim follows.
Proposition 6(Finite Euler-score identity).For everyA⊆ {1, . . . , N},
X
n∈A
logn=
X
d≤N
Λ(d)
X
m≤N/d
1A(md).
Proof.Reverse the order of summation:
X
d≤N
Λ(d)
X
m≤N/d
1A(md) =
X
n∈A
X
d|n
Λ(d)
=
X
n∈A
logn.
5

## Section: A curvature lemma for the cold zeta law

Pages: 6-8

### Page 6

4 A curvature lemma for the cold zeta law
The following estimate is the free-energy curvature input used in the second application.
Lemma 7(Uniform positive-axis curvature bound).For everys≥3,
(logζ) ′′(s) = Vars(logN)< 1
3 .(6)
Proof.By Proposition 1,
(logζ) ′′(s) = ζ ′′(s)
ζ(s) −
 ζ ′(s)
ζ(s)
2
≤ ζ ′′(s)
ζ(s) ≤ζ ′′(s).
Fors≥3,
ζ ′′(s) =
∞X
m=2
(logm) 2
ms ≤
∞X
m=2
(logm) 2
m3 .
The functionx7→(logx) 2x−3 is decreasing forx≥2. Therefore
∞X
m=2
(logm) 2
m3 ≤ (log 2)2
8 +
Z ∞
2
(logx) 2
x3 dx.
A direct calculation gives
Z ∞
2
(logx) 2
x3 dx= (log 2)2 + log 2 + 1
2
8 .
Hence
(logζ) ′′(s)≤ 2(log 2)2 + log 2 + 1
2
8 < 1
3 .
5 Application I: Nantomah’s zeta positivity problem
Nantomah [1] asked whether
K(n) := (n+ 2)ζ(n+ 1)ζ(n+ 3)−(n+ 1)ζ(n+ 2) 2 −ζ(n+ 1)ζ(n+ 2)
is positive for alln∈N. The zeta-law moment calculus gives an affirmative answer.
Theorem 8(Affirmative solution of Nantomah’s problem).For everyn∈N,
(n+ 2)ζ(n+ 1)ζ(n+ 3)−(n+ 1)ζ(n+ 2) 2 −ζ(n+ 1)ζ(n+ 2)>0.(7)
Proof.Put
s=n+ 1≥2, Z s =ζ(s).
The expression becomes
Ks = (s+ 1)Z sZs+2 −sZ 2
s+1 −Z sZs+1.
LetX(m) = 1/munder the zeta lawρ s. By Proposition 1,
Es[X] = Zs+1
Zs
,E s[X 2] = Zs+2
Zs
.
6

### Page 7

Therefore Ks
Z2s
= (s+ 1)E s[X 2]−sE s[X] 2 −E s[X].
Equivalently,
Ks
Z2s
= (s+ 1) Vars(X) +E s[X] 2 −E s[X].
This is the moment form of the problem.
We now prove positivity. Define
a=ζ(s)−1, b=ζ(s+ 1)−1, c=ζ(s+ 2)−1.
Then
Zs = 1 +a, Z s+1 = 1 +b, Z s+2 = 1 +c.
ExpandingK s gives
Ks =L s +Q s,
where
Ls =sa+ (s+ 1)c−(2s+ 1)b
and
Qs = (s+ 1)ac−sb 2 −ab.
The linear part is positive term by term:
Ls =
∞X
m=2
m−s

s− 2s+ 1
m + s+ 1
m2

=
∞X
m=2
m−s (m−1)(s(m−1)−1)
m2 .
Fors≥2 andm≥2, the summand is positive. In particular, them= 2 term gives
Ls ≥2 −s s−1
4 .
For the quadratic correction, observe that
b=
∞X
m=2
m−s−1 ≤ 1
2
∞X
m=2
m−s = a
2 .
Sincec≥0,
Qs = (s+ 1)ac−sb 2 −ab≥ −sb 2 −ab≥ − s+ 2
4 a2.
Fors≥4,
a=
∞X
m=2
m−s ≤2 −s +
Z ∞
2
x−s dx= 2 −s

1 + 2
s−1

.
Hence, fors≥4,
Ks ≥ 1
4
"
2−s(s−1)−(s+ 2)2 −2s

1 + 2
s−1
2#
.
7

### Page 8

It is enough to prove
2s(s−1)>(s+ 2)

1 + 2
s−1
2
.
Equivalently,
F(s) := 2s(s−1) 3
(s+ 2)(s+ 1) 2 >1.
Ats= 4,
F(4) = 16·27
6·25 = 72
25 >1.
Moreover,
d
ds logF(s) = log 2 + 3
s−1 − 1
s+ 2 − 2
s+ 1 >0 (s≥4),
because 3
s−1 − 2
s+ 1 − 1
s+ 2 > 3
s+ 1 − 2
s+ 1 − 1
s+ 2 = 1
s+ 1 − 1
s+ 2 >0.
ThusK s >0 for alls≥4.
It remains to checks= 2 ands= 3.
Fors= 2,
K2 = 3ζ(2)ζ(4)−2ζ(3) 2 −ζ(2)ζ(3).
Using
ζ(3)<1 + 1
8 +
Z ∞
2
x−3 dx= 5
4 ,
together withζ(2) =π 2/6 andζ(4) =π 4/90, we obtain
K2 > π6
180 − 5π2
24 − 25
8 .
The function
f(x) = x6
180 − 5x2
24 − 25
8
is increasing forx≥3. Sinceπ >313/100,
K2 > f
313
100

= 10415360504209
180000000000000 >0.
Fors= 3,
K3 = 4ζ(3)ζ(5)−3ζ(4) 2 −ζ(3)ζ(4).
We use the elementary bounds
ζ(3)>1 + 1
8 + 1
27 = 251
216 ,
ζ(5)>1 + 1
32 + 1
243 = 8051
7776 ,
and
ζ(4) = π4
90 < 13
12 .
Since
4· 8051
7776 − 13
12 >0,
8

## Section: Application I: Nantomah's zeta positivity problem

Pages: 6-8

### Page 6

4 A curvature lemma for the cold zeta law
The following estimate is the free-energy curvature input used in the second application.
Lemma 7(Uniform positive-axis curvature bound).For everys≥3,
(logζ) ′′(s) = Vars(logN)< 1
3 .(6)
Proof.By Proposition 1,
(logζ) ′′(s) = ζ ′′(s)
ζ(s) −
 ζ ′(s)
ζ(s)
2
≤ ζ ′′(s)
ζ(s) ≤ζ ′′(s).
Fors≥3,
ζ ′′(s) =
∞X
m=2
(logm) 2
ms ≤
∞X
m=2
(logm) 2
m3 .
The functionx7→(logx) 2x−3 is decreasing forx≥2. Therefore
∞X
m=2
(logm) 2
m3 ≤ (log 2)2
8 +
Z ∞
2
(logx) 2
x3 dx.
A direct calculation gives
Z ∞
2
(logx) 2
x3 dx= (log 2)2 + log 2 + 1
2
8 .
Hence
(logζ) ′′(s)≤ 2(log 2)2 + log 2 + 1
2
8 < 1
3 .
5 Application I: Nantomah’s zeta positivity problem
Nantomah [1] asked whether
K(n) := (n+ 2)ζ(n+ 1)ζ(n+ 3)−(n+ 1)ζ(n+ 2) 2 −ζ(n+ 1)ζ(n+ 2)
is positive for alln∈N. The zeta-law moment calculus gives an affirmative answer.
Theorem 8(Affirmative solution of Nantomah’s problem).For everyn∈N,
(n+ 2)ζ(n+ 1)ζ(n+ 3)−(n+ 1)ζ(n+ 2) 2 −ζ(n+ 1)ζ(n+ 2)>0.(7)
Proof.Put
s=n+ 1≥2, Z s =ζ(s).
The expression becomes
Ks = (s+ 1)Z sZs+2 −sZ 2
s+1 −Z sZs+1.
LetX(m) = 1/munder the zeta lawρ s. By Proposition 1,
Es[X] = Zs+1
Zs
,E s[X 2] = Zs+2
Zs
.
6

### Page 7

Therefore Ks
Z2s
= (s+ 1)E s[X 2]−sE s[X] 2 −E s[X].
Equivalently,
Ks
Z2s
= (s+ 1) Vars(X) +E s[X] 2 −E s[X].
This is the moment form of the problem.
We now prove positivity. Define
a=ζ(s)−1, b=ζ(s+ 1)−1, c=ζ(s+ 2)−1.
Then
Zs = 1 +a, Z s+1 = 1 +b, Z s+2 = 1 +c.
ExpandingK s gives
Ks =L s +Q s,
where
Ls =sa+ (s+ 1)c−(2s+ 1)b
and
Qs = (s+ 1)ac−sb 2 −ab.
The linear part is positive term by term:
Ls =
∞X
m=2
m−s

s− 2s+ 1
m + s+ 1
m2

=
∞X
m=2
m−s (m−1)(s(m−1)−1)
m2 .
Fors≥2 andm≥2, the summand is positive. In particular, them= 2 term gives
Ls ≥2 −s s−1
4 .
For the quadratic correction, observe that
b=
∞X
m=2
m−s−1 ≤ 1
2
∞X
m=2
m−s = a
2 .
Sincec≥0,
Qs = (s+ 1)ac−sb 2 −ab≥ −sb 2 −ab≥ − s+ 2
4 a2.
Fors≥4,
a=
∞X
m=2
m−s ≤2 −s +
Z ∞
2
x−s dx= 2 −s

1 + 2
s−1

.
Hence, fors≥4,
Ks ≥ 1
4
"
2−s(s−1)−(s+ 2)2 −2s

1 + 2
s−1
2#
.
7

### Page 8

It is enough to prove
2s(s−1)>(s+ 2)

1 + 2
s−1
2
.
Equivalently,
F(s) := 2s(s−1) 3
(s+ 2)(s+ 1) 2 >1.
Ats= 4,
F(4) = 16·27
6·25 = 72
25 >1.
Moreover,
d
ds logF(s) = log 2 + 3
s−1 − 1
s+ 2 − 2
s+ 1 >0 (s≥4),
because 3
s−1 − 2
s+ 1 − 1
s+ 2 > 3
s+ 1 − 2
s+ 1 − 1
s+ 2 = 1
s+ 1 − 1
s+ 2 >0.
ThusK s >0 for alls≥4.
It remains to checks= 2 ands= 3.
Fors= 2,
K2 = 3ζ(2)ζ(4)−2ζ(3) 2 −ζ(2)ζ(3).
Using
ζ(3)<1 + 1
8 +
Z ∞
2
x−3 dx= 5
4 ,
together withζ(2) =π 2/6 andζ(4) =π 4/90, we obtain
K2 > π6
180 − 5π2
24 − 25
8 .
The function
f(x) = x6
180 − 5x2
24 − 25
8
is increasing forx≥3. Sinceπ >313/100,
K2 > f
313
100

= 10415360504209
180000000000000 >0.
Fors= 3,
K3 = 4ζ(3)ζ(5)−3ζ(4) 2 −ζ(3)ζ(4).
We use the elementary bounds
ζ(3)>1 + 1
8 + 1
27 = 251
216 ,
ζ(5)>1 + 1
32 + 1
243 = 8051
7776 ,
and
ζ(4) = π4
90 < 13
12 .
Since
4· 8051
7776 − 13
12 >0,
8

## Section: Application II: Alzer–Kwong convexity and concavity problem

Pages: 9-10

### Page 9

we get
K3 > 251
216

4· 8051
7776 − 13
12

−3
13
12
2
= 13783
419904 >0.
ThereforeK s >0 for every integers≥2, and henceK(n)>0 for everyn∈N.
6 Application II: Alzer–Kwong convexity and concavity problem
Alzer and Kwong [3, Conjecture 1.12] conjectured that, for everyn∈N, the function 1/ζis strictly
convex on
(−4n,−4n+ 2)
and strictly concave on
(−4n−2,−4n).
The free-energy curvature bound above gives a direct proof.
Theorem 9(Alzer–Kwong Conjecture 1.12).Let
F(x) = 1
ζ(x) .
For every integern≥1,
F ′′(x)>0on(−4n,−4n+ 2).(8)
and
F ′′(x)<0on(−4n−2,−4n).(9)
Thus1/ζis strictly convex on(−4n,−4n+ 2)and strictly concave on(−4n−2,−4n).
Proof.Put
x=−u, u >2.
The functional equation of the Riemann zeta function gives
ζ(−u) =−2 −uπ−u−1 sin
 πu
2

Γ(u+ 1)ζ(u+ 1).
Therefore
1
ζ(−u) =− 2uπu+1
Γ(u+ 1)ζ(u+ 1) sin(πu/2) .
Define the positive function
G(u) := 2uπu+1
Γ(u+ 1)ζ(u+ 1)|sin(πu/2)| .
Onu∈(4n−2,4n),
sin
 πu
2

<0,
so 1
ζ(−u) =G(u).
9

### Page 10

Onu∈(4n,4n+ 2),
sin
 πu
2

>0,
so 1
ζ(−u) =−G(u).
Sincex=−u, second derivatives are unchanged:
d2
dx2 F(x) = d2
du2 F(−u).
It is therefore enough to prove
G′′(u)>0 (u >2).
Let
ℓ(u) = logG(u).
Then
ℓ(u) =ulog 2 + (u+ 1) logπ−log Γ(u+ 1)−logζ(u+ 1)−log
sin
 πu
2
 .
Differentiating twice,
ℓ′′(u) =−ψ ′(u+ 1)−(logζ) ′′(u+ 1) + π2
4 csc2
 πu
2

,
whereψ ′ is the trigamma function.
Put
s=u+ 1.
Sinceu >2, we haves >3. The trigamma function satisfies
ψ′(s) =
∞X
k=0
1
(s+k) 2 <
Z ∞
s−1
dt
t2 = 1
s−1 ≤ 1
2 .
By Lemma 7,
(logζ) ′′(s)< 1
3 .
Also,
csc2
 πu
2

≥1.
Therefore
ℓ′′(u)> π2
4 − 1
2 − 1
3 = π2
4 − 5
6 >0.
SinceG >0,
G′′(u) =G(u)

ℓ′′(u) +ℓ ′(u)2
>0.
Now return tox=−u.
Ifx∈(−4n,−4n+ 2), thenu∈(4n−2,4n), and
F(x) =F(−u) =G(u).
Thus
F ′′(x) =G ′′(u)>0.
10

## Section: Application III: A generalized Hölder problem of Sroysang

Pages: 11-13

### Page 11

Ifx∈(−4n−2,−4n), thenu∈(4n,4n+ 2), and
F(x) =F(−u) =−G(u).
Thus
F ′′(x) =−G ′′(u)<0.
This proves the claimed convexity and concavity pattern.
7 Application III: A generalized H¨ older problem of Sroysang
Sroysang [2, Section 3] uses the notation
ξ(s) = 1
Γ(s)
Z ∞
0
ts−1
et −1 dt, s >1.
Thus, in standard notation,
ξ(s) =ζ(s), s >1.
This is not Riemann’s completed xi-function. In this section we writeζin the main statement, and
then restate the result in Sroysang’s notation.
Sroysang proved the H¨ older-type inequality
ζ
 mX
i=1
xi
pi
!
≤
Qm
i=1 (Γ(xi)ζ(x i))1/pi
Γ(Pm
i=1 xi/pi) ,
under the assumptions
xi >1, p i >1,
mX
i=1
1
pi
= 1.
He then asked how to generalize this inequality using the generalized H¨ older condition
mX
i=1
1
pi
= 1
r , r≥1.
The following theorem gives the corresponding sharp extension.
Theorem 10(Solution of Sroysang’s generalized H¨ older problem).Letm≥2, letr≥1, and let
x1, . . . , xm >1, p 1, . . . , pm >1,
satisfy
mX
i=1
1
pi
= 1
r .
Define
T:=r
mX
i=1
xi
pi
.
ThenT >1and
ζ(T)≤
Qm
i=1 (Γ(xi)ζ(x i))r/pi
Γ(T) . (10)
11

### Page 12

Equivalently, in Sroysang’s notation,
ξ
 
r
mX
i=1
xi
pi
!
≤
Qm
i=1 (Γ(xi)ξ(xi))r/pi
Γ(rPm
i=1 xi/pi) . (11)
Forr= 1, this reduces to Sroysang’s inequality.
Proof.Let
M(s) := Γ(s)ζ(s) =
Z ∞
0
ts−1
et −1 dt, s >1.
Set
λi := r
pi
.
Then
λi >0,
mX
i=1
λi = 1,
and
T=
mX
i=1
λixi.
Since eachx i >1, we haveT >1.
We prove the inequality directly from generalized H¨ older. Define
qi := pi
r .
Then mX
i=1
1
qi
= 1.
Form≥2, the assumptions implyq i >1 for alli. Indeed, ifq j ≤1 for somej, then 1/p j ≥1/r,
leaving no room for the other positive terms in P
i 1/pi = 1/r.
Now define
fi(t) :=
 txi−1
et −1
1/pi
, t >0.
Then mY
i=1
fi(t) =t
P
i(xi−1)/pi(et −1) − P
i 1/pi =t
P
i(xi−1)/pi(et −1) −1/r.
Therefore  mY
i=1
fi(t)
!r
= tr P
i(xi−1)/pi
et −1 .
Using
r
mX
i=1
xi −1
pi
=r
mX
i=1
xi
pi
−r
mX
i=1
1
pi
=T−1,
we get  mY
i=1
fi(t)
!r
= tT−1
et −1 .
12

### Page 13

Hence 





mY
i=1
fi






r
Lr(0,∞)
=
Z ∞
0
tT−1
et −1 dt= Γ(T)ζ(T).
By generalized H¨ older, 





mY
i=1
fi






Lr
≤
mY
i=1
∥fi∥Lpi .
But
∥fi∥pi
Lpi =
Z ∞
0
txi−1
et −1 dt= Γ(x i)ζ(x i).
Therefore
(Γ(T)ζ(T)) 1/r ≤
mY
i=1
(Γ(xi)ζ(x i))1/pi .
Raising both sides to the powerrgives
Γ(T)ζ(T)≤
mY
i=1
(Γ(xi)ζ(x i))r/pi .
Dividing by Γ(T) proves the result.
Remark 11(Free-energy interpretation).The same result can be phrased as log-convexity of the
Mellin–Planck partition function
M(s) = Γ(s)ζ(s) =
Z ∞
0
ts−1
et −1 dt.
Fors >1, define the probability law
νs(dt) := ts−1
(et −1)M(s) dt.
Then
d2
ds2 logM(s) = Var νs(logt)≥0.
ThusMis log-convex on(1,∞). With
λi = r
pi
,
mX
i=1
λi = 1, T=
mX
i=1
λixi,
Jensen’s inequality gives
M(T)≤
mY
i=1
M(x i)λi =
mY
i=1
(Γ(xi)ζ(x i))r/pi .
SinceM(T) = Γ(T)ζ(T), this is exactly Theorem 10. This places Sroysang’s generalized H¨ older
problem inside the same zeta-law free-energy framework used throughout the paper.
13

## Section: Summary of the framework

Pages: 14-15

### Page 14

8 Summary of the framework
The results above use four levels of the same zeta-law viewpoint.
First, the moment layer:
ζ(s+r)
ζ(s) =E s[N −r].
This converts zeta-ratio inequalities into moment inequalities under the Riemann law. Theorem 8
uses this layer.
Second, the free-energy curvature layer:
(logζ) ′′(s) = Vars(logN).
This converts positive-axis control ofζinto thermodynamic curvature estimates. Theorem 9 uses
this layer, transported to the negative axis by the functional equation.
Third, the Mellin–Planck free-energy layer:
M(s) = Γ(s)ζ(s),(logM) ′′(s) = Varνs(logt).
This converts generalized H¨ older inequalities into log-convexity of a continuous zeta partition func-
tion. Theorem 10 uses this layer.
Fourth, the modular entropy layer:
Σ(β) = sup
q≥2
Bq(β).
This says that additive successor entropy of the microscopic zeta law is recovered from finite modular
observations. For prime moduli, these modular observations are explicit nonlinear functionals of
DirichletL-values.
References
[1] Kwara Nantomah,Open Problem on Riemann Zeta Function, ResearchGate problem note, Oc-
tober 2024. Available at:https://www.researchgate.net/publication/384676538_Open_
Problem_on_Riemann_Zeta_Function. The note asks whether
(n+ 2)ζ(n+ 1)ζ(n+ 3)−(n+ 1)ζ(n+ 2) 2 −ζ(n+ 1)ζ(n+ 2)
is positive for alln∈N.
[2] Banyat Sroysang,Two Inequalities for the Riemann Zeta Functions, Mathematica Aeterna, Vol.
3, No. 1 (2013), 21–24. Section 3 asks how Theorem 2.2 changes under the generalized H¨ older
conditionP
i 1/pi = 1/r,r≥1.
[3] Horst Alzer and Man Kam Kwong,On the concavity and convexity of1/ζ, International Jour-
nal of Number Theory, Vol. 21, No. 8 (2025), 1825–1835. DOI:https://doi.org/10.1142/
S1793042125500897. Conjecture 1.12 asks for the convexity and concavity pattern of 1/ζon
the intervals (−4n,−4n+ 2) and (−4n−2,−4n).
[4] Tom M. Apostol,Introduction to Analytic Number Theory, Undergraduate Texts in Mathemat-
ics, Springer, 1976.
14

### Page 15

[5] Harold Davenport,Multiplicative Number Theory, 3rd ed., revised by Hugh L. Montgomery,
Graduate Texts in Mathematics, vol. 74, Springer, 2000.
[6] E. C. Titchmarsh,The Theory of the Riemann Zeta-function, 2nd ed., revised by D. R. Heath-
Brown, Oxford University Press, 1986.
[7] Thomas M. Cover and Joy A. Thomas,Elements of Information Theory, 2nd ed., Wiley-
Interscience, 2006.
15
