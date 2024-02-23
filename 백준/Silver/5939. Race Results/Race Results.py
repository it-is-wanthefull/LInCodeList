my_list = []

for _ in range(int(input())):
    my_list.append(list(map(int, input().split())))

my_list.sort()

for e in my_list:
    print(e[0], e[1], e[2])