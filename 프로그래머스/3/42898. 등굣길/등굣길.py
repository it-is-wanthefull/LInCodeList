# 내 풀이: q로 순회하며 down-top, 속도4배느린범인=(딕셔너리?o, 0값초기화?x .update함수?x, 큐?x, in[]?x, 조건문수?x, 접근수?o)
from collections import deque

def solution(m, n, puddles):
    START, WATER = (1,1), -1 # 상수값 선언: START는 시작점(집)의 좌표, WATER는 물웅덩이 위치에 저장될 값(-1)
    
    dic = {(r,c): 0 for c in range(m+1) for r in range(n+1)} # 딕셔너리 초기화, 이후 dic[(r,c)] = dp값(도달가능 경우의수)이 저장될 예정
    dic.update({(r,c): WATER for c,r in puddles}) # 물웅덩이 좌표에 WATER값(-1) 입력 (물웅덩이 좌표가 비일반적이게도 [c,r]꼴로 되어있음)
    
    dic[START] = 1 # 시작점(집) 좌표에 dp값 입력
    q = deque([START])
    recent = START # recent는 차후 q.append시 중복append 방지위한 최근append 저장하는 변수
    
    while q:
        r, c = q.popleft()
        curr, down, right = (r,c), (r+1,c), (r,c+1) # 문제조건에 좌향상향은 제거됨
        for next_ in [down, right]:
            if next_ in dic and dic[next_] != WATER:
                dic[next_] += dic[curr]
                if next_ != recent: # 중복append 방지, 'not in q'조건은 q를 전부 검사하게 되므로 시간매우낭비
                    recent = next_
                    q.append(next_)
                
    return dic[(n,m)] % 1000000007 # 문제에 숨겨진 비일반적인 조건





# 베스트채택된 다른사람 풀이: 순차계산이 가능하기에 q대신 그냥 2중반복문 쓰며 left-right
def solution(m, n, puddles):
    grid = [[0]*(m+1) for i in range(n+1)] #왼쪽, 위로 한줄씩 만들어서 IndexError 방지
    if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
        for a, b in puddles:
            grid[b][a] = -1                #미리 -1로 체크
    grid[1][1] = 1
    for j in range(1,n+1):
        for k in range(1,m+1):
            if j == k == 1:                #(1,1)은 1로 만들어두고, 0이 되지 않도록
                continue
            if grid[j][k] == -1:           #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
                grid[j][k] = 0
                continue
            grid[j][k] = (grid[j][k-1] + grid[j-1][k])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식

    return grid[n][m]





# 차선채택된 다른사람 풀이: 재귀로 top-down 역행계산
def solution(m, n, puddles):
    answer = 0
    info = dict([((2, 1), 1), ((1, 2), 1)])
    for puddle in puddles:
        info[tuple(puddle)] = 0

    def func(m, n):
        if m < 1 or n < 1:
            return 0
        if (m, n) in info:
            return info[(m, n)]
        return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
    return  func(m, n) % 1000000007





# 리팩토링한 내 풀이: 범인찾는중(딕셔너리?x, 0값초기화?x .update함수?x, 큐?x, in[]?x, 조건문수?x)
from collections import deque, defaultdict

def solution(m, n, puddles):
    START, WATER = (1,1), -1 # 상수값 선언: START는 시작점(집)의 좌표, WATER는 물웅덩이 위치에 저장될 값(-1)
    
    map_ = [[0]*(m+1) for i in range(n+1)]
    dic = defaultdict(int) # 딕셔너리 기본값 0으로 설정, 이후 dic[(r,c)] = dp값(도달가능 경우의수)이 저장될 예정
    dic.update({(r,c): WATER for c,r in puddles}) # 물웅덩이 좌표에 WATER값(-1) 입력 (물웅덩이 좌표가 비일반적이게도 [c,r]꼴로 되어있음)
    dic[START] = 1 # 시작점(집) 좌표에 dp값 입력
    
    for r in range(n+1):
        for c in range(m+1):
            for next_ in [down:=(r+1,c), right:=(r,c+1)]: # 문제조건에 좌향상향은 제거됨
                if dic[next_] != WATER and dic[r,c] != WATER:
                    dic[next_] += dic[r,c]
    # for r in range(1, n+1):
    #     for c in range(1, m+1):
    #         print(dic, end=' ')
    #     print()
                    
    return dic[n,m] % 1000000007 # 문제에 숨겨진 비일반적인 조건