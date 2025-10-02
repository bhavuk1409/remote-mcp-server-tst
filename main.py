from fastmcp import FastMCP
import random
import json

#create a FastMCP instance
mcp = FastMCP(name="simple calculator")

#add tools to the mcp
@mcp.tool
def add(a, b):
    '''Adds two numbers.'''
    return a + b 

@mcp.tool
def subtract(a, b):
    '''Subtracts two numbers.'''
    return a - b    

@mcp.tool
def multiply(a, b):
    '''Multiplies two numbers.'''
    return a * b            

@mcp.tool
def divide(a, b):
    '''Divides two numbers.'''
    if b == 0:
        return "Error: Division by zero."
    return a / b

@mcp.tool
def random_number(min_val, max_val):
    '''Generates a random number between min_val and max_val.'''
    return random.randint(min_val, max_val)

# resource server information

@mcp.resource("info://server")
def get_resource_info() -> str:
    '''get the information about the server.'''
    info = {
        "name": "Simple Calculator Resource Server",
        "version": "1.0",
        "description": "A resource server for the simple calculator.",
        "tools": ["add", "subtract", "multiply", "divide", "random_number"],
        "authors": ["Bhavuk Agrawal"],
    }
    return json.dumps(info,indent=2)

#start the mcp server for remote calls and this is the only change required to make it a remote server
if __name__ == "__main__":
    mcp.run(transport='http', host="0.0.0.0", port=8000)


