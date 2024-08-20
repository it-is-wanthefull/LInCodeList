from collections import deque 

def solution(m, n, puddles):
    arr = [[0]*(m+1) for _ in range(n+1)] # arr[n+1][m+1] = dp값
    arr[1][1] = 1
    q = deque([[1,1]])
    
    while q:
        r, c = q.popleft()
        if r < n and [c, r+1] not in puddles: # 문제조건에 좌향상향 특수케이스는 제거됨, puddles값이 비일반적이게도 [c,r]꼴로 되어있음
            arr[r+1][c] += arr[r][c]
            if [r+1,c] not in q: # 중복append 방지
                q.append([r+1,c])
        if c < m and [c+1, r] not in puddles:
            arr[r][c+1] += arr[r][c]
            if [r,c+1] not in q:
                q.append([r,c+1])
        
    return arr[n][m] % 1000000007 # 문제에 숨겨진 비일반적인 조건





# from collections import deque 

# def solution(m, n, puddles):
#     dic = {(r,c): 0 for c in range(m+1) for r in range(n+1)} # dic[(r,c)] = dp값(기본값0)
#     dic[(1,1)] = 1
#     q = deque([(1,1)])
    
#     while q:
#         r, c = q.popleft()
#         curr, down, right = (r,c), (r+1,c), (r,c+1)
#         if r < n and list(down) not in puddles: # 문제조건에 좌향상향 특수케이스는 제거됨
#             dic[down] += dic[curr]
#             if down not in q: # 중복append 방지
#                 q.append(down)
#         if c < m and list(right) not in puddles:
#             dic[right] += dic[curr]
#             if right not in q:
#                 q.append(right)
                
#     return dic[(n,m)] % 1000000007 # 문제에 숨겨진 비일반적인 조건