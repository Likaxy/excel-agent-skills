# excel-agent-skills

Context-efficient Excel tooling: minimal op surface plus runners. Use slate docs and run scripts (or xl_cli) so only one small doc and the runner output go in context.

## Run

- **Minimal path:** See `slate/` for one doc per op; `run/*.sh` or `run/xl_cli.py <op> [args...]`. Paths must be absolute. Python 3.10+ required for the CLI.
- **Context cost:** See [analysis/context-cost.md](analysis/context-cost.md) for token baselines and scenario comparison.

## Server

The package also runs as a full server (stdio/SSE/HTTP). See TOOLS.md and existing docs for transport options.
