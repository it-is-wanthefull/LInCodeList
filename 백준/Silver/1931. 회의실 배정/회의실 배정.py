meetings = [tuple(map(int, input().split())) for _ in range(int(input()))]
meetings.sort(key=lambda x: (x[1], x[0]))

now, ans = 0, 0
for start, end in meetings:
    if now <= start:
        now = end
        ans += 1
        
print(ans)