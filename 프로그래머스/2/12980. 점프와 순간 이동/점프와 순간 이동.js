function solution(n) {
    ans = 0;
    
    for (; n; n/=2) {
        if (n%2 == 1) {
            n -= 1;
            ans++;
        }
    }
    
    return ans;
}