my_list = []

for i in range(int(input())):
    age, name = map(str, input().split())
    my_list.append([int(age), i, name])

my_list.sort()

for e in my_list:
    print(e[0], e[2])