def solution(words):
    words.sort()
    words.append('')
    answer = 0
    prev = cnt = 1
    
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        prev, cnt = cnt, 1
        
        for j in range(min(len(w1),len(w2))):
            if w1[j] != w2[j]:
                break
            cnt += 1
                
        answer += min(max(cnt, prev),len(w1))
        
    return answer