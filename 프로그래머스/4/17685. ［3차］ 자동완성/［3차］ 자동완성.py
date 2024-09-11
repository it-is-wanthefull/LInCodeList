# # 내 풀이: 문자열.sort()가 트리식 정렬과 같음을 이해하고 활용
# def solution(words):
#     words.sort()
#     words.append('')
#     answer = 0
#     prev = cnt = 1
    
#     for i in range(len(words)-1):
#         w1, w2 = words[i], words[i+1]
#         prev, cnt = cnt, 1
        
#         for j in range(min(len(w1),len(w2))):
#             if w1[j] != w2[j]:
#                 break
#             cnt += 1
                
#         answer += min(max(cnt, prev),len(w1))
        
#     return answer





# # 다른사람 풀이 1: 링크드리스트형 트리
# class Trie():
#     def __init__(self):
#         self.next = dict()
#         self.value = 0

# def solution(words):
#     answer = 0
#     tree = Trie()
#     for word in words:
#         subtree = tree
#         for idx, val in enumerate(word):
#             subtree.value += 1
#             if val not in subtree.next:
#                 subtree.next[val] = Trie()
#             subtree = subtree.next[val]
#             if (idx == len(word) - 1):
#                 subtree.value += 1

#     for word in words:
#         subtree = tree
#         counts = 0
#         for idx, val in enumerate(word):
#             if (subtree.value == 1):
#                 answer += counts
#                 break
#             elif idx == len(word) - 1:
#                 answer += counts + 1
#                 break
#             else:
#                 subtree = subtree.next[val]
#                 counts += 1


#     return answer





# 다른사람 풀이 2: 딕셔너리형 트리
def solution(words):
    answer = 0

    root = {}
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict["_end_"] = None

    for word in words:
        current = root
        duplicated_pos = 0
        for i, letter in enumerate(word):
            current = current[letter]
            if len(current) > 1:
                duplicated_pos = i + 1

        if duplicated_pos == 0:
            answer += 1
        elif duplicated_pos < len(word):
            answer += duplicated_pos + 1
        elif duplicated_pos == len(word):
            answer += duplicated_pos

    return answer