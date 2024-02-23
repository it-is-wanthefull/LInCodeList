size = int(input())
list_1 = list(range(size, 0, -1))
list_2 = []
list_3 = []

while True:
    a, b = map(int, input().split())

    if a == 1:
        for _ in range(b):
            list_2.append(list_1.pop())
    else: #a == 2:
        for _ in range(b):
            list_3.append(list_2.pop())

    if len(list_3) == size:
        for _ in range(size):
            print(list_3.pop())
        break