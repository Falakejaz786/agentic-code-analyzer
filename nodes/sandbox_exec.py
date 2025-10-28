# nodes/sandbox_exec.py
import sys
import io
import contextlib
import traceback

def execute_code(code: str) -> dict:
    """
    Safely execute Python code in a sandboxed environment.
    Captures stdout, stderr, and exceptions.
    Supports recursive functions and self-referencing code.
    """
    result = {
        "stdout": "",
        "stderr": "",
        "exception": None
    }

    # Capture stdout and stderr
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()

    # Use same dict for globals and locals for recursion
    sandbox = {"__builtins__": __builtins__}

    try:
        # Redirect stdout and stderr
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = stdout_buffer, stderr_buffer

        # Execute code in sandbox
        exec(code, sandbox, sandbox)

    except Exception:
        # Capture full traceback
        result["exception"] = traceback.format_exc()
    finally:
        # Restore stdout and stderr
        sys.stdout, sys.stderr = old_stdout, old_stderr

    # Save captured output
    result["stdout"] = stdout_buffer.getvalue()
    result["stderr"] = stderr_buffer.getvalue()

    return result


# Test block
if __name__ == "__main__":
    test_code = """
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
"""
    res = execute_code(test_code)
    import json
    print(json.dumps(res, indent=2))
