# 내 풀이
def solution(n, computers):
    network = 0
    visited = [0] * n
    schedule = []
    
    for node in range(n):
        if visited[node] == 1:
            continue
        schedule.append(node)
        
        while schedule:
            node = schedule.pop()
            visited[node] = 1

            for edge in range(n):
                if visited[edge] == 1:
                    continue
                if computers[node][edge] == 1:
                    schedule.append(edge)
                    
        network += 1
        
    return network





# 베스트채택된 다른사람 풀이
# def solution(n, computers):
#     answer = 0
#     visited = [0 for i in range(n)]
#     def dfs(computers, visited, start):
#         stack = [start]
#         while stack:
#             j = stack.pop()
#             if visited[j] == 0:
#                 visited[j] = 1
#             # for i in range(len(computers)-1, -1, -1):
#             for i in range(0, len(computers)):
#                 if computers[j][i] ==1 and visited[i] == 0:
#                     stack.append(i)
#     i=0
#     while 0 in visited:
#         if visited[i] ==0:
#             dfs(computers, visited, i)
#             answer +=1
#         i+=1
#     return answer





# 간결한 다른사람 풀이
# def solution(n, computers):
#     temp = []
#     for i in range(n):
#         temp.append(i)
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j]:
#                 for k in range(n):
#                     if temp[k] == temp[i]:
#                         temp[k] = temp[j]
#     return len(set(temp))