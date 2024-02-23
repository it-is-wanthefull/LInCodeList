N = int(input())
A_list = [int(num) for num in input().split()]
A_list.sort()

M = int(input())
B_list = [int(num) for num in input().split()]

for b in B_list:
    if b in A_list:
        print(1)
    else:
        print(0)