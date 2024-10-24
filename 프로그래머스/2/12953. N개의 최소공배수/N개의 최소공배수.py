def solution(arr):
    answer = 1
    
    # 중복제거, 내림차순 정렬
    arr = sorted(list(set(arr)), reverse=True)
    
    # 각각 q=나누는수, d=몫, r=나머지
    q, r, d = 2, -1, -1
    
    # 제곱근까지만 나눠볼 예정
    while q <= 100:#int(arr[0]**0.5):
        is_divised = 0
        
        # 배열의 각 수를 q로 나눠봄 (q는 2부터 시작)
        for i in range(len(arr)):
            r = arr[i] % q
            d = arr[i] / q
            if r == 0:
                arr[i] = d
                is_divised = 1
        
        # 배열의 어떤 수 1개라도 나눠졌는지 확인 후, 답에 곱하기
        if is_divised == 1:     answer *= q
        else:                   q += 1
        
        # 이미 다 나눠져버린 수는 배열에서 제거해놓기
        while len(arr) and arr[-1] == 1:
            arr.pop()
        
        # 배열이 모두 나눠져 비워진 경우 반복종료
        if len(arr) == 0:
            break
    
    # 소수여서 남겨진 경우 등을 처리
    for a in arr:
        answer *= a
    
    return answer