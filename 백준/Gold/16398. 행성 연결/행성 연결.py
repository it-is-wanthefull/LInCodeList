def kruskal(n, edges) -> int: #Kruskal 알고리즘
    def find(v, set): #부모 찾기
        if set[v] != v:
            set[v] = find(set[v], set)
        return set[v]

    set = list(range(n + 1))
    sum_cost = 0
    used_edges = 0

    for v1, v2, c in edges:
        if used_edges == n-1: #n개의 점점에 대하여 n-1개 간선만 연결하면 됨
            break
        set_v1 = find(v1, set)
        set_v2 = find(v2, set)
        if set_v1 != set_v2: #선택한 두점이 부모가 같지않다면, 즉 사이클이 안된다면
            set[set_v1] = set_v2 #union(그룹결합)이 재사용되지 않고 1줄로 줄여져 굳이함수화하지않음
            sum_cost += c
            used_edges += 1

    return sum_cost

#----- ----- ----- ----- ----- ----- ----- ----- ----- -----

if __name__ == '__main__': #배운것1: 메인지정
    from sys import stdin  #배운것2: 라이브러리/모듈을 중간에도 가능
    from sys import setrecursionlimit

    input = stdin.readline #배운것3: 함수이름변경, 단 함수형프로그래밍x
    setrecursionlimit(10**5) #재귀한계 올리기

    n = int(input()) #입력받기
    edges = []

    for i in range(n):
        row_list = list(map(int, input().split()))  # 간선입력 인접행렬 형태로 받기
        for j in range(n):
            edges.append([i, j, row_list[j]])
    edges.sort(key=lambda x: x[2]) #가중치기준 오름차순 정렬, heapq가 아닌 이유는 중간삽입없이 1번만 sort하면 되기때문 so 이래서 Prim대신 Kruskal, 게다가 Kruskal은 2마을 문제에도 딱맞

    print(kruskal(n, edges) if True else 0) #특수케이스 처리