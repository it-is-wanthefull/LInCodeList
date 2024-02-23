import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int t = Integer.parseInt(st.nextToken());
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int answer = 1;

            if (a < b) { int swap = a; a = b; b = swap; } // a>b이도록 swap
            
            int ta = a, tb = b;
            while (ta % tb != 0) { int r = ta % tb; ta = tb; tb = r; } // 유클리드 호제법
            
            int gcd = tb;
            int lcm = a / gcd * b / gcd * gcd;

            bw.write(lcm+"\n");
        }
        bw.close();
    }
}