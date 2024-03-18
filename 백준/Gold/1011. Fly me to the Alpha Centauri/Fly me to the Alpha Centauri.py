import math

for _ in range(int(input())):
    x, y = map(int, input().split())
    k = int(math.sqrt(y - x))
    print(2*k + (y-x > k**2+k) if (y-x) != k**2 else 2*k -1)
