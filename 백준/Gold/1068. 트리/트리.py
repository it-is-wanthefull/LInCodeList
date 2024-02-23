def remove_branch(target, dict):
    for child in dict[target]:
        remove_branch(child, dict)
    dict.pop(target)

#----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

import collections, sys

N = int(input())
parent = list(map(int, sys.stdin.readline().split())) #parent가 적힌 list
dict = collections.defaultdict(list)                  #child가 적힌 dict
cnt = 0

for child in range(N):
    dict[parent[child]].append(child)
    dict[child].append(None)

target = int(input())
remove_branch(target, dict)         #해당node계열 branch전부 삭제
dict[parent[target]].remove(target) #해당node를 dict에서도 삭제

for key in dict.keys():
    if dict[key] == [None]: #child기록문서인 dict에서 child가 없다는뜻
        cnt += 1

print(cnt)