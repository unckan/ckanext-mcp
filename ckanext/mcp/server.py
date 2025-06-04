"""
The main view for the MCP server.
"""
import logging
from mcp.server.fastmcp import FastMCP


log = logging.getLogger(__name__)


# Create an MCP server
mcp_instructions = (
    "Welcome to the CKAN MCP server! This server allows you to define which questions any resource can answer, "
    "and let users interact with your data through resources and tools."
)
mcp = FastMCP("CKAN MCP Server", instructions=mcp_instructions)


@mcp.resource("ckan://what")
def whats_ckan() -> str:
    """ Tell the user what CKAN is """
    ckan_is = (
        "CKAN is a powerful data management system that makes data accessible - "
        "for everyone. It is used by governments, organizations, and individuals to publish, share, and collaborate on data."
    )
    return ckan_is
