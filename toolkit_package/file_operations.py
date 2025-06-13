# file_operations.py

# File Handling Functions

def write_to_file(filename, content):
    """
    Appends content to a text file.
    Creates the file if it doesn't exist.
    """
    try:
        with open(filename, "a") as file:
            file.write(content + "\n")
        print("Content written successfully.")
    except Exception as e:
        print("Error writing to file:", e)

def read_file(filename):
    """
    Reads and prints content of the file.
    """
    try:
        with open(filename, "r") as file:
            print("File Content:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error reading file:", e)

def clear_file(filename):
    """
    Deletes content of the file by opening it in write mode.
    """
    try:
        with open(filename, "w") as file:
            file.write("")
        print("File cleared.")
    except Exception as e:
        print("Error clearing file:", e)
