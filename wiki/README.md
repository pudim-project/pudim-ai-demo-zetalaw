# Pudim Wiki Ingestion Guide

This folder is the public wiki surface for the staged theory. It is intentionally kept under `/wiki` instead of being promoted on the repository front page.

## Layout

- `latest/`: mutable latest public wiki vault for the current staged theory.
- `versions/stage_v006/`: immutable wiki snapshot for theory `v006`.
- Each vault contains `Home.md`, `GOAL.md`, `STATUS.md`, `STRATEGY.md`, `wiki/index.md`, `wiki/graph.json`, and `wiki/nodes/`.

Direct node paths are `wiki/latest/wiki/nodes/` for the latest vault and `wiki/versions/stage_v006/wiki/nodes/` for this immutable snapshot. The file `mrw-593af0548f67.md`, for example, lives at `wiki/latest/wiki/nodes/mrw-593af0548f67.md`.

## Open In Obsidian

Open `wiki/latest/` as the Obsidian vault folder when you want the newest graph. Open a directory under `wiki/versions/` when you need an immutable snapshot. Do not open the repository root as the vault if you want the generated wiki links to resolve without extra path setup.

In Obsidian, start at `Home.md`, then open `wiki/index.md`. Use Backlinks to inspect local dependencies and Graph View to inspect node neighborhoods. The generated `wiki/graph.json` is for agents and tooling; Obsidian builds its visible graph from the Markdown links.

## Current Node Summary

- total nodes: 215
- by type: conjecture: 2, corollary: 43, counterexample: 5, definition: 5, example: 1, lemma: 4, note: 14, problem: 17, proposition: 98, theorem: 26
- by status: conjectural: 1, open: 8, partial: 3, proved: 194, superseded: 9

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
| \(P_0(x)\) | Theorem: APP-0007: Complete monotonicity of reciprocal digamma product curvature |
| \(P_n(x)\) | Theorem: APP-0008: Counterexample to complete monotonicity of higher-order polygamma product curvature |
| \(D(\rho_\alpha\Vert\rho_\beta)\) | Proposition: Zeta-law calculus |
| \(Z_{s,n}\) | Definition: Tail zeta partition function |
| \(\zeta_n(s)\) | Definition: Tail zeta partition function |
| \(\rho_{s,n}(k)\) | Definition: Tail zeta partition function |
| \(T_7(n)\) | Theorem: APP-0005: Exact inverse-tail floor formula at s=7 |
| \(\zeta_n(7)\) | Theorem: APP-0005: Exact inverse-tail floor formula at s=7 |
| \(Q(n)\) | Theorem: APP-0005: Exact inverse-tail floor formula at s=7 |
| \(P(n)\) | Theorem: APP-0005: Exact inverse-tail floor formula at s=7 |
