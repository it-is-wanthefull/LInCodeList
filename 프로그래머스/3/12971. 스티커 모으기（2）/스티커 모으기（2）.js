function solution(sticker) {
    if (sticker.length <= 3)
        return Math.max(... sticker);
    
    s1 = sticker.slice(0,sticker.length-1);
    s2 = sticker.slice(1,sticker.length-0);
    s1[2] += s1[0];
    s2[2] += s2[0];
    
    for (i=3; i<s1.length; i++) {
        s1[i] += Math.max(s1[i-2], s1[i-3]);
        s2[i] += Math.max(s2[i-2], s2[i-3]);
    }

    return Math.max(s1[s1.length-1], s1[s1.length-2], s2[s2.length-1], s2[s2.length-2]);
}

/*  14  6   5   11  3   9   2   10
    14  6   19  25  22  34  27  44
    
    14  6   5   11  3   9   2   x
    14  6   19  25  22  34  27  x
    
    x   6   5   11  3   9   2   10
    x   6   5   17  9   26  19  36
*/