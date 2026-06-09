# Python - Test Driven Development

## Description

This project introduces Test Driven Development (TDD) in Python.

The main goal is to learn how to write tests before implementing code, document modules and functions properly, identify edge cases, and create reliable software through automated testing.

All tasks are completed using Python 3.8.5 on Ubuntu 20.04 LTS and follow the Holberton School requirements.

---

## Learning Objectives

At the end of this project, I should be able to explain:

- Why Python programming is awesome
- What an interactive test is
- Why tests are important
- How to write Docstrings to create tests
- How to document modules and functions
- How to execute doctests
- How to find and handle edge cases
- The principles of Test Driven Development (TDD)

---

## Requirements

### Python Scripts

- Ubuntu 20.04 LTS
- Python 3.8.5
- First line: `#!/usr/bin/python3`
- All files must be executable
- All files must end with a new line
- Code must follow pycodestyle 2.7.*

### Test Files

- Stored inside the `tests/` directory
- Extension: `.txt`
- Executed with:

```bash
python3 -m doctest ./tests/*
```

---

## Project Structure

```text
python-test_driven_development/
├── README.md
├── 0-add_integer.py
└── tests/
    └── 0-add_integer.txt
```

---

## Files

| File | Description |
|--------|-------------|
| `0-add_integer.py` | Function that adds two integers |
| `tests/0-add_integer.txt` | Doctest file for add_integer |

---

## Usage

Example:

```python
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
```

Output:

```text
3
```

Run tests:

```bash
python3 -m doctest ./tests/*
```

Check style:

```bash
pycodestyle *.py
```

---

## Author

Anthony Caban

Student at Holberton School