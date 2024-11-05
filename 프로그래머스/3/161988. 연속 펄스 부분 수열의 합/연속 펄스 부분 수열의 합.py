from collections import deque

# 서브함수: 3개의 수 중 가운데 수'b'의 절대값'abs()'이 가장작은경우 True 반환
def is_mid_small(a, b, c):
    if abs(a) >= abs(b) <= abs(c):  return True
    else:                           return False

# 메인함수
def solution(sequence):
    # 1) 홀수때 -1 펄스 반영한 버전을 세팅 (짝수는 단순 반전일뿐) = O(n)
    s2 = deque([])
    for i in range(len(sequence)):
        if i % 2 == 1:             s2.append( -sequence[i] ) # 짝수때 -1펄스
        else:                      s2.append(  sequence[i] ) # 홀수때 +1펄스
    
    # 2) 음수/양수끼리 묶어 합 = O(n)
    s3 = deque([s2.popleft()])
    while len(s2)>=1:
        if s3[-1] * s2[0] >= 0:    s3[-1] +=  s2.popleft()   # 부호가 같으면
        else:                      s3.append( s2.popleft() ) # 부호가 다르면
    
    # 3) 연속한3개의 수 중 가운데 수의 절대값이 가장작은경우 추가 묶기 반복 = O(n)
    s4 = deque([s3.popleft()])
    while len(s3)>=1:
        if    len(s3)>=2 and is_mid_small(s4[-1], s3[ 0], s3[ 1]):
            s4.append(s4.pop()     + s3.popleft() + s3.popleft())
        else:
            s4.append(s3.popleft())
        while len(s4)>=3 and is_mid_small(s4[-3], s4[-2], s4[-1]):
            s4.append(s4.pop()     + s4.pop()     + s4.pop()    )
    
    return max(max(s4), -min(s4)) # '-min'은 반전버전을 고려한 것





def solution(sequence):
    v = [0]
    for i,s in enumerate(sequence): v.append(v[-1] + s * [1,-1][i%2])
    return max(v) - min(v)