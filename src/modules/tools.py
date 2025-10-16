import os
from typing import Dict, Tuple

from mcp.server.fastmcp import FastMCP

def list_logging_steps() -> str:
        """Return the structured logging workflow stages."""
        return (
            "Stage 1: Identify/create logging utility\n"
            "Stage 2: Plan insertion points (create LoggingSuggestions.md)\n"
            "Stage 3: Add logger calls per approved plan\n"
            "Stage 4: Summarize where logs were added"
        )

def register_tools(app: FastMCP) -> None:
    """Register the tools for logging instrumentation."""
    app.tool("list_logging_steps")(list_logging_steps)
