def expand_around_center(s, left, right):
    while 0 <= left <= right < len(s) and s[left] == s[right]:
        left  -= 1
        right += 1
    return right - left - 1

def solution(s):
    max_length = 0

    for i in range(len(s)):
        odd_length  = expand_around_center(s, i, i)    # 'aba' 와 같은 홀수형 팰린드롬
        even_length = expand_around_center(s, i, i+1)  # 'abba'와 같은 짝수형 팰린드롬
        max_length  = max(max_length, odd_length, even_length)

    return max_length