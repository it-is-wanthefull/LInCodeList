# def solution(operations):
#     my_list = []
    
#     for command in operations:
#         command1, command2 = command.split(' ')
        
#         if command1 == 'I':
#             my_list.append(int(command2))
#         if command1 == 'D' and my_list:
#             my_list.sort()
#             if command2 == '1':
#                 my_list.pop()
#             if command2 == '-1':
#                 my_list.pop(0)
                
#     my_list.sort()
#     if len(my_list) == 0:
#         my_list.append(0)
#     return [my_list[-1], my_list[0]]

import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]