#  Python Comparison Operators

This module covers the fundamentals of comparison operators and how Python supports chained comparisons for clean and readable code.

---

##  01 - Basic Comparison Operators

| Operator | Description                                                   | Example            |
|----------|---------------------------------------------------------------|--------------------|
| `==`     | Equal to                                                      | `(a == b)`         |
| `!=`     | Not equal to                                                  | `(a != b)`         |
| `>`      | Greater than                                                  | `(a > b)`          |
| `<`      | Less than                                                     | `(a < b)`          |
| `>=`     | Greater than or equal to                                      | `(a >= b)`         |
| `<=`     | Less than or equal to                                         | `(a <= b)`         |

Each operator returns a boolean value: `True` or `False`.

---

## 🔗 02 - Chained Comparison Operators

Python allows chaining multiple comparisons in a clean and readable way:

```python
print(1 < 2 < 3)                  # True
print(1 < 2 and 2 < 3)            # True
print(1 < 3 > 2)                  # True
print(1 < 3 and 3 > 2)            # True
print(1 == 2 or 2 < 3)            # True
print(1 == 1 or 100 == 1)         # True
