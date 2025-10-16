
from src.utils.constants import *
from src.utils.files_management import _load_file
from mcp.server.fastmcp import FastMCP


#####################################
### Info Sources for logging MCP  ###
#####################################

async def get_logging_info_doc() -> str:
    """IMPORTANT: This resource contains essential logging information that should be read first.
    
    Returns:
        Detailed information on logging from the logging info source file.
    """
    print("Calling get_logging_info_doc() resource")

    try:
        return _load_file(INFO_DOCS_PATH + "Logging_Info_Doc.md")
    except Exception as e:
        return f"ERROR: Failed to load logging info source documentation: {str(e)}"


def register_resources(app: FastMCP) -> None:
    """Register the resources for logging orchestration."""
    app.resource("help://get_logging_info_doc")(get_logging_info_doc)
