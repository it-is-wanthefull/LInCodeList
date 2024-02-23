import collections, sys
dict_graph = collections.defaultdict(list)
dict_parent = collections.defaultdict(list, {1: 1}) #1을 루트노드의미로 미리 넣음
q = collections.deque([1])

N = int(input())
for i in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().split())
    dict_graph[v1].append(v2)
    dict_graph[v2].append(v1)

while q:
    node = q.popleft()
    for neighbor in dict_graph[node]:
        if neighbor not in dict_parent:  #이미 부모가 설정된 노드는 스킵
            dict_parent[neighbor] = node  #현재 노드를 이웃 노드의 부모로 설정
            q.append(neighbor)

for j in range(2, N+1):
    sys.stdout.write(str(dict_parent[j]) + "\n")