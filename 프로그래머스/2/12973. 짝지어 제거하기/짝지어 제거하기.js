// // 내 풀이 1: 정규식으로 깔끔하게 작성, but replace가 매번 O(n)여서인듯 시간초과
// function solution(s) {
//     s2 = s
    
//     do {
//         [s, s2] = [s2, s2.replace(/(\w)\1/g,'')]
//     } while (s2.length != s.length);
    
//     return Number(s == '');
// }





// 내 풀이 2: '올바른 괄호' 유형의 문제를 떠올리고 stack을 이용하여 풀이
function solution(s) {
    stk = [];
    
    for (i=0; i<s.length; i++) {
        l = stk.length;
        if (l==0 || stk[l-1]!=s[i])
            stk.push(s[i]);
        else
            stk.pop();
    }
    
    if (stk.length==0)
        return 1;
    return 0;
}