n = int(input())
k = int(input())

lst = sorted(list(map(int, input().split())))
gap = sorted([lst[i+1] - lst[i] for i in range(n-1)])

print(sum(gap[:n-k]))