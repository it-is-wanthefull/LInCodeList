function solution(A,B){
    var answer = 0;
    
    A.sort((a, b) => b - a); // JS의 내림차순 정렬법: 2개씩 비교정렬하며 부등호'>' 대신 'b-a'의 음수여부를 통해 크기를 비교한다.
    B.sort((a, b) => a - b); // B.sort()는 오름차순은 맞으나 문자열식 오름차순이라 부적합, 예를들어 11이 2보다 작다고 판정된다.
    
    for (let i=0; i<A.length; i++) {
        answer += A[i] * B[i]
    }

    return answer;
}