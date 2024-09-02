function solution(n, stations, w) {
    stations.push(n+w+1);
    
    for (i=0,cur=1,tower=0; cur<=n; i++) { // 주의할점: 아파트는 0이아닌 1부터 존재함
        if (cur < stations[i]-w) {
            need_area = stations[i]-w-cur;
            tower += Math.ceil(need_area/(2*w+1));
        }
        cur = stations[i]+w+1;
    }
    
    return tower;
}