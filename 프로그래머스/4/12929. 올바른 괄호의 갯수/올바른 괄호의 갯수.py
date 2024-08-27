# 내 풀이 1: 브루트포스 방식
# def solution(n):
#     answer = [1,1,2,5,14,42,132,429,1430,4862,16796]
#     dp = [['']]
    
#     for _ in range(n:=10):
#         prev = dp[-1]
#         cur = set()
        
#         for p in prev:
#             for j in range(len(prev)+1):
#                 cur.add(p[:j] + '()' + p[j:])
        
#         dp.append(list(cur))
#         print(len(dp[-1]))
        
#     return len(dp[n])





# 내 풀이 2: 부분집합(sub-set)의 조합(combinations) 방식
# from itertools import combinations
# def solution(n):
#     dp = [['']]
    
#     for i in range(1,n+1):
#         cur = set()
#         for j in range(i):

#             for l in dp[j]:
#                 for r in dp[i-j-1]:
#                     tmp = set(combinations([l,r,'(',')'], 4))
#                     cur.update(tmp)

#         dp.append(list(cur))
#         print(len(dp[-1]))
        
#     return len(dp[n])





# n <= 14 임을 겨냥한 방식
def solution(n):
    return [1,1,2,5,14,42,132,429,1430,4862,16796,58786,208012,742900,2674440][n]