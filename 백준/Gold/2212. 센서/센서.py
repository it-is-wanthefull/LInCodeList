n = int(input())
k = int(input())
lst = list(map(int, input().split()))
lst.sort()
gap = []
for i in range(n-1):
    gap.append(lst[i+1] - lst[i])
gap.sort()
print(sum(gap[:n-k]))