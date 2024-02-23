def dfs_stack(matrix):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows = len(matrix)
    cols = len(matrix[0])
    cnt_group = [] #모든 단지의 카운트 리스트

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == '0':
                continue

            #if matrix[][] == '1':
            matrix[row][col] = '0' #맵에 탐색완료 표시
            stack = [(row, col)]   #주변탐색 예정
            cnt_each = 1           #각 단지별 카운트

            while stack:
                x, y = stack.pop()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or matrix[nx][ny] == '0':
                        continue
                    #if matrix[][] == '1':
                    matrix[nx][ny] = '0'
                    stack.append((nx, ny))
                    cnt_each += 1

            cnt_group.append(cnt_each)

    return cnt_group





def dfs_recursive(matrix):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows = len(matrix)
    cols = len(matrix[0])
    cnt_group = []

    def dfs(r, c):
        cnt_each = 0
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] == '0':
            return

        # 방문처리
        matrix[r][c] = '0'
        cnt_each += 1
        for i in range(4):
            cnt_each += dfs(r + dx[i], c + dy[i])
        return cnt_each

    for r in range(rows):
        for c in range(cols):
            node = matrix[r][c]
            if node != '1':
                continue

            cnt_each = dfs(r, c)
            cnt_group.append(cnt_each)

    return cnt_group





N = int(input())
matrix = []

for _ in range(N):
    row = list(input())
    matrix.append(row)

answer_stack = sorted(dfs_stack(matrix))
answer_recursive = sorted(dfs_recursive(matrix))
answer = answer_stack

print(len(answer))
for e in answer:
    print(e)