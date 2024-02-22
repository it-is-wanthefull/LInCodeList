def Solution():
    my_dict = {}
    my_list = []

    for _ in range(int(input())):
        my_list.append(input())
    my_list.sort()

    for str in my_list:
        for i in range(len(str)):
            if str[:i] in my_dict:
                return False
        my_dict[str] = str
    return True

if __name__ == '__main__':
    for _ in range(int(input())):
        if Solution():
            print("YES")
        else:
            print("NO")