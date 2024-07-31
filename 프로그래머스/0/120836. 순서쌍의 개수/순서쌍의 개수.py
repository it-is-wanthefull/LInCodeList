import math

def root(n):
    return int(math.sqrt(n))

def solution(n):
    answer = 1
    
    for i in range(2, root(n)+1):
        cnt = 1
        while n % i == 0:
            cnt += 1
            n = n/i
        if cnt != 1:
            answer *= cnt
    
    if n != 1:
        answer *= 2
    
    return answer