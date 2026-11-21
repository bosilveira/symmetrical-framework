# Repository instructions for future assistants

**Read [REFERENCE_INDEX.md](REFERENCE_INDEX.md) before answering research questions or changing files.** This is the repository's handoff and navigation protocol. It supplements, not replaces, inspection of the actual referenced mathematical files.

## Branches and evidence

- The GitHub default branch is **main**. It contains the numbered `01-foundational/` reference series (currently status: draft) and the provisional `draft/` research corpus.
- The substantial eight-Part research encyclopedia and revised Part I proofs are on **feat/part-i-rigorous-revision**, not yet merged to main. Inspect that branch explicitly; do not assume the directories exist in main.
- Check the current branch and commit SHA. Read exact source files, local proof/correction notes and tests. Do not reconstruct a proof from a chat summary alone; if access fails, say so.
- Research drafts, chat archives, broad identity tables and aspirational physical analogies are **provisional** until their individual statements have been checked.

## Canonical mathematics

- Keep $`u=\log(x/c)`$, $`x,c,r>0`$ and, where used, $`\mu>0`$ explicit. Distinguish $`\xi=x/c`$ and $`\theta=ru`$.
- Distinguish the given profile, a solution of a first-order zero-energy constraint, and a general solution of the second-order cubic Master.
- State the precise differential variable, domains, coupling, boundary data, branch choices, conserved energy and normalization.
- An identity does not establish its converse, uniqueness, a global map, novelty or physical realization without a separate proof.
- Status labels differ between the two branches. Consult the status crosswalk in `REFERENCE_INDEX.md`; do not interpret `[C]` without its local legend.

## Source/revision workflow

1. Read `REFERENCE_INDEX.md` and the linked foundational or feature-branch chapter.
2. Locate the exact claim and its hypotheses. Recover earlier discussions through source files rather than assuming memory is complete.
3. Check algebra symbolically or numerically **as a supplement to proof**; record counterexamples and corrections.
4. Update the source claim and its local audit; provide branch, file path, stable ID/equation anchor when present, and commit SHA.
5. Preserve existing stable IDs. Avoid bulk file moves or archival deletions unless requested. For any eventual rename, maintain a crosswalk and redirects.
6. Check the final diff to avoid unrelated changes; do not merge branches without an explicit instruction.

## GitHub Markdown

Follow [MARKDOWN_STYLE.md](MARKDOWN_STYLE.md). Inline math uses the dollar-backtick convention; displayed math uses unindented single-line `math` code fences with exactly one blank line above/below. Use `\mathrm{sech}`, `\mathrm{gd}`, etc., rather than unsupported `\operatorname{...}`; no `\boxed`. Preserve derivation steps.

**Scope:** a file named `AGENTS.md` can guide capable coding agents, but its existence alone does not guarantee that an unrelated ChatGPT conversation has read this repository. The user must give the repository URL or enable a compatible GitHub connection and ask the assistant to read the index.
