# Repository Instructions for Research Assistants

**Read [REFERENCE_INDEX.md](REFERENCE_INDEX.md) first**, then [reference/NOTATION.md](reference/NOTATION.md) and the corresponding numbered mathematical source. This is the durable research handoff; do not assume access to earlier chats or their memory.

## Repository source hierarchy

- Work on the default **main** branch unless the user explicitly requests otherwise.
- [reference/](reference/README.md) is the canonical mathematical reading path. Its numbered foundational series still carries **draft** status, and the algebra-geometry series contains revised proofs and correction registers. **The status of a claim is not guaranteed by the folder name.**
- [research/](research/README.md) contains provisional mathematical investigations and older Parts II–VI/VIII that have **not** undergone complete claim-by-claim review.
- [archive/](archive/README.md) contains historically important but unverified/over-interpreted material, including the old Part VII moonshine/K3/phenomenology corpus. Do not repeat its implications as established theorems.
- Existing non-main Git branches are **backups**, not competing canonical texts. Keep them untouched without specific user authorization.
- Consult [MIGRATION.md](MIGRATION.md) and [PATH_CROSSWALK.json](PATH_CROSSWALK.json) for original paths and source blob SHA.

## Mathematics and mathematical proof

1. Use $`u=\log(x/c)`$, with $`x,c,r>0`$, and $`\xi=x/c`$, $`\theta=ru`$ distinct. When present, keep $`\mu>0`$ and its normalization explicit.
2. State derivative coordinates, energy levels, positivity, regularity, branch/domain conditions and boundary data.
3. Distinguish the original function from any general solution of its second-order nonlinear Master; the first-order energy-zero equation is not logically equivalent.
4. Distinguish a proved identity, a chosen metric or embedding, a conditional correspondence, an externally established theorem, an exploratory conjecture, and a physical model.
5. Trace claims to source proofs and local correction registers; if a source cannot be opened, say so rather than guessing from memory or a summary.
6. When a claim says two structures are equivalent, construct the map, test its inverse, and identify preserved invariants. A shared formula, pole, period or integer does not suffice.
7. Do not attribute novelty or a physical realization without independent evidence and correct mathematical hypotheses.

## Workflow for adding results

- Search the [Claim Registry](reference/CLAIM_REGISTRY.md) for an existing ID, then read the **full theorem and proof**, not only the overview.
- For genuine new statements, assign an unused stable SF-R ID, distinguish verified results from open conjectures, and add dependencies/citations.
- Use SymPy, mpmath or independent calculations to check formulas where useful. Computational examples supplement but do not replace a quantified proof.
- Preserve the historical source/provenance when revising or refuting an assertion. Never silently delete an archive or change a backup branch.
- Update internal links, indexes, relevant code tests, and the correction record. Verify the diff has no unintended paths before committing.
- Report the exact path and branch/commit SHA to the user.

## GitHub math conventions

Follow [MARKDOWN_STYLE.md](MARKDOWN_STYLE.md). Inline mathematics requires the dollar-backtick form; display equations require unindented, single-line `math` fences with exactly one blank line above/below. Use `\mathrm{sech}`, `\mathrm{gd}`, etc., not unsupported `\operatorname{...}`, and avoid `\boxed`.

**Access limitation:** placing this file in GitHub does not automatically expose it to every ChatGPT chat. A new conversation must explicitly open this repository via a GitHub connection or provided file.
