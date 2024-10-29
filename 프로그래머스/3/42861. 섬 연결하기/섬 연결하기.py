from collections import defaultdict

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    dic = defaultdict(set)
    min_total_cost = 0
    
    for v1, v2, c in costs:
        key1, key2 = -1, -1
        
        # 두 점이 각각 이미 본 적이 있는지 dic에서 검색
        for key in dic.keys():
            if v1 in dic[key]:
                key1 = key
            if v2 in dic[key]:
                key2 = key
            if key1!=-1 and key2!=-1: # 두 점 모두 찾은 경우 break로 시간단축
                break
                
        # 두 점 모두 처음인 경우 새로운 set 추가
        if key1==-1 and key2==-1:
            dic[v1].update([v1,v2])
            min_total_cost += c
        
        # v2만 처음인 경우 v1이 속한 set에 v2도 추가
        if key1!=-1 and key2==-1:
            dic[key1].add(v2)
            min_total_cost += c
        
        # v1만 처음인 경우 v2이 속한 set에 v1도 추가
        if key1==-1 and key2!=-1:
            dic[key2].add(v1)
            min_total_cost += c
            
        # 각 점이 다른 2개의 set에 있는 간선인 경우 두 set을 병합
        if key1!=-1 and key2!=-1 and key1!=key2:
            dic[key1].update(dic[key2])
            min_total_cost += c
            dic.pop(key2)
    
    return min_total_cost