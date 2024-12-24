import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

def binary_search(start, end, target):
    if start == end:
        if A[start] == target:
            print(1)
        else:
            print(0)
        return

    mid = (start + end) // 2
    if A[mid] < target:
        binary_search(mid+1, end, target)
    else:
        binary_search(start, mid, target)
        

for target in B:
    binary_search(0, N-1, target)