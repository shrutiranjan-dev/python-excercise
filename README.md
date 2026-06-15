# 🐍 Python Phase 1 — Fundamentals

### From Node.js to AI Engineering

> **Master Python fundamentals through the lens of an experienced backend developer.**
> No hand-holding. Real concepts. Real code. Real AI relevance.

---

## 📌 Badges

![Python](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-beta-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Style](https://img.shields.io/badge/code%20style-PEP%208-ff69b4)

---

## 📖 Overview

Python is the **lingua franca** of AI/ML engineering. This course is designed exclusively for **backend developers** — especially those coming from **Node.js / TypeScript** — who want to pivot into **AI Engineering**.

We skip the "what is a computer" nonsense and jump straight into:
- Python's type system compared to JavaScript/TypeScript
- Idiomatic Python patterns (not "writing JS in Python")
- Real-world AI engineering patterns from day one
- Production-ready code standards (PEP 8, type hints, dataclasses)

By the end of Phase 1, you will have written **200+ exercises**, **2 real projects**, and be comfortable reading/writing production Python code.

---

## 🎯 Target Audience

| Background | Why This Course |
|---|---|
| Node.js / Express backend devs | Python is required for AI/LLM engineering |
| Full-stack JS devs | You already know programming — learn *Python* |
| Engineers pivoting to AI | All AI tooling (PyTorch, HuggingFace, LangChain) is Python-first |
| CS students who know Java/C# | Python is different — unlearn your verbosity |

This course is **NOT** for:
- Absolute beginners who have never programmed
- People who want slow-paced tutorials
- Anyone looking for a "learn Python in 24 hours" gimmick

---

## ✅ Prerequisites

- **Programming experience**: ≥1 year in any language (JS, TS, Java, C#, Go, Rust)
- **JavaScript familiarity** helpful for comparison tables throughout
- **Terminal comfort**: navigating directories, running scripts
- **Python 3.12+** installed locally
- **A code editor** (VS Code recommended with Python extension)

If you can write a `for` loop, understand functions, and know what a type error is — you're ready.

---

## 🧠 Learning Philosophy

```
┌──────────────────────────────────────────────┐
│         The 80/20 Rule of Python              │
│                                              │
│  20% syntax  →  80% of what you write        │
│  20% idioms  →  80% of what you read         │
│  20% tooling →  80% of professional output   │
└──────────────────────────────────────────────┘
```

### How this course works:

1. **Explanation first** — Read the `explanation.md` in each module
2. **Study examples** — Levels 0→5, from trivial to production-grade
3. **Fill in the blanks** — Guided muscle memory (`fill_blanks.py`)
4. **Solve exercises** — Open-ended problems (`exercises.py`)
5. **Build the project** — Apply everything in a surprise project

Each file is self-contained. Open it in your editor and work through it line by line.

---

## 📚 Module Overview

| # | Module | Concepts | AI Relevance | Exercises |
|---|---|---|---|---|
| 01 | Variables & Types | `int`, `float`, `str`, `bool`, `None`, `type()`, dynamic typing, `dataclass` | Model configs, token counts, confidence scores | 35 + project |
| 02 | Operators | `+`, `-`, `*`, `/`, `//`, `%`, `**`, `==`, `!=`, `is`, `in`, `and`/`or`/`not` | Threshold checks, RAG membership, cost calc | 35 + project |
| 03 | Strings & Formatting | F-strings, `.format()`, slicing, `.split()`, `.join()`, `.strip()`, regex | Prompt engineering, text preprocessing | 35 + project |
| 04 | Collections (Lists) | `list`, `append`, `extend`, slicing, comprehensions, sorting | Dataset management, batch processing | 35 + project |
| 05 | Collections (Dicts & Sets) | `dict`, `set`, `defaultdict`, `Counter`, merging, views | Token vocab, embedding lookups, dedup | 35 + project |
| 06 | Tuples & Unpacking | `tuple`, immutability, unpacking, `*args`, `**kwargs`, namedtuple | Fixed configs, return values, function signatures | 30 + project |
| 07 | Control Flow | `if`/`elif`/`else`, `match`/`case` (3.10+), ternary, truthiness | Guard clauses, model routing, fallback logic | 35 + project |
| 08 | Loops & Iteration | `for`, `while`, `range`, `enumerate`, `zip`, `break`/`continue`/`else` | Epoch loops, data streaming, batch iteration | 35 + project |
| 09 | Functions | `def`, `return`, default args, `*args`/`**kwargs`, lambdas, closures, decorators | Pipeline functions, callbacks, wrapping API calls | 35 + project |
| 10 | Error Handling | `try`/`except`/`else`/`finally`, custom exceptions, `raise` | API error handling, rate limits, retry logic | 30 + project |
| 11 | File I/O | `open()`, `with`, `.read()`/`.write()`, `json`, `csv`, `pathlib` | Data loading, config files, logging | 30 + project |
| 12 | Modules & Imports | `import`, `from`, `__name__`, `if __name__`, packages, `sys.path` | Package structure, modular AI pipelines | 25 + project |
| 13 | Virtual Environments | `venv`, `pip`, `requirements.txt`, `pyproject.toml`, `pip freeze` | Reproducible AI environments | 15 + project |
| 🏁 | Capstone Project | All modules combined | End-to-end AI tool | 1 large project |

---

## 🚀 How to Use This Repository

```bash
# 1. Clone the repository
git clone <repo-url>
cd python-phase-1-fundamentals

# 2. Start with Module 01
cd 01_variables_and_types

# 3. Read the explanation
# Open explanation.md in your editor

# 4. Run the examples
python examples.py

# 5. Work through fill_blanks.py
python fill_blanks.py

# 6. Solve exercises.py
# Edit the file and run it
python exercises.py

# 7. Build the surprise project
cd surprise_project
python solution.py  # See the expected solution first
# Then build your own version from project.md
```

### Workflow Tip

For each module, follow this exact sequence. Do NOT skip the fill-in-the-blanks — they build muscle memory. Do NOT look at the exercise solutions before trying for at least 15 minutes.

---

## 📁 Project Structure

```
python-phase-1-fundamentals/
│
├── README.md                          ← You are here
├── AGENTS.md                           ← Course conventions (opencode AI)
│
├── 01_variables_and_types/
│   ├── explanation.md                  ← Deep dive into concepts
│   ├── examples.py                     ← Level 0→5 runnable examples
│   ├── fill_blanks.py                  ← Guided practice (25+ exercises)
│   ├── exercises.py                    ← Open-ended problems (35 exercises)
│   └── surprise_project/
│       ├── project.md                  ← Project specification
│       └── solution.py                 ← Complete solution with comments
│
├── 02_operators/
│   └── ...                             ← Same structure as Module 01
│
├── 03_strings/
│   └── ...
│
├── 04_lists/
│   └── ...
│
├── 05_dicts_and_sets/
│   └── ...
│
├── 06_tuples/
│   └── ...
│
├── 07_control_flow/
│   └── ...
│
├── 08_loops/
│   └── ...
│
├── 09_functions/
│   └── ...
│
├── 10_error_handling/
│   └── ...
│
├── 11_file_io/
│   └── ...
│
├── 12_modules/
│   └── ...
│
├── 13_venv/
│   └── ...
│
└── capstone/
    └── ...
```

---

## 🧭 Progression Path

```
Phase 1 ─► Phase 2 ─► Phase 3 ─► Phase 4 ─► Phase 5 ─► Phase 6 ─► Phase 7
Fund.       Data&Libs    AI/ML       LLMs        Production   Deployment  MLOps

Phase 1: Python Fundamentals        ← You are here
Phase 2: NumPy, Pandas, Matplotlib  ← Data manipulation & visualization
Phase 3: Scikit-learn, ML basics    ← Traditional ML algorithms
Phase 4: Transformers, LangChain    ← LLMs, RAG, prompt engineering
Phase 5: FastAPI, async, testing    ← Production AI services
Phase 6: Docker, cloud, CI/CD       ← Deployment & infrastructure
Phase 7: Kubeflow, monitoring       ← Production ML pipelines
```

Each phase builds on the previous. You cannot skip Phase 1.

---

## 📊 Assessment Rubric

| Level | Description | Score |
|---|---|---|
| **Novice** | Can read Python, struggles to write without reference | 0-20% |
| **Advanced Beginner** | Can write basic scripts with lookups | 21-40% |
| **Competent** | Writes idiomatic Python, understands type system | 41-60% |
| **Proficient** | Writes production code, uses type hints, debug fluently | 61-80% |
| **Expert** | Deep understanding of internals, optimization, patterns | 81-100% |

### Module Completion Criteria

- [ ] All `fill_blanks.py` exercises completed with ≤2 errors
- [ ] All `exercises.py` problems solved without looking at solutions
- [ ] Surprise project builds and passes all test cases
- [ ] Can explain every line of `solution.py`
- [ ] Can teach the concepts to another developer

---

## 🎯 Expected Outcomes

After completing Phase 1, you will:

1. **Write Python** that doesn't look like JavaScript
2. **Understand Python's type system** (dynamic but strong)
3. **Use idiomatic patterns** — list comprehensions, unpacking, context managers
4. **Read production Python code** in AI repos (HuggingFace, LangChain, etc.)
5. **Debug effectively** using `type()`, `print()`, and reading tracebacks
6. **Structure projects** properly using modules and virtual environments
7. **Be ready for Phase 2** (NumPy, Pandas, data manipulation)

You will have written:
- **~450 exercises** across 13 modules
- **13 surprise projects** (one per module)
- **1 capstone project** combining everything

---

## 🤝 Contribution Guidelines

We welcome contributions! Here's how:

1. **Found a typo?** Open a PR with the fix
2. **Bug in an exercise?** File an issue with the module number and problem
3. **Want to add an exercise?** Open a PR — maintain the same format and level structure
4. **Suggestions for improvement?** Start a discussion

### Style Guide

- All Python code must be **PEP 8** compliant
- Use **Python 3.12+** features where appropriate
- Every example must have **expected output in comments**
- Exercises must have **solutions at the bottom** (not inline)
- `fill_blanks.py` must have **hints** and a **solutions section**

---

## 📄 License

MIT License. See `LICENSE` file for details.

---

<p align="center">
  <strong>From Node.js to AI Engineering</strong><br>
  <em>One Python file at a time.</em>
</p>
