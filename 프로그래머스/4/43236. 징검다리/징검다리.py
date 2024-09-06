def solution(distance, rocks, n):
    left, right = (START:=0), (END:=distance)
    rocks.sort()
    rocks.append(END)
    
    while left <= right:
        mid = (left + right) // 2
        expected = mid
        cnt = 0
        
        for r in rocks:
            if    r   >= expected:  expected = r + mid
            elif  r   <  expected:  cnt += 1
            if    cnt >  n       :  break
                
        if   cnt >  n:  right = mid - 1
        elif cnt <= n:  left  = mid + 1
        
    return right