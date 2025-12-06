#!/bin/sh
cd "$(dirname "$0")/.." && python3 run/xl_cli.py get_data_validation_info "$@"
