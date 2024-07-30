import math

def solution(n):
    for x in range(int(math.sqrt(n))):
        if n % (x+1) == 1:
            return x+1
    return n-1