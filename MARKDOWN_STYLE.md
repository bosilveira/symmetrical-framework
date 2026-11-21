# GitHub mathematical Markdown conventions

Apply these conventions to **maintained** Symmetrical Framework files; historical conversational archives are excluded from automatic conversion.

1. **Inline math**: require `$` followed immediately by a backtick and the LaTeX, then a backtick followed immediately by `$`; the literal source example below is authoritative.
2. **Displayed math**: an unindented ```math` fence, one expression on **one physical source line**, closing fence, with **exactly one blank line** before and after. Do not use double-dollar display delimiters.
3. **Named functions**: prefer `\mathrm{sech}`, `\mathrm{arctanh}`, `\mathrm{gd}`, `\mathrm{sl}`, `\mathrm{disc}`, `\mathrm{dn}` and `\mathrm{cn}`. Avoid unsupported `\operatorname{...}` and `\boxed`.
4. **Mathematical fidelity**: formatting must not remove proof steps, signs, parameter domains, integration constants or energy restrictions. Keep the logarithmic coordinate $`u=\log(x/c)`$ and the scale $`c`$ explicit.
5. **Validation**: the feature branch currently contains a checker at `Part I - Algebra And Geometry/check_markdown_style.py`; it enforces the maintained Part I scope there. This default branch does **not** yet include that checker. Do not claim repository-wide automated validation on main.

Example source for inline math:

```markdown
The coordinate is $`u=\log(x/c)`$ and the profile is $`S=\mathrm{sech}(ru)`$.
```

Example display source:

```math
S(u)^2+W(u)^2=1,\qquad u=\log(x/c).
```

GitHub supports both inline delimiters in general, but this project **requires the dollar-backtick variant** to reduce Markdown interference. See [GitHub's math documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) and the `REFERENCE_INDEX.md` protocol.
