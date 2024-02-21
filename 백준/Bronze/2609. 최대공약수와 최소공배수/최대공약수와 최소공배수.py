a, b = map(int, input().split())
a2, b2 = a, b

while True:
    r = a2 % b2
    if r != 0:
        a2, b2 = b2, r
    else:
        print(b2)
        print(a*b//b2)
        break