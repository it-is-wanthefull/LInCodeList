def dfs_stack(matrix, color):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows = len(matrix)
    cols = len(matrix[0])
    is_bomb = False

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == color:
                matrix[row][col] = '.'  #탐색완료 표시
                stack1 = [(row, col)]   #주변탐색 예정
                stack2 = [(row, col)]
                cnt_each = 1            #카운트

                while stack1:
                    x, y = stack1.pop() #;print(color, 'x', x, 'y', y)
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i] #;print(color, 'nx', nx, 'ny', ny, 'cnt', cnt_each)
                        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == color:
                            matrix[nx][ny] = '.' #;print(color, 'nx', nx, 'ny', ny, 'cnt', cnt_each, 'ifin')
                            stack1.append((nx, ny))
                            stack2.append((nx, ny))
                            cnt_each += 1

                if cnt_each < 4:
                    while stack2:
                        x, y = stack2.pop()
                        matrix[x][y] = color
                else:
                    is_bomb = True

    if is_bomb:
        return 1
    else:
        return 0

def gravity(pypy):
    for col in range(6):
        q = deque()
        for row in range(11, -1, -1):
            if pypy[row][col] != '.':
                q.append(pypy[row][col])
        for row in range(11, -1, -1):
            if q:
                pypy[row][col] = q.popleft()
            else:
                pypy[row][col] = '.'

def print_pypy(pypy):
    for i in range(12):
        for j in range(6):
            print(pypy[i][j], end=" ")
        print()
    print()

#----- ----- ----- ----- ----- ----- ----- ----- ----- -----

if __name__ == '__main__':
    from sys import stdin
    from collections import deque

    input = stdin.readline
    pypy = []
    color = ['R', 'G', 'B', 'P', 'Y']
    is_bomb = 0
    cnt_bomb = 0

    for i in range(12):
        row = list(map(str, input()))
        row.pop() #개행 제거
        pypy.append(row)

    while True:
        for c in color:
            is_bomb += dfs_stack(pypy, c)

        #print_pypy(pypy)
        gravity(pypy)
        #print_pypy(pypy)
        #print(is_bomb, cnt_bomb)

        if is_bomb == 0:
            break
        elif is_bomb >= 1:
            is_bomb = 0
            cnt_bomb += 1

    print(cnt_bomb)