# # 내 풀이 1: 브루트포스 방식
# def solution(n):
#     dp = [['']]
    
#     for _ in range(n):
#         cur = set()
        
#         for d in dp[-1]:
#             for j in range(len(d)+1):
#                 cur.add(d[:j] + '()' + d[j:])
        
#         dp.append(list(cur))
        
#     return len(dp[n])





# # 내 풀이 2: 부분집합(sub-set)의 조합(combinations) 직접 방식
# from itertools import combinations
# def solution(n):
#     dp = [['']]
    
#     for i in range(1, n+1):
#         cur = set()

#         for j in range(i):
#             for l in dp[j]:
#                 for r in dp[i-j-1]:
#                     cur.update(combinations([l,r,'(',')'], 4))

#         dp.append(list(cur))
        
#     return len(dp[n])





# 내 풀이 3: 부분집합(sub-set)의 조합(combinations) 수치계산 방식
from itertools import combinations
def solution(n):
    dp = [1,1,2,5]
    
    for i in range(len(dp), n+1):
        dp.append(0)
        for j in range(i):
            dp[-1] += dp[j] * dp[i-j-1]
            
    return dp[n]





# # 내 풀이 4: n <= 14 임을 겨냥한 방식
# def solution(n):
#     return [1,1,2,5,14,42,132,429,1430,4862,16796,58786,208012,742900,2674440][n]





# # 베스트채택된 다른사람 풀이 1: 카탈란 수
# from math import factorial as f
# def solution(n):
#     return f(2*n)//(f(n)**2*(n+1))