# 내 풀이:#
import math
def solution(n, times):
    start, end = 0, math.ceil(n//len(times))*max(times) # 최대값으로 10억의제곱은 너무 크고
    
    while True:
        mid = (start + end) // 2
        cnt = sum(mid//t for t in times)
            
        if   cnt <  n: start = mid+1
        elif cnt >  n: end   = mid-1
        elif cnt == n: return mid - min(mid%t for t in times)
        
        if   start > end: return end+1





# # 베스트채택된 다른사람 풀이:
# def count(period, times):
#     cnt = 0
#     for time in times:
#         cnt += period // time
#     return cnt

# def solution(n, times):
#     digit = 50
#     t = 0
#     for i in range(digit, -1, -1):
#         temp  = t + 2**i
#         cnt = count(temp, times)
#         if cnt >= n:
#             if count(temp-1, times) < n:
#                 return temp
#         else:
#             t = temp