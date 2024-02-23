import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int T = Integer.parseInt(st.nextToken());

        for(int i=1; i<=T; i++) {
            st = new StringTokenizer(bf.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            
            dynamic_db = new int[N][M];   // Main클래스 전역변수
            for(int j=0; j<N; j++)        // 다이나믹DB배열 초기화(-1)
                for(int k=0; k<M; k++)
                    dynamic_db[j][k] = -1;
                    
            bw.write(countWay(N,M)+"\n"); // 경우의수계산함수 호출과 출력
        }
        bw.close();
    }

    public static int[][] dynamic_db;
    public static int countWay(int n, int m) {
        if(n==1) return m;
        if(m==1) return 1;
        if(dynamic_db[n-1][m-1] != -1) return dynamic_db[n-1][m-1];

        int count = 0;
        for(int i=m-1; i>=n-1; i--)
            count += countWay(n-1, i);
        return (dynamic_db[n-1][m-1] = count);
    }
}