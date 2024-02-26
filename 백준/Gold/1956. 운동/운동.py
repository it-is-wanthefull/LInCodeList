def floyd(graph, N):
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    for start, adjs in graph.items():
        for adj, d in adjs:
            dist[start][adj] = d

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    return dist

#----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

if __name__ == '__main__':
    import sys
    from collections import defaultdict
    INF = int(1e9)
    input = sys.stdin.readline
    dict = defaultdict(list)

    num_v, num_e = map(int, input().split())
    for _ in range(num_e):
        a, b, c = map(int, input().split())
        dict[a].append([b, c])

    dist = floyd(dict, num_v)
    min = INF
    for i in range(1, num_v + 1):
        if dist[i][i] < min:
            min = dist[i][i]

    print(-1 if min==INF else min)