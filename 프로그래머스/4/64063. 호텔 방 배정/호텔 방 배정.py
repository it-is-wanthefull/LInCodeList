# 시도1: Dict로 인덱싱은 빠르지만, 충돌이 빈번해지면 빈방탐색으로인해 결국 List와 차이없음
def solution(k, room_number):
    answer = []
    dic = dict()
    
    for n in room_number:
        while n in dic:
            n += 1
        dic[n]=n
        answer.append(n)
        
    return answer





# 시도2: 범위로 기억, 범위기억은 순차탐색이 필요하여 Dict로는 불가 
def solution(k, room_number):
    answer = []
    lst = [ [-1,-1], [9999999999999,9999999999999] ]
    min_, max_ = 0, 1
    
    for n in room_number:
        for i in range(len(lst)):
            if lst[i][max_]+1 < n < lst[i+1][min_]-1:
                lst.insert(i+1, [n,n]) # insert
                answer.append(n)
                break
            elif lst[i][min_] <= n <= lst[i][max_]+1:
                lst[i][max_] += 1 # fix range
                answer.append(lst[i][max_])
                if lst[i][max_] == lst[i+1][min_]-1: # merge
                    lst[i][max_] = lst[i+1][max_]
                    lst.pop(i+1)
                break
            elif n == lst[i+1][min_]-1:
                lst[i+1][min_] -= 1 # fix range
                answer.append(lst[i+1][min_])
                break
        
    return answer





# 시도3: 충돌이 적을경우 Dict가, 많을경우 범위저장형 List가 적합함, 장점 조합시도, but 결국은 둘다 저장/탐색해야해서 장점조합이 아니라 단점조합이 되버림
# 시도4: N-Tree, 문제는 List와 Value(int)라는 서로다른타입을 담는게 불가능
# 시도5: 자료구조는 풀이2처럼 범위List로하고, 풀이4의 Tree는 자료구조가 아니라 탐색알고리즘응로하여, List탐색을 2진탐색으로 한다면?
def solution(k, room_number):
    answer = []
    min_, max_, inf = 0, 1, 9999999999999
    lst = [ [-inf,-inf], [inf,inf] ] # 예시: [[-inf~-inf], [1~4], [6~6], [9~17], ..., [inf,inf]], 충돌시 범위에 넣음
    
    def bin_search(lst, lst_range, n):
        start, end = lst_range
        mid = (start + end) // 2
        length = end - start + 1
        
        if length <= 1: # 길이가 0~1 이면 return
            return mid
        
        if lst[mid][min_]-1 <= n <= lst[mid][max_]+1: # 범위 안쪽값이면 return
            return mid
        elif n < lst[mid][min_]-1: # 범위 좌측값이면 recursive
            return bin_search(lst, [start,mid-1], n)
        elif lst[mid][max_]+1 < n: # 범위 우측값이면 recursive
            return bin_search(lst, [mid+1,end], n)
    
    for n in room_number:
        i = bin_search(lst, [0,len(lst)-1], n)
        
        if n < lst[i][min_]-1: # 범위 좌측값이면 좌측에 insert
            lst.insert(i, [n,n])
            answer.append(n)
        elif lst[i][max_]+1 < n: # 범위 우측값이면 우측에 insert
            lst.insert(i+1, [n,n])
            answer.append(n)
        elif lst[i][min_] <= n <= lst[i][max_]+1: # 범위 안쪽값이면 우측경계값 plus
            lst[i][max_] += 1
            answer.append(lst[i][max_])
            if lst[i][max_] == lst[i+1][min_]-1: # 이후 두개의 범위가 맞닿아지면 merge
                lst[i][max_] = lst[i+1][max_]
                lst.pop(i+1)
        elif n == lst[i][min_]-1: # 범위 좌경계이면 좌측경계값 minus
            lst[i][min_] -= 1
            answer.append(lst[i][min_])
            if lst[i-1][max_] == lst[i][min_]-1: # 이후 두개의 범위가 맞닿아지면 merge
                lst[i-1][max_] = lst[i][max_]
                lst.pop(i)
        
    return answer





# 시도6: 시간단축이 많이됐으나 시간초과가 1개 잔존, List.pop()때문인듯, so List->LinkedList로 개선시도, 하려했는데 Linked는 인덱싱이 안되니 2진탐색을할수없음
# 시도7: Dict.items()의 시간/공간복잡도가 O(n)이 아니라 O(1)이라해서 Dict로도 시도, but 인덱싱을 할 수 없고 그래서 2진탐색도 불가
# 시도8: Dict에 넣되 Dict의 key를 heapq에 넣음으로써 hash/index 모두 조합? but 단점도 조합됨
# 시도9: Dict에 넣되 Dict의 key를 2진Tree에 넣기? but cash충돌 케이스 자체가 Tree로는 평향Tree가 될 가능성이 높아 탐색효율 높지않음
# 시도10: 시도1에서 UnionFind방식을 차용하여 Dict를 운용, 공간을 다소소비하는 대신 pop않고 이정표를 일괄갱신
def solution(k, room_number):
    answer = []
    dic = dict()
    
    for n in room_number:
        visited = [n] # 방문노트
        
        while n in dic:
            n = dic[n] # 방에 기록된 이정표만큼 건너뛰기형 탐색
            visited.append(n) # 방문할 방 저장
            
        for v in visited: # 방문한 방의 이정표 업데이트
            dic[v] = n + 1
            
        answer.append(n)
        
    return answer