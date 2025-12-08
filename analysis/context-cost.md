# Context cost

- **MCP baseline (all 25 tool defs):** 2379 tokens (server.py tool blocks; words × 1.3).
- **Slate baseline (all 25 op docs):** 446 tokens.
- **Scenario (3 ops):** MCP 293 vs slate ~54; invoke path loads one slate + output only.

Method: tool defs extracted from server, words counted, ×1.3. Slate: sum of words in slate/*.md × 2.
