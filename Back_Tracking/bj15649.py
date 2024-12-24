"""
백트래킹

- 숫자가 적을 때
- 재귀함수, 결과 코드 추가 필요
"""

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())

result = []
chk = [False] * (N+1)

def recur(num):
    if num == M:
        print(" ".join(map(str, result)))
        return
    
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            result.append(i)
            recur(num+1)
            chk[i] = False
            result.pop()

recur(0)