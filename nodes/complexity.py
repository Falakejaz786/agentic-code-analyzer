# nodes/complexity.py
import radon.complexity as radon_cc  # type: ignore

def analyze_complexity(code: str) -> dict:
    """
    Analyze Python code for cyclomatic complexity using Radon.
    
    Returns a dictionary with:
    - functions: list of functions and their complexity
    - average_complexity: average complexity of all functions
    - suggestions: tips based on complexity
    """
    try:
        # Analyze code
        results = radon_cc.cc_visit(code)
        functions_info = []
        total_complexity = 0

        for item in results:
            if hasattr(item, "complexity") and hasattr(item, "name"):
                functions_info.append({
                    "name": item.name,
                    "complexity": item.complexity,
                    "lineno": item.lineno
                })
                total_complexity += item.complexity

        avg_complexity = total_complexity / len(functions_info) if functions_info else 0

        # Generate suggestions
        suggestions = [
            f"Function '{f['name']}' is complex (CC={f['complexity']}). Consider refactoring."
            for f in functions_info if f["complexity"] > 10
        ]

        return {
            "functions": functions_info,
            "average_complexity": avg_complexity,
            "suggestions": suggestions
        }

    except Exception as e:
        return {"error": str(e)}

# Test block
if __name__ == "__main__":
    test_code = """
def add(a, b):
    return a + b

def complex_func(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                print(i)
            else:
                print(-i)
"""
    result = analyze_complexity(test_code)
    print(result)
