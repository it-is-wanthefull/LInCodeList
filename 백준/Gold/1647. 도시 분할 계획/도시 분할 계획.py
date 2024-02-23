def kruskal(n, edges) -> int:
    def find(v, set):
        if set[v] != v:
            set[v] = find(set[v], set)
        return set[v]

    set = list(range(n + 1))
    sum_cost = 0
    used_edges = 0

    for v1, v2, c in edges:
        if used_edges == n-2:
            break
        set_v1 = find(v1, set)
        set_v2 = find(v2, set)
        if set_v1 != set_v2:
            set[set_v1] = set_v2
            sum_cost += c
            used_edges += 1

    return sum_cost

from sys import stdin
n, m = map(int, stdin.readline().split())
edges = []

for _ in range(m):
    v1, v2, c = map(int, stdin.readline().split())
    edges.append([v1, v2, c])
edges.sort(key=lambda x: x[2])

print(kruskal(n, edges))