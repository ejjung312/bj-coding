import sys

input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))

M = int(input())
target_list = list(map(int, input().split()))

card.sort()

def search(start, end, target):
    if start == end:
        if target == card[start]:
            print(1)
        else:
            print(0)
        return
    
    mid = (start+end) // 2
    if card[mid] < target:
        search(mid+1, end, target)
    else:
        search(start, mid, target)

for target in target_list:
    search(0, N-1, target)