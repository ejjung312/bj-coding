N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# C = [0] * (N+M)
C = []

i, j = 0, 0
while len(C) < (N+M):
    if i == N:
        C.append(B[j])
        j += 1
    elif j == M:
        C.append(A[i])
        i += 1
    else:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

print(" ".join(map(str, C)))