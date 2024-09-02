function solution(people, limit) {
    people.sort((a,b) => b-a);
    [len, half] = [people.length, limit/2];
    
    for (l=0,r=len-1,cnt=0; l<=r; l++,cnt++) { // 최대2명이기에 2포인터방법 가능
        if (people[l] <= half) { // 남은사람들이 전부 limit절반 이하라면 항상 2명씩 태울수 있기에 빠른계산
            cnt += Math.ceil((r-l+1)/2);
            break;
        }
        if (people[l] + people[r] <= limit)
            r--;
    }
    
    return cnt;
}