# Mystery Module

## Overview
The `mystery_module.py` file contains a Python function `fn_x` that solves quadratic equations of the form:

\[ ax^2 + bx + c = 0 \]

This function calculates the roots of the equation using the **Quadratic Formula**:

\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

The function determines the nature of the roots based on the discriminant \( \Delta = b^2 - 4ac \):
- If \( \Delta > 0 \): Two distinct real roots.
- If \( \Delta = 0 \): One real root (double root).
- If \( \Delta < 0 \): No real roots (returns `None`).

## Function Details

### `fn_x(a, b, c)`

#### Parameters:
- `a` (float): Coefficient of \( x^2 \) (must not be 0).
- `b` (float): Coefficient of \( x \).
- `c` (float): Constant term.

#### Returns:
- A tuple `(x1, x2)` containing the two roots if real roots exist.
- `None` if the equation has no real roots.

#### Example Usage:
```python
from mystery_module import fn_x

# Example 1: Two distinct real roots
a, b, c = 1, -5, 6
roots = fn_x(a, b, c)
print(roots)  # Output: (3.0, 2.0)

# Example 2: One real root (double root)
a, b, c = 1, -4, 4
roots = fn_x(a, b, c)
print(roots)  # Output: (2.0, 2.0)

# Example 3: No real roots
a, b, c = 1, 0, 1
roots = fn_x(a, b, c)
print(roots)  # Output: None
```

## Mathematical Background
The quadratic formula is derived from completing the square for the general quadratic equation \( ax^2 + bx + c = 0 \). The discriminant \( \Delta \) determines the nature of the roots:

- \( \Delta > 0 \): Two distinct real roots.
- \( \Delta = 0 \): One real root (double root).
- \( \Delta < 0 \): No real roots (complex roots).

## Example Equations

| Equation           | Parameters (a, b, c) | Roots          |
|--------------------|-----------------------|----------------|
| \( x^2 - 5x + 6 = 0 \) | 1, -5, 6             | (3.0, 2.0)    |
| \( x^2 - 4x + 4 = 0 \) | 1, -4, 4             | (2.0, 2.0)    |
| \( x^2 + 1 = 0 \)      | 1, 0, 1              | None          |
| \( 2x^2 + 3x - 2 = 0 \) | 2, 3, -2             | (0.5, -2.0)   |

## Notes
- Ensure that the coefficient `a` is not zero. If `a = 0`, the equation is not quadratic.
- The function does not handle complex roots; it returns `None` if the discriminant is negative.

## License
This module is provided as-is under the MIT License.