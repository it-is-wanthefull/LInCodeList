def solution(n, words):
    dic = dict()
    prev = words[0][0]
    
    for i in range(len(words)):
        if words[i] in dic or words[i][0] != prev:
            return [(i%n)+1, int(i/n)+1]
        else:
            dic[words[i]] = 'ok'
            prev = words[i][-1]
        
    return [0, 0]