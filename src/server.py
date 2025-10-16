"""MCP Server for logging creation.

This server acts as a joyful AI telemetries assistant, 
helping developers to create logging.
"""

import sys
import logging
from pathlib import Path

# Add the project root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Configure logging to reduce MCP framework noise
logging.getLogger('mcp.server.fastmcp').setLevel(logging.WARNING)
logging.getLogger('mcp').setLevel(logging.WARNING)

from mcp.server.fastmcp import FastMCP

from src.utils.constants import *
from src.modules.resources import register_resources
from src.modules.tools import register_tools

# Initialize FastMCP server with configuration options
app = FastMCP(
    "logging-mcp-server",
    instructions="""{
        "logging_info_available": True,
        "MANDATORY_FIRST_ACTION": "🚨 CRITICAL: You MUST call the 'help://get_logging_info_doc' resource FIRST before using any tools or other resources. This resource contains essential logging information that MUST be read before proceeding with any workflow.",
        "failure_handling": "If any step fails, immediately return to the user with error details before attempting to continue or retry.",
    }"""
)

register_resources(app)
register_tools(app)

def main():
    """Run the MCP server."""   
    print("Creating logging MCP Server instant in main() `server.py`...")

    app.run(transport='stdio')

if __name__ == "__main__":
    main()
