#!/bin/sh
cd "$(dirname "$0")/.." && python3 run/xl_cli.py write_data_to_excel "$@"
