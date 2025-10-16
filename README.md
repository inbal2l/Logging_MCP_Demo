# Logging_MCP_Demo

This repo was created as a demo for the talk: "Code Smarter: Harnessing AI tools for C++ Development"
It demonstrates how enriched context can improve the results of AI


## Setting up the server

NOTE: This manual is for setting up the server in WSL (on windows). Of course, if can also be set on Linux or other environemnts, by running the "server.py" directly.

### Steps for setting up the server

#### Step 1: make sure your environment have the "requirements.txt" packages installed, by running:
```
pip install -r requirements.txt --upgrade
```

#### Step 2: add to your MCP configuration (in this example - "cline_mcp_settings.json"):

```
{
  "mcpServers": {
    "logging_mcp_server": {
      "autoApprove": [],
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "bash",
      "args": [
        "/path/to/repo/Logging_MCP_Demo/run_server.sh"
      ]
    },
    ...
  }
}
```

Or you can run directly using python:
```
{
  "mcpServers": {
    "logging_mcp_server": {
      "autoApprove": [],
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "python",
      "args": [
        "\\path\\to\\repo\\Logging_MCP_Demo\\src\\server.py"
      ]
    },
    ...
  }
}
```

The server should now appear in your MCP servers list.