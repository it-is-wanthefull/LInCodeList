# 출발지가 여러군데이지만 Floyd로 하면 10만의3승이나 걸린다, 단순히 인접행렬 생성에도 10만의2승(100억) 즉 1만초나 걸린다.
# 잘 역발상해보면 도착지가 1군데뿐이므로, 도착지에서 출발지로 역행하는 Dijkstra를 짜보면 된다. 10log10=170만

from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    road_dic = defaultdict(list)
    cost_dic = defaultdict(lambda: defaultdict(int))
    
    for v1, v2 in roads:
        road_dic[v1].append(v2)
        road_dic[v2].append(v1)
    
    visited = set([destination])
    q = deque([destination])
    cost_dic[destination][destination] = 0
    while q:
        cur = q.popleft()
        for v in road_dic[cur]:
            if v not in visited:
                visited.add(v)
                q.append(v)
                cost_dic[destination][v] = cost_dic[destination][cur] + 1
    
    result = []
    for s in sources:
        result.append(cost_dic[destination].get(s, -1)) # cost_dic[destination][s]가 존재하지 않는 경우 -1 반환
    
    return result