n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(sum(lst[i] * (n-i) for i in range(n)))