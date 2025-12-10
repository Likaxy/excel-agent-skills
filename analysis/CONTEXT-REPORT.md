# Context cost — appendix

Summary and key numbers are in the README. This doc is the full methodology, per-tool breakdown, and how to reproduce.

---

## What we're measuring

- **Pattern A (full):** All 25 tool defs (name, params, types, descriptions) in context.
- **Pattern B (minimal):** One slate doc per op plus runner output; no full schema.

## Methodology

- **Tool defs:** From `src/xl_agent/server.py`, each block from `@mcp.tool(...)` through end of function. Words × 1.3.
- **Slate:** Each `slate/*.md`, words × 2.
- **Runner output:** What `run/xl_cli.py` or `run/<op>.sh` prints only.

## Per-tool token counts (full surface)

```
apply_formula                    124    validate_formula_syntax           72
format_range                     257    read_data_from_excel              185
write_data_to_excel              139    create_workbook                    61
create_worksheet                  66    create_chart                      93
create_pivot_table                93    create_table                      87
copy_worksheet                    63    delete_worksheet                  59
rename_worksheet                  63    get_workbook_metadata              68
merge_cells                       66    unmerge_cells                     66
get_merged_cells                  58    copy_range                       104
delete_range                      88    validate_excel_range               85
get_data_validation_info         170    insert_rows                       78
insert_columns                    78    delete_sheet_rows                 78
delete_sheet_columns              78
────────────────────────────────────
TOTAL                           2379
```

## Scenario (3 ops)

create_workbook → write_data_to_excel → create_chart. Full: 61+139+93 = 293. Minimal: 3×~18 = ~54.

## Reproduce

- Tool counts: `run/count_tokens.py`. Outputs: `analysis/raw_tool_token_counts.txt`, `analysis/mcp_baseline_tokens.txt`.
- Slate total: sum words in `slate/*.md` × 2. In `analysis/slate_total.txt`, `analysis/slate_baseline_tokens.txt`.
- Scenario: `analysis/scenario_compare.txt`.

Approximate (word-based, fixed multipliers). Re-run scripts to recompute.
