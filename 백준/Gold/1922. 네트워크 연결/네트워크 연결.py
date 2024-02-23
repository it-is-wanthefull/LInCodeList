def prim(n, edges): #Prim알고리즘
    import heapq

    graph = [[] for _ in range(n + 1)]
    for idx, adj, cost in edges:
        graph[idx].append((cost, adj)) #양방향
        graph[adj].append((cost, idx))

    visited = [False] * (n + 1)
    visited[1] = True #1번점을 시작점으로 선택
    heap = []
    for cost, adj in graph[1]:
        heapq.heappush(heap, (cost, adj)) #앞값인 cost기준 오름차순정렬

    result = 0
    used_edges = 0
    while used_edges < n - 1:
        cost, idx = heapq.heappop(heap)
        if visited[idx]: #사이클 방지
            continue
        visited[idx] = True
        result += cost #비용 추가
        used_edges += 1 #N-1에서 멈출예정
        for adj_cost, adj in graph[idx]: #확장된 집합에서 간선 업데이트
            if not visited[adj]:
                heapq.heappush(heap, (adj_cost, adj))

    return result

#----- ----- ----- ----- ----- ----- ----- ----- ----- -----

if __name__ == '__main__': #배운것1: 메인지정
    from sys import stdin  #배운것2: 라이브러리/모듈을 중간에도 가능

    input = stdin.readline #배운것3: 함수이름변경, 단 함수형프로그래밍x
    n = int(input())
    m = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(prim(n, edges))