'''
PR.7 MODULAR AND PACKAGE

Create a Python-based Multi-Utility Toolkit that integrates multiple standard modules, custom
modules, and packages to perform a variety of tasks. This project will demonstrate the effective
use of Python's modular structure and provide utility functions for date-time operations, 
mathematical computations, random data generation, and unique identifer creation.

'''

from toolkit_package import file_operations
from toolkit_package import math_utils
import datetime
import time
import math
import random
import uuid

def display_datetime():
    now = datetime.datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def date_difference():
    date1 = input("Enter first date (YYYY-MM-DD): ")
    date2 = input("Enter second date (YYYY-MM-DD): ")
    try:
        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        diff = abs(d2 - d1)
        print("Difference in days:", diff.days)
    except Exception as e:
        print("Invalid date format. Try again.")

def stopwatch():
    input("Press Enter to start stopwatch.")
    start = time.time()
    input("Press Enter to stop stopwatch.")
    end = time.time()
    print("Elapsed Time: {:.2f} seconds".format(end - start))

def countdown_timer():
    seconds = int(input("Enter time in seconds: "))
    while seconds:
        print("Time left:", seconds, "seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    length = int(input("Enter password length: "))
    password = "".join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)

def generate_uuid():
    print("UUID1:", uuid.uuid1())
    print("UUID4:", uuid.uuid4())

def explore_module():
    mod_name = input("Enter module name (e.g., math, random): ")
    try:
        module = __import__(mod_name)
        print("Attributes of module", mod_name, "are:")
        print(dir(module))
    except Exception as e:
        print("Module not found or error occurred.")

def math_operations_menu():
    print("\nMath Utilities:")
    print("1. Compound Interest")
    print("2. Area of Shapes")
    print("3. Factorial")
    print("4. Log base 10")
    print("5. Trigonometric Functions")
    choice = input("Enter your choice: ")

    if choice == "1":
        p = float(input("Enter principal: "))
        r = float(input("Enter rate: "))
        t = float(input("Enter time: "))
        result = math_utils.calculate_compound_interest(p, r, t)
        print("Compound Interest:", result)

    elif choice == "2":
        shape = input("Enter shape (square/rectangle/circle): ").lower()
        if shape == "square":
            side = float(input("Enter side: "))
            print("Area:", math_utils.calculate_area(shape, side))
        elif shape == "rectangle":
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            print("Area:", math_utils.calculate_area(shape, l, b))
        elif shape == "circle":
            r = float(input("Enter radius: "))
            print("Area:", math_utils.calculate_area(shape, r))
        else:
            print("Invalid shape.")

    elif choice == "3":
        n = int(input("Enter number: "))
        print("Factorial:", math_utils.factorial(n))

    elif choice == "4":
        n = float(input("Enter number: "))
        print("Log base 10:", math_utils.log_base_10(n))

    elif choice == "5":
        angle = float(input("Enter angle in degrees: "))
        trig = math_utils.trigonometry_functions(angle)
        print("sin:", trig["sin"], "cos:", trig["cos"], "tan:", trig["tan"])
    else:
        print("Invalid choice.")

def main_menu():
    while True:
        print("\n--- Multi Utility Toolkit ---")
        print("1. Show Date and Time")
        print("2. Date Difference")
        print("3. Stopwatch")
        print("4. Countdown Timer")
        print("5. Math Operations")
        print("6. Generate Password")
        print("7. Generate UUID")
        print("8. Explore Module")
        print("9. File - Write")
        print("10. File - Read")
        print("11. File - Clear")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_datetime()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            stopwatch()
        elif choice == "4":
            countdown_timer()
        elif choice == "5":
            math_operations_menu()
        elif choice == "6":
            generate_password()
        elif choice == "7":
            generate_uuid()
        elif choice == "8":
            explore_module()
        elif choice == "9":
            data = input("Enter text to write: ")
            file_operations.write_to_file("log.txt", data)
        elif choice == "10":
            file_operations.read_file("log.txt")
        elif choice == "11":
            file_operations.clear_file("log.txt")
        elif choice == "12":
            print("Exiting Toolkit. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
