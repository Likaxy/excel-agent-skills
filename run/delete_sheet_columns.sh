#!/bin/sh
cd "$(dirname "$0")/.." && python3 run/xl_cli.py delete_sheet_columns "$@"
