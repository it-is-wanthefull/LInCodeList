# 다른문제에서 썼던 DP코드
# def solution(money):
#     n = len(money)

#     if n == 1: return money[0]
#     prev, curr = money[0], max(money[0], money[1])

#     for i in range(2, n):
#         prev, curr = curr, max(prev + money[i], curr)

#     return curr





# 해당문제에 맞게 최적화
# def solution(m):
#     a = b = 0

#     for i in m:
#         a, b = b, max(a+i,b)

#     return b





# 속도상 max를 쓰기보다 직접비교
# def solution(m):
#     a = b = 0

#     for i in m:
#         a, b = b, (a+i if a+i>b else b)

#     return b





# 첫째집과 마지막집이 원형으로 인접해있는 문제상황 반영
def solution(m):
    a = b = c = d = 0

    for i in m[1:]:
        a, b = b, (a+i if a+i>b else b)
    for i in m[:-1]:
        c, d = d, (c+i if c+i>d else d)

    return b if b>d else d





# # 중복코드 함수화
# def solution(m):
#     def part(p):
#         a = b = 0
#         for i in p:
#             a, b = b, (a+i if a+i>b else b)
#         return b

#     return max( part(m[1:]), part(m[:-1]) )