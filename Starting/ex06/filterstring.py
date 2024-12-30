from ft_filter import ft_filter


def main():
    """
    Expects exactly two command-line arguments:\n
        1. A string `s` containing words to be filtered.
        2. An integer `n` that specifies the length threshold.
    \n
    Prints the words with length greater than `n` as a list
    """
    import sys

    try:
        if len(sys.argv) != 3:
            raise AssertionError('the arguments are bad')
        s: str = sys.argv[1]

        try:
            n = int(sys.argv[2])
        except ValueError as exc:
            raise AssertionError('the arguments are bad') from exc

        result = ft_filter(lambda string: len(string) > n, s.split())
        print(list(result))

    except AssertionError as asser:
        print(f"{AssertionError.__name__}: {str(asser)}")


if __name__ == '__main__':
    main()
