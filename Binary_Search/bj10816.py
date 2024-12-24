import sys

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

hash = {}
for num in a:
    hash[num] = hash.setdefault(num, 0) + 1

for num in b:
    print(hash.setdefault(num, 0), end = ' ')