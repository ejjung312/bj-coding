# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

def recur(num):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(num, N+1):
        if i not in result:
            result.append(i)
            recur(i+1)
            result.pop()
            
N, M = map(int, input().split())
result = []
recur(1)