# 바구니 N개. 왼쪽->오른쪽 순
# M번 바구니의 순서를 역순으로 만듬
N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for m in range(M):
    i, j = map(int, input().split())

    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

print(" ".join(map(str, basket)))
