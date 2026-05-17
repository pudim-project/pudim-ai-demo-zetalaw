# Project Connectors

## GitHub

- Account/owner: `pudim-project`
- Repository: `pudim-project/zetalaw-demo`
- Remote URL: `https://github.com/pudim-project/zetalaw-demo.git`
- Local `origin` points at this URL.
- Current blocker: the local GitHub CLI is authenticated as `DomingosSalazar`, so live creation/push to `pudim-project` requires switching or adding that account.

Recommended command once authenticated:

```powershell
gh auth switch -u pudim-project
gh repo create pudim-project/zetalaw-demo --private --source=. --remote=origin --push
```

## Gmail

- Project account: `pudimproject@gmail.com`
- Pudim label convention: `Pudim/zetalaw-demo`
- Outreach subject prefix: `[PUDIM-APP-zetalaw-demo]`

The Gmail connector should be authenticated as `pudimproject@gmail.com` before creating Pudim outreach drafts. No email should be sent without explicit batch confirmation.
