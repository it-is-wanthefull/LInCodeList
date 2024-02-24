n = int(input())
lst = sorted(list(map(int, input().split())))
print(sum(lst[i] * (n-i) for i in range(n)))