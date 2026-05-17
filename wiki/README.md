# Pudim Wiki Ingestion Guide

This folder is the public wiki surface for the staged theory. It is intentionally kept under `/wiki` instead of being promoted on the repository front page.

## Layout

- `latest/`: mutable latest public wiki vault for the current staged theory.
- `versions/stage_v001/`: immutable wiki snapshot for theory `v001`.
- Each vault contains `Home.md`, `GOAL.md`, `STATUS.md`, `STRATEGY.md`, `wiki/index.md`, `wiki/graph.json`, and `wiki/nodes/`.

## Open In Obsidian

Open `wiki/latest/` as the Obsidian vault folder when you want the newest graph. Open a directory under `wiki/versions/` when you need an immutable snapshot. Do not open the repository root as the vault if you want the generated wiki links to resolve without extra path setup.

In Obsidian, start at `Home.md`, then open `wiki/index.md`. Use Backlinks to inspect local dependencies and Graph View to inspect node neighborhoods. The generated `wiki/graph.json` is for agents and tooling; Obsidian builds its visible graph from the Markdown links.

## Current Node Summary

- total nodes: 17
- by type: corollary: 1, definition: 4, lemma: 1, note: 2, problem: 3, proposition: 2, theorem: 4
- by status: open: 3, partial: 8, proved: 6

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
| \(A'(\beta)\) | Definition: Zeta free energy |
| \(A''(\beta)\) | Definition: Zeta free energy |
| \(\mu_{q,\beta}(a)\) | Definition: Residue distribution and successor entropy |
| \(B_q(\beta)\) | Definition: Residue distribution and successor entropy |
| \(\Sigma(\beta)\) | Problem: Successor entropy resolution |
| \(S_a(p,\beta)\) | Problem: Prime-modulus Dirichlet \(L\)-resolution |
| \(\mu_{p,\beta}(a)\) | Problem: Prime-modulus Dirichlet \(L\)-resolution |
| \(\mu_{p,\beta}(0)\) | Problem: Prime-modulus Dirichlet \(L\)-resolution |
| \(\mu_{d,\beta}(0)\) | Proposition: Euler-score decomposition |
| \(M(s)\) | Definition: Mellin-Planck partition function |
