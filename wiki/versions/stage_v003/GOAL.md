# Goal

## Active Terminal Goal

Build a raw Pudim wiki for the theory in `C:\Users\domin\Downloads\main.pdf`: zeta-law entropy, modular resolution, Euler-score identities, the curvature lemma, and the three zeta-inequality applications.

## Accepted Terminal Outcomes

- A local `.math-wiki/` vault initialized for Pudim.
- The PDF preserved as bootstrap provenance.
- Atomic wiki nodes for definitions, theorem claims, problems, applications, references, and framework notes.
- Conservative proof statuses: only self-contained audited nodes may be marked `proved`; imported theorem material can remain `partial`.

## Stop Conditions

- The raw wiki import is complete, graph refresh succeeds, and the project connector configuration is recorded.
- Later proof-audit or publisher cycles should be launched explicitly.

## Scope Constraints

- Bootstrap import only; do not run a full max-depth proof cycle yet.
- Do not send email.
- Do not publish to GitHub until the `pudim-project` GitHub account is authenticated locally.
