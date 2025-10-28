# nodes/static_analysis.py
import subprocess
import tempfile
import json
import sys

def run_pylint(code: str) -> dict:
    """
    Run pylint on the given Python code and return a structured result.
    """
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as tmp_file:
        tmp_file.write(code)
        tmp_file_path = tmp_file.name

    # Run pylint using python -m to ensure it works on Windows
    result = subprocess.run(
        [sys.executable, "-m", "pylint", tmp_file_path, "--disable=R,C", "--output-format=json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    try:
        pylint_output = json.loads(result.stdout) if result.stdout else []
    except json.JSONDecodeError:
        pylint_output = [{"error": result.stdout or result.stderr}]

    return {
        "pylint": pylint_output,
        "stderr": result.stderr
    }

def run_mypy(code: str) -> dict:
    """
    Run mypy on the given Python code and return the result.
    """
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as tmp_file:
        tmp_file.write(code)
        tmp_file_path = tmp_file.name

    result = subprocess.run(
        [sys.executable, "-m", "mypy", tmp_file_path, "--ignore-missing-imports"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    return {
        "mypy": result.stdout.strip(),
        "stderr": result.stderr.strip()
    }

def analyze_code(code: str) -> dict:
    """
    Combines pylint and mypy results for the given code.
    """
    pylint_result = run_pylint(code)
    mypy_result = run_mypy(code)

    return {
        "pylint": pylint_result,
        "mypy": mypy_result
    }

# Test block
if __name__ == "__main__":
    test_code = """
def add(a: int, b: int) -> int:
    return a + b

x = add("1", 2)
print(x)
"""
    result = analyze_code(test_code)
    import json
    print(json.dumps(result, indent=2))
