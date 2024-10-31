from collections import defaultdict
import copy

# 서브함수: 재귀로 티켓사용/여행
def recursive_trip(dic, log, n_ticket):
    if len(log) == n_ticket + 1: # ticket을 모두사용시 재귀종료
        return log

    recent = log[-1]
    for i in range(len(dic[recent])):
        copy_dic = copy.deepcopy(dic) # 'dic.copy()'로는 얕은복사만 됨
        copy_log = log.copy()
        next_ = copy_dic[recent].pop(i)
        copy_log.append(next_)
        
        result = recursive_trip(copy_dic, copy_log, n_ticket)
        if result != "Not All Ticket":
            return result

    return "Not All Ticket"

# 메인함수
# 문제요점: node가 아닌 edge를 모두방문해야함, 추가조건으로 최소비용/거리가 아닌 알파벳순
def solution(tickets):
    dic = defaultdict(list)
    log = list(["ICN"])
    n_ticket = len(tickets)
    
    for t1, t2 in tickets:
        dic[t1].append(t2) # 단방향 그래프
    
    for key in dic.keys(): # 알파벳순 정렬
        dic[key].sort()
    
    return recursive_trip(dic, log, n_ticket)