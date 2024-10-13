# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division and handle potential errors."""
    try:
        # Attempt to convert arguments to float
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
