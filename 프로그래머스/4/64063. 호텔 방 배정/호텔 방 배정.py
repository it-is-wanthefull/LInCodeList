def solution(k, room_number):
    answer = []
    dic = dict()
    
    for n in room_number:
        visited = [n] # 방문노트
        
        while n in dic:
            n = dic[n] # 방에 기록된 이정표만큼 건너뛰기형 탐색
            visited.append(n) # 방문할 방 저장
            
        for v in visited: # 방문한 방의 이정표 업데이트
            dic[v] = n + 1
            
        answer.append(n)
        
    return answer