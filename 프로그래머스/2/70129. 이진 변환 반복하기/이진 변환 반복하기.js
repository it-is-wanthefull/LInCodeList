function solution(s) {
    for (answer=[0,0]; s>1; answer[0]++) {
        b = s.toString(2);      // JS식 2진법 변형법이다.
        r = b.replace(/0/g,''); // JS에선 replace가 전부교체하게 작동시키려면 '/g'를 달아야한다.
        s = r.length;
        answer[1] += b.length - r.length;
    }
    return answer;
}