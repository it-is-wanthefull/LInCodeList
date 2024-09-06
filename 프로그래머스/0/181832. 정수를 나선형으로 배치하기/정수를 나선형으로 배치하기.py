def solution(n):
    answer = [[0] * n for _ in range(n)]    # answer = [[]] 은 틀린 2차원배열 선언
    r, c, cnt, sign = 0, -1, 0, 1           # sign 은 부호를 뜻함
    
    while n > 0:
        for _ in range(n):
            r, c, cnt = r, c+sign, cnt+1
            answer[r][c] = cnt
        
        for _ in range(n-1):
            r, c, cnt = r+sign, c, cnt+1
            answer[r][c] = cnt
        
        sign *= -1
        n -= 1
            
    return answer