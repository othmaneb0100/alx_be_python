# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / den}"
    except ValueError:
        return "Error: Please enter numeric values only."

# If you want to add some quick test cases for the function
if __name__ == "__main__":
    print(safe_divide("10", "5"))  # Should return "The result of the division is 2.0"
    print(safe_divide("10", "0"))  # Should return "Error: Cannot divide by zero."
    print(safe_divide("ten", "5"))  # Should return "Error: Please enter numeric values only."
