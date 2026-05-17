# Wiki Vault

This directory is the immutable wiki snapshot `stage_v002` for theory `v002`.

## Obsidian Ingestion

Open this directory itself as an Obsidian vault. Start from `Home.md`, then inspect `wiki/index.md`, and use Graph View plus Backlinks to move through node dependencies. The durable mathematical objects live in `wiki/nodes/`; `wiki/graph.json` is a generated machine-readable graph.

## Files

- `GOAL.md`: terminal objective.
- `STATUS.md`: current research state and next obstruction.
- `STRATEGY.md`: route map and branch status.
- `wiki/index.md`: generated node catalog.
- `wiki/nodes/`: atomic definitions, problems, conjectures, propositions, lemmas, theorems, corollaries, examples, counterexamples, and notes.

## Node Summary

- total nodes: 17
- by type: corollary: 1, definition: 4, lemma: 1, note: 2, problem: 3, proposition: 2, theorem: 4
- by status: open: 3, partial: 8, proved: 6

## Notation Highlights

This table is an ingestion aid, not a substitute for the LaTeX definitions. Open the repo-root file `theory/latest/THEORY.tex` for exact source.

| notation | introduced in |
| --- | --- |
| \(\rho_\beta(n)\) | Definition: Riemann zeta probability law |
| \(E(n)\) | Definition: Riemann zeta probability law |
| \(Z(\beta)\) | Definition: Riemann zeta probability law |
| \(A(\beta)\) | Definition: Zeta free energy |
| \(A'(\beta)\) | Proposition: Free-energy derivatives |
| \(A''(\beta)\) | Proposition: Free-energy derivatives |
| \(\mu_{q,\beta}(a)\) | Definition: Residue distribution |
| \(B_q(\beta)\) | Definition: Successor entropy |
| \(\Sigma(\beta)\) | Problem: Successor entropy resolution |
| \(S_a(p,\beta)\) | Problem: Prime-modulus Dirichlet \(L\)-resolution |
| \(\mu_{p,\beta}(a)\) | Problem: Prime-modulus Dirichlet \(L\)-resolution |
| \(\mu_{p,\beta}(0)\) | Problem: Prime-modulus Dirichlet \(L\)-resolution |
| \(\mu_{d,\beta}(0)\) | Theorem: Euler-score decomposition |
| \(M(s)\) | Definition: Mellin-Planck partition function |
