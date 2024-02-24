n = int(input())
lst = list(map(int, input().split()))
m = int(input())

lst.sort()
if sum(lst) <= m:
    print(max(lst))
else:
    total_divide = 0
    exceed = -1
    pass_mem = 0
    while exceed != 0:
        divide_n = m // (n-pass_mem)
        m = m % (n-pass_mem)
        total_divide += divide_n
        exceed = 0
        for i in range(pass_mem, n):
            if lst[i] <= total_divide:
                exceed += total_divide - lst[i]
            else:
                m += exceed
                pass_mem = i
                break
    print(total_divide)