push_max = int(input())
answer = []

my_stack = []
rest_target = push_max
target = int(input())
rest_target -= 1

for i in range(1, push_max + 1):
    my_stack.append(i)
    answer.append("+\n")

    while my_stack and my_stack[-1] == target:
        my_stack.pop()
        answer.append("-\n")
        
        if rest_target > 0:
            target = int(input())
            rest_target -= 1

if not my_stack:
    print("".join(answer))
else:
    print("NO")