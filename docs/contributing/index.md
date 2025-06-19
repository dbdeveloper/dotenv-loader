---
title: Contributing
---
# 🛠 CONTRIBUTING.md

## 📌 Purpose

This guide provides all necessary instructions for developers who want to:

- Run or contribute to the `dotenv-loader` project.
- Understand the test layout and configuration resolution logic.
- Set up a local development environment.
- Publish the package to PyPI.
- Ensure consistent development and testing practices.

If you plan to submit a pull request or maintain the package — **this is your go-to reference**.

## 🧩 Requirements

- Python **3.8 or higher**
- Git
- `pip` (Python package manager)
- Unix-like system recommended (Linux/macOS) — but Windows is supported.

Optional (but recommended):

- `venv` or `virtualenv`
- `pytest`, `coverage`, `twine`, `build`
- `black`, `flake8`, `mypy` for static checks and formatting

## 📦 Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dbdeveloper/dotenv-loader.git
cd dotenv-loader
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dev Dependencies

```bash
pip install -r requirements-dev.txt
```

Or manually:

```bash
pip install -e .[dev,test]
```
Optional (for static checking and formatting):

```txt
black
flake8
mypy
```

## 🪪 Running Tests

### Run all tests:

```bash
pytest
```

### Run with verbose output:

```bash
pytest -v
```

### Run with code coverage:

```bash
pytest --cov=dotenv_loader --cov-report=term-missing
```

> The `.coveragerc` file (optional) can be added if you want to fine-tune what's included.

## 🧼 Cleaning Up

To remove Python cache and temporary test files:

```bash
find . -type d -name "__pycache__" -exec rm -r {} +
rm -rf .pytest_cache .coverage dist build
```

## 🧲 What’s Tested

- Default `.env` loading from project root
- Use of `DOTPROJECT`, `DOTSTAGE`, and `DOTENV` overrides
- Custom `config_root`, `steps_to_project_root`, and other arguments
- Environment variable vs parameter priority
- Fallbacks and error handling (e.g., missing or invalid files)
- Resolution path combinations via environment or arguments

---

## 📁 Project Structure (Developer View)

```bash
dotenv-loader/
│
├── src/dotenv_loader/         # Main loader logic
│   └── __init__.py
│
├── tests/                     # Tests for full path resolution logic
│   ├── test_dotenv_loader.py
│   ├── proj1/
│   │   └── manage.py
│   ├── proj2/
│   │   ├── app/
│   │   └── manage.py
│   └── dotconfig_root/        # Configs: ~/.config/python-projects (mocked)
│       ├── proj1/.env
│       ├── proj2/.env
│       └── ...
│
├── pyproject.toml             # Metadata for PyPI
├── requirements-dev.txt       # Dev dependencies
├── .gitignore
├── .coveragerc (optional)
└── CONTRIBUTING.md             # This file
```

---

## 📦 Publishing to PyPI

Ensure the following before publishing:

- All tests pass.
- Version in `pyproject.toml` is updated.
- `README.md` is correct and well-formatted (rendered by PyPI).
- `LICENSE` (MIT) is present.

### 📜 Publishing Steps

1. Build the package:

```bash
python -m build
```

2. Inspect the output under `dist/`. It should include:

```
dist/dotenv_loader-X.Y.Z.tar.gz
dist/dotenv_loader-X.Y.Z-py3-none-any.whl
```

3. Upload to PyPI:

```bash
twine upload dist/*
```

4. (Optional) If publishing for the first time, create an account at https://pypi.org/account/register

### 🛡 Notes

- Credentials can be stored in `~/.pypirc`.
- You can test publishing using [TestPyPI](https://test.pypi.org/) by replacing `twine upload` with:

```bash
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

### 💻 Automate it (Optional)

Steps 1,2,3 can be automated by executing the script `tools/publish.sh`

## ✅ GitHub CI/CD (Optional but Recommended)

Your `ci.yml` workflow ensures:

- Tests are run on every `push` and `pull_request`.
- Uses Python 3.12.
- Fails early if tests do not pass.

You can enable code coverage via `codecov.io` for 100% badges.

---

## 🤝 Contribution Guidelines

- Follow PEP8.
- Write tests for every feature or bug fix.
- Use readable comments and docstrings.
- Follow the structure of existing tests.

---

## 🤖 Acknowledgment

This project was created collaboratively by **Vladyslav Kozlovskyy** with the help of ChatGPT (OpenAI), using models GPT-4o, GPT-4.5, and GPT-3.5 — to combine human clarity with AI precision.

