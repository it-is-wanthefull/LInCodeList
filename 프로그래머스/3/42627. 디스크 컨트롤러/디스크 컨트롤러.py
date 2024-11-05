import heapq

def solution(jobs):
    n = len(jobs)
    jobs.sort(reverse=True)         # pop()을 위해 후단이 최소값이 되도록 내림차순정렬
    end, current, total  = 0, 0, 0  # 각각 직전종료시간, 현재시간, 총소요시간
    hq = []                         # heapq(힙큐)
    
    while jobs or hq: # 둘 다 빌때까지, jobs(request기준정렬) -> heapq(cost기준정렬) 로 데이터 이동
        if not hq: # heapq가 비었을시 end(직전종료시간)을 최신jobs([-1])로 갱신함
            end = max(end, request := jobs[-1][0])
        while jobs and jobs[-1][0] <= end: # 요청시간이 직전종료시간보다 이전이되버린 job들을 heapq에 새로 추가
            request, cost = jobs.pop()
            heapq.heappush(hq, [cost, request]) # heapq는 cost기준으로 정렬해야하기에 cost를 1번째요소로
        cost, request = heapq.heappop(hq)
        current = max(end, request)
        total += current - request + cost
        end = current + cost
            
    return total // n