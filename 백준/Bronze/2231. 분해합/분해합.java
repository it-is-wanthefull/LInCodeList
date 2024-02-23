import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int digit = 1;
        int answer = 0;

        while(n/(int)Math.pow(10,digit) != 0)
            digit++;


        for(int i=n-digit*9; i<=n; i++) { // n보다 작고 자릿수*9만큼만 탐색
            int temp = i;
            int sum = 0;
            for(int j=1; j<=digit; j++) {
                sum += temp % 10;
                temp /= 10;
            }
            sum += i;
            if(sum == n) { answer = i; break; }
        }
        bw.write(answer+"\n");
        bw.close();
    }
}