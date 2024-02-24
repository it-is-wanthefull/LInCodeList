import sys

def possible(lan_length, lan_list, k):
    cnt = sum(lan // lan_length for lan in lan_list)
    return cnt >= k

def binary_search(lan_list, k, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if possible(mid, lan_list, k):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

def main():
    k, n = map(int, sys.stdin.readline().split())
    lan_list = [int(sys.stdin.readline()) for _ in range(k)]
    max_length = max(lan_list)
    answer = binary_search(lan_list, n, 1, max_length)
    print(answer)

if __name__ == "__main__":
    main()