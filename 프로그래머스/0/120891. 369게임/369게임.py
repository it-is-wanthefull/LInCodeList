def solution(order):
    answer = 0
    for e in str(order):
        if e in {'3', '6', '9'}:
            answer += 1
    return answer