# 🧠 SmartCalc — A CLI Calculator with Exception Handling

SmartCalc is a command-line calculator that does more than basic arithmetic—it showcases robust Python error handling. Designed as a hands-on project to demonstrate understanding of `try`, `except`, `else`, and `finally`, this script accepts user input, validates it, performs calculations, and handles errors smoothly.

##  Key Features

- **Flexible Input Formatting**  
  Accepts both spaced (`5 + 2`) and unspaced (`5+2`) expressions
- **Comprehensive Operation Support**  
  Handles `+`, `-`, `*`, `/`, and `**` (exponentiation)
- **Robust Error Handling**  
  Gracefully manages:
  - Division by zero attempts
  - Invalid number formats
  - Unsupported operators
  - Unexpected input structures
- **Clean User Experience**  
  Maintains operation flow with `finally` block
  - Clear, specific error messages
  - Persistent calculator session until explicit exit

##  What I Learned

While building SmartCalc, I deepened my practical understanding of:
- Python's exception hierarchy
- The importance of specific error catching vs broad `Exception`
- How `try/except/else/finally` work together in real applications
- User input validation techniques
- The balance between flexibility and strict input requirements

## 🛠️ Implementation Highlights

```python
# Example of the core error handling structure
try:
    # Parse and validate user input
    # Perform calculation
except ZeroDivisionError:
    # Special handling for math error
except ValueError:
    # Handle input format issues
except Exception:
    # Catch-all for unexpected errors
else:
    # Success case output
finally:
    # Ensure clean state for next operation