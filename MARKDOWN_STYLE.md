# Markdown mathematical formatting standards

These rules apply to maintained Markdown documentation in the Symmetrical Framework, including the revised Part I chapters. Historical archive files are retained without compulsory retroactive reformatting.

1. **Inline mathematics:** use single dollar delimiters, as in `$u=\log(x/c)$`. Do not use display-math delimiters for inline equations.
2. **Displayed mathematics:** use a fenced `math` block. Open and close the fence at column 1, with **no indentation**.
3. **Whitespace:** insert **exactly one empty line** immediately before and after each displayed mathematical block.
4. **Physical line length:** write each displayed mathematical expression on **one source-code line**. If alignment is needed, keep the full `\begin{aligned}...\end{aligned}` or equivalent expression on one physical line, or split the derivation into successive displayed blocks.
5. **Readable mathematics:** do **not** use `\boxed`. Use prose or section labels to distinguish important identities instead.
6. **GitHub compatibility:** use `\mathrm{...}` rather than `\operatorname{...}` for named functions in maintained math. Examples: `\mathrm{sech}`, `\mathrm{arctanh}`, `\mathrm{gd}`, `\mathrm{sl}`, and `\mathrm{disc}`. Preserve the function arguments and meaning; this is a rendering convention.
7. **Proof structure:** retain every meaningful step of a step-by-step proof. A formatting revision must not delete algebraic steps, logical hypotheses, boundary conditions, or reasoning.
8. **Pre-commit validation:** scan all maintained Markdown for `\operatorname{...}`, `\boxed` and double-dollar display math. Use unindented single-line fenced `math` blocks, with exactly one blank line above and below.

## Example

```math
J^2-(J'/r)^2=(Ae^{ru}+Be^{-ru})^2-(Ae^{ru}-Be^{-ru})^2=4AB.
```

Use ordinary prose between derivation steps, with one display block per mathematical step where that improves clarity. All code fences must start in column 1.

**Scope note:** this is a Markdown rendering convention, not a change to the definitions of $f$, $S$, $W$, $r$, $c$, or $u=\log(x/c)$.
