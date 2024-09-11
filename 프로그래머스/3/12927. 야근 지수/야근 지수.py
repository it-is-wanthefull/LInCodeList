# 내 풀이 1
def solution(n, works):
    works.sort(reverse=True)
    
    while True:
        for i in range(len(works)):
            if works[i] >= works[0] >= 0:
                works[i] -= 1
                n -= 1
            if n == 0 or works[-1] == 0:
                return sum(e*e for e in works)

            
            
            
            
# 내 풀이 2 (특수케이스 최적화)
# def solution(n, works):
#     if sum(works) <= n:
#         return 0
    
#     works.sort(reverse=True)
    
#     while True:
#         for i in range(len(works)):
#             if works[i] >= works[0]:
#                 works[i] -= 1
#                 n -= 1
#             if n == 0:
#                 return sum(e*e for e in works)
            
            
            
            

# 내 풀이 3
# from collections import Counter

# def solution(n, works):
#     if sum(works) <= n:
#         return 0
    
#     labors = sorted(Counter(works).items(), reverse=True)
    
#     while True:
#         hour, count = labors[0]
#         if n > count:
#             n -= count
#             if len(labors)>1 and hour-1 == labors[1][0]:
#                 labors[1] = (labors[1][0], labors[1][1]+count)
#                 labors.pop(0)
#             else:
#                 labors[0] = (hour-1, count)
#         else:
#             return sum(h*h*c for h,c in labors) + n*(1-2*hour)
#             # -hour**2*n +(hour-1)**2*n
#             # == -nx^2 + n(x-1)^2
#             # == n(x-1)^2 - nx^2
#             # == n * ((x-1)^2-x^2)
#             # == n * (1-2x)
#             # == n * (1-2*hour)





# 베스트채택된 다른사람 풀이 (구버전)
# def solution(n, works):
#     if n>=sum(works):
#         return 0;
#     while n > 0:
#         works[works.index(max(works))] -= 1
#         n -= 1
#     return sum([w ** 2 for w in works])





# 베스트채택된 다른사람 풀이 (신버전)
# from heapq import heapify, heappush, heappop
# def solution(n, works):
#     heapify(works := [-i for i in works])
#     for i in range(min(n, abs(sum(works)))):
#         heappush(works, heappop(works)+1)
#     return sum([i*i for i in works])





# 많이 엉망인 다른사람 풀이
# def solution(n, works):
#     while n>=1:
#         works.sort()
#         works[-1]-=1
#         n-=1
#     return sum(x**2 for x in works)