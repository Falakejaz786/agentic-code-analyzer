# main.py
from nodes import syntax_analysis, static_analysis, complexity, sandbox_exec
from utils.gemini_api import call_gemini

def analyze_code_agent(code: str) -> dict:
    """
    Main agentic workflow:
    1. Syntax check
    2. Static analysis (pylint + mypy)
    3. Complexity analysis
    4. Safe execution
    5. LLM suggestions (Gemini)
    """
    # Step 1: Syntax Analysis
    syntax_result = syntax_analysis.check_syntax(code)
    if not syntax_result["is_valid"]:
        return {
            "syntax_error": syntax_result["error"],
            "message": "Code has syntax errors, cannot proceed further."
        }

    # Step 2: Static Analysis
    static_result = static_analysis.analyze_code(code)

    # Step 3: Complexity Analysis
    complexity_result = complexity.analyze_complexity(code)

    # Step 4: Sandbox Execution
    execution_result = sandbox_exec.execute_code(code)

    # Step 5: Prepare prompt for Gemini
    prompt = f"""
You are an expert Python developer. Analyze the following code:

{code}

1. Syntax issues: {syntax_result}
2. Lint/type issues: {static_result}
3. Complexity: {complexity_result}
4. Execution results: {execution_result}

Provide:
- Bug fixes (if any)
- Optimizations suggestions
- Code improvements
Return the fixed code and explanations.
"""
    # Call Gemini only if API key exists
    try:
        llm_suggestions = call_gemini(prompt) if call_gemini else "Gemini API not configured."
    except Exception as e:
        llm_suggestions = f"Error calling Gemini API: {str(e)}"

    return {
        "syntax_result": syntax_result,
        "static_result": static_result,
        "complexity_result": complexity_result,
        "execution_result": execution_result,
        "llm_suggestions": llm_suggestions
    }


# Test CLI
if __name__ == "__main__":
    user_code = """
def add(a, b):
    return a + b

x = add("1", 2)
print(x)
"""
    result = analyze_code_agent(user_code)
    import json
    print(json.dumps(result, indent=2))
