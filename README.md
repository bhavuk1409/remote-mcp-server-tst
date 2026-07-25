# Remote MCP Calculator Server

A minimal **remote Model Context Protocol (MCP) server** built with
**FastMCP**, exposing basic arithmetic tools over HTTP. Unlike a local
stdio-based MCP server, this one runs as a standalone HTTP service — connect
to it from any MCP-compatible client over the network, no local process
required.

![python](https://img.shields.io/badge/python-3.13%2B-3776ab) ![framework](https://img.shields.io/badge/framework-FastMCP-6e56cf) ![transport](https://img.shields.io/badge/transport-HTTP-2ea44f) ![pkg](https://img.shields.io/badge/package%20manager-uv-de5fe9)

---

## What it does

- **Arithmetic tools** — add, subtract, multiply, divide, and generate a
  random number in a range, all callable as MCP tools.
- **Runs remotely over HTTP** — served with `mcp.run(transport="http")` on
  `0.0.0.0:8000`, so any client on the network (not just the local machine)
  can connect.
- **Self-describing** — an `info://server` resource returns the server's
  name, version, description, tool list, and authors as JSON.

---

## Repository layout

```
├── main.py              # FastMCP server: tools + info resource + HTTP entrypoint
├── pyproject.toml       # Project configuration
├── uv.lock              # Dependency lock file
└── README.md            # This file
```

---

## Quickstart

### 1. Prerequisites

- Python 3.13+
- [`uv`](https://docs.astral.sh/uv/) package manager

### 2. Install

```bash
git clone https://github.com/bhavuk1409/remote-mcp-server-tst.git
cd remote-mcp-server-tst

uv sync
```

### 3. Run

```bash
uv run python main.py
```

The server starts on `http://0.0.0.0:8000` using the streamable-HTTP MCP
transport.

### 4. Connect a client

Point any MCP-compatible client at the server's HTTP endpoint, e.g.:

```
http://localhost:8000/mcp
```

For local testing with the FastMCP Inspector:

```bash
uv run fastmcp dev main.py
```

---

## Tools & resources

| Type     | Name              | Description                                              |
| -------- | ------------------ | ---------------------------------------------------------- |
| Tool     | `add`               | Add two numbers (`a`, `b`)                                  |
| Tool     | `subtract`          | Subtract `b` from `a`                                       |
| Tool     | `multiply`          | Multiply two numbers (`a`, `b`)                              |
| Tool     | `divide`            | Divide `a` by `b` (returns an error message on divide-by-zero) |
| Tool     | `random_number`     | Generate a random integer between `min_val` and `max_val`   |
| Resource | `info://server`     | Server metadata as JSON — name, version, description, tool list, authors |

**Example — call `add`:**

```json
{
  "a": 4,
  "b": 7
}
```

**Example — `info://server` response:**

```json
{
  "name": "Simple Calculator Resource Server",
  "version": "1.0",
  "description": "A resource server for the simple calculator.",
  "tools": ["add", "subtract", "multiply", "divide", "random_number"],
  "authors": ["Bhavuk Agrawal"]
}
```

---

## Development

- **New tools** — add a new `@mcp.tool` decorated function in `main.py`.
- **New resources** — add a new `@mcp.resource(...)` decorated function.
- **Transport / host / port** — change the `transport`, `host`, and `port`
  arguments passed to `mcp.run(...)` at the bottom of `main.py`.

---

## Deployment

Since this server speaks plain HTTP, it can run behind any process manager
or container platform — bind it to a public host/port, put a reverse proxy
or TLS termination in front of it, and point your MCP client at the public
URL.

---

## License

MIT — see [LICENSE](./LICENSE).

---

**Built with [FastMCP](https://github.com/jlowin/fastmcp)** — a fast, simple framework for building MCP servers.
