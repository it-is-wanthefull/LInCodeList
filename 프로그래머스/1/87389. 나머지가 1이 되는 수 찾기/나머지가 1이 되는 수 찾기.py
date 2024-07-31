import math

def solution(n):
    sqrt = int( math.sqrt(n) )
    
    for x in range(1, sqrt+1):
        if n % (x) == 1:
            return x
        
    return n-1