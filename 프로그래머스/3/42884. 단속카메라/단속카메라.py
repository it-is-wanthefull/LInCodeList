def solution(routes):
    routes.sort()
    cam, answer = -30001, 0
    
    for r in routes:
        if cam < r[0]: # 새구간시 추가설치
            cam = r[1]
            answer += 1
        elif r[1] < cam: # 앞구간이 너무길었다면 cam위치 재설정
            cam = r[1]
    
    return answer