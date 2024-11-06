# 합산의 10%가 아니라 개별의 10%, 이게 차이점이 뭐냐면 소수점 절사가 오차를 냄, so 계산을 최하위노드부터 할필요가 없음
from collections import defaultdict
import math

def solution(enroll, referral, seller, amount):
    parent_dic  = dict()            # referral 로 바로먼저 만들어지는 데이터, 나중에 10%송금시 사용
    account_dic = defaultdict(int)  # 정산금액을 저장하기위해 사용
    result      = list()
    
    for e, r in zip(enroll, referral):
        parent_dic[e] = r
    
    for s, a in zip(seller, amount):
        recipient = s
        remnant = a * 100
        while remnant > 0:
            give = math.ceil(remnant * 0.9)
            remnant -= give
            account_dic[recipient] += give
            if recipient in parent_dic:
                recipient = parent_dic[recipient]
            else:
                break
    
    for e in enroll:
        result.append(account_dic[e])
    
    return result