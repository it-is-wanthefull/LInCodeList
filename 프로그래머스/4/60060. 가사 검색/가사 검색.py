# 내 풀이 2: 카운트(자식노드수)를 미리 입력해놓은 트리/역트리
# 장점: 해당 쿼리에 유사한 문자열이 많아도 카운트로 단번에 끝낼 수 있다
# 단점: 다만 카운트에 접근할때, 쿼리길이('?' 길이 제외)가 길면 트리를 깊게 들어가야해서 많은 시간 소요
def input_nested_dict(s, top_dic):
    if len(s) not in top_dic:
        top_dic[len(s)] = {'len_count': 0}
        
    current_dic = top_dic[len(s)]
    current_dic['len_count'] += 1

    for char in s: # 문자열의 각 문자를 차례대로 중첩된 딕셔너리로 만들어 나감
        current_dic = current_dic.setdefault(char, {'count': 0})
        current_dic['count'] += 1  # 자식노드수 카운트
    current_dic['value'] = s
    
    return top_dic

def find_nested_dict(s, top_dic):
    if len(s) not in top_dic:
        return 0  # 길이에 대한 딕셔너리가 없으면 0 반환
    
    current_dic = top_dic[len(s)]
    
    for char in s:
        if char == '?':
            break
        if char not in current_dic: # 문자가 없으면 0 반환
            return 0
        current_dic = current_dic[char]
        
    return current_dic.get('count', 0)

def solution(words, queries):
    answer = list()
    dic = dict()
    reversed_dic = dict() # '?'로 시작하는 쿼리 대비용
    
    for w in words: # 딕셔너리 입력 시작
        input_nested_dict(w, dic)
        input_nested_dict(w[::-1], reversed_dic)
            
    for q in queries: # 쿼리 판독 시작
        if   q[0]  == '?' == q[-1]: # '?'만으로 이뤄진 쿼리("?????"등)는 같은문자열길이 갯수를 저장한 len_count값 바로 반환
            answer.append(dic.get(len(q), {}).get('len_count', 0))
        elif q[-1] == '?':
            answer.append(find_nested_dict(q, dic))
        elif q[0]  == '?':
            answer.append(find_nested_dict(q[::-1], reversed_dic))
        
    return answer