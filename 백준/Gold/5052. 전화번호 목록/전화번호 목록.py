def Solution():
    answer = True
    my_dict = {}
    my_list = []

    for _ in range(int(input())):
        my_list.append(input())
    my_list.sort()

    for str in my_list:
        for i in range(len(str)):
            if str[:i] in my_dict:
                #print(str)
                answer = False
        my_dict[str] = str
    return answer

if __name__ == '__main__':
    for _ in range(int(input())):
        if Solution():
            print("YES")
        else:
            print("NO")