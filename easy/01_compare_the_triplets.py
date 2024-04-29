# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    result = [0, 0]
    for alice, bob in zip(a, b):
        if alice > bob:
            result[0] += 1
        elif bob > alice:
            result[1] += 1
    return result

a = [1, 2, 3]
b = [3, 2, 1]
print(compareTriplets(a, b))