from collections.abc import Sequence 

def find_max(arr: Sequence):
    """
    Finds the maximum value in a sequence.

    Args:
        arr (Sequence): The input sequence.

    Returns:
        The maximum value found in the sequence.

    >>> find_max([1, 3, 5, 7, 9])
    9
    >>> find_max([-10, -5, 0, 5, 10])
    10
    >>> find_max([])
    Traceback (most recent call last):
        ...
    ValueError: max() arg is an empty sequence
    """
    if not arr:
        raise ValueError("max() arg is an empty sequence")

    max_value = arr[0]  # Initialize max_value with the first element
    for v in arr:
        if v > max_value:
            max_value = v
    return max_value

if __name__ == "__main__":
    import doctest
    doctest.testmod()