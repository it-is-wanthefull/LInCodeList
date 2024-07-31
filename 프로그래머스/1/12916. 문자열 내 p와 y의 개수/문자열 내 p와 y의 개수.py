# def solution(s):
#     return s.lower().count('p') == s.lower().count('y')

def solution(s):
    cnt = 0

    for c in s:
        if c == 'p' or c == 'P':
            cnt += 1
        if c == 'y' or c == 'Y':
            cnt -= 1

    return cnt==0