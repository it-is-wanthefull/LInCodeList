def after_one_second(h1, m1, s1): 
    count = 0
    
    # 시침/분침/초침이 1바퀴 도는 '각(angle) 속도' 비율
    h1 %= 43200
    m1 %= 43200
    s1 %= 43200
    h2 = h1 + 1
    m2 = m1 + 12
    s2 = s1 + 720
    
    # 원리: 추월하게 되면 둘 중 한 쪽은 음수가 되며, 곱도 음수가 된다
    # 주의: 시침=분침은 세는게 아니었따...
    
    # 시침=초침 횟수 계산
    if (h1-s1) * (h2-s2) < 0 or (h2-s2) == 0:
        count += 1
    # 분침=초침 횟수 계산
    if (m1-s1) * (m2-s2) < 0 or (m2-s2) == 0:
        count += 1
        
    return count, h2, m2, s2

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

def solution(h1, m1, s1, h2, m2, s2):
    
    answer =0
    
    # 시작시각/지날시간을 초단위로 환산
    started_time =  h1    *3600 +  m1    *60 +  s1
    elapsed_time = (h2-h1)*3600 + (m2-m1)*60 + (s2-s1)
    
    # 시침/분침/초침이 1바퀴 도는 '각(angle) 속도'가 각각 1:12:720 임을 고려 현재 각을 계산
    h = (started_time      ) % 43200
    m = (started_time * 12 ) % 43200
    s = (started_time * 720) % 43200
    
    # 특수케이스: 시작시각에 이미 겹쳐있었는지를 확인
    if h == m or h == s or m == s:
        answer += 1
    
    # 특수케이스: 시침=분침=초침 횟수 계산: 정오/자정만 모두 겹칠 수 있음
    if [h1, m1, s1] == [0, 0, 0]:
        answer -= 0
    if [h1, m1, s1] < [12, 0, 0] <= [h2, m2, s2]:
        answer -= 1
    
    # 1초 후 추월여부로 겹쳤는지를 확인
    for i in range(elapsed_time):
        count, h, m, s = after_one_second(h, m, s)
        answer += count
    
    return answer