import collections

def dfs(key, visited, dict):
    for value in dict[key]:
        if value not in visited:
            visited.append(value)
            print(" " + str(value), end="")
            dfs(value, visited, dict) #Queue를 구현하는 BFS와 달리 DFS는 재귀자체가 Stack이라 Stack구현필요없다

def bfs(key, visited, dict, q):
    while q:
        key = q.popleft()

        for value in dict[key]:
            if value not in visited:
                visited.append(value)
                print(" " + str(value), end="")
                q.append(value)

dict = collections.defaultdict(list)
q = collections.deque()

N, M, V = map(int, input().split()) #N=점갯수, M=간선수, V=시작점

for _ in range(M):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

for key in dict.keys():
    dict[key] = sorted(dict[key])

visited = [V]
print(V, end="") #end="" 개행없이출력
dfs(V, visited, dict)
print() #개행만출력

visited = [V]
q.append(V)
print(V, end="")
bfs(V, visited, dict, q)