---

```markdown
# 🧠 Agentic Code Analyzer

Agentic Code Analyzer is an AI-powered coding assistant that **analyzes Python code**, detects errors, computes complexity, executes safely in a sandbox, and provides **LLM-based improvement suggestions** using Google Gemini API — all through an elegant web interface.

---

## 🌐 Live Demo

- 🔹 **Frontend (Vercel):** [agentic-code-analyzer.vercel.app](https://agentic-code-analyzer.vercel.app)
- 🔹 **Backend (Render):** [agentic-code-analyzer-3.onrender.com](https://agentic-code-analyzer-3.onrender.com)

---

## 🧰 Tech Stack

| Frontend | Backend | AI/ML | Deployment |
|-----------|----------|--------|-------------|
| HTML, CSS, JavaScript | FastAPI | Gemini API | Vercel (Frontend), Render (Backend) |

---

## ⚙️ Features

- 🧩 **Syntax Analysis** – Detects syntax errors and invalid code structures  
- 🧠 **Static Analysis** – Integrates with Pylint & Mypy for type and lint checks  
- 📊 **Complexity Analysis** – Evaluates cyclomatic complexity for performance insights  
- ⚙️ **Secure Execution** – Runs user code in a sandboxed environment  
- 💬 **AI Suggestions (Gemini)** – Explains, fixes, and improves code intelligently  
- 🎨 **Modern UI** – Sleek, minimal interface for smooth code analysis  

---

## 🚀 How It Works

1. **Frontend (Vercel)**  
   Users paste Python code into the web interface and click *Analyze Code*.  
2. **Backend (Render)**  
   - Receives the code through a FastAPI endpoint (`/analyze`)  
   - Runs syntax, static, and complexity checks  
   - Executes code safely in a sandbox  
   - Calls **Gemini API** for natural-language analysis  
3. **Frontend displays results**  
   The output includes syntax validation, execution output, AI suggestions, and complexity score.  

---

## 🧠 Example Output

```

🧠 Agentic Code Analyzer
def read_file(filename):
try:
with open(filename, "r") as f:
return f.read()
except FileNotFoundError:
return "File not found!"

print(read_file("test.txt"))

Analyze Code
🧩 Syntax Check:
✅ No errors
🧠 Static Analysis:
Pylint & Mypy report: Success: no issues found
📊 Complexity:
Average = 2
⚙️ Execution Output:
File not found!
💡 Gemini Suggestions:
This code is correct and executes as expected. No bugs detected.

```

---

## 🔒 Environment Variables

Create a `.env` file in your project root (not committed to GitHub):

```

GEMINI_API_KEY=your_api_key_here

```

> ⚠️ Make sure `.env` is included in your `.gitignore` before committing.

---

## 🧠 Future Enhancements

- Add support for **multi-language code analysis**  
- Integrate **real-time AI explanations** while typing  
- Add **code refactoring and optimization metrics**  
- Include **user authentication and history tracking**

---

```

---

Would you like me to make a **LinkedIn post caption** for this project too? (short, catchy, and recruiter-friendly)
