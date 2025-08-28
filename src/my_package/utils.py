"""
Simple utility functions
"""

def add_numbers(a, b):
    """Add two numbers together"""
    return a + b


def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b


def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def save_data(data, filename):
    """Save data to a text file"""
    with open(filename, 'w') as file:
        file.write(str(data))
    print(f"Data saved to {filename}")


def load_data(filename):
    """Load data from a text file"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None