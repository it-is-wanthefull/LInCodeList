from collections import defaultdict

def solution(n, edge): # BFS와 set 활용
    START_VERTEX = 1
    dic          = defaultdict(list)
    visited      = set({START_VERTEX})
    stack        = list([START_VERTEX])
    next_stack   = list()
    
    # 딕셔너리로 그래프 분석/분류
    for v1, v2 in edge:
        dic[v1].append(v2)
        dic[v2].append(v1)
        
    while len(visited) != n:
        while stack:
            v = stack.pop()
            for dv in dic[v]:
                if dv not in visited:
                    visited.add(dv)
                    next_stack.append(dv)
                
        stack = next_stack
        next_stack = []
    
    return len(stack)