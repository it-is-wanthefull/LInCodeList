# from collections import Counter

# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
    
#     value_count_list = sorted(Counter(food_times).items()) +[(100000001,0)]
#     prev_value, num_rotate, num_remain = 0, 0, len(food_times)
    
#     for value, count in value_count_list:
#         gap = min((full:=value-prev_value), (caculated:=int(k/num_remain)))
#         k -= num_remain*gap
#         num_rotate += gap
#         num_remain -= count
#         prev_value = value
        
#         if gap != full:
#             for index in range(len(food_times)):
#                 if food_times[index] > num_rotate:
#                     if (k:=k-1) < 0:
#                         return index+1
                    
# 2. (value,index) dict
# 3. (value,index) list
# 4. list.pop(0) 대신 list[next_index]





def solution(food_times, k):
    food_times_dic = {}
    food_times_list = []
    totalTime = 0

    for i in range(0, len(food_times)):
        food_times_list.append([i, food_times[i]])
        totalTime+=food_times[i]

    if totalTime <= k:
        return -1

    food_times_list = sorted(food_times_list, key=lambda x:x[1])

    delTime = food_times_list[0][1]*len(food_times_list)
    i=1
    # print k
    # print delTime
    while delTime < k:
        k-=delTime
        delTime = (food_times_list[i][1]-food_times_list[i-1][1])*(len(food_times_list)-i)
        # print k, delTime
        i+=1

    food_times_list = sorted(food_times_list[i-1:], key=lambda x:x[0])
    # print food_times_list
    # print k
    return food_times_list[k%len(food_times_list)][0]+1





# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#     def remain_dishes():
#         return len(food_times)-food_times.count(0)
    
#     while True:
#         d = k // remain_dishes()
#         r = k %  remain_dishes()

#         for index in range(len(food_times)):
#             if food_times[index] != 0:
#                 food_times[index] -= d
#                 if food_times[index] < 0:
#                     r += abs(food_times[index])
#                     food_times[index] = 0
#             k = r

#         if remain_dishes() > k:
#             for index in range(len(food_times)):
#                 if food_times[index] != 0:
#                     if (k:=k-1) < 0:
#                         return index+1