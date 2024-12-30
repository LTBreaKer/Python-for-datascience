import sys


def to_morse(string: str) -> None:
    """
    Takes a string containing only alphanumeric characters an prints it
    """
    NESTED_MORSE: dict = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
        'U': '..-',   'V': '...-', 'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    encoded_string: str = ''
    for char in string:
        try:
            encoded_string += f"{NESTED_MORSE[char.upper()]} "
        except KeyError as key_error:
            raise AssertionError('the arguments are bad') from key_error

    print(encoded_string[:-1])


def main():
    """
    Takes one command-line argument:\n
        1. A string contanig only alphanumeric characters
    calls to_morse() with the string as argument
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError('the arguments are bad')
        to_morse(sys.argv[1])
    except AssertionError as asser:
        sys.exit(f"{AssertionError.__name__}: {str(asser)}")


if __name__ == '__main__':
    main()
