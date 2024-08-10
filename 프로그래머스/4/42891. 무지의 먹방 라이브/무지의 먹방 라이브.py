from collections import Counter

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    tuple_ = sorted(Counter(food_times).items()) +[(100000001,0)]
    num_nonzero = len(food_times)
    cut_line, prev_value = 0, 0
    
    for i in range(len(tuple_)):
        value, count = tuple_[i]
        low_limit, high_limit = 1, value - prev_value
        gap = min(high_limit, int(k/num_nonzero))
        
        if gap >= high_limit:
            cut_line += gap
            k -= num_nonzero*gap
            num_nonzero -= count
            prev_value = value
            
        elif gap >= low_limit:
            cut_line += gap
            k -= num_nonzero*gap
            
        else:
            for i in range(len(food_times)):
                if food_times[i] > cut_line:
                    k -= 1
                    if k < 0:
                        return i+1





# from collections import OrderedDict, defaultdict

# def solution(food_times, k):
#     # if sum(food_times) <= k:
#     #     return -1
    
#     food_sum = 0
#     food_dict = defaultdict(list)
#     count_dict = defaultdict(int)
    
#     for index in range(len(food_times)):
#         value = food_times[index]
#         food_sum += value
#         food_dict[value].append(index)
#         count_dict[value] += 1
    
#     if food_sum <= k:
#         return -1
    
#     food_dict = OrderedDict(sorted(food_dict.items()))
#     count_tuple = sorted(count_dict.items()) +[(100000001,0)]
    
#     num_nonzero = len(food_times)
#     cut_line, prev_value = 0, 0
    
#     while True:
#         value, count = count_tuple[0]
#         low_limit, high_limit = 1, value - prev_value
#         gap = min(high_limit, int(k/num_nonzero))
        
#         if gap >= high_limit:
#             k -= num_nonzero*gap
#             cut_line += gap
#             num_nonzero -= count
#             prev_value = value
#             count_tuple.pop(0)
#             food_dict.pop(value)
            
#         elif gap >= low_limit:
#             k -= num_nonzero*gap
#             cut_line += gap
            
#         else:
#             all_values = [value for sublist in food_dict.values() for value in sublist]
#             sorted_values = sorted(all_values)
#             return sorted_values[k]+1





# from collections import defaultdict
# def solution(food_times, k):
#     food_sum = 0
#     food_list = []
#     count_dict = defaultdict(int)
    
#     for index in range(len(food_times)):
#         value = food_times[index]
#         food_sum += value
#         food_list.append( (value, index) )
#         count_dict[value] += 1
    
#     if food_sum <= k:
#         return -1
    
#     food_list.sort()
#     count_tuple = sorted(count_dict.items()) +[(100000001,0)]
    
#     num_nonzero = len(food_times)
#     cut_line, prev_value = 0, 0
    
#     while True:
#         value, count = count_tuple[0]
#         low_limit, high_limit = 1, value - prev_value
#         gap = min(high_limit, int(k/num_nonzero))
        
#         if gap >= high_limit:
#             k -= num_nonzero*gap
#             cut_line += gap
#             num_nonzero -= count
#             prev_value = value
#             count_tuple.pop(0)
            
#         elif gap >= low_limit:
#             k -= num_nonzero*gap
#             cut_line += gap
            
#         else:
#             final = sorted(food_list[len(food_list)-num_nonzero:], key=lambda x: x[1])
#             return final[k][1]+1