import math

def root(n):
    return int(math.sqrt(n))

def is_square(n):
    return n == root(n)**2

def solution(left, right):
    answer = 0
    
    for n in range(left, right+1):
        if is_square(n):
            answer -= n
        else:
            answer += n
            
    return answer