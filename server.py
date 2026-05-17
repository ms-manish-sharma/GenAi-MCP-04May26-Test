from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello-mcp-python")


@mcp.tool(name="greet", description="Say hello to someone")
def greet(name: str) -> str:
    return f"hello, {name}"


@mcp.tool(name="scold", description="Scolding someone")
def scold(name: str) -> str:
    return f"hello, {name} are cursed"


def main():
    # initialize and run the server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
