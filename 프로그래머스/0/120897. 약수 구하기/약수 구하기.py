import math

def root(n):
    return int(math.sqrt(n))

def solution(n):
    answer = []
    
    for i in range(1, root(n)+1):
        if n % i == 0:
            answer.append(i)
            answer.append(n/i)
            
    if n == root(n)**2: # n이 제곱수인경우의 중복append 예외처리
        answer.pop()
    
    return sorted(answer)