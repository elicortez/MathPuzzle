import re
from itertools import permutations


"""
Math Puzzle

An eight-digit number contains two 1's, two 2's, two 3's, and two 4's. 
The 1's are separated by one digit, the 2's by two digits, the 3's by three digits, 
and the 4's by four digits.

What's the number?
"""


def generate_valid_combinations():
    # Create all permutations of the digits 1, 2, 3, and 4
    all_permutations = set(permutations("11223344", 8))

    valid_combinations = []

    for permutation in all_permutations:
        combination = ''.join(permutation)

        # Check if the combination has 2 instances of each digit
        if (
            combination.count('1') == 2 and
            combination.count('2') == 2 and
            combination.count('3') == 2 and
            combination.count('4') == 2
        ):
            valid_combinations.append(combination)

    return valid_combinations


def verify_input_string(input_str):
    # Check if the input string contains exactly 8 digits
    if not re.match(r'^\d{8}$', input_str):
        return False

    # Check if the input string contains 2 instances of each of the digits 1, 2, 3, and 4
    if (
        input_str.count('1') != 2 or
        input_str.count('2') != 2 or
        input_str.count('3') != 2 or
        input_str.count('4') != 2
    ):
        return False

    # Check if there is a single digit between the 1s
    if not re.search(r'1\d1', input_str):
        return False

    # Check if there are two digits between the 2s
    if not re.search(r'2\d{2}2', input_str):
        return False

    # Check if there are three digits between the 3s
    if not re.search(r'3\d{3}3', input_str):
        return False

    # Check if there are four digits between the 4s
    if not re.search(r'4\d{4}4', input_str):
        return False

    return True


combinations = generate_valid_combinations()
print("Valid Combinations:")
for combination in combinations:
    if verify_input_string(combination):
        print(combination)
