def solution(cookie):
    def is_in_index(l,r):
        if 0<=l and r<n:
            return True
        return False
        
    all_box = n = len(cookie)
    max_box = 0
    
    for i in range(n-1):
        l, r = i, i+1
        l_sum, r_sum = cookie[l], cookie[r]
        
        while is_in_index(l,r):
            if l_sum == r_sum:
                max_box = max(max_box, l_sum)
                if is_in_index((l:=l-1),(r:=r+1)):
                    l_sum += cookie[l]
                    r_sum += cookie[r]
            elif l_sum < r_sum:
                if is_in_index((l:=l-1),r):
                    l_sum += cookie[l]
            elif l_sum > r_sum:
                if is_in_index(l,(r:=r+1)):
                    r_sum += cookie[r]
                    
    return max_box