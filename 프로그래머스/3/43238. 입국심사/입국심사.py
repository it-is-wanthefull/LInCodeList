def solution(n, times):
    start, end = 0, n*max(times)
    
    while True:
        mid = (start + end) // 2
        cnt = sum(mid//t for t in times)
            
        if   cnt <  n: start = mid+1
        elif cnt >  n: end   = mid-1
        elif cnt == n: return mid - min(mid%t for t in times)
        
        if   start > end: return end+1