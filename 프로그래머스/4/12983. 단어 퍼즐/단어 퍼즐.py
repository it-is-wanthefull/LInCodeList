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





# # 베스트채택된 다른사람 풀이: 다이나믹프로그래밍 with 자료구조Set
# # 설명: 거의다 똑같은데 strs를 list->set 으로 바꾼후 list.startswith(s)->'s in strs(set상태)' 를 하여 탐색속도를 -60%정도 줄였다.
# # 이유: 단 이건 퍼즐(strs)의 길이가 1~5 밖에 안됐기에 그랬을뿐
# # 장점: 퍼즐(strs) 수가 많아도 Set으로 시간절약 가능
# # 단점: 퍼즐(strs)의 길이 종류 수가 많아지면 그만큼 배로 느려짐
# # 비교: 내 코드는 O(n/알파벳종류수), 이 코드는 O(1*길이종류수), 즉 퍼즐 28개마다 길이종류수가 1개이상 늘어나면 더 느림
# def solution(strs, t):
#     n = len(t)
#     memo = [float("inf")] * (n + 1)
#     memo[0] = 0
#     sizes = set(len(s) for s in strs)
#     strs = set(strs)
#     for i in range(n + 1):
#         for size in sizes:
#             if i + size < n + 1 and t[i:i + size] in strs:
#                 memo[i + size] = min(memo[i + size], memo[i] + 1)
#     return memo[n] if memo[n] < float("inf") else -1