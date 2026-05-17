# Pudim Wiki Ingestion Guide

This folder is the public wiki surface for the staged theory. It is intentionally kept under `/wiki` instead of being promoted on the repository front page.

## Layout

- `latest/`: mutable latest public wiki vault for the current staged theory.
- `versions/stage_v002/`: immutable wiki snapshot for theory `v002`.
- Each vault contains `Home.md`, `GOAL.md`, `STATUS.md`, `STRATEGY.md`, `wiki/index.md`, `wiki/graph.json`, and `wiki/nodes/`.

Direct node paths are `wiki/latest/wiki/nodes/` for the latest vault and `wiki/versions/stage_v002/wiki/nodes/` for this immutable snapshot. The file `mrw-593af0548f67.md`, for example, lives at `wiki/latest/wiki/nodes/mrw-593af0548f67.md`.

## Open In Obsidian

Open `wiki/latest/` as the Obsidian vault folder when you want the newest graph. Open a directory under `wiki/versions/` when you need an immutable snapshot. Do not open the repository root as the vault if you want the generated wiki links to resolve without extra path setup.

In Obsidian, start at `Home.md`, then open `wiki/index.md`. Use Backlinks to inspect local dependencies and Graph View to inspect node neighborhoods. The generated `wiki/graph.json` is for agents and tooling; Obsidian builds its visible graph from the Markdown links.

## Current Node Summary

- total nodes: 17
- by type: corollary: 1, definition: 4, lemma: 1, note: 2, problem: 3, proposition: 2, theorem: 4
- by status: partial: 1, proved: 13, superseded: 3

## Reading Order

1. Read `latest/GOAL.md` for the terminal mathematical objective.
2. Read `latest/STATUS.md` for the current state and unresolved obstruction.
3. Read `latest/STRATEGY.md` for route decisions and quarantined branches.
4. Read `latest/wiki/index.md` for the node catalog.
5. Open relevant files in `latest/wiki/nodes/` and follow their `parents` and wiki links.

## Node Semantics

`type` says what mathematical object the node claims to be. `status` says how much proof support it has. Treat `proved` nodes as locally audited only when a complete proof is present; treat `open`, `partial`, and `conjectural` nodes as frontier material. Application candidates are not solved applications until their problem or linked solution node is `proved` or `superseded`.

## Notation Highlights

This table is an ingestion aid, not a substitute for the LaTeX definitions. Open the repo-root file `theory/latest/THEORY.tex` for exact source.

| notation | introduced in |
| --- | --- |
| \(\rho_\beta(n)\) | Definition: Riemann zeta probability law |
| \(E(n)\) | Definition: Riemann zeta probability law |
| \(Z(\beta)\) | Definition: Riemann zeta probability law |
| \(A(\beta)\) | Definition: Zeta free energy |
| \(D(\rho_\alpha\Vert\rho_\beta)\) | Proposition: Zeta-law calculus |
| \(\mu_{q,\beta}(a)\) | Definition: Modular residue distribution and successor entropy |
| \(B_q(\beta)\) | Definition: Modular residue distribution and successor entropy |
| \(\Sigma(\beta)\) | Theorem: Zeta-law successor entropy and modular resolution |
| \(S_a(p,\beta)\) | Corollary: Prime-modulus Dirichlet L-resolution |
| \(\mu_{p,\beta}(a)\) | Corollary: Prime-modulus Dirichlet L-resolution |
| \(\mu_{p,\beta}(0)\) | Corollary: Prime-modulus Dirichlet L-resolution |
| \(\mu_{d,\beta}(0)\) | Theorem: Euler-score decomposition |
| \(M(s)\) | Definition: Mellin-Planck partition function |
| \(\zeta(s)\) | Definition: Mellin-Planck partition function |
