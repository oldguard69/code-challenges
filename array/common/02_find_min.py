from typing import Sequence

def find_min(arr: Sequence):
    """
    Finds the minimum value in a sequence.

    Args:
        arr (Sequence): The input sequence.

    Returns:
        The minimum value found in the sequence.

    >>> find_min([1, 3, 5, 7, 9])
    1
    >>> find_min([-10, -5, 0, 5, 10])
    -10
    >>> find_min([])
    Traceback (most recent call last):
        ...
    ValueError: min() arg is an empty sequence
    """
    if not arr:
        raise ValueError("min() arg is an empty sequence")

    min_value = arr[0]  # Initialize min_value with the first element
    for v in arr:
        if v < min_value:
            min_value = v
    return min_value
