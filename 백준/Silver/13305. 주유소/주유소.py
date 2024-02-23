n = int(input())
roadkm_list = list(map(int, input().split()))
oilcost_list = list(map(int, input().split()))
min = oilcost_list[0]
answer = 0

for i in range(n):
    if  min > oilcost_list[i]:
        min = oilcost_list[i]
    else:
        oilcost_list[i] = min

for i in range(n-1):
    answer += oilcost_list[i] * roadkm_list[i]

print(answer)