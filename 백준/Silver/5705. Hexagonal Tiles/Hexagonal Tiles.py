while (n := int(input())) != 0: 
    prev, current = 0, 1
    for _ in range(n):
        prev, current = current, prev+current
    print(current)