def on_off(switch_list, index):
    switch_list[index] = (switch_list[index]+1) %2
    #다른더좋은방법: switch_list[index] = 1 - switch_list[index]

#----- ----- ----- ----- ----- ----- ----- ----- ----- -----

if __name__ == '__main__':
    from sys import stdin
    input = stdin.readline

    n_switch = int(input())
    switch_list = list(map(int, input().split()))
    n_student = int(input())

    for i in range(n_student):
        gender, number = list(map(int, input().split()))
        if gender == 1: #남학생
            for j in range(number-1, n_switch, number): #number 배수단위로 액션
                on_off(switch_list, j)
        else: #여학생
            left = right = number = number-1 #number 배열방식으로 보정
            on_off(switch_list, number) #일단 해당number 액션
            while left != -1 and right != n_switch: #오버플로우 체크
                if switch_list[left] == switch_list[right]: #좌우 같다면 액션
                    on_off(switch_list, left)
                    on_off(switch_list, right)
                    left -= 1
                    right += 1
                else: #좌우 달라질때 액션반복 스톱
                    break

    for i in range(0, len(switch_list), 20): #20개씩 출력
        print(' '.join(map(str, switch_list[i:i + 20])))