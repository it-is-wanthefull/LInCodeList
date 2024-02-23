if __name__ == '__main__':
    from sys import stdin
    from collections import deque, Counter

    input = stdin.readline
    n, k = map(int, input().split())
    q = deque(map(int, input().split())) #q크기 = 2n
    robot = deque() #로봇위치가 저장된다, 로봇퇴장이 존재하고 순서는 바뀔일이 없기에 q사용

    time_cnt = 1 #1부터 시작
    while True:
        #step1: 회전, 내구도와 무관
        q.rotate(1)
        for i in range(len(robot)):
            robot[i] += 1
        #print(time_cnt, "회전후", q, robot)

        #step2: 로봇이동, 내구도 및 앞로봇 조건
        for i in range(len(robot) - 1, -1, -1):
            pos = robot[i]
            if pos >= n-1:
                robot.pop()
            elif q[pos + 1] >= 1 and (i == len(robot)-1 or robot[i+1] != pos + 1):
                q[pos + 1] -= 1
                robot[i] = pos+1
        #print(time_cnt, "이동후", q, robot)

        #step3: 로봇올림, 내구도 조건
        if q[0] >= 1:
            q[0] -= 1
            robot.appendleft(0)
        #print(time_cnt, "올림후", q, robot)

        #step4: 내구도검사
        hp0_cnt = Counter(q)[0]
        if hp0_cnt >= k:
            break

        time_cnt += 1

    print(time_cnt)