# N개의 바구니, M개의 공
N, M = map(int, input().split())

basket = [0] * N

for m in range(1, M+1):
    # i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다
    i, j, k = map(int, input().split())

    # 2 5 6: 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻
    # 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다
    for num in range(i, j+1):
        basket[num-1] = k

print(" ".join(map(str, basket)))