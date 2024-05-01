"""
https://cses.fi/problemset/task/1068
"""
def custom_print(n):
    print(n, end=" ")
n = int(input())

custom_print(n)
while n != 1:
    if not n % 2:
        n /= 2
    else:
        n = n*3 + 1
    custom_print(int(n))