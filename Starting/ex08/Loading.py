def ft_tqdm(lst: range) -> None:
    """
    A custom implementation of a progress bar, similar to the tqdm module.

    Args:
        lst (range): A range or iterable

    Yields:
        item: Each item from the provided iterable.
    """
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        percentage = i * 100 // total
        bar_length = 200
        filled_length = int(bar_length * i // total)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)
        print(f"\r{percentage}%|{bar}| {i}/{total}", end='', flush=True)
        yield item

    print()


def main():
    """
    A test function to demonstrate the usage of ft_tqdm.
    """
    for _ in ft_tqdm(range(10)):
        pass


if __name__ == '__main__':
    main()
