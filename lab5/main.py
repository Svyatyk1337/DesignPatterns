# Tasks using lambda expressions and functional programming features in Python

# 1. Filter odd numbers from a list of integers using lambda expression
def filter_odd_numbers(numbers):
    """Filter odd numbers from a list."""
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(f"Input: {numbers}")
    print(f"Odd numbers: {odd_numbers}")
    return odd_numbers

# 2. Find average of a list of real numbers using lambda expression
def find_average(numbers):
    """Find the average value of a list."""
    if not numbers:
        return 0
    average = sum(numbers) / len(numbers)
    print(f"Input: {numbers}")
    print(f"Average value: {average}")
    return average

# 3. Sort a list of strings alphabetically using lambda expression
def sort_strings_alphabetically(strings):
    """Sort strings in alphabetical order."""
    sorted_strings = sorted(strings, key=lambda s: s.lower())
    print(f"Input: {strings}")
    print(f"Sorted strings: {sorted_strings}")
    return sorted_strings

# 4. Calculate the sum of all even numbers using lambda expression
def sum_even_numbers(numbers):
    """Sum of all even numbers."""
    even_sum = sum(filter(lambda x: x % 2 == 0, numbers))
    print(f"Input: {numbers}")
    print(f"Sum of even numbers: {even_sum}")
    return even_sum

# 5. Calculate factorial of a given number using lambda expression
def calculate_factorial(n):
    """Calculate factorial of a number."""
    from functools import reduce
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = reduce(lambda x, y: x * y, range(1, n + 1))
        print(f"Factorial of {n}: {factorial}")
        return factorial

# 6. Calculate product and sum of all elements in a list of integers using lambda expression
def calculate_product_and_sum(numbers):
    """Calculate product and sum of all numbers in a list."""
    from functools import reduce
    if not numbers:
        return (0, 0)
    
    product = reduce(lambda x, y: x * y, numbers)
    total_sum = sum(numbers)
    
    print(f"Input: {numbers}")
    print(f"Product of all numbers: {product}")
    print(f"Sum of all numbers: {total_sum}")
    
    return (product, total_sum)

# 7. Calculate square of each number in a list of integers using lambda expression
def calculate_squares(numbers):
    """Calculate square of each number in a list."""
    squares = list(map(lambda x: x ** 2, numbers))
    
    print(f"Input: {numbers}")
    print(f"Squares: {squares}")
    
    return squares

# 8. Sort strings based on their length in ascending order using lambda expression
def sort_strings_by_length(strings):
    """Sort strings based on their length."""
    sorted_strings = sorted(strings, key=lambda s: len(s))
    
    print(f"Input: {strings}")
    print(f"Strings sorted by length: {sorted_strings}")
    
    return sorted_strings

# 9. Count number of words in a sentence (words separated by spaces) using lambda expression
def count_words(sentence):
    """Count number of words in a sentence."""
    if not sentence:
        return 0
    
    # Split by spaces and filter out empty strings
    words = list(filter(lambda x: x != '', sentence.split(' ')))
    word_count = len(words)
    
    print(f"Input: '{sentence}'")
    print(f"Word count: {word_count}")
    
    return word_count

# 10. Find first non-empty string in a list of strings using lambda expression
def find_first_nonempty_string(strings):
    """Find first non-empty string in a list."""
    non_empty = next(filter(lambda s: s.strip() != '', strings), None)
    
    print(f"Input: {strings}")
    print(f"First non-empty string: {non_empty}")
    
    return non_empty

# 11. Check if all strings in a list start with a capital letter using lambda expression
def check_capital_letter_start(strings):
    """Check if all strings start with a capital letter."""
    all_capitalized = all(map(lambda s: s and s[0].isupper(), strings))
    
    print(f"Input: {strings}")
    print(f"All strings start with capital letter: {all_capitalized}")
    
    return all_capitalized

# 12. Find second largest number in a list of integers using lambda expression
def find_second_largest(numbers):
    """Find second largest number in a list."""
    if len(numbers) < 2:
        return None
    
    # Sort in descending order and take the second element
    sorted_nums = sorted(numbers, reverse=True)
    second_largest = sorted_nums[1]
    
    print(f"Input: {numbers}")
    print(f"Second largest number: {second_largest}")
    
    return second_largest

# 13. Find largest even number in a list of integers using lambda expression
def find_largest_even(numbers):
    """Find largest even number in a list."""
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    
    if not even_numbers:
        print(f"Input: {numbers}")
        print("No even numbers in the list")
        return None
    
    largest_even = max(even_numbers)
    
    print(f"Input: {numbers}")
    print(f"Largest even number: {largest_even}")
    
    return largest_even

# Main execution with example data
if __name__ == "__main__":
    print("\n1. Filter odd numbers:")
    filter_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    print("\n2. Find average:")
    find_average([1.5, 2.5, 3.5, 4.5, 5.5])
    
    print("\n3. Sort strings alphabetically:")
    sort_strings_alphabetically(["Banana", "apple", "Cherry", "date", "Elderberry"])
    
    print("\n4. Sum of even numbers:")
    sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    print("\n5. Calculate factorial:")
    calculate_factorial(5)
    
    print("\n6. Product and sum of numbers:")
    calculate_product_and_sum([1, 2, 3, 4, 5])
    
    print("\n7. Calculate squares:")
    calculate_squares([1, 2, 3, 4, 5])
    
    print("\n8. Sort strings by length:")
    sort_strings_by_length(["apple", "banana", "pear", "strawberry", "fig"])
    
    print("\n9. Count words in sentence:")
    count_words("This is a sample sentence with seven words")
    
    print("\n10. Find first non-empty string:")
    find_first_nonempty_string(["", "  ", "Hello", "World"])
    
    print("\n11. Check if all strings start with capital letter:")
    check_capital_letter_start(["Hello", "World", "Python", "Lambda"])
    
    print("\n12. Find second largest number:")
    find_second_largest([5, 10, 3, 8, 15, 7])
    
    print("\n13. Find largest even number:")
    find_largest_even([5, 10, 3, 8, 15, 7, 12])