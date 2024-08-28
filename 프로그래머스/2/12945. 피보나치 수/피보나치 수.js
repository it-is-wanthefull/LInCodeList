function solution(n) {
    [a, b] = [0, 1];
    while (--n)
        [a, b] = [b, (a+b)%1234567];
    return b;
}