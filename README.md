# excel-agent-skills

**Context-efficient Excel tooling for AI agents:** a full server (stdio/SSE/HTTP) plus a *minimal-invoke path*—small op docs and shell runners—so you can choose how much goes into the model’s context.

---

## Why two ways to run?

Agents that call tools usually load **full tool schemas** (names, parameters, types, descriptions) into the context window. That uses a lot of tokens and can hit limits when many tools are available.

This project offers:

1. **Full server** — All 25 tools as a standard server; full schemas in context.
2. **Minimal path** — One short doc per op in `slate/`, plus `run/*.sh` or `run/xl_cli.py`. Only the doc for the op you need + the runner’s output go in context.

```
┌─────────────────────────────────────────────────────────────────────────┐
│  FULL SERVER (all tools in context)                                      │
│  ─────────────────────────────────                                      │
│  Context: [ Tool₁ schema | Tool₂ schema | … | Tool₂₅ schema ]  ≈ 2379 tokens
│           Agent picks tool → server runs it → result back                 │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  MINIMAL PATH (one op at a time)                                         │
│  ─────────────────────────────────                                      │
│  Context: [ one slate doc (~18 tokens) | runner output ]  ≈ 18 + result │
│           Agent picks op by name → run/xl_cli.py <op> … → stdout only    │
└─────────────────────────────────────────────────────────────────────────┘
```

For token baselines, methodology, and a worked scenario, see **[analysis/CONTEXT-REPORT.md](analysis/CONTEXT-REPORT.md)**.

---

## Quick start

### Minimal path (slate + runners)

- **Python 3.10+** required for the CLI.
- Paths must be **absolute** when using the runners.

```bash
# One doc per op in slate/; run via CLI or shell scripts
./run/create_workbook.sh /tmp/my.xlsx
./run/create_worksheet.sh /tmp/my.xlsx Sheet2

# Or call the CLI directly
python3 run/xl_cli.py create_workbook /path/to/file.xlsx
python3 run/xl_cli.py create_worksheet /path/to/file.xlsx Sheet2
```

- **Slate docs:** `slate/*.md` — one file per operation (e.g. `slate/create_workbook.md`).
- **Runners:** `run/<op>.sh` and `run/xl_cli.py` — same behavior as the server, no server process.

### Full server

The package also runs as a full server (stdio, SSE, streamable HTTP). See **TOOLS.md** and the docs for transport options and configuration.

---

## Layout

| Path | Purpose |
|------|--------|
| `slate/` | Minimal one-page docs per op (~18 tokens each). |
| `run/` | `xl_cli.py` and `run/<op>.sh` — invoke ops from the shell. |
| `analysis/` | Token counts, baselines, and the context-cost report. |
| `notes/` | Short design notes (when to use full vs minimal path). |

---

## Summary

- **25 Excel ops** (workbooks, sheets, data, formatting, charts, pivot tables, validation, etc.).
- **Two usage modes:** full server (all schemas in context) or minimal path (one slate doc + runner output).
- **Measured context cost:** see **analysis/CONTEXT-REPORT.md** for numbers and methodology.
