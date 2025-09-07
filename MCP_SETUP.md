# MCP Server Configuration

This project uses Model Context Protocol (MCP) servers to enhance AI capabilities. The following servers are configured:

## Installed MCP Servers

### 1. Sequential Thinking Server
- **Purpose**: Advanced problem-solving and step-by-step reasoning
- **Command**: `mcp-server-sequential-thinking`
- **Use cases**: Complex mathematical proofs, multi-step problem solving, course content planning

### 2. Memory Server  
- **Purpose**: Knowledge graph for persistent learning and context
- **Command**: `mcp-server-memory`
- **Use cases**: Remember course concepts, track learning progress, connect mathematical topics

### 3. Filesystem Server
- **Purpose**: File operations and workspace management
- **Command**: `mcp-server-filesystem`
- **Security**: Restricted to project directory (`/home/julihocc/mlm/mlm`)
- **Use cases**: Course content management, file organization, batch operations

## Configuration

MCP servers are configured in `.vscode/settings.json`:

```json
{
  "mcp.servers": {
    "sequential-thinking": {
      "command": "mcp-server-sequential-thinking"
    },
    "memory": {
      "command": "mcp-server-memory"
    },
    "filesystem": {
      "command": "mcp-server-filesystem",
      "env": {
        "ALLOWED_DIRECTORIES": "/home/julihocc/mlm/mlm"
      }
    }
  }
}
```

## Installation Commands

If you need to reinstall or set up on a new system:

```bash
# Install globally
npm install -g @modelcontextprotocol/server-sequential-thinking
npm install -g @modelcontextprotocol/server-memory
npm install -g @modelcontextprotocol/server-filesystem

# Create system-wide symlinks (for NVM users)
sudo ln -sf ~/.nvm/versions/node/[VERSION]/bin/mcp-server-* /usr/local/bin/
```

## Usage in VS Code

Once configured, these servers provide enhanced AI capabilities through:
- Advanced reasoning for mathematical content creation
- Persistent memory for course development context
- File management operations for content organization

## Troubleshooting

### Common Issues
1. **"spawn npx ENOENT"**: Node.js/npx not in PATH
   - Solution: Create symlinks or ensure Node.js is in system PATH

2. **Permission errors**: MCP servers can't access files
   - Solution: Check `ALLOWED_DIRECTORIES` configuration

3. **Server startup failures**: Missing dependencies
   - Solution: Reinstall globally with `npm install -g`

### Logs
MCP server logs can be found in VS Code's Output panel under "MCP" channel.

## Security Note

The filesystem server is restricted to this project directory for security. If you need access to other directories, update the `ALLOWED_DIRECTORIES` environment variable in the VS Code settings.
