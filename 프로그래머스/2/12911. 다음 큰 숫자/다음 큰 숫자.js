function solution(n) {
    target = n.toString(2).replace(/0/g,'').length;
    
    do {
        current = (++n).toString(2).replace(/0/g,'').length;
    } while(current != target)
    
    return n
}