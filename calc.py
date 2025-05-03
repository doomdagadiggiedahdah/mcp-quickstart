from mcp.server.fastmcp import FastMCP

# Initialize the MCP server with a name
mcp = FastMCP("Simple Calculator")

# Define a simple addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

# Define a subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

# Define a multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

# Define a division tool
@mcp.tool()
def divide(a: float, b: float) -> float:
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Run the server using stdio transport
if __name__ == "__main__":
    mcp.run(transport="stdio")




#### Config file #### 
"""
"calculator": {
    "command": "/home/mat/Documents/ProgramExperiments/cortext-exp/.venv/bin/python",
    "args": ["/home/mat/Documents/ProgramExperiments/cortext-exp/calc.py"],
    "disabled": false,
    "transportType": "stdio"
}
"""