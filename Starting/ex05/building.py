def analize_string(string: str) -> None:
    """
    Analyzes the given string and prints various statistics about its contents.

    The function calculates and displays the following counts
    for the input string:
        - Total number of characters
        - Number of uppercase letters
        - Number of lowercase letters
        - Number of punctuation marks
        - Number of spaces
        - Number of digits

    Args:
    - string (str): The string to be analyzed.

    Returns:
    - None: This function does not return any value.
            It prints the results to the console.
    """
    char_number = len(string)
    upper_characters_count = sum(1 for char in string if char.isupper())
    lower_characters_count = sum(1 for char in string if char.islower())
    punctuation_marks = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    punctuation_count = sum(1 for char in string if char in punctuation_marks)
    space_count = sum(1 for char in string if char.isspace())
    digit_count = sum(1 for char in string if char.isdigit())

    print(f"The text contains {char_number} characters:")
    print(f"{upper_characters_count} upper letters")
    print(f"{lower_characters_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main() -> int:
    """
    Main entry point of the program. Handles input from the user or
    command-line arguments and passes the string to the `analize_string`
    function for analysis.

    This function ensures that the user either provides the string
    via command-line argument (exactly one argument) or through standard input.
    If there is an incorrect number of arguments, the program exits with an
    error message. If no command-line argument is provided, it asks the user
    for input interactively.

    Returns:
    - int: Exits with a status code, typically 0 for successful execution
           or a non-zero code for errors.
    """
    import sys

    if len(sys.argv) > 2:
        sys.exit("AssertionError: more than one argument is provided")
    s: str = ''
    try:
        s = input("What is the text to count?\n") \
            if len(sys.argv) != 2 else sys.argv[1]
        if len(sys.argv) != 2:
            s += '\n'
    except EOFError:
        pass
    analize_string(s)


if __name__ == '__main__':
    main()
