import sys

input = sys.stdin.readline

n = int(input())

s = 0
e = int(n ** (1/2))

while s <= e:
    mid = (s + e) // 2
    if mid ** 2 < n:
        s = mid + 1
    else:
        e = mid - 1

print(s)