"""Simple Calculator Application for DevSecOps Lab."""


def add(a, b):
    """Return the addition of a and b."""
    return a + b


def subtract(a, b):
    """Return the subtraction of b from a."""
    return a - b


def multiply(a, b):
    """Return the multiplication of a and b."""
    return a * b


def divide(a, b):
    """Return the division of a by b. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulus(a, b):
    """Return the modulus of a by b. Raises ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot perform modulus by zero")
    return a % b


if __name__ == "__main__":
    print("=" * 30)
    print("   Simple Calculator")
    print("=" * 30)
    print(f"  Addition:       {add(10, 5)}")
    print(f"  Subtraction:    {subtract(10, 5)}")
    print(f"  Multiplication: {multiply(10, 5)}")
    print(f"  Division:       {divide(10, 5)}")
    print(f"  Modulus:        {modulus(11, 5)}")
    print("=" * 30)

