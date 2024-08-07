def solution(n, works):
    works.sort(reverse=True)
    
    while True:
        for i in range(len(works)):
            if works[i] >= works[0] >= 0:
                works[i] -= 1
                n -= 1
            if n == 0 or works[-1] == 0:
                return sum(e**2 for e in works)

            
            
            
            
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
#                 return sum(e**2 for e in works)
            
            
            
            
            
# from collections import Counter

# def solution(n, works):
#     if sum(works) <= n:
#         return 0
    
#     times = sorted(Counter(works).items(), reverse=True)
    
#     while True:
#         hour, count = times[0]
#         if n > count:
#             n -= count
#             if len(times)>1 and hour-1 == times[1][0]:
#                 times[1] = (times[1][0], times[1][1]+count)
#                 times.pop(0)
#             else:
#                 times[0] = (hour-1, count)
#         else:
#             return sum(k**2*v for k, v in times) + n*(1-2*hour)
#             # -hour**2*n +(hour-1)**2*n
#             # == -nx^2 + n(x-1)^2
#             # == n(x-1)^2 - nx^2
#             # == n * ((x-1)^2-x^2)
#             # == n * (1-2x)
#             # == n * (1-2*hour)