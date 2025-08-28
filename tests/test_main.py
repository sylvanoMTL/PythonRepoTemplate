"""
Simple tests for the main module
"""

import sys
from pathlib import Path

# Add the src directory to Python path
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

# Now import the functions we want to test
from my_package.main import process_numbers
from my_package.utils import add_numbers, calculate_average


def test_add_numbers():
    """Test the add_numbers function"""
    # Test basic addition
    result = add_numbers(2, 3)
    assert result == 5
    
    # Test with negative numbers
    result = add_numbers(-1, 1)
    assert result == 0
    
    # Test with decimals
    result = add_numbers(2.5, 1.5)
    assert result == 4.0


def test_calculate_average():
    """Test the calculate_average function"""
    # Test with normal numbers
    numbers = [1, 2, 3, 4, 5]
    result = calculate_average(numbers)
    assert result == 3.0
    
    # Test with empty list
    result = calculate_average([])
    assert result == 0
    
    # Test with single number
    result = calculate_average([10])
    assert result == 10


def test_process_numbers():
    """Test the process_numbers function"""
    # Test with simple numbers
    numbers = [1, 2, 3, 4, 5]
    result = process_numbers(numbers)
    
    # Check that we get the expected results
    assert result['total'] == 15
    assert result['average'] == 3.0
    assert result['max'] == 5
    assert result['min'] == 1
    assert result['count'] == 5


def test_process_numbers_single():
    """Test process_numbers with a single number"""
    numbers = [42]
    result = process_numbers(numbers)
    
    assert result['total'] == 42
    assert result['average'] == 42
    assert result['max'] == 42
    assert result['min'] == 42
    assert result['count'] == 1


def test_process_numbers_negative():
    """Test process_numbers with negative numbers"""
    numbers = [-1, -2, -3]
    result = process_numbers(numbers)
    
    assert result['total'] == -6
    assert result['average'] == -2.0
    assert result['max'] == -1
    assert result['min'] == -3
    assert result['count'] == 3