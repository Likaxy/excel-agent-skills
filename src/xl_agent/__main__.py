import asyncio
import typer

from .server import run_sse, run_stdio, run_streamable_http

app = typer.Typer(help="Excel agent skills")

@app.command()
def sse():
    """Start Excel agent skills in SSE mode"""
    print("Excel agent skills - SSE mode")
    print("----------------------")
    print("Press Ctrl+C to exit")
    try:
        asyncio.run(run_sse())
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Service stopped.")

@app.command()
def streamable_http():
    """Start Excel agent skills in streamable HTTP mode"""
    print("Excel agent skills - Streamable HTTP mode")
    print("---------------------------------------")
    print("Press Ctrl+C to exit")
    try:
        asyncio.run(run_streamable_http())
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Service stopped.")

@app.command()
def stdio():
    """Start Excel agent skills in stdio mode"""
    print("Excel agent skills - Stdio mode")
    print("-----------------------------")
    print("Press Ctrl+C to exit")
    try:
        run_stdio()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Service stopped.")

if __name__ == "__main__":
    app() 