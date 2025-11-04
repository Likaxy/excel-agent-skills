  <img src="assets/logo.svg" alt="Excel MCP Server Logo" width="300"/>

[![PyPI version](https://img.shields.io/pypi/v/excel-agent-skills.svg)](https://pypi.org/project/excel-agent-skills/)
[![PyPI downloads](https://img.shields.io/pypi/dm/excel-agent-skills.svg)](https://pypi.org/project/excel-agent-skills/)

A Model Context Protocol (MCP) server that lets you manipulate Excel files without needing Microsoft Excel installed. Create, read, and modify Excel workbooks with your AI agent.

## Features

- 📊 Create and modify Excel workbooks
- 📝 Read and write data
- 🎨 Apply formatting and styles
- 📈 Create charts and visualizations
- 📊 Generate pivot tables
- 🔄 Manage worksheets and ranges
- 🔌 Dual transport support: stdio and SSE

## Quick Start

### Prerequisites

- Python 3.10 or higher

### Running the Server

The server supports two transport modes: stdio and SSE.

#### Using stdio transport

Stdio transport is ideal for direct integration with tools like Cursor Desktop or local development, which can manipulate local files:

```bash
uvx excel-agent-skills stdio
```

#### Using SSE transport

SSE transport is perfect for remote connections, which manipulate remote files:

```bash
uvx excel-agent-skills sse
```

### Add to Cursor


## Using with AI Tools

1. Add this configuration to your client, choosing the appropriate transport method for your needs:

**Stdio transport connection** (for local integration):
```json
{
   "mcpServers": {
      "excel-stdio": {
         "command": "uvx",
         "args": ["excel-agent-skills", "stdio"]
      }
   }
}
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

2. The Excel tools will be available through your AI assistant.

## Environment Variables & File Path Handling

### SSE Transport

When running the server with the **SSE protocol**, you **must set the `EXCEL_FILES_PATH` environment variable on the server side**. This variable tells the server where to read and write Excel files.
- If not set, it defaults to `./excel_files`.

You can also set the `FASTMCP_PORT` environment variable to control the port the server listens on (default is `8000` if not set).
- Example (Windows PowerShell):
  ```powershell
  $env:EXCEL_FILES_PATH="E:\MyExcelFiles"
  $env:FASTMCP_PORT="8080"
  uvx excel-agent-skills sse
  ```
- Example (Linux/macOS):
  ```bash
  EXCEL_FILES_PATH=/path/to/excel_files FASTMCP_PORT=8080 uvx excel-agent-skills sse
  ```

### Stdio Transport

When using the **stdio protocol**, the file path is provided with each tool call, so you do **not** need to set `EXCEL_FILES_PATH` on the server. The server will use the path sent by the client for each operation.

## Available Tools

The server provides a comprehensive set of Excel manipulation tools. See [TOOLS.md](TOOLS.md) for complete documentation of all available tools.




