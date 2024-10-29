from collections import defaultdict, deque

def solution(gems):
    dic = defaultdict(deque)
    for i in range(len(gems)):
        dic[gems[i]].append(i)
    
    start, end = 999999, -1
    for key in dic.keys():
        if start  > dic[key][0]:
            start = dic[key][0] # start = min(start, dic[key][0])
        if end    < dic[key][0]:
            end   = dic[key][0] # end   = max(end,   dic[key][0])
    min_area = [start+1, end+1]
    
    for gem in gems:
        dic[gem].popleft()
        
        # start 갱신 로직: start 동류보석이 더이상없는경우 고정, 그외엔 1씩증가
        if dic[gems[start]]:
            start += 1
        
        # end 갱신 로직: pop보석의 next동류보석이 start~end밖인 경우 end 갱신
        if dic[gem]:
            if end < (nxt:=dic[gem][0]):
                end = nxt
        
        # min 갱신 로직: 기록된 min_area값과 비교, 갱신시 +1의 이유는 배열은 0부터 시작하나 진열대는 1부터 시작하는 오차 고려
        if end-start < min_area[1]-min_area[0]:
            min_area = [start+1, end+1]
        
        # return 로직: start/end가 둘다 고정이 되버린 경우 return
        if not dic[gems[start]]:
            if not dic[gems[end]]:
                return min_area