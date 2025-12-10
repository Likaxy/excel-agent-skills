# Context-Window Cost Analysis

Token usage for the full-tool path vs the minimal-invoke path in this repo.

---

## 1. What we're measuring

Compare how much of an LLM’s context window is used when:

- **Pattern A (full surface):** All 25 tool definitions (name, parameters, types, descriptions) are loaded into context so the agent can choose and call tools.
- **Pattern B (minimal invoke):** Only a short “slate” doc for the chosen op plus the runner’s output are loaded; no full schema.

So you can see the tradeoff and decide when to use the full server vs the minimal path.

---

## 2. Methodology

### 2.1 Token estimation

- **Tool definitions (full surface):** We use `src/xl_agent/server.py`. Each tool is the block from `@mcp.tool(...)` through the end of that tool’s function (signature, docstring, body). For each block we count words (whitespace-separated) and multiply by **1.3** as a rough tokens-per-word for English and code.
- **Slate docs (minimal surface):** Each `slate/*.md` file is one or two lines (what the op does, args). We count words and use **×2** as a conservative token estimate per word.
- **Runner output:** We only count what `run/xl_cli.py` or `run/<op>.sh` prints; no schema in there.

### 2.2 Scopes

- **Baseline (all 25 tools):** Total tokens for every tool definition.
- **Baseline (all 25 slates):** Total tokens for every slate doc.
- **Scenario (3 ops):** A small workflow (create workbook, write data, create chart) to compare Pattern A vs Pattern B on something realistic.

---

## 3. Results

### 3.1 Full-tool baseline (Pattern A)

All 25 tool definitions were extracted and measured. Per-tool and total:

```
Tool                        Tokens (est.)
────────────────────────────────────────
apply_formula                    124
validate_formula_syntax           72
format_range                     257
read_data_from_excel             185
write_data_to_excel              139
create_workbook                   61
create_worksheet                  66
create_chart                      93
create_pivot_table                93
create_table                      87
copy_worksheet                    63
delete_worksheet                  59
rename_worksheet                  63
get_workbook_metadata             68
merge_cells                       66
unmerge_cells                     66
get_merged_cells                  58
copy_range                       104
delete_range                      88
validate_excel_range              85
get_data_validation_info         170
insert_rows                       78
insert_columns                    78
delete_sheet_rows                 78
delete_sheet_columns              78
────────────────────────────────────────
TOTAL                           2379
```

So with all tools in context, the model gets about **2379 tokens** of tool definitions before you add any conversation or results.

### 3.2 Slate baseline (Pattern B)

All 25 slate docs were measured (words × 2):

```
Total tokens (all 25 slate docs):  446
Average per slate:                ~18
```

So the minimal surface for the same 25 ops is **446 tokens** total, or about **18 per op** when you only load one.

### 3.3 Scenario: 3-op workflow

Workflow: **create_workbook** → **write_data_to_excel** → **create_chart**.

| Pattern | What is in context | Token count (est.) |
|--------|---------------------|--------------------|
| **A (full)** | Schemas for all 3 tools | 61 + 139 + 93 = **293** |
| **B (minimal)** | 3 slate docs + runner outputs | 3 × ~18 = **~54** (plus output length) |

Conceptually:

```
Pattern A (full):
  Context ─┬─ Tool: create_workbook     (61)
           ├─ Tool: write_data_to_excel (139)
           └─ Tool: create_chart        (93)
           ─────────────────────────────────
           Subtotal (schemas only): 293 tokens

Pattern B (minimal):
  Context ─┬─ slate/create_workbook.md     (~18)
           ├─ slate/write_data_to_excel.md (~18)
           └─ slate/create_chart.md       (~18)
           ─────────────────────────────────
           Subtotal (slate only): ~54 tokens
           (+ runner output per step, no schema)
```

So for this scenario, **Pattern B uses about 5× fewer tokens** for the “tool surface” than Pattern A (54 vs 293). The exact ratio depends on how much runner output is kept in context.

---

## 4. What it means

- **Full surface (A)** is good when the agent is exploring or needs full param docs in one shot. Cost is fixed at about 2379 tokens for all 25 tools (or whatever subset the runtime actually loads).
- **Minimal path (B)** is good when the workflow is known and you only need a few ops per turn. Only the slate doc(s) you use and the runner output go in context; rest of the window is free for conversation and results.
- **Tradeoff:** A gives you discoverability and full schema; B gives you less context use and deterministic script-like execution. See `notes/when-full-surface.md` for when to pick which.

---

## 5. How to reproduce

- **Tool counts:** Run `run/count_tokens.py` (it reads `src/xl_agent/server.py`, splits on `@mcp.tool`, word-count × 1.3). We used `analysis/raw_tool_token_counts.txt` and `analysis/mcp_baseline_tokens.txt`.
- **Slate total:** Sum of word counts in `slate/*.md` × 2, in `analysis/slate_total.txt` and `analysis/slate_baseline_tokens.txt`.
- **Scenario:** Just math from those baselines; see `analysis/scenario_compare.txt`.

Numbers are approximate (word-based with fixed multipliers). Re-run the scripts if you want to recompute.
