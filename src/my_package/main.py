"""
Main program file
"""

from .utils import add_numbers, calculate_average, save_data


def process_numbers(numbers):
    """Process a list of numbers and return results"""
    print(f"Processing {len(numbers)} numbers...")
    
    # Calculate some basic stats
    total = sum(numbers)
    average = calculate_average(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    results = {
        'total': total,
        'average': average,
        'max': maximum,
        'min': minimum,
        'count': len(numbers)
    }
    
    return results


def run_simple_demo():
    """Run a simple demonstration"""
    # Some sample data
    my_numbers = [10, 20, 30, 40, 50]
    
    print("=== Simple Demo ===")
    print(f"Numbers: {my_numbers}")
    
    # Process the numbers
    results = process_numbers(my_numbers)
    
    # Show results
    print("\nResults:")
    for key, value in results.items():
        print(f"{key}: {value}")
    
    # Save results to file
    save_data(results, "results.txt")


def main():
    """Main function - runs when script is executed"""
    run_simple_demo()


if __name__ == "__main__":
    main()