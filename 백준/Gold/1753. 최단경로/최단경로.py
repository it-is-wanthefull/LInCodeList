import heapq
def dij_q(graph, start, N): #N 추가
    dist = [INF] * (N+1) #N->N+1 수정

    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        acc, cur = heapq.heappop(q)

        if dist[cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

def dij(graph, start, N): #N 추가
    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N+1): #N->N+1 수정
            if dist[i] < min_value and not visited[i]:
                min_value = dist[i]
                idx = i
        return idx

    visited = [False] * (N+1) #N->N+1 수정
    dist    = [INF]   * (N+1) #N->N+1 수정

    visited[start] = True
    dist[start]    = 0
    for adj, d in graph[start]:
        dist[adj] = d

    for _ in range(N - 1):
        cur = get_smallest_node()
        visited[cur] = True
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost

    return dist

#----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

import sys
from collections import defaultdict
INF = int(1e9)
input = sys.stdin.readline
dict = defaultdict(list)

num_v, num_e = map(int, input().split())
start = int(input())
for _ in range(num_e):
    u, v, w = map(int, input().split())
    dict[u].append([v, w])

dist = dij_q(dict, start, num_v)
for i in range(1, num_v+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])