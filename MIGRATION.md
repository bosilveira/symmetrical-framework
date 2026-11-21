# Reorganization and Provenance Log

**Date:** 21 November 2026. **Target:** GitHub default `main`. **Action:** a non-destructive promotion of the existing mathematical corpus into a single navigable branch, with explicit editorial status tiers.

## Preserved backup revisions

- Original `main` before unification: [eff89fd01fe788cddeb20035741c8681ea44daed](https://github.com/bosilveira/symmetrical-framework/commit/eff89fd01fe788cddeb20035741c8681ea44daed)
- Original eight-Part feature source: [45d80ed5a68b6763fe6e4b1abb9dbb96d19055c4](https://github.com/bosilveira/symmetrical-framework/commit/45d80ed5a68b6763fe6e4b1abb9dbb96d19055c4)
- Other development branches, including `feat/introduction` and `feat/project-v0`, were **not changed**.

No backup branch was deleted, force-updated or silently merged. The new commit on `main` has the previous `main` head as its parent, while reusing source blob SHA from the feature branch. This preserves source bytes and Git provenance even where directory names change.

## Path crosswalk

| Previous branch + path | New canonical path | Classification |
|---|---|---|
| `main:01-foundational/*` | `reference/foundations/*` | Foundational reference **drafts**; SF-I IDs retained |
| `feature:Part I - Algebra And Geometry/*` | `reference/algebra-geometry/*` | Mathematically revised reference, local proof registers and scripts |
| `feature:Part I - Algebra And Geometry/*gemini*` | `archive/conversation-sources/<original path>` | Historical AI/conversation sources; compatibility pointers remain in reference |
| `main:draft/*` | `research/active-drafts/*` | Current provisional mathematical investigations |
| `feature:Part II–VI, VIII/*` | `research/legacy-parts/<original Part>/*` | Legacy encyclopedia, **not uniformly checked** |
| `feature:identities/*, theorems/*, drafts/*` | `research/legacy-catalog/<original path>` | Older exploratory catalogs and source notes |
| `feature:Part VII - Moonshine, K3, and Equivariant Geometry/*` | `archive/legacy-interpretations/<original Part>/*` | Historical interpretations; claims **not endorsed** |

Three Gemini source files formerly nested within Part I were additionally placed in `archive/conversation-sources/` as **unchanged originals**, while their old reference paths contain short pointers. The revised mathematical chapter text was not rewritten by this move.

The root [PATH_CROSSWALK.json](PATH_CROSSWALK.json) records individual source paths, source branch, original blob SHA and destination. It is machine-readable provenance; it is not a claim verifier.

The old `main:01-foundational/*` and `main:draft/*` paths are retained as **small Markdown compatibility pointers**, not duplicate copies of their original mathematical content. Older URLs to those files therefore still lead to the relocated canonical file.

## Why Part VII was archived

The old materials assert unproved automatic deductions connecting kernel poles and hyperbolic identities to Mathieu modules, K3 cohomological obstructions, Leech-lattice realizations, BKT/entanglement effects, or particle generations. They conflate sound mathematical facts with unsupported maps between unrelated structures. The exact nine original files remain under [archive/](archive/legacy-interpretations/README.md), with a review protocol for individual salvageable identities.

A statement is not declared false merely because it was archived; it is excluded from the current list of established results until independently specified and verified.

## Review status and remaining work

The revised Part I mathematical arguments are presented as **proof-bearing sources**, not as a declaration that every historical statement has undergone external peer review. The newly relocated main foundational documents remain marked `draft`; the older Parts II–VIII and archived hypotheses remain provisional or excluded. An assertion's status belongs to its precise hypothesis and proof, not its directory.

The next editorial phase is to add stable, equation-level anchors inside the source files, map older F-/D-/H- IDs to the SF-R registry, and audit cross-document dependencies, literature citations, and contradictory legacy formulas. The current migration preserves existing prose and mathematical content and does **not** silently rewrite it.

The organization follows DLMF's emphasis on explicit definitions, equation-level references, notation, errata and subject indexes without adopting its section numbering or claiming the same editorial certification.

## Integrity correction during repository migration (21 November 2026)

A source-formatting audit detected accidental text duplication in two files inherited from the earlier feature revision: `03-04-riccati-coupled.md` and `03-09-jacobi-elliptic-solutions.md`. Both were restored **from their uncorrupted Git blobs** in the intermediate clean tree `b28485b7205cff2f4d06eda222ebf154340e9bc7` (SHA `09a269527b7dd446e85eebb019ae3d84963b9851` and `69682bfd4cf5b05f46bcce452e2a68a54e194a7f`, respectively). The mathematical derivations and GitHub dollar-backtick format of these clean versions were preserved.

This correction was applied on the new canonical `main` tree only. The feature branch remains unchanged as a historical backup; its versions of those two files should **not** be used as authoritative text. See `PATH_CROSSWALK.json` for the exact source/destination blob distinction.

