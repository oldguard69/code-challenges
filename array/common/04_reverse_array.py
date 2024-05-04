import timeit


def reverse_array(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def reverse_array_2(arr):
    return arr[::-1]

print(reverse_array_2([1, 2, 3, 4, 5]))
print(reverse_array_2([1, 2, 3, 4, 5, 6]))


# Define the arrays to test
arr1 = list(range(1000))
arr2 = list(range(10000))

# Measure the execution time of reverse_array
time_reverse_array_1 = timeit.timeit(lambda: reverse_array(arr1), number=1000)
time_reverse_array_2 = timeit.timeit(lambda: reverse_array(arr2), number=1000)

# Measure the execution time of reverse_array_2
time_reverse_array_2_1 = timeit.timeit(lambda: reverse_array_2(arr1), number=1000)
time_reverse_array_2_2 = timeit.timeit(lambda: reverse_array_2(arr2), number=1000)

print("Time taken by reverse_array for arr1: ", time_reverse_array_1)
print("Time taken by reverse_array for arr2: ", time_reverse_array_2)
print("Time taken by reverse_array_2 for arr1: ", time_reverse_array_2_1)
print("Time taken by reverse_array_2 for arr2: ", time_reverse_array_2_2)