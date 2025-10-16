#!/usr/bin/env bash
set -euo pipefail

# Extra debug to stderr
echo "[run_server.sh] Starting logging_mcp_server wrapper" >&2
echo "[run_server.sh] Using python: $(command -v python)" >&2

export FASTMCP_DEBUG=1
export PYTHONUNBUFFERED=1

exec /usr/bin/python3 -u /home/inbal/AI/Logging_MCP_Demo/src/server.py 2>&1
