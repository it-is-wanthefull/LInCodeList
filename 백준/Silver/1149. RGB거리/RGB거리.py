import sys

prev = current = [0, 0, 0]

for _ in range(int(sys.stdin.readline())):
    r, g, b = map(int, sys.stdin.readline().split())
    prev = current.copy()
    current[0] = min(prev[1], prev[2]) + r
    current[1] = min(prev[0], prev[2]) + g
    current[2] = min(prev[0], prev[1]) + b
    
print(min(current))