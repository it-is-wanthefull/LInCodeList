n, m = map(int, input().split())
lst = sorted(list(map(int, input().split()))) #정렬포함

m = sum(lst) - m

divide_n = 0
exceed = -1
pass_mem = 0

while exceed != 0:
    divide_n += (m // (n-pass_mem))
    m = m % (n-pass_mem)
    exceed = 0

    for i in range(pass_mem, n):
        if lst[i] <= divide_n:
            exceed += divide_n - lst[i]
        else:
            m += exceed
            pass_mem = i
            break

print(divide_n)