from sys import stdin
input = stdin.readline

t = int(input())
for i in range(t):

    lst, lst_b = [], []
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        lst.append([a, b])
    lst.sort()

    min_a = lst[0]
    for i in range(n):
        #print(lst[i])
        if min_a[1] >= lst[i][1]:
            min_a[1] = lst[i][1]
        else:
            lst[i] = [-1, -1] #지금당장 제거는 곤란
    cnt = lst.count([-1, -1])
    #print(lst)
    print(n-cnt)