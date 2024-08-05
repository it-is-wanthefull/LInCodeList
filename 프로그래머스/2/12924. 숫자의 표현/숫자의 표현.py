def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        midd = n/i
        diff = i/2 - 0.5
        value = midd - diff
        if value < 1:
            break
        if value % 1 == 0:
            answer += 1
    
    return answer