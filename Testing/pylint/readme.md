# 🧪 Pylint Practice

Compare Pylint results between poorly-written and well-structured Python code.

## Files

- `simple1.py` - Bad code (missing docstring, undefined variable, poor naming)
- `simple2.py` - Good code (proper docstrings, clean syntax)

## Usage

1. Install Pylint:
```bash
pip install pylint

2.Run linting:

```bash
pylint simple1.py  # Expect low score (0.00/10)
pylint simple2.py  # Expect high score (~10/10)

3.Execute scripts:

```bash
python simple1.py  # Will raise NameError
python simple2.py  # Will execute correctly

