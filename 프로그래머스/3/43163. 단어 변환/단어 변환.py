def solution(begin, target, words):
    def is_adjacent(str1, str2):
        diff_cnt = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff_cnt += 1
            if diff_cnt >= 2:
                return False
        if diff_cnt == 1:
            return True
    
    def make_adjacent_matrix(words, adj, n):
        for i in range(n):
            for j in range(n):
                adj[i][j] =  is_adjacent(words[i], words[j])
    
    def find_shortest_using_bfs(target_idx, adj, n):
        visited = [False] * n; visited[0] = True # 방문여부
        cost    = [0]     * n                    # 변환비용
        stk     = [0]                            # BFS스택, 다음탐색할 adj인덱스를 저장
        while stk:
            i = stk.pop()
            for j in range(n):
                if adj[i][j] == True and visited[j] == False:
                    stk.append(j)
                    visited[j] = True
                    cost[j] = cost[i] + 1
        return cost[target_idx]
    
    words = [begin] + words
    n = len(words)
    adj = [[False]*n for _ in range(n)] # 인접행렬
    
    if target not in words:
        return 0
    else:
        target_idx = words.index(target)
        make_adjacent_matrix(words, adj, n)
        return find_shortest_using_bfs(target_idx, adj, n)
    

# 1. 비교함수
# 2. 인접행렬, Tree로는 앞글자 기준일뿐
# 3. ShortestPath: Dijkstra(특정점시작)이 Floyd(모든점시작고려)보다 적합, 근데 가중치가 전부 1일터라 결국 BFS내지DFS
# 최대 wwl=50*50*10=2.5만=0.025s=25ms
# Dijkstra: 특정점에서의 특정점으로의 최소비용 탐색, 모든인접노드 갱신하고 다음선택노드는 시작점으로부터 최저비용 점 (FIFO아님 heapq에 가까움 so heapq를 쓰면 O(n^2)에서 O(nlogn)으로 줄어듬), MST와 차이점은 N개 점의 연결의 최소비용을 구하는게 아니라 특정점에서 특정점으로의 탐색의 최소비용을 찾는 것