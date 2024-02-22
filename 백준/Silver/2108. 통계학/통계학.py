my_list = []
cnt_list = []

n = int(input())
for i in range(n):
    my_list.append(int(input()))
my_list.sort()

my_set = set(my_list)
for e in my_set:
    cnt_list.append([my_list.count(e), e])
cnt_list.sort()

max_cnt = cnt_list[-1][0]
max_cnt_num = -1
if len(cnt_list) >= 2 and cnt_list[-2][0] == max_cnt:
    cnt = 0
    for i in range(len(cnt_list)):
        if cnt_list[i][0] == max_cnt:
            cnt += 1
        if cnt == 2:
            max_cnt_num = cnt_list[i][1]
            break
else:
    max_cnt_num = cnt_list[-1][1]

print(round(sum(my_list)/n))
print(my_list[(n-1)//2])
print(max_cnt_num)
print(my_list[-1]-my_list[0])