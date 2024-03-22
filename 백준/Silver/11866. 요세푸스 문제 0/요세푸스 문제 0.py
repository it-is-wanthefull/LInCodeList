import sys

N, K = map(int, sys.stdin.readline().split())

check = [True] * N
finder = 0

print("<", end="")

for i in range(1, N + 1):
    count = 0
    while count < K:
        finder = (finder + 1) % N
        if check[finder]:
            count += 1
        if count == K:
            check[finder] = False
    
    if finder == 0:
        print(N, end="")
    else:
        print(finder, end="")

    if i != N:
        print(", ", end="")

print(">")
