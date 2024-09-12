# 내 풀이 1: 1) land를 같은층수끼리 Counter로 압축, 2) 적정층수 예측, 3) 2진탐색으로 오차 조정

from collections import Counter
from math import ceil, log2

def solution(land, P, Q):
    def cost(cur_floor): # 해당층으로 평탄화 할때 비용 계산
        sum_ = 0
        for floor, num in dic.items():
            diff = floor - cur_floor
            if diff < 0:    sum_ -= diff * num * P
            else:           sum_ += diff * num * Q
        return sum_
    
    dic = Counter(f for l in land for f in l)                   # land를 같은층수끼리 묶은 딕셔너리 (key=층,value=같은층블럭수)
    TOTAL_BLOCK = sum(f*n for f,n in dic.items())               # 전체 블럭수
    FLOOR_BLOCK = len(land) ** 2                                # 밑면 면적
    cur_floor = ESTIMATE_FLOOR = TOTAL_BLOCK // FLOOR_BLOCK     # 적정층수 예측
    min_ = ESTIMATE_FLOOR_COST = cost(ESTIMATE_FLOOR)           # 적정층수의 비용 계산
    MAX_FLOOR = max(max(dic),2)                                 # 최고층탐색, 단 0~1층인 경우 2층으로 산정
    bin_ = 2 ** ceil(log2(MAX_FLOOR))                           # 최고층보다는 큰 2의제곱수를 계산, 2진탐색을 위함
    
    while (bin_:=bin_//2) != 0:                                 # 2진탐색으로 오차 조정
        up, down = cost(cur_floor +bin_), cost(cur_floor -bin_)
        if   up   < min_:     min_ = up;       cur_floor += bin_
        elif down < min_:     min_ = down;     cur_floor -= bin_
    
    return min_





# 내 풀이 2: 풀이1은 중복제거된 key수 (max90000) * 이진탐색 횟수 (max30), 이번건 수학적 변곡점활용으로 key수 번에 끝내기
# 풀고나서 알게된 점: cost 그래프는 2차함수처럼 단 1번의 휘어짐만 있는게 아니었음

from collections import Counter

def solution(land, P, Q):
    def cost(cur_height): # 해당층으로 평탄화 할때 비용 계산
        total_cost = 0
        for height, count in heights:
            diff = height - cur_height
            if diff < 0:    total_cost -= diff * count * P
            else:           total_cost += diff * count * Q
        return total_cost
    
    heights = sorted(Counter(h for l in land for h in l).items()) # 높이별 카운트한 후 (높이, 해당높이인 블럭수)쌍의 리스트로 저장
    down, up = 0, (BLOCK_PER_FLOOR := len(land) ** 2)
    min_cost = current_cost = cost(prev_height:=0)
    
    for cur_height, count in heights:
        diff = cur_height - prev_height
        current_cost += down*diff*P - up*diff*Q
        min_cost = min(min_cost, current_cost)
        
        prev_height = cur_height
        down += count
        up   -= count
    
    return min_cost





# 다른사람 풀이: 비례식으로 답을 1번에 계산, but 그 1번에 계산이 좀 무거움

def solution(land, P, Q):
    answer = 0
    linear_land = sum(land, [])
    linear_land.sort()
    N_square = len(land)**2
    max_count = int((N_square*Q)/(Q+P))
    small = linear_land[:max_count]
    big = linear_land[max_count:]
    mid = linear_land[max_count]
    answer += ((mid*len(small) - sum(small))) * P
    answer += (sum(big) - (mid*len(big))) * Q

    return answer