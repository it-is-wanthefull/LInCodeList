# 내 풀이: 다이나믹프로그래밍
# 설명: index 0에서 len(t)까지 반복문, 각 index마다 해당 접두사로 시작하는 strs가 있는지 확인후 현재index + 매칭strs길이 만큼의 index에 조합카운트 저장 또는 값비교로 최소값 선택

from collections import defaultdict
def solution(strs, t):
    dic = defaultdict(list)
    dp = [0] + [20001] * (len(t))
    
    for s in strs:
        dic[s[0]].append(s)
        
    for i in range(len(t)):
        sliced = t[i:]
        for s in dic[sliced[0]]:
            if sliced.startswith(s):
                dp[i+len(s)] = min(dp[i+len(s)], dp[i]+1)
                
    return dp[-1] if dp[-1]!=20001 else -1