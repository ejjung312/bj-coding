n = int(input())
k = int(input())
card = [int(input()) for _ in range(n)]

# n개 중 k개를 뽑아서 나열 가능한 수. 중복 불가

total = []
result = []
chk = [False] * n

def recur(num):
    if num == k:
        s = "".join(map(str, result))
        if s not in total:
            total.append(s)
        return
    
    for i in range(0, n):
        if chk[i] == False:
            chk[i] = True
            result.append(card[i])
            recur(num+1)
            result.pop()
            chk[i] = False

recur(0)
print(len(total))