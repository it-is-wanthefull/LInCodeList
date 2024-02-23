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

            count_db = new int[N+2][2];
            for(int j=0; j<=N; j++) {
                count_db[j][0] = -1; count_db[j][1] = -1;
            }
            count_db[0][0] = 1; count_db[0][1] = 0;
            count_db[1][0] = 0; count_db[1][1] = 1;

            fib(N);
            bw.write(count_db[N][0] +" "+ count_db[N][1] +"\n");
        }
        bw.close();
    }

    public static int[][] count_db;
    public static void fib(int n) {
        if (n-2 < 0) return;
        if (count_db[n][0] == -1) {
            fib(n-1); fib(n-2);
            count_db[n][0] = count_db[n-1][0] + count_db[n-2][0];
            count_db[n][1] = count_db[n-1][1] + count_db[n-2][1];
        }
    }
}