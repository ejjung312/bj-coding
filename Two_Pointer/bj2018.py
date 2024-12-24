N = int(input())

end = 0
total = 0
count = 0

for start in range(0, N):
    while total < N and end < N:
        total += end + 1
        end += 1
    if total == N:
        count += 1
    total -= start + 1

print(count)