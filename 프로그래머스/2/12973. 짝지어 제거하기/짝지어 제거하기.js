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
    // if (s.length % 2 == 1)
    //     return 0;
    
    stk = [];
    
    for (i of s) {
        if (stk[stk.length-1]!=i) // JS에선 stk이 중간에 비어 인덱스가 -1이 되면 false 처리 됨
            stk.push(i);
        else
            stk.pop();
    }
    
    return Number(stk.length==0);
}