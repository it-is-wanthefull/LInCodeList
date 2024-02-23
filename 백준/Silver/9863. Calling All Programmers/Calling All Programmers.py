from collections import deque

a, b, c = map(int, input().split())
while a!=0 and b!=0 and c!=0:
    q = deque(range(1,a+1))

    picked = -1
    for _ in range(c):
        for _ in range(b):
            picked = q.popleft()
            q.append(picked)
        picked = q.pop()

    print(picked)
    a, b, c = map(int, input().split())