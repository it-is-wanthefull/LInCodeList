function solution(brown, yellow) {
    function quadratic_formula(a, b) {
        root_bb_4ac = Math.sqrt(Math.pow(a/2 -2, 2) - 4*b)
        t1 = (a/2 -2 + root_bb_4ac) /2
        t2 = (a/2 -2 - root_bb_4ac) /2
        return [t1+2, t2+2]
    }
    return quadratic_formula(brown, yellow);
}