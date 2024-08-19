# 1. 비교함수
def is_adjacent(str1, str2):
    diff_cnt = 0
    for a, b in zip(str1, str2):
        if a != b:
            diff_cnt += 1
        if diff_cnt >= 2:
            return False
    if diff_cnt == 1:
        return True

# 2. 인접행렬, Tree로는 앞글자 기준탐색일뿐 최단경로탐색엔 부적절
def make_adjacent_matrix(words, n):
    adj = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            adj[i][j] =  is_adjacent(words[i], words[j])
    return adj

# 3. ShortestPath: Dijkstra(특정점시작)이 Floyd(모든점시작고려)보다 적합, 근데 가중치가 전부 1일터라 결국 BFS내지DFS
def find_shortest_using_dfs(adj, n, target_idx):
    visited = [False] * n; visited[0] = True # 방문여부
    cost    = [99]    * n; cost[0]    = 0    # 변환비용
    stk     = [0]                            # DFS스택, 다음탐색할 adj인덱스를 저장
    while stk:
        i = stk.pop()
        for j in range(n):
            if adj[i][j] == True and visited[j] == False:
                stk.append(j)
                visited[j] = True
                cost[j] = min(cost[j], cost[i]+1)
    return cost[target_idx]
    
# 4. 메인코드
def solution(begin, target, words):
    words = [begin] + words
    n = len(words)
    
    if target not in words:
        return 0
    else:
        target_idx = words.index(target)
        adj = make_adjacent_matrix(words, n)
        return find_shortest_using_dfs(adj, n, target_idx)