
## what is MCP? why is it good? why are you here?

---
essentially, this is standardized function or tool calling 
![[Screenshot 2025-05-03 at 09-04-59 Introduction - Model Context Protocol.png]]

---

why good? 

---
we want models do a lot! <split >
training them to do everything 
</split>
- time consuming
- expensive
- not deterministic 


---

a simple example is having an llm multiply large numbers

- how can we test generalization?
- or make sure it predicts the next token each time?

---

this is difficult to know! and then we're not sure if our tools are reliable 😢

---

(and again, it'd likely be expensive to train this anyways)

---

so what do we do?

---

follow the Unix philosophy that says 

<split > "tools should do one thing and one thing well" </split>

---


we write programs which go through tests to make sure they operate **exactly** how we want them to in production

---
....so why not just use those and save the hassle?

---

Outside of this, it also gives us *access to up to date information*

<split >
"Knowledge cutoff" is now cutoff from being an issue
</split>
---

#### a small aside on how MCP is providing value
- now **how** do we do it and why is MCP an advancement?
	- function calling has been around, but it also wasn't perfect

---
remove the complexity that the llms don't handle well

(picture credit to PHILSCHMID: https://www.philschmid.de/mcp-introduction)
![[Pasted image 20250502185852.png]] 

---

### using MCP (getting setup)
- theory is fine and dandy, but how do we use it?

---

- We'll need a couple of things:
	1. computer
	2. host app
	3. client app
	4. server (`the mcp server` you've heard so much about)

---

#### easiest method:
- Mac and Windows? Claude Desktop: https://claude.ai/download
	- this gets you your host (Claude) and client (Desktop) apps in one go (computer you're on your own)

---

- Linux untouchable? https://modelcontextprotocol.io/clients HUGE list
	- I use VSCode and installed the Cline plugin with just a click

---

#### getting servers
- install the mcp server you want to use
- google "MCP servers", or places like 
- https://smithery.ai/ or https://github.com/punkpeye/awesome-mcp-servers

---


- pick an MCP server, install it via the marketplace or via command line (note, this is the most difficult part btw, finding and updating your config file)
	- which will be something like `npx -y @smithery/cli install @basicmachines-co/basic-memory --client {cline, claude, your_host_app}`
	- https://github.com/basicmachines-co/basic-memory

---

and to make it explicit again, think of an MCP server as just an api, but now it's your agent calling it for you.

---
### and creating (then installing) MCP's
- easy: https://modelcontextprotocol.io/tutorials/building-mcp-with-llms
	- "Claude 3.5 Sonnet is adept at quickly building MCP server implementations" https://www.anthropic.com/news/model-context-protocol

---
1. load Claude with the linked docs (llms-full.txt and README for TS or Python)
2. describe your MCP server
3. install and good to go

---

- build on top of previous projects: fastMCP
	- fastAPI for MCPs; use a decorator on the functions you want as endpoints
	- https://github.com/jlowin/fastmcp

---

install (this is often the most confusing part)
- find your config 
- update with something like this


```
{
    "mcpServers": {
        "graphlit-mcp-server": {
            "command": "npx",
            "args": [
                "-y",
                "graphlit-mcp-server"
            ],
            "env": {
                "GRAPHLIT_ORGANIZATION_ID": "your-organization-id",
                "GRAPHLIT_ENVIRONMENT_ID": "your-environment-id",
                "GRAPHLIT_JWT_SECRET": "your-jwt-secret",
            }
        }
    }
}
```

---

if all else fails, plug your current json in and ask Claude to generate


---

### demo! 


```
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
```

https://github.com/doomdagadiggiedahdah/mcp-quickstart