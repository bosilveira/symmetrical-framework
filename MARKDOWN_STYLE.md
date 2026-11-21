# Mathematical Markdown conventions for GitHub

Apply these rules to maintained Symmetrical Framework documentation. The maintained reference is enforced by a repository checker. Historical Gemini drafts are excluded from compulsory reformatting.

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

## Run the checker

```bash
python "reference/algebra-geometry/check_markdown_style.py"
```

The checker rejects old bare-dollar inline formulas, invalid math-fence spacing, indented fences and disallowed LaTeX commands in **maintained reference Markdown**. Historical Gemini files are excluded deliberately. The same rules apply to other maintained documentation as it is revised.

**The source notation rule is about Markdown files.** Equations already rendered visually do not need to contain literal delimiter characters.
