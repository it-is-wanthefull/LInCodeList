def solution(n, computers):
    network = 0
    visited = [0] * n
    schedule = [0]
    
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