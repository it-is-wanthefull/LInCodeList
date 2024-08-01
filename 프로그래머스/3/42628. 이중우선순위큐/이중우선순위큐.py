import heapq

def solution(operations):
    my_list = []
    
    for command in operations:
        command1, command2 = command.split(' ')
        
        if command1 == 'I':
            my_list.append(int(command2))
            my_list.sort()
        if command1 == 'D' and my_list:
            if command2 == '1':
                my_list.pop()
            if command2 == '-1':
                my_list.pop(0)
                
    if len(my_list) == 0:
        my_list.append(0)
    return [my_list[-1], my_list[0]]

# 1. 2개의 heapq + 크기변수따로 -> O(nlogn)*2 / 문제점: 결국 삭제를 안하면 삭제됐어야하는 값들이 min/max에서 논리적오류 발생
# 2. list + sort -> O(nlogn)
# 3. list + min/max -> O(n**2)
# 3. 완전 새로운 모형?