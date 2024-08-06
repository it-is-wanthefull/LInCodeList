def solution(triangle):
    for i in range(len(triangle) -1):
        triangle[i+1][0] += triangle[i][0]
        triangle[i+1][-1] += triangle[i][-1]
        
        for j in range(len(triangle[i+1]) -2):
            if triangle[i][j] > triangle[i][j+1]:
                triangle[i+1][j+1] += triangle[i][j]
            else: 
                triangle[i+1][j+1] += triangle[i][j+1]
                
    return max(triangle[-1])





# def solution(triangle):
#     for i in range(len(triangle) -1):
#         triangle[i+1][0] += triangle[i][0]
#         triangle[i+1][-1] += triangle[i][-1]
        
#         for j in range(len(triangle[i+1]) -2):
#             if triangle[i][j] > triangle[i][j+1]:
#                 triangle[i+1][j+1] += triangle[i][j]
#             else: 
#                 triangle[i+1][j+1] += triangle[i][j+1]
                
#     return max(triangle[-1])





# def solution(triangle):
#     for height in range(len(triangle),1,-1):
#         for j in range(height-1):
#             if triangle[height-1][j] > triangle[height-1][j+1]:
#                 triangle[height-2][j] += triangle[height-1][j]
#             else:
#                 triangle[height-2][j] += triangle[height-1][j+1]
        
#     return triangle[0][0]





# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])