import os
from typing import Dict, Tuple

from mcp.server.fastmcp import FastMCP


def register_tools(app: FastMCP) -> None:
    """Register the tools for logging instrumentation."""
    # app.tool("setup_logging_tests")(setup_logging_tests)
