def check_syntax(code: str) -> dict:
    """
    Checks Python code for syntax errors without executing it.
    
    Returns a dictionary:
    {
        "is_valid": bool,
        "error": str (empty if no error)
    }
    """
    try:
        # Try to compile the code — this checks syntax
        compile(code, "<string>", "exec")
        return {"is_valid": True, "error": ""}
    except SyntaxError as e:
        return {
            "is_valid": False,
            "error": f"SyntaxError: {e.msg} at line {e.lineno}, offset {e.offset}"
        }
    except Exception as e:
        return {
            "is_valid": False,
            "error": f"Error: {str(e)}"
        }

# Test block (optional, can be removed in production)
if __name__ == "__main__":
    test_code = """
def add(a, b)
    return a + b
"""
    result = check_syntax(test_code)
    print(result)
