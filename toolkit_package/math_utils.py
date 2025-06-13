# math_utils.py

import math

# Basic math utility functions

def calculate_compound_interest(p, r, t):
    """
    Formula: A = P * (1 + r/100) ** t
    """
    try:
        amount = p * (1 + r/100) ** t
        return amount
    except Exception as e:
        print("Error calculating compound interest:", e)

def calculate_area(shape, *dimensions):
    """
    Calculates area for basic shapes: square, rectangle, circle
    """
    if shape == "square":
        return dimensions[0] ** 2
    elif shape == "rectangle":
        return dimensions[0] * dimensions[1]
    elif shape == "circle":
        return math.pi * (dimensions[0] ** 2)
    else:
        return "Unknown shape"

def factorial(n):
    return math.factorial(n)

def log_base_10(n):
    return math.log10(n)

def trigonometry_functions(angle_degree):
    rad = math.radians(angle_degree)
    return {
        "sin": math.sin(rad),
        "cos": math.cos(rad),
        "tan": math.tan(rad)
    }
