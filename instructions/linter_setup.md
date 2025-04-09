# Linter setup

Instructions on setting up a linter for Python project on Ruff example

## [Ruff](https://docs.astral.sh/ruff/)
New, fast-growing linter.

**Advantages**:
- speed is 10-100 times faster than its analogues (implemented on Rust)
- completely replaces flake8 and isort
- has already gained recognition in large projects.
- 2-in-1: linter + formatting
- caching

## Installing and Using Ruff

### Install

`pip install ruff`

Verify installation by running `ruff --version`

### Run Ruff

On a Python file or directory: `ruff check path/to/your/code`

Ruff will analyze Python files and report any issues found

For testing you can use `/code/linter_test.py`

### Create a configuration file 

`pyproject.toml` to customize Ruff's behavior:

```toml
[tool.ruff]
line-length = 88
select = ["E", "F", "W"]
```

After creating the `pyproject.toml` file with Ruff configuration, 
Ruff will automatically use it when you run the ruff command in the 
directory containing the file.

The select option in the `pyproject.toml` file for Ruff specifies which 
categories of linting errors you want Ruff to check for. 

Here's what each code stands for:

- E: Errors related to PEP 8, the style guide for Python code.
- F: Pyflakes codes, which are typically related to logical errors like using 
undefined variables or importing unused modules.
- W: Warnings, which might include stylistic issues or potential problems that 
aren't necessarily errors.
- C: Cyclomatic complexity checks. 
- N: Naming conventions. 
- Q: Quotes (single vs. double). 
- B: Bugs and potential errors not covered by other categories. 
- S: Security issues. 
- T: Type hints and annotations. 
- R: Refactoring suggestions.

By specifying select = ["E", "F", "W"], you're instructing Ruff to check for
all errors, logical mistakes, and warnings in your code.
