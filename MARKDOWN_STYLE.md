# Mathematical Markdown conventions for GitHub

Apply these rules to actively maintained Symmetrical Framework documentation. The maintained `reference/` tree and the new `mathematics/` tree have **separate read-only checkers**. Historical sources in `research/` and `archive/` are not subject to compulsory bulk reformatting; preserve their provenance.

## Inline mathematics: mandatory dollar-backtick syntax

Use an opening dollar sign immediately followed by a backtick, the LaTeX expression, then a backtick immediately followed by a closing dollar sign. Never use old single-dollar inline delimiters.

```markdown
The coordinate is $`u=\log(x/c)`$.
The profile is $`S=\mathrm{sech}(ru)`$, with $`r,c>0`$.
```

This is GitHub's inline-math alternative. Do not place spaces between the dollar signs and their adjacent backticks. Inline mathematical formulas inside prose, lists, and tables must follow the same rule. Use ordinary Markdown code spans for filenames and commands.

## Displayed mathematics

Use unindented fenced code blocks marked `math`, with **exactly one blank line** above and below. The equation inside each block occupies **exactly one source line**; split multi-step proofs into successive blocks, retaining every step.

```math
J^2-(J_u/r)^2=(Ae^{ru}+Be^{-ru})^2-(Ae^{ru}-Be^{-ru})^2=4AB.
```

Never use double-dollar displays or indent fences. If alignment is needed, keep the complete `\begin{aligned}...\end{aligned}` expression on a single source line. No `\boxed` commands.

## Function names and mathematical rigor

Prefer `\mathrm{...}` for function names not reliably recognized by GitHub. Explicitly use `\mathrm{sech}`, `\mathrm{arctanh}`, `\mathrm{gd}`, `\mathrm{sl}`, `\mathrm{disc}`, `\mathrm{dn}`, and `\mathrm{cn}`, not `\operatorname{...}`.

A format revision must not remove algebraic proof steps, change the meaning of a function, omit parameter restrictions, or conflate the original coordinate and the logarithmic one. Canonical definitions remain `u=ln(x/c)` and `r,c>0`, with separate expressions for `x/c` and `ru`.

## Run both maintained-tree checkers

From the repository root:

```bash
python reference/algebra-geometry/check_markdown_style.py
python mathematics/_standards/check_tree.py
```

The first checker scans `reference/` Markdown (excluding historical Gemini drafts); the second checks `mathematics/` Markdown **and local file links**. Both enforce one-line display-math fences and the dollar-backtick syntax where math delimiters appear. The mathematics checker also rejects `\\operatorname`, `\\boxed`, or dollar signs inside display-math bodies. Root files (`README.md`, `AGENTS.md`, `REFERENCE_INDEX.md` and this guide) are maintained but **not currently covered by these automatic scans**. Review them explicitly when editing.

These are syntax/link checks, **not mathematical theorem verifiers**. A checker cannot reliably infer whether every ordinary code span should instead be a mathematical expression: authors must review that distinction. Keep unreviewed historical sources unchanged unless an individual edit is justified.

**The source notation rule is about Markdown files.** Equations already rendered visually do not need to contain literal delimiter characters.
