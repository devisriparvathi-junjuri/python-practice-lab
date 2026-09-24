# Python Practice Lab

A structured, executable curriculum for a B.Sc. Computer Science student preparing for software engineering, data analytics, and AI-related roles. Lessons are organized by Python concept, with small examples, exercises, reusable functions, tests, mini-projects, and problem-solving patterns.

## Learning objectives

- Build reliable Python fundamentals and problem-solving habits.
- Use collections, functions, exceptions, files, JSON, and CSV confidently.
- Design small object-oriented programs with clear responsibilities.
- Read and write type-hinted, tested, maintainable code.
- Practice common interview patterns and complexity analysis.

## Curriculum

1. Basics and control flow
2. Data structures and functions
3. Intermediate Python and object-oriented programming
4. Advanced Python and testing
5. Mini-projects and problem solving

## Requirements and setup

Python 3.11 or newer is recommended. From PowerShell:

```powershell
cd python-practice-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

The lessons themselves use only the standard library. `requirements-dev.txt` adds pytest and ruff for development checks.

## Running examples

Most lessons are standalone scripts:

```powershell
python .\01_basics\variables_datatypes.py
python .\05_intermediate_python\json_handling.py
python .\09_mini_projects\calculator\calculator.py add 2 3
```

Exercises intentionally contain functions and prompts you can extend. Read the module docstrings first.

## Running tests

```powershell
python -m pytest
python -m compileall -q .
python -m ruff check .
```

## Progress checklist

- [ ] Basics and control flow
- [ ] Data structures
- [ ] Functions
- [ ] Intermediate Python
- [ ] Object-oriented programming
- [ ] Advanced Python
- [ ] Testing
- [ ] Mini-projects
- [ ] Problem solving

## Mini-projects

Each project is independent and includes a focused README. Start with `09_mini_projects/calculator`, then try student management, expense tracking, contacts, and file organization.

## Future roadmap

Add a database-backed project, HTTP clients using a free local test server, pandas and NumPy for analytics, a small machine-learning workflow, packaging, CI, and profiling after the standard-library foundations feel comfortable.
