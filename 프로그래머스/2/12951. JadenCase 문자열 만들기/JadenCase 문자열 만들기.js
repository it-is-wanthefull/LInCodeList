function solution(s) {
    let arr = s.split(' '); // 문자열을 배열로 변환 (JS에서 문자열은 배열이 아님)
    
    arr = arr.map(word => 
        word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
    );
    
    return arr.join(' ');
}