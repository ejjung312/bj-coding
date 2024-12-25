# 바구니 N개. 바구니에 공 1개씩.
# M번 공을 바꿈
# 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환
N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for m in range(M):
    # i번 바구니와 j번 바구니에 들어있는 공을 교환
    i, j = map(int, input().split())

    temp = basket[j-1]
    basket[j-1] = basket[i-1]
    basket[i-1] = temp

print(" ".join(map(str, basket)))