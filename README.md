  <img src="assets/logo.png" alt="Excel MCP Server Logo" width="300"/>

[![PyPI version](https://img.shields.io/pypi/v/excel-agent-skills.svg)](https://pypi.org/project/excel-agent-skills/)
[![Total Downloads](https://static.pepy.tech/badge/excel-agent-skills)](https://pepy.tech/project/excel-agent-skills)

A Model Context Protocol (MCP) server that lets you manipulate Excel files without needing Microsoft Excel installed. Create, read, and modify Excel workbooks with your AI agent.

## Features

- 📊 **Excel Operations**: Create, read, update workbooks and worksheets
- 📈 **Data Manipulation**: Formulas, formatting, charts, pivot tables, and Excel tables
- 🔍 **Data Validation**: Built-in validation for ranges, formulas, and data integrity
- 🎨 **Formatting**: Font styling, colors, borders, alignment, and conditional formatting
- 📋 **Table Operations**: Create and manage Excel tables with custom styling
- 📊 **Chart Creation**: Generate various chart types (line, bar, pie, scatter, etc.)
- 🔄 **Pivot Tables**: Create dynamic pivot tables for data analysis
- 🔧 **Sheet Management**: Copy, rename, delete worksheets with ease
- 🔌 **Triple transport support**: stdio, SSE (deprecated), and streamable HTTP
- 🌐 **Remote & Local**: Works both locally and as a remote service

## Usage

The server supports three transport methods:

### 1. Stdio Transport (for local use)

```bash
uvx excel-agent-skills stdio
```

```json
{
   "mcpServers": {
      "excel": {
         "command": "uvx",
         "args": ["excel-agent-skills", "stdio"]
      }
   }
}
```

### 2. SSE Transport (Server-Sent Events - Deprecated)

```bash
uvx excel-agent-skills sse
```

**SSE transport connection**:
```json
{
   "mcpServers": {
      "excel": {
         "url": "http://localhost:8000/sse",
      }
   }
}
```

### 3. Streamable HTTP Transport (Recommended for remote connections)

```bash
uvx excel-agent-skills streamable-http
```

**Streamable HTTP transport connection**:
```json
{
   "mcpServers": {
      "excel": {
         "url": "http://localhost:8000/mcp",
         "transport": "streamable-http"
      }
   }
}
```

## Environment Variables & File Path Handling

### SSE and Streamable HTTP Transports

When running the server with the **SSE or Streamable HTTP protocols**, you **must set the `EXCEL_FILES_PATH` environment variable on the server side**. This variable tells the server where to read and write Excel files.
- If not set, it defaults to `./excel_files`.

You can also set the `FASTMCP_PORT` environment variable to control the port the server listens on (default is `8000` if not set).
- Example (Windows PowerShell):
  ```powershell
  $env:EXCEL_FILES_PATH="E:\MyExcelFiles"
  $env:FASTMCP_PORT="8007"
  uvx excel-agent-skills streamable-http
  ```
- Example (Linux/macOS):
  ```bash
  EXCEL_FILES_PATH=/path/to/excel_files FASTMCP_PORT=8007 uvx excel-agent-skills streamable-http
  ```

### Stdio Transport

When using the **stdio protocol**, the file path is provided with each tool call, so you do **not** need to set `EXCEL_FILES_PATH` on the server. The server will use the path sent by the client for each operation.

## Available Tools

The server provides a comprehensive set of Excel manipulation tools. See [TOOLS.md](TOOLS.md) for complete documentation of all available tools.




