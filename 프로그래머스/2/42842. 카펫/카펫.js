function solution(brown, yellow) {
    function quadratic_formula(brown, yellow) {
        // brown = width*2 + height*2 - 4
        // yellow = (width-2) * (height-2) = wh - 2(w+h) + 4 = wh - brown
        
        // w + h = brown/2 + 2
        // w * h = brown + yellow
        
        // t^2 - (-1)(w+h)t + wh = t^2 - (-1)(brown/2+2) + (brown+yellow)
        
        a = 1
        b = - (brown/2 + 2)
        c = brown + yellow
        
        root_bb_4ac = Math.sqrt(Math.pow(b, 2) - 4*a*c)
        
        t1 = (-b + root_bb_4ac) / 2*a
        t2 = (-b - root_bb_4ac) / 2*a
        
        return [t1, t2]
    }
    return quadratic_formula(brown, yellow);
}