# Python Development Practice Lab

A focused Python engineering workspace for building reliable, maintainable software. It covers the language and development practices that support larger software engineering, data analysis, and machine learning projects.

The repository is intentionally practical: each topic is represented by executable code, reusable functions, tests, small applications, and problem-solving exercises. It complements project work in analytics and machine learning by strengthening the Python development layer underneath those workflows.

## Focus areas

- Python language fundamentals, control flow, and data structures
- Functions, modules, exceptions, file formats, and standard-library tooling
- Object-oriented design, composition, inheritance, and encapsulation
- Iterators, generators, decorators, type hints, dataclasses, and enums
- Automated testing with pytest and code quality checks with Ruff
- Command-line applications and small domain-focused projects
- Searching, sorting, recursion, frequency counting, and complexity analysis

## Repository map

| Directory | Purpose |
| --- | --- |
| `01_basics` - `04_functions` | Core Python language and reusable function patterns |
| `05_intermediate_python` | Files, JSON, CSV, exceptions, modules, and comprehensions |
| `06_object_oriented_programming` | Classes, object design, inheritance, and polymorphism |
| `07_advanced_python` | Iteration, generators, decorators, typing, and dataclasses |
| `08_testing` | Deterministic pytest examples and error-path tests |
| `09_mini_projects` | Calculator, student management, expense tracking, contacts, and file organization |
| `10_problem_solving` | Interview-style problems with examples and complexity notes |
| `docs` | Learning notes and Python interview reference material |

## Requirements

- Python 3.11 or newer
- The lessons use the Python standard library.
- Development checks use pytest and Ruff.

## Setup

From PowerShell:

```powershell
cd python-practice-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Usage

Run an example directly:

```powershell
python .\01_basics\variables_datatypes.py
python .\05_intermediate_python\json_handling.py
python .\09_mini_projects\calculator\calculator.py add 2 3
```

For each topic, read the module docstring, run the example, inspect the implementation, and extend the exercise functions with your own test cases.

## Verification

Run the complete local quality checks from the repository root:

```powershell
python -m pytest
python -m compileall -q .
python -m ruff check .
```

## Development direction

The lab provides a compact foundation for production-oriented Python work: clear interfaces, validation, error handling, type hints, automated tests, and maintainable project structure. Natural next steps are packaging, database-backed applications, APIs, profiling, CI, and applying these practices within data analysis and machine learning systems.

---

## LeetCode Practice Progress

Solving Data Structures and Algorithms problems using Python.

| Problem # | Problem Name | Topic | Difficulty | Time Complexity |
|---|---|---|---|---|
| 1 | Two Sum | Hash Map | Easy | O(n) average |
| 125 | Valid Palindrome | Two Pointers | Easy | O(n) |
| 217 | Contains Duplicate | Hash Set | Easy | O(n) average |
| 704 | Binary Search | Binary Search | Easy | O(log n) |

### Topics Practiced

- Arrays and Strings
- Hash Maps and Hash Sets
- Two Pointers
- Binary Search

### Learning Approach

1. Understand the problem.
2. Implement the solution in Python.
3. Test different inputs.
4. Analyze time and space complexity.
5. Push the solution to GitHub.

**Language:** Python 3

**Platform:** LeetCode
