def solution(friends, gifts):
    n = len(friends)
    give_take = [[0] * n for _ in range(n)]
    gift_score = [0] * n    # 이번 달 선물 지수
    gift_next = [0] * n     # 다음 달 선물 수량
    
    # 친구 이름을 인덱스로 매핑
    friend_idx = {name: idx for idx, name in enumerate(friends)}
    
    for g in gifts:
        a, b = g.split()
        a = friend_idx[a]
        b = friend_idx[b]
        give_take[a][b] += 1
        gift_score[a] += 1
        gift_score[b] -= 1
    
    for a in range(n):
        for b in range(n):
            if give_take[a][b] > give_take[b][a]:
                gift_next[a] += 1
            if give_take[a][b] == give_take[b][a]:
                if gift_score[a] > gift_score[b]:
                    gift_next[a] += 1
    
    return max(gift_next)