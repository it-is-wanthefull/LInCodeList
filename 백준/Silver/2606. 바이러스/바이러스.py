import collections

n_pc = int(input())
n_connect = int(input())
dict = collections.defaultdict(list)
stack = [1] #무조건 pc1부터 시작이라
cnt = -1 #pc1 본인은 cnt에서 제외됨

if n_pc == 1:
    cnt = 0

for _ in range(n_connect):
    v1, v2 = input().split()
    dict[v1].append(v2)
    dict[v2].append(v1) #biDirect Graph로

while stack:
    target = stack.pop()
    if str(target) in dict:
        adjacent = dict.pop(str(target), [])
        stack.extend(adjacent) #target과 연결된 점들을 모두 넣음
        cnt += 1

print(cnt)