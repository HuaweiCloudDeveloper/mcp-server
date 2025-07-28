from .server import mcp


def main():
    import asyncio
    import argparse

    parser = argparse.ArgumentParser(description="Time MCP Server")
    parser.add_argument(
        "-H",
        "--host",
        type=str,
        default="localhost",
        help="Host address (default: localhost)",
    )
    parser.add_argument("-p", "--port", type=int, default=8999, help="Port number")
    args = parser.parse_args()

    # Validate required parameters and display configuration
    if args.port:
        print(f"Web service will run on {args.host}:{args.port}")
    else:
        print(f"Host configured as {args.host}, but port is not specified")

    print("Starting MCP DATE Server...")
    asyncio.run(
        mcp.run(
            transport="streamable-http",
            host=args.host,
            port=args.port,
            path="/mcp",
        )
    )


if __name__ == "__main__":
    main()
