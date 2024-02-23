meet_list = [list(map(int, input().split())) for _ in range(int(input()))]
meet_list.sort(key=lambda x: (x[1], x[0]))

current, answer = 0, 0
for start, end in meet_list:
    if current <= start:
        current = end
        answer += 1

print(answer)