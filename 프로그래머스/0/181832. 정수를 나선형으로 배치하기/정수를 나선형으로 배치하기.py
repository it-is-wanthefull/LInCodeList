def solution(n):
    answer = [[0] * n for _ in range(n)]  #answer = [[]] 은 틀린 2차원배열 선언
    r, c, cnt = 0, 0-1, 1-1
    
    for j0 in range(n):
            r, c, cnt = r, c+1, cnt+1
            answer[r][c] = cnt
    
    n -= 1
    
    while(1):
        if n == 0:
            break;
        
        for j1 in range(n):
            r, c, cnt = r+1, c, cnt+1
            answer[r][c] = cnt
        for j2 in range(n):
            r, c, cnt = r, c-1, cnt+1
            answer[r][c] = cnt
        
        n -= 1
        
        if n == 0:
            break;
        
        for j3 in range(n):
            r, c, cnt = r-1, c, cnt+1
            answer[r][c] = cnt
        for j4 in range(n):
            r, c, cnt = r, c+1, cnt+1
            answer[r][c] = cnt
        
        n -= 1
        
    return answer