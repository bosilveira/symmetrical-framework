# Template — Definition / Proposition / Theorem

**Use as a template; do not treat examples as a new theorem.**

```markdown
---
id: <stable-claim-id, or "pending">
kind: definition | theorem | proposition | identity | construction
status: provisional | proved | checked | known | superseded
source:
  - <exact repository path/commit or attachment filename/section>
depends_on:
  - <stable object/claim IDs>
parameters:
  - <SF-P IDs>
---

# <Title>

## Bound variables and hypotheses

| Symbol (with scope) | Type/domain | Role |
|---|---|---|
| ... | ... | independent / dependent / coupling / integration constant |

## Statement
Use mathematical formulas with their valid domain, orientation and branch.

## Proof or construction
List each change of variables, Jacobian, derivative convention and parameter substitution.

## Converse / exceptions / limiting cases
State exactly what does not follow, and identify counterexamples.

## Tests, external references and corrections
Distinguish complete proof from finite checks. Link the original and errata.

## Dependencies and downstream review
Link primary source object, affected derived objects and known open issues.
```

**Equation IDs:** use stable claim IDs from [reference/CLAIM_REGISTRY.md](../../reference/CLAIM_REGISTRY.md) when applicable, and never overwrite a distinct historical theorem with a matching short name. Future equation anchors can be generated without changing the meaning of an ID.
