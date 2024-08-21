def solution(n, s):
    d, r = s//n, s%n
    if d == 0: return [-1]
    else:      return [d]*(n-r) + [d+1]*r