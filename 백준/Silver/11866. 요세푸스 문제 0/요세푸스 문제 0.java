import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader((new InputStreamReader(System.in)));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        boolean[] check = new boolean[N];  //체크할 배열
        Arrays.fill(check, true);
        int finder = 0;
        int count = 0;

        System.out.print("<");
        for(int i=1; i<=N; i++) {
            count = 0;
            while (count < K) {
                finder = ++finder % N;
                if (check[finder] == true)
                    count++;
                if (count == K)
                    check[finder] = false;
            }
            if (finder == 0) System.out.print(N);
            else System.out.print(finder);

            if (i != N) System.out.print(", ");
        }
        System.out.println(">");
    }
}