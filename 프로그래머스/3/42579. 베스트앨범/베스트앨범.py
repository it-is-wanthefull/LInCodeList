from collections import defaultdict

def solution(genres, plays):
    answer = []
    dic_sum  = defaultdict(int)
    dic_each = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        dic_sum[g]  += p
        dic_each[g].append([p, i])
        
    for g, g_sum in sorted(list(dic_sum.items()), key=lambda x: -x[1]): # 장르 별 총 재생횟수 기준 내림차순 정렬
        lst = sorted(dic_each[g], key=lambda x: (-x[0], x[1])) # 장르 내 각 재생횟수 높은순 -> 고유번호 낮은순 기준 정렬
        answer.append(lst[0][1])
        if len(lst) > 1: # 장르 내 1곡만 있는 특수케이스 처리
            answer.append(lst[1][1])
        
    return answer